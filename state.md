# PROJECT STATE

## Last Updated
Date: 2026-10-22 (Asia/Saigon; no time was recorded)

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

## Verified Teaching Slides Used for the Group Report
- Technical lecture source: `Chapter 3_ Transport Layer - Chapter_3_v9.0.pptx` from the CO3093 L02/L03 course collection; 154 slides; SHA-256 `0d30baf63053f753be037a81fc23604c7148ddcf55ff9c650920e28f0c4c2379`.
- Matching lecture PDF: `Chapter 3 Transport - Mux_Demux, RDT- reilable data transfer - Chapter_3_v9.0.pdf`; 154 pages; SHA-256 `1600eaaf85f9a2e95f4eae2ae5a5e4606206c7fd6d076b2b6d19dd9ea572f4f4`. PDF page numbers match the printed lecture slide numbers in the inspected pages.
- Reliability evidence: slides 45, 47-48, 53, 56-64, 66-67. Flow Control: slides 93-98, especially 97. Congestion Control: slides 108, 112-120, 122-126.
- The CO3094/L07 study pack did not contain a separate Transport Layer lecture deck. The report labels the available CO3093 deck accurately and leaves its suitability for this Lab 2 to Gia Đạo and Thiên Kỳ to confirm.

## Environment Discovery (initial read 2026-10-21)
- Windows 11 build 10.0.26200; Python 3.14.4 x64.
- VirtualBox 7.2.20r175154 is installed; GUI is installed but not running.
- Registered `ubuntu` VM is Ubuntu 64-bit and powered off; Adapter 1 is Bridged to Wi-Fi, adapters 2–8 disabled.
- `NetApp-EndHost` is also registered and powered off.
- Host-only interface is Up at 192.168.56.1/24; VirtualBox DHCP server is enabled with guest range 192.168.56.101–192.168.56.254.
- Guest IP, guest firewall, and server listener are unknown because guests are off.
- No VM settings were changed during that initial read; no TCP, curl, browser, or HTTP test was run then.

### Rechecked during HTTP/DNS form execution (2026-10-22)
- VirtualBox 7.2.20r175154: `ubuntu` remains configured as Ubuntu 64-bit, Adapter 1 Bridged to Intel Wi-Fi 6 AX203, adapters 2–8 disabled. A headless boot attempt failed at BIOS with `No bootable medium found`; the VM was powered off afterward. No guest IP was available.
- `NetApp-EndHost` was running and bridged to the same Wi-Fi. Guest-reported OS is TinyCore Linux 10.1; `eth0` is `192.168.111.61/24`; Python versions are 3.6.4 and 2.7.14. Windows Wi-Fi was `192.168.111.188/24`.
- No `ufw`, `iptables`, or `nft` command was present in the TinyCore guest, and `/proc/net/ip_tables_names` was unavailable. Actual incoming TCP 8000 and UDP 53 requests succeeded; no firewall or VirtualBox network setting was changed.
- Form HTTP and DNS tests below were run on `NetApp-EndHost`; they are not Ubuntu VM or instructor-server port-22236 test results.

## Current Phase
- Phase 1B Source Recovery: **PARTIAL** — CO3094/L07 package and forum overwrite/settings verified; the linked complete server source is unavailable.
- Phase 2 Team handover: **READY FOR LOCAL TEAM START** — main Vietnamese guide, short handover, six detailed task cards, announcement, checklist, prompt instructions and a visually reviewed Word fallback exist. Exact Google Docs read returned 404; sync is pending.
- Phase 3 HTTP environment: **PARTIAL**. A separate form HTTP demo passed from Windows to `NetApp-EndHost` at TCP 8000, including curl and Edge button interaction. The named Ubuntu VM fails BIOS boot; the official/forum server and port 22236 remain untested.
- HTTP/DNS Google Form exercises: **PASS ON `NetApp-EndHost`**. UDP DNS port 53 answered Windows `nslookup` for `www.example.com`; packet validation confirmed transaction ID `0xC309` and an A/IN record for demo address `192.0.2.123`. Screenshots are ready locally and excluded from Git due the private lab IP.
- Phase 4 Streaming: three design proposals exist; **not implemented or experimentally evaluated**, and not confirmed Assignment 1-compliant. The CO3094 group report has been cleaned for submission and reduced to 9 pages. The project record retains the source note that its Transport Layer lecture material is from the CO3093 L02/L03 collection.
- Phase 5 Repository: public GitHub repo; handover remains on main. Reliability review is on feat/reliability-lab2-draft in open draft PR #1; no merge or student approval is recorded.

## Session Status Fields

```text
TEAM_HANDOVER_STATUS: READY_FOR_LOCAL_TEAM_START
TEAM_HANDOVER_READY: YES (local fallback package; Google Docs sync pending)
GOOGLE_DOC_STATUS: GOOGLE_DOC_SYNC_PENDING (exact-ID metadata and native text reads returned 404)
HTTP_FORM_DEMO_STATUS: PASS on NetApp-EndHost TinyCore 10.1 / 192.168.111.61:8000; NOT TESTED on the VM named ubuntu or instructor server port 22236
HTTP_FORM_SCREENSHOT: READY at evidence/http-form.png (21,934 bytes; local-only)
DNS_DEMO_STATUS: PASS on NetApp-EndHost TinyCore 10.1 / 192.168.111.61:53/UDP; demo A answer 192.0.2.123
DNS_NSLOOKUP_SCREENSHOT: READY at evidence/dns-nslookup.png (26,129 bytes; local-only)
STREAMING_DESIGN_STATUS: PROPOSED_NOT_REVIEWED_BY_PAIRS
GROUP_ROSTER_STATUS: 6 member names supplied; IDs missing for Hà Duy Lộc, Lê Thành Tiến, and Nguyễn Tuấn Anh; group number not supplied
PROMPT_EVIDENCE_STATUS: latest HTTP/DNS task prompt saved in prompts/2026-10-22-http-dns-form-submission.txt and indexed in prompt-history.md; earlier task prompts retained
RELIABILITY_DRAFT_STATUS: SLIDE_ONLY_DRAFT_READY; TECHNICAL_REVIEW_PENDING; TEAM_DECISION_PENDING
RELIABILITY_NEXT_ACTION: Gia Đạo and Thiên Kỳ review the slide-only draft and report; confirm the CO3093 slide source, RDT 3.0 choice, sequence-label mapping, timeout example, and scope; keep all review boxes unchecked
STREAMING_REPORT_STATUS: SUBMISSION_CLEANED; LaTeX/PDF 9 pages; visual and text checks passed; personal student review pending
NEXT_ACTION: Gia Đạo and Thiên Kỳ review the final report and Reliability design; to repeat the form tests on the exact Ubuntu guest, provide a bootable Ubuntu VM/media or confirm that NetApp-EndHost is acceptable; do not change VirtualBox networking without approval
```

## Latest Report Deliverable — 2026-10-22
- Created `report/co3094_lab2_report.tex`, `report/graphics/hcmut.png`, and `output/pdf/co3094_lab2_report.pdf` for Reliability, Flow Control, and Congestion Control.
- Report figures: one overview, two Reliability cases, one TCP `rwnd` flow-control diagram, and one AIMD congestion-control graph. Group examples and proposed choices are labeled; the RDT 3.0 bit alternation (0/1) is distinguished from the user-requested example labels (1/2/3).
- Compiled twice with XeLaTeX/MiKTeX; final cleaned PDF is 9 pages, 198,865 bytes, SHA-256 `4230fb3fe25a947bccfb54397ad543c2ca645378be3a862c4f3e7406c4142f2d`. All pages were rendered and visually inspected; final runs reported no overfull/underfull layout warnings.
- Removed internal preparation notes from the PDF, added the six supplied member names and three supplied IDs, and kept an em dash where three IDs were not provided. Extracted-text search found none of the specified internal-process terms; all five figures, contents, and references were present.
- The report does not claim that the HTTP VM demo or any mechanism was implemented or experimentally evaluated. No personal student review or approval is recorded.

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
- Completed the Reliability final correction pass: distinguished the custom count of three later ACKed ack-eliciting packets from RFC 9002's raw PN-distance condition with a worked PN 100-103 comparison; added scheduled `loss_time` re-evaluation, single-timer precedence over PTO, and the rule that PTO alone never declares loss.
- Replaced the presentation's lost-ACK diagram with a prominent loss-recovery sequence showing PN 100 loss, the custom threshold, retransmission of bytes 0-99 under PN 106, ACK, and one receiver delivery. Cross-checked the detailed design, presentation, oral preparation, and interface review.
- Mermaid CLI 12.0.0 rendered all five detailed-design diagrams and both presentation diagrams; all seven rendered successfully, and the updated loss-recovery diagrams were visually inspected.
- Regenerated the presentation PDF and visually inspected both rendered pages. It remains two pages; final PDF SHA-256 is `1c2e3918802c4b24978afca135f4c2b88c445ac1b88ef9c6738d34a40b46dc4d`.
- Saved this exact user correction prompt in `prompts/2026-10-21-reliability-final-correction.txt` (2,235 bytes; SHA-256 `3530ec029a0939f57d6c8604f7aeb74ed200b548bc232031e61a358416995620`). No student-review checkbox was checked; no protocol code or network test was added or run.
- Located the original CO3093 Chapter 3 lecture deck in the course folder. The source-pack index identifies Chapter 3_ Transport Layer - Chapter_3_v9.0.pptx as slide source src_7d0e4bf812cb; the actual deck has 154 slides. Read slides 45, 47-48, 53, 56-64, and 66-67; visually inspected the corresponding lecture PDF pages.
- Cross-checked the available user-supplied Email A/B excerpts recorded in docs/requirements-matrix.md: Lab 2 requires draft designs for Reliability, Flow Control, and Congestion Control; QUIC/Steam are examples; implementation is not required by those excerpts.
- Added docs/reliability-slide-only.md and docs/reliability-easy-study.md; simplified docs/reliability-lab2-presentation.md to RDT 3.0 stop-and-wait. Preserved docs/reliability-design.md as the earlier advanced draft and left Flow Control/Congestion Control documents unchanged.
- Mermaid CLI rendered the slide-only design and presentation diagrams successfully. Regenerated the two-page presentation PDF (124,874 bytes) and visually inspected both pages; SHA-256 is e8bcbd9d2e6ac7bd2088726bf66836419ab8ae4b97b2b9572d27f1ff013104ca.
- Saved the current user prompt in prompts/2026-10-22-reliability-slide-only.txt (6,176 bytes; SHA-256 8a1becfaf94abe12afc0f11f2ddab2ebecf86f8b110a01e32c6829ef1464b749). Existing student-review checkboxes remain unchecked; no implementation or network tests were run.

## Waiting / Pending
- Gia Đạo and Thiên Kỳ review the slide-only RDT 3.0 proposal, stop-and-wait suitability, timeout choice, direction scope, and pair roles; no student confirmations are recorded.
- The earlier advanced Reliability design remains preserved and unapproved; it is not the current easier-to-present candidate.
- Complete forum-linked `sample_code_http_server_process.txt` or matching server source, including the accept/thread call that must match `new_connection(conn, addr)`.
- The task-named `ubuntu` VM cannot boot (`No bootable medium found`); the separate form demos passed on `NetApp-EndHost`, so an exact Ubuntu-guest rerun remains pending.
- Confirm the Reliability pair and fill the other four names; assign HTTP primary/backup.
- Re-review the AI-proposed designs with their pairs and add actual prompt evidence.
- Restore access to the original Google Doc or provide the missing Word copy if it contains changes beyond the previously reviewed text; then sync the local fallback without creating a duplicate.
- Clarify Assignment 1 transport, group size, HoL expectations and exact deadline.
- Export the full conversation privately and inspect it before any upload.

## Blockers
- The ZIP contains a sample server image in a PDF but no standalone Python server/client or OVA. The forum override is confirmed in the supplied PDF, but its linked complete server attachment is unavailable without LMS authentication.
- The named `ubuntu` VM cannot boot and has no guest IP. `NetApp-EndHost` test state is recorded above; do not use it as evidence for the official forum server.
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
- The submission report lists the six names supplied by the user. It does not invent IDs for Hà Duy Lộc, Lê Thành Tiến, or Nguyễn Tuấn Anh and does not infer a group number.

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
- Reliability slide-only content commit: f0fc4abe07a45b2c7288301b1de11cffba1d9396 (pushed; origin ref verified; state/log push evidence is recorded separately)
- CO3094 group report content commit: `5733f1fa174f94012cd2e153ddef100772f6a0de` (pushed to `origin/feat/reliability-lab2-draft`; `git ls-remote` matched). PR #1 readback after push: OPEN / DRAFT / NOT MERGED; no student approval recorded.
- HTTP + DNS form execution commit: `96c4d43e6b397c8ffa9785da6b1a5e524fe5349c` (pushed to `origin/feat/reliability-lab2-draft`; remote OID matched). PR #1 remains OPEN / DRAFT / NOT MERGED; no student approval recorded.
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
- [Slide-only Reliability draft](docs/reliability-slide-only.md) and [easy study guide](docs/reliability-easy-study.md)
- [CO3094 Lab 2 LaTeX group report](report/co3094_lab2_report.tex) and [compiled PDF](output/pdf/co3094_lab2_report.pdf)
- [prompt history](prompts/prompt-history.md)

## Next 3 Actions
1. Gia Đạo and Thiên Kỳ personally review the cleaned report and Reliability design; confirm the RDT 3.0 sequence-label explanation and 100 ms example.
2. Provide a bootable Ubuntu guest or confirm `NetApp-EndHost` is acceptable if the form task must be repeated on Ubuntu; no network-setting change is needed for the current TinyCore results.
3. Obtain the linked full server attachment and ask the instructor about Assignment 1 conflicts when available.

## Resume Instructions
Read this file, README, and the end of log first. Check Git status, branch, remote and HEAD. Keep original course sources outside Git. Do not treat the Sample NetApp PDF code as the forum overwrite. Do not mark tests passed without real outputs.

## Latest HTTP + DNS Form Execution — 2026-10-22

- Read the supplied Lab 2 LMS PDF directly: pages 2–4 contain the UDP/DNS sample and DNS A-response structure; page 9 shows the textbox/button/label HTML requirement.
- Added separate standard-library socket demos: `examples/http_server_form.py` and `examples/dns_udp_server.py`, plus `docs/http-dns-form-runbook.md`. The instructor's source and `examples/http_server_reconstructed_demo.py` were not modified.
- Real test guest: `NetApp-EndHost`, TinyCore Linux 10.1, Python 3.6.4, `eth0` `192.168.111.61/24`; Bridged to Wi-Fi. The host was `192.168.111.188/24`. This was not the VM named `ubuntu`.
- HTTP: port 8000 reachable from Windows; `Test-NetConnection` succeeded; `curl.exe` received HTTP 200 with the form HTML; Edge loaded the page, filled the textbox, clicked the button and read label `Welcome, CO3094 Student!`.
- DNS: UDP 53 bound with `sudo -n`; Windows `nslookup www.example.com 192.168.111.61` returned `192.0.2.123`. The server logged real queries including ID `0xc309`; a wire check validated matching ID, QR/AA flags, one compressed-owner A/IN record, TTL 60 and 4-byte address data.
- `192.0.2.123` is a documentation-only demonstration address, not a claim about the public DNS address of `www.example.com`.
- Guest firewall inspection found no `ufw`, `iptables`, or `nft` utility and no readable `/proc/net/ip_tables_names`; both observed inbound tests succeeded. No firewall rule or VirtualBox network setting was changed.
- The VM named `ubuntu` was started once for this task, but BIOS reported `No bootable medium found`; it was powered off without changing settings. Exact-guest Ubuntu validation and the forum/instructor server on port 22236 remain NOT TESTED.
- Screenshots: `evidence/http-form.png` (21,934 bytes) and `evidence/dns-nslookup.png` (26,129 bytes). Both are real captures, under 1 MB, kept local and ignored by Git because the DNS image shows the private lab IP.
- Exact task prompt is saved in `prompts/2026-10-22-http-dns-form-submission.txt` and indexed in `prompts/prompt-history.md`.
