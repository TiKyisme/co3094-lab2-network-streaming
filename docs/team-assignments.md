# Thẻ giao việc cho nhóm CO3094 Lab 2

**Trạng thái roster:** chưa chốt. Hai tên Reliability giữ ở mức **TENTATIVE / CHỜ XÁC NHẬN**; bốn vị trí còn lại là placeholder. Đây là phân công **PROPOSED**, chưa phải quyết định đã được cả nhóm xác nhận.

## Bảng tiến độ

| Task / owner | Status | File, reviewer và bằng chứng |
|---|---|---|
| **REL-01** — M1 Gia Đạo (**TENTATIVE**), ACK/packet number | NOT STARTED | `docs/reliability-design.md`; review M2 + Flow; sơ đồ ACK, hai tình huống, prompt thật, giải thích miệng |
| **REL-02** — M2 Thiên Kỳ (**TENTATIVE**), loss/retry/reorder | NOT STARTED | `docs/reliability-design.md`; review M1 + Congestion; bảng retry, hai tình huống, prompt thật, giải thích miệng |
| **FLOW-01** — M3 (**CHỜ ĐIỀN TÊN**), receiver buffer/credit | NOT STARTED | `docs/flow-control-design.md`; review M4 + Reliability; byte credit, sơ đồ, slow receiver case, prompt thật |
| **FLOW-02** — M4 (**CHỜ ĐIỀN TÊN**), sender window/zero-window | NOT STARTED | `docs/flow-control-design.md`; review M3 + Congestion; pause/resume, zero-window case, prompt thật |
| **CC-01** — M5 (**CHỜ ĐIỀN TÊN**), RTT/loss detection | NOT STARTED | `docs/congestion-control-design.md`; review M6 + Reliability; signal/state table, hai tình huống, prompt thật |
| **CC-02** — M6 (**CHỜ ĐIỀN TÊN**), `cwnd`/pacing/recovery | NOT STARTED | `docs/congestion-control-design.md`; review M5 + Flow; `cwnd` update, byte example, prompt thật |
| **HTTP-01** — HTTP Demo Owner (**CHỜ PHÂN CÔNG**), source | BLOCKED | `docs/http-server-analysis.md`; backup/reviewer đối chiếu full attachment, nguồn và giới hạn |
| **HTTP-02** — HTTP Backup/Reviewer (**CHỜ PHÂN CÔNG**), integration | IN PROGRESS | `examples/http_server_reconstructed_demo.py`; HTTP Owner review; syntax checked, output chạy thật còn chờ |
| **HTTP-03** — Owner (**CHỜ PHÂN CÔNG**), VM/IP/listener | BLOCKED | `docs/network-setup.md`; reviewer kiểm tra adapter, `ip -4 addr`, `ss -lntp` output thật |
| **HTTP-04** — Owner (**CHỜ PHÂN CÔNG**), Windows checks | NOT STARTED | `docs/network-test-cases.md`; HTTP Owner review; output TCP, HTTP status/body và Chrome riêng |
| **HTTP-05** — Owner (**CHỜ PHÂN CÔNG**), evidence/runbook | NOT STARTED | `docs/network-test-cases.md`; team reviewer kiểm tra screenshot thật và bước tái chạy |

**Các trạng thái:** `NOT STARTED`, `IN PROGRESS`, `BLOCKED`, `READY FOR REVIEW`, `VERIFIED / DONE`. Chỉ đổi sang `VERIFIED / DONE` sau khi reviewer xem deliverable và bằng chứng; AI-generated text không tự tạo ra trạng thái DONE.

## Cách làm chung cho từng cặp

Mỗi cặp cùng bàn giao một thiết kế; hai task card chia phần nghiên cứu, không tạo hai thiết kế rời. Thiết kế của cặp phải có:

1. Bài toán và loại dữ liệu cần xử lý.
2. Thuật toán/mô hình đã chọn, từng bước rõ ràng.
3. Sơ đồ sequence hoặc flowchart.
4. Packet/message/state/biến quan trọng và đơn vị đo.
5. Ít nhất hai tình huống ví dụ có diễn tiến cụ thể.
6. Lý do chọn, ưu/nhược điểm và giới hạn.
7. Tương tác với hai cơ chế còn lại.
8. Câu hỏi chưa giải quyết và prompt AI thật đã dùng.

Cặp phải đọc, phản biện và sửa bản `PROPOSED` hiện có. Không được chép nguyên đề xuất AI rồi đánh dấu hoàn thành.

## REL-01 — M1: xác nhận packet và ACK

**Owner:** Nguyễn Đăng Gia Đạo — **TENTATIVE / CHỜ XÁC NHẬN**.

### A. Mục tiêu

Giải thích được sender nhận biết packet/message nào đã tới và vì sao packet ACK khác với xác nhận ứng dụng đã xử lý message.

### B. Kiến thức cần học

Packet number; sequence number/stream offset; ACK range; duplicate; packet-level ACK so với message completion; trạng thái đã gửi/chưa được xác nhận.

### C. Công việc

1. Đọc `docs/reliability-design.md` và phần ACK trong `docs/integration-design.md`.
2. Vẽ luồng sender gửi packet, receiver nhận, receiver báo ACK, sender cập nhật trạng thái.
3. Đề xuất cách nhận biết duplicate mà không giao message hai lần.
4. Ghi rõ ACK xác nhận packet tới receiver; reliable data có thể cần theo dõi riêng đến khi đủ byte/range.
5. Thống nhất với M2 và gửi đề xuất cho cặp Flow về offset/ACK cần dùng.

### D. Deliverable

Phần ACK/packet-number trong `docs/reliability-design.md`, một sequence diagram, state table và prompt evidence trong `prompts/`.

### E. Acceptance criteria

- Có định nghĩa từng số thứ tự và vòng đời của nó.
- Có ví dụ ACK đến đúng thứ tự và ACK đến trễ.
- Duplicate không làm ứng dụng nhận message hai lần.
- Nêu được dữ liệu nào được ACK và dữ liệu nào vẫn còn outstanding.
- M1 tự giải thích được sơ đồ mà không đọc nguyên văn.

### F. Dependencies

Thống nhất packet number với cặp Congestion; thống nhất reliable offset/message ID với M2 và Flow. Không chọn field width trước khi cả nhóm review.

### G. Questions for oral exam

1. ACK packet đã chứng minh ứng dụng xử lý xong message chưa?
2. Nếu ACK bị mất nhưng packet đã tới receiver thì sender làm gì?
3. Làm sao tránh giao cùng một command hai lần?

### H. GitHub handover location

`docs/reliability-design.md`, `docs/integration-design.md`, và prompt thật tại `prompts/<ngày>-reliability-ack-<mã-thành-viên>.txt`.

## REL-02 — M2: mất gói, timeout và thứ tự

**Owner:** Nguyễn Đổng Thiên Kỳ — **TENTATIVE / CHỜ XÁC NHẬN**.

### A. Mục tiêu

Giải thích khi nào một packet được xem là mất, cách retransmit reliable data và cách receiver xử lý dữ liệu đến sai thứ tự.

### B. Kiến thức cần học

Packet loss; reordering; timeout/PTO; retransmission; exponential backoff; duplicate suppression; ordered delivery; expiration của real-time update.

### C. Công việc

1. Đọc `docs/reliability-design.md` và `docs/streaming-architecture.md`.
2. Viết state diagram cho sent → acknowledged hoặc suspected-lost → retransmitted.
3. Dùng packet 14 mất, packet 15 ACK đến làm ví dụ; ghi điều kiện trước khi retransmit.
4. Giải thích retransmission gửi cùng reliable data/offset trong packet number mới.
5. So sánh reliable ordered data với update hết hạn: gói cũ có thể bỏ, không chặn update mới.

### D. Deliverable

Phần timeout/retransmit/reorder trong `docs/reliability-design.md`, hai bảng tình huống, các giới hạn và prompt evidence.

### E. Acceptance criteria

- Có điều kiện loss/reorder không tuyên bố mất quá sớm.
- ACK cũ/trễ và ACK mất đều có phản ứng cụ thể.
- Retransmit không dùng lại packet number cũ và không giao duplicate hai lần.
- Nêu rõ ordered delivery chỉ chặn kênh reliable liên quan.
- M2 trả lời được cách timeout ảnh hưởng đến congestion control.

### F. Dependencies

Nhận ACK/packet semantics từ M1; thống nhất với Flow về buffer cho out-of-order data; thống nhất với Congestion rằng retransmission vẫn chiếm path budget.

### G. Questions for oral exam

1. Vì sao không retransmit ngay sau khi thấy một packet number bị thiếu?
2. Retransmission là packet mới hay packet cũ gửi lại? Vì sao?
3. Reliable in-order delivery tạo HoL blocking ở phạm vi nào?

### H. GitHub handover location

`docs/reliability-design.md`, `docs/integration-design.md`, và prompt thật tại `prompts/<ngày>-reliability-recovery-<mã-thành-viên>.txt`.

## FLOW-01 — M3: receiver buffer và receive credit

**Owner:** Member 3 — **CHỜ ĐIỀN TÊN**.

### A. Mục tiêu

Cho thấy receiver quảng bá còn có thể lưu bao nhiêu byte reliable data và vì sao flow control bảo vệ receiver, không đo tình trạng mạng.

### B. Kiến thức cần học

Receiver buffer; receive window; absolute max offset/credit; consumed bytes; flow credit; zero window; unit consistency.

### C. Công việc

1. Đọc `docs/flow-control-design.md` và công thức trong `docs/integration-design.md`.
2. Định nghĩa credit bằng byte hoặc một đơn vị duy nhất; không trộn packet count với bytes.
3. Vẽ buffer: received, buffered out-of-order, delivered/consumed và free capacity.
4. Viết slow receiver case và cách receiver tăng receive limit sau khi ứng dụng đọc dữ liệu.
5. Kiểm tra với Reliability xem data nào được tính vào credit và cách duplicate không dùng thêm buffer.

### D. Deliverable

Phần receiver trong `docs/flow-control-design.md`, sơ đồ buffer/window, hai ví dụ và prompt evidence.

### E. Acceptance criteria

- Có một định nghĩa cụ thể cho `advertised_max_data` và `receiver_credit` bằng byte.
- Có ví dụ receiver chậm và credit giảm còn zero.
- Duplicate/reorder không làm phép tính credit tăng sai.
- Phân biệt credit receiver với `cwnd - bytes_in_flight`.
- M3 giải thích được cách receiver mở lại cửa sổ.

### F. Dependencies

Thống nhất reliable byte offset với Reliability; phối hợp Congestion để không gọi receiver-full là congestion.

### G. Questions for oral exam

1. Receive window bảo vệ bên nào?
2. Vì sao zero window không đồng nghĩa với packet loss?
3. Receiver báo credit theo byte hay packet, và sender áp dụng ra sao?

### H. GitHub handover location

`docs/flow-control-design.md`, `docs/integration-design.md`, và prompt thật tại `prompts/<ngày>-flow-receiver-<mã-thành-viên>.txt`.

## FLOW-02 — M4: sender window và zero-window recovery

**Owner:** Member 4 — **CHỜ ĐIỀN TÊN**.

### A. Mục tiêu

Giải thích sender được phép phát reliable bytes nào, cách nhận window update và cách phục hồi khi receiver báo zero window.

### B. Kiến thức cần học

Send offset; advertised limit; flow credit còn lại; window update; probe; zero-window recovery; retry có giới hạn.

### C. Công việc

1. Đọc `docs/flow-control-design.md` và `docs/integration-design.md`.
2. Viết pseudocode pause/resume khi flow credit bằng zero hoặc lớn hơn zero.
3. Mô phỏng window update bị mất và bị lặp; dùng absolute limit để tránh credit giảm lùi.
4. Phối hợp với Congestion để sender đợi cả receive credit lẫn network budget.
5. Nêu rõ flow credit chỉ áp dụng cho byte reliable mới; retransmission vẫn cần congestion budget.

### D. Deliverable

Phần sender/window update trong `docs/flow-control-design.md`, pseudocode, hai case và prompt evidence.

### E. Acceptance criteria

- Sender không gửi reliable data vượt receive limit.
- Có cách nhận lại tiến triển sau zero window, không probe vô hạn.
- Window update lặp/mất không gây gửi vượt limit hoặc deadlock không hồi phục.
- Có ví dụ tách receiver credit khỏi congestion budget.
- M4 giải thích được công thức tích hợp bằng byte.

### F. Dependencies

Nhận buffer/credit convention từ M3; thống nhất ACK/retry với Reliability và bytes in flight với Congestion.

### G. Questions for oral exam

1. Sender dừng điều gì khi receiver credit bằng zero?
2. Vì sao absolute window limit dễ phục hồi khi update bị lặp?
3. Retransmission có tiêu thụ flow credit mới không, và có tiêu thụ congestion budget không?

### H. GitHub handover location

`docs/flow-control-design.md`, `docs/integration-design.md`, và prompt thật tại `prompts/<ngày>-flow-sender-<mã-thành-viên>.txt`.

## CC-01 — M5: RTT và phát hiện congestion

**Owner:** Member 5 — **CHỜ ĐIỀN TÊN**.

### A. Mục tiêu

Giải thích sender dùng ACK timing, RTT và loss/ECN signal nào để suy luận network path đang bị nghẽn.

### B. Kiến thức cần học

RTT sample; smoothed RTT; RTT variation; ACK/loss; packet reordering; ECN (nếu chọn); phân biệt congestion với receiver limit.

### C. Công việc

1. Đọc `docs/congestion-control-design.md` và `docs/integration-design.md`.
2. Lập bảng signal → diễn giải → hành động; tách RTT tăng khỏi loss trong baseline NewReno-like.
3. Mô phỏng ACK trễ, packet loss và packet reorder để chỉ ra false positive có thể xảy ra ở đâu.
4. Thống nhất với Reliability cách ACK range/loss event được báo cho controller.
5. Ghi nguồn RFC 9002 cho cơ chế tham khảo; đánh dấu lựa chọn là PROPOSED.

### D. Deliverable

Phần congestion signals trong `docs/congestion-control-design.md`, bảng event, ít nhất hai ví dụ và prompt evidence.

### E. Acceptance criteria

- RTT/loss signal được định nghĩa và đơn vị rõ.
- RTT tăng không tự động bị mô tả là loss trong baseline hiện tại.
- Có cách giảm báo mất do reorder quá sớm.
- Tách congestion của network khỏi receiver zero window.
- M5 giải thích được vì sao một loss event có thể làm giảm sending budget.

### F. Dependencies

Nhận packet ACK/loss facts từ Reliability; thống nhất cách đo bytes in flight với M6; báo Flow cách phân biệt nghẽn mạng và receiver chậm.

### G. Questions for oral exam

1. RTT tăng có luôn chứng minh packet loss không?
2. ACK đến trễ ảnh hưởng thế nào đến loss detector?
3. Làm sao phân biệt receiver không còn buffer với mạng đang nghẽn?

### H. GitHub handover location

`docs/congestion-control-design.md`, `docs/integration-design.md`, và prompt thật tại `prompts/<ngày>-congestion-signals-<mã-thành-viên>.txt`.

## CC-02 — M6: `cwnd`, pacing và recovery

**Owner:** Member 6 — **CHỜ ĐIỀN TÊN**.

### A. Mục tiêu

Trình bày cách controller điều chỉnh lượng dữ liệu đang bay và thời điểm gửi để tránh burst, phản ứng với congestion và vẫn bỏ update đã hết hạn.

### B. Kiến thức cần học

Congestion window (`cwnd`); bytes in flight; AIMD/NewReno-like; `ssthresh`; pacing; recovery episode; expired real-time update.

### C. Công việc

1. Đọc `docs/congestion-control-design.md` và `docs/integration-design.md`.
2. Viết pseudocode cho slow start, congestion avoidance và một lần giảm `cwnd` trong loss episode.
3. Tạo ví dụ `cwnd=12 KiB`, `bytes_in_flight=9 KiB`; tính network budget 3 KiB.
4. Cho thấy retransmission và real-time updates đều tiêu thụ congestion budget; flow credit không thay thế budget này.
5. Phối hợp cả hai cặp còn lại để quyết định ưu tiên khi credit, pacing hoặc deadline chặn send.

### D. Deliverable

Phần controller/pacing/recovery trong `docs/congestion-control-design.md`, pseudocode, ví dụ có đơn vị và prompt evidence.

### E. Acceptance criteria

- `cwnd`, bytes in flight và network budget cùng dùng byte.
- Tính được `max(0, cwnd - bytes_in_flight)`.
- Có hành động sau loss và không giảm nhiều lần cho cùng loss episode.
- Pacing giới hạn cả reliable, retry và real-time packets.
- Update hết hạn được drop thay vì gửi muộn; M6 giải thích được trade-off.

### F. Dependencies

Nhận loss events từ M5; thống nhất retry behavior với Reliability; thống nhất receiver byte credit với Flow.

### G. Questions for oral exam

1. Vì sao `cwnd - bytes_in_flight` chứ không phải `cwnd` là budget hiện tại?
2. Retransmission có được bỏ qua congestion control không?
3. Nếu còn congestion budget nhưng update đã hết hạn thì sender làm gì?

### H. GitHub handover location

`docs/congestion-control-design.md`, `docs/integration-design.md`, và prompt thật tại `prompts/<ngày>-congestion-controller-<mã-thành-viên>.txt`.

## Definition of done cho từng cặp

- [ ] Một bản thiết kế chung đã được cả hai thành viên đọc và quyết định.
- [ ] Có sơ đồ, thuật toán, trường/state, hai ví dụ và trade-off.
- [ ] Ghi assumptions, edge cases và nguồn tham khảo.
- [ ] Nêu điểm nối với hai cơ chế còn lại.
- [ ] Thành viên reviewer chéo xác nhận các công thức và đơn vị.
- [ ] Hai người đều trả lời được câu hỏi vấn đáp ở task card.
- [ ] Prompt thực tế được lưu; AI suggestion và quyết định của nhóm được phân biệt.
- [ ] Reviewer chuyển trạng thái sang `VERIFIED / DONE` và ghi commit/evidence.

## Quy tắc cập nhật

Mỗi cặp chỉ có một người sửa trực tiếp file thiết kế tại một thời điểm. Nếu cả nhóm quen Git, dùng branch + Pull Request; nếu chưa, mỗi cặp chuẩn bị một patch riêng và một người tích hợp lần lượt. Không cấp quyền repository tự động; repository đang private và chủ repo phải mời thành viên.
