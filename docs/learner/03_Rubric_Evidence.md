# Rubric và minh chứng học viên

Phiên bản 1.0, 19/09/2026. Draft chi tiết để instructor review; giữ trọng số chương trình hiện tại.

## Điểm toàn khóa

| Thành phần | Trọng số | Bằng chứng |
| --- | --- | --- |
| Quiz | 10% | Kết quả quiz theo syllabus, không thay bằng số test code |
| PRE | 15% | Bài chuẩn bị đúng hạn theo lịch lớp, tự phân tích trước AI và kiểm chứng sau AI |
| Assignment | 25% | Các milestone M1-M3, chất lượng PR, thiết kế/test và tích hợp |
| Capstone | 35% | Sản phẩm theo phạm vi được giao, demo, release và bảo vệ |
| Chuyên cần/peer review | 15% | Tham gia, review có căn cứ và phản hồi nhóm |

Điểm tổng = 0,10 × Quiz + 0,15 × PRE + 0,25 × Assignment + 0,35 × Capstone + 0,15 × Chuyên cần/peer review, các thành phần cùng thang 10. Điều kiện hiện tại: tổng và Capstone từ 6/10, không thành phần nguồn bằng 0, tham gia tối thiểu 8/10 buổi. Tỷ lệ điểm nhóm/cá nhân và hạn nộp do instructor công bố, không tự xác lập trong học liệu này.

## Rubric Capstone, thang 100 quy đổi về 10

| Tiêu chí | Điểm tối đa | Căn cứ cho mức đạt đầy đủ |
| --- | --- | --- |
| Chức năng và phạm vi | 25 | Auth, Notebook, hội thoại/ghi chú, đúng hai tool đã chọn và phần dùng chung; mapping AC có bằng chứng |
| Quyền và tính toàn vẹn | 20 | Kiểm hai tài khoản chéo nhau; server xác lập owner; xóa nguồn, session/linking, migration và retry không phá dữ liệu |
| UI/UX và Figma | 15 | Luồng chính/ngoại lệ khớp thiết kế; 1440x900 và 390x844; keyboard, lỗi và phục hồi rõ |
| Chất lượng AI và nguồn | 15 | Real AEV đúng bộ được giao, claims/locator được review, NoEvidence/injection và schema mỗi tool đạt |
| Test và release | 15 | Test dựa rủi ro, CI, clean-room, backup/restore có dữ liệu; không đóng lỗi khi chưa retest |
| Quyết định và đóng góp | 10 | ADR, PR review, giải thích code và ví dụ đã kiểm/bác bỏ AI; minh chứng cá nhân |

Với mỗi tiêu chí: 100% điểm khi đủ evidence và không có lỗi ảnh hưởng hành vi bắt buộc; 70% khi luồng chính đạt nhưng còn lỗi nhỏ đã ghi; 40% khi chỉ demo happy path hoặc thiếu bằng chứng quan trọng; 0% khi chưa triển khai/không tái hiện được. Trường hợp lộ dữ liệu chéo tài khoản, bịa dữ kiện/nguồn hoặc mất dữ liệu phải ghi yêu cầu liên quan chưa đạt và yêu cầu sửa/retest; không tự thay điều kiện hoàn thành hoặc phê duyệt ngoại lệ của instructor.

## Bộ đánh giá AI cho bài tập hai tool

- RAG: 6 trường hợp AEV-01 + lặp một câu có căn cứ = 7 lượt; bao gồm tiếng Anh, đa tài liệu, hai NoEvidence và injection có câu hỏi trả lời được.
- Mỗi tool đã chọn: 2 trường hợp theo AEV tương ứng trong SRS, tổng 4 lượt. Giữ yêu cầu định dạng và nghiệp vụ riêng của tool.
- Lặp thêm 1 trường hợp có căn cứ của một tool đã chọn: 1 lượt.
- Tổng tối thiểu cho bài tập: 12 lượt nội dung AI; thêm kiểm schema và đầu vào/lỗi dùng chung ở tầng thích hợp. PDF ingestion là phép kiểm bổ sung, không tính thay một lượt nội dung.
- Nếu chọn thêm tool hoặc thay phạm vi, cập nhật số lượt và mapping trước khi chạy. Không áp cứng 18 lượt của sản phẩm đủ năm tool vào bài tập hai tool.

Bảng mỗi lượt: case/run, SRS/AC, nguồn và hash, ý kỳ vọng, provider/model/prompt, trạng thái, claims/citations/locator, latency/token, ý có/không được nguồn hỗ trợ, verdict, reviewer và evidence. Lưu cả lượt lỗi; không chọn lại kết quả đẹp để thay lượt đã thất bại. Đối chiếu câu chữ tương đương nghĩa, không chấm riêng bằng keyword.

## Quy cách Git/PR và thư mục nộp

Một issue mô tả vấn đề/AC, một PR có phạm vi vừa review, reviewer khác người triển khai nếu quy mô nhóm cho phép. PR ghi trước/sau, lý do, test và rủi ro; link tới evidence đúng commit. Không squash hoặc viết lại lịch sử chỉ để che đóng góp.

```text
evidence/
  M0/setup.md
  M1/scope-and-backlog.md
  M2/design-and-integration.md
  M3/test-matrix.csv
  M3/ai-evaluation.json
  M4/release-and-restore.md
  individual/<member>/contribution.md
```

Mẫu dòng test: `case_id,srs_ac,commit,input,expected,actual,status,evidence,defect`. Mỗi thành viên ghi nhiệm vụ, PR/review, quyết định kỹ thuật và một lỗi tự xử lý. Nhật ký AI chỉ giữ phần cần giải thích kết quả, đã loại secret/dữ liệu cá nhân; không nộp toàn bộ hội thoại vô chọn lọc.
