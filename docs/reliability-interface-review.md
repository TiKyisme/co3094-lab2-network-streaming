# Reliability interface review

**Status:** questions for pair-to-pair review; no interface has been approved by the owners.  
**Scope:** clarify Reliability dependencies without changing the Flow Control or Congestion Control designs.

## Reliability <-> Flow Control

Reliability needs a stable way to identify reliable bytes and to report what the receiver has buffered or delivered. The current Flow Control proposal uses absolute maximum offsets, which is compatible with the proposed channel plus stream-offset model if the scopes are made explicit.

| Question | Draft boundary | Decision owner |
|---|---|---|
| Is credit connection-wide, per channel, or both? | If both apply, sender new-byte allowance is the minimum remaining credit at the scopes that apply | Flow pair with REL-01/REL-02 |
| Do out-of-order ranges consume credit? | Yes. Bytes waiting behind a gap occupy receiver memory | Flow pair |
| Does a packet ACK free receiver credit? | No. Credit grows when application consumption actually releases buffer | Flow pair |
| Does retransmitting an authorized offset consume new credit? | No new application offset is allocated, but receiving/storing the copy still has memory and network costs | Flow pair and Congestion pair |
| What happens when a gap cannot fit within the remaining buffer? | Receiver rejects data beyond advertised limits; sender waits for credit or reports protocol error | Flow pair |
| Can one full channel block another? | Only if credit is connection-wide and exhausted; independent per-channel credit may isolate buffer use | Flow pair |

## Reliability <-> Congestion Control

Reliability reports packet and recovery events. Congestion Control owns the path budget, pacing, and response to confirmed congestion.

| Event / field | Reliability reports | Congestion pair decides |
|---|---|---|
| Packet ACK | PN/range, newly ACKed wire bytes, ACK delay | ACK growth and bytes-in-flight removal |
| RTT | Send time, ACK arrival time, bounded peer ACK delay | RTT smoothing and pacing update |
| Confirmed loss | PN, size, reason (packet threshold or time threshold), any late-ACK signal | Recovery epoch and congestion-window response |
| PTO | Expiration count, probe PN, whether probe carries retry data | Probe budget and whether probe sends while near congestion limit |
| Retransmission | Old reliable range and fresh PN/wire bytes for the new packet | Count retransmission as a new in-flight transmission |
| Real-time packet | PN, update sequence, size, no-retransmit flag | Whether it can be delayed or dropped under congestion |
| Pure ACK-only packet | Rate-limited ACK packet and size; it is non-ack-eliciting in this draft | Whether ACK bytes count toward pacing or bytes-in-flight |

Draft agreement: PTO expiry is not itself a confirmed loss event; retransmission uses the same congestion budget; ACK-only traffic must not create an ACK loop. Do not change the Congestion Control document until its owners accept these boundaries.

## Reliability <-> application framing

- Reliable byte offset is the canonical identity for retransmission and reassembly.
- A complete message is exposed only at the next contiguous offset and only once in the live connection.
- Reusing the same command payload at a new offset is a new command. A stable command ID is required if retries can cross reconnects or if the receiver may crash after performing a side effect but before the sender learns the result.
- A message with a partial byte range is not complete and is not delivered to the application.
- Expiring updates use update sequence, not reliable stream offset; receiver rejects a sequence that is not newer than the latest delivered one.
- Absolute cross-host expiry needs an agreed clock basis. Until then, sender-local queue expiry and receiver sequence freshness are the guaranteed draft behavior.

## Joint review agenda

1. Confirm each component's units: packet counts, bytes, offsets, milliseconds.
2. Agree whether ACK ranges include only ack-eliciting packets and how many ranges are retained.
3. Verify that bytes-in-flight is incremented/decremented once per packet transmission, including retransmission packets.
4. Confirm that receive credit covers both in-order and out-of-order reliable data.
5. Agree how a zero-credit probe is distinguished from a PTO probe.
6. Decide whether independent channels are part of the baseline or only a possible extension.
7. Assign a student to update each shared document after the pairs reach agreement.

## Acceptance checklist

- [ ] REL-01 confirms PN, ACK range, and reliable-range completion semantics.
- [ ] REL-02 confirms loss, PTO, retransmission, and late-ACK semantics.
- [ ] Flow pair confirms byte-offset and out-of-order buffer accounting.
- [ ] Congestion pair confirms event fields, bytes-in-flight, and ACK-only policy.
- [ ] Application owner confirms framing, command ID/idempotency needs, and update freshness rule.
- [ ] Group records its decisions and student prompt evidence.

No items are checked. This is not an approved interface contract.
