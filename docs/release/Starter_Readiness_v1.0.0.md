# Starter Readiness v1.0.0

Ngày đánh giá: 19/09/2026. Technical candidate `v1.0.0-rc.3`. Phạm vi: nền RAG được cấp cho C07; chưa phải sản phẩm hoàn chỉnh hoặc quyết định phát hành lớp.

| Gate | Kết quả | Bằng chứng và giới hạn |
| --- | --- | --- |
| Baseline/contract | Đạt kiểm kỹ thuật | SRS 2.4 đóng gói nội bộ; 72 yêu cầu/163 AC được mapping; validator kiểm version/hash/link. SRS và học liệu vẫn Draft chờ review nội dung. |
| Backend/data | Đạt | 86 backend tests: lỗi terminal, deadline cả SQL/lock, replay nguồn đã xóa, Markdown heading/table/code, failed/pending dedup; forward migration 002. |
| Web/recovery | Đạt | Build/typecheck, 6 unit tests; Chrome và Edge mỗi trình duyệt 14 kiểm tra tại 1440x900 và 390x844, gồm reload/lost response/keyboard/source invalidation. |
| Real RAG | Đạt trên corpus synthetic | DeepSeek flash + Gemini embedding 2, 1024D, reranker none; 8/8 lượt, 13 claim có nguồn, hai NoEvidence, injection và PDF. Reviewer: Codex, chưa phải review độc lập của instructor. |
| Recovery | Đạt trên fixture có dữ liệu | Hash 8 bảng khớp sau restore; bytes/segments/locator/chat/retrieval qua API đạt, không orphan. Không dùng kết quả này làm đánh giá chất lượng AI. |
| Packaging | Công cụ và hướng dẫn đầy đủ | SRS nằm trong repo, Git init từ ZIP, pinned CI, SBOM, sạch working tree, kiểm manifest/hash/secret và hướng dẫn tự đóng gói. Biên nhận exact-package clean-room được lưu cùng hồ sơ bàn giao bên ngoài ZIP. |
| Học liệu đầu khóa | Đã biên soạn Draft | Learning Contract, PRE B1-B2, B1-B10/milestones, mapping, rubric/evidence, desk spike Auth/email. |
| Vận hành lớp | Chưa xác nhận | Pilot với Developer đại diện, Google OAuth bằng client/tài khoản lớp, lựa chọn email sandbox/hai tool và rubric calibration. Không thể thay bằng unit test hoặc agent timing. |

## Bằng chứng kèm package

- [AEV thật và review từng claim](evidence/AEV-01_20260919.json).
- [Chrome](evidence/chrome_20260919.json), [Edge](evidence/msedge_20260919.json).
- [Restore có dữ liệu](evidence/Restore_20260919.json).
- Học liệu hiện hành: [Requirements](../learner_v1.0_20260923/01_Requirements_InsightHub.md), [Auth/email](../learner_v1.0_20260923/01_Requirements_InsightHub.md#auth-email). Các liên kết này phục vụ phát triển tiếp; bảng đánh giá trên chỉ ghi nhận candidate ngày 19/09/2026.

Lệnh tái lập: `make test`, `make smoke`, `npm run test:e2e` trong web, `python3 scripts/check_project.py`, `make aev` trên runtime real riêng và restore drill theo Runbook. CI đã có các bước fixture, browser, restore, audit và package; chỉ coi GitHub CI của lớp đạt khi workflow chạy ở repository lớp.

Giữ nhãn rc.3 cho tới khi instructor quyết định baseline lớp. Không tự đổi thành 1.0.0, không gửi tài liệu/publish LMS. Các model và dịch vụ có thể đổi theo thời gian; chạy lại AEV khi thay model/prompt/retrieval/corpus. Không dùng working tree hoặc báo cáo lịch sử thay manifest của ZIP thực tế.
