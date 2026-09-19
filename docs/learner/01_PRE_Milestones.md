# PRE và milestone theo 10 buổi

Phiên bản 1.0, 19/09/2026. Draft; lịch nộp cụ thể do instructor gắn với lịch lớp. Mỗi buổi 150 phút trên lớp. Cột giờ dưới đây là ngân sách tự học gồm cả trước và sau buổi, tổng 45 giờ, cần pilot xác nhận.

| Buổi | Tự học | Trước buổi | Trong buổi | Sau buổi và đầu ra |
| --- | --- | --- | --- | --- |
| B1 - Foundation | 3 giờ | Đọc Learning Contract và Getting Started; giải nén, tạo Git, cấu hình fixture | Tự giải thích luồng upload/chat; so prompt thiếu/đủ context bằng AI | M0-a: ảnh hoặc log healthy, upload/nguồn/chat; 3 quan sát về giới hạn fixture |
| B2 - AI và công cụ | 4 giờ | Đọc API contract, một test và một lỗi của Starter; chuẩn bị prompt phản biện | Tự viết tiêu chí đúng/sai rồi dùng AI đề xuất test; kiểm lại nguồn | M0-b: PR nhỏ về tài liệu hoặc test, nhật ký prompt/context/output/verification; không thêm Auth vội |
| B3 - Khởi tạo dự án | 3 giờ | Đọc code theo kiến trúc; tự đề xuất backlog và rủi ro | AI hỗ trợ phân rã issue; reviewer kiểm phạm vi Instructor/học viên | M1-a: backlog có AC, owner, dependencies; Git/PR workflow; CI fixture chạy |
| B4 - Yêu cầu | 4 giờ | Đọc UC/AC được giao; đề xuất hai tool và câu hỏi làm rõ | Phân tích ngoại lệ, nguồn/quyền; dùng AI tìm mâu thuẫn rồi đối chiếu SRS | M1-b: scope chốt hai tool, mapping AC, test oracle; bắt đầu spike Auth/email |
| B5 - Thiết kế | 4 giờ | Tự vẽ luồng Auth/Notebook và mô hình dữ liệu; phác thảo Figma | Review API, ownership, migration, optimistic concurrency và giao diện | M2-a: Figma 2 viewport, ERD, API/seam và ADR lựa chọn thư viện; kế hoạch tích hợp |
| B6 - Phát triển | 6 giờ | Chuẩn bị nhánh Auth và Notebook, test quyền hai người dùng | Triển khai vertical slice; AI hỗ trợ code/review sau thiết kế đã kiểm | M2-b: Auth/Notebook chạy một luồng xuyên suốt; ownership server-side, một negative test |
| B7 - Phát triển | 6 giờ | Tiếp tục hội thoại/ghi chú và hai tool đã chọn | Tích hợp Figma, RAG và kết quả AI; kiểm refactor giữ invariant | M2-c: các luồng chính được giao chạy được, PR và test theo từng thành viên |
| B8 - Chất lượng | 6 giờ | Lập ma trận kiểm dựa rủi ro và chuẩn bị corpus/oracle | Chạy test, AEV thật, kiểm quyền/nguồn/lỗi; dùng AI hỗ trợ triage | M3: báo cáo đủ lần chạy, defect/fix/retest, claim review và giới hạn còn lại |
| B9 - Release/bảo trì | 5 giờ | Chuẩn bị README, migration, backup và gói release | Cài sạch, restore cách ly; tiếp nhận một CR/defect nhỏ | M4-a: tag/ZIP/checksum, CI, clean-room, restore và bằng chứng xử lý CR |
| B10 - Demo/bàn giao | 4 giờ | Chuẩn bị hành trình demo và evidence cá nhân | Demo, bảo vệ quyết định, peer review và phản biện AI output | M4-b: bộ nộp cuối, tự đánh giá rubric, phần chưa đạt và hướng tiếp tục |

Tổng: 45 giờ tự học + 25 giờ trên lớp. Phân bổ đề xuất giữ C01 = 7 giờ và C02 = 38 giờ tự học theo Curriculum/Syllabus v0.5; từng buổi cần đối soát trong pilot. Việc phát triển bắt đầu từ các spike/thiết kế trước B6 và tiếp tục ngoài giờ của B6-B7 trong ngân sách đã phân bổ. Không suy rằng toàn bộ Auth/Notebook/hai tool chỉ cần 12 giờ code để hoàn thiện.

## PRE B1 - Setup và hiểu ứng dụng

1. Đọc [Getting Started](../../GETTING_STARTED.md), ghi OS, Docker/Compose, cổng đang dùng và commit/package version.
2. Tạo repository từ ZIP theo hướng dẫn; chạy fixture ở namespace riêng. Upload TXT và MD, mở nguồn; chọn một tài liệu rồi hỏi, chụp kết quả có nhãn FIXTURE.
3. Tự vẽ luồng Browser - Web - API - DB - provider và chỉ ra fixture thay phần nào.
4. Viết ba câu hỏi muốn làm rõ; dùng AI tìm điểm thiếu trong sơ đồ rồi tự sửa theo code. Không dùng câu trả lời AI làm bằng chứng duy nhất.
5. Nộp `evidence/M0/setup.md`: lệnh đã chạy, kết quả, lỗi/cách xử lý, thời gian thực tế. Không chép `.env` hoặc logs có secret.

Hoàn thành khi Web/API healthy, nguồn mở được, chat fixture chạy và giải thích được vì sao fixture không chứng minh semantic quality. Nếu setup chưa đạt trong ngân sách, nộp lỗi tái hiện được để mentor hỗ trợ, không tự giấu việc chưa chạy.

## PRE B2 - Kiểm chứng thay đổi với AI

Chọn một hành vi nhỏ trong API contract. Tự viết input/expected output trước; nhờ AI bổ sung edge case; đọc code và chạy test để xác nhận hoặc bác bỏ. Nộp PR có vấn đề, thay đổi, lệnh kiểm và một nhận định AI đã phải sửa. Không yêu cầu key AI thật cho PRE B1-B2; instructor có thể demo real RAG sau khi cấu hình chung được kiểm.

## Quy cách nghiệm thu milestone

Mỗi milestone gồm: commit SHA, danh sách AC áp dụng, sản phẩm, lệnh tái hiện, kết quả thực tế, defect còn mở và bằng chứng cá nhân. M0 dùng fixture; M3 phải có real-provider cho nội dung AI. Chỉ đánh dấu pass khi evidence khớp đúng commit, không chuyển trạng thái chỉ vì đã nộp file.
