# PROJECT STATE

## Last Updated
Date: 2026-10-21 (Asia/Saigon; no time was recorded)

## Project Goal
Prepare CO3094 Lab 2: Windows physical host → Ubuntu VirtualBox HTTP access using the instructor's forum-overwritten `new_connection`, plus explainable draft designs for Reliability, Flow Control and Congestion Control. Preserve actual AI prompt evidence and a resumable project history.

## Instructor Requirements — Lab 2
Source basis: Email A and Email B excerpts supplied by the user. Original mailbox messages and the live LMS forum have not been independently opened.

- **REQUIRED** — Physical host accesses HTTP server in VM using the instructor's overwritten `new_connection`.
- **REQUIRED** — Draft design for reliability, flow control and congestion control.
- **REQUIRED** — Six-person Lab 2 design group, approximately two students per feature.
- **REQUIRED** — Preserve/show AI prompt history.
- **SUPPORTED** — Steam UDP gaming and Google QUIC are examples, not mandates to reproduce full protocols.
- **REQUIRED for Assignment 1 only** — Oral evaluation in the week containing 2026-11-17; this is not a Lab 2 deadline.
- **CONFIRMED from the user-supplied Lab 1 forum PDF** — Handler signature `new_connection(conn, addr)`, listener IP `0.0.0.0`, and port `22236`.
- **UNVERIFIED** — Complete linked server-process source, current Lab 2 topology, deliverables and prototype requirement.

## Verified CO3094 Sources
- User-supplied handoff file and ZIP are present beside the verified CO3094/L07 course folder. `00_START_HERE.md` confirms identity; `03_SOURCE_INDEX.md` provides stable IDs.
- Assignment 1 PDF `src_076bd2c18b0d`, pp. 1–4, was read directly from the ZIP.
- CO3094 Lab 1 PDF `src_bb5408286b99`, pp. 1–8, was read directly from the ZIP.
- Sample NetApp PDF `src_b850d73292a7`, pp. 7–8, was rendered and visually inspected. Page 7 shows a sample TCP accept/print server, not an HTTP responder or confirmed forum overwrite.
- User-supplied LMS PDF export “Lab 1 - Network device and Network application,” pp. 1–3, was text- and visually inspected. It confirms forum listener settings, the overwritten HTTP handler, and a historical instructor-posted HTTP 200/browser demo.
- The linked `sample_code_http_server_process.txt` attachment redirects to BK-LMS login without a session and was not found in the inspected local source/repo/download/attachment folders. Its server loop and thread argument order remain unavailable.
- The forum handler expects `(conn, addr)`, while the separate Sample NetApp skeleton passes `(addr, conn)`; the sample call cannot be reused unchanged.
- The historical screenshot shows `192.168.56.103:22236`, but the text above it says `192.168.56.100:22236`; neither is treated as the current guest IP.
- ZIP integrity check found no bad member; it has 325 entries and no standalone `.py` or `.ova` members. The relevant PDF hashes match the extracted copies.
- Assignment 1 transport, group-size, HoL and deadline conflicts are in docs/requirements-matrix.md. They remain unresolved and do not replace Lab 2 email requirements.
- The forum-overwritten `new_connection` and its listener settings are confirmed; the complete linked server file remains unavailable.

## Environment Discovery
- Windows 11 build 10.0.26200; Python 3.14.4 x64.
- VirtualBox 7.2.20r175154 is installed; GUI is installed but not running.
- Registered `ubuntu` VM is Ubuntu 64-bit and powered off; Adapter 1 is Bridged to Wi-Fi, adapters 2–8 disabled.
- `NetApp-EndHost` is also registered and powered off.
- Host-only interface is Up at 192.168.56.1/24; VirtualBox DHCP server is enabled with guest range 192.168.56.101–192.168.56.254.
- Guest IP, guest firewall, and server listener are unknown because guests are off.
- No VM settings were changed. No TCP, curl, browser, or HTTP test was run.

## Current Phase
- Phase 1B Source Recovery: **PARTIAL** — CO3094/L07 package and forum overwrite/settings verified; the linked complete server source is unavailable.
- Phase 2 Team handover: **READY FOR LOCAL TEAM START** — main Vietnamese guide, short handover, six detailed task cards, announcement, checklist, prompt instructions and a visually reviewed Word fallback exist. Exact Google Docs read returned 404; sync is pending.
- Phase 3 HTTP environment: **WAITING_FOR_MANUAL_TEST**. Forum settings and local reconstruction are documented; syntax is checked only. The VM is off and no TCP/HTTP/browser test has been run.
- Phase 4 Streaming: draft proposals exist; **not reviewed by the pairs, not implemented/tested**, and not confirmed Assignment 1-compliant. The Reliability review package is AI_DRAFT_COMPLETE; TECHNICAL_REVIEW_PENDING and TEAM_DECISION_PENDING.
- Phase 5 Repository: public GitHub repo; handover remains on main. Reliability review is on feat/reliability-lab2-draft in open draft PR #1; no merge or student approval is recorded.

## Session Status Fields

```text
TEAM_HANDOVER_STATUS: READY_FOR_LOCAL_TEAM_START
TEAM_HANDOVER_READY: YES (local fallback package; Google Docs sync pending)
GOOGLE_DOC_STATUS: GOOGLE_DOC_SYNC_PENDING (exact-ID metadata and native text reads returned 404)
HTTP_DEMO_STATUS: WAITING_FOR_MANUAL_TEST (syntax only; VM powered off)
STREAMING_DESIGN_STATUS: PROPOSED_NOT_REVIEWED_BY_PAIRS
GROUP_ROSTER_STATUS: PARTIAL (2 tentative names, 4 placeholders, HTTP owners unassigned)
PROMPT_EVIDENCE_STATUS: latest user master prompt saved byte-identically; student prompts pending
RELIABILITY_DRAFT_STATUS: AI_DRAFT_COMPLETE; TECHNICAL_REVIEW_PENDING; TEAM_DECISION_PENDING
RELIABILITY_NEXT_ACTION: REL-01 and REL-02 review packet/ACK and recovery sections; keep every team-review box unchecked
NEXT_ACTION: REL-01 and REL-02 review the Reliability draft; VM network checks remain pending
```

## Completed Tasks
- Read the continuation prompt, previous README/state/log, requirements, source inventory, open questions, and all five streaming design docs.
- Read the user's Reliability implementation-draft prompt and saved it byte-identically in prompts/.
- Created the detailed Reliability proposal, four sequence diagrams plus a recovery state diagram, algorithms, state tables, worked cases, alternatives, interface boundaries, and a short presentation/oral review package.
- Verified RFC 9000, RFC 9002, RFC 9221, and Valve GameNetworkingSockets primary references for the technical claims used in the draft.
- Mermaid CLI 12.0.0 rendered all five detailed-design diagrams and both presentation diagrams to PNG; all seven render runs succeeded and the diagrams were visually reviewed.
- Exported the short presentation to a two-page PDF in output/pdf and visually inspected both rendered pages. The PDF contains the two key flow diagrams and direct technical-reference links.
- Read the source handoff, `00_START_HERE.md`, `03_SOURCE_INDEX.md`, Assignment 1 PDF, CO3094 Lab 1 PDF, Assignment 1 LMS note, general announcement note and Sample NetApp text.
- Inspected Assignment 1, Lab 1 and Sample NetApp PDFs from the ZIP; visually checked Sample NetApp pages 7–8.
- Inspected all pages of the user-supplied Lab 1 forum PDF. Confirmed `hostip = "0.0.0.0"`, port `22236`, `new_connection(conn, addr)`, and a historical HTTP 200/browser-rendering result. Recorded the `.100` text vs `.103` screenshot discrepancy.
- Checked the linked forum attachment without LMS authentication; it redirects to login. Searched the relevant local course, repo, Downloads, `D:\download`, `D:\TiKy`, and Codex attachment folders; no matching `server.py` or `sample_code_http_server_process.txt` was found.
- Located and read `server_skeleton_previous_upload.py`. Its `Thread(args=(conn, addr))` matches the forum handler argument order, but the handler body only prints and its host helper differs from the forum's wildcard bind instruction.
- Created `examples/http_server_reconstructed_demo.py` as a clearly labeled group reconstruction; Python AST syntax checks passed for it and the old skeleton. Neither was run on a VM.
- Built the local team handover package: complete guide, 2–3 page handover, six member task cards/progress board, announcement draft, reviewer checklist, and prompt evidence instructions.
- Created `docs/lab2-group-guide.docx` by combining the guide and detailed task cards; Word export was rendered to 17 page images and visually inspected. The supplied original Word copy was not found and was not overwritten.
- Checked the connected Google Drive profile, tried the exact original Doc ID for metadata and native text, and searched for the exact supplied DOCX title. The native reads returned 404 and the DOCX search returned no results; no duplicate Google Doc was created.
- Saved the current execution/finalization prompt byte-identically in `prompts/`; 30,226 bytes, SHA-256 `bfbead30d4206ea34cabf4439373e9583aa5b022fbde905fd7dee5667f555182`.
- Verified the ZIP has 325 entries, no bad member, no standalone `.py` or `.ova`, and that the checked extracted PDFs match the ZIP members.
- Confirmed Sample NetApp page 7 uses accept order `conn, addr`, passes thread args `(addr, conn)` to `new_connection(addr, conn)`, derives a host IP and uses sample port 22236. The handler only prints the socket.
- Discovered Windows/Python/VirtualBox/VM/Host-only/DHCP configuration read-only.
- Preserved the earlier Reliability-pair names as TENTATIVE.
- Copied the continuation prompt byte-for-byte into `prompts/`; verified both copies are 8208 bytes and identical.
- Updated requirements/conflict matrix, source inventory, guide review, HTTP analysis, network setup, open questions and A1 compatibility notes.

## Waiting / Pending
- REL-01/REL-02 technical review and cross-pair agreement on packet semantics, ACK-only congestion treatment, expiry clock, and retry cap; no student confirmations are recorded.
- Complete forum-linked `sample_code_http_server_process.txt` or matching server source, including the accept/thread call that must match `new_connection(conn, addr)`.
- Confirm whether the local `ubuntu` VM is the intended test guest.
- Start the intended Ubuntu VM; obtain guest `ip -4 addr`, then proceed to listener, Windows TCP, curl and Chrome checks.
- Confirm the Reliability pair and fill the other four names; assign HTTP primary/backup.
- Re-review the AI-proposed designs with their pairs and add actual prompt evidence.
- Restore access to the original Google Doc or provide the missing Word copy if it contains changes beyond the previously reviewed text; then sync the local fallback without creating a duplicate.
- Clarify Assignment 1 transport, group size, HoL expectations and exact deadline.
- Export the full conversation privately and inspect it before any upload.

## Blockers
- The ZIP contains a sample server image in a PDF but no standalone Python server/client or OVA. The forum override is confirmed in the supplied PDF, but its linked complete server attachment is unavailable without LMS authentication.
- The local VMs are powered off; guest IP/firewall/server state and HTTP results are unavailable.
- Google Docs sync is pending: the exact ID returned 404 under the connected account, the exact-title DOCX search returned no results, and no supplied DOCX was found in the checked local folders.
- Assignment 1 source conflicts are unresolved.
- The original Google Doc remains unchanged because its native Docs read/fetch API returned 404 in the prior pass.

## Important Decisions
- Lab 2 email requirements outrank the Assignment 1 PDF for Lab 2 scope.
- Keep Assignment 1 PDF conflicts visible; do not select a transport/group/date by assumption.
- Sample_NetApp page 7 is a separate reference skeleton, not the forum handler or HTTP responder. The user's previous skeleton matches the forum `(conn, addr)` order but is only a print stub.
- Forum source confirms listener `0.0.0.0:22236`; this does not establish the current guest IP or current listener state.
- The forum handler signature is `(conn, addr)`; do not pair it with the sample's `(addr, conn)` thread args without verifying the complete server source.
- `examples/http_server_reconstructed_demo.py` is a group reconstruction, not an authenticated copy of the instructor's full server. Syntax checks do not prove runtime behavior.
- Host-only is proposed, but do not change adapters until the linked server source and intended VM are confirmed.
- Preserve the earlier Reliability names as TENTATIVE; other names remain placeholders.

## Environment & Commands
- Windows PowerShell; all shell commands are prefixed with `rtk`.
- Git 2.50.0.windows.1; GitHub CLI authenticated as `TiKyisme`.
- VirtualBox installed at `C:\Program Files\Oracle\VirtualBox`; `VBoxManage` runs via `C:\Progra~1\Oracle\VirtualBox\VBoxManage.exe`.
- Project: `D:\01. Dai_Hoc_Dai_Dai_Di\05. HKI_NAM3\Mạng máy tính (TN) (CO3094)_NGUYỄN PHƯƠNG DUY (CQ_HK261) [L07]\co3094-lab2-network-streaming`.
- CO3094 source root: `D:\01. Dai_Hoc_Dai_Dai_Di\05. HKI_NAM3\Mạng máy tính (TN) (CO3094)_NGUYỄN PHƯƠNG DUY (CQ_HK261) [L07]`.

## GitHub Status
- Repo: [public repository](https://github.com/TiKyisme/co3094-lab2-network-streaming)
- Branch: feat/reliability-lab2-draft, tracking origin/feat/reliability-lab2-draft; draft PR #1 targets main
- Remote: `https://github.com/TiKyisme/co3094-lab2-network-streaming.git`
- Reliability content commit: 6514a17e6399307de4d704be5d4159f1ffaf2b8e (pushed; state/log handoff updates are recorded separately)
- Pull request: [#1 - Reliability Lab 2 draft](https://github.com/TiKyisme/co3094-lab2-network-streaming/pull/1), OPEN / DRAFT / NOT MERGED
- Handover package commit `10087e85a7c8d0e57995156df2f1044077cd5f94` was pushed to `origin/main`; `git ls-remote` matched at the post-push check. GitHub API readback confirmed the guide, handover, assignments, announcement, review checklist, prompt instructions and DOCX paths.
- The user-provided forum PDF, source ZIP, extracted pack and handoff are present as untracked repo-root copies. The PDF, ZIP and handoff byte-match the copies in the external course folder. They were left unchanged, unstaged and uncommitted; `git ls-files` contains no PDF or ZIP.
- `server_skeleton_previous_upload.py` remains an untracked user file. The reconstructed example and handover docs are separate files; the original skeleton is not staged.

## Important File Paths
- [README](README.md)
- [log](log.txt)
- [requirements/conflicts](docs/requirements-matrix.md)
- [source inventory](docs/source-inventory.md)
- [HTTP analysis](docs/http-server-analysis.md)
- [network setup](docs/network-setup.md)
- [streaming compatibility](docs/streaming-architecture.md)
- [Reliability draft](docs/reliability-design.md), [presentation](docs/reliability-lab2-presentation.md), [oral prep](docs/reliability-oral-preparation.md), and [interface review](docs/reliability-interface-review.md)
- [prompt history](prompts/prompt-history.md)

## Next 3 Actions
1. REL-01 and REL-02 review the Reliability draft and record real decisions and prompt evidence.
2. Start the intended Ubuntu VM and share ip -4 addr output so the HTTP network checks can proceed.
3. Obtain the linked full server attachment and ask the instructor about Assignment 1 conflicts when available.

## Resume Instructions
Read this file, README, and the end of log first. Check Git status, branch, remote and HEAD. Keep original course sources outside Git. Do not treat the Sample NetApp PDF code as the forum overwrite. Do not mark tests passed without real outputs.
