# Chạy InsightHub SDLC tại máy học viên

## Điều kiện

Có Docker với Compose, khoảng 4 GB RAM khả dụng cho các container, cổng 8107 và 3107 trống. Đây là mức chuẩn bị đề xuất, chưa là benchmark tài nguyên. Python 3 dùng cho smoke script; Node/Python chạy ứng dụng đã được đóng gói trong image.

Từ thư mục repository:

```sh
cp .env.example .env
make up
```

Lần đầu có thể cần mạng để lấy image/dependency. Mặc định là `fixture`, không gọi dịch vụ AI trả phí. Mở web tại http://localhost:3107, API docs tại http://localhost:8107/docs. Nếu đổi cổng, sửa `.env`; khi chạy smoke truyền API_URL/WEB_URL tương ứng. Không thêm key thật vào tài liệu hoặc Git.

## Kiểm tra hành vi

1. Upload `sample-docs/huong-dan-nguoi-moi.md`, xác nhận trạng thái `ready` và số chunk lớn hơn 0.
2. Đặt câu hỏi về giới hạn file. Chế độ fixture trả nội dung có nhãn `[FIXTURE...]`; tên nguồn là các tài liệu được truy hồi, không phải chứng nhận tính đúng của câu trả lời.
3. Upload file TXT chỉ có khoảng trắng. API trả lỗi; UI làm mới danh sách và hiển thị bản ghi `failed`. Chức năng retry sẽ được học viên bổ sung.
4. Chạy kiểm tra dưới đây. Integration tests tạo schema riêng; smoke chỉ xóa tài liệu do lần chạy đó tạo.

```sh
make test
make smoke
make down
```

`make down` giữ volume dữ liệu. Không dùng xóa volume để né lỗi migration. Database chỉ được khởi tạo schema khi volume mới; bản có dữ liệu cần migration có kiểm thử.

## Chẩn đoán ứng dụng

- Không mở được web: kiểm tra trạng thái các service bằng `docker compose ps` và cổng trong `.env`.
- API chưa ready: đọc lỗi ứng dụng bằng `docker compose logs api`; không đưa nội dung nhạy cảm vào báo cáo.
- Upload timeout: làm mới danh sách để biết server có hoàn tất hay không. Chưa có deadline xuyên suốt nhiều batch provider; core lab dùng corpus nhỏ và fixture.
- Tài liệu pending sau khi tiến trình bị dừng: chưa có recovery tự động. Ghi nhận lỗi để phân tích; không tự coi polling UI là worker.
- Port bị chiếm: chọn cổng khác cho riêng project, không dừng container của dự án khác.

## Provider thật là nhánh tùy chọn

Các adapter kế thừa vẫn được giữ cho việc so sánh và kiểm thử. Tên model/endpoint trong `.env.example` là cấu hình kế thừa, chưa được xác nhận bằng cuộc gọi live trong bản SDLC. Chỉ chọn provider sau khi giảng viên xác nhận quyền dùng, ngân sách, dữ liệu và khả năng tương thích.

Chuyển fixture sang real cần database/index riêng. Không trộn vector khác provider/model/dimension/revision trong index đã có. Không tự chuyển về fixture nếu provider thật lỗi. Bài tập Developer có thể hoàn thành bằng fixture và provider được mock trong test; chất lượng trả lời của model thật cần một lần đánh giá riêng.
