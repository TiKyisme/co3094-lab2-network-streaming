# Lab 2: HTTP form and DNS over UDP

This is a separate, small socket demonstration based on the Lab 2 LMS PDF. It
does not modify or replace the instructor's files. The PDF's page 9 shows the
textbox/button/label HTML idea; pages 2–4 show a UDP server and DNS A-record
response structure.

## HTTP form

Copy `examples/http_server_form.py` to the Ubuntu guest, then run:

```bash
python3 http_server_form.py --bind 0.0.0.0 --port 8000
```

If using the course's older `NetApp-EndHost` VM, its bundled interpreter may
be Python 2.7; the script is compatible with Python 2.7 and Python 3. Verify
with `python3 --version` or `python --version` and use the interpreter that is
available.

In Ubuntu, find the guest IPv4 address with `ip -4 addr` and inspect the
listener with `ss -lntp | grep 8000`. From Windows, substitute the current
guest address:

```powershell
Test-NetConnection <VM_IP> -Port 8000
curl.exe -i http://<VM_IP>:8000/
```

Open `http://<VM_IP>:8000/` in Edge or Chrome. Enter a name and press
**Display**; the result label should show `Welcome, <name>!`. The textbox,
button, label update and HTTP response are served by the socket demo. The
example uses a high TCP port so it does not need administrator privileges.

## DNS A query over UDP

The server answers only the A/IN query for `www.example.com`. The default
answer `192.0.2.123` is reserved for documentation and is **only a demo value**;
it does not claim to be the public address of `www.example.com`. This IP is in
`192.0.2.0/24` (TEST-NET-1), an IPv4 range reserved for documentation by
[RFC 5737](https://www.rfc-editor.org/rfc/rfc5737). The A-record fields follow
the DNS message/resource-record layout in [RFC 1035](https://www.rfc-editor.org/rfc/rfc1035);
for A/IN, RDATA is four IPv4 octets.

On Ubuntu, run:

```bash
sudo python3 dns_udp_server.py --bind 0.0.0.0 --port 53 --answer-ip 192.0.2.123
```

Binding UDP port 53 normally needs root privileges on Linux. If a firewall is
enabled, allow incoming UDP port 53 only on the lab network. Do not change the
VirtualBox adapter mode as part of this test. Record the guest IP from
`ip -4 addr`, then on Windows run:

```powershell
nslookup www.example.com <VM_IP>
```

The server log should show the client's address, matching transaction ID,
question name/type/class and response. The `nslookup` output should list the
server address and demo answer `192.0.2.123`. If it times out, check the guest
listener (`sudo ss -lunp | grep ':53'`), guest firewall, and host-to-guest
reachability without changing VirtualBox networking.

## Current environment note

The registered VM named `ubuntu` currently fails BIOS boot with “No bootable
medium found”; its guest IP is therefore unknown. A separate course VM named
`NetApp-EndHost` is running on the bridged Wi-Fi network and currently showed
`192.168.111.61`. That address is transient and must be checked again before
each test. `NetApp-EndHost` identifies itself as TinyCore Linux 10.1, not
Ubuntu; it has Python 3.6.4 and Python 2.7.14. Results from it must be labeled
with that exact guest name and OS. The host Wi-Fi address during the test was
`192.168.111.188`; no VirtualBox adapter setting was changed.

## Verified run on the available course VM (2026-10-22)

On `NetApp-EndHost`, HTTP TCP port 8000 passed Windows `Test-NetConnection`,
`curl.exe` returned `HTTP/1.1 200 OK`, and an Edge browser test loaded the page,
filled the textbox, clicked the button and observed `Welcome, CO3094 Student!`.
The DNS server bound UDP port 53 with `sudo -n`; Windows `nslookup` returned
`192.0.2.123`. A separate UDP packet check confirmed a matching transaction ID,
one A/IN resource record, four-byte IPv4 data and the same demo address. The
guest had no `ufw`, `iptables`, or `nft` command and no readable iptables names
file; the observed incoming TCP and UDP tests succeeded. This is evidence for
the course TinyCore guest, not for the unbootable VM named `ubuntu` or the
instructor's separate HTTP server on port 22236.
