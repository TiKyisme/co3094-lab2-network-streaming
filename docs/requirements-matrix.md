# Requirements and source-conflict matrix

## Lab 2 requirements from the instructor emails

The two email excerpts were supplied by the user; the original mailbox and current LMS forum have not been opened. Email A/B remain the highest available authority for Lab 2.

| Requirement / claim | Classification | Source | Boundary |
|---|---|---|---|
| Physical Windows host accesses an HTTP server running in a VM using the teacher-overwritten `new_connection` | REQUIRED | Email A, 2026-10-08 | The exact forum function and matching server are still missing |
| Draft design for Reliability, Flow Control, Congestion Control | REQUIRED | Email A and Email B | “Draft design” does not itself require implementation |
| Six-person team, approximately two students per feature | REQUIRED / SUPPORTED | Email B | The six-person Lab 2 design group is stated; this does not by itself settle Assignment 1 project grouping |
| Preserve AI prompt history | REQUIRED | Email A and Email B | Preserve exact prompts and a private session export; no unreviewed export is committed |
| Steam UDP gaming and Google QUIC | SUPPORTED examples | Email A | Reference examples, not a mandate to reproduce either full protocol |
| Forum HTTP listener settings | SUPPORTED, instructor-provided implementation settings | User-supplied Lab 1 LMS forum export, pp. 1–2 | Specifies `hostip = "0.0.0.0"`, port `22236`, and handler signature `new_connection(conn, addr)`; complete linked server source is still unavailable |
| Assignment 1 oral evaluation in the week containing 2026-11-17 | REQUIRED for Assignment 1 | Email B excerpt | This is an evaluation-week statement, not a Lab 2 deadline |
| Lab 2 must use UDP, submit screenshots/report/code, or implement the three mechanisms | UNVERIFIED | Not stated in Email A/B | Do not infer from Assignment 1 or Lab 1 requirements. The forum port applies to its HTTP server task, not the streaming design |
| Generic LMS note says practical classes submit reports; major assignments have reports and presentations | SUPPORTED general course policy | `Announcements - Ghi chú`, source ID `src_2f001836c9a5` | Does not specify a Lab 2 screenshot, file format, or exact report content |

## Assignment 1 statements in the CO3094 source pack

These statements are relevant to later Assignment 1 implementation and to whether the current design draft will transfer. They do **not** override the Lab 2 email.

| Statement | Source locator | Classification |
|---|---|---|
| Goal: custom application-layer protocol over “UDP STREAMING”; reliable messaging and file transfer | Assignment 1 PDF, `src_076bd2c18b0d`, p. 1 | REQUIRED for the project as written; conflicts with later transport details |
| TCP for reliable file/message transfer; UDP for heartbeat/discovery | Same PDF, p. 2 | REQUIRED for the project as written; conflicts with UDP-only language elsewhere |
| Monotonic sequence number and sliding window for flow control and in-order delivery; retransmit missing segments | Same PDF, p. 2 | REQUIRED for the project as written |
| Time-sensitive UDP stream should eliminate head-of-line blocking | Same PDF, p. 2 | REQUIRED for the project as written; exact scope of “eliminate” is unspecified |
| Raw sockets; no high-level network libraries; Flask/Django and WebSockets prohibited | Same PDF, p. 3 | REQUIRED for Assignment 1; do not assume a framework is allowed |
| Basic client-server handshake over TCP | Same PDF, p. 3, milestone 2 | REQUIRED for Assignment 1 as written; transport conflict remains |
| Reliable file transfer chunks/reassembly over UDP without corruption | Same PDF, p. 3, milestone 6 | REQUIRED for Assignment 1 as written; conflicts with TCP reliable-transfer text |
| HTTP-based UI with client-side JavaScript | Same PDF, p. 4, milestone 9 | REQUIRED for Assignment 1 as written; may be possible with raw sockets, but implementation boundary needs clarification |
| Submit source code, README and technical explanation PDF | Same PDF, p. 4 | Assignment 1 submission requirement; not confirmed for Lab 2 |
| “Individual / Pair Project” | Same PDF, p. 1 | Project grouping stated in PDF; potential conflict with Email B group registration |
| “Suggested Deadline: Sunday, November 17, 2026, at 11:59 PM” | Same PDF, p. 4 | Date/weekday conflict; the calendar date 2026-11-17 is Tuesday |
| “Deadline: 17 Nov 2026” | Assignment 1 socket-programming LMS note, `src_4c5a77dffaa2`, document | Packaged LMS note has no weekday/time; live page not opened |
| Oral exam in week 47 / week containing Nov 17 | Email B | Separate oral-evaluation statement; does not resolve the PDF's suggested hand-in timestamp |
| Sample server uses port 22236 | Sample NetApp PDF, `src_b850d73292a7`, p. 7 (embedded code image) | SUPPORTED for that sample; the forum independently specifies the same port for its handler, but uses a different `new_connection` argument order |

## Reported conflicts — preserve, do not resolve by assumption

| ID | Conflict | Evidence | Status / action |
|---|---|---|---|
| C-01 | UDP streaming goal vs TCP reliable file/message transfer; milestone 2 uses TCP while milestone 6 requires UDP file reassembly | Assignment 1 PDF pp. 1–3 | **CONFLICT.** Keep both statements. Ask the instructor which transport applies to which channel/file operation before final architecture |
| C-02 | “Individual / Pair Project” vs Email B's six-person assignment group and six-person Lab 2 design team | Assignment 1 PDF p. 1; Email B | **CONFLICT / scope ambiguous.** Could refer to different scopes or revisions; confirm current Assignment 1 team size |
| C-03 | Suggested Sunday 2026-11-17 vs the calendar date being Tuesday; packaged LMS note says 17 Nov without weekday/time; Email B names an evaluation week | Assignment 1 PDF p. 4; LMS note; Email B | **CONFLICT.** Do not publish an exact hand-in deadline until the instructor/LMS calendar confirms it |
| C-04 | “Eliminate” HoL blocking vs reliable in-order delivery and sliding-window sequencing | Assignment 1 PDF p. 2 | **TECHNICAL AMBIGUITY.** Independent channels can confine blocking, but the PDF does not define which ordering guarantees may be relaxed |
| C-05 | HTTP UI milestone vs prohibition on HTTP frameworks/WebSockets | Assignment 1 PDF pp. 3–4 | **AMBIGUITY, not proven contradiction.** A raw-socket HTTP server may be intended; clarify whether the prohibition is on frameworks only or HTTP itself |

## Proposal status

Current files under `docs/*-design.md` are **PROPOSED Lab 2 drafts**. They are not a final Assignment 1 architecture, do not select a winner among C-01 through C-05, and are not implementations. The forum handler and port are verified, but the complete linked server source and its compatibility with the handler remain unverified.
