# Integration Guide - Auth và Notebook

## Mục tiêu

Mở rộng starter mà không sửa lại ingestion/RAG core. Auth, Notebook, quyền và quota là phần học viên triển khai.

## Thay đổi schema dự kiến

- Thêm `users`, `notebooks` và ownership theo SRS.
- Thêm `notebook_id NOT NULL` vào documents và operation scope.
- Chuyển dedup từ toàn starter sang unique/lock theo `(notebook_id, content_sha256)`.
- Scope operation record theo `(owner_id, operation_type, operation_key)`.
- Backfill dữ liệu starter bằng migration có owner/notebook mục tiêu được operator chọn rõ. Không tự gán cho user đầu tiên.

## Policy points

- Router xác thực session rồi resolve owner từ server.
- Service nhận `authorized_notebook_id` hoặc policy object đã xác minh.
- `document_ids` phải cùng Notebook, thuộc owner, `Ready` và chưa xóa.
- Retrieval luôn nhận allow-list ID đã kiểm chứng; không query toàn index rồi lọc ở response.
- Delete Notebook/document phải dùng cùng lock/fencing với chat và AI task.
- Quota 20 document tính cả `Failed` chưa xóa.

## Thứ tự migration khuyến nghị

1. Tạo bảng Auth/Notebook và nullable foreign key.
2. Chọn owner/notebook cho dữ liệu starter bằng command vận hành có tham số bắt buộc.
3. Backfill và kiểm orphan/cross-owner.
4. Đặt foreign key `NOT NULL`, index và unique scope mới.
5. Bật policy trong API, sau đó mới mở UI đa người dùng.

Mỗi bước cần forward migration và rollback procedure về ứng dụng. Không rollback bằng xóa volume.
