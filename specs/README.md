# Specs: Specify -> Plan -> Tasks -> Implement

Chuỗi spec (đặc tả) dùng làm đầu vào cho coding agent (Kit K8). Bắt buộc cho **Quiz**; tính năng khác dùng lại template nếu muốn.

| Bước | File | Milestone | Đầu vào | Người chốt |
| --- | --- | --- | --- | --- |
| Specify | `specs/<feature>/spec.md` | M2.1 LR-08 | SRS, trace đã `Human-verified` | Học viên |
| Plan | `specs/<feature>/plan.md` | M2 LR-11 | spec, OpenAPI, ERD, ADR | Học viên |
| Tasks | `specs/<feature>/tasks.md` | M2 LR-11 | plan | Học viên |
| Implement | PR theo từng task | M3 LR-16..18 | task + agent task brief | Học viên review diff |

Quy tắc:

- spec mô tả **cái gì và vì sao** theo SRS, không chép lại toàn bộ SRS; dẫn mã AC.
- Mỗi task nhỏ đủ review trong một PR (khoảng 400 dòng diff trở xuống), có AC, lệnh kiểm và stop condition (điều kiện dừng).
- Khi code khác plan, cập nhật plan/tasks trong cùng PR và ghi lý do. Thay đổi hành vi phải quay lại spec.

Template: [spec](_template/spec.md), [plan](_template/plan.md), [tasks](_template/tasks.md).
