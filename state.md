# PROJECT STATE

## Last Updated
Date: 2026-10-21 (Asia/Saigon; no time was recorded)

## Project Goal
Prepare CO3094 Lab 2: evidence-grounded Windows host → Ubuntu VirtualBox HTTP access using the instructor's overwritten `new_connection`, plus one explainable draft design integrating reliability, flow control, and congestion control. Preserve actual prompt evidence and a resumable project log.

## Official Requirements
Source basis: two instructor email excerpts supplied in the user's attached prompt. Their original mailbox messages and LMS forum have not been independently opened.

- **REQUIRED** — Physical host can access the HTTP server running in the VM; use the instructor-provided overwritten `new_connection`.
- **REQUIRED** — Prepare a draft design for reliability, flow control, and congestion control for a streaming application.
- **REQUIRED** — Six-person team, approximately two students per mechanism.
- **REQUIRED** — Preserve/show AI prompts and history.
- **SUPPORTED** — Steam UDP gaming networking and Google QUIC are examples for reference, not a direction to reproduce their complete protocols.
- **REQUIRED for Assignment 1 only** — Direct oral evaluation in the week containing 2026-11-17. This is not a confirmed Lab 2 deadline.
- **UNVERIFIED** — Specific VM network mode, port, Lab 2 deliverables, screenshots, transport, and whether a prototype is needed.

## Verified Sources
- User-supplied prompt includes Email A (dated 2026-10-08), Email B excerpt, and the Google Docs link.
- Google Drive Search returned the native document title, metadata, and indexed text. Direct Docs text read and Drive fetch both returned 404; native structure and editability are unverified.
- Adjacent local `MMT` bundle identifies itself as **CO3093**, not CO3094. Its Chapter 2 v9 slide 31 is a client-side netcat HTTP exercise. It is not treated as CO3094 authority.
- Oracle VirtualBox 7.2, Python socket/threading docs, RFC 9000/9002/9221, and Valve GameNetworkingSockets are linked in the technical docs; they inform proposals only.

## Current Phase
- Phase 1 Discovery: **PARTIAL** — available sources inventoried; the CO3094 folder and LMS forum are missing.
- Phase 2 Documentation audit: **PARTIAL** — full indexed text reviewed and Markdown correction prepared; original native Google Doc could not be edited/read through its content API.
- Phase 3 HTTP networking: **WAITING_FOR_SOURCE_AND_MANUAL_TEST**.
- Phase 4 Streaming design: draft proposals written; **not implemented or tested**.
- Phase 5 Repository handoff: local repo created and staged diff inspected; GitHub private repo not created yet.

## Completed Tasks
- Read the full attached master prompt and RTK instruction file.
- Queried Drive by the exact guide title and reviewed its returned text.
- Confirmed native Docs text read and Drive fetch return 404; no unsafe write was attempted.
- Verified the supplied CO3094 path is absent; inspected only the adjacent CO3093 MMT bundle.
- Extracted Chapter 2 v9 PDF page 31 and confirmed its netcat client exercise.
- Searched the adjacent MMT bundle for Python files; none were found. Lab 1/2 PDF searches found no `new_connection` or `22236`.
- Checked GitHub CLI authentication, Git availability, and VBoxManage (not found in PATH).
- Created requirements, source inventory, Google Doc review, corrected Markdown guide, network setup/test instructions, and integrated streaming design drafts.
- Copied the attached master prompt byte-for-byte and verified source/destination are both 30257 bytes and identical.
- Checked 20 Markdown files for broken relative `.md` links; none were found.
- Initialized Git only inside the new project folder.

## In Progress
- Create and push the private GitHub repository; then record the verified remote, branch, and commit.
- Obtain correct course sources and perform real VM validation when available.

## Pending Tasks
- Locate the actual CO3094/L07 source folder.
- Obtain the instructor's exact forum `new_connection` implementation and matching `server.py`.
- Verify function signature, accept order, thread arguments, bind address, and port from that source.
- Configure VM networking and execute host-side TCP and browser checks.
- Confirm team members and final feature pairs.
- Export the full Codex conversation/history privately and complete a privacy pass before any upload.
- Ask the instructor about unresolved protocol and deliverable requirements.

## Blockers
- The environment-provided path containing `05. HKI_NAM3\Mạng máy tính (TN) ... [L07]` does not exist. The nearby available directory is `05. HK1_NAM3\MMT`, whose course file says CO3093.
- LMS forum and the instructor's overwritten function are unavailable in the accessible sources.
- `VBoxManage` is not on PATH; no VirtualBox GUI/VM validation was run.
- Google Docs native API returns 404 for read/fetch, so the original Doc could not safely be edited through the connected tool.

## Important Decisions
- Keep instructor requirements distinct from proposals.
- Do not treat CO3093 materials as CO3094 requirements.
- Recommend Host-only for a local host↔guest demo; add NAT only if the guest needs Internet. Bridged networking is a fallback subject to LAN policy.
- Do not invent the instructor's code, port, test results, screenshots, or member assignments.
- Keep the original prompt private and verbatim; the full conversation export is not yet available.

## Environment & Commands
- Windows PowerShell; every shell command is prefixed with `rtk`.
- Git 2.50.0.windows.1 is available.
- GitHub CLI is authenticated to `TiKyisme` with repo scope.
- `VBoxManage` is not found in PATH.
- Project folder: `D:\01. Dai_Hoc_Dai_Dai_Di\05. HK1_NAM3\co3094-lab2-network-streaming`.
- Adjacent source bundle: `D:\01. Dai_Hoc_Dai_Dai_Di\05. HK1_NAM3\MMT`.

## GitHub Status
- Repo: not created yet
- Local branch: main (no commit yet)
- Remote: none
- Last commit: none

## Important File Paths
- [README](README.md)
- [log](log.txt)
- [requirements](docs/requirements-matrix.md)
- [source inventory](docs/source-inventory.md)
- [Google Docs review](docs/docs-review.md)
- [network setup](docs/network-setup.md)
- [streaming design](docs/streaming-architecture.md)
- [prompt evidence](prompts/prompt-history.md)

## Next 3 Actions
1. Commit the reviewed local file set and create the private GitHub repository.
2. Obtain the correct CO3094 folder and instructor forum code.
3. Run the documented Windows↔Ubuntu manual checks and attach real results.

## Resume Instructions
Read this file, README, and the end of log first. Confirm Git status and source paths. Continue only from evidence in the correct CO3094 materials. Keep proposals marked as proposals and update state/log after each milestone.
