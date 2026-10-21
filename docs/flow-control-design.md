# Flow control design — draft proposal

**Classification:** PROPOSED. This design limits receiver memory; it is separate from congestion control.

## Receiver credit

For reliable data, receiver advertises a monotonic **absolute maximum byte offset**:
- connection limit `max_data`
- optional per-channel `max_channel_data[channel]`

Sender tracks the next reliable byte offset and may send new data only up to the peer's absolute limit. For one connection-level limit, define `flow_credit = max(0, peer_max_data - next_new_data_offset)` bytes. If connection and channel limits both apply, available credit is the minimum of the nonnegative remaining byte credit at each scope. Do not treat ACK arrival alone as proof that receiver application consumed buffer space; the receiver raises its absolute limit only when capacity is actually freed.

This resembles QUIC's limit-based flow control; it is a design reference, not a requirement to copy QUIC frames.

## Rules

1. Receiver initializes limits based on its allocated buffer capacity.
2. Reliable data received within credit is stored in a bounded queue/reassembly buffer.
3. When the application consumes data and frees space, receiver raises the absolute limit and repeats the update until it sees progress.
4. Sender accepts only larger limits; reordered old updates cannot reduce credit.
5. At zero available credit, sender pauses new reliable data. It can send a small, bounded credit probe/control packet, subject to congestion control, to recover from a lost update.
6. Real-time unreliable updates use a separate bounded latest-value queue. If full, receiver drops old/expired updates instead of blocking the reliable receiver queue.
7. Any protocol violation that exceeds advertised credit is rejected and recorded.

## State

Receiver: buffer capacity, bytes queued, consumed offset, connection max offset, per-channel max offsets.  
Sender: sent offsets, peer-advertised max offsets, flow-blocked state, next credit-probe time.

## Example

The receiver has 64 KiB assigned to the reliable channel and has consumed 48 KiB. It can raise its absolute max offset to allow 48 KiB more bytes without exceeding that capacity. If no space is free, it does not raise the limit. These values only illustrate accounting; 64 KiB is not a proposed required setting.

## Flow-control test scenarios

- Slow receiver: credit stops increasing; sender stops new reliable bytes while still processing ACKs.
- Zero credit: sender pauses payload and resumes after a higher limit arrives.
- Lost or reordered credit update: repeating the absolute limit avoids deadlock/regression.
- Full real-time queue: older update is dropped; reliable credit accounting remains intact.

This credit says what the receiver can buffer. The separate congestion window says what the network path can carry in flight. See [RFC 9000, Data Flow Control](https://www.rfc-editor.org/rfc/rfc9000.html#section-4).


## Assignment 1 compatibility note

Assignment 1 PDF p. 2 calls for a window-based sliding window. The absolute max-offset credit here is a proposal inspired by QUIC. Before claiming Assignment 1 alignment, define how this credit advances relative to the expected sliding-window model and confirm the instructor accepts it.
