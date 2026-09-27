# Module legacy chỉ định cho bài Legacy Modernization

Dùng cho buổi 7 (C02-U04-T05..T07): đọc legacy, characterization tests, refactor từng bước có rollback. Starter **không** refactor sẵn các module này; chúng được giữ nguyên để học viên thực hành.

## Module chỉ định

| Module | Hàm | Cyclomatic complexity (radon) | Vì sao chọn | Test hiện có |
| --- | --- | --- | --- | --- |
| [`api/app/core/config.py`](../api/app/core/config.py) | `Settings.validate_configuration` | E (40) | Một hàm gom mọi quy tắc cấu hình: chunk/retrieval, fixture vs real, key theo provider, kiểm URL, reranker local, model embedding. Nhiều nhánh lồng nhau, lặp logic kiểm URL, lỗi là chuỗi tự do | Một phần trong `api/tests/test_unit_config.py`; nhiều nhánh chưa có test riêng |
| [`api/app/services/ingestion.py`](../api/app/services/ingestion.py) | `extract_source` | C (19) | Rẽ nhánh theo đuôi file và magic bytes (TXT/MD/PDF), giới hạn ký tự/trang, deadline, gói lỗi `InvalidDocument`. Được gọi từ luồng ingestion chính nên thay đổi có tác động lớn | Chưa có unit test trực tiếp; chỉ được phủ gián tiếp qua integration test cần PostgreSQL |

Số liệu đo bằng `radon cc -s` trên Starter `v1.0.0-rc.3` ngày 27/09/2026. Học viên đo lại trên fork của mình trước khi bắt đầu.

## Cách làm gợi ý

1. Đọc hàm, vẽ các nhánh hành vi và liệt kê input biên (file rỗng, sai magic bytes, PDF mã hóa, vượt giới hạn; thiếu key, URL có credential, cổng sai).
2. Viết characterization tests ghi lại hành vi **hiện tại**, kể cả hành vi có vẻ lạ, trước lần sửa đầu tiên. Test phải chạy offline, không cần PostgreSQL cho `extract_source`.
3. Refactor từng bước nhỏ (extract function, bảng quy tắc, early return), chạy lại test sau mỗi bước, commit riêng để rollback được.
4. Không đổi thông điệp lỗi công khai, giới hạn mặc định, embedding identity hoặc quy tắc "provider thật không fallback sang fixture" nếu không có ADR.

## Chứng minh test bắt lỗi (mutation testing)

Rubric Assignment (mức Đầy đủ) yêu cầu chứng minh test bắt lỗi. Cách gọn: chạy mutation testing trên đúng module đã chọn, ví dụ `mutmut` cho Python, giới hạn phạm vi file để thời gian chạy ngắn. Ghi số mutant sống, phân tích ít nhất một mutant sống (test thiếu assertion hay mutant tương đương), bổ sung test rồi chạy lại. Không đặt mục tiêu phần trăm mutation score cố định; giá trị nằm ở phân tích.

## Chọn module khác

Học viên được chọn module khác (ví dụ `api/app/services/llm.py::_parse_result`, D (22)) nếu nêu lý do trong hồ sơ milestone: độ phức tạp đo được, mức rủi ro, test hiện có và phạm vi ảnh hưởng. Module chọn phải thuộc mã nền của Starter, không phải phần học viên vừa viết.
