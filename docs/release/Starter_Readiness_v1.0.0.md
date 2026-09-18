# Starter Readiness v1.0.0

Ngày đánh giá: 19/09/2026  
Trạng thái: Candidate

| Gate | Trạng thái | Bằng chứng |
| --- | --- | --- |
| G0 Baseline/contract | Pass | Architecture, API contract, 3 ADR và SRS 2.4 hash trong package manifest |
| G1 Data/ingestion | Pass | Forward migration; original/extracted/segment/chunk; limits; retry/dedup tests |
| G2 Operation/RAG | Pass local/mock | Idempotency, deadline, source scope, citation validator, delete locks, operation reconciliation, cursor pagination, 59 backend tests |
| G3 UX/real RAG | Pending real AEV | UI journey, desktop 1440 x 900, mobile 390 x 844 và web tests pass; semantic AEV với provider thật chưa chạy |
| G4 Clean-room/package | Pass | Archive từ commit sạch; verifier pass; fresh volume; 58 backend tests, 3 web tests và smoke MD/PDF/source locator pass trên namespace riêng. Bản code cuối tăng thêm contract test pagination/operation và đã pass 59 backend tests. |

## Điều kiện chuyển Ready

1. Chạy AEV-01 trên provider/model được lớp sử dụng, ghi cấu hình không chứa secret, corpus hash và kết quả `Answered`/`NoEvidence`/injection.
2. Ghi Chrome hoặc Edge version chính thức của lớp và hoàn tất keyboard walkthrough nếu khác môi trường kiểm hiện tại.
3. Cập nhật manifest từ `candidate` sang release, tạo archive từ working tree sạch và xác nhận SHA-256.

Không dùng fixture hoặc mock HTTP làm bằng chứng semantic của AI thật.
