# Network test cases

**Overall status: WAITING_FOR_MATCHING_SERVER_SOURCE_AND_MANUAL_TEST.** The forum PDF contains a historical instructor demonstration; no VirtualBox VM or GUI test of the current local environment was run.

## Historical course demonstration (not a current test pass)

The supplied LMS PDF p. 3 shows command-prompt output with `HTTP/1.1 200 OK` and a browser-rendered welcome page at `192.168.56.103:22236`. The text above the screenshot instead names `192.168.56.100:22236`. Treat this as historical course evidence only; it does not establish the current VM, network mode, or server state.

| ID | Test | Procedure | Expected result | Status |
|---|---|---|---|---|
| NET-01 | Guest interface | In Ubuntu run `ip -4 addr`; record the Host-only NIC and IPv4 | A real address on the selected Host-only subnet | NOT RUN |
| NET-02 | Server listener | Run the matching server source; inspect startup/log and bind/port | Listener is active on the reachable interface and actual source port | BLOCKED: linked `sample_code_http_server_process.txt` server source is unavailable; forum handler is confirmed, Sample NetApp skeleton has incompatible argument order |
| NET-03 | TCP reachability | Windows: `Test-NetConnection <VM_IP> -Port <PORT>` | `TcpTestSucceeded : True` | NOT RUN |
| NET-04 | HTTP response | Browser: `http://<VM_IP>:<PORT>/`; optionally `curl.exe -v` | Valid HTTP status/headers/body; server logs the request | NOT RUN |
| NET-05 | Refresh/repeat | Reload browser or repeat GET | A second request is logged and response remains valid | NOT RUN |
| NET-06 | Wrong port negative control | Test a confirmed unused port | TCP check fails; do not mistake this for a server defect | NOT RUN |
| NET-07 | Server stopped negative control | Stop server and retry the correct port | Refused/failed connection; restart server before proceeding | NOT RUN |
| NET-08 | NAT forwarding alternative | Only if using NAT: test host port mapped to guest service port | Host-side forwarding reaches the guest listener | NOT RUN |

## Evidence to capture after a real test

- Date/time and host OS/Ubuntu VM version.
- VirtualBox version and adapter mode(s).
- Guest interface name, IP, subnet, and actual server port.
- Exact server source revision/hash and run command.
- Full PowerShell test output.
- Browser URL and HTTP result.
- Relevant Ubuntu server log.
- Any firewall change, if a narrow rule was needed.
- Privacy review before placing evidence in GitHub.

Telnet is optional unless a current instructor instruction requires it. It can help inspect raw HTTP, but it is not proof that the browser flow works.
