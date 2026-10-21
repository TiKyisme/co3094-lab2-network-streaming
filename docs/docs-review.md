# Review of the existing Google Doc

**Document:** “CO3094 - LAB 2 | Hướng dẫn chuẩn bị & phân công nhóm 6 người”  
**Basis:** full indexed text returned by Google Drive Search, compared with the supplied Email A/B excerpts and the CO3094/L07 source package now available.

**Access limit:** Drive Search returned the document text/metadata; native Docs read and Drive fetch returned 404. This remains a text-content review. Native formatting/comments and in-place editing were not available. The original is unchanged; see the corrected [Markdown guide](lab2-group-guide.md).

| Nội dung | Nhận định | Nguồn chứng minh | Mức độ | Hành động |
|---|---|---|---|---|
| Lab 2 scope: host→VM HTTP using forum-overwritten `new_connection`; three feature drafts | Matches supplied instructor emails | Email A/B | Pass; exact code still missing | Keep; mark topology/code values unknown until forum source is read |
| No claim that all three mechanisms require implementation | Guide correctly separates draft design from implementation | Email B says “draft design” | Pass | Keep distinction |
| Steam UDP and Google QUIC | Correctly presented as examples, not complete protocol mandates | Email A says “ví dụ” | Pass | Preserve as references |
| Six-person Lab 2 team, two per feature | Matches Email B for Lab 2; Assignment 1 PDF separately says Individual/Pair | Email B; Assignment 1 PDF p. 1 | **CONFLICT / scope ambiguity** | Preserve the earlier Reliability pair as TENTATIVE; confirm current Assignment 1 grouping |
| Assignment 1 evaluation week | Email says oral examination in week containing Nov 17; Assignment 1 source has separate date text | Email B; Assignment 1 PDF p. 4 and LMS note | Pass for week statement; exact hand-in timestamp unverified | Do not present the PDF's “Sunday” label as confirmed |
| Screenshots/browser logs/checklist | Useful proposed internal evidence; emails do not specify screenshots. A generic LMS note says practical classes submit reports and major assignments have reports/presentations, but it does not define Lab 2 evidence format | Email A/B; LMS note `src_2f001836c9a5` | Medium | Keep screenshots PROPOSED; confirm the exact Lab 2 report/presentation requirements |
| Host-only plus optional NAT | Host-only supports host↔guest; NAT inbound service needs forwarding. Existing Ubuntu VM currently uses Bridged, and sample code's route helper may bind an unsuitable interface under Host-only/NAT | Oracle VirtualBox manual; Sample_NetApp PDF p. 7 | Pass with important caveat | Do not change topology until forum bind logic is checked |
| Function signature and argument order | The Sample NetApp PDF p. 7 shows a sample handler `new_connection(addr, conn)` called with `args=(addr, conn)`; this is not the forum overwrite | CO3094 Sample_NetApp PDF p. 7; Python docs | High / forum version UNVERIFIED | Preserve the sample finding separately; obtain exact forum post before using it |
| Port 22236 | Confirmed only in Sample_NetApp PDF p. 7, not in an HTTP response server or the forum override | CO3094 Sample_NetApp PDF p. 7 | Supported for sample; unverified for Lab 2 server | Label as sample port; do not assume the forum version matches |
| HTTP handler claim | Sample NetApp page 7 only prints the socket; it does not parse HTTP or send a response. CO3094 Lab 1 pp. 5–6 show a separate GNS3/lighttpd HTTP exercise | CO3094 Sample_NetApp PDF p. 7; Lab 1 PDF pp. 5–6 | High | Do not call either source the overwritten HTTP server |
| Test-NetConnection and browser checks | Appropriate separate tests; TCP success is not HTTP success | Microsoft cmdlet docs; project test cases | Pass | Keep TCP, curl, and browser as separate results |
| Reliability/flow/congestion content | Suitable Lab 2 draft themes, but Assignment 1 PDF has transport and HoL conflicts | Email A/B; Assignment 1 PDF pp. 1–3 | Pass for Lab 2 proposal; A1 compatibility unresolved | Keep proposed designs, add explicit compatibility caveat |
| `min(rwnd,cwnd)` integration | Needs precise quantities: receiver credit bounds new bytes; congestion budget bounds bytes in flight | RFC 9000/9002 | Medium | Use `min(flow_credit, cwnd - bytes_in_flight)` for new reliable bytes |
| Names in original guide | Reliability pair names were present while other pair names were blank | Existing Google Doc text | TENTATIVE | Preserve names only as tentative; don't declare roster confirmed |
| Lab 1/Telnet carryover | Lab 1 material is useful context but does not create Lab 2 screenshot/Telnet requirements | User prompt; CO3094 Lab 1 PDF | Medium | Keep optional unless current instructor instruction requires it |
| Assignment 1 source fit | PDF p. 1 says UDP streaming, p. 2 TCP reliable transfer, p. 3 TCP handshake and UDP file reassembly; p. 4 HTTP UI and submission requirements | Assignment 1 PDF `src_076bd2c18b0d`, pp. 1–4 | CONFLICT for A1 design; separate from Lab 2 scope | Record in requirements matrix; do not choose one transport as official |

## Corrected copy

The Markdown guide now preserves the earlier Reliability names as TENTATIVE, distinguishes the page 7 sample from the missing forum overwrite, labels the 22236 port as sample-only, records Assignment 1 conflicts without resolving them, and separates Assignment 1 submissions from Lab 2. No source ZIP/PDF was copied into Git.
