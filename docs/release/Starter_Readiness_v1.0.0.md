# Starter Readiness v1.0.0

Ngày đánh giá: 19/09/2026  
Trạng thái: Release candidate `v1.0.0-rc.2`

| Gate | Trạng thái | Bằng chứng |
| --- | --- | --- |
| G0 Baseline/contract | Pass | Architecture, API contract, 3 ADR và SRS 2.4 hash trong package manifest |
| G1 Data/ingestion | Pass | Forward migration; original/extracted/segment/chunk; limits; retry/dedup tests |
| G2 Operation/RAG | Pass local/mock | Evidence gate, optional local/Cohere reranker, claim citation, idempotency/reconciliation, deadlines, source scope, delete locks và 70 backend tests |
| G3 UX/real RAG | Pending real AEV | UI disclosure và 3 web tests pass; AEV-01 v2 có grounded, multi-document, NoEvidence, injection và repeated case; provider thật chưa chạy vì package không chứa API key |
| G4 Data/recovery/package | Pass local | Backup-restore drill pass; clean-volume smoke pass; npm audit có 0 vulnerability; CycloneDX SBOM và secret-aware package verifier có trong release candidate |

## Điều kiện chuyển Ready

1. Chạy AEV-01 trên provider/model được lớp sử dụng, ghi cấu hình không chứa secret, corpus hash và kết quả `Answered`/`NoEvidence`/injection.
2. Ghi Chrome hoặc Edge version chính thức của lớp và hoàn tất keyboard walkthrough nếu khác môi trường kiểm hiện tại.
3. Xác nhận archive SHA-256 từ working tree sạch khi phát hành bản gửi học viên.
4. Khi các gate trên pass, đổi version từ `rc.2` sang `1.0.0` và đóng baseline lớp.

Không dùng fixture hoặc mock HTTP làm bằng chứng semantic của AI thật.
