# Starter Readiness v1.0.0

Ngày đánh giá: 19/09/2026  
Trạng thái: Candidate

| Gate | Trạng thái | Bằng chứng |
| --- | --- | --- |
| G0 Baseline/contract | Pass | Architecture, API contract, 3 ADR và SRS 2.4 hash trong package manifest |
| G1 Data/ingestion | Pass | Forward migration; original/extracted/segment/chunk; limits; retry/dedup tests |
| G2 Operation/RAG | Pass local/mock | Idempotency, deadline, source scope, citation validator, delete locks, 58 backend tests |
| G3 UX/real RAG | Pending một phần | UI journey và web tests pass; semantic AEV với provider thật chưa chạy |
| G4 Clean-room/package | Pending | Package/verify automation đã có; cần chạy từ commit sạch và máy/namespace mới |

## Điều kiện chuyển Ready

1. Chạy AEV-01 trên provider/model được lớp sử dụng, ghi cấu hình không chứa secret, corpus hash và kết quả `Answered`/`NoEvidence`/injection.
2. Clone hoặc giải nén package trên môi trường sạch; chạy setup, 58 backend tests, web tests và smoke.
3. Ghi browser/version, kiểm 1440 x 900 và 390 x 844, bàn phím và mở citation.
4. Cập nhật manifest từ `candidate` sang release, tạo archive từ working tree sạch và xác nhận SHA-256.

Không dùng fixture hoặc mock HTTP làm bằng chứng semantic của AI thật.
