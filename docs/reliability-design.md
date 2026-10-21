# Reliability design — draft proposal

**Classification:** PROPOSED. This is an explainable design sketch, not an instructor requirement or implementation.

## Data classes

- **Reliable ordered control/data:** setup, configuration and commands. Delivered once to the application and in order within its channel.
- **Expiring real-time state:** each update has a sequence/deadline; a stale or duplicate update is dropped. Do not retransmit after its useful deadline.

## State

Sender keeps:
- `next_packet_number`
- sent-packet map: packet number, send time, bytes in flight, and reliable chunks carried
- outstanding reliable message/stream offsets and retry deadline
- `smoothed_rtt`, `rtt_variance`, and probe timer

Receiver keeps:
- received packet-number ranges for ACKs
- per-channel next-delivery offset/message number
- bounded reordering/deduplication state
- recent update sequence/deadline state

## Operation

1. Assign a fresh packet number to every transmission.
2. Receiver discards duplicate packet processing but sends an ACK range again when useful.
3. ACK ranges allow sender to identify acknowledged packets and infer a missing earlier packet when later packets arrive.
4. Declare loss with a packet/time threshold that tolerates limited reordering; use a probe timeout (PTO) with backoff when progress is absent.
5. Retransmit only reliable chunks that remain outstanding and useful. Put them in a new packet number; never retransmit an old real-time snapshot after expiration.
6. Receiver buffers out-of-order reliable chunks within the advertised flow limit and releases data to the application only when the next contiguous offset/message is available.
7. Receiver suppresses duplicate message delivery using channel plus message ID/offset.
8. If ACK is lost, a later ACK range can cover the received packet; if data is retransmitted first, duplicate suppression prevents a second delivery and receiver can ACK again.

## Example cases

| Event | Sender/receiver behavior |
|---|---|
| Packet 14 lost, later packet 15 acknowledged | Loss detector marks 14 lost after threshold; retransmit its still-useful reliable chunk in a new packet number |
| ACK lost | Sender may retransmit; receiver recognizes duplicate, does not redeliver, and repeats ACK information |
| Reliable chunk arrives out of order | Buffer within limit; release once missing earlier data arrives |
| Duplicate reliable chunk | Deduplicate by stream offset/message ID; do not execute command twice |
| State update sequence 22 arrives after 23 | Drop 22 if 23 is already current or 22 expired |
| No ACK progress | PTO probe with bounded exponential backoff; close/report failure after proposal retry cap |

## Trade-offs

Selective retransmission reduces repeated data compared with stop-and-wait. Ordered reliable delivery can still block later messages in the same channel behind a missing earlier chunk. Separate unreliable state updates keep freshness, but the application must tolerate missing snapshots. Retransmission improves delivery only while the payload remains valuable and consumes congestion capacity.

## Draft validation cases

- Drop one reliable packet, deliver later ACKs, verify only missing useful chunk is retransmitted.
- Drop an ACK, deliver duplicate payload, verify one application delivery.
- Reorder reliable messages and verify bounded buffering and ordered delivery.
- Delay a real-time update past its deadline and verify no stale retransmission.

These are planned scenarios, not test results. See also [RFC 9002](https://www.rfc-editor.org/rfc/rfc9002.html) and the [Valve packet wire format](https://github.com/ValveSoftware/GameNetworkingSockets/blob/master/src/steamnetworkingsockets/clientlib/SNP_WIRE_FORMAT.md) as references.


## Assignment 1 implementation gap

The current draft does not yet specify file IDs, chunk offsets, file size, per-chunk integrity checks, final-file verification, or a resume policy. Assignment 1 PDF p. 3 explicitly asks for file chunking/reassembly over UDP, while p. 2 also says TCP handles reliable files/messages. Do not claim this draft satisfies that milestone until the transport conflict is resolved and file-transfer semantics are added.
