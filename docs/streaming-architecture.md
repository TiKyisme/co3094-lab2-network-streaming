# Streaming architecture — draft proposal

**Classification:** PROPOSED; not a teacher requirement, implementation, or tested protocol.

## Workload

A single interactive real-time session sends two application data classes over a UDP-oriented transport:

1. **Reliable ordered messages:** session setup, configuration changes, and commands whose loss would make the session incorrect.
2. **Expiring real-time updates:** periodic game/media state. Each update has a sequence and expiration time; stale updates may be dropped rather than retransmitted late.

This division makes reliability, receiver flow limits, and network congestion work together. It is inspired by the distinction between reliable QUIC streams and unreliable QUIC DATAGRAM frames, and by Valve GameNetworkingSockets' reliable/unreliable message types. It does not copy their wire protocol or claim compatibility.

## Proposed packet fields

Every packet has:
- `connection_id`
- monotonic `packet_number` (new number for each transmission)
- `packet_type` and flags
- optional ACK ranges for received packet numbers
- optional absolute receive-credit update
- one or more framed payloads

Each payload identifies a channel/message or reliable byte offset. Expiring updates additionally carry a message sequence and deadline/age limit. Exact field widths and encoding are intentionally TBD until group review.

## Send/receive flow

```mermaid
sequenceDiagram
    participant S as Sender
    participant N as Network
    participant R as Receiver
    S->>N: Reliable control (packet number, message/offset)
    N->>R: Deliver, reorder if needed
    R->>N: ACK range + new receive credit
    N->>S: ACK/credit
    S->>N: Expiring state update (sequence, deadline)
    N->>R: Deliver if fresh; otherwise drop
    R->>N: ACK packet status (for congestion/loss measurement)
    N->>S: ACK range
    Note over S: Reliability retries only unacknowledged reliable data before deadline
    Note over S: Congestion control limits both classes; receiver credit limits reliable new data
```

ACKing a packet and acknowledging application delivery are separate concepts: ACK ranges report packet receipt for loss/congestion accounting; reliable-message completion is tracked until all its data is acknowledged/delivered under the selected protocol semantics.

## Shared invariants

- Packet numbers never repeat within a connection.
- Duplicate packets are not delivered twice to the application.
- Reliable data is retransmitted only while useful; obsolete real-time updates are dropped.
- Receiver credit constrains reliable data that would consume receiver buffer.
- Congestion budget and pacing constrain every transmitted packet, including ACKs where applicable, retries, and unreliable updates.
- A sender does not send new reliable bytes beyond receiver credit or beyond the current congestion budget.
- A bounded queue prevents a slow receiver from retaining unlimited stale updates.
- All timeout, MTU, buffer, and deadline values are tunable proposal parameters, not course requirements.

## Scope and references

- **PROPOSED:** the group may present this model as its own draft after reviewing and changing it.
- Not production-ready: no authentication, encryption, handshake security, NAT traversal, key rotation, or interoperable encoding is specified.
- [RFC 9000](https://www.rfc-editor.org/rfc/rfc9000.html) describes reliable in-order QUIC streams and absolute flow-control limits.
- [RFC 9002](https://www.rfc-editor.org/rfc/rfc9002.html) describes QUIC loss detection, NewReno congestion control, and pacing.
- [RFC 9221](https://www.rfc-editor.org/rfc/rfc9221.html) adds unreliable QUIC datagrams without retransmission but still subject to connection congestion control.
- [Valve GameNetworkingSockets](https://github.com/ValveSoftware/GameNetworkingSockets) documents reliable and unreliable messages plus packet-status ACK ideas.

## Unresolved design choices

Confirm whether the instructor expects a custom UDP design or a protocol-level design using QUIC; choose exact ordering, timeout and buffer parameters; decide whether channel-level ACKs are required; and have all six members explain the final choices.
