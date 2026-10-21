# HTTP server source analysis

## Source status

The CO3094/L07 package includes a Sample NetApp PDF and a CO3094 Lab 1 PDF, but no standalone `.py` files in the ZIP. The Sample NetApp PDF page 7 contains the sample `server.py` as an image; page 8 contains `client.py` as an image. The exact LMS forum-overwritten `new_connection` is still missing.

## Verified sample from Sample_NetApp.pdf, page 7

Visual inspection of the embedded code shows:

- `server_program(host, port)` creates a default TCP socket, binds it, calls `listen(10)`, then loops over `accept()`.
- Python `accept()` supplies `(conn, addr)`.
- The sample calls the worker with `Thread(target=new_connection, args=(addr, conn))`.
- Its worker signature is `new_connection(addr, conn)`, and its body only prints the connection object.
- The sample sets port **22236**.
- It derives `host` with `get_host_default_interface_ip()`, which uses a UDP socket attempt to `8.8.8.8:1` and falls back to `127.0.0.1` on exception.

This verifies argument order and port for this printed **sample only**. The handler does not parse an HTTP request or send an HTTP response. The exact forum overwrite may change the signature, body, bind logic or port; inspect that post before running the required Lab 2 server.

## Lab 1 evidence

The CO3094 Lab 1 PDF (source ID `src_bb5408286b99`) says on page 8 that sample `server.py`/`client.py` and a VM template are provided. Pages 5–6 describe a separate GNS3 PC-to-HTTP-server exercise using `lighttpd`, static IPs and a browser GET. That exercise does not identify the forum-overwritten Python handler required by Email A.

## HTTP implementation status

- No verified HTTP request parsing, status line, headers, response body or browser response handler was found in the page 7 sample code.
- The ZIP has no standalone Python source file; the visible sample is embedded in the PDF.
- The forum post and its matching current `server.py` remain **MISSING**.
- Port 22236 is **SUPPORTED for the page 7 sample**, but **UNVERIFIED for the forum-overwritten server**.
- Do not rename the page 7 sample or claim it satisfies the HTTP requirement.

## Current execution status

No server was started. The local `ubuntu` VM is powered off, and no running VirtualBox guests were found. No Windows TCP, curl, browser, or server-log result exists yet. Continue with [network setup](network-setup.md) after the forum code is supplied.
