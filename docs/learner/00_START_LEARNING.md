# Learning Contract - InsightHub C07

Phiên bản 1.0, ngày 19/09/2026. Draft học liệu để instructor review. Nguồn yêu cầu: [SRS 2.4](../../requirements/SRS_InsightHub_v2.4.md). Phạm vi: B2B C07, 10 buổi, 25 giờ trên lớp và 45 giờ tự học đề xuất; không tự xác lập lịch lớp hoặc phê duyệt phát hành.

## Phần được cấp và phần phải làm

| Được cấp trong Starter | Học viên triển khai |
| --- | --- |
| Web/API/PostgreSQL, migration, cấu hình, fixture và dữ liệu mẫu | Auth, Google sign-in, xác minh email, khôi phục/đổi mật khẩu, profile và phiên |
| Upload TXT/MD/PDF, trích xuất, chunk, embedding, nguồn/locator, retry/dedup | Notebook, ownership/quota, CRUD, tích hợp toàn bộ tài nguyên vào đúng Notebook/tài khoản |
| RAG có chọn nguồn, claim/citation, NoEvidence, deadline và idempotency | Hội thoại, ghi chú, lưu kết quả và vòng đời dữ liệu sản phẩm |
| UI nền, test, CI, AEV, backup/restore và công cụ đóng gói | Thiết kế Figma và triển khai UI/UX; tối thiểu hai AI Tool; kiểm thử và release local/sandbox |

SRS sản phẩm yêu cầu đủ năm AI Tool: Mindmap, Tóm tắt, Slide, Quiz và Báo cáo. Bài tập tối thiểu hai tool, chọn và ghi rõ ở buổi 4; triển khai phần dùng chung IH-AI/IH-OUT và các AC của hai nhóm đã chọn. Không tuyên bố hoàn thiện toàn sản phẩm R1 chỉ vì bài tập đạt. Instructor không cấp sẵn Auth/Notebook hoặc đáp án thiết kế.

Đọc theo thứ tự: [Getting Started](../../GETTING_STARTED.md), [PRE và milestone](01_PRE_Milestones.md), [mapping yêu cầu](02_SRS_Assignment_Map.md), [rubric và minh chứng](03_Rubric_Evidence.md), [spike Auth/email](04_Auth_Email_Feasibility.md), [integration guide](../Integration_Guide_Auth_Notebook.md).

## Quy tắc thực hành và dùng AI

- Trước khi nhờ AI: tự mô tả vấn đề, vẽ luồng hoặc đưa ra cách làm ban đầu. Sau đó dùng AI để phản biện, tạo phương án, test hoặc refactor; kiểm chứng bằng code/test/nguồn và giải thích được thay đổi.
- Dùng dữ liệu mẫu được phép. API key nằm trong `.env` local; không nộp key, token, dữ liệu thật, dump có tài khoản hoặc prompt chứa thông tin cá nhân.
- Mỗi nhóm giữ một repository. Instructor chốt quy mô nhóm, người review và thời điểm nộp theo lịch lớp; học liệu không tự ấn định các mục này.
- Mỗi thành viên có issue hoặc nhiệm vụ, PR/commit và minh chứng kiểm thử; mọi người phải giải thích được ít nhất một quyết định và một lỗi đã xử lý. Số dòng code hoặc số commit không thay thế chất lượng đóng góp.
- Không tắt guard quyền, checksum, citation, deadline hoặc test để làm demo pass. Thay đổi phạm vi cần ghi CR, lý do, tác động và quyết định instructor trước khi coi là yêu cầu mới.
- Chạy fixture trước, AI thật sau. Chỉ kết quả real-provider được dùng đánh giá chất lượng nội dung.

## Đầu ra cuối khóa

Một tag release và archive có checksum; README tái lập; nguồn Figma; mapping AC/test; code và migration; kết quả AEV; backup/restore; nhật ký quyết định/AI/PR và kịch bản demo. Bộ nộp phải chỉ rõ hai tool, chức năng đạt/chưa đạt và cách tái hiện lỗi còn lại. Chấm theo [rubric](03_Rubric_Evidence.md), không chỉ dựa bản demo.

## Giới hạn và hỗ trợ

Triển khai local/sandbox. Cloud, Kubernetes, hàng đợi, benchmark tải lớn, xuất PPTX/DOCX/PDF không phải điều kiện mặc định. Nếu setup hoặc dịch vụ Auth chặn tiến độ, ghi lỗi và thời gian đã dùng; chuyển sang fixture/mock đúng seam để tiếp tục phần độc lập. Mock không được tính là nghiệm thu Google/email thật. Instructor điều chỉnh kế hoạch dựa trên pilot, không cộng ngầm giờ học ngoài ngân sách.
