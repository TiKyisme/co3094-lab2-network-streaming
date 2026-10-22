#!/usr/bin/env python3
"""Minimal authoritative DNS A responder for CO3094 Lab 2.

Uses only Python's standard library and runs on Python 2.7+ and Python 3.
The default answer is a documentation-only example address, not the real
public address for www.example.com.
"""

from __future__ import print_function

import argparse
import socket
import struct
import sys


DEFAULT_NAME = "www.example.com"
DEFAULT_DEMO_IP = "192.0.2.123"
TYPE_A = 1
CLASS_IN = 1


def decode_name(packet, start):
    labels = []
    cursor = start
    end = None
    visited = set()
    hops = 0

    while cursor < len(packet):
        length = packet[cursor]
        if length & 0xC0 == 0xC0:
            if cursor + 1 >= len(packet):
                raise ValueError("truncated DNS name pointer")
            pointer = ((length & 0x3F) << 8) | packet[cursor + 1]
            if pointer >= len(packet) or pointer in visited or hops > 16:
                raise ValueError("invalid or looping DNS name pointer")
            if end is None:
                end = cursor + 2
            visited.add(pointer)
            cursor = pointer
            hops += 1
            continue

        if length & 0xC0:
            raise ValueError("unsupported DNS label encoding")
        cursor += 1
        if length == 0:
            if end is None:
                end = cursor
            return ".".join(labels).lower(), end
        if length > 63 or cursor + length > len(packet):
            raise ValueError("invalid or truncated DNS label")
        labels.append(packet[cursor:cursor + length].decode("ascii").lower())
        cursor += length

    raise ValueError("unterminated DNS name")


def parse_query(packet):
    if len(packet) < 12:
        raise ValueError("DNS packet shorter than header")
    transaction_id, flags, question_count, answer_count, authority_count, additional_count = struct.unpack(
        "!HHHHHH", packet[:12]
    )
    if flags & 0x8000:
        raise ValueError("received a DNS response, not a query")
    if question_count != 1:
        raise ValueError("demo expects exactly one DNS question")

    qname, name_end = decode_name(packet, 12)
    if name_end + 4 > len(packet):
        raise ValueError("truncated DNS question type/class")
    qtype, qclass = struct.unpack("!HH", packet[name_end:name_end + 4])
    question = packet[12:name_end + 4]
    return transaction_id, flags, qname, qtype, qclass, question


def build_response(query, answer_ip):
    transaction_id, query_flags, qname, qtype, qclass, question = query
    answer = b""
    rcode = 0

    if qname != DEFAULT_NAME:
        rcode = 3  # NXDOMAIN: this demo is authoritative only for one name.
    elif qtype != TYPE_A or qclass != CLASS_IN:
        rcode = 4  # NOTIMP: only A/IN is implemented.
    else:
        answer = (
            b"\xc0\x0c"
            + struct.pack("!HHIH", TYPE_A, CLASS_IN, 60, 4)
            + socket.inet_aton(answer_ip)
        )

    response_flags = 0x8000 | 0x0400 | (query_flags & 0x0100) | rcode
    answer_count = 1 if answer else 0
    header = struct.pack("!HHHHHH", transaction_id, response_flags, 1, answer_count, 0, 0)
    return header + question + answer


def serve(bind_address, port, answer_ip):
    # Validate the configured IPv4 address before opening the UDP socket.
    socket.inet_aton(answer_ip)
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        server.bind((bind_address, port))
    except OSError as error:
        server.close()
        if port < 1024:
            print(
                "Cannot bind UDP port {0}: {1}. On Linux, run with sudo for a port below 1024.".format(port, error),
                file=sys.stderr,
            )
        else:
            print("Cannot bind UDP {0}:{1}: {2}".format(bind_address, port, error), file=sys.stderr)
        return 1

    print(
        "DNS UDP server listening on {0}:{1}; {2} A -> {3} (DEMO ONLY, not the public example.com address)".format(
            bind_address, port, DEFAULT_NAME, answer_ip
        )
    )
    sys.stdout.flush()
    try:
        while True:
            packet, client = server.recvfrom(4096)
            try:
                query = parse_query(packet)
                response = build_response(query, answer_ip)
                server.sendto(response, client)
                print(
                    "Query from {0}: id=0x{1:04x} {2} type={3} class={4}; response answers={5}".format(
                        client,
                        query[0],
                        query[2],
                        query[3],
                        query[4],
                        struct.unpack("!H", response[6:8])[0],
                    )
                )
                sys.stdout.flush()
            except (ValueError, UnicodeError, struct.error) as error:
                print("Dropped malformed DNS query from {0}: {1}".format(client, error), file=sys.stderr)
    except KeyboardInterrupt:
        print("DNS server stopped.")
    finally:
        server.close()
    return 0


def main():
    parser = argparse.ArgumentParser(description="CO3094 demo DNS A responder over UDP")
    parser.add_argument("--bind", default="0.0.0.0", help="listen address (default: 0.0.0.0)")
    parser.add_argument("--port", type=int, default=53, help="UDP port (default: 53)")
    parser.add_argument(
        "--answer-ip",
        default=DEFAULT_DEMO_IP,
        help="demo IPv4 answer; default 192.0.2.123 is documentation-only",
    )
    args = parser.parse_args()
    return serve(args.bind, args.port, args.answer_ip)


if __name__ == "__main__":
    sys.exit(main())
