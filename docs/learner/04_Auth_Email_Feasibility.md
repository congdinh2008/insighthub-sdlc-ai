# Spike khả thi Auth, Google và email

Phiên bản 1.0, 19/09/2026. Draft cho B4-B5. Đây là checklist lựa chọn và phép thử tích hợp, không phải Auth được xây sẵn trong Starter.

## Kết luận kỹ thuật và lựa chọn

Dùng thư viện/dịch vụ Auth có hỗ trợ password, OIDC, xác minh email và thu hồi phiên. Nhóm tự so sánh phương án theo AC và lập ADR; không tự viết thuật toán hash/token hoặc coi default của thư viện là đáp ứng SRS. [Integration Guide](../Integration_Guide_Auth_Notebook.md) mô tả nơi bổ sung ownership.

Google OIDC cần OAuth client, redirect URI khớp chính xác và kiểm ID token; dùng `sub` làm định danh nhà cung cấp. Kiểm `state`, issuer, audience, expiry và nonce theo flow/thư viện đã chọn. Nguồn: [Google OIDC](https://developers.google.com/identity/openid-connect/openid-connect). Redirect local được kiểm theo quy tắc ứng dụng Web; localhost là ngoại lệ với yêu cầu HTTPS trong môi trường phát triển. Nguồn: [Google URI validation](https://developers.google.com/identity/protocols/oauth2/web-server#uri-validation).

Email local có thể dùng SMTP sink như Mailpit; mặc định SMTP 1025, Web UI 8025. Môi trường này giữ thư trong máy, không gửi cho người nhận bên ngoài. Nguồn: [Mailpit configuration](https://mailpit.axllent.org/docs/configuration/). Phát hành sandbox thật cần cấu hình provider/domain và kiểm giao nhận riêng.

## Input cần chuẩn bị trước B5

| Input | Cách giữ và điều cần xác nhận |
| --- | --- |
| OAuth client ID/secret | Secret ở env hoặc kho bí mật của nhóm; đăng ký đúng redirect path của thư viện, không dùng callback ví dụ như endpoint đã tồn tại |
| Google test users/consent | Chủ tài khoản cấu hình phạm vi tester và quyền sử dụng của tổ chức; không chia sẻ password Google |
| Email transport | Dùng sink local trước; provider thật chỉ khi có tài khoản và địa chỉ thử nghiệm được phép |
| Session/token policy | Mapping LIM-01, LIM-07 đến LIM-09 và LIM-19; ghi chỗ thư viện hỗ trợ/chỗ phải bổ sung |
| Dữ liệu kiểm | Hai tài khoản riêng, một email đã có tài khoản password, một tài khoản pending và một Google-only |

Không thêm các biến này vào `.env.example` nền khi chưa chọn giải pháp; chúng thuộc extension của nhóm. Starter chỉ cần key DeepSeek/Gemini cho RAG.

## Phép thử và tiêu chí pass

| Phép thử | Expected và evidence |
| --- | --- |
| OIDC happy path | Code đổi token ở server, token được thư viện xác minh, tạo/tìm user theo issuer + sub, đúng tài khoản |
| Callback sai/hết hạn | Sai state, nonce hoặc audience/expired token bị từ chối; không tạo phiên |
| Email trùng tài khoản Active | Không tự merge vì trùng email; xác minh quyền tài khoản hiện hữu theo BR-03/LIM-19 |
| Tài khoản Pending | Nhánh tiếp nhận đúng SRS; credential/link cũ bị vô hiệu trước khi truy cập dữ liệu |
| Password reset | Phản hồi công khai không lộ account existence; token có hạn, dùng một lần; đổi mật khẩu thu hồi phiên cũ |
| Google-only | Không tự bật đổi mật khẩu ứng dụng; đường khôi phục/linking theo SRS |
| Email verification | Link hợp lệ, hết hạn, dùng lại và gửi lỗi được xử lý; kiểm tại mailbox/sink |
| Authorization | Hai user thử đổi ID Notebook/document/operation/source; mọi endpoint đều kiểm server-side |

Reset token ngẫu nhiên, hết hạn và dùng một lần là căn cứ từ [OWASP Forgot Password](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html); giá trị thời hạn và phản hồi cụ thể lấy từ SRS, không lấy ví dụ của thư viện thay chính sách sản phẩm.

## Trạng thái và xử lý phụ thuộc

Đã đối chiếu tính năng/protocol với tài liệu chính thức ngày 19/09/2026. Chưa có OAuth client/test users và email provider của lớp để xác nhận Google sign-in và giao nhận email bên ngoài trên đúng tenant. Đây là phần thử nghiệm tích hợp của học viên/instructor trước B5, không phải chức năng có sẵn được nghiệm thu bằng mock.

Nếu tenant hoặc mạng doanh nghiệp chặn dịch vụ, tiếp tục thiết kế/test ở seam bằng mock và local mailbox; ghi blocker, người phụ trách và bước kiểm lại. Không bỏ AC Google/email hoặc coi mock là nghiệm thu thật. Hồ sơ spike nộp gồm ADR lựa chọn, kết quả bảng trên và danh sách input còn thiếu; instructor quyết định phương án khả dụng trước khi nhóm tích hợp phụ thuộc.
