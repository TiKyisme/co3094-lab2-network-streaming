# Windows host ↔ Ubuntu guest HTTP setup

**Status:** The forum handler/settings remain verified, but its complete source and port-22236 run are still unavailable. A separate HTTP form/DNS socket demo was tested on the course VM `NetApp-EndHost`; the VM named `ubuntu` fails BIOS boot. No VirtualBox network setting was changed.

## Read-only environment discovery (2026-10-21)

| Item | Observed |
|---|---|
| Windows | Windows 11, build 10.0.26200 |
| Python | 3.14.4 x64 at `C:\Python314\python.exe` |
| VirtualBox | Installed at `C:\Program Files\Oracle\VirtualBox`; `VBoxManage` version 7.2.20r175154 |
| VirtualBox GUI | Installed; no `VirtualBox.exe` or `VirtualBoxVM.exe` process was running during discovery |
| Registered VMs | `ubuntu` (Ubuntu 64-bit, powered off) and `NetApp-EndHost` (Linux 64-bit, powered off); no VM was running |
| `ubuntu` adapter config | Adapter 1 is Bridged to Intel Wi-Fi 6 AX203; adapters 2–8 disabled |
| Host-only interface | VirtualBox Host-Only Ethernet Adapter, Up; host IPv4 192.168.56.1/24 |
| Host-only DHCP server | Enabled; guest lease range 192.168.56.101–192.168.56.254 |
| Guest IPv4/firewall/server | NOT AVAILABLE: guests are powered off |

## Recheck and form-demo execution (2026-10-22)

VirtualBox 7.2.20r175154 currently lists `ubuntu` as Ubuntu 64-bit with Adapter 1
Bridged to Intel Wi-Fi 6 AX203; adapters 2–8 remain disabled. Starting it
headless produced the BIOS error `No bootable medium found`; it was powered off
again without changing its settings. No guest IP was available for this VM.

The separate `NetApp-EndHost` guest was already running, bridged to the same
Wi-Fi network, and reported TinyCore Linux 10.1, Python 3.6.4 and `eth0`
`192.168.111.61/24`. Windows Wi-Fi was `192.168.111.188/24`. The form demo on
TCP 8000 passed `Test-NetConnection`, `curl.exe` returned HTTP 200 and a real
Edge browser check confirmed the button updates the label. The UDP DNS demo on
port 53 passed Windows `nslookup`; a packet check verified transaction ID
`0xC309` and one A/IN answer with demo address `192.0.2.123`. No `ufw`,
`iptables` or `nft` utility was present in that TinyCore guest; the observed TCP
and UDP requests reached their listeners. These results do not establish the
Ubuntu VM or the separate instructor HTTP server on port 22236.

The ZIP contains no OVA, so the registered `ubuntu` VM's identity as the instructor's intended VM is not established.

## Instructor forum source and historical result

The supplied Lab 1 forum export specifies listener `hostip = "0.0.0.0"` and port `22236`; the handler signature is `new_connection(conn, addr)`. The old user skeleton has matching `Thread(args=(conn, addr))`, but its handler only prints. `examples/http_server_reconstructed_demo.py` combines the skeleton flow and visible forum handler; it is labeled as group reconstruction, not official complete source. The linked attachment is still needed to verify the teacher's full server. A historical screenshot shows HTTP 200 and browser rendering at `192.168.56.103:22236`; the text above says `.100`. Neither is confirmed for the local VM.

## Topology decision

**PROPOSED:** Host-only is preferred for isolated host↔guest access; add NAT only if Ubuntu needs Internet. The local `ubuntu` VM is currently Bridged over Wi-Fi; no settings have been changed. The forum's `0.0.0.0` is a wildcard listener address, while Windows must connect to the guest's actual IPv4 address. The historical `.103` screenshot does not establish the current VM's address or adapter mode.

The separate Sample NetApp page 7 helper discovers an outgoing-interface address through a UDP route attempt and falls back to loopback; that behavior belongs to the sample only. The forum specifies `0.0.0.0`, but the linked server file is needed to confirm how it applies that setting. Verify the actual listener with `ss -lntp` before choosing or changing the adapter combination.

## Guided manual sequence

1. In VirtualBox Manager, select the intended Ubuntu VM and inspect **Settings → Network**. Record all enabled adapters. Do not assume the local `ubuntu` VM is the course VM.
2. Host-only remains **PROPOSED** for isolated host↔guest traffic; add NAT only if Ubuntu needs Internet. The local VM is Bridged today. Do not change adapters until the intended VM and test candidate are confirmed.
3. Start the VM and run Ubuntu `ip -4 addr`. Record the guest IPv4 and interface.
4. Copy the instructor server or explicitly approved group reconstruction to the guest, run it, then check `ss -lntp`. Record the exact listening IP/port from output.
5. On Windows run `ipconfig`, then `Test-NetConnection <VM_IP> -Port <PORT>`.
6. If TCP succeeds, run `curl.exe -v http://<VM_IP>:<PORT>/`; then open the same URL in a Windows browser.
7. Save real output and server log. Do not mark a test PASS until its output is observed.

Microsoft documents `Test-NetConnection -Port` as a TCP connectivity test; it does not prove a valid HTTP response. Browser rendering is a separate check.

## Troubleshooting

| Symptom | Check |
|---|---|
| Guest IP missing | VM adapter, host-only network/DHCP, guest NIC state |
| Listener only at `127.0.0.1` | Windows cannot reach that guest-local listener; verify the forum code's bind address |
| Listener on NAT IP with Host-only enabled | Check which interface the server helper selected; bind behavior may be in the forum overwrite |
| TCP test fails | VM/guest IP, actual listener/port, adapter reachability and guest firewall |
| TCP succeeds, curl fails | HTTP request/response behavior; TCP success is not HTTP success |
| Curl succeeds, browser fails | URL/scheme/path and browser-visible response |

Do not disable the firewall globally or open the service to the public Internet.
