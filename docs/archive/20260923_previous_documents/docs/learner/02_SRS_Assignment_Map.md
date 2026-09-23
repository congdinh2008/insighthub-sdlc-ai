# Mapping SRS 2.4 vào bài tập cá nhân

B2B C07 | Phiên bản 2.2 | 19/09/2026

Bảng này là phạm vi giao bài, không phải kết quả kiểm thử. [SRS 2.4](../../requirements/SRS_InsightHub_v2.4.md) giữ nguyên; học viên đọc nội dung gốc của từng AC. Việc cần làm và rubric ghi đầy đủ trong [Requirements theo milestone](01_PRE_Milestones.md). Mã LR chỉ dùng để truy vết trong bảng này; danh mục bên dưới dẫn đến đúng công việc, học viên không cần ghi nhớ mã.

## 1. Quy tắc phạm vi

Có **72 yêu cầu, 163 AC** được truy vết; **66 yêu cầu/151 AC thuộc bài tập**, **6 yêu cầu/12 AC ngoài bài tập**. AC điều chỉnh vẫn thuộc 151 AC phải kiểm. Đây là số AC được giao, không phải số test hoặc số AC đã Pass.

| Mã | Cách áp dụng |
| --- | --- |
| A | Giữ hành vi, giới hạn và ngoại lệ gốc đối với đối tượng thuộc bài tập |
| D1 | Phần liên quan danh mục, cấu hình, schema, nguồn, API hoặc lọc theo loại chỉ áp dụng **Tóm tắt + Quiz**; bỏ trường/nhánh riêng của Mindmap/Slide/Báo cáo. Không hạ yêu cầu dữ liệu, nguồn, trạng thái hoặc an toàn |
| D2 | Figma/UI-01..08 và hành trình sử dụng có đủ Tóm tắt + Quiz; không phải vẽ/triển khai ba tool mở rộng. Các trạng thái, viewport, keyboard và tiêu chí UX khác giữ nguyên |
| D3 | Tích hợp/đo AI thật cho RAG + Tóm tắt + Quiz: AEV-01/03/05 và hai lượt lặp = 12 lượt nội dung. Google/email vẫn kiểm live, không đổi thành tùy chọn |
| D4 | Nghiệm thu **R1 bài tập hai tool**, với 151 AC áp dụng, UAT-01..21 theo scope và AEV tương ứng; không kết luận đạt R1 sản phẩm đủ năm tool |
| N | Ngoài bài tập bắt buộc: Mindmap/Slide/Báo cáo. Ghi OutOfScope, không ghi Pass; nếu tự làm thêm phải bổ sung test/AEV riêng |

Quy tắc chung: các mục BR/LIM/UC/data/NFR/MSG vẫn áp dụng cho core. Đề bài không bỏ Auth, Google, email, Quiz attempt, quyền hoặc ngoại lệ. “Năm email” EML-001..005 giữ đủ năm; không nhầm với điều chỉnh từ năm xuống hai AI Tool.

- UAT-11 kiểm Tóm tắt/Quiz và vòng đời kết quả; không yêu cầu Mindmap/Slide/Báo cáo.
- UAT-15 kiểm màn hình UI-01..08 theo D2. UAT-14/20 và AEV-07 kiểm cấu trúc Tóm tắt/Quiz; các ngoại lệ khác giữ nguyên.
- AEV-02/04/06 ngoài bài tập; AEV-08 giữ cả bốn tình huống đại diện và không thay test quyền từng loại tài nguyên.
- LIM-05 cho đầu vào tool không giới hạn RAG còn ba nguồn. RAG dùng tập Ready của Notebook theo BR-05/IH-CHAT-001.
- Mỗi AC phải có verdict riêng, kể cả khi dùng chung test/evidence. Cột UAT chỉ là liên kết kịch bản tổng hợp, không thay test chi tiết.

## 2. Từ yêu cầu học tập tới năng lực và rubric

Các mã Course/Unit/Topic có tiền tố B2BC07. Cột LR áp dụng cho từng ID trong khoảng ghi; cột PLO/CLO theo chương trình.

| LR | PLO / CLO | Unit/Topic | Output | Rubric |
| --- | --- | --- | --- | --- |
| LR-01..03 | PLO-1 / C01-CLO-1,2 | C01-U01 T01-T04 | Môi trường, prompt và kết quả kiểm AI | Kiểm chứng đầu ra AI |
| LR-04..05 | PLO-1 / C01-CLO-3,4 | C01-U02 T01-T04 | Hướng dẫn AI và quy trình agent | Quy trình agent và kiểm soát quyền |
| LR-06..07 | PLO-1 / C02-CLO-1 | C02-U01 T01-T04 | Hồ sơ dự án, backlog và CI | Phạm vi và kế hoạch |
| LR-08..09 | PLO-2 / C02-CLO-2 | C02-U02 T01-T04 | Yêu cầu, ca kiểm và thử tích hợp | Đặc tả và truy vết yêu cầu |
| LR-10..11 | PLO-3 / C02-CLO-3 | C02-U03 T01-T04 | Figma, API, dữ liệu và quyết định kiến trúc | Thiết kế UI/API/dữ liệu |
| LR-12..13 | PLO-4 / C02-CLO-4 | C02-U04 T01-T04 | Luồng tích hợp và TDD | Chức năng và TDD |
| LR-14..18 | PLO-4 / C02-CLO-4 | C02-U04 T05-T08 | Chức năng đầy đủ | Chức năng sản phẩm |
| LR-19 | PLO-4 / C02-CLO-4 | C02-U04 T05-T08 | Module refactor và tác vụ tự động | Refactor, tự động hóa và Assignment |
| LR-20..22 | PLO-5 / C02-CLO-5 | C02-U05 T01-T08 | Kết quả test và nghiệm thu | Kiểm thử, nghiệm thu và phân quyền |
| LR-23 | PLO-5 / C02-CLO-5 | C02-U05 T01-T08 | Nguồn, kỳ vọng và kết quả AI | Chất lượng nội dung AI |
| LR-24 | PLO-1,5 / C01-CLO-4, C02-CLO-5 | C02-U05 T01-T08 | Mô hình đe dọa, scan và kiểm bảo mật | Bảo mật ứng dụng và quy trình AI |
| LR-25..26 | PLO-6 / C02-CLO-6 | C02-U06 T01-T04 | Bản phát hành, runbook và restore | Phát hành và khôi phục |
| LR-27 | PLO-6 / C02-CLO-6 | C02-U06 T01-T04 | Hồ sơ thay đổi và hồi quy | Thay đổi sau phát hành |
| LR-28 | PLO-1..6 / C02-CLO-1..6 | C02-U07 T01-T04 | Demo và vấn đáp | Demo và vấn đáp |
| LR-29 | PLO-6 / C02-CLO-6 | C02-U07 T01-T04 | Kế hoạch áp dụng 30 ngày | Kế hoạch áp dụng 30 ngày |

LR-01..11 là chuẩn bị/phân tích/thiết kế; LR-20..24 kiểm các AC đã triển khai ở LR-12..18. Vì vậy một AC có thể tham chiếu thêm nhiều LR trong bảng truy vết bài làm. Các hoạt động Foundation, TDD, refactor và vấn đáp không bị ép thành yêu cầu sản phẩm mới.

### Tra công việc theo mã truy vết

| Mã trong bảng | Milestone | Việc cần làm |
| --- | --- | --- |
| LR-01 | M0.1 | [Khởi động starter](01_PRE_Milestones.md#lr-01) |
| LR-02 | M0.1 | [Tạo đầu ra có cấu trúc](01_PRE_Milestones.md#lr-02) |
| LR-03 | M0.1 | [Phát hiện và sửa một lỗi AI](01_PRE_Milestones.md#lr-03) |
| LR-04 | M0.2 | [Viết quy tắc dùng AI cho dự án](01_PRE_Milestones.md#lr-04) |
| LR-05 | M0.2 | [Thực hành một quy trình agent có dùng công cụ/MCP](01_PRE_Milestones.md#lr-05) |
| LR-06 | M1 | [Lập hồ sơ dự án và backlog](01_PRE_Milestones.md#lr-06) |
| LR-07 | M1 | [Thiết lập quy trình phát triển](01_PRE_Milestones.md#lr-07) |
| LR-08 | M2.1 | [Lập bảng yêu cầu và ca kiểm thử](01_PRE_Milestones.md#lr-08) |
| LR-09 | M2.1 | [Thử tích hợp trước khi chốt thiết kế](01_PRE_Milestones.md#lr-09) |
| LR-10 | M2 | [Thiết kế Figma](01_PRE_Milestones.md#lr-10) |
| LR-11 | M2 | [Thiết kế API và dữ liệu](01_PRE_Milestones.md#lr-11) |
| LR-12 | M3.1 | [Triển khai hành trình đầu tiên](01_PRE_Milestones.md#lr-12) |
| LR-13 | M3.1 | [Thực hiện TDD cho một hành vi có rủi ro](01_PRE_Milestones.md#lr-13) |
| LR-14 | M3 | [Hoàn thiện tài khoản và email](01_PRE_Milestones.md#lr-14) |
| LR-15 | M3 | [Hoàn thiện Notebook, tài liệu, hội thoại và ghi chú](01_PRE_Milestones.md#lr-15) |
| LR-16 | M3 | [Xây dựng Tóm tắt](01_PRE_Milestones.md#lr-16) |
| LR-17 | M3 | [Xây dựng Quiz](01_PRE_Milestones.md#lr-17) |
| LR-18 | M3 | [Hoàn thiện vòng đời công cụ AI](01_PRE_Milestones.md#lr-18) |
| LR-19 | M3 | [Refactor một module và tự động hóa một tác vụ](01_PRE_Milestones.md#lr-19) |
| LR-20 | M4 | [Kiểm toàn bộ phạm vi bài tập](01_PRE_Milestones.md#lr-20) |
| LR-21 | M4 | [Kiểm giao diện và hiệu năng](01_PRE_Milestones.md#lr-21) |
| LR-22 | M4 | [Kiểm phân quyền và vòng đời dữ liệu](01_PRE_Milestones.md#lr-22) |
| LR-23 | M4 | [Đánh giá AI bằng mô hình thật](01_PRE_Milestones.md#lr-23) |
| LR-24 | M4 | [Kiểm bảo mật và sửa lỗi](01_PRE_Milestones.md#lr-24) |
| LR-25 | M5 | [Phát hành bản R1](01_PRE_Milestones.md#lr-25) |
| LR-26 | M5 | [Kiểm nâng cấp và khôi phục dữ liệu](01_PRE_Milestones.md#lr-26) |
| LR-27 | M5 | [Thực hiện một thay đổi sau R1](01_PRE_Milestones.md#lr-27) |
| LR-28 | Capstone | [Demo và bảo vệ cá nhân](01_PRE_Milestones.md#lr-28) |
| LR-29 | Capstone | [Lập kế hoạch áp dụng AI trong 30 ngày](01_PRE_Milestones.md#lr-29) |

## 3. Trách nhiệm kế thừa và phát triển

| Nhóm | Trách nhiệm |
| --- | --- |
| AUTH, NB, NOTE, SUM, QUIZ, OUT; CHAT-004 | Học viên xây nghiệp vụ UI/API/DB và kiểm đầy đủ |
| DOC; CHAT còn lại; nền operation/provider | Kế thừa thuật toán nền; học viên tích hợp Notebook/ownership/quota/vòng đời và kiểm regression, không mặc định đạt sau sửa |
| AI, DATA, INT | Kế thừa seam/provider/migration; xây phần dùng chung, schema, policy và tích hợp Auth/email/hai tool |
| UX, MSG | Học viên thiết kế và triển khai, kế thừa thành phần phù hợp; email/trạng thái có evidence riêng |
| NFR, REL | Học viên chứng minh trên phiên bản cuối, mở rộng test/runbook/backup/package theo dữ liệu mới |

## 4. Danh mục từng AC

Mốc thể hiện triển khai/kiểm trọng tâm; phân tích tất cả AC tại M2.1, thiết kế tại M2 và cập nhật sau CR. Bảng giữ từng AC riêng để sao vào traceability; bổ sung test ID, evidence, commit, result và defect của bài làm theo mẫu bảng kết quả.

| Yêu cầu | AC | Scope | LR trọng tâm | Mốc | UAT nguồn |
| --- | --- | --- | --- | --- | --- |
| IH-AUTH-001 | IH-AUTH-001-AC01 | A | LR-14 | M3 → M4 | UAT-01 |
| IH-AUTH-001 | IH-AUTH-001-AC02 | A | LR-14 | M3 → M4 | UAT-01 |
| IH-AUTH-002 | IH-AUTH-002-AC01 | A | LR-14 | M3 → M4 | UAT-01 |
| IH-AUTH-002 | IH-AUTH-002-AC02 | A | LR-14 | M3 → M4 | UAT-01 |
| IH-AUTH-003 | IH-AUTH-003-AC01 | A | LR-14 | M3 → M4 | UAT-01 |
| IH-AUTH-003 | IH-AUTH-003-AC02 | A | LR-14 | M3 → M4 | UAT-01 |
| IH-AUTH-004 | IH-AUTH-004-AC01 | A | LR-14 | M3 → M4 | UAT-02 |
| IH-AUTH-004 | IH-AUTH-004-AC02 | A | LR-14 | M3 → M4 | UAT-02 |
| IH-AUTH-005 | IH-AUTH-005-AC01 | A | LR-14 | M3 → M4 | UAT-02, UAT-03 |
| IH-AUTH-005 | IH-AUTH-005-AC02 | A | LR-14 | M3 → M4 | UAT-02, UAT-03 |
| IH-AUTH-005 | IH-AUTH-005-AC03 | A | LR-14 | M3 → M4 | UAT-02, UAT-03 |
| IH-AUTH-005 | IH-AUTH-005-AC04 | A | LR-14 | M3 → M4 | UAT-02, UAT-03 |
| IH-AUTH-006 | IH-AUTH-006-AC01 | A | LR-14 | M3 → M4 | UAT-03 |
| IH-AUTH-006 | IH-AUTH-006-AC02 | A | LR-14 | M3 → M4 | UAT-03 |
| IH-AUTH-007 | IH-AUTH-007-AC01 | A | LR-14 | M3 → M4 | UAT-03 |
| IH-AUTH-007 | IH-AUTH-007-AC02 | A | LR-14 | M3 → M4 | UAT-03 |
| IH-AUTH-007 | IH-AUTH-007-AC03 | A | LR-14 | M3 → M4 | UAT-03 |
| IH-AUTH-008 | IH-AUTH-008-AC01 | A | LR-14 | M3 → M4 | UAT-04 |
| IH-AUTH-008 | IH-AUTH-008-AC02 | A | LR-14 | M3 → M4 | UAT-04 |
| IH-AUTH-009 | IH-AUTH-009-AC01 | A | LR-14 | M3 → M4 | UAT-04 |
| IH-AUTH-009 | IH-AUTH-009-AC02 | A | LR-14 | M3 → M4 | UAT-04 |
| IH-AUTH-010 | IH-AUTH-010-AC01 | A | LR-14 | M3 → M4 | UAT-03 |
| IH-AUTH-010 | IH-AUTH-010-AC02 | A | LR-14 | M3 → M4 | UAT-03 |
| IH-NB-001 | IH-NB-001-AC01 | A | LR-15 | M3 → M4 | UAT-05 |
| IH-NB-001 | IH-NB-001-AC02 | A | LR-15 | M3 → M4 | UAT-05 |
| IH-NB-002 | IH-NB-002-AC01 | A | LR-15 | M3 → M4 | UAT-05 |
| IH-NB-002 | IH-NB-002-AC02 | A | LR-15 | M3 → M4 | UAT-05 |
| IH-NB-003 | IH-NB-003-AC01 | A | LR-15 | M3 → M4 | UAT-12 |
| IH-NB-003 | IH-NB-003-AC02 | A | LR-15 | M3 → M4 | UAT-12 |
| IH-NB-004 | IH-NB-004-AC01 | A | LR-15 | M3 → M4 | UAT-13 |
| IH-NB-004 | IH-NB-004-AC02 | A | LR-15 | M3 → M4 | UAT-13 |
| IH-DOC-001 | IH-DOC-001-AC01 | A | LR-15 | M3 → M4 | UAT-06 |
| IH-DOC-001 | IH-DOC-001-AC02 | A | LR-15 | M3 → M4 | UAT-06 |
| IH-DOC-002 | IH-DOC-002-AC01 | A | LR-15 | M3 → M4 | UAT-06 |
| IH-DOC-002 | IH-DOC-002-AC02 | A | LR-15 | M3 → M4 | UAT-06 |
| IH-DOC-003 | IH-DOC-003-AC01 | A | LR-15 | M3 → M4 | UAT-07 |
| IH-DOC-003 | IH-DOC-003-AC02 | A | LR-15 | M3 → M4 | UAT-07 |
| IH-DOC-004 | IH-DOC-004-AC01 | A | LR-15 | M3 → M4 | UAT-07 |
| IH-DOC-004 | IH-DOC-004-AC02 | A | LR-15 | M3 → M4 | UAT-07 |
| IH-DOC-005 | IH-DOC-005-AC01 | A | LR-15 | M3 → M4 | UAT-06, UAT-08, UAT-12 |
| IH-DOC-005 | IH-DOC-005-AC02 | A | LR-15 | M3 → M4 | UAT-06, UAT-08, UAT-12 |
| IH-DOC-006 | IH-DOC-006-AC01 | A | LR-15 | M3 → M4 | UAT-12 |
| IH-DOC-006 | IH-DOC-006-AC02 | A | LR-15 | M3 → M4 | UAT-12 |
| IH-CHAT-001 | IH-CHAT-001-AC01 | A | LR-15 | M3 → M4 | UAT-08 |
| IH-CHAT-001 | IH-CHAT-001-AC02 | A | LR-15 | M3 → M4 | UAT-08 |
| IH-CHAT-002 | IH-CHAT-002-AC01 | A | LR-15 | M3 → M4 | UAT-08 |
| IH-CHAT-002 | IH-CHAT-002-AC02 | A | LR-15 | M3 → M4 | UAT-08 |
| IH-CHAT-003 | IH-CHAT-003-AC01 | A | LR-15 | M3 → M4 | UAT-09 |
| IH-CHAT-003 | IH-CHAT-003-AC02 | A | LR-15 | M3 → M4 | UAT-09 |
| IH-CHAT-004 | IH-CHAT-004-AC01 | A | LR-15 | M3 → M4 | UAT-08, UAT-12 |
| IH-CHAT-004 | IH-CHAT-004-AC02 | A | LR-15 | M3 → M4 | UAT-08, UAT-12 |
| IH-CHAT-004 | IH-CHAT-004-AC03 | A | LR-15 | M3 → M4 | UAT-08, UAT-12 |
| IH-CHAT-004 | IH-CHAT-004-AC04 | A | LR-15 | M3 → M4 | UAT-08, UAT-12 |
| IH-CHAT-004 | IH-CHAT-004-AC05 | A | LR-15 | M3 → M4 | UAT-08, UAT-12 |
| IH-CHAT-005 | IH-CHAT-005-AC01 | A | LR-15 | M3 → M4 | UAT-09, UAT-12 |
| IH-CHAT-005 | IH-CHAT-005-AC02 | A | LR-15 | M3 → M4 | UAT-09, UAT-12 |
| IH-NOTE-001 | IH-NOTE-001-AC01 | A | LR-15 | M3 → M4 | UAT-10 |
| IH-NOTE-001 | IH-NOTE-001-AC02 | A | LR-15 | M3 → M4 | UAT-10 |
| IH-NOTE-001 | IH-NOTE-001-AC03 | A | LR-15 | M3 → M4 | UAT-10 |
| IH-NOTE-001 | IH-NOTE-001-AC04 | A | LR-15 | M3 → M4 | UAT-10 |
| IH-NOTE-002 | IH-NOTE-002-AC01 | A | LR-15 | M3 → M4 | UAT-10, UAT-12 |
| IH-NOTE-002 | IH-NOTE-002-AC02 | A | LR-15 | M3 → M4 | UAT-10, UAT-12 |
| IH-AI-001 | IH-AI-001-AC01 | D1 | LR-18 | M3 → M4 | UAT-11 |
| IH-AI-001 | IH-AI-001-AC02 | D1 | LR-18 | M3 → M4 | UAT-11 |
| IH-AI-002 | IH-AI-002-AC01 | A | LR-18 | M3 → M4 | UAT-11 |
| IH-AI-002 | IH-AI-002-AC02 | A | LR-18 | M3 → M4 | UAT-11 |
| IH-AI-003 | IH-AI-003-AC01 | D1 | LR-18 | M3 → M4 | UAT-11, UAT-14 |
| IH-AI-003 | IH-AI-003-AC02 | A | LR-18 | M3 → M4 | UAT-11, UAT-14 |
| IH-AI-004 | IH-AI-004-AC01 | D1 | LR-18 | M3 → M4 | UAT-11, UAT-12 |
| IH-AI-004 | IH-AI-004-AC02 | A | LR-18 | M3 → M4 | UAT-11, UAT-12 |
| IH-MM-001 | IH-MM-001-AC01 | N | - | Mở rộng | UAT-11 |
| IH-MM-001 | IH-MM-001-AC02 | N | - | Mở rộng | UAT-11 |
| IH-MM-002 | IH-MM-002-AC01 | N | - | Mở rộng | UAT-11, UAT-15 |
| IH-MM-002 | IH-MM-002-AC02 | N | - | Mở rộng | UAT-11, UAT-15 |
| IH-SUM-001 | IH-SUM-001-AC01 | A | LR-16 | M3 → M4 | UAT-11 |
| IH-SUM-001 | IH-SUM-001-AC02 | A | LR-16 | M3 → M4 | UAT-11 |
| IH-SUM-002 | IH-SUM-002-AC01 | A | LR-16 | M3 → M4 | UAT-10, UAT-11 |
| IH-SUM-002 | IH-SUM-002-AC02 | A | LR-16 | M3 → M4 | UAT-10, UAT-11 |
| IH-SLD-001 | IH-SLD-001-AC01 | N | - | Mở rộng | UAT-11 |
| IH-SLD-001 | IH-SLD-001-AC02 | N | - | Mở rộng | UAT-11 |
| IH-SLD-002 | IH-SLD-002-AC01 | N | - | Mở rộng | UAT-11, UAT-15 |
| IH-SLD-002 | IH-SLD-002-AC02 | N | - | Mở rộng | UAT-11, UAT-15 |
| IH-QUIZ-001 | IH-QUIZ-001-AC01 | A | LR-17 | M3 → M4 | UAT-11 |
| IH-QUIZ-001 | IH-QUIZ-001-AC02 | A | LR-17 | M3 → M4 | UAT-11 |
| IH-QUIZ-002 | IH-QUIZ-002-AC01 | A | LR-17 | M3 → M4 | UAT-11 |
| IH-QUIZ-002 | IH-QUIZ-002-AC02 | A | LR-17 | M3 → M4 | UAT-11 |
| IH-RPT-001 | IH-RPT-001-AC01 | N | - | Mở rộng | UAT-11 |
| IH-RPT-001 | IH-RPT-001-AC02 | N | - | Mở rộng | UAT-11 |
| IH-RPT-002 | IH-RPT-002-AC01 | N | - | Mở rộng | UAT-11, UAT-13 |
| IH-RPT-002 | IH-RPT-002-AC02 | N | - | Mở rộng | UAT-11, UAT-13 |
| IH-OUT-001 | IH-OUT-001-AC01 | D1 | LR-18 | M3 → M4 | UAT-11, UAT-13 |
| IH-OUT-001 | IH-OUT-001-AC02 | A | LR-18 | M3 → M4 | UAT-11, UAT-13 |
| IH-OUT-002 | IH-OUT-002-AC01 | A | LR-18 | M3 → M4 | UAT-11, UAT-12 |
| IH-OUT-002 | IH-OUT-002-AC02 | A | LR-18 | M3 → M4 | UAT-11, UAT-12 |
| IH-OUT-003 | IH-OUT-003-AC01 | A | LR-18 | M3 → M4 | UAT-12 |
| IH-OUT-003 | IH-OUT-003-AC02 | A | LR-18 | M3 → M4 | UAT-12 |
| IH-DATA-001 | IH-DATA-001-AC01 | D1 | LR-15/LR-18 | M3 → M4 | UAT-05, UAT-06, UAT-08, UAT-10, UAT-11, UAT-20 |
| IH-DATA-001 | IH-DATA-001-AC02 | D1 | LR-15/LR-18 | M3 → M4 | UAT-05, UAT-06, UAT-08, UAT-10, UAT-11, UAT-20 |
| IH-DATA-001 | IH-DATA-001-AC03 | D1 | LR-15/LR-18 | M3 → M4 | UAT-05, UAT-06, UAT-08, UAT-10, UAT-11, UAT-20 |
| IH-DATA-001 | IH-DATA-001-AC04 | A | LR-15/LR-18 | M3 → M4 | UAT-05, UAT-06, UAT-08, UAT-10, UAT-11, UAT-20 |
| IH-DATA-001 | IH-DATA-001-AC05 | A | LR-15/LR-18 | M3 → M4 | UAT-05, UAT-06, UAT-08, UAT-10, UAT-11, UAT-20 |
| IH-DATA-001 | IH-DATA-001-AC06 | A | LR-15/LR-18 | M3 → M4 | UAT-05, UAT-06, UAT-08, UAT-10, UAT-11, UAT-20 |
| IH-DATA-002 | IH-DATA-002-AC01 | A | LR-17 | M3 → M4 | UAT-10, UAT-11, UAT-12, UAT-20 |
| IH-DATA-002 | IH-DATA-002-AC02 | A | LR-22 | M3 → M4 | UAT-10, UAT-11, UAT-12, UAT-20 |
| IH-DATA-002 | IH-DATA-002-AC03 | A | LR-17 | M3 → M4 | UAT-10, UAT-11, UAT-12, UAT-20 |
| IH-DATA-002 | IH-DATA-002-AC04 | A | LR-22 | M3 → M4 | UAT-10, UAT-11, UAT-12, UAT-20 |
| IH-UX-001 | IH-UX-001-AC01 | D2 | LR-10/LR-21 | M2 → M4 | UAT-15 |
| IH-UX-001 | IH-UX-001-AC02 | D2 | LR-10/LR-21 | M2 → M4 | UAT-15 |
| IH-UX-002 | IH-UX-002-AC01 | D2 | LR-10/LR-21 | M2 → M4 | UAT-15 |
| IH-UX-002 | IH-UX-002-AC02 | A | LR-10/LR-21 | M2 → M4 | UAT-15 |
| IH-UX-003 | IH-UX-003-AC01 | A | LR-10/LR-21 | M2 → M4 | UAT-15 |
| IH-UX-003 | IH-UX-003-AC02 | A | LR-10/LR-21 | M2 → M4 | UAT-15 |
| IH-UX-004 | IH-UX-004-AC01 | A | LR-10/LR-21 | M2 → M4 | UAT-07, UAT-09, UAT-14, UAT-15 |
| IH-UX-004 | IH-UX-004-AC02 | A | LR-10/LR-21 | M2 → M4 | UAT-07, UAT-09, UAT-14, UAT-15 |
| IH-MSG-001 | IH-MSG-001-AC01 | A | LR-15/LR-18 | M3 → M4 | UAT-18 |
| IH-MSG-001 | IH-MSG-001-AC02 | A | LR-15/LR-18 | M3 → M4 | UAT-18 |
| IH-MSG-002 | IH-MSG-002-AC01 | A | LR-15/LR-18 | M3 → M4 | UAT-15, UAT-18 |
| IH-MSG-002 | IH-MSG-002-AC02 | A | LR-15/LR-18 | M3 → M4 | UAT-15, UAT-18 |
| IH-MSG-003 | IH-MSG-003-AC01 | A | LR-14/LR-24 | M3 → M4 | UAT-01, UAT-02, UAT-03, UAT-19 |
| IH-MSG-003 | IH-MSG-003-AC02 | A | LR-14/LR-24 | M3 → M4 | UAT-01, UAT-02, UAT-03, UAT-19 |
| IH-MSG-003 | IH-MSG-003-AC03 | A | LR-14/LR-24 | M3 → M4 | UAT-01, UAT-02, UAT-03, UAT-19 |
| IH-MSG-004 | IH-MSG-004-AC01 | A | LR-15/LR-18 | M3 → M4 | UAT-07, UAT-09, UAT-14, UAT-18 |
| IH-MSG-004 | IH-MSG-004-AC02 | A | LR-15/LR-18 | M3 → M4 | UAT-07, UAT-09, UAT-14, UAT-18 |
| IH-INT-001 | IH-INT-001-AC01 | D1 | LR-11/LR-18 | M2.1 → M4 | UAT-16 |
| IH-INT-001 | IH-INT-001-AC02 | A | LR-11/LR-18 | M2.1 → M4 | UAT-16 |
| IH-INT-002 | IH-INT-002-AC01 | A | LR-11/LR-18 | M2.1 → M4 | UAT-06, UAT-11, UAT-15, UAT-16 |
| IH-INT-002 | IH-INT-002-AC02 | A | LR-11/LR-18 | M2.1 → M4 | UAT-06, UAT-11, UAT-15, UAT-16 |
| IH-INT-002 | IH-INT-002-AC03 | A | LR-11/LR-18 | M2.1 → M4 | UAT-06, UAT-11, UAT-15, UAT-16 |
| IH-INT-003 | IH-INT-003-AC01 | D3 | LR-09/LR-23 | M2.1 → M4 | UAT-01, UAT-02, UAT-03, UAT-11, UAT-16 |
| IH-INT-003 | IH-INT-003-AC02 | A | LR-09/LR-23 | M2.1 → M4 | UAT-01, UAT-02, UAT-03, UAT-11, UAT-16 |
| IH-INT-004 | IH-INT-004-AC01 | A | LR-11/LR-18 | M2.1 → M4 | UAT-07, UAT-09, UAT-12, UAT-16, UAT-17, UAT-20 |
| IH-INT-004 | IH-INT-004-AC02 | A | LR-11/LR-18 | M2.1 → M4 | UAT-07, UAT-09, UAT-12, UAT-16, UAT-17, UAT-20 |
| IH-NFR-001 | IH-NFR-001-AC01 | A | LR-20/LR-24 | M4 | UAT-01, UAT-02, UAT-03, UAT-04 |
| IH-NFR-001 | IH-NFR-001-AC02 | A | LR-20/LR-24 | M4 | UAT-01, UAT-02, UAT-03, UAT-04 |
| IH-NFR-001 | IH-NFR-001-AC03 | A | LR-20/LR-24 | M4 | UAT-01, UAT-02, UAT-03, UAT-04 |
| IH-NFR-001 | IH-NFR-001-AC04 | A | LR-20/LR-24 | M4 | UAT-01, UAT-02, UAT-03, UAT-04 |
| IH-NFR-001 | IH-NFR-001-AC05 | A | LR-20/LR-24 | M4 | UAT-01, UAT-02, UAT-03, UAT-04 |
| IH-NFR-002 | IH-NFR-002-AC01 | A | LR-20/LR-24 | M4 | UAT-12, UAT-13 |
| IH-NFR-002 | IH-NFR-002-AC02 | A | LR-20/LR-24 | M4 | UAT-12, UAT-13 |
| IH-NFR-003 | IH-NFR-003-AC01 | A | LR-20/LR-24 | M4 | UAT-13, UAT-14 |
| IH-NFR-003 | IH-NFR-003-AC02 | A | LR-20/LR-24 | M4 | UAT-13, UAT-14 |
| IH-NFR-004 | IH-NFR-004-AC01 | A | LR-20/LR-24 | M4 | UAT-07, UAT-12, UAT-16 |
| IH-NFR-004 | IH-NFR-004-AC02 | A | LR-20/LR-24 | M4 | UAT-07, UAT-12, UAT-16 |
| IH-NFR-005 | IH-NFR-005-AC01 | A | LR-20/LR-24 | M4 | UAT-07, UAT-09, UAT-14, UAT-16 |
| IH-NFR-005 | IH-NFR-005-AC02 | A | LR-20/LR-24 | M4 | UAT-07, UAT-09, UAT-14, UAT-16 |
| IH-NFR-006 | IH-NFR-006-AC01 | A | LR-21 | M4 | UAT-17 |
| IH-NFR-006 | IH-NFR-006-AC02 | A | LR-21 | M4 | UAT-17 |
| IH-NFR-007 | IH-NFR-007-AC01 | D3 | LR-21/LR-23 | M4 | UAT-17 |
| IH-NFR-007 | IH-NFR-007-AC02 | A | LR-21/LR-23 | M4 | UAT-17 |
| IH-NFR-008 | IH-NFR-008-AC01 | A | LR-20/LR-24 | M4 | UAT-16 |
| IH-NFR-008 | IH-NFR-008-AC02 | A | LR-20/LR-24 | M4 | UAT-16 |
| IH-NFR-009 | IH-NFR-009-AC01 | A | LR-26 | M5 | UAT-16 |
| IH-NFR-009 | IH-NFR-009-AC02 | A | LR-26 | M5 | UAT-16 |
| IH-NFR-010 | IH-NFR-010-AC01 | A | LR-25 | M5 | UAT-16 |
| IH-NFR-010 | IH-NFR-010-AC02 | A | LR-25 | M5 | UAT-16 |
| IH-NFR-011 | IH-NFR-011-AC01 | A | LR-14/LR-24 | M4 | UAT-04, UAT-13, UAT-21 |
| IH-NFR-011 | IH-NFR-011-AC02 | A | LR-14/LR-24 | M4 | UAT-04, UAT-13, UAT-21 |
| IH-REL-001 | IH-REL-001-AC01 | D4 | LR-25 | M5 | UAT-01..21 |
| IH-REL-001 | IH-REL-001-AC02 | A | LR-25 | M5 | UAT-01..21 |
| IH-REL-002 | IH-REL-002-AC01 | A | LR-25/LR-26 | M5 | UAT-16 |
| IH-REL-002 | IH-REL-002-AC02 | A | LR-25/LR-26 | M5 | UAT-16 |
| IH-REL-003 | IH-REL-003-AC01 | A | LR-27 | M5 | UAT-16 |
| IH-REL-003 | IH-REL-003-AC02 | A | LR-27 | M5 | UAT-16 |
