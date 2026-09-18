# InsightHub Starter

19/09/2026 | B2B C07 - SDLC with AI | Starter v1.0.0 | Owner: Đinh Xuân Công.

Codebase nền cho Running Project InsightHub theo SRS 2.4. Starter giữ kiến trúc đồng bộ ba dịch vụ và để học viên phát triển Auth, Notebook, hội thoại, ghi chú và AI Tools trong khóa học.

## Năng lực nền đã có

- Next.js Web, FastAPI API, PostgreSQL 16 và pgvector.
- Upload TXT/MD/PDF đồng bộ, HTTP 201 chỉ sau khi ingestion thành công.
- Giới hạn 10 MiB, 100 trang PDF, 200.000 ký tự trích xuất; Unicode NFC.
- Lưu tệp gốc, toàn văn, segment/page locator, chunks và embedding identity.
- Idempotency 24 giờ cho upload, retry và chat; dedup theo SHA-256.
- Trạng thái tài liệu, attempt history, retry cùng document, xem nguồn và xóa.
- RAG theo tập `document_ids`, structured `Answered`/`NoEvidence`, citation validator và khóa chống race với delete.
- Deadline tuyệt đối 120 giây cho ingestion, 60 giây cho chat.
- Forward migration, health/readiness, metrics, fixture offline, provider thật cấu hình tường minh.
- Backend regression, web tests, smoke test và package verifier.

## Phạm vi học viên tiếp tục phát triển

- Auth và hồ sơ người dùng.
- Notebook, ownership, quota và optimistic concurrency.
- Lưu hội thoại, ghi chú và vòng đời dữ liệu sản phẩm.
- AI Tools: mindmap, summary, slide, quiz và report.
- Policy/rate limit theo owner/Notebook, audit, backup/restore và chất lượng AI theo AEV.

Các điểm tích hợp được mô tả tại [Integration Guide](docs/Integration_Guide_Auth_Notebook.md). Không gắn dữ liệu starter cho tài khoản đầu tiên và không tin `owner_id` do client gửi.

## Bắt đầu

Đọc [GETTING_STARTED.md](GETTING_STARTED.md), [API contract](docs/API_Contract_Starter_v1.md), [Architecture](docs/Architecture_Starter_v1.md) và [Release checklist](docs/release/Starter_Readiness_v1.0.0.md).

Fixture dùng cho setup và regression, không phải bằng chứng chất lượng AI thật. Không gọi provider trả phí trong luồng mặc định.
