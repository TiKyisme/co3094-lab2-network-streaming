# Ma trận yêu cầu

Nguồn chính là hai đoạn email do người dùng cung cấp trong prompt. Email gốc và LMS chưa được mở độc lập; các dòng về yêu cầu chính thức vì vậy truy xuất được tới bản trích dẫn trong prompt, chưa xác minh bằng hộp thư/LMS.

| Yêu cầu / nhận định | Phân loại | Nguồn | Diễn giải / giới hạn |
|---|---|---|---|
| Máy thật truy cập HTTP server chạy trong VM | REQUIRED | Email A, 08/10/2026 (trích trong prompt) | Mục tiêu kết nối host → VM. Chưa biết IP, port, VM network mode, hay định dạng nộp. |
| Dùng `new_connection` đã được thầy ghi đè trên forum | REQUIRED | Email A | Cần lấy nguyên văn code từ đúng forum; hiện UNVERIFIED vì LMS/forum không truy cập được. |
| Chuẩn bị draft design cho reliability, flow control, congestion control | REQUIRED | Email A và Email B | Bản nháp là mức được nêu; chưa có yêu cầu implement cả ba cơ chế. |
| Ví dụ Steam UDP gaming và Google QUIC | SUPPORTED | Email A (“ví dụ”) | Ví dụ tham khảo; không phải yêu cầu sao chép hay tương thích toàn bộ giao thức. |
| Nhóm 6 người, khoảng 2 người/cơ chế | REQUIRED / SUPPORTED | Email B | Cơ cấu tương đối; danh tính và phân công thật do nhóm xác nhận. |
| Lưu lịch sử prompt/chat AI | REQUIRED | Email A và Email B | Cần giữ prompt nguyên văn và export gốc. Không commit bí mật; repo dự kiến private. |
| Vấn đáp Assignment 1 trong tuần có 17/11/2026 | REQUIRED cho Assignment 1 | Email B như được người dùng diễn giải | Không phải deadline Lab 2. Không suy ra ngày cụ thể. |
| Lab 2 bắt buộc Telnet, hai ảnh, một báo cáo hay một loại file cụ thể | UNVERIFIED | Không có trong email A/B | Không trình bày thành yêu cầu. Có thể giữ ảnh/log để nhóm tự kiểm tra nội bộ. |
| Lab 2 bắt buộc UDP hoặc QUIC/Steam | UNVERIFIED | Email chỉ nêu ví dụ | Hỏi giảng viên trước khi chốt protocol nền. |
| Lab 2 bắt buộc code/prototype cho ba cơ chế | UNVERIFIED | Email B nói “draft design” | Hiện hiểu là thiết kế nháp; cần hỏi nếu code ảnh hưởng phân công/thời gian. |
| Port 22236 | UNVERIFIED | Chỉ xuất hiện trong Google Doc cũ | Không sử dụng nếu source thật không xác nhận. |
| Dùng Host-only để Windows↔Ubuntu | PROPOSED kỹ thuật | Oracle VirtualBox manual 7.2 | Hợp với host↔guest và không nối VM ra LAN/Internet; không phải yêu cầu của thầy. |
| Assignment 1 là ứng dụng mạng | SUPPORTED | CO3093 adjacent bundle only | Không dùng làm bằng chứng yêu cầu CO3094; email B cung cấp bối cảnh riêng cho CO3094. |

## Nguyên tắc
- `REQUIRED` chỉ dành cho câu nói trực tiếp trong email được cung cấp.
- `SUPPORTED` là diễn giải có căn cứ rõ nhưng không thêm nghĩa vụ mới.
- `PROPOSED` là quyết định kỹ thuật của nhóm, cần được nhóm/thầy rà soát.
- `UNVERIFIED` là điều chưa có nguồn đủ thẩm quyền.
