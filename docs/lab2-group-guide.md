# CO3094 Lab 2 — Hướng dẫn chuẩn bị và phân công

**Trạng thái:** bản Markdown làm việc dựa trên hai email thầy, nội dung Google Doc đã đọc qua Drive Search, và các nguồn CO3094/L07 vừa được kiểm chứng.  
**Giới hạn:** chưa có bài forum chứa phiên bản `new_connection` overwritten; chưa chạy VM.

Nhãn: **REQUIRED** = email nói trực tiếp; **SUPPORTED** = diễn giải có căn cứ; **PROPOSED** = nhóm đề xuất; **UNVERIFIED/CONFLICT** = cần nguồn hoặc thầy xác nhận.

## 1. Tóm tắt Lab 2

**REQUIRED**
1. Máy thật truy cập HTTP server chạy trên VM bằng `new_connection` thầy ghi đè trên forum.
2. Nhóm chuẩn bị draft design cho Reliability, Flow Control và Congestion Control.
3. Nhóm Lab 2 có sáu thành viên, khoảng hai người/cơ chế.
4. Lưu prompt và lịch sử AI để trình bày khi được yêu cầu.

**SUPPORTED**
- Email nêu Steam UDP gaming networking và Google QUIC làm ví dụ tham khảo.
- Email B yêu cầu draft design, không xác nhận phải viết code cả ba cơ chế.
- Email B đặt vấn đáp Assignment 1 vào tuần chứa 17/11/2026, không xác nhận đó là deadline Lab 2.

**UNVERIFIED / CONFLICT**
- Topology bắt buộc, port của forum version, deliverables Lab 2, prototype, transport Assignment 1, nhóm Assignment 1, và ngày giờ nộp Assignment 1.

## 2. Phần A — Windows host truy cập HTTP server trên Ubuntu VM

### Topology

**PROPOSED:** Host-only phù hợp cho kết nối host↔guest; thêm NAT chỉ khi guest cần Internet. VM hiện tại đang cấu hình Bridged trên Wi-Fi; chưa có thay đổi cấu hình.

Có caveat trong code sample: Sample_NetApp PDF p. 7 lấy IP bằng cách thử UDP route tới `8.8.8.8:1`, fallback sang loopback. Host-only đơn lẻ hoặc NAT+Host-only có thể làm helper chọn sai interface. Chỉ chọn topology sau khi xem đúng forum overwrite và kiểm tra listener thật.

### Source và lời gọi

1. Lấy nguyên văn `new_connection` overwritten và đúng `server.py` từ forum “Lab 1 - Network device and Network application”. Forum post chưa được cung cấp.
2. Sample_NetApp PDF p. 7 (không phải forum override) cho thấy `accept()` trả `conn, addr`, rồi thread truyền `(addr, conn)` tới `new_connection(addr, conn)`. Worker mẫu chỉ in socket; không xử lý HTTP.
3. Port **22236** được xác nhận cho sample PDF p. 7 (chỉ là sample). Chưa xác nhận đó là port của forum-overwritten server.
4. Lấy đúng `server.py`/function forum trước khi xác định bind address, port và cách đọc request/gửi HTTP response.

### Test sequence sau khi source xác nhận

1. Trong VirtualBox kiểm tra VM và adapter; không đổi sang Host-only cho tới khi xác định code bind nào.
2. Boot VM, chạy Ubuntu `ip -4 addr` và ghi interface/IP.
3. Chạy đúng server; Ubuntu `ss -lntp` để ghi địa chỉ/port đang lắng nghe.
4. Windows `ipconfig`, sau đó `Test-NetConnection <VM_IP> -Port <PORT>`.
5. Nếu TCP thành công, `curl.exe -v http://<VM_IP>:<PORT>/`; sau đó browser.
6. Lưu output/log thật. TCP success, HTTP response success và browser rendering success là ba kết quả riêng.

**Không có test nào PASS** cho tới khi output thật được quan sát. Sample PDF p. 7 không phải HTTP server hoàn chỉnh.

## 3. Phần B — Design nháp streaming

**PROPOSED:** ứng dụng tương tác thời gian thực có reliable ordered control/file messages và expiring state updates. Xem [architecture](streaming-architecture.md), [reliability](reliability-design.md), [flow control](flow-control-design.md), [congestion control](congestion-control-design.md) và [integration](integration-design.md).

**Assignment 1 compatibility warning:** PDF p. 1 nói UDP streaming/reliable transfer; p. 2 nói TCP reliable transfer và UDP heartbeat; p. 3 có TCP handshake nhưng cũng yêu cầu reliable file reassembly over UDP. Draft UDP-oriented hiện tại không giải quyết mâu thuẫn đó và chưa phải Assignment 1 architecture. Giữ các phương án tách bạch đến khi thầy xác nhận.

## 4. Phân công

- Cặp A — Reliability: **Nguyễn Đăng Gia Đạo** và **Nguyễn Đổng Thiên Kỳ** — **TENTATIVE** theo Google Doc cũ; xác nhận lại với nhóm.
- Cặp B — Flow Control: Member C/D — placeholder.
- Cặp C — Congestion Control: Member E/F — placeholder.
- Tất cả cùng duyệt workload/packet format, ba cơ chế phối hợp, prompt evidence và test demo.
- Cả nhóm cần nắm mục tiêu Windows↔Ubuntu; một người demo chính và một người dự phòng là đề xuất.

Mỗi cặp nên chuẩn bị (PROPOSED): bài toán, state/algorithm, sơ đồ, ít nhất hai tình huống kiểm tra và trade-off.

## 5. Checklist trước Lab 2

- [ ] Có exact forum overwrite và matching server source.
- [ ] Biết guest IP, listener IP/port và topology thật.
- [ ] Windows TCP test, curl HTTP test và browser test đều có output riêng.
- [ ] Mỗi design draft trả lời được loss/reorder/slow receiver/congestion cases.
- [ ] Đã ghi nhận Assignment 1 transport/group/deadline conflicts, không tự giải quyết.
- [ ] Lịch sử prompt thật được lưu; full session export bảo quản riêng.

Email không xác nhận ảnh chụp hay định dạng nộp cụ thể. Ghi chú LMS chung nói buổi thực tập cần báo cáo và bài tập lớn có báo cáo/thuyết trình; cần xác nhận yêu cầu cụ thể của Lab 2.
