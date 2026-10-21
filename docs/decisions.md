# Decisions and rationale

| ID | Decision | Classification | Rationale / revisit when |
|---|---|---|---|
| D-01 | Use user-supplied instructor email excerpts as the highest available requirement source; mark LMS/forum evidence missing | Evidence policy | Prompt ranks sources this way; revisit when original LMS post is supplied |
| D-02 | Keep repository separate from the broad course bundle | REQUIRED | Avoid accidentally committing copyrighted course files |
| D-03 | Keep GitHub repository private by default | REQUIRED | Prompt history and course context are not public artifacts |
| D-04 | Treat reachable `MMT` files as CO3093 background, not CO3094 authority | Evidence boundary | Its course text explicitly says CO3093 |
| D-05 | Recommend Host-only for a same-machine host↔guest demo; add NAT only if guest needs Internet | PROPOSED | Oracle manual describes Host-only as host↔guest without external access |
| D-06 | Do not recreate or guess the instructor's `new_connection` | REQUIRED | Exact code is not available |
| D-07 | Draft two delivery classes: reliable ordered control and expiring unreliable real-time updates | PROPOSED | Gives one integrated workload for the three mechanisms |
| D-08 | Use a NewReno-like AIMD controller with pacing as the design baseline | PROPOSED | RFC 9002 offers a teachable reference, not a required implementation |
| D-09 | Preserve the exact attached prompt in private evidence; keep full session export out until privacy-reviewed | REQUIRED / privacy | Prompt history is required; no full export has been generated |
