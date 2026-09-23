# Bắt đầu dự án cá nhân InsightHub

B2B C07 - SDLC with AI | Bộ yêu cầu v2.2 | 19/09/2026

Mỗi học viên phát triển một ứng dụng InsightHub trên repository cá nhân được tạo bằng chức năng Fork từ starter và môi trường riêng, từ phân tích yêu cầu đến bàn giao và xử lý thay đổi. Sản phẩm gồm Auth, Notebook, tài liệu, hỏi đáp có nguồn, hội thoại, ghi chú, Tóm tắt và Quiz.

## Thứ tự thực hiện

1. Fork và clone starter theo [GETTING_STARTED](../../../../../GETTING_STARTED.md), giữ lịch sử Git và ghi commit nền. Sau đó khởi động ứng dụng.
2. Đọc [Yêu cầu thực hiện theo milestone](01_PRE_Milestones.md): phạm vi, lộ trình 10 buổi, việc cần làm, rubric và hướng dẫn gửi bài.
3. Dùng [Mapping SRS và AC](02_SRS_Assignment_Map.md) để lập bảng truy vết của bài làm; đọc AC gốc trong [SRS 2.4](../../requirements/SRS_InsightHub_v2.4.md).
4. Đọc rubric ngay trong milestone đang làm. [Cách tính điểm và biểu mẫu](03_Rubric_Evidence.md) bổ sung cách tổng hợp điểm khóa và mẫu ghi kết quả khi cần.
5. Hoàn thành [spike Auth/Google/email](04_Auth_Email_Feasibility.md) tại M2.1, trước khi tích hợp nghiệp vụ phụ thuộc.
6. Đọc [điểm mở rộng Auth/Notebook](../Integration_Guide_Auth_Notebook.md) trước khi sửa ingestion/RAG core; mở rộng test hiện có thay vì viết lại baseline.

## Công cụ và trách nhiệm

- Dùng **Claude là công cụ AI chính**; ChatGPT do công ty cung cấp dùng bổ trợ khi cần. Học viên tự chạy, kiểm chứng và giải thích sản phẩm.
- Claude/ChatGPT phục vụ phát triển phần mềm. **DeepSeek** phục vụ tính năng AI của InsightHub; embedding theo cấu hình starter. Hai nhóm công cụ có tài khoản và cấu hình riêng.
- Starter đã có ingestion/RAG, Web/API/DB và công cụ kiểm. Auth, Notebook, dữ liệu nghiệp vụ và hai AI Tool là phần học viên xây và tích hợp.
- Bài tập thực hiện Tóm tắt + Quiz. Mindmap, Slide và Báo cáo nằm ngoài phạm vi bắt buộc; hoàn thành bài tập không đồng nghĩa đạt toàn bộ sản phẩm năm tool trong SRS.
- Mỗi người chịu trách nhiệm toàn bộ bài. Review bất đồng bộ hỗ trợ phản biện, không yêu cầu chia nhóm hoặc chờ bài của người khác để phát triển.
- Nộp phiên bản có thể tái chạy và evidence đúng phiên bản. Không đưa secret, `.env` thật hoặc dữ liệu công ty chưa được phép vào repository, hội thoại AI hay hồ sơ nộp.

Mỗi buổi có 150 phút học trên lớp. Tổng 45 giờ tự học bao gồm PRE, phát triển, kiểm thử, review, sửa bài và chuẩn bị bảo vệ.

Mỗi milestone có kiến thức liên quan, việc cần làm, gợi ý ứng dụng AI, rubric có điểm, cách nộp bài và tài liệu sử dụng. Đọc mục 2 trong Requirements để biết cách tạo PR trong repository cá nhân và gửi đường dẫn cho giảng viên. Tag chỉ bắt buộc khi phát hành ở M5.
