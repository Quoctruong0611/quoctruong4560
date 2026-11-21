# 90S Cargo Express – Marketing Facebook page (bàn giao từ Claude chat, 19/11/2026)

Bạn (Claude Code) đang tiếp quản dự án marketing cho page Facebook **90S Cargo Express**
(https://www.facebook.com/90scargoexpress) của anh Trường. Trả lời bằng tiếng Việt.

## Mục tiêu
Tìm khách có nhu cầu gửi hàng đi nước ngoài, ưu tiên tuyến **Hàn Quốc** và **Úc**.
Anh Trường muốn: đăng 3 bài/ngày tự động, đăng ngay 5 bài đầu, chạy quảng cáo trên các bài đó.

## Thông tin doanh nghiệp (do chủ page cung cấp – chỉ dùng đúng các thông tin này)
- Hàn Quốc: giá ưu đãi **75.000đ/kg cho đơn từ 21kg**
- Úc: giá ưu đãi **135.000đ/kg cho đơn từ 21kg**
- Thời gian giao: **3–5 ngày kể từ ngày bay**
- Miễn phí pickup nội ô HCM, Bình Dương, Đồng Nai bán kính 30km cho đơn hàng 20kg
  (đang hiểu là "đơn từ 20kg" – chưa xác nhận lại)
- Hoặc khách gửi chành xe / công ty pickup về kho, 90S chụp hình và đóng gói
- Quy trình: 1) Nhận hàng 2) Kiểm tra, phân loại hàng khô – chất lỏng
  3) Đóng thùng, hỗ trợ hút chân không, cân kg, đo kích thước, báo giá
  4) Đợi ngày bay, khách có mã tracking theo dõi tới tay người nhận
- Văn phòng: 585/12/18 Quốc lộ 13, P. Hiệp Bình, Thủ Đức, TP.HCM
- Kho: 191A Gò Dưa, P. Tam Bình, Thủ Đức, TP.HCM
- Zalo/WhatsApp: 0334 477 577 – 0339 788 798 (website 90scargo.com ghi 0925 424 242 – không dùng)
- Website 90scargo.com còn chữ mẫu lorem ipsum, mã [instagram-feed] lỗi, dịch vụ thừa – cần dọn

## Đã làm trên page (19/11/2026)
- Tiểu sử mới (4 dòng: gửi hàng quốc tế, gom hàng/thông quan, địa chỉ VP, Zalo)
- Hạng mục: Công ty vận tải hàng hóa · Dịch vụ chuyển phát nhanh · Dịch vụ vận chuyển & lưu trữ
- Liên kết: 90scargo.com + zalo.me/0334477577
- Dịch vụ: Chuyên tuyến Hàn Quốc, Khai báo & thông quan hải quan, Gom hàng đại lý,
  Vận chuyển hàng không & đường biển
- Ghim bài tuyến Hàn Quốc ngày 9/11/2026 vào mục "Đáng chú ý"

## Trong thư mục này
- `posts/1_han_gia.jpg … 5_uc_tet.jpg` – 5 ảnh 1080x1080 đã duyệt
- `posts/captions.md` – nội dung 5 bài, anh Trường đã duyệt đăng
- `make_images.py` – tạo ảnh bằng HTML + Playwright (font Montserrat, cam #FF7A1A, nền navy #0E1A2B).
  Sửa dict `POSTS` để làm ảnh mới; cần `pip install playwright` và một Chrome/Chromium.
- `ke-hoach.md` – kế hoạch nội dung, quảng cáo, KPI

## Việc còn dang dở – làm tiếp theo thứ tự
1. **Đăng 5 bài** trong `posts/captions.md` kèm ảnh tương ứng. Anh Trường đã duyệt nội dung.
   Chat bị chặn vì không tải được ảnh lên. Các cách khả thi trên máy anh:
   - Meta Graph API: tạo app ở developers.facebook.com, lấy Page access token
     (quyền pages_manage_posts), gọi `POST /{page-id}/photos` với `source` = file ảnh,
     `message` = caption. Page ID: 658414260680854.
   - Hoặc vidIQ (đã có trong Claude, hỗ trợ Facebook Pages): anh cần kết nối page qua
     vidiq_social_account_connect, rồi upload ảnh và tạo bài.
   - Hoặc anh tự đăng qua Meta Business Suite (nhanh nhất).
   Giãn cách bài, không đăng 5 bài cùng lúc (ví dụ 2 bài hôm nay, 3 bài ngày mai).
2. **Quảng cáo**: đề xuất quảng cáo tin nhắn trên bài 1 (Hàn) và bài 2 (Úc), 100.000đ/ngày/bài x 7 ngày
   = 1.400.000đ. **Chưa được duyệt số tiền** – phải hỏi anh Trường chốt ngân sách trước khi bật.
   Không nhập thông tin thẻ/thanh toán. Nhóm khách: (a) TP.HCM, Bình Dương, Đồng Nai;
   (b) người dùng tiếng Việt đang sống ở Hàn Quốc và Úc.
3. **3 bài/ngày tự động**: mỗi tuần soạn 21 bài + ảnh, gửi anh duyệt 1 lần, rồi hẹn giờ
   (Graph API `scheduled_publish_time` + `published=false`, hoặc Meta Business Suite).
   Không tự đăng nội dung anh chưa xem: sai giá hay sai món được gửi là mất uy tín.
4. Hỏi lại: giờ làm việc thật, khu vực pickup chính xác, có đền bù thất lạc không.

## Lưu ý nội dung
- Không liệt kê món ăn cụ thể được gửi: Hàn và Úc cấm nhiều loại thực phẩm (Úc kiểm dịch rất chặt).
  Luôn viết "nhắn danh sách đồ để 90S kiểm tra món nào gửi được".
- Không so sánh tên đối thủ trong bài. Tham khảo: GHN ghi Hàn ~105.000đ/kg cho 50–99kg,
  nên 75K/kg là lợi thế giá – đặt giá lên đầu bài.
- Từ khóa: gửi hàng đi Hàn Quốc, gửi hàng đi Úc giá rẻ, gửi đồ ăn sang Hàn, gửi quà Tết đi Úc,
  ship hàng đi Hàn Quốc. Tết Đinh Mùi: 6/2/2027.

## Phong cách poster (học từ mẫu TCG, ShipMore, Axis, ForwardAir)
- `poster.py` → `posters/` (phong cách NSK/QT: trời xanh, dải tên nước + cờ, khối giá cam chữ vàng)
- `poster2.py` → `posters2/` 4 kiểu: A tổng quan sạch (dịch vụ + vì sao chọn 90S + cờ tuyến),
  B nền hoàng hôn tối + chữ 3D "GỬI NHIỀU TIẾT KIỆM" + nút CTA, C khối chữ nổi bật "VỊ QUÊ NHÀ" + sóng cam,
  D đường băng hoàng hôn + máy bay 90S (tuyến Úc, Tết)
- Quy tắc: chữ tiêu đề Anton 2 màu (navy + cam #F05A0F/#FF8A1F), 1 cụm chữ nổi bật trong khối cam,
  vật thể trung tâm là thùng hàng có logo 90S, hàng 4 icon cam kết có vạch ngăn, thanh liên hệ navy dưới cùng.
  Chỉ dùng thông tin thật của doanh nghiệp, không ghi "24/7", "bảo hiểm 100%" khi chưa được xác nhận.

## Nhận diện thương hiệu – LOGO THẬT (chủ page gửi 21/11/2026)
- Logo: chữ "90S" xám than #363636 + "CARGO" cam #F27E29 có đường bay máy bay cắt ngang, dòng "EXPRESS" bên dưới.
- File trong `brand/logo/`: `logo-90s-mau.png` (nền trong, dùng trên nền sáng), `logo-90s-trang.png` (chữ 90S trắng, dùng trên nền tối/ảnh), 3 file gốc `logo-goc-*.jpg` (nền trắng, nền xám, nền cam hoàng hôn).
- Poster: LUÔN dùng hàm `logo()` trong poster2.py (đã nhúng logo thật; dark=True cho nền tối). KHÔNG tự vẽ logo hình tròn hay chữ "90S CARGO" giả. Trên ảnh thật đặt logo màu trong nhãn trắng (poster_anh.py đã làm sẵn).
- Màu nền poster vẫn giữ navy #0D2B5E + cam như mẫu đã duyệt; cam chính của logo là #F27E29.
