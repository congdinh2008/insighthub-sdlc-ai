# Database migrations

Migration là forward-only, chạy theo thứ tự tên file dưới PostgreSQL advisory lock. Mỗi file phải idempotent cho lần retry sau crash và được ghi vào `schema_migrations`.

Không sửa migration đã phát hành. Tạo file số tiếp theo, thêm integration test cho fresh schema và upgrade schema hiện hữu. Không dùng xóa volume làm migration.
