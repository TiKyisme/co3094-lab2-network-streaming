# CO3094 - LAB 2 | Hướng dẫn chuẩn bị & phân công nhóm 6 người

**Bản hướng dẫn nhóm — 21/10/2026**  
**Trạng thái:** Có thể bắt đầu phân công theo bản fallback này. Google Docs gốc chưa đồng bộ; HTTP demo trên VM hiện tại chưa được chạy.

## ĐỌC PHẦN NÀY TRƯỚC — LAB 2 CẦN LÀM GÌ?

Trong ba phút, cả nhóm cần nắm hai việc chính:

1. **Demo HTTP:** máy Windows thật truy cập một HTTP server đang chạy trong máy ảo Ubuntu, dùng handler `new_connection` do thầy cập nhật trên forum. Đây là phần phải chứng minh bằng kết quả chạy thật.
2. **Draft design cho streaming:** nhóm sáu người chia thành ba cặp, mỗi cặp chuẩn bị một bản thiết kế nháp cho Reliability, Flow Control hoặc Congestion Control. Email thầy yêu cầu draft; chưa có bằng chứng Lab 2 bắt buộc phải code hoàn chỉnh cả ba cơ chế.

Nhóm đã xác minh cấu hình forum `hostip = "0.0.0.0"`, port `22236`, handler `new_connection(conn, addr)` và ảnh demo lịch sử HTTP 200. Đã tìm được bộ khung Python cũ; nó có đúng thứ tự đối số `(conn, addr)` nhưng handler hiện chỉ in địa chỉ. Chưa lấy được file server-process đầy đủ, chưa khởi động VM và chưa có test hiện tại.

**Nhóm có thể bắt đầu ngay:** xác nhận roster, đọc bản thiết kế `PROPOSED`, chia từng cặp, dựng sơ đồ và viết hai tình huống cho cơ chế mình nhận. **Đang chờ input/test:** bốn tên thành viên, hai người phụ trách HTTP, full server source, guest IP, và output từ VM thật.

| Trạng thái tổng | Giá trị hiện tại |
|---|---|
| `TEAM_HANDOVER_READY` | **YES — local fallback**, đủ để phân việc và bắt đầu |
| `GOOGLE_DOC_STATUS` | **GOOGLE_DOC_SYNC_PENDING**; link gốc trả 404 qua tài khoản Drive đang kết nối; không tạo tài liệu trùng |
| `HTTP_DEMO_STATUS` | **WAITING_FOR_MANUAL_TEST**; handler/setting đã xác minh, VM đang tắt |
| `STREAMING_DESIGN_STATUS` | **PROPOSED — chưa được các cặp review** |
| `GROUP_ROSTER_STATUS` | **PARTIAL**; hai tên tentative, bốn placeholder; HTTP owners chưa gán |
| `PROMPT_EVIDENCE_STATUS` | Hướng dẫn đã có; prompt thật của từng cặp sẽ lưu khi bắt đầu nghiên cứu |

## 1. Yêu cầu và độ tin cậy của nguồn

Ưu tiên nguồn theo thứ tự: email mới nhất của thầy → thông báo/forum BK-LMS → tài liệu CO3094/source gốc → tài liệu nhóm đã xác minh → Google Docs/Markdown cũ → tài liệu ngoài và đề xuất AI.

| Nội dung | Nhãn | Phạm vi |
|---|---|---|
| Physical host truy cập HTTP server trên VM bằng handler thầy ghi đè | **REQUIRED** | Email Lab 2 ngày 08/10/2026 |
| Draft Reliability, Flow Control, Congestion Control; nhóm sáu người, khoảng hai người/cơ chế | **REQUIRED** | Email Assignment Group áp dụng cho buổi Lab 2 |
| Lưu prompt AI và đủ khả năng giải thích thiết kế | **REQUIRED** | Email thầy |
| Steam UDP gaming và Google QUIC | **SUPPORTED examples** | Ví dụ tham khảo, không phải yêu cầu dựng lại nguyên giao thức |
| Host-only topology, port `22236`, screenshot/report format, code hoàn chỉnh ba cơ chế | **UNVERIFIED** | Chỉ dùng port `22236` cho HTTP forum theo PDF; không suy ra yêu cầu streaming từ port này |
| Vấn đáp trong tuần có 17/11/2026 | **REQUIRED for Assignment 1** | Không phải deadline Lab 2 |

PDF Assignment 1 vẫn có mâu thuẫn TCP/UDP, Individual/Pair so với nhóm sáu người, yêu cầu HoL và ngày/thứ deadline. Chúng được ghi ở [requirements matrix](requirements-matrix.md) và [open questions](open-questions.md); không dùng để tự chọn kiến trúc hoặc deadline Lab 2.

## 2. Nguồn HTTP và trạng thái môi trường

Forum PDF xác nhận bind address `0.0.0.0`, port `22236`, handler `new_connection(conn, addr)` và trả HTTP 200 cho GET. `0.0.0.0` là địa chỉ lắng nghe trên các interface IPv4 của guest; **không** nhập `0.0.0.0` vào browser. Windows phải dùng IP thật của guest.

Bộ khung `server_skeleton_previous_upload.py` gọi thread với `(conn, addr)`, đúng với handler. Phần `new_connection` trong khung chỉ in địa chỉ và không trả HTTP. File đính kèm `sample_code_http_server_process.txt` của forum chưa lấy được; vì vậy mã tích hợp local được gắn rõ **GROUP RECONSTRUCTION — NOT VERIFIED AS THE COMPLETE INSTRUCTOR SOURCE**.

Máy host đang dùng Windows 11; VirtualBox đã cài. VM `ubuntu` đang **powered off** và cấu hình Bridged qua Wi-Fi. Host-only adapter của host có `192.168.56.1/24`, DHCP đang bật. Chưa biết guest IP, firewall hoặc trạng thái listener. Ảnh forum cũ cho thấy HTTP 200/browser tại `.103`, trong khi dòng chữ nói `.100`; không dùng hai địa chỉ đó làm IP hiện tại.

## 3. Bảng phân công sáu vị trí

| Vị trí | Phụ trách | Tên | Trạng thái |
|---|---|---|---|
| M1 | Reliability: packet number, ACK, duplicate detection | Nguyễn Đăng Gia Đạo | **TENTATIVE / chờ xác nhận** |
| M2 | Reliability: loss, timeout, retransmit, reorder | Nguyễn Đổng Thiên Kỳ | **TENTATIVE / chờ xác nhận** |
| M3 | Flow Control: receiver buffer, receive window, flow credit | **CHỜ ĐIỀN TÊN** | Chưa phân công |
| M4 | Flow Control: sender limit, window update, zero-window recovery | **CHỜ ĐIỀN TÊN** | Chưa phân công |
| M5 | Congestion: RTT, ACK/loss signals, detection | **CHỜ ĐIỀN TÊN** | Chưa phân công |
| M6 | Congestion: `cwnd`, pacing, rate/recovery | **CHỜ ĐIỀN TÊN** | Chưa phân công |

HTTP Demo Owner và HTTP Backup/Reviewer là hai vai trò chung, **CHỜ PHÂN CÔNG**. Không tự gán người. Task card chi tiết A–H và câu hỏi vấn đáp của từng vị trí nằm trong [team assignments](team-assignments.md).

## 4. Sản phẩm chung của mỗi cặp

Mỗi cặp cùng cập nhật một file thiết kế hiện có và bàn giao: (1) bài toán; (2) thuật toán từng bước; (3) sequence diagram/flowchart; (4) packet, message, state và đơn vị đo; (5) ít nhất hai tình huống; (6) lý do chọn, ưu/nhược điểm/giới hạn; (7) cách phối hợp với hai cơ chế kia; (8) assumptions, edge cases và nguồn; (9) prompt thật và quyết định cuối của nhóm.

File: [Reliability](reliability-design.md), [Flow Control](flow-control-design.md), [Congestion Control](congestion-control-design.md), [integration](integration-design.md). Đây đều là đề xuất AI `PROPOSED`; cặp phải phản biện và sửa trước khi nhận là sản phẩm nhóm.

## 5. Mô hình streaming chung để thảo luận

Đề xuất hiện tại mô tả ứng dụng tương tác thời gian thực qua một transport hướng UDP: control/configuration cần reliable delivery; state update có deadline có thể bị drop khi đã cũ. Đây là mô hình **PROPOSED**, không phải yêu cầu của thầy và chưa được chọn chính thức.

- Reliability theo dõi packet number/ACK và reliable offset/message; retransmission dùng packet number mới, receiver deduplicate.
- Flow Control giới hạn byte reliable mới bằng receive credit của receiver.
- Congestion Control giới hạn byte đang bay trên network path; mọi gói congestion-controlled, gồm retransmission và update, đều chịu pacing/path budget.
- ACK packet receipt và hoàn tất ứng dụng là hai trạng thái khác nhau. Reliable ordering chỉ chặn kênh liên quan; update đã quá hạn không cần gửi muộn.

**Đơn vị tích hợp:**

`receiver_credit = max(0, peer_max_data - next_new_data_offset)`  
`congestion_budget = max(0, cwnd - bytes_in_flight)`  
`new_reliable_bytes_now = min(receiver_credit, congestion_budget)`

Cả ba đại lượng trên là byte. `peer_max_data` là absolute receiver limit; `next_new_data_offset` là offset tiếp theo sẽ dùng cho reliable data mới. Nếu có cả connection và channel limit, lấy mức credit còn lại nhỏ nhất. Retransmission không tiêu thụ receive credit của byte mới lần nữa, nhưng packet retransmit vẫn chiếm congestion budget khi đang bay. Real-time update không bị receiver flow credit trong draft này, nhưng vẫn tiêu thụ congestion budget và pacing. Cặp Congestion có thể dùng AIMD/NewReno-like làm baseline so sánh; đây là **PROPOSED**, không phải lựa chọn đã chốt.

**Tình huống xuyên suốt:** sender có `cwnd = 12 KiB`, `bytes_in_flight = 9 KiB`, nên còn 3 KiB congestion budget. Receiver chỉ còn 8 KiB flow credit. Sender được phát tối đa 3 KiB reliable mới. Nếu một packet mất, retransmission vẫn dùng budget; nếu receiver phát zero window thì reliable data phải chờ credit, không gọi đó là congestion. Nếu state update đã hết hạn thì drop, không chặn update kế tiếp.

## 6. PHẦN A — HTTP SERVER / VIRTUALBOX

**Sơ đồ:** Windows Physical Host → VirtualBox Network → Ubuntu Virtual Machine → HTTP Server → HTTP Response → Windows browser.

| ID / việc | Owner / trạng thái | File và bằng chứng hoàn thành |
|---|---|---|
| HTTP-01 — Handler, full source, bind, port | Owner chờ gán / **BLOCKED**: full attachment chưa có | `docs/http-server-analysis.md`; đối chiếu accept/thread call, tách nguồn official/reconstruction, reviewer ký |
| HTTP-02 — Tích hợp, syntax, run command | Backup chờ gán / **IN PROGRESS**: reconstruction syntax-check, chưa chạy | `examples/http_server_reconstructed_demo.py`; giữ nguyên khung gốc, reviewer kiểm tra attribution và lệnh |
| HTTP-03 — VM, adapter, guest IP, listener | Owner chờ gán / **BLOCKED**: VM tắt, intended VM chưa rõ | `docs/network-setup.md`; VirtualBox, `ip -4 addr`, `ss -lntp` output thật |
| HTTP-04 — Windows TCP, HTTP GET, Chrome | Owner chờ gán / NOT STARTED | `docs/network-test-cases.md`; TCP, HTTP status/body và browser có output riêng |
| HTTP-05 — Evidence và hướng dẫn chạy lại | Owner chờ gán / NOT STARTED | `docs/network-test-cases.md`; screenshot/output thật, ngày, IP, port, source hash và reviewer |

### Thứ tự chạy và tiêu chí

1. Xác nhận đúng VM trong VirtualBox; xem adapter trước khi đổi cài đặt.
2. Ubuntu: `ip -4 addr`; ghi guest IP/interface.
3. Chạy server ứng viên; Ubuntu: `ss -lntp | grep 22236` để xem listener thật.
4. Windows: `ipconfig`, rồi `Test-NetConnection <GUEST_IP> -Port 22236`.
5. Chỉ sau TCP PASS, chạy `curl.exe -v http://<GUEST_IP>:22236/`.
6. Mở cùng URL trên Chrome Windows; xác nhận trang được render.
7. Lưu terminal/server log và screenshot thật.

**Pass riêng:** VM boot → listener trên guest → TCP tới được → HTTP status/body đúng → browser render. TCP PASS không chứng minh HTTP PASS. Không tắt firewall toàn cục hoặc mở server ra Internet công cộng. Host-only là phương án **PROPOSED**; chưa đổi adapter.

## 7. Lịch làm việc (PROPOSED SCHEDULE)

- **D0:** nhóm xác nhận tên, cặp, HTTP owner/backup và người tích hợp.
- **D0–D1:** đọc nguồn, đọc draft AI, ghi assumptions và prompt thật.
- **D1–D2:** mỗi cặp hoàn thiện thuật toán, sơ đồ, ví dụ và trade-off.
- **D2:** review chéo theo [checklist](team-review-checklist.md), sửa interface chung.
- **Trước buổi Lab 2:** rehearsal giải thích và chạy HTTP demo nếu VM/source sẵn sàng.

Chưa có ngày Lab 2 xác minh; không đổi lịch tương đối này thành ngày cụ thể.

## 8. Workflow nhóm và cập nhật GitHub

**Nhận việc → nghiên cứu nguồn → cặp tạo bản nháp → review chéo → chỉnh sửa → chốt thiết kế.** Mỗi cặp cập nhật file thiết kế đúng chủ đề. Nếu quen Git, dùng branch + Pull Request. Nếu chưa quen, chỉ một người tích hợp; mỗi cặp gửi patch riêng, tránh nhiều người sửa cùng file một lúc.

Repo [TiKyisme/co3094-lab2-network-streaming](https://github.com/TiKyisme/co3094-lab2-network-streaming) đang private. Chủ repo mời thành viên sau; tài liệu này không tự cấp quyền. Tiến độ/evidence ghi ở [team assignments](team-assignments.md), prompt ghi ở `prompts/`, thay đổi lớn ghi ở `log.txt`.

## 9. Prompt evidence và liêm chính học thuật

Lưu prompt thực tế nguyên văn; không tạo prompt hồi cứu. Ghi rõ phần nào AI gợi ý, nhóm sửa gì, nguồn nào xác nhận và ai review. Không commit password/token, email riêng tư, transcript chưa rà soát, hoặc bản gốc ZIP/PDF/slide/source có bản quyền. Xem [prompt evidence instructions](prompt-evidence-instructions.md).

## 10. Checklist trước buổi Lab 2

- [ ] Xác nhận đủ sáu tên; giữ hai tên Reliability là tentative cho tới khi hai bạn xác nhận.
- [ ] Điền bốn placeholder và gán HTTP owner/backup.
- [ ] Xác định server official hay group reconstruction, không nhập nhằng hai mã nguồn.
- [ ] Biết guest IP, interface, listener address/port và adapter thật.
- [ ] Có output riêng cho boot, listener, TCP, HTTP status/body và browser.
- [ ] Mỗi cặp có thuật toán, sơ đồ, state/message, hai ví dụ, trade-off, prompt evidence.
- [ ] Review chéo đủ ba interface; cả sáu giải thích được thiết kế.
- [ ] Assignment 1 conflict, deadline và deliverables Lab 2 chưa xác nhận vẫn được gắn nhãn.

## 11. Tài liệu và trạng thái nguồn

- Source inventory: https://github.com/TiKyisme/co3094-lab2-network-streaming/blob/main/docs/source-inventory.md
- Requirements/conflicts: https://github.com/TiKyisme/co3094-lab2-network-streaming/blob/main/docs/requirements-matrix.md
- HTTP analysis and setup: https://github.com/TiKyisme/co3094-lab2-network-streaming/blob/main/docs/http-server-analysis.md and https://github.com/TiKyisme/co3094-lab2-network-streaming/blob/main/docs/network-setup.md
- Streaming overview and integration: https://github.com/TiKyisme/co3094-lab2-network-streaming/blob/main/docs/streaming-architecture.md and https://github.com/TiKyisme/co3094-lab2-network-streaming/blob/main/docs/integration-design.md
- Team handover, task cards, review checklist and announcement: https://github.com/TiKyisme/co3094-lab2-network-streaming/blob/main/docs/team-handover.md, https://github.com/TiKyisme/co3094-lab2-network-streaming/blob/main/docs/team-assignments.md, https://github.com/TiKyisme/co3094-lab2-network-streaming/blob/main/docs/team-review-checklist.md, https://github.com/TiKyisme/co3094-lab2-network-streaming/blob/main/docs/team-announcement.md
- Prompt evidence rules: https://github.com/TiKyisme/co3094-lab2-network-streaming/blob/main/docs/prompt-evidence-instructions.md
- [Google Docs gốc — đồng bộ đang chờ](https://docs.google.com/document/d/1hxqLAD0eRfdBhDJJyopSYi0vFqJUDhFCy7lOGO2CxQ/edit). Lần đọc native hiện tại trả 404; không tạo bản Google Docs trùng.

**Chưa được xác nhận:** full server-process file, intended VM/topology, guest IP/firewall, roster cuối, HTTP owners, Lab 2 date, report/screenshot/prototype requirements, và các mâu thuẫn Assignment 1. Không trạng thái nào ở trên được xem là giảng viên duyệt.
