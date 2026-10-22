# CO3094 Lab 2 — HTTP Networking & Streaming Design

Working repository for evidence-grounded Lab 2 preparation and future Assignment 1 comparison. Original course ZIP/PDF/OVA files are not in Git.

## Confirmed Lab 2 scope from instructor emails

- Physical host accesses the VM's HTTP server using the forum-overwritten `new_connection`.
- Draft designs are needed for Reliability, Flow Control and Congestion Control.
- The Lab 2 design team has six members, approximately two per feature.
- AI prompt/history evidence must be preserved.
- Assignment 1 oral evaluation is in the week containing 17 November 2026; it is not a Lab 2 deadline.

The Lab 1 LMS export confirms the overwritten HTTP handler and its listener settings. The linked complete server-process attachment is not available locally yet. Assignment 1 source conflicts are recorded separately and do not replace Lab 2 email requirements.

## START HERE — LAB 2 TEAM MEMBERS

Use the **local team guide as the current handover**. The original Google Docs link is kept here, but its native read returned 404 for the connected account; no duplicate Google Doc was created. `GOOGLE_DOC_SYNC_PENDING`.

- [Google Docs original](https://docs.google.com/document/d/1hxqLAD0eRfdBhDJJyopSYi0vFqJUDhFCy7lOGO2CxQ/edit) — sync pending
- [Main Lab 2 guide](docs/lab2-group-guide.md)
- [Word fallback for the main guide](docs/lab2-group-guide.docx) — upload manually if Google Docs remains unavailable
- [Short team handover](docs/team-handover.md)
- [Six member task cards and progress board](docs/team-assignments.md)
- [Draft team announcement](docs/team-announcement.md)
- [Windows to Ubuntu network setup](docs/network-setup.md)
- [Streaming design overview](docs/streaming-architecture.md)
- [Prompt evidence instructions](docs/prompt-evidence-instructions.md)
- [Team review checklist](docs/team-review-checklist.md)

## Current status

- Phase 1B: CO3094/L07 package identity, Assignment 1 and Lab 1 sources verified. The Lab 1 forum export confirms the HTTP handler, bind address and port; Assignment 1's transport/group/deadline inconsistencies remain unresolved.
- Phase 2: the prior full-text Google Doc review is recorded in `docs/docs-review.md`; the supplied Word copy was not found, and the exact native Doc now returns 404. The local Markdown guide, task cards, announcement, checklist and rendered Word fallback are ready; Google Docs sync is pending.
- Phase 3: Windows/VirtualBox discovered. The Ubuntu VM is off and bridged; no guest IP, current server listener or connection test has been observed. A separately labeled group-reconstructed demo candidate is syntax-checked only.
- Phase 4: Reliability, Flow Control and Congestion Control remain AI proposals awaiting pair review. The Reliability draft is complete as a review package on a feature branch; student and team decisions are still pending. Assignment 1 compliance is not claimed.
- Phase 5: repository is public at [GitHub](https://github.com/TiKyisme/co3094-lab2-network-streaming); the handover remains on main and Reliability review is in [draft PR #1](https://github.com/TiKyisme/co3094-lab2-network-streaming/pull/1).

## Key documents

- [Project state](state.md) and [append-only log](log.txt)
- [Requirements and conflict matrix](docs/requirements-matrix.md)
- [Source inventory](docs/source-inventory.md)
- [Guide review](docs/docs-review.md) and [corrected Lab 2 guide](docs/lab2-group-guide.md)
- [HTTP source analysis](docs/http-server-analysis.md), [network setup](docs/network-setup.md), [test cases](docs/network-test-cases.md)
- [Streaming architecture](docs/streaming-architecture.md) and component design docs
- [Reliability design draft](docs/reliability-design.md), [short presentation](docs/reliability-lab2-presentation.md), [oral preparation](docs/reliability-oral-preparation.md), and [pair-interface review](docs/reliability-interface-review.md)
- [Reliability presentation PDF](output/pdf/reliability-lab2-presentation.pdf) - two-page rendered copy of the short presentation
- [Tentative team assignments](docs/team-assignments.md), [open questions](docs/open-questions.md)
- [Prompt history](prompts/prompt-history.md)

## Running the HTTP demo

The forum export confirms `hostip = "0.0.0.0"`, port `22236`, and a `new_connection(conn, addr)` HTTP handler. `examples/http_server_reconstructed_demo.py` is a local group reconstruction from that visible handler and the old skeleton, not the complete instructor source. It has not been run on the Ubuntu VM. See [HTTP source analysis](docs/http-server-analysis.md) and [network test cases](docs/network-test-cases.md).

## Resume

Read README, state, and the end of log; verify Git status/HEAD. Confirm member names and HTTP owners. Obtain the linked server attachment or, if unavailable, keep the group reconstruction labeled as such and guide the real VM checks. Keep each Assignment 1 contradiction unresolved until an authoritative clarification arrives.
