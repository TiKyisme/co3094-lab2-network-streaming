# Open questions

| Question | Why it matters | Evidence needed |
|---|---|---|
| What is the correct CO3094/L07 workspace path? | Supplied path is absent; the reachable nearby bundle is CO3093 | User reopens/supplies the exact CO3094 folder |
| What is the exact forum post and overwritten `new_connection` code? | Needed for signature, argument order, socket lifetime and server behavior | Copy/export the LMS post and matching server source |
| What is the matching `server.py`, port and bind address? | Required for accurate commands and source review | Correct CO3094 source file |
| Is VM networking mode fixed by the instructor? | Host-only, NAT forwarding and bridged have different reachability | Current Lab 2/LMS instruction |
| Must the three mechanisms be implemented as code? | Email B says “draft design” but does not specify prototype scope | Instructor clarification if it changes workload |
| Must the application use UDP, QUIC, or another transport? | Email lists examples but no mandated protocol | Instructor clarification |
| What files or evidence must be shown at Lab 2? | Email does not list a report, screenshot or repository deliverable | LMS announcement or instructor clarification |
| Is the Assignment 1 oral week separate from the Lab 2 due date? | Avoids misusing the Assignment 1 date | Current Lab 2 calendar |
| Are prior-draft Reliability names the correct current team members? | Existing guide names one pair while leaving others blank | Group roster confirmation |
| Can the connected account edit the Google Doc? | Search returned text, but Docs API and Drive fetch returned 404 | Owner opens/shares the same Doc with the connected account |
| Does the VM have Host-only DHCP and an allowed guest firewall rule? | Needed for a real host↔guest request | VirtualBox GUI and Ubuntu checks |

## Current blockers

- LMS forum and exact code are unavailable.
- Correct CO3094/L07 folder is unavailable.
- `VBoxManage` is not on PATH; no VM/GUI check was run.
- Google Docs native read/edit API returns 404. Markdown review and revised copy are available.
