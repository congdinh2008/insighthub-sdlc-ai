# InsightHub Starter - Quy tắc làm việc

Đọc `README.md`, `GETTING_STARTED.md`, `docs/Architecture_Starter_v1.md` và `docs/API_Contract_Starter_v1.md` trước khi sửa.

- Tài liệu bài tập sử dụng [Requirements học viên 1.0](docs/learner_v1.0_20260923/01_Requirements_InsightHub.md) và SRS v1.0 đính kèm trong cùng thư mục. Bộ học viên gồm một Requirements chính, một SRS và một ZIP API/Schema tham khảo. Hợp đồng API tham khảo là thiết kế để đối chiếu; không tự thay giao tiếp runtime. Manifest của gói mã nguồn chỉ xác nhận đúng phiên bản gói được kiểm.
- Giữ kiến trúc đồng bộ Web/API/PostgreSQL và HTTP 201 sau ingestion thành công, trừ khi có quyết định mới được ghi bằng ADR.
- Không làm yếu checksum, embedding identity, idempotency, deadline, citation validation, locks hoặc transaction để test pass.
- Mọi thay đổi schema dùng forward migration. Không yêu cầu xóa volume như cách nâng cấp.
- Giữ fixture hoàn toàn offline. Không gọi provider trả phí, tải model hoặc gửi tài liệu ra ngoài khi chưa có chỉ dẫn phù hợp.
- Auth/Notebook là extension của học viên. Policy ownership phải do server xác lập; không tin owner do client gửi và không tự nhận dữ liệu nền cho user đầu tiên.
- Không log credentials, toàn văn tài liệu, prompt có nội dung nguồn hoặc provider body thô.
- Dùng Compose namespace riêng. Không thao tác container hoặc volume của project khác.
- Chạy backend, web và smoke tests phù hợp trước khi đóng gói. `scripts/verify_package.py` phải pass.
- Fixture xác nhận behavior của phần mềm, không phải semantic evaluation của AI thật.
