# Hướng dẫn lưu prompt AI

Mục tiêu là giữ lại prompt đã dùng thật để nhóm có thể giải thích cách xây dựng và kiểm tra thiết kế. Không viết lại lịch sử sau khi biết kết quả.

## Với mỗi phiên làm việc

1. Lưu prompt người dùng thực tế nguyên văn thành `prompts/YYYY-MM-DD-<topic>-<member-id>.txt`.
2. Nếu trao đổi kéo dài, ghi các lần thay đổi yêu cầu riêng theo thứ tự; không chỉ lưu prompt đầu tiên.
3. Trong file thiết kế, ghi prompt nào hỗ trợ phần nào và nhóm đã chấp nhận, sửa hay bác bỏ gợi ý nào.
4. Ghi nguồn kỹ thuật/giảng viên độc lập với câu trả lời AI.
5. Giữ log ngắn về người review, quyết định và commit liên quan. Không sửa prompt cũ để làm nó trông tốt hơn.

## Không đưa vào repo

- Mật khẩu, token, dữ liệu tài khoản, email riêng tư hoặc thông tin cá nhân không cần thiết.
- Toàn bộ email, tin nhắn riêng, transcript chat chưa được rà soát.
- ZIP/PDF/slide hoặc source nguyên bản có bản quyền của môn học. Ghi metadata và trang cần dẫn; giữ bản gốc ở vị trí do nhóm quản lý.

## Đánh dấu nội dung

- `AI SUGGESTION`: ý do công cụ gợi ý.
- `TEAM DECISION`: lựa chọn đã được các thành viên liên quan đọc và thống nhất.
- `UNVERIFIED`: chưa có nguồn hoặc bằng chứng thực tế.
- `CONFLICT`: có hai nguồn chỉ dẫn khác nhau.

Chỉ prompt thực tế mới là evidence. File này là hướng dẫn mới, không thay thế các prompt đã lưu trước đó trong `prompts/`.
