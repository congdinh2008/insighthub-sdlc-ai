# Spike Auth, Google và email tại M2.1

B2B C07 - Dự án cá nhân InsightHub | Phiên bản 2.2 | 19/09/2026

Mục tiêu: chọn giải pháp Auth có bằng chứng đáp ứng SRS trước khi tích hợp vào Notebook. Thực hiện tại M2.1; kết quả làm căn cứ cho thiết kế tại M2. Starter chưa có Auth nghiệp vụ.

## 1. Chuẩn bị

| Đầu vào | Trách nhiệm và cách sử dụng |
| --- | --- |
| Giải pháp Auth | Học viên so sánh thư viện/dịch vụ hỗ trợ password, OIDC, xác minh email, linking và thu hồi phiên; ghi phiên bản và phần phải tự bổ sung |
| OAuth client/test users | Giảng viên hoặc quản trị lớp cấp quyền/cấu hình được phép; học viên khai báo đúng redirect URI của giải pháp đã chọn, không chia sẻ password Google |
| Email transport | Dùng mailbox local cho phát triển; chuẩn bị provider và địa chỉ test được phép để kiểm live |
| Chính sách | Lấy LIM-01, LIM-07..09, LIM-19 và BR-03 từ [SRS](../../requirements/SRS_InsightHub_v2.4.md); không dùng default thư viện thay quy định |
| Dữ liệu | Tài khoản A/B độc lập; account password Active, PendingVerification và Google-only; dữ liệu giả, email thử nghiệm |
| Secret | Bổ sung tên biến của extension vào `.env.example`; giá trị thật chỉ ở `.env` hoặc kho bí mật lớp. Không tạo nhiều file env theo chức năng |

Đọc [Integration Guide](../Integration_Guide_Auth_Notebook.md) để xác định nơi thêm ownership. Chọn thư viện thay vì tự viết thuật toán mật mã; học viên vẫn chịu trách nhiệm quy tắc nghiệp vụ và authorization.

## 2. Trình tự thực hiện

1. Lập bảng AC - khả năng thư viện - phần cần bổ sung - cách kiểm, ưu tiên linking/pending account/thu hồi phiên.
2. Tạo nhánh spike nhỏ, thiết lập callback/session và mailbox test. Chưa cần xây toàn bộ UI sản phẩm.
3. Chạy các phép thử bên dưới; ghi rõ `mock`, `local sink` hoặc `live`.
4. Chọn phương án qua ADR: ít nhất hai lựa chọn, căn cứ AC, effort/rủi ro và hạn chế.
5. Ghi blocker với owner/bước kiểm lại; chỉ tích hợp phần có contract rõ. Giữ evidence spike để mở rộng ở M3-M4.

## 3. Phép thử phải chuẩn bị và thực hiện

| Phép thử | Kết quả kỳ vọng và bằng chứng |
| --- | --- |
| Password/verification | Đăng ký PendingVerification; không được truy cập Notebook trước xác minh; link có hạn, đúng mục đích, dùng một lần |
| OIDC hợp lệ | Thư viện kiểm token ở server; identity theo issuer + sub; email được xác minh; cấp đúng phiên |
| Callback sai/hủy | Sai state, nonce theo flow, issuer/audience/expiry hoặc hủy đăng nhập không tạo quyền/phiên |
| Email trùng Active | Không auto-merge theo email; liên kết sau xác nhận mật khẩu trong đúng giao dịch, tối đa 5 phút và một lần |
| Email trùng PendingVerification | Theo BR-03/UC-02.A4: đặt lại mật khẩu, vô hiệu credential/phiên/link cũ trước Active; không tự login/link Google sau reset |
| Reset/change password | Phản hồi công khai không tiết lộ account existence; link sai/hết hạn/dùng lại bị từ chối; reset/change thành công thu hồi phiên cũ trong 60 giây |
| Google-only | Không tự tạo password hoặc gửi link đặt password; EML-004 hướng dẫn đăng nhập Google |
| Session/browser | Hết hạn 2 giờ không hoạt động hoặc 24 giờ tuyệt đối; polling không kéo dài idle; logout/API bằng phiên cũ bị từ chối; client xóa dữ liệu phiên và không nhận kết quả muộn sau hết phiên |
| Throttle | Giới hạn sai mật khẩu theo cả account/IP, dùng chung login/reauth; gửi email theo LIM-09; không khóa vĩnh viễn |
| Token gửi lại | Khi phát hành link mới thành công, link trước cùng mục đích hết hiệu lực; yêu cầu bị rate-limit trước phát hành không vô hiệu link hiện hữu |
| Email bị lỗi | Lưu trạng thái chuyển giao và mã tra cứu; lỗi EML-003/005 không hoàn tác linking/password hoặc khôi phục phiên cũ |
| Authorization | API từ chối user B đổi ID Notebook/document/source/operation của A; server không tin owner client gửi |

Có thể dùng test doubles tại biên provider để tái hiện token sai hoặc lỗi vận chuyển. Google login và EML-001..005 vẫn phải có evidence live tại M4; không ghi toàn bộ bảng đã đạt chỉ từ local sink.

## 4. Kiểm email giao dịch

| Mã | Thời điểm | Kiểm thực tế |
| --- | --- | --- |
| EML-001 | Đăng ký/chờ xác minh | Đúng hộp thư, link verification và hạn; mở link có kết quả đúng |
| EML-002 | Khôi phục account có password | Đúng hộp thư, link reset một lần; không thay password trước hoàn tất |
| EML-003 | Sau linking Google hợp lệ | Thông báo sự kiện/hướng dẫn hỗ trợ; không có link cấp quyền |
| EML-004 | Khôi phục account Google-only | Hướng dẫn Google; không có link đặt password |
| EML-005 | Sau reset/change thành công | Thông báo sự kiện và đăng nhập lại; không có password hoặc link cấp phiên |

Evidence live ghi loại email, tài khoản test đã che địa chỉ, thời điểm, transport/message ID an toàn, thư nhận thực tế và kết quả hành động. Chỉ log “provider accepted” chưa chứng minh đã nhận thư. Không chụp URL/token xác thực còn hiệu lực vào hồ sơ nộp.

## 5. Hồ sơ nộp và xử lý blocker

Nộp ADR, cấu hình mẫu không secret, bảng kết quả expected/actual, log đã lọc và dependency chưa hoàn tất. Mỗi blocker ghi ảnh hưởng AC, người xử lý và bước kiểm lại.

Nếu tenant/mạng chưa cho phép Google/email, tiếp tục phần spec, local mailbox và test seam; giữ trạng thái live `Blocked`. Giảng viên giải quyết cấu hình hoặc xác định phương án khả dụng trước phần tích hợp phụ thuộc. Không tự bỏ AC hoặc coi mock là nghiệm thu thật.

## 6. Tài liệu kỹ thuật

- [Google OpenID Connect](https://developers.google.com/identity/openid-connect/openid-connect): kiểm identity/token theo flow và thư viện sử dụng.
- [Google redirect URI validation](https://developers.google.com/identity/protocols/oauth2/web-server#uri-validation): khai báo callback đúng quy tắc, không coi URL ví dụ là endpoint đã có trong starter.
- [Mailpit configuration](https://mailpit.axllent.org/docs/configuration/): mailbox local phục vụ phát triển; không chứng minh gửi ra hộp thư bên ngoài.
- [OWASP Forgot Password](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html): nguyên tắc bảo vệ reset; thời hạn cụ thể vẫn theo SRS của bài tập.
