# Traceability matrix AC và kiểm chứng theo rủi ro

`ac-trace.csv` là **một traceability matrix (bảng truy vết) xuyên khóa** cho 165 AC (153 áp dụng, 12 ngoài phạm vi), thay cho việc tự dựng bảng ở LR-08. Cột bên trái do giảng viên cấp; cột bên phải học viên điền dần từ M2.1 đến M5. Cách ghi theo [Requirements mục 16.1](../docs/learner/01_Requirements_InsightHub.md#bang-ket-qua).

## Cột

| Nhóm | Cột | Ý nghĩa |
| --- | --- | --- |
| Giảng viên cấp | `ac_id`, `req_id`, `group`, `scope`, `lr`, `due`, `uat`, `srs_ref` | Lấy từ Requirements mục 15.4; không sửa. `scope` là mã A, D1 đến D9 (trừ D7), N tại Requirements mục 15.1 |
| Giảng viên cấp | `tier` | `Core` (chấm, 91 AC), `Extended` (Stretch, 62 AC), `OutOfScope` (12 AC). Tầng công bố 29/09/2026, cập nhật 04/10/2026 theo Requirements 1.3 và SRS v1.1. `Pending` chỉ dùng khi giảng viên chưa công bố tầng |
| Giảng viên cấp | `risk_suggested` | Mức rủi ro gợi ý R1/R2/R3 |
| Học viên | `risk`, `risk_reason` | Mức rủi ro áp dụng; hạ mức so với gợi ý phải ghi lý do |
| Học viên | `branches`, `expected` | Nhánh cần kiểm, input và expected result theo SRS |
| Học viên | `draft_by` | `AI` nếu AI viết nháp, `Human` nếu tự viết |
| Học viên | `verification`, `verified_by`, `verify_method` | `Unverified` hoặc `Human-verified`; người kiểm; `SRS-crosscheck`, `Test`, `Sample`, `Review` |
| Học viên | `design_ref`, `test_ids`, `actual`, `commit`, `evidence`, `verdict`, `notes` | Thiết kế, test, kết quả thực tế, commit đã kiểm, minh chứng, kết luận |

`verdict`: `NotRun`, `Passed`, `Failed`, `Blocked`, `Extended-NotDone`, `OutOfScope`.

## Mức rủi ro

| Mức | Tiêu chí | Cách kiểm |
| --- | --- | --- |
| R1 | Auth/session, ownership, lộ hoặc mất dữ liệu, lộ đáp án Quiz, grounding/NoEvidence, secret trong log | Kiểm sâu 100%; `Passed` cần evidence trực tiếp có `test_ids` |
| R2 | Vòng đời, trạng thái, idempotency, CRUD, luồng UI chính, schema output | Kiểm đủ trước khi giao agent; evidence dùng chung được nếu có mapping |
| R3 | Nội dung thông báo, avatar, tài liệu API, hồ sơ bàn giao | Checklist hoặc lấy mẫu |

## Quy trình theo milestone

| Mốc | Việc | Lệnh |
| --- | --- | --- |
| M2.1 LR-08 | Skill `ac-drafter` viết nháp `branches`/`expected` cho AC áp dụng, ghi `draft_by=AI`. Kiểm 100% AC R1 của hành trình M3.1; AC R2 của hành trình kiểm đúng lúc trong DoD của PR. Phân tích sâu 1-2 AC kèm Gherkin. Lấy mẫu phần còn lại | `python3 scripts/trace_sample.py --seed <mã học viên + ngày> --size 10` |
| M2.1 LR-08 | Ghi `result` OK/Error cho từng dòng mẫu; đánh giá. Tỷ lệ lỗi từ 20% trở lên: sửa context pack hoặc prompt của skill, sinh lại nhóm lỗi, lấy mẫu vòng mới. Ghi tỷ lệ lỗi vào Delivery Log | `python3 scripts/trace_sample.py --evaluate` |
| M3.1-M3 | Trước khi giao agent một task: chuyển AC R1/R2 của task sang `Human-verified` (mục DoD của PR) | `python3 scripts/trace_check.py` |
| M4 LR-20 | Kết luận từng AC Core đến hạn | `python3 scripts/trace_check.py --gate M4` |
| M5 | Bổ sung AC release/restore/CR | `python3 scripts/trace_check.py --gate M5` |

`trace_check.py` chạy trong CI trên mọi PR. Script chỉ kiểm tính nhất quán; điểm và verdict vẫn dựa trên minh chứng thật. Không đổi tên cột hoặc xóa dòng; có thể thêm cột riêng ở cuối.
