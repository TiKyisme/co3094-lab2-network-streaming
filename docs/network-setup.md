# Windows host ↔ Ubuntu guest HTTP setup

**Status:** instructions drafted; **WAITING_FOR_MANUAL_TEST**. No VirtualBox GUI/VM was available in this environment, and `VBoxManage` was not found in PATH.

## Recommended mode

**PROPOSED:** Use **Host-only** when only Windows host ↔ Ubuntu guest access is needed. Oracle's [VirtualBox 7.2 networking manual](https://docs.oracle.com/en/virtualization/virtualbox/7.2/user/networkingdetails.html) describes Host-only as connectivity among host and VMs without a physical/external network. Add a separate NAT adapter only if Ubuntu needs Internet during preparation.

- **Host-only:** host and guest can reach each other; no external network route.
- **NAT:** guest can initiate outbound connections; inbound guest server is not reachable without port forwarding.
- **NAT + Host-only:** host-only path for the demo; NAT path for guest Internet.
- **Bridged:** guest joins the physical LAN. Use only if permitted and needed; it exposes the guest to LAN peers.

The exact GUI labels can vary by VirtualBox release.

## Setup sequence

1. In VirtualBox Manager, open the VM's **Settings → Network**. Enable a Host-only adapter and select/create a host-only network. Confirm its host-side interface and DHCP settings in Network Manager.
2. If the VM requires Internet, enable a second adapter as NAT. Do not route the HTTP demo through NAT unless port forwarding is explicitly configured.
3. Boot Ubuntu and run `ip -4 addr`. Identify the IPv4 address assigned to the Host-only interface; do not copy an example address.
4. Get the instructor's exact `server.py` and overwritten `new_connection` from the forum. Inspect actual port, bind address, and function signature before running it.
5. Ensure the server binds to the Host-only guest IP or otherwise listens on the interface Windows can reach. A bind to `127.0.0.1` accepts only guest-local connections. `0.0.0.0` listens on all guest interfaces and should be used only with the intended exposure understood.
6. Start the server using the exact command in the course source.
7. On Windows, run `Test-NetConnection <HOST_ONLY_VM_IP> -Port <PORT>`. If `TcpTestSucceeded` is true, open `http://<HOST_ONLY_VM_IP>:<PORT>/` in the browser or use `curl.exe -v`.
8. Save real terminal output, browser result, adapter mode, guest interface/IP and source hash/version for the group.

## NAT port forwarding alternative

If Host-only cannot be used, VirtualBox NAT can forward a selected host port to the guest service port. The manual says the NAT engine listens on the host side and relays to the guest. Choose an unused host port and map it to the actual guest port. Then test through the host address/forwarded port (often `127.0.0.1:<host-port>` on the same machine). Do not publish a rule to all host interfaces unless required. The exact rule must match the installed VirtualBox version.

## Troubleshooting

| Symptom | Check |
|---|---|
| No Host-only IP in Ubuntu | Adapter is enabled; selected host-only network exists; DHCP is enabled or static addresses are in the same subnet |
| Windows TCP test fails immediately | Server process, actual port, bind address, guest firewall rule, and adapter selection |
| Windows test times out | Host-only interface/subnet on both systems, VM state, routing, and firewall; do not disable a firewall globally |
| TCP test succeeds, browser fails | Correct `http://` scheme/path, HTTP response/parser, server log; TCP success alone is not HTTP success |
| Ubuntu browser works at `127.0.0.1`, Windows cannot connect | Likely loopback-only bind or wrong VM interface/IP |
| Bridged mode has no address | Network/Wi-Fi policy may restrict bridging; use Host-only or a permitted alternative |
| NAT IP is not reachable from Windows | Expected unless a NAT forwarding rule exists |

Do not open the service to the public Internet for this local demo. Do not alter system firewall/network settings broadly.
