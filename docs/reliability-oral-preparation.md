# Reliability oral preparation

**Mục tiêu:** hiểu draft đủ để tự giải thích, nhận ra giả định, và đề xuất cách sửa khi tình huống thay đổi.  
**Trạng thái:** tài liệu ôn tập AI-assisted; chưa được hai sinh viên review.  
**Owners:** REL-01 Nguyễn Đăng Gia Đạo và REL-02 Nguyễn Đổng Thiên Kỳ, TENTATIVE.

## 1. Từ cơ bản đến mức bảo vệ thiết kế

### Packet

Một packet là đơn vị truyền qua mạng. Một packet có thể chở ACK, reliable data, real-time data, hoặc nhiều frame. Mất một packet chỉ nói rằng một lần truyền có thể không tới; chưa tự nói message nào đã được ứng dụng xử lý.

### Packet number (PN)

PN tăng theo từng chiều gửi và nhận diện một lần truyền cụ thể. Ví dụ, command ở offset 100 có thể được gửi lần đầu trong PN 14, rồi gửi lại trong PN 18. PN mới cho biết đó là lần gửi khác, dù data range giống nhau.

### Stream offset và message boundary

Offset là vị trí byte trong một reliable channel. Nếu byte range 100-199 bị mất, retransmission giữ đúng offset 100. Receiver ghép các byte đến sai thứ tự và chỉ giao message hoàn chỉnh khi mọi byte trước đó đã có. Framing cho biết ranh giới message; offset không tự thay thế framing.

### ACK và ACK range

ACK xác nhận packet-number range đã tới receiver ở tầng transport. Nó không xác nhận ứng dụng đã lưu file, hoàn tất giao dịch, hoặc chạy side effect. Một ACK range như [21,22] và [25,25] báo 21, 22, 25 đã tới; 23-24 vẫn là gap chưa được ACK. ACK có thể lặp lại range cũ để bù cho một ACK đã bị mất.

### Duplicate packet và duplicate content

Nếu cùng một PN tới hai lần, receiver bỏ lần xử lý sau. Nếu cùng byte range được retransmit trong một packet PN khác, packet không trùng nhưng content trùng. Receiver dedupe bằng channel/offset, không chỉ bằng PN.

### Packet loss và reordering

Packet đến trễ có thể tạo gap tạm thời. Nếu sender kết luận loss ngay khi thấy gap, nó có thể retransmit thừa. Draft chờ ACK của packet mới hơn và dùng packet threshold hoặc time threshold để có thêm bằng chứng.

### Probe Timeout (PTO)

PTO là lúc gửi probe để hỏi xem đường truyền còn tiến triển không, nhất là khi packet cuối hoặc ACK cuối bị mất. Theo RFC 9002, PTO expiry không tự đánh dấu packet cũ là lost. Draft này giữ đúng sự phân biệt đó.

### Selective retransmission

Khi loss được xác nhận, gửi lại những reliable byte ranges còn unacknowledged, không phát lại nguyên packet cũ. Mỗi retransmission có PN mới. Nếu dữ liệu không còn hữu ích trước khi gửi, ứng dụng có thể bỏ hoặc phải có semantics hủy rõ ràng.

### Out-of-order buffer và flow control

Receiver giữ range mới hơn trong lúc đợi lỗ hổng. Dữ liệu đang đợi vẫn chiếm bộ nhớ, nên phải tính vào receive credit. ACK packet không có nghĩa application đã consume buffer; Flow Control chỉ tăng absolute limit khi có dung lượng được giải phóng thật.

### Head-of-Line (HoL) blocking

Ordered delivery làm channel bị gap phải đợi. Với nhiều channel độc lập, gap trong channel 1 không bắt buộc chặn channel 2. Nhưng congestion, buffer đầy, scheduler hoặc packet chứa nhiều frame vẫn có thể tạo trễ chung. Không được nói thiết kế loại bỏ mọi HoL.

### Expiring real-time update

Update mới thường hữu ích hơn update cũ. Sender bỏ update đã hết hạn khỏi queue và không retransmit update bị mất. Receiver dùng update sequence để loại bản cũ. Nếu cần kiểm tra deadline tuyệt đối qua hai máy, phải thống nhất clock hoặc cách biểu diễn thời gian; clock đơn điệu riêng của mỗi máy không so sánh trực tiếp được.

### Exactly-once boundary

Transport duplicate suppression có thể ngăn một command đang còn trong cùng session được giao hai lần do retransmission. Nó không đảm bảo một side effect đúng một lần qua crash/reconnect khi trạng thái receiver mất. Với thao tác quan trọng, application cần command ID bền vững và idempotent processing hoặc transaction acknowledgment.

## 2. Mười câu hỏi có thể được hỏi

### 1. Packet number khác stream offset thế nào?

**Trả lời ngắn:** packet number nhận diện một lần gửi; stream offset nhận diện vị trí byte của reliable data. Retransmission dùng PN mới nhưng giữ offset của bytes đó.

**Vì sao:** nếu gộp hai số này, sender khó biết packet nào mất và receiver khó ghép dữ liệu đã tới sai thứ tự.

### 2. ACK range [105,106] và [101,102] nói gì?

**Trả lời ngắn:** receiver đã nhận 101, 102, 105, 106; 103-104 là gap chưa được ACK. Chưa thể kết luận ngay 103-104 mất.

**Vì sao:** mạng có thể reorder; sender cần packet/time threshold trước khi retransmit.

### 3. Packet ACK chứng minh ứng dụng đã chạy command chưa?

**Trả lời ngắn:** chưa. Nó chứng minh packet tới transport layer. Ứng dụng cần acknowledgment riêng nếu sender phải biết command đã commit.

**Vì sao:** transport có thể buffer bytes trước khi ứng dụng đọc hoặc xử lý chúng.

### 4. Vì sao retransmission cần packet number mới?

**Trả lời ngắn:** đó là transmission attempt mới; packet tracking và ACK/loss accounting phải phân biệt được lần đầu với lần gửi lại.

**Vì sao:** nếu dùng lại PN, receiver có thể coi data retry là packet duplicate và bỏ nó.

### 5. Khi nào gap trở thành loss trong baseline?

**Trả lời ngắn:** khi có ba packet ack-eliciting mới hơn được ACK hoặc time threshold được đáp ứng. Packet number của ACK-only không được tính vào ngưỡng này. Một PN bị thiếu riêng lẻ chưa đủ.

**Vì sao:** chờ thêm bằng chứng giảm spurious retransmission do reordering. Các ngưỡng là technical reference từ RFC 9002, không phải yêu cầu môn học.

### 6. PTO hết hạn có nghĩa packet bị mất không?

**Trả lời ngắn:** không. Sender gửi probe để lấy ACK progress. Packet chỉ được mark lost theo loss-detection thresholds.

**Vì sao:** PTO còn khắc phục được ACK bị mất hoặc tail loss; nó không chứng minh packet trước đó không tới.

### 7. Receiver làm gì với reliable bytes đến sai thứ tự?

**Trả lời ngắn:** kiểm tra offset/credit, giữ missing ranges trong buffer, và chỉ giao message hoàn chỉnh tại next contiguous offset của channel.

**Vì sao:** ứng dụng yêu cầu ordered data không nên thấy message sau trước message trước; Flow Control giới hạn bộ nhớ đợi.

### 8. Làm sao tránh xử lý retransmitted command hai lần?

**Trả lời ngắn:** cùng PN thì packet duplicate filter bỏ packet; PN mới nhưng cùng byte range thì reassembler bỏ overlap theo channel/offset và giao frame một lần.

**Vì sao:** retransmission luôn là packet mới nên chỉ lọc PN là chưa đủ.

### 9. Có loại bỏ HoL blocking không?

**Trả lời ngắn:** không hoàn toàn. Gap chặn ordered delivery trong reliable channel đó. Channel độc lập có thể tiến triển, nhưng scheduler, congestion, hoặc buffer vẫn có thể gây trễ.

**Vì sao:** cần nêu đúng phạm vi bảo đảm, không biến “nhiều channel” thành “không bao giờ bị block”.

### 10. Nếu state update cũ bị mất thì sender có retransmit không?

**Trả lời ngắn:** không. Sender bỏ update hết hạn; receiver bỏ sequence cũ. Reliable commands và expiring updates có semantics khác nhau.

**Vì sao:** gửi lại state cũ có thể làm latency và freshness xấu hơn. Update vẫn chịu congestion control dù không retransmit.

## 3. Ba tình huống đổi giả định để kiểm tra hiểu biết

### Tình huống A: mạng reorder mạnh

**Thay đổi:** PN 40 bị trì hoãn; PN 41-44 tới trước.  
**Cần trả lời:** ACK các packet mới hơn để báo reordering, nhưng chưa gửi lại PN 40 trước khi packet/time threshold đạt. Nếu ACK PN 40 tới sau khi sender đã mark loss, nhận late ACK, không trừ bytes-in-flight lần hai, và hủy retry nếu chưa gửi. Nếu pattern này lặp lại, xem lại ngưỡng bằng số liệu thay vì nói mọi gap đều loss.

### Tình huống B: receiver buffer gần đầy

**Thay đổi:** receiver đã nhận out-of-order bytes nhưng ứng dụng chậm consume.  
**Cần trả lời:** Flow Control không tăng credit đến khi có dung lượng thật; sender dừng gửi new offsets khi credit hết. Retransmission của offset đã được cấp credit vẫn cần congestion budget và có thể cần buffer để receiver hoàn thiện range. Update realtime dùng bounded latest-value queue, không làm reliable buffer vô hạn.

### Tình huống C: sender/receiver reconnect sau receiver crash

**Thay đổi:** receiver đã chạy command nhưng crash trước khi ACK sender; trạng thái dedupe mất.  
**Cần trả lời:** draft transport không thể đảm bảo exactly-once qua restart. Dùng command ID bền vững, idempotent handler hoặc application transaction/ack. Không khẳng định packet ACK giải quyết được crash consistency.

## 4. Phần review của hai owner

### REL-01 - Nguyễn Đăng Gia Đạo (TENTATIVE)

Đọc trong [reliability-design.md](reliability-design.md):

- Mục 3-5: phân biệt PN, stream offset, ACK semantics và state tables.
- Mục 8: pseudocode xử lý ACK và receiver ACK generation.
- Mục 9, diagrams 1 và 3: normal ACK và lost ACK.
- Mục 16: chốt packet/message semantics, ACK policy, ACK range cap.

Review checklist cá nhân:

- [ ] Xác nhận packet number theo từng chiều gửi và không lặp trong session.
- [ ] Xác nhận ACK ranges chỉ nói packet receipt, không nói application commit.
- [ ] Giải thích duplicate packet khác retransmitted reliable range.
- [ ] Đề xuất range cap và cách giữ minimum acceptable PN.
- [ ] Gửi câu hỏi cho REL-02 về state/offset mapping.

### REL-02 - Nguyễn Đổng Thiên Kỳ (TENTATIVE)

Đọc trong [reliability-design.md](reliability-design.md):

- Mục 7-8: loss thresholds, PTO, backoff, retry cap, pseudocode.
- Mục 9, diagrams 2, 4 và loss/recovery state diagram.
- Mục 10-13: ví dụ, scenario table và phạm vi HoL.
- Mục 15-16: test cases dự kiến và quyết định còn mở.

Review checklist cá nhân:

- [ ] Xác nhận packet/time threshold đủ chịu reordering cho mục tiêu demo.
- [ ] Giải thích vì sao PTO không tự mark packet lost.
- [ ] Xác nhận late ACK không làm bytes-in-flight âm hoặc giảm hai lần.
- [ ] Chốt cách hủy retry và xử lý data hết hữu ích.
- [ ] Gửi câu hỏi cho REL-01 về ACK ranges và offset confirmation.

## 5. TEAM REVIEW REQUIRED

Chỉ sinh viên mới được đánh dấu các mục sau sau khi tự review. Hiện tại tất cả đều chưa được xác nhận:

- [ ] Gia Đạo đã review ACK design.
- [ ] Thiên Kỳ đã review retransmission design.
- [ ] Hai người đã thống nhất packet/message semantics.
- [ ] Đã đối chiếu Flow Control.
- [ ] Đã đối chiếu Congestion Control.
- [ ] Đã chọn cuối cùng giữa các alternative.
- [ ] Cả hai đã giải thích được bốn sequence diagrams và recovery state diagram.
- [ ] Đã lưu prompt AI thực tế của sinh viên; master prompt này không thay thế prompt của sinh viên.

**Chưa đạt READY_FOR_LAB_REVIEW.** Sau khi hai người xác nhận và cập nhật bằng chứng, hãy đổi status theo quyết định thật của nhóm; không tự đánh dấu hoàn tất.

## 6. Câu hỏi cần thống nhất trước Lab

1. REL-01 và REL-02 có xác nhận vai trò không?
2. Message framing có cần command ID/application ACK ngoài stream offset không?
3. Một hay nhiều reliable channel? Channel nào cần in-order?
4. Có dùng 5 PTO no-progress cap trong bản trình bày, hay chọn khác? Đây là giả định ứng dụng.
5. Deadline update dùng clock sync, remaining lifetime, hay chỉ sender-side expiry plus sequence freshness?
6. ACK-only packet có chịu bytes-in-flight/pacing theo đề xuất Congestion Control pair không?
7. Flow Control muốn connection credit, channel credit, hay cả hai?
8. Thầy muốn conceptual draft hay một UDP prototype trong Lab 2? Email hiện có chỉ xác nhận draft design.

## 7. Kế hoạch trả lời ngắn

Nếu bị hỏi một tình huống mới, trả lời theo bốn bước:

1. Nêu trạng thái đã biết: PN nào ACK, range nào còn thiếu, credit và congestion budget còn bao nhiêu.
2. Phân biệt packet loss với content chưa được xác nhận.
3. Nêu rule đang áp dụng: threshold, PTO, retransmit range mới PN, dedupe/ordered delivery.
4. Nêu giả định còn phải nhóm hoặc giảng viên xác nhận.

## 8. Technical references

- [RFC 9000](https://www.rfc-editor.org/rfc/rfc9000.html): packet numbers, ACK ranges, retransmission of information, and flow-controlled streams.
- [RFC 9002](https://www.rfc-editor.org/rfc/rfc9002.html): RTT, loss thresholds, PTO, and congestion control.
- [RFC 9221](https://www.rfc-editor.org/rfc/rfc9221.html): unreliable QUIC DATAGRAM extension and its congestion-control boundary.
- [Valve GameNetworkingSockets packet wire format](https://github.com/ValveSoftware/GameNetworkingSockets/blob/master/src/steamnetworkingsockets/clientlib/SNP_WIRE_FORMAT.md): example reliable message segments, ACK blocks, and new PN on retransmission.

These are technical references only. They do not establish that CO3094 requires QUIC or this packet format.
