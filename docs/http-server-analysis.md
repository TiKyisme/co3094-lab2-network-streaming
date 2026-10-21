# HTTP server source analysis

## Source status

The user supplied a three-page PDF export of the LMS thread “Lab 1 - Network device and Network application.” Visual and text inspection confirms the instructor's forum reply, HTTP handler, listener settings, and a historical demonstration result. The PDF is outside this repository. The linked attachment `sample_code_http_server_process.txt` is not present in the repo, the course-source folder, Downloads, `D:\download`, `D:\TiKy`, or the inspected Codex attachments.

The attachment link on PDF p. 2 points to LMS file ID `84252`. An unauthenticated request redirects to the BK-LMS login page, so the complete attached server source could not be retrieved. No credentials were used. The forum handler is now confirmed, but its matching server loop remains unavailable.

## Confirmed forum settings and handler

The instructor's reply on PDF p. 1 says to set `hostip = "0.0.0.0"` and `port = 22236`. The code on p. 2 defines `new_connection(conn, addr)` and a `receive_http_header(conn)` helper. The handler:

- reads until the HTTP header terminator `\r\n\r\n` or the peer closes the connection, receiving in chunks of up to 1024 bytes;
- decodes the request as UTF-8, checks whether the first line starts with `GET`, and sends the prepared HTTP response for that case;
- returns a static “HTTP Welcome” HTML page with status `HTTP/1.1 200 OK`, a content length, `Connection: close`, and UTF-8 HTML content;
- closes the connection in `finally`.

The `MAX_HEADER_SIZE` constant controls each `recv` chunk, not the total accumulated header size. The code does not parse a path or produce an HTTP error response for non-GET requests; that branch only prints a message before the connection is closed. These are observations about the supplied handler, not changes to instructor code.

## Matching server source still required

The forum handler's positional signature is `new_connection(conn, addr)`. The separate Sample NetApp PDF p. 7 calls `Thread(..., args=(addr, conn))` for a different signature, `new_connection(addr, conn)`. Reusing that sample call unchanged would reverse the forum handler's arguments. The linked full server-process attachment is needed to confirm the actual `accept()` loop, thread arguments, startup command, and how the forum's `hostip` and `port` settings are applied.

## Historical Lab 1 demonstration in the forum export

PDF p. 3 contains an instructor-posted result image showing a command prompt response with `HTTP/1.1 200 OK`, `Content-Length: 174`, and the HTML body, followed by a Chrome rendering of the welcome page. The browser address bar in the image shows `192.168.56.103:22236`; the text immediately above the image says `http://192.168.56.100:22236`. The displayed command output is dated 10 September 2026. This is evidence that the course demonstration worked at that time, not a current test of the local `ubuntu` VM or proof of its adapter configuration. The `.100`/`.103` difference is unresolved.

## Separate Sample NetApp PDF, page 7

Visual inspection of the embedded code shows a TCP accept/print skeleton:

- `server_program(host, port)` creates a default TCP socket, binds it, calls `listen(10)`, then loops over `accept()`.
- `accept()` supplies `(conn, addr)`; the sample passes `(addr, conn)` to `new_connection(addr, conn)`.
- Its worker body only prints the socket object. It does not parse an HTTP request or send a response.
- The sample sets port `22236` and derives `host` using a UDP route attempt to `8.8.8.8:1`, with a `127.0.0.1` fallback.

The forum independently confirms port `22236`, but its handler signature differs from the sample's. Do not treat the sample server loop as the matching forum server.

## Current execution status

No server was started in this session. The local `ubuntu` VM is powered off; its guest IP, firewall, and listening state remain unknown. No current Windows TCP, `curl.exe`, browser, or server-log test was run. Continue with [network setup](network-setup.md) after the linked server source is provided.
