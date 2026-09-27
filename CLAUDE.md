@AGENTS.md

## Ghi chú riêng cho Claude Code

- Bắt đầu mỗi task bằng plan mode: trình bày plan, chờ học viên duyệt rồi mới sửa code.
- Không tắt permission prompt (không dùng `--dangerously-skip-permissions` hoặc `bypassPermissions`). Đọc kỹ từng lệnh trước khi duyệt.
- `.claude/settings.json` chặn đọc `.env`, `.env.*` (kể cả `.env.example`), `secrets/`, file khóa; chặn `rm -rf`, `git push --force`, `git reset --hard` và lệnh đóng gói. Đây là lưới an toàn, không phải ranh giới bảo mật: không vòng qua bằng script, `grep -r` hoặc `bash -c`. Cần biết tên biến cấu hình thì đọc mục "Cấu hình AI" trong `README.md`.
- Thiết lập cá nhân đặt trong `.claude/settings.local.json` (không commit); không nới rule `deny` của repo.
- Không dùng `/feedback` khi transcript chứa bài làm chưa công khai.
