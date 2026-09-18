# ADR-003 - Operation idempotency trong database

- Status: Accepted
- Date: 19/09/2026

Upload, retry và chat dùng operation record giữ tối thiểu 24 giờ. Advisory lock serialize cùng operation key; fingerprint phát hiện key tái dùng với payload khác. Response thành công hoặc thất bại được replay. Đây là nền cho retry do mất kết nối và sẽ được scope thêm theo owner khi tích hợp Auth.
