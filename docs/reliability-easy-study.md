# Học nhanh Reliability theo slide (5-10 phút)

## Ý tưởng chính

Kênh truyền có thể làm packet bị hỏng hoặc bị mất. Sender không thể chỉ gửi rồi đoán là receiver đã nhận. RDT (Reliable Data Transfer, truyền dữ liệu tin cậy) 3.0 trong bài giảng dùng checksum, sequence number, ACK và timer để sender biết khi nào có thể gửi packet tiếp theo hoặc cần gửi lại packet cũ.

Nhóm đang đề xuất dùng **stop-and-wait** làm bản draft Reliability: gửi một packet, rồi chờ ACK của packet ấy. Đây là cách đơn giản để trình bày; hai thành viên vẫn cần xác nhận nó có phù hợp với mục tiêu streaming của Lab 2 không.

## Thuật ngữ bằng lời đơn giản

| Thuật ngữ | Nghĩa và ví dụ |
|---|---|
| Ứng dụng | Chương trình tạo hoặc nhận dữ liệu; ví dụ receiver giao dữ liệu lên ứng dụng sau khi packet hợp lệ. |
| Sender | Bên đang gửi data; trong slide 63, sender gửi pkt0 rồi chờ. |
| Receiver | Bên nhận và kiểm tra packet; ví dụ receiver gửi ACK0 sau khi nhận pkt0 đúng. |
| RDT 3.0 | Một phiên bản cơ chế truyền dữ liệu tin cậy trong bài giảng, dùng sequence number, ACK và timer; ví dụ slide 63(b) gửi lại pkt1 sau khi timer hết hạn. |
| Packet | Một gói chứa data và thông tin kiểm tra; slide 61 tạo packet từ sequence number, data và checksum. |
| Checksum | Một giá trị giúp phát hiện bit trong packet có bị đổi hay không; slide 47 dùng checksum để phát hiện lỗi bit. |
| Sequence number | Nhãn 0 hoặc 1 cho packet hiện tại để receiver nhận ra packet mới hay bản gửi lại; slide 56 nói hai số này là đủ cho cách này. |
| ACK | Thông báo nhận đúng một packet; ACK0 xác nhận packet có sequence number 0. |
| Timer | Đồng hồ đếm thời gian sender chờ ACK; khi timer hết hạn, sender gửi lại packet đang chờ. |
| Duplicate | Packet đã được nhận trước đó nhưng được gửi lại; receiver dùng sequence number để không giao data đó lần thứ hai. |
| Stop-and-wait | Sender chỉ có một packet đang chờ ACK; ví dụ sender chờ ACK0 rồi mới gửi pkt1. |

## Cách RDT 3.0 diễn ra

1. Ứng dụng đưa data cho sender.
2. Sender gắn sequence number 0 hoặc 1 và checksum vào packet, gửi packet, rồi bật timer.
3. Receiver kiểm tra checksum và sequence number đang chờ. Nếu packet đúng, receiver giao data lên trên một lần và gửi ACK có sequence number của packet.
4. Sender nhận đúng ACK thì dừng timer, chuyển sang sequence number còn lại, rồi mới gửi packet tiếp theo.
5. Nếu packet hoặc ACK bị mất, sender không nhận ACK đúng và timer hết hạn. Sender gửi lại chính packet đã lưu với cùng sequence number rồi bật lại timer.
6. Nếu receiver đã nhận packet trước đó, sequence number cho biết đây là bản gửi lại. Receiver không giao data lần nữa, nhưng gửi lại ACK để sender có thể tiếp tục.

Slide chỉ yêu cầu chờ một khoảng thời gian “hợp lý”; slide không đưa ra một con số timeout tính bằng mili-giây. Bản draft vì vậy không tự thêm công thức hay giá trị timeout.

## Hai tình huống trong slide

- **Không mất packet:** slide 63(a) cho thấy sender gửi pkt0, nhận ACK0, gửi pkt1, nhận ACK1, rồi quay về pkt0.
- **ACK bị mất:** trong slide 64(c), receiver đã nhận pkt1 nhưng ACK1 bị mất. Timer làm sender gửi lại pkt1; receiver nhận ra sequence number trùng, không giao data lần hai và gửi ACK1 lại.

## 5 câu hỏi vấn đáp

1. **Checksum dùng để làm gì?** Giúp receiver phát hiện packet có thể bị lỗi bit.
2. **Vì sao cần sequence number 0 và 1?** Để receiver phân biệt packet mới với packet được sender gửi lại.
3. **ACK0 có nghĩa gì?** Receiver báo đã nhận đúng packet mang sequence number 0.
4. **Sender làm gì khi timer hết hạn?** Gửi lại packet đang chờ với cùng sequence number và bật lại timer.
5. **Làm sao receiver không giao data hai lần khi ACK bị mất?** Receiver nhận ra sequence number đã thấy, bỏ lần giao trùng và gửi lại ACK.

## Chia nhau chuẩn bị

- **Gia Đạo:** đọc thuật ngữ, các bước 1-4 và slide 45, 47-58; giải thích checksum, sequence number, ACK và packet trùng.
- **Thiên Kỳ:** đọc các bước 4-6, hai ví dụ và slide 59-67; giải thích timer, retransmission, packet/ACK loss và hạn chế stop-and-wait.

## Nguồn đã đối chiếu

- `Chapter 3_ Transport Layer - Chapter_3_v9.0.pptx`: slides 47-48, 53, 56-64, 66-67; số chân trang tương ứng là `Transport Layer: 3-n`. PDF cùng bài giảng có các trang tương ứng.
- `docs/reliability-slide-only.md` ghi rõ slide nào hỗ trợ từng phần và tách riêng các đề xuất của nhóm.
