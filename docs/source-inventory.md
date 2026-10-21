# Source inventory

## Access and scope

The workspace path supplied by the session was:

`D:\01. Dai_Hoc_Dai_Dai_Di\05. HKI_NAM3\Mạng máy tính (TN) (CO3094)_NGUYỄN PHƯƠNG DUY (CQ_HK261) [L07]`

That exact path does not exist in the accessible filesystem. A recursive directory-name search under `D:\01. Dai_Hoc_Dai_Dai_Di` found no `CO3094` or `L07` folder. The nearest available materials are at `D:\01. Dai_Hoc_Dai_Dai_Di\05. HK1_NAM3\MMT`. The digit in `HK1` is numeral one. Its `data\ThongTin.txt` identifies the course as **CO3093**, so it is adjacent background only, not CO3094 authority.

## Primary and user-provided sources

| ID | Source | Material read | Trust / use | Missing evidence |
|---|---|---|---|---|
| P1 | User-attached master prompt, including Email A (dated 2026-10-08) and Email B excerpts | Full attachment | Highest available authority for this pass | Original mailbox messages and LMS announcement not independently opened |
| P2 | Google Doc “CO3094 - LAB 2 | Hướng dẫn chuẩn bị & phân công nhóm 6 người” | Drive Search returned indexed text and metadata (native Doc, size 6699, updated 2026-10-21) | Reviewed as an AI-produced guide, not as authority | Native Docs text read and Drive fetch each returned 404; structure and editability unverified |
| P3 | Forum “Lab 1 - Network device and Network application” | Not accessible | Must contain the teacher-overwritten `new_connection` per Email A | Post, code, timestamp, and matching `server.py` unavailable |

## Adjacent local CO3093 bundle

| File | Content inspected | Relevance / confidence |
|---|---|---|
| `MMT\data\ThongTin.txt` | Identifies CO3093 | Confirms this is a different course |
| `MMT\data\Description.txt` | General course description/outcomes mentioning HTTP, TCP/UDP, reliability, flow and congestion control | Generic CO3093 context only |
| `MMT\data\General information and course outline.txt` | Chapter 2 application layer, HTTP, socket programming; assignment described as network application | CO3093 only |
| `MMT\data\slide\Chapter_2_v9.0.pdf` | Extracted PDF page 31, labeled “Application Layer: 2-31”: netcat/ncat client sends an HTTP GET to a remote server | Does not show the VM server or `new_connection`; version for CO3094 unconfirmed |
| `MMT\data\slide\Chapter_2_v8.0.pdf` | Extracted page 31 is an OCR/translation fragment about HTTP status codes | Not evidence for the target server |
| `MMT\data\Lab\Lab 01\Lab_1a_Network Devices.pdf` | First page identifies Lab 1 as Network Devices; PDF search for `new_connection` and `22236` had no hits | Not the target HTTP forum handout |
| `MMT\data\Lab\Lab 01\Lab_1b_Wireshark_Intro_v8.0.pdf` | First page identifies Wireshark Getting Started | Background only |
| `MMT\data\Lab\Lab 02\Lab_2a_Wireshark_HTTP_v8.0.pdf` | HTTP packet inspection; no `new_connection` or `22236` hits | CO3093 exercise, not the CO3094 host-to-VM task |
| `MMT\data\Lab\Lab 02\Lab_2b_Wireshark_DNS_v8.0.pdf` | DNS packet inspection | Not the target task |
| `MMT\data\Lab\Lab 02\Lab02_1513804.pdf` | Student report with named student and HTTP Wireshark exercise | Not used as course authority or copied; contains personal data |
| Recursive `MMT\*.py` inventory | No Python files found | No local `server.py`, `client.py`, or `new_connection` implementation in this adjacent bundle |

### Code and port findings

- No `.py` files exist in the accessible adjacent `MMT` tree.
- Searches of its Lab 1 and Lab 2 PDFs found neither `new_connection` nor port `22236`.
- The teacher's implementation, signature, handler argument order, port, and bind address remain **UNVERIFIED for CO3094**. Do not copy student work or CO3093 sources into this repository.

## External technical references

These explain protocol/tool behavior; they do not add instructor requirements.

| Source | Use |
|---|---|
| [Oracle VirtualBox 7.2 Virtual Networking](https://docs.oracle.com/en/virtualization/virtualbox/7.2/user/networkingdetails.html) | Host-only is host↔guest without external network; NAT is not inbound-reachable without port forwarding; bridged joins the physical LAN |
| [Python socket docs](https://docs.python.org/3/library/socket.html#socket-objects) | `accept()` returns `(conn, address)` |
| [Python threading docs](https://docs.python.org/3/library/threading.html#thread-objects) | `Thread.args` are positional arguments passed to the target |
| [Microsoft Test-NetConnection docs](https://learn.microsoft.com/en-us/powershell/module/nettcpip/test-netconnection?view=windowsserver2025-ps) | Supports a remote TCP port test with `-Port`; this checks TCP connectivity, not an HTTP response |
| [RFC 9000](https://www.rfc-editor.org/rfc/rfc9000.html) | QUIC reliable ordered streams and receiver-advertised flow-control limits |
| [RFC 9002](https://www.rfc-editor.org/rfc/rfc9002.html) | QUIC loss detection, NewReno-like congestion control, and pacing |
| [RFC 9221](https://www.rfc-editor.org/rfc/rfc9221.html) | Unreliable QUIC DATAGRAM frames without retransmission, still congestion controlled |
| [Valve GameNetworkingSockets](https://github.com/ValveSoftware/GameNetworkingSockets) | Official message-oriented example with reliable/unreliable messages and packet-status ACK ideas |

## Search record

Local listing and recursive `*.py` search used `rtk proxy python` from the reachable `MMT` directory. Chapter 2 page text was extracted with Python `pypdf`. Drive Search returned the exact supplied Google Doc text; direct Docs text read and Drive fetch returned 404.
