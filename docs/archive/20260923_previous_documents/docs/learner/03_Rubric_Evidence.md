# Cách tính điểm khóa học và biểu mẫu kết quả

B2B C07 - Dự án cá nhân InsightHub | Phiên bản 2.2 | 19/09/2026

Rubric có tiêu chí và điểm nằm ngay trong từng milestone của [yêu cầu dự án](01_PRE_Milestones.md). Tài liệu này dùng khi cần xem cách tổng hợp điểm hoặc mẫu ghi kết quả; không cần chuyển qua đây để hiểu việc phải làm ở từng mốc.

## 1. Cơ cấu điểm khóa

| Thành phần | Trọng số | Cách xác định |
| --- | --- | --- |
| Quiz | 10% | Trung bình 10 quiz theo syllabus; tự làm, không dùng AI. Quiz buổi 8 chia chất lượng/bảo mật 50/50 |
| Chuẩn bị trước buổi học | 15% | Trung bình 10 bản chuẩn bị; chấm theo tiến độ và nội dung của buổi tương ứng |
| Assignment refactor | 25% | Bài refactor một module trong dự án; giao buổi 7, nộp trước buổi 9 ít nhất 12 giờ. Rubric 30/30/20/20 tại M3 |
| Capstone | 35% | Chấm toàn sản phẩm và bảo vệ cá nhân theo rubric tại Capstone |
| Chuyên cần và review | 15% | Tham dự và hai lần review bất đồng bộ tại M2/M4 |

Quy tất cả điểm thành phần về thang 10. Điểm khóa bằng `0,10 × Quiz + 0,15 × Chuẩn bị + 0,25 × Assignment + 0,35 × Capstone + 0,15 × Chuyên cần/review`.

Điều kiện hoàn thành: tổng điểm và Capstone từ 6/10, không thành phần nguồn nào bằng 0, tham dự ít nhất 8/10 buổi. Rubric tiến độ M0.1-M5 dùng phản hồi, không cộng thêm vào công thức. Assignment và phần refactor trong Capstone được chấm theo phiên bản/phạm vi riêng, không sao chép điểm.

## 2. Bài chuẩn bị trước buổi học

Mỗi tiêu chí tối đa 25 điểm. Chọn mức cao nhất đáp ứng đầy đủ mô tả; nhân điểm tối đa với 0/40/70/100%, cộng bốn dòng rồi chia 10. Điểm chuẩn bị của khóa là trung bình 10 buổi.

| Tiêu chí | Chưa có (0%) | Một phần (40%) | Đạt cốt lõi (70%) | Đầy đủ (100%) |
| --- | --- | --- | --- | --- |
| Phần tự thực hiện và câu hỏi | Chưa có bài | Chưa xác định phần đã tự làm | Có kết quả tự học/thực hành phù hợp buổi và phần cần hỗ trợ | Kết quả mở được, xác định rõ phụ thuộc và cách đã thử xử lý |
| Tính đúng | Không kiểm được nội dung | Có lỗi cơ bản chưa nhận diện | Phần đã thực hiện đúng với tài liệu và phạm vi chuẩn bị | Kiểm thêm tình huống biên liên quan và sửa sai có căn cứ |
| Giải thích cách làm và sử dụng AI | Chỉ chép đầu ra | Có kết luận thiếu lý do | Nêu cách tự phân tích, phần AI hỗ trợ và quyết định | So sánh giả định/phương án, nêu giới hạn và câu hỏi cụ thể |
| Minh chứng | Không có căn cứ | Chỉ khẳng định hoặc ảnh thiếu ngữ cảnh | Có đầu vào, kỳ vọng và kết quả thực tế phù hợp nhiệm vụ | Người khác kiểm lại được, đúng phiên bản và rõ phần chưa kiểm |

Bài chuẩn bị không cần hoàn tất sản phẩm cuối milestone. Buổi 1 chưa bắt có CI hoặc Auth; khó khăn về quyền truy cập cần được ghi để giảng viên hỗ trợ. Mốc chuẩn bị buổi 1-9: trước giờ học ít nhất 2 giờ; hồ sơ Capstone: trước buổi 10 ít nhất 12 giờ.

## 3. Chuyên cần và review

Phân bổ trong đề bài: tham dự chiếm 10 điểm phần trăm toàn khóa, chất lượng hai review chiếm 5 điểm phần trăm. Giữ tổng 15% đã quy định trong chương trình.

- Điểm tham dự trên thang 10 bằng số buổi tham dự hợp lệ, tối đa 10; điều kiện hoàn thành vẫn là ít nhất 8 buổi.
- Mỗi review chấm 0/4/7/10: không nộp / nhận xét chung / nhận xét gắn yêu cầu và minh chứng, có đề xuất kiểm / nhận xét đã được đối chiếu, giải thích tác động và có kết quả theo dõi.
- Điểm review bằng trung bình hai lần. Điểm chuyên cần/review bằng `(2 × điểm tham dự + điểm review) / 3`.
- Không buộc tìm lỗi nếu sản phẩm đúng; xác nhận có phép kiểm và căn cứ vẫn được ghi nhận. Nếu chưa có bài bạn học, dùng mẫu tương đương do giảng viên cấp; không phụ thuộc tiến độ người khác.

## 4. Bản ghi kết quả và minh chứng

**Nộp bài:** gửi link PR trong repository cá nhân và link bản ghi ngắn theo mẫu ở mục 2 của Requirements. Commit/push đầy đủ, bảo đảm giảng viên có quyền xem. Không bắt manifest hoặc tag mỗi milestone; M5 và bản phát hành Capstone phải có tag. Nếu sửa code sau kiểm, chạy lại phần bị ảnh hưởng và cập nhật link commit đã kiểm.

### Bảng kết quả theo yêu cầu

| Tiêu chí chấp nhận | Phạm vi | Ca kiểm thử | Kỳ vọng | Thực tế | Phiên bản đã kiểm | Minh chứng | Kết luận/lỗi |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Mã tiêu chí trong SRS | Áp dụng/điều chỉnh/ngoài phạm vi | Mã hoặc tên ca | Kết quả đúng theo yêu cầu | Kết quả quan sát được | Link commit | File/log/ảnh | Đạt/chưa đạt/bị chặn/ngoài phạm vi |

Lấy danh sách từ [bảng phạm vi SRS](02_SRS_Assignment_Map.md). Mỗi tiêu chí có kết luận riêng kể cả khi dùng chung test; ngoài phạm vi không ghi đạt. Có thể dùng Markdown, CSV hoặc công cụ quản lý của lớp, miễn đọc và kiểm được.

### Nội dung cần ghi theo loại công việc

| Loại | Nội dung |
| --- | --- |
| Test/nghiệm thu | Yêu cầu, điều kiện, bước chạy, kỳ vọng/thực tế, môi trường, commit, kết quả và lỗi liên quan |
| Đánh giá AI | Ca/lượt, nguồn và mã băm/vị trí, ý kỳ vọng, model/embedding/prompt/schema, kết quả đối chiếu, thời gian/mức sử dụng và người kiểm |
| Lỗi | Bước tái hiện, kỳ vọng/thực tế, tác động, phiên bản lỗi, bản sửa, kết quả kiểm lại và hồi quy |
| Quyết định kiến trúc | Vấn đề, yêu cầu chi phối, các phương án, lựa chọn, đánh đổi, căn cứ và hệ quả |
| Thay đổi sau phát hành | Lý do, hành vi trước/sau, tác động tới yêu cầu/thiết kế/dữ liệu/test, rủi ro, cách quay lại và kết quả kiểm |
| Quyết định với AI | Ngữ cảnh, đề xuất, phép kiểm, phần giữ/sửa/bác bỏ và lý do |
| Review | Sản phẩm/phiên bản, yêu cầu đối chiếu, nhận xét có căn cứ, đề xuất và phản hồi nếu có |

Có thể gộp nội dung cùng loại trong một file; không bắt tạo tài liệu riêng cho mỗi bản ghi. Phân biệt fixture/mock với dịch vụ thật. Không đưa secret hay dữ liệu chưa được phép vào hồ sơ.

## 5. Nguyên tắc phản hồi

- Ghi tên tiêu chí, điểm, căn cứ và việc cần sửa. Không chấm bằng số commit, số dòng code, số prompt hoặc số công cụ AI.
- Điểm học tập, mức năng lực đã chứng minh và trạng thái sản phẩm là ba kết quả riêng. Điểm đạt không biến tiêu chí sản phẩm chưa kiểm thành đạt.
- Lỗi chặn phát hành phải sửa và kiểm lại trước khi kết luận bàn giao. Dịch vụ hoặc credential lớp bị chặn được ghi rõ để hỗ trợ; mock không thay kết quả tích hợp thật.
- Thời điểm nhận bài dựa trên kênh nộp của lớp. Không tự đặt mức trừ điểm mới vì nộp muộn; áp dụng chính sách lớp đã công bố và giữ lịch sử phản hồi.
