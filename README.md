# InsightHub Starter

19/09/2026 | B2B C07 - SDLC with AI | Starter v1.0.0-rc.2 | Owner: Đinh Xuân Công.

Codebase nền cho Running Project InsightHub theo SRS 2.4. Starter giữ kiến trúc đồng bộ ba dịch vụ và để học viên phát triển Auth, Notebook, hội thoại, ghi chú và AI Tools trong khóa học.

## Năng lực nền đã có

- Next.js Web, FastAPI API, PostgreSQL 16 và pgvector.
- Upload TXT/MD/PDF đồng bộ, HTTP 201 chỉ sau khi ingestion thành công.
- Giới hạn 10 MiB, 100 trang PDF, 200.000 ký tự trích xuất; Unicode NFC.
- Lưu tệp gốc, toàn văn, segment/page locator, chunks và embedding identity.
- Idempotency 24 giờ cho upload, retry và chat; dedup theo SHA-256.
- Trạng thái tài liệu, attempt history, retry cùng document, xem nguồn và xóa.
- RAG theo tập `document_ids`, evidence threshold, candidate pool, diversity và context token budget.
- Reranker là option: tắt, TEI local hoặc Cohere. Không silent fallback khi provider lỗi.
- Structured claims bắt buộc citation, `Answered`/`NoEvidence`, source validator và khóa chống race với delete.
- Deadline tuyệt đối 120 giây cho ingestion, 60 giây cho chat.
- Forward migration, health/readiness, structured request log, metrics và runtime profile không lộ secret.
- Operation reconciliation cho upload, retry, delete và chat khi client mất response.
- AEV runner, backup-restore drill, CycloneDX SBOM, backend/web regression, smoke và package verifier.

## Phạm vi học viên tiếp tục phát triển

- Auth và hồ sơ người dùng.
- Notebook, ownership, quota và optimistic concurrency.
- Lưu hội thoại, ghi chú và vòng đời dữ liệu sản phẩm.
- AI Tools: mindmap, summary, slide, quiz và report.
- Policy/rate limit theo owner/Notebook, audit nghiệp vụ và mở rộng evaluation theo product use case.

Các điểm tích hợp được mô tả tại [Integration Guide](docs/Integration_Guide_Auth_Notebook.md). Không gắn dữ liệu starter cho tài khoản đầu tiên và không tin `owner_id` do client gửi.

## Bắt đầu

Đọc [START_HERE.md](START_HERE.md), [GETTING_STARTED.md](GETTING_STARTED.md), [Model Profiles](docs/Model_Profiles_And_Reranking.md), [API contract](docs/API_Contract_Starter_v1.md), [Architecture](docs/Architecture_Starter_v1.md) và [Release checklist](docs/release/Starter_Readiness_v1.0.0.md).

Fixture dùng cho setup và regression, không phải bằng chứng chất lượng AI thật. Không gọi provider trả phí trong luồng mặc định.
