# Source inventory — CO3094/L07 recovery

## Correct source package

The user supplied `CO3094_L07_source_handoff.md` and the actual source package is present beside it:

`D:\01. Dai_Hoc_Dai_Dai_Di\05. HKI_NAM3\Mạng máy tính (TN) (CO3094)_NGUYỄN PHƯƠNG DUY (CQ_HK261) [L07]`

- `CO3094_L07_source_handoff.md`: 4,439 bytes. Read fully; treated as a navigation/review aid, then checked against the package.
- `CO3094_L07_AI_Study_Pack.zip`: 19,474,824 bytes. Archive integrity check returned no bad member; 325 entries.
- Extracted `CO3094_L07_AI_Study_Pack\`; `00_START_HERE.md` explicitly confirms CO3094/L07 and `03_SOURCE_INDEX.md` provides stable source IDs.
- The ZIP contains no standalone `.py` or `.ova` entries. Do **not** copy the ZIP, PDFs, slides, OVA files, or extracted course materials into this GitHub repo.
- Relevant PDF bytes in the ZIP were SHA-256-compared with the extracted copies; all three checked PDFs matched.

## Primary sources inspected

| Source | Location / ID | Locator | Verified content and limits |
|---|---|---|---|
| Handoff summary | `CO3094_L07_source_handoff.md` | Whole file | Useful source map; all consequential claims below were checked against the pack |
| Course identity | `00_START_HERE.md` | Whole file | Explicitly identifies one course: CO3094/L07 |
| Source index | `03_SOURCE_INDEX.md` | Relevant entries at lines 357–375, 478–498, 500–555 | Maps source IDs to original titles/paths, normalized text, retained PDFs and page locators |
| Assignment 1 — Distributed Streaming-based Client-Server Collaboration Application | `src_076bd2c18b0d`; `sources/src_076bd2c18b0d__Assignment 1 - Assignment 1 - Distributed Streaming-based Client-Server Collaboration Application.pdf` | PDF pp. 1–4 | Original PDF read from ZIP; contains internally inconsistent TCP/UDP statements, project grouping, raw-socket restriction and deadline wording |
| Assignment 1 socket-programming LMS note | `src_4c5a77dffaa2`; `documents/other/assignment_1_building_a_network_application_socket_programming_ghi_chu__src_4c5a77dffaa2.md` | Document | Says application protocols are group-defined over TCP/IP and gives 17 Nov 2026 as a deadline; live LMS page not opened |
| General LMS announcement note | `src_2f001836c9a5`; `documents/00_course/announcements_ghi_chu__src_2f001836c9a5.md` | Document | General policy says practical classes submit reports; major assignments are evaluated with reports/presentations. It does not define Lab 2 evidence format |
| CO3094 Lab 1 — Network infrastructure and Network applications | `src_bb5408286b99`; `sources/src_bb5408286b99__Lab1 Network infrastructure and Network applications - CO3094 -Lab1-Network Device.pdf` | PDF pp. 1–8 | p. 1 includes PC-to-HTTP-server work and network-programming outcome; pp. 5–6 show a separate GNS3/lighttpd static-IP HTTP exercise; p. 8 says sample `server.py`/`client.py` and a VM template are provided |
| Sample network application — Sample NetApp | `src_b850d73292a7`; `sources/src_b850d73292a7__Sample network application - Sample_NetApp.pdf` | PDF pp. 7–8 | Embedded code images visually inspected. p. 7 shows a sample TCP accept/print server; p. 8 shows a client. Not the forum-overwritten HTTP handler |
| Sample source index entries | `src_098d45bf7b43` client; `src_86ccb3bac15a` server | `03_SOURCE_INDEX.md` lines 500–507 and 548–555 | Original `.py` entries are marked unsupported/skipped; standalone files are not present in the ZIP |

## Sample server details — do not confuse with forum override

Sample_NetApp PDF p. 7 visually shows:
- `accept()` values unpacked as `conn, addr`
- worker signature `new_connection(addr, conn)`
- thread called with `args=(addr, conn)`
- worker body only prints the socket object
- `server_program(host, port)` binds/listens; sample port is `22236`
- `get_host_default_interface_ip()` probes a UDP route to `8.8.8.8:1`, then falls back to `127.0.0.1`

Thus the printed sample demonstrates argument order and a sample port, but does not parse an HTTP request or send an HTTP response. The handoff's text-search claim that the exact name was absent from extracted text is accurate; visual PDF inspection found this different sample function. The exact LMS forum overwrite and matching current `server.py` are still missing.

## Assignment 1 conflict evidence

- PDF p. 1: custom application-layer protocol over UDP streaming and reliable messaging/file transfer.
- PDF p. 2: TCP for reliable file/message transfer, UDP for heartbeat/discovery; sliding-window sequencing; also says time-sensitive UDP should eliminate HoL blocking.
- PDF p. 3: basic TCP handshake milestone and reliable file chunk/reassembly over UDP; raw sockets required and high-level frameworks/WebSockets prohibited.
- PDF p. 4: HTTP-based UI milestone and source/README/report submission list; “Suggested Deadline: Sunday, November 17, 2026, at 11:59 PM.”
- The calendar date 2026-11-17 is Tuesday. The packaged LMS note gives 17 Nov without weekday/time, while Email B describes oral evaluation in the week containing Nov 17. Exact hand-in time and exam date remain unresolved.
- PDF p. 1 says Individual/Pair Project; Email B describes a six-person assignment group and a six-person Lab 2 feature-design group. Scope/revision conflict remains unresolved.

See [requirements-matrix.md](requirements-matrix.md) for classification and [open-questions.md](open-questions.md) for clarifications needed.

## Runtime source still needed

The CO3094 forum “Lab 1 - Network device and Network application” is not in the ZIP. The required overwritten `new_connection`, matching server source, actual HTTP request/response behavior, and final forum port are **UNVERIFIED**. No source ZIP/PDF/VM image was committed.


## External technical references (background, not course requirements)

| Source | Use |
|---|---|
| [Oracle VirtualBox 7.2 Virtual Networking](https://docs.oracle.com/en/virtualization/virtualbox/7.2/user/networkingdetails.html) | Host-only, NAT, bridged and NAT forwarding behavior |
| [Python socket docs](https://docs.python.org/3/library/socket.html#socket-objects) | `accept()` returns `(conn, address)` |
| [Python threading docs](https://docs.python.org/3/library/threading.html#thread-objects) | `Thread.args` are passed positionally |
| [Microsoft Test-NetConnection docs](https://learn.microsoft.com/en-us/powershell/module/nettcpip/test-netconnection?view=windowsserver2025-ps) | `-Port` checks TCP connectivity, not HTTP correctness |
| [RFC 9000](https://www.rfc-editor.org/rfc/rfc9000.html), [RFC 9002](https://www.rfc-editor.org/rfc/rfc9002.html), [RFC 9221](https://www.rfc-editor.org/rfc/rfc9221.html) | QUIC stream reliability/flow control, loss/congestion control, and unreliable datagrams as references |
| [Valve GameNetworkingSockets](https://github.com/ValveSoftware/GameNetworkingSockets) | Official reliable/unreliable message-oriented transport reference |
