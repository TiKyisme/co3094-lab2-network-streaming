# CO3094 Lab 2 — HTTP Networking & Streaming Design

Tài liệu làm việc riêng để chuẩn bị Lab 2 và ghi lại bằng chứng nghiên cứu. Repository được tạo tách khỏi course bundle; GitHub target là **private** theo yêu cầu, không công khai.

## Phạm vi từ email thầy do người dùng cung cấp

- Máy thật truy cập HTTP server chạy trong VM bằng phiên bản `new_connection` thầy ghi đè trên forum.
- Nhóm chuẩn bị draft design cho Reliability, Flow Control và Congestion Control.
- Nhóm có sáu thành viên, khoảng hai người cho mỗi cơ chế.
- Lưu lịch sử prompt/AI để trình bày khi được yêu cầu.
- Tuần có ngày 17/11/2026 là mốc vấn đáp Assignment 1, không phải deadline Lab 2.

Giao thức, mã nguồn, port, deliverables và ảnh minh chứng chưa được email xác nhận. Xem [ma trận yêu cầu](docs/requirements-matrix.md).

## Trạng thái

- Phase 1: khảo sát một phần; đường dẫn CO3094/L07 trong môi trường không tồn tại. Bộ tài liệu lân cận là CO3093 và được gắn nhãn riêng.
- Phase 2: đã review nội dung chữ Google Doc từ Drive Search; chưa thể xác minh cấu trúc native hoặc sửa bản gốc do Docs API trả 404. Xem [review](docs/docs-review.md) và [bản Markdown hiệu chỉnh](docs/lab2-group-guide.md).
- Phase 3: chưa xác minh code của thầy; `new_connection` UNVERIFIED. Cần code forum và kiểm thử thật trên Windows–Ubuntu.
- Phase 4: tài liệu streaming là PROPOSED; chưa triển khai hay kiểm thử.
- Phase 5: repository local được tạo tại `D:\01. Dai_Hoc_Dai_Dai_Di\05. HK1_NAM3\co3094-lab2-network-streaming`; GitHub private repo chưa được tạo.

## Đọc theo thứ tự

1. [state.md](state.md)
2. [log.txt](log.txt)
3. [requirements matrix](docs/requirements-matrix.md)
4. [source inventory](docs/source-inventory.md)
5. [Google Docs review](docs/docs-review.md)
6. [network setup](docs/network-setup.md) và [HTTP source analysis](docs/http-server-analysis.md)
7. [streaming architecture](docs/streaming-architecture.md), [reliability](docs/reliability-design.md), [flow control](docs/flow-control-design.md), [congestion control](docs/congestion-control-design.md), [integration](docs/integration-design.md)
8. [team assignments](docs/team-assignments.md) và [open questions](docs/open-questions.md)

## Cấu trúc và chạy demo

- `docs/`: yêu cầu, nguồn, review, hướng dẫn mạng và thiết kế nháp.
- `prompts/`: prompt người dùng thực tế; full session export vẫn cần được bảo quản riêng.
- `evidence/`: chỉ chứa bằng chứng thật sau khi nhóm kiểm thử.
- Chưa có `src/`: code server gốc của lớp chưa được cung cấp/định vị; không thay bằng code tự viết rồi gọi là code của thầy.
- Chưa có lệnh chạy chính xác. Khi có source sẽ ghi đúng interpreter, port và tham số. Không dùng port 22236 nếu source không xác nhận.

## Tiếp tục

Đọc state và cuối log trước; kiểm tra Git status; lấy đúng CO3094/L07 folder và forum code; sau đó chạy test thủ công theo network setup. Thành viên tự xác nhận roster. Mọi đề xuất vẫn phải được nhóm kiểm tra và giải thích.
