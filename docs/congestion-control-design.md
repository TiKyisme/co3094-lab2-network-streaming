# Congestion control design — draft proposal

**Classification:** PROPOSED. Baseline is a simplified NewReno-like AIMD controller with pacing, adapted as a learning design; it is not claimed to be QUIC-compliant.

## Signals and state

Sender tracks `cwnd` in bytes, `bytes_in_flight`, `ssthresh`, smoothed RTT, RTT variation, delivery/ACK progress, loss indications, recovery boundary, and pacer schedule. Loss/time thresholds should tolerate reordering. Validated ECN feedback may be a future extension.

## Proposed controller

1. Start with a conservative initial congestion window and a pacing schedule.
2. **Slow start:** while below `ssthresh`, grow `cwnd` in response to acknowledged bytes.
3. **Congestion avoidance:** grow approximately additively, at most about one maximum datagram size per acknowledged window.
4. On a confirmed loss or congestion mark, enter recovery once per recovery period and reduce `cwnd` (NewReno-style, roughly half), with a configured minimum. Do not reduce repeatedly for every ACK of the same loss episode.
5. Use a probe timeout to ensure forward progress. A single PTO expiration is not automatically proof of persistent congestion; track subsequent ACK/loss evidence.
6. Pace transmissions at a rate related to `cwnd / smoothed_rtt`, and never exceed `cwnd - bytes_in_flight` for congestion-controlled data.
7. Apply the same path budget to reliable data, retransmissions and unreliable real-time updates. Drop an expired update if it cannot be sent while useful.

## RTT increase without loss

In this loss-based baseline, rising RTT updates the smoothed RTT and therefore lowers the pacing rate `cwnd / smoothed_rtt`; it does not by itself halve `cwnd`. Record the latency and let the application drop expired media updates. A separate delay-target guard could reduce media rate after sustained queueing delay, but that is an optional extension to test, not part of this baseline.

## Distinguish receiver and network limits

- Receiver flow credit can stop new reliable payload even if the path has free capacity.
- Congestion budget can stop all traffic even if receiver credit remains.
- Available new reliable bytes are constrained by both: `min(flow_credit, cwnd - bytes_in_flight)`.
- If receiver credit is zero, wait for credit/probe; do not mislabel this as network congestion.
- Loss or validated ECN can trigger recovery while receiver credit remains. RTT informs the pacer and loss timer; RTT growth alone does not trigger a cwnd reduction in this baseline.

## Trade-offs

AIMD/NewReno is explainable and responds to loss, but can react after queues form and may reduce throughput on lossy wireless paths. Pacing smooths bursts. Delay-only signals can react earlier but can mistake path variation for queueing; the optional guard needs hysteresis and experiments. CUBIC/BBR are comparison candidates, not required designs.

## Draft test scenarios

- Increase bandwidth-delay product with no loss: cwnd/pacing should grow without exceeding receiver credit.
- Introduce repeatable loss: one recovery reduction per episode, then cautious growth.
- Raise RTT without loss: pacing rate falls as smoothed RTT rises; cwnd stays unchanged in this baseline.
- Set receiver credit to zero while network is healthy: sender blocks reliable data without declaring congestion.
- Queue an expired real-time update behind pacing: discard rather than send stale data.

Not tested. Reference: [RFC 9002](https://www.rfc-editor.org/rfc/rfc9002.html), including congestion window, recovery and pacing.
