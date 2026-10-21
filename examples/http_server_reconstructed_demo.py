"""Local group reconstruction for a Lab 2 HTTP smoke demo.

This is NOT the complete instructor server source. It combines the user's old
server skeleton (whose accept/thread argument order is conn, addr) with the
visible handler from the supplied Lab 1 forum PDF. The separate official
sample_code_http_server_process.txt attachment is still unavailable.

Keep this file distinct from server_skeleton_previous_upload.py and do not
present it as an unmodified teacher-provided server.
"""

import datetime
import socket
from threading import Thread


HTML = """<!DOCTYPE html>
<html>
   <head>
       <title>HTTP Welcome</title>
   </head>
   <body>
       <p>An example of a simple HTML Hello World! page.</p>
   </body>
</html>"""


def build_http_response():
    html_bytes_len = len(HTML.encode("utf-8"))
    current_time_gmt = (
        datetime.datetime.now(datetime.timezone.utc)
        .strftime("%a, %d %b %Y %H:%M:%S GMT")
    )
    response = (
        "HTTP/1.1 200 OK\r\n"
        f"Date: {current_time_gmt}\r\n"
        "Server: pdnguyen @ HCMUT-VNUHCM HTTP server\r\n"
        f"Last-Modified: {current_time_gmt}\r\n"
        "Accept-Ranges: bytes\r\n"
        f"Content-Length: {html_bytes_len}\r\n"
        "Connection: close\r\n"
        "Content-Type: text/html; charset=utf-8\r\n"
        "\r\n"
        f"{HTML}"
    )
    return response.encode("utf-8")


HTTP_RESPONSE = build_http_response()


def receive_http_header(conn):
    """Read request bytes through the HTTP header terminator."""
    request_bytes = b""
    max_chunk_size = 1024

    while b"\r\n\r\n" not in request_bytes:
        chunk = conn.recv(max_chunk_size)
        if not chunk:
            break
        request_bytes += chunk

    return request_bytes


def new_connection(conn, addr):
    """Handle one GET using the visible forum handler's argument order."""
    try:
        request_bytes = receive_http_header(conn)
        request_text = request_bytes.decode("utf-8")
        first_line = request_text.split("\r\n")[0]

        if first_line.upper().startswith("GET"):
            print(f"Returned 200 OK response to {addr}")
            conn.sendall(HTTP_RESPONSE)
        else:
            # The visible forum handler logs non-GET methods and closes; it
            # does not send a separate HTTP error status for this branch.
            print(f"Method is not decoded successfully for {addr}")
    except Exception as error:
        print(f"Error handling connection from {addr}: {error}")
    finally:
        print(f"Closing connection to {addr}")
        conn.close()


def server_program(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(10)
    print(f"Listening on {host}:{port}")

    try:
        while True:
            conn, addr = server_socket.accept()
            # This order matches new_connection(conn, addr).
            Thread(target=new_connection, args=(conn, addr)).start()
    finally:
        server_socket.close()


if __name__ == "__main__":
    # 0.0.0.0 is the listener address. Clients must use the guest's real IPv4.
    HOSTIP = "0.0.0.0"
    PORT = 22236
    server_program(HOSTIP, PORT)
