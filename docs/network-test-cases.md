# Network test cases

**Overall status: PARTIAL.** A separate HTTP form and UDP DNS demo were tested on the running course VM `NetApp-EndHost` (TinyCore Linux 10.1). The Ubuntu VM named `ubuntu` fails BIOS boot, and the instructor/forum HTTP server on port 22236 remains untested. The forum PDF's historical result is not a current test pass.

## Historical course demonstration (not a current test pass)

The supplied LMS PDF p. 3 shows command-prompt output with `HTTP/1.1 200 OK` and a browser-rendered welcome page at `192.168.56.103:22236`. The text above the screenshot instead names `192.168.56.100:22236`. Treat this as historical course evidence only; it does not establish the current VM, network mode, or server state.

| ID | Test | Procedure | Expected result | Status |
|---|---|---|---|---|
| NET-00 | Python syntax | Parse `server_skeleton_previous_upload.py` and `examples/http_server_reconstructed_demo.py` with Python AST | Both source files parse | PASS: syntax only; no server was run |
| NET-01 | Guest interface | In Ubuntu run `ip -4 addr`; record the Host-only NIC and IPv4 | A real address on the selected Host-only subnet | NOT RUN |
| NET-02 | Server listener | Run the selected instructor source or group reconstruction; inspect startup/log and bind/port | Listener is active on the reachable interface and actual source port | NOT RUN: VM is off; official attachment missing. Local candidate is syntax-only |
| NET-03 | TCP reachability | Windows: `Test-NetConnection <VM_IP> -Port <PORT>` | `TcpTestSucceeded : True` | NOT RUN |
| NET-04 | HTTP response | Browser: `http://<VM_IP>:<PORT>/`; optionally `curl.exe -v` | Valid HTTP status/headers/body; server logs the request | NOT RUN |
| NET-05 | Refresh/repeat | Reload browser or repeat GET | A second request is logged and response remains valid | NOT RUN |
| NET-06 | Wrong port negative control | Test a confirmed unused port | TCP check fails; do not mistake this for a server defect | NOT RUN |
| NET-07 | Server stopped negative control | Stop server and retry the correct port | Refused/failed connection; restart server before proceeding | NOT RUN |
| NET-08 | NAT forwarding alternative | Only if using NAT: test host port mapped to guest service port | Host-side forwarding reaches the guest listener | NOT RUN |
| NET-09 | Separate HTTP form demo | Run `examples/http_server_form.py` on course guest TCP 8000; test from Windows with TCP check, curl and browser input/button | TCP succeeds, HTTP 200, label displays the greeting | PASS on TinyCore 10.1 at 192.168.111.61; Edge check returned `Welcome, CO3094 Student!`; not the instructor server or Ubuntu VM |
| NET-10 | Separate UDP DNS demo | Run `examples/dns_udp_server.py` on UDP 53; use Windows `nslookup` and a binary query with transaction ID 0xC309 | `nslookup` returns the demo A value; transaction ID and A/IN resource record are valid | PASS on TinyCore 10.1 at 192.168.111.61; `192.0.2.123` is a documentation-only answer, not the public address of example.com |

## Evidence from the 2026-10-22 form demo

- `evidence/http-form.png`: real Edge page screenshot after filling and clicking the button; 21,934 bytes.
- `evidence/dns-nslookup.png`: real Windows terminal screenshot with the `nslookup` command, server IP and returned A answer; 26,129 bytes.
- Both screenshots remain local and are excluded from Git because the DNS image contains the private lab-network IP. The DNS server's live output and a packet-level check were also observed during the session.

## Evidence to capture after a real instructor-server test

- Date/time and host OS/guest VM version.
- VirtualBox version and adapter mode(s).
- Guest interface name, IP, subnet, and actual server port.
- Exact server source revision/hash and run command.
- Full PowerShell test output.
- Browser URL and HTTP result.
- Relevant guest server log.
- Any firewall change, if a narrow rule was needed.
- Privacy review before placing evidence in GitHub.

Telnet is optional unless a current instructor instruction requires it. It can help inspect raw HTTP, but it is not proof that the browser flow works.
