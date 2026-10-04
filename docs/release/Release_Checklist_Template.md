# Checklist phát hành InsightHub <R1 | R1.1>

Dùng cho LR-25 (R1) và LR-27 (R1.1). Sao chép file này thành `docs/release/Release_Checklist_<R1|R1.1>.md`, điền từng dòng theo **đúng commit phát hành**. Dòng chưa kiểm, bị chặn hoặc bỏ qua ghi rõ lý do, không đánh dấu đạt.

Tag: <tag> | Commit: <SHA> | Ngày: <ngày> | Người kiểm: <tên>

## 1. Phạm vi và truy vết

| Mục kiểm | Lệnh hoặc cách kiểm | Kết quả | Evidence |
| --- | --- | --- | --- |
| Trace đủ 153 AC áp dụng, 12 ngoài phạm vi | `python3 scripts/trace_check.py --gate M5` | | |
| AC Core R1 có `test_ids` và evidence trực tiếp | Lọc `tier=Core`, `risk=R1` trong `trace/ac-trace.csv` | | |
| Phần chưa đạt và AC Extended đã làm được ghi trong ghi chú phát hành | Đối chiếu [Release Notes](Release_Notes_Template.md) | | |

## 2. Kiểm tự động trên đúng commit

| Mục kiểm | Lệnh | Kết quả | Evidence |
| --- | --- | --- | --- |
| Backend, Web, công cụ | `DB_PORT=5434 make COMPOSE="docker compose --env-file .env.example -p insighthub-c07-check" test` | | |
| App CI xanh trên commit phát hành | Liên kết lần chạy GitHub Actions | | |
| Eval fixture đạt trên đúng commit phát hành | Bước `eval-fixture` của App CI hoặc `make eval` với suite của bài làm | | |
| Smoke có phiên đăng nhập | `INSIGHTHUB_SESSION_COOKIE` từ `scripts/session_cookie.py`, rồi `make smoke` | | |
| E2E hành trình M3.1 | `make test-pw` | | |
| Dependency và secret scan | Cấu hình CI của M1 | | |

## 3. Gói phát hành và cài sạch

| Mục kiểm | Cách kiểm | Kết quả | Evidence |
| --- | --- | --- | --- |
| Git tag annotated trỏ đúng commit | `git show <tag> --no-patch` | | |
| Gói có checksum, `.env.example`, hướng dẫn cài, chạy, xử lý lỗi | `sha256sum <gói>` | | |
| Gói không chứa `.env`, khóa, dữ liệu thật, cookie | Kiểm danh sách file trong gói | | |
| Cài sạch trên thư mục hoặc máy khác theo hướng dẫn | Clone hoặc giải nén mới, `docker compose up --build -d --wait` | | |
| Luồng chính sau cài sạch: đăng nhập, Notebook, Document, Chat, Summary, Quiz | Thực hiện qua UI | | |

## 4. Dữ liệu, nâng cấp và khôi phục (LR-26)

| Mục kiểm | Cách kiểm | Kết quả | Evidence |
| --- | --- | --- | --- |
| Migration chạy trên dữ liệu đã có | `make migrate` trên bản sao dữ liệu | | |
| Backup và restore gồm bảng Auth, `ai_jobs` và bảng bài làm | `--extra-tables auth_user,auth_session,auth_account,auth_verification,ai_jobs,<bảng bài làm>` | | |
| Quyền A/B sau restore | Đăng nhập A và B, thử đọc chéo bằng ID | | |
| Rollback R1.1 về R1 không mất dữ liệu (chỉ R1.1) | Theo kế hoạch rollback của CR | | |

## 5. Tính năng AI và ghi chú phát hành

| Mục kiểm | Cách kiểm | Kết quả | Evidence |
| --- | --- | --- | --- |
| Nhãn "nội dung do AI tạo" trên Chat, Summary, Quiz | Ảnh chụp UI | | |
| Provider, model, phiên bản prompt và schema khớp AI-BOM | `make ai-bom` | | |
| Giới hạn đã biết, kênh báo sự cố | Ghi chú phát hành | | |
| Lỗi còn mở có mức độ và hướng xử lý | Danh sách issue | | |

## 6. Kết luận

- Quyết định: <Phát hành | Chưa phát hành>
- Lý do và điều kiện còn thiếu: <ghi rõ>
- Người quyết định và thời điểm: <tên, ngày giờ>
