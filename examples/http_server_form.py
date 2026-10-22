#!/usr/bin/env python3
"""Small HTTP-over-TCP form demo for CO3094 Lab 2.

Uses only Python's socket module and runs on Python 2.7+ and Python 3.
This is a separate lab demo; it does not modify or replace instructor code.
"""

from __future__ import print_function

import argparse
import socket
import sys
from datetime import datetime


HTML = b"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>CO3094 HTTP Form Demo</title>
  <style>
    body { font: 18px/1.5 sans-serif; max-width: 42rem; margin: 3rem auto; padding: 0 1rem; }
    input, button { font: inherit; padding: .45rem .7rem; margin: .35rem 0; }
    #result { display: block; margin-top: 1rem; color: #124c83; font-weight: 700; }
  </style>
</head>
<body>
  <h1>CO3094 HTTP Server over TCP</h1>
  <p>Enter your name and press Display.</p>
  <label for="name">Name:</label>
  <input id="name" type="text" autocomplete="off">
  <button id="display" type="button">Display</button>
  <label id="result" aria-live="polite">The greeting will appear here.</label>
  <script>
    document.getElementById("display").addEventListener("click", function () {
      var name = document.getElementById("name").value.trim();
      document.getElementById("result").textContent = name
        ? "Welcome, " + name + "!"
        : "Please enter your name.";
    });
  </script>
</body>
</html>
"""


def response(status, reason, body):
    date_value = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")
    headers = (
        "HTTP/1.1 {0} {1}\r\n"
        "Date: {2}\r\n"
        "Server: CO3094-socket-demo\r\n"
        "Content-Type: text/html; charset=utf-8\r\n"
        "Content-Length: {3}\r\n"
        "Connection: close\r\n"
        "\r\n"
    ).format(status, reason, date_value, len(body))
    return headers.encode("ascii") + body


def handle_client(conn, address):
    request = b""
    try:
        conn.settimeout(5)
        while b"\r\n\r\n" not in request and len(request) < 16384:
            chunk = conn.recv(4096)
            if not chunk:
                break
            request += chunk

        first_line = request.split(b"\r\n", 1)[0]
        if first_line.startswith(b"GET "):
            conn.sendall(response(200, "OK", HTML))
            print("HTTP 200 sent to {0}: {1}".format(address, first_line.decode("ascii", "replace")))
        else:
            body = b"<html><body><h1>405 Method Not Allowed</h1></body></html>"
            conn.sendall(response(405, "Method Not Allowed", body))
            print("HTTP 405 sent to {0}: {1}".format(address, first_line.decode("ascii", "replace")))
    except Exception as error:
        print("HTTP client error for {0}: {1}".format(address, error), file=sys.stderr)
    finally:
        conn.close()


def serve(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(10)
    print("HTTP TCP server listening on {0}:{1}".format(host, port))
    sys.stdout.flush()
    try:
        while True:
            conn, address = server.accept()
            handle_client(conn, address)
    except KeyboardInterrupt:
        print("HTTP server stopped.")
    finally:
        server.close()


def main():
    parser = argparse.ArgumentParser(description="CO3094 socket HTTP form demo")
    parser.add_argument("--bind", default="0.0.0.0", help="listen address (default: 0.0.0.0)")
    parser.add_argument("--port", type=int, default=8000, help="TCP port (default: 8000)")
    args = parser.parse_args()
    serve(args.bind, args.port)


if __name__ == "__main__":
    main()
