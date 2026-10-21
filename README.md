# CO3094 Lab 2 — HTTP Networking & Streaming Design

Private working repository for evidence-grounded Lab 2 preparation and future Assignment 1 comparison. Original course ZIP/PDF/OVA files are not in Git.

## Confirmed Lab 2 scope from instructor emails

- Physical host accesses the VM's HTTP server using the forum-overwritten `new_connection`.
- Draft designs are needed for Reliability, Flow Control and Congestion Control.
- The Lab 2 design team has six members, approximately two per feature.
- AI prompt/history evidence must be preserved.
- Assignment 1 oral evaluation is in the week containing 17 November 2026; it is not a Lab 2 deadline.

The exact forum function remains missing. Assignment 1 source conflicts are recorded separately and do not replace Lab 2 email requirements.

## Current status

- Phase 1B: CO3094/L07 package identity, Assignment 1 PDF and CO3094 Lab 1 sources verified. Assignment 1's transport/group/deadline inconsistencies remain unresolved.
- Phase 2: Google Doc text review and Markdown replacement are complete; native Docs edit remains unavailable through the connected API.
- Phase 3: Windows/VirtualBox discovered. The Ubuntu VM is off and bridged; no guest IP, server listener or connection test has been observed.
- Phase 4: streaming design remains a Lab 2 proposal. Assignment 1 compliance is not claimed.
- Phase 5: repository is private at [GitHub](https://github.com/TiKyisme/co3094-lab2-network-streaming), branch `main`.

## Key documents

- [Project state](state.md) and [append-only log](log.txt)
- [Requirements and conflict matrix](docs/requirements-matrix.md)
- [Source inventory](docs/source-inventory.md)
- [Guide review](docs/docs-review.md) and [corrected Lab 2 guide](docs/lab2-group-guide.md)
- [HTTP source analysis](docs/http-server-analysis.md), [network setup](docs/network-setup.md), [test cases](docs/network-test-cases.md)
- [Streaming architecture](docs/streaming-architecture.md) and component design docs
- [Tentative team assignments](docs/team-assignments.md), [open questions](docs/open-questions.md)
- [Prompt history](prompts/prompt-history.md)

## Running the HTTP demo

No run command is approved yet. Sample_NetApp PDF page 7 is a TCP accept/print skeleton, not an HTTP responder; the forum-overwritten function and matching server are required first. The sample page's port 22236 is not confirmed for the forum version.

## Resume

Read README, state, and the end of log; verify Git status/HEAD. Then inspect the exact forum post and matching server source before guiding any VM changes. Keep each Assignment 1 contradiction unresolved until an authoritative clarification arrives.
