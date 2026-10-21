# Integrated protocol rules — draft proposal

**Classification:** PROPOSED, not implemented or tested.

## Send eligibility

Keep separate state for receiver capacity and path capacity:

- `flow_credit`: new reliable bytes still allowed by the receiver's advertised absolute limit.
- `congestion_budget = cwnd - bytes_in_flight`: current path budget in bytes.

For new reliable data, send no more than:

```text
min(flow_credit, congestion_budget)
```

For an unreliable real-time update, receiver flow credit does not apply in this proposal; it still consumes the congestion budget and pacing allowance. A full local update queue drops the oldest/expired state instead of blocking the receiver indefinitely. A retransmission uses a new packet number and consumes path congestion budget; it does not count as new application bytes against flow credit if it refers to already-authorized reliable stream offsets.

## Example scheduler

1. Process ACKs: update packet receipt, bytes in flight, RTT estimate, loss state and reliable-message state.
2. Process receive-credit updates: accept only a larger absolute limit.
3. Drop expired updates from local queues.
4. If reliable bytes are blocked by credit, pause that class and send a small credit probe on a bounded timer.
5. If congestion budget/pacer is exhausted, wait; do not bypass the controller for either class.
6. Schedule eligible reliable retransmissions and new reliable bytes before their usefulness deadline; schedule fresh real-time updates according to application priority.
7. Receiver validates packet number and deadline, suppresses duplicates, then stores/reorders reliable data or delivers the freshest update.
8. Receiver advertises more absolute credit after application consumption frees buffer.

## Invariants and failure behavior

- A lost credit update can be resent; absolute credit never decreases.
- ACK loss does not cause duplicate application delivery: repeated ACK ranges and message IDs make processing idempotent.
- Out-of-order reliable data is buffered within a configured cap; gaps block ordered delivery only for that reliable channel.
- Expiring updates never block later updates behind an old gap.
- On repeated probe timeout with no ACK progress, declare connection failure after a configured cap and notify the application.
- All limits, retry caps, buffer sizes and deadlines are proposal parameters to be chosen and then tested.

## Example interaction

Receiver buffer is nearly full and advertises 20 KiB additional reliable credit. The sender has 8 KiB of that credit left but only 3 KiB of congestion budget, so at most 3 KiB of reliable data can be sent now. A fresh state update may use any remaining congestion budget; it cannot exceed it. If the receiver consumes data and raises its absolute limit, new reliable data becomes eligible. If network ACKs are delayed, the congestion budget may remain exhausted even while receiver credit is available.

## Review checklist

- Does every member distinguish byte credit from bytes in flight?
- Does the design account for retransmissions in congestion control?
- Can an unreliable update expire without blocking the reliable stream?
- Can a lost ACK/credit update recover without duplicate delivery or deadlock?
- Are resource caps and deadlines explicit?


## Assignment 1 compatibility note

The current integration assumes one UDP-oriented transport with reliable and expiring classes. Assignment 1 PDF pp. 1–3 also describes TCP reliable transfer/handshake and UDP file reassembly. Keep this design as the Lab 2 draft; do not declare it the final Assignment 1 architecture until those conflicting transport statements are resolved. File chunking, reassembly, integrity checks, and any TCP path remain out of scope here.
