# Checklist review thiết kế theo cặp

Dùng checklist này trước khi chuyển task sang `READY FOR REVIEW` hoặc `VERIFIED / DONE`. Ghi reviewer, ngày, file/commit và bằng chứng trong `docs/team-assignments.md`.

## Phạm vi và nguồn

- [ ] Đúng phần được giao: Reliability, Flow Control hoặc Congestion Control.
- [ ] Mỗi yêu cầu được gắn `REQUIRED`, `SUPPORTED`, `PROPOSED`, `UNVERIFIED` hoặc `CONFLICT`.
- [ ] Nguồn chính thức và trang/đoạn liên quan được dẫn rõ.
- [ ] AI proposal không bị mô tả thành yêu cầu của giảng viên.
- [ ] Xung đột Assignment 1 không bị tự ý giải quyết trong thiết kế Lab 2.

## Thiết kế

- [ ] Bài toán và loại dữ liệu được mô tả cụ thể.
- [ ] Thuật toán đủ bước để thành viên khác lần theo.
- [ ] Có sequence diagram hoặc flowchart.
- [ ] Packet/message/state và đơn vị đo được định nghĩa.
- [ ] Có ít nhất hai ví dụ diễn tiến từ đầu đến cuối.
- [ ] Có ưu điểm, nhược điểm, giới hạn và assumptions.
- [ ] Có edge cases: mất, trùng, reorder, timeout, buffer đầy/zero window, ACK trễ hoặc update hết hạn phù hợp với cơ chế.
- [ ] Đơn vị trong công thức khớp; không lẫn flow credit với network congestion budget.

## Tích hợp ba cơ chế

- [ ] ACK packet được phân biệt với delivery/completion của reliable message.
- [ ] Flow credit chỉ giới hạn reliable data mới theo byte receiver cho phép.
- [ ] Congestion budget tính `max(0, cwnd - bytes_in_flight)` theo byte.
- [ ] Retransmission và real-time packets vẫn tiêu thụ congestion budget/pacing.
- [ ] Update đã hết hạn không bị gửi muộn chỉ để đạt reliability.
- [ ] Chỉ ra nơi ordering tạo head-of-line blocking.

## Bằng chứng và giải thích

- [ ] Prompt AI thực tế được lưu; không tạo lại prompt thay cho lịch sử.
- [ ] Phân biệt output AI với quyết định cuối của cặp.
- [ ] Cả hai thành viên đều trả lời được câu hỏi trong task card.
- [ ] Có review chéo từ ít nhất một cặp khác.
- [ ] Không có test hoặc demo nào được đánh dấu PASS nếu chưa có output thật.

**Kết quả review:** `READY FOR REVIEW` / `CHANGES REQUESTED` / `VERIFIED / DONE`  
**Reviewer:** ____________________  **Ngày:** ____________________  
**File/commit/evidence:** __________________________________________
