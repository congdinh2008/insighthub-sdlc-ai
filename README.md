# InsightHub

18/09/2026 | B2B C07 | Bản khởi động lại từ first commit | Owner: Đinh Xuân Công.

Theo yêu cầu anh Công, project này được tạo từ first commit C07 `10a1a61b4968d6d0f8a7d1f81b4cd8ba1e0af640`. Không kế thừa các commit Auth/Enterprise/Governance về sau. Hai project cũ đã được lưu trữ nguyên trạng, gồm cả thay đổi chưa commit.

## Phạm vi hiện có

- Web Next.js, API FastAPI, PostgreSQL/pgvector.
- Nạp tài liệu đồng bộ, chunking/embedding/retrieval và Chatbot; chế độ fixture mặc định.
- Backend tests, web utility tests và smoke script của first commit.
- Chưa có Auth, Notebook hoặc AI Tool mới. Các chức năng này chưa được triển khai trong lượt khởi động lại.

## Nguồn và hướng dẫn

- [Trạng thái và quyết định khởi động lại](../00_INDEX.md).
- [Chạy và kiểm tra trong môi trường riêng](GETTING_STARTED.md).
- [Quy tắc làm việc](AGENTS.md).
- [Hồ sơ archive và ánh xạ đường dẫn](../../../99_Archive/20260918_Reset_InsightHub_FirstCommit/00_README.md).

Toàn bộ 66 file khớp first commit tại thời điểm khôi phục. Sau đó chỉ cập nhật README.md, AGENTS.md và GETTING_STARTED.md để xác định đúng nguồn và cách chạy riêng; mã ứng dụng, test, dependency và cấu hình gốc giữ nguyên.

SRS Enterprise, đề bài Governance và kế hoạch WP/G trước ngày khởi động lại là hồ sơ của hướng cũ, không tự áp dụng cho project này. Các file kế thừa trong `docs/` giữ provenance/tham chiếu kỹ thuật, không xác lập yêu cầu mới. Phạm vi Running Project mới cần được biên soạn theo trao đổi Auth/Notebook; lượt này chỉ tạo code base mới và archive hai project cũ.

Starter chưa có xác thực, chỉ dùng local và dữ liệu giả lập. Fixture kiểm hành vi phần mềm, không chứng minh chất lượng câu trả lời AI thật. Chưa chạy lại runtime hoặc nghiệm thu trong lượt khôi phục.
