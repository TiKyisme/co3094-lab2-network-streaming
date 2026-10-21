# Review of the existing Google Doc

**Document:** “CO3094 - LAB 2 | Hướng dẫn chuẩn bị & phân công nhóm 6 người”  
**Review basis:** Full indexed text returned by Google Drive Search for the exact title/ID, compared with the two instructor email excerpts in the user's attached prompt and primary technical references.

**Access limit:** Drive Search returned text and metadata. Native Docs text read and Drive fetch both returned 404 for the same ID. This is therefore a text-content review; native formatting, comments, tables, and editability were not independently inspected. No in-place edit was attempted. The corrected working copy is [lab2-group-guide.md](lab2-group-guide.md).

| Nội dung | Nhận định | Nguồn chứng minh | Mức độ | Hành động |
|---|---|---|---|---|
| Scope includes host→VM HTTP and three streaming features | Matches supplied Email A and Email B excerpts | Email A/B in user prompt | Pass | Keep, while marking exact topology and code details unknown |
| Full implementation required for all three features | Guide does not claim this; correctly says the email only names a draft design | Email B says “draft design” | Pass | Keep this distinction; ask about prototype only if it changes workload |
| Steam UDP and Google QUIC | Correctly used as examples, not mandated complete protocols | Email A says “for example” | Pass | Preserve as references |
| Six-person group and two people per feature | Matches “6 members” and “approx. 2 students/feature”; email does not establish names | Email B | Pass with roster caveat | Use placeholders until group confirms roster |
| Assignment 1 oral exam week of 17 Nov 2026 | Correctly separated from Lab 2 deadline | Email B excerpt and user's explicit clarification | Pass | Keep; do not infer a Lab 2 due date |
| Screenshots, browser logs, checklist | Useful internal preparation, but no screenshot submission requirement appears in the emails. Checklist phrasing could look mandatory | Email A/B omit deliverables | Medium | Label screenshots/logs PROPOSED internal evidence |
| Host-only plus optional NAT | Technically valid for host↔guest plus optional guest Internet. Host-only alone is simpler if guest needs no Internet. NAT alone needs port forwarding for inbound guest services | Oracle VirtualBox 7.2 manual | Pass with refinement | Recommend Host-only first; add NAT only for separate Internet need. Bridged is a LAN-exposed fallback |
| IP and server bind instructions | Correct that loopback-only bind cannot accept Windows connections to VM IP. `0.0.0.0` listens on every guest interface | Python sockets and VirtualBox networking | Pass with safety refinement | Prefer Host-only guest IP if class code allows; otherwise understand interface exposure |
| `new_connection` replacement/thread call | Correctly directs team to forum version, but the document cannot prove function signature or argument order | Email A; Python docs; forum code unavailable | High / UNVERIFIED | Obtain exact forum code and matching server. `accept()` returns `(conn, address)`; `Thread(args=...)` passes them positionally; neither fact proves teacher signature |
| Port 22236 | Guide itself warns to check the actual file; no local source supports it | Existing guide; adjacent CO3093 inventory has no match | Medium / UNVERIFIED | Do not use until correct source confirms it |
| Test-NetConnection and browser | Good layered checks. TCP reachability alone does not prove an HTTP response | Command semantics and guide | Pass with refinement | Keep both; use browser or curl GET for HTTP validation |
| Reliability section | Sequence number, ACK, timeout, retransmission, duplicate/order handling and real-time expiry fit a draft design | Email asks for design; RFC 9000/9002 and Valve repo are references | Pass as proposal | Add ACK range/status details; separate reliable control from expiring media |
| Flow control section | Buffer/window, updates, pause, slow receiver fit a draft design | Email; RFC 9000 reference | Pass as proposal | Define credit units, update semantics and zero-credit behavior |
| Congestion control section | RTT/loss, `cwnd`, pacing and AIMD/CUBIC/BBR comparisons are suitable | Email; RFC 9002 reference | Pass as proposal | Pick one baseline and state what RTT growth without loss does |
| `min(rwnd,cwnd)` example | Useful intuition but can compare unlike quantities. Receive credit limits new data; congestion budget limits bytes in flight | RFC 9000 flow control; RFC 9002 congestion window | Medium | Use `min(flow_credit, cwnd - bytes_in_flight)` for new reliable bytes; all transmitted packets, including retransmissions/datagrams, remain congestion controlled |
| Team allocation | Role pairs are reasonable. Old guide names one Reliability pair but says elsewhere to fill names later, while other pairs are unnamed | Existing guide; no roster source | Medium | Working copy uses Member A–F placeholders until confirmed |
| Lab 1 and Telnet carryover | Useful optional context, not confirmed Lab 2 deliverables. Nearby CO3093 Lab 1 files are Network Devices/Wireshark, not the target server lab | User prompt's Lab 1 context and adjacent local files | Medium | Keep Telnet optional; do not require old Lab 1 screenshots |
| Questions to instructor | Existing questions target protocol, prototype, deliverables and compatibility | Email A/B leave these unspecified | Pass | Add exact forum code, topology, Lab 2 date and roster confirmation |
| Overall test assurance | No live VirtualBox/Windows/Ubuntu check; no server source in reachable bundle | `VBoxManage` missing; source inventory | High limitation | Mark all network tests WAITING_FOR_MANUAL_TEST |

## Corrected copy

The Markdown copy preserves confirmed requirements, labels recommendations as PROPOSED, removes unconfirmed member identities, refines the VirtualBox recommendation, and does not invent code, ports, deliverables, or test results. The original Google Doc remains unchanged because the native Docs API returned 404 and its structure/editability could not be checked.
