# CO3094 Lab 2 — Hướng dẫn chuẩn bị và phân công

**Trạng thái:** bản Markdown làm việc dựa trên nội dung Google Doc do Drive Search trả về và hai email trích trong prompt.  
**Nguồn:** chưa mở được LMS/forum, chưa có server source, chưa chạy VirtualBox.

Nhãn: **REQUIRED** = email nói trực tiếp; **SUPPORTED** = diễn giải có căn cứ; **PROPOSED** = nhóm đề xuất; **UNVERIFIED** = cần nguồn/giảng viên xác nhận.

## 1. Tóm tắt

**REQUIRED**
1. Máy thật truy cập HTTP server chạy trong VM bằng `new_connection` đã được thầy ghi đè trên forum.
2. Nhóm chuẩn bị draft design cho Reliability, Flow Control và Congestion Control.
3. Nhóm có sáu người, khoảng hai người/cơ chế.
4. Lưu prompt và lịch sử AI để có thể trình bày khi được yêu cầu.

**SUPPORTED**
- Steam UDP gaming networking và Google QUIC là ví dụ tham khảo; email không yêu cầu implement nguyên giao thức.
- Email B yêu cầu draft design, không xác nhận phải viết code cho cả ba cơ chế.
- Tuần có ngày 17/11/2026 là mốc vấn đáp Assignment 1, không tự suy thành deadline Lab 2.

**UNVERIFIED**
Transport bắt buộc, VM network mode, port, deliverables/ảnh, prototype requirement, và lịch Lab 2 cụ thể.

## 2. Phần A — Windows host truy cập HTTP server trên Ubuntu VM

### Topology đề xuất

**PROPOSED:** Dùng **Host-only** nếu VM không cần Internet. Nếu VM cần Internet, thêm adapter **NAT**. **Bridged** là phương án thay thế khi Host-only không phù hợp và mạng cho phép; VM sẽ tham gia LAN. Tên các lựa chọn có thể thay đổi theo VirtualBox version.

Theo [Oracle VirtualBox 7.2](https://docs.oracle.com/en/virtualization/virtualbox/7.2/user/networkingdetails.html), Host-only nối host với guest nhưng không nối guest ra mạng ngoài. NAT không nhận kết nối inbound tới server trong guest nếu chưa tạo port forwarding.

### Trình tự

1. **Lấy source chính thức.** Từ forum “Lab 1 - Network device and Network application”, lấy nguyên văn hàm `new_connection` thầy ghi đè và đúng `server.py`. Không thay bằng code tự viết hoặc course bundle khác.
2. **Đối chiếu lời gọi.** Python `socket.accept()` trả `(conn, address)`; `Thread(args=...)` chuyển các phần tử thành positional argument cho target. So sánh đúng định nghĩa hàm với nơi gọi; không đoán `(conn, addr)` hay `(addr, conn)` nếu chưa có code.
3. **Cấu hình VM.** Bật Host-only adapter và chọn host-only network có host interface/DHCP, hoặc đặt IP tĩnh theo dải thật. Bên Ubuntu chạy `ip -4 addr` và ghi IPv4 trên đúng interface.
4. **Kiểm tra server.** Xác định port từ source thực tế. Server không thể chỉ bind `127.0.0.1` nếu Windows truy cập bằng IP VM. Nếu code cho phép, ưu tiên bind IP interface Host-only. `0.0.0.0` nghe trên mọi interface guest; chỉ dùng nếu hiểu phạm vi exposure.
5. **Chạy server.** Dùng đúng lệnh/interpreter trong source. `python3 server.py` chỉ là ví dụ, chưa xác minh cho code của thầy. Ghi log terminal và IP/port.
6. **Kiểm tra từ Windows.** `Test-NetConnection <IP_VM> -Port <PORT>` chỉ xác nhận TCP reachability. Sau đó mở `http://<IP_VM>:<PORT>/` hoặc chạy `curl.exe -v http://<IP_VM>:<PORT>/` để kiểm tra HTTP.
7. **Bằng chứng nội bộ.** **PROPOSED:** lưu output thật từ Windows, log server Ubuntu, mode/adapter/IP/port và ảnh browser. Email không xác nhận ảnh là deliverable Lab 2.

### Phương án thay thế

**PROPOSED:** NAT port forwarding có thể map cổng host sang guest port; truy cập qua host address/port đã map, không dùng IP NAT của guest như IP được expose trực tiếp. Chỉ tạo rule cần thiết. Bridged có thể làm VM lộ trên LAN; hỏi chính sách mạng trước khi dùng.

## 3. Phần B — Draft design streaming

Trước khi chia cơ chế, cả nhóm thống nhất workload và delivery class. Proposal hiện tại là một ứng dụng tương tác thời gian thực có:
- **Reliable ordered messages:** setup, cấu hình, lệnh quan trọng.
- **Expiring updates:** trạng thái media/game có sequence và deadline; packet quá hạn được bỏ, không retransmit muộn.
- **PROPOSED:** transport UDP-oriented do nhóm mô tả để học các cơ chế; không phải QUIC/Steam implementation, không tương thích với chúng và không dành cho production.

Xem [kiến trúc](streaming-architecture.md), [reliability](reliability-design.md), [flow control](flow-control-design.md), [congestion control](congestion-control-design.md), [tích hợp](integration-design.md).

## 4. Phân công sáu người

**PROPOSED**, chờ nhóm xác nhận:
- Cặp A — Reliability: Member A/B.
- Cặp B — Flow Control: Member C/D.
- Cặp C — Congestion Control: Member E/F.
- Cả nhóm cùng duyệt packet format, sơ đồ tích hợp, câu hỏi mở và prompt evidence.
- Phần Windows↔Ubuntu là việc chung: một người thao tác chính, một người dự phòng; mọi thành viên cần hiểu đường đi của request.

Google Doc cũ điền tên một cặp Reliability nhưng để hai cặp khác trống. Bản này không khẳng định những tên đó là roster hiện tại. Nhóm xác nhận tên trước khi phân công.

Mỗi cặp nên chuẩn bị (PROPOSED): bài toán, sơ đồ, trạng thái/thuật toán, ví dụ packet loss hoặc receiver chậm, ít nhất hai tình huống kiểm tra, trade-off và prompt history.

## 5. Checklist trước Lab 2

- [ ] Đã lấy và đối chiếu code forum `new_connection`.
- [ ] Windows truy cập server bằng topology đã chọn; ghi IP/port thật.
- [ ] Browser nhận HTTP response; chưa đánh dấu cho tới khi test thật.
- [ ] Cả nhóm thống nhất workload và delivery class.
- [ ] Mỗi cơ chế có sơ đồ, trạng thái, quy tắc, ví dụ và trade-off.
- [ ] Ba cơ chế dùng chung packet numbering, ACK, flow credit, congestion budget và deadline.
- [ ] Prompt thật được lưu; full session export bảo quản riêng và rà soát riêng tư.
- [ ] Hỏi thầy nếu protocol, prototype, deliverables hoặc ngày Lab 2 chưa rõ.

## 6. Giới hạn nguồn

Email A/B trong prompt là nguồn yêu cầu cao nhất hiện có. Chưa có bài đăng LMS, code của thầy, roster đã xác nhận, kết quả test, screenshot hay phản hồi của giảng viên.
