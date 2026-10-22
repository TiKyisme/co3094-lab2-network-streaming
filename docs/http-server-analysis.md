# Phân tích nguồn HTTP server Lab 2

## Nguồn đã kiểm chứng

Forum PDF “Lab 1 - Network device and Network application” được người dùng cung cấp; cả ba trang đã được đọc và xem trực quan. Bài trả lời trên p. 1 yêu cầu `hostip = "0.0.0.0"` và `port = 22236`. Code p. 2 có `receive_http_header(conn)` và handler `new_connection(conn, addr)`. Handler đọc tới `\r\n\r\n`, nhận theo chunk 1024 byte, tìm dòng request bắt đầu bằng `GET`, gửi HTTP/1.1 200 với trang HTML tĩnh, rồi đóng connection.

`MAX_HEADER_SIZE = 1024` chỉ giới hạn kích thước mỗi lần `recv`, không phải tổng kích thước header. Handler không parse path hay trả HTTP error status cho non-GET; branch đó chỉ in log rồi đóng. Đây là ghi nhận hành vi, không phải phần đã sửa trong source của thầy.

## Bộ khung cũ do người dùng cung cấp

`server_skeleton_previous_upload.py` hiện có trong worktree dưới dạng file người dùng cung cấp, chưa được thêm vào Git. Nội dung cho thấy:

- `accept()` trả `(conn, addr)`.
- Thread gọi `Thread(target=new_connection, args=(conn, addr))`.
- Signature cũ cũng là `new_connection(conn, addr)`, nên **thứ tự đối số khớp** với forum handler.
- Body cũ chỉ `print(addr)`, nên chưa phải HTTP responder.
- `hostip` cũ lấy từ UDP route tới `8.8.8.8:1` rồi fallback `127.0.0.1`; forum lại yêu cầu bind `0.0.0.0`.
- Port của khung là `22236`, trùng port trong forum.

Syntax của bộ khung đã parse thành công bằng Python AST. Điều đó chỉ kiểm tra syntax; không chứng minh server chạy hoặc truy cập được.

## Mã tích hợp local

`examples/http_server_reconstructed_demo.py` là **GROUP RECONSTRUCTION**, kết hợp thứ tự `accept()`/Thread từ bộ khung người dùng với handler nhìn thấy trong forum PDF. Bản này đặt bind address `0.0.0.0`, port `22236`, và giữ nguyên đặc tính handler GET/non-GET quan sát được. Syntax đã parse thành công.

Đây không phải file server đầy đủ chính thức của thầy. Tệp `sample_code_http_server_process.txt` được liên kết trong forum chưa có trong thư mục repo, course source, Downloads hay Codex attachments; truy cập không có phiên LMS chuyển hướng tới trang đăng nhập. Không dùng mã reconstruction như bằng chứng nguồn chính thức.

### Lệnh ứng viên

Trên Ubuntu, sau khi copy file reconstruction sang guest:

```bash
python3 --version
python3 http_server_reconstructed_demo.py
```

Trong terminal Ubuntu khác, xem listener:

```bash
ip -4 addr
ss -lntp | grep 22236
```

Trên Windows, thay `<GUEST_IP>` bằng địa chỉ thật vừa thấy:

```powershell
ipconfig
Test-NetConnection <GUEST_IP> -Port 22236
curl.exe -v http://<GUEST_IP>:22236/
```

Sau đó mở `http://<GUEST_IP>:22236/` trong Chrome. `0.0.0.0` là địa chỉ bind, không phải URL client.

## Khác biệt với Sample NetApp PDF

Sample_NetApp p. 7 là server TCP accept/print khác: `new_connection(addr, conn)` và Thread args `(addr, conn)`. Thứ tự này **không khớp** forum handler `(conn, addr)`. Sample này không parse HTTP và không gửi response. Không thay bộ khung người dùng bằng sample này.

## Demo lịch sử trong forum

P. 3 có ảnh terminal với `HTTP/1.1 200 OK`, Content-Length 174 và ảnh Chrome. Text ngay trên ảnh ghi `192.168.56.100:22236`, còn thanh địa chỉ ảnh cho thấy `192.168.56.103:22236`. Đây là evidence demo lịch sử của lớp, không phải test VM hiện tại; chưa xác định IP nào đúng cho máy đang dùng.

## Trạng thái server forum/reconstruction

- Syntax check: bộ khung và reconstruction đều **PASS (syntax only)**.
- VM `ubuntu` đã được khởi động thử ngày 2026-10-22 nhưng BIOS báo `No bootable medium found`; guest IP chưa biết.
- Không chạy mã forum/reconstruction cổng 22236; complete server attachment vẫn thiếu.
- Các kết quả từ `http_server_form.py` ở mục dưới là bài form riêng, không phải kiểm thử source forum.

## Bài HTTP form riêng (2026-10-22)

`examples/http_server_form.py` là bài minh họa riêng theo yêu cầu HTML của Lab 2;
nó không sửa hoặc thay thế mã forum/giảng viên. Bản này đã chạy trên VM môn học
`NetApp-EndHost` (TinyCore Linux 10.1, Python 3.6.4), IP bridged hiện tại
`192.168.111.61`, cổng TCP 8000. Windows `Test-NetConnection` thành công,
`curl.exe` nhận HTTP 200, và Edge tải trang, điền textbox, bấm button, rồi đọc
label `Welcome, CO3094 Student!`. Ảnh thật được lưu ở
`evidence/http-form.png` (21,934 bytes, local-only).

VM đăng ký tên `ubuntu` được khởi động thử nhưng dừng ở BIOS; guest đó chưa có
IP để thử. Vì vậy kết quả form không được xem là kiểm thử trên Ubuntu hay kiểm
thử của server forum cổng 22236. Mã server forum chính thức vẫn chưa được chạy.
