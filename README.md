# InsightHub SDLC

Running Project xuyên suốt chương trình **B2B_C07_SDLC_with_AI**, tùy biến cho Samsung SDS, tập trung vai trò **Developer**. Starter v0.1.0, ngày 09/09/2026, Draft; owner học liệu: Đinh Xuân Công. Chưa là bản nghiệm thu của khách hoặc bản production.

Định vị đề xuất ngày 10/09/2026: InsightHub là hệ quản trị tri thức doanh nghiệp. Starter hiện chỉ có nền nạp tài liệu/hỏi đáp. Kế hoạch học tập kế thừa nền kỹ thuật và xây mới nghiệp vụ để đi từ yêu cầu tới UAT, release, bàn giao và thay đổi sau phát hành. Xem [outline v0.2](../Outline_DeXuat_InsightHub_Full_SDLC_v0.2.md) và [Running Project v0.4](../RP_B2B_C07_InsightHub_SDLC_v0.4.md). Đây là phạm vi nháp; nghiệp vụ mới chưa triển khai.

## Requirements sản phẩm

[SRS InsightHub doanh nghiệp v1.1](../04_Requirements/SRS_InsightHub_Enterprise_Knowledge_Management_v1.1.docx) là bản đặc tả làm việc hiện hành; [hướng dẫn áp dụng](../04_Requirements/HuongDan_ApDung_SRS_InsightHub_v1.1.md) phân biệt scaffold và phần học viên thực hiện. Requirements recovery cũ chỉ để đối chiếu. SRS chưa đồng nghĩa code đã đáp ứng hoặc được nghiệm thu.

## Bắt đầu

- [Chạy và kiểm tra ứng dụng](GETTING_STARTED.md).
- [Đặc tả recovery cũ, chỉ tham khảo kỹ thuật](docs/Requirements_InsightHub_SDLC_v0.1.md).
- [Nguồn gốc và thay đổi](docs/Provenance_InsightHub_SDLC_v0.1.md).
- [Quy tắc coding assistant](AGENTS.md).

## Đã có trong starter

| Thành phần | Hành vi hiện có |
|---|---|
| Web Next.js | Upload, danh sách trạng thái, hỏi đáp và tên nguồn |
| API FastAPI | Upload đồng bộ HTTP 201, danh sách/xóa tài liệu, chat, health/readiness |
| PostgreSQL + pgvector | Documents, chunks, identity của embedding index |
| Ingestion service | Kiểm tra SHA-256/pipeline/identity, khóa hàng, rollback; có thể gọi lại nội bộ an toàn |
| Kiểm thử | Backend unit/integration, frontend utility, build/typecheck, smoke local |
| Fixture | Luồng giả lập không cần API key; không đo chất lượng ngữ nghĩa |

**Chưa có theo MVP mới:** auth/session/membership, không gian tri thức, người phụ trách và vòng đời công bố, retrieval theo quyền, history/feedback nghiệp vụ. Ranh giới scaffold và phần học viên tự xây được đề xuất trong outline v0.2. Retry/history ingestion là mở rộng, không còn trục bắt buộc của dự án. Backend có xử lý lại nội bộ chưa đồng nghĩa có chức năng khôi phục cho người dùng.

## Cấu trúc

```text
api/             API, domain services, provider adapters, backend tests
web/             UI, proxy cùng origin, frontend tests
infra/db/        Schema và môi trường database được cung cấp
sample-docs/     Dữ liệu nghiệp vụ giả lập
scripts/         Smoke test ứng dụng
.github/         Workflow kiểm tra ứng dụng mẫu
```

Môi trường local gồm web, API và database. Học viên dùng cấu hình được cung cấp; release tập trung vào code, test, migration và hướng dẫn bàn giao. Yêu cầu xây cloud, Kubernetes, queue/worker, ChatOps, observability stack hoặc FinOps của lớp nguồn không thuộc bài tập này.

Không có xác thực hoặc phân quyền tổ chức trong starter. Chỉ dùng local, dữ liệu giả lập và một thư viện chung. Origin guard hỗ trợ ngăn trình duyệt từ website khác gửi yêu cầu thay đổi dữ liệu; không thay thế authentication. Không đưa starter lên mạng công khai.

Nguồn được kế thừa từ InsightHub của chương trình DevOps, commit `0d5b838776a5f1af01d737674d8fc85724c3c60f`. Bản nguồn được giữ nguyên; snapshot và manifest ở thư mục archive của chương trình. Phạm vi tái phát hành ngoài hồ sơ đào tạo VTI chưa được xác lập chỉ bằng việc sao chép source.
