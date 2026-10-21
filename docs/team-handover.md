# Bàn giao nhanh CO3094 Lab 2

**Trạng thái:** Có thể dùng bản fallback trong repository để cả nhóm bắt đầu. Google Docs gốc chưa đồng bộ; demo HTTP trên VM hiện tại chưa chạy.

## Lab 2 cần làm gì?

1. **HTTP demo:** từ máy Windows thật truy cập HTTP server trên Ubuntu VM bằng handler `new_connection` thầy cập nhật trên forum. Đây là phần cần demo thực tế.
2. **Ba bản thiết kế nháp:** Reliability, Flow Control và Congestion Control. Email thầy yêu cầu draft; chưa có nguồn xác nhận phải hoàn thiện code cả ba cơ chế.
3. **Giải thích được lựa chọn:** lưu prompt AI thật, ghi nguồn và phân biệt gợi ý AI với quyết định của nhóm.

Email yêu cầu nhóm Lab 2 có sáu người, khoảng hai người mỗi cơ chế. Chưa có deadline Lab 2 được xác minh. Mốc vấn đáp tuần có 17/11/2026 là cho Assignment 1, không tự suy ra thành hạn Lab 2.

## Nhóm đang ở đâu?

- Forum PDF xác nhận `hostip = "0.0.0.0"`, port `22236` và handler `new_connection(conn, addr)`. Ảnh trong forum cho thấy demo lịch sử HTTP 200/browser; đây không phải test VM hiện tại.
- Bộ khung cũ `server_skeleton_previous_upload.py` có `Thread(args=(conn, addr))`, khớp thứ tự handler, nhưng body chỉ in địa chỉ và chưa trả HTTP.
- Bản server-process đính kèm chính thức chưa tải được. Đã chuẩn bị một bản **group reconstruction** riêng và chỉ kiểm tra cú pháp; chưa chạy trên VM.
- VM `ubuntu` đang tắt và dùng Bridged. IP, firewall, listener và kết nối Windows hiện tại chưa biết.
- Các thiết kế trong repo là **PROPOSED của AI**, chưa được cặp sinh viên review.

## Phân công đề xuất

| Pair | Chủ đề | Thành viên |
|---|---|---|
| A | Reliability | Nguyễn Đăng Gia Đạo và Nguyễn Đổng Thiên Kỳ — **TENTATIVE / xác nhận lại** |
| B | Flow Control | M3 và M4 — **điền tên** |
| C | Congestion Control | M5 và M6 — **điền tên** |

HTTP Demo Owner và Backup/Reviewer là hai vai trò chung, hiện **CHỜ PHÂN CÔNG**. Không ai được xem là đã nhận việc cho tới khi tự xác nhận trong nhóm.

Chi tiết việc, kiến thức, file, tiêu chí hoàn thành và câu hỏi vấn đáp nằm trong [thẻ giao việc](team-assignments.md). Cặp Reliability giữ tên tentative như chỉ dẫn; bốn vị trí còn lại là placeholder.

## Bắt đầu theo thứ tự

**D0:** xác nhận sáu tên, cặp và hai HTTP owners. Chọn một người tích hợp nếu thành viên chưa quen Git.

**D0–D1:** mỗi cặp đọc bản `PROPOSED` hiện tại và nguồn được trích dẫn. Tách assumptions khỏi yêu cầu thầy.

**D1–D2:** mỗi cặp sửa một file thiết kế, thêm thuật toán, sơ đồ, ít nhất hai tình huống và trade-off.

**D2:** review chéo; Reliability ↔ Flow ↔ Congestion kiểm tra interface và đơn vị.

**Trước buổi Lab 2:** chốt các bản nháp, rehearsal câu hỏi, và chạy HTTP demo nếu có thể. Đây là lịch **PROPOSED** theo mốc tương đối, không phải deadline chính thức.

## Cập nhật ở đâu?

- Bản hướng dẫn chính: `docs/lab2-group-guide.md`.
- Tiến độ, người phụ trách và task cards: `docs/team-assignments.md`.
- Thiết kế: `docs/reliability-design.md`, `docs/flow-control-design.md`, `docs/congestion-control-design.md`, `docs/integration-design.md`.
- HTTP: `docs/network-setup.md`, `docs/network-test-cases.md`, `docs/http-server-analysis.md`.
- Prompt thật: `prompts/` theo [hướng dẫn lưu prompt](prompt-evidence-instructions.md).

Repository: [TiKyisme/co3094-lab2-network-streaming](https://github.com/TiKyisme/co3094-lab2-network-streaming). Repo đang private; chủ repo cần mời thành viên. Không chia sẻ quyền tự động.

## Checklist trước buổi lab

- [ ] Đã xác nhận roster và từng vai trò.
- [ ] Đã chọn đúng VM, ghi adapter, guest IP và listener.
- [ ] Có output riêng cho VM boot, listener, TCP, HTTP response và browser.
- [ ] Mỗi cặp có bản thiết kế được người còn lại review.
- [ ] Cả sáu hiểu cách ba cơ chế phối hợp và mỗi người giải thích được phần mình.
- [ ] Prompt evidence thật và nguồn tham khảo được lưu.
- [ ] Các điều chưa xác nhận vẫn được gắn `UNVERIFIED` hoặc `CONFLICT`.

Khi gặp vấn đề kỹ thuật, hỏi bạn cùng cặp trước, sau đó HTTP owner hoặc người tích hợp của nhóm (chưa được gán). Câu hỏi về yêu cầu chính thức cần được nhóm trưởng xác nhận với giảng viên; tài liệu này không thay mặt nhóm gửi câu hỏi.

## Trạng thái riêng

`TEAM_HANDOVER_READY = YES (local fallback)` · `GOOGLE_DOC_SYNC_PENDING` · `HTTP_DEMO_STATUS = WAITING_FOR_MANUAL_TEST` · `STREAMING_DESIGNS = PROPOSED / CHƯA REVIEW` · `GROUP_ROSTER = CHƯA CHỐT`.
