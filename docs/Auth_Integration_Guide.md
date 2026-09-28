# Hướng dẫn tích hợp Auth và Email

Dùng cho M2.1 (LR-09 spike), M2 (LR-11 thiết kế, ADR), M3.1 (LR-12) và M3 (LR-14). Tài liệu nêu **quyết định mặc định, fit-gap và điểm kiểm**; không phải lời giải. Hành vi phải đạt vẫn theo [SRS](learner/02_SRS_InsightHub_v1.0.md#req-ih-auth-001) và [Requirements mục 14](learner/01_Requirements_InsightHub.md#auth-email).

## 1. Thư viện mặc định

| Phương án | Khi nào dùng | Ghi chú |
| --- | --- | --- |
| **Better Auth** (TypeScript, chạy trong Next.js, lưu bảng ở PostgreSQL của app) | Mặc định của lớp | Có email/password, xác minh email, reset mật khẩu, Google, account linking, session trong DB. Học viên tập trung vào phần SRS khác mặc định thư viện |
| Authlib + pwdlib (Argon2) + session tự xây trong FastAPI | Muốn giữ Auth trong Python | Nhiều code và rủi ro bảo mật hơn; bắt buộc ADR so sánh với phương án mặc định |
| Firebase Auth | Không khuyến nghị | Email theo template dịch vụ, user nằm ngoài DB ứng dụng nên backup/restore (LR-26) phức tạp, thêm luồng dữ liệu ra nước ngoài |

Pin phiên bản thư viện trong `package-lock.json`. Giá trị mặc định có thể đổi theo phiên bản: kiểm lại bằng spike LR-09, không dựa vào tài liệu này hoặc câu trả lời của AI.

## 2. Kiến trúc cần quyết định trong ADR (M2)

| Câu hỏi | Lựa chọn thường gặp | Điểm kiểm |
| --- | --- | --- |
| FastAPI xác định người dùng thế nào? | (a) Tra bảng session của Better Auth trong cùng PostgreSQL. (b) JWT/JWKS | LIM-07 yêu cầu thu hồi phiên trong tối đa 60 giây và IH-AUTH-008-AC02 từ chối request sau logout. JWT không tra DB chỉ đạt khi TTL rất ngắn; ghi trade-off |
| Cookie đi từ trình duyệt tới API ra sao? | Next.js route/proxy chuyển tiếp cookie hoặc session token; API không nhận định danh người dùng từ header do client tự đặt | Tài khoản B gọi thẳng API `:8107` bằng ID của A phải bị từ chối |
| Email gửi từ đâu? | (a) Callback Better Auth trong Next.js gửi SMTP tới Mailpit. (b) Gọi mailer `api/app/core/mailer.py` qua endpoint nội bộ có xác thực | IH-MSG-003-AC02: lỗi gửi được ghi nhận, không đổi kết quả nghiệp vụ, không lộ tài khoản |
| Bảng Auth được quản lý thế nào? | Sinh SQL từ CLI của thư viện, **review như migration do AI/tool sinh**, đưa vào `api/migrations/` dạng forward | Chạy trên DB đã có dữ liệu; thêm bảng vào `--extra-tables` khi kiểm restore (LR-26) |

## 3. Fit-gap: mặc định thư viện so với SRS

SRS ghi rõ không coi giá trị mặc định của thư viện là đã đáp ứng chính sách sản phẩm. Bảng dưới là điểm khởi đầu cho LR-09; học viên xác nhận bằng spike.

| Chính sách SRS | Hành vi mặc định cần kiểm | Việc học viên làm |
| --- | --- | --- |
| BR-03: không tự liên kết Google khi trùng email | Account linking bật sẵn và có thể liên kết ngầm khi email trùng | Tắt liên kết ngầm (tùy chọn `disableImplicitLinking` hoặc tương đương); kiểm IH-AUTH-005-AC02 |
| LIM-01: mật khẩu 15-128 ký tự, không cắt khoảng trắng | Có tùy chọn độ dài tối thiểu/tối đa với mặc định khác SRS | Cấu hình 15/128; test mật khẩu có khoảng trắng đầu/cuối |
| LIM-07: hết hạn sau 2 giờ không hoạt động hoặc tối đa 24 giờ; thu hồi trong 60 giây | Thời hạn session và chu kỳ làm mới theo mặc định thư viện | Cấu hình idle; tự kiểm giới hạn tuyệt đối 24 giờ; API tra trạng thái session |
| Tài khoản `PendingVerification` không truy cập dữ liệu nghiệp vụ | Chế độ bắt buộc xác minh email thường chặn đăng nhập, không có phiên hạn chế | Core: chặn dữ liệu nghiệp vụ (IH-AUTH-001-AC01). Phiên hạn chế là Extended (IH-AUTH-002-AC02) |
| LIM-09: đếm sai theo tài khoản và IP, sliding window | Rate limit của thư viện theo cửa sổ và đường dẫn | Extended (IH-AUTH-003-AC02, IH-AUTH-006-AC02): tự xây bộ đếm |
| LIM-19: bằng chứng mật khẩu dùng một lần, tối đa 5 phút | Đổi mật khẩu nhận mật khẩu hiện tại trong cùng request | Ghi trong ADR cách đáp ứng IH-AUTH-010 và IH-NFR-011-AC02 |
| EML-001..005 | Có callback cho xác minh và reset; không có sẵn thông báo đổi mật khẩu, hướng dẫn tài khoản chỉ dùng Google | Tự bắt sự kiện cho EML-004, EML-005; EML-003 thuộc Extended |

## 4. Phạm vi chấm AUTH (quyết định 28/09/2026)

| Tầng | AC |
| --- | --- |
| Core (chấm) | IH-AUTH-001-AC01/02, 002-AC01, 003-AC01, 004-AC01/02, 005-AC02, 006-AC01, 007-AC01/02, 008-AC01/02, 009-AC01, 010-AC01/02; IH-MSG-003-AC01 (D5: bốn email EML-001, 002, 004, 005), IH-MSG-003-AC02 |
| Extended (Stretch, không trừ điểm) | IH-AUTH-002-AC02, 003-AC02, 005-AC01/03/04, 006-AC02, 007-AC03, 009-AC02; IH-MSG-003-AC03 |

Khi chưa làm liên kết Google, đăng nhập Google bằng email trùng tài khoản mật khẩu phải **bị từ chối an toàn**, không tự liên kết và không cấp phiên. Nguồn đầy đủ: cột `tier` trong [trace/ac-trace.csv](../trace/ac-trace.csv).

## 5. Chuẩn bị và dữ liệu

- Tài khoản Google và email **test riêng** cho khóa học; OAuth client ở chế độ testing với danh sách test user; callback trên `localhost`.
- Mailpit cho kiểm local (`make mail-up`); bằng chứng thư nhận thật gửi tới inbox test theo Requirements mục 14.
- Client secret chỉ nằm trong `.env`; không dán vào Claude, log, issue hoặc ảnh chụp.

## 6. Điểm kiểm tối thiểu trước khi báo Auth đạt

- Tài khoản B không đọc, sửa, xóa được tài nguyên của A khi gọi thẳng API bằng ID của A.
- Logout, đổi mật khẩu, reset mật khẩu làm request dùng phiên cũ bị từ chối trong giới hạn LIM-07.
- Phản hồi đăng nhập và quên mật khẩu không tiết lộ tài khoản tồn tại (IH-NFR-001-AC05).
- Log, lỗi và report không chứa mật khẩu, token, link reset (IH-NFR-008-AC02).
- `/security-review` đã chạy trên PR Auth; finding đã phân loại theo [Review Workflow](ai/Review_Workflow.md).
