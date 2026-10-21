# HTTP server source analysis

## Status: WAITING_FOR_SOURCE

The accessible filesystem does not contain the stated CO3094/L07 directory. The nearest available `MMT` tree is CO3093 and has no Python files. Its Lab 1/2 PDFs contain no `new_connection` or `22236` match. Therefore no local `server.py`, `client.py`, or teacher function was reviewed.

## What can be verified generally

Official Python documentation states:
- `socket.accept()` returns a pair `(conn, address)`.
- `threading.Thread(args=...)` passes the tuple/list elements as positional arguments to its target.

A conventional call may therefore look like:

```python
conn, addr = listener.accept()
thread = Thread(target=new_connection, args=(conn, addr))
thread.start()
```

This is only an illustration of Python's API. It is **not** the teacher's code or a verified call for the CO3094 server. The forum function may use a different signature; inspect it and the call site together before editing.

## Required source review when provided

1. Record the exact `new_connection` definition and parameters.
2. Trace values from `accept()` through the thread's `args` to the function body.
3. Record the listener's bind IP and port from the file; do not assume 22236.
4. Check whether the server binds to loopback, a single interface, or all interfaces.
5. Check how the HTTP request is read and how the status line, headers, body, and connection close are sent.
6. Preserve the course code in the original source copy; make any experiments in this repository.
7. Run tests only after the source is understood, then record actual output.

## Not established

- Whether the official function expects `(conn, addr)` or another order.
- The current port and bind address.
- Whether the server code handles HTTP/1.0 or HTTP/1.1, multiple requests, or multiple clients.
- Whether a local source file matches the forum's overwritten version.
