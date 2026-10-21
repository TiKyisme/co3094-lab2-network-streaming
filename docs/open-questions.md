# Open questions after CO3094 source recovery

| Question | Why it matters | Evidence needed / owner |
|---|---|---|
| What is the exact forum post containing the overwritten `new_connection` and matching `server.py`? | The page 7 sample is not the forum override and does not send HTTP | User copies the complete LMS post and matching source |
| Which VM is intended for Windows↔Ubuntu testing? | `ubuntu` is registered locally but the ZIP contains no OVA and does not identify this VM as the instructor template | User/instructor confirms the VM; provide its image only if permitted |
| Which interface/address should the forum server bind to? | Page 7 sample's route helper may select loopback or a NAT-side address under Host-only topologies | Inspect forum code and observe `ip -4 addr` / `ss -lntp` |
| Does Assignment 1 require UDP for all payloads, or TCP reliable file/message transfer plus UDP discovery/streaming? | Assignment 1 PDF has conflicting transport statements on pp. 1–3 | Instructor clarification or a later authoritative LMS update |
| Is reliable file transfer specifically reassembled over UDP? | A1 milestone 6 says UDP; p. 2 says TCP reliable transfer | Instructor clarification |
| Is Assignment 1 solo/pair or six-person group? | PDF p. 1 says Individual/Pair; Email B refers to an Assignment group and a six-person Lab 2 team | Confirm whether the PDF version/group scope is current |
| What are the exact A1 hand-in deadline and oral-exam date? | PDF p. 4 labels Nov 17 2026 a Sunday, but 17 Nov 2026 is Tuesday; the LMS note/email use different wording | Current LMS calendar / instructor confirmation |
| How should “eliminate HoL blocking” coexist with reliable in-order delivery? | Reliable data may block later bytes within one ordered channel | Clarify whether independent channels suffice or ordering can be relaxed |
| How should the HTTP UI milestone work with raw sockets and no HTTP frameworks? | It may be a custom raw-socket HTTP server, but the boundary is unstated | Instructor clarification if it affects implementation |
| Can the old guide's Reliability pair remain assigned? | Names were previously in the Google Doc, but the roster may have changed | Keep names TENTATIVE until the group confirms |

## Current blockers

- Exact LMS forum overwrite and matching server code are missing.
- The local VMs are powered off; guest IP, firewall, and server listener are unknown.
- Assignment 1 transport, group size, HoL scope, and exact deadline are unresolved.
- The original Google Doc remains unchanged; the connected Docs API returned 404 in the prior pass.
