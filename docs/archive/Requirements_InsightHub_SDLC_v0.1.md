# Requirements Specification - InsightHub SDLC

> **Tham khảo lịch sử:** Phạm vi recovery dưới đây đã được thay trong bản Requirements làm việc bằng [SRS InsightHub doanh nghiệp v1.1](../../04_Requirements/SRS_InsightHub_Enterprise_Knowledge_Management_v1.1.docx) theo yêu cầu hoàn thiện của anh Công ngày 10/09/2026, cập nhật sau review ngày 12/09/2026. Giữ nội dung cũ để truy vết, không dùng làm scope sản phẩm hiện hành hoặc yêu cầu bắt buộc retry. SRS mới chưa là bằng chứng phê duyệt/nghiệm thu.

| Thuộc tính | Giá trị |
|---|---|
| Mã | RS-B2BC07-IH-001 |
| Phiên bản | v0.1 Draft, 09/09/2026 |
| Program | B2B_C07_SDLC_with_AI, Samsung SDS customization |
| Owner | Đinh Xuân Công |
| Đối tượng | Developer đã có kinh nghiệm phát triển web/API |
| Nguồn | Chỉ đạo Developer-focused của anh Công; starter đã tách; outline Samsung SDS v2.0 |
| Trạng thái | Đặc tả mục tiêu học tập, chưa được khách nghiệm thu; tính năng mở rộng chưa được cài đặt |

## 1. Mục tiêu và vấn đề người dùng

InsightHub là thư viện tri thức nhỏ cho nhóm sản phẩm. Thành viên đưa tài liệu vào hệ thống, kiểm tra kết quả xử lý và hỏi đáp với các đoạn nguồn. Khi xử lý thất bại, giao diện hiện tại chỉ báo failed; người dùng không có thao tác khôi phục trên tài liệu đó và không biết những lần xử lý trước đã kết thúc thế nào.

Phiên bản học tập bổ sung luồng **xem lỗi -> chọn lại file gốc -> thử lại -> xem lịch sử -> hỏi đáp sau khi tài liệu ready**. Mục tiêu kỹ thuật là đưa một thay đổi có giá trị xuyên qua UI, API, service, dữ liệu và các bước kiểm chứng, phát hành, sửa lỗi. Đây là SDLC của Developer trên một ứng dụng được cung cấp sẵn môi trường local.

Thành công được đo bằng acceptance tests và bằng chứng từ yêu cầu đến bản phát hành. Chưa đặt KPI năng suất AI hoặc chất lượng câu trả lời mà chưa có baseline đo.

## 2. Actor và bối cảnh sử dụng

| Actor | Nhu cầu | Giới hạn |
|---|---|---|
| Thành viên nhóm | Upload, biết tài liệu có dùng được không, thử lại khi lỗi tạm thời, hỏi đáp | Dùng chung thư viện local; không có account/role |
| Developer hỗ trợ | Xem error code, lịch sử xử lý để tái hiện và sửa lỗi | Không xem key hoặc raw provider exception từ giao diện |
| Học viên | Phân tích, thiết kế, triển khai và bảo vệ thay đổi | Không phải xây lại hệ thống RAG hoặc hạ tầng |
| Giảng viên/reviewer | Đánh giá quyết định, code, test và khả năng giải thích | Dùng corpus giả lập và lỗi được inject trong test |

Hai actor nghiệp vụ đầu là cách sử dụng ứng dụng, không là hai vai trò phân quyền đã triển khai. Tài liệu thật của Samsung SDS/VTI không nằm trong corpus học tập.

## 3. Phạm vi và baseline

| Hạng mục | Starter hiện có | Mục tiêu bài tập |
|---|---|---|
| Upload TXT/MD/PDF văn bản | Có, đồng bộ, 201; tối đa 10 MB | Giữ tương thích; lỗi sau khi đã tạo bản ghi cần trả document_id |
| Danh sách tài liệu | Có status/chunk_count/error_code qua API; UI mới hiển thị trạng thái | Hiển thị lỗi có thể hành động, lọc trạng thái phía client |
| Xử lý lại | Service có checksum/identity/lock và chống trùng | API/UI retry cho đúng tài liệu |
| Lịch sử | Chưa có bảng/endpoint/UI | Lưu kết quả lần xử lý thực sự; truy vấn và hiển thị |
| Hỏi đáp | Có answer, sources và contexts | Giữ hoạt động sau recovery, hiển thị rõ fixture/real và đoạn nguồn |
| Xóa tài liệu | Có API, chưa có UI | Giữ API; UI xóa là mở rộng tùy chọn |
| Migration | Chỉ có schema cho volume mới | Migration thêm lịch sử, chạy được trên DB đang có |
| Release | Có container local và workflow kiểm tra mẫu | Bản phát hành có test, migration, smoke và hướng dẫn bàn giao |

**Must:** FR-01 đến FR-06, NFR-01 đến NFR-05 và toàn bộ pha SDLC. Không yêu cầu viết lại provider adapter hoặc thuật toán embedding.

**Tùy chọn sau core:** UI xóa có xác nhận, phân trang danh sách tài liệu phía server, đánh giá real provider trên corpus nhỏ. Chưa đưa vào điểm bắt buộc.

**Ngoài phạm vi:** account/SSO/multi-tenant, OCR, lưu file gốc lâu dài, tự động retry nền, queue/worker, AWS/EKS/Terraform, ChatOps, FinOps, hệ thống dashboard vận hành hoặc SLA production. Học viên có thể so sánh các phương án trong ADR nhưng không cần triển khai chúng.

## 4. User journeys

### J1. Nạp tài liệu thành công

Chọn file -> xác thực -> tạo document -> trích xuất/chunk/embed -> commit ready -> UI cập nhật -> hỏi đáp và xem các đoạn truy hồi. HTTP 201 chỉ khi xử lý thành công. Không đổi thành 202 khi chưa có cơ chế xử lý nền.

### J2. Khôi phục lỗi tạm thời

Một document failed do provider_error -> người dùng đọc hướng dẫn -> chọn lại đúng file gốc -> xác nhận retry -> hệ thống kiểm tra nội dung và cấu hình -> xử lý -> kết quả ready hoặc failed được lưu -> UI hiển thị trạng thái và lịch sử. Giữ nguyên document_id để truy vết.

### J3. Từ chối thao tác không hợp lệ

Người dùng chọn file khác, sai định dạng hoặc tài liệu đang pending -> hệ thống từ chối bằng mã lỗi rõ ràng -> dữ liệu và lịch sử xử lý thành công không bị thay đổi. Không tự upload một document mới để giả lập retry.

### J4. Developer xử lý lỗi sau phát hành

Từ error code và attempt_id -> tái hiện với dữ liệu giả lập -> viết regression test -> sửa/refactor -> review và kiểm tra -> ghi release note -> chạy smoke trên môi trường local và bàn giao. Không yêu cầu học viên vận hành cloud để hoàn tất journey này.

## 5. Yêu cầu chức năng và tiêu chí chấp nhận

| ID | Yêu cầu | Tiêu chí kiểm chứng |
|---|---|---|
| FR-01 | Khi mở danh sách, hệ thống phải hiển thị tên, trạng thái, số chunk và lỗi đã làm sạch | AC-01: failed có error_code và hướng dẫn; pending không được coi là ready; lọc All/Ready/Failed/Pending không thay dữ liệu; trạng thái rỗng và lỗi tải danh sách phân biệt được |
| FR-02 | Khi người dùng retry document failed bằng đúng file, hệ thống phải xử lý trên cùng ID | AC-02: thành công trả 200, ready và chunk_count > 0; document không tăng thêm; failure tiếp tục failed, chunk_count = 0; UI không báo thành công khi HTTP lỗi |
| FR-03 | Trước khi xử lý lại, hệ thống phải kiểm tra file và tính tương thích dữ liệu | AC-03: không tồn tại trả 404; tên/SHA-256/pipeline/embedding identity khác trả 409; file quá lớn 413; định dạng không hỗ trợ 400; dữ liệu không hợp lệ 422; mỗi trường hợp không tạo chunk hoặc lần xử lý mới nếu chưa qua kiểm tra |
| FR-04 | Sau một lần xử lý thực sự, hệ thống phải lưu và cho xem kết quả | AC-04: mỗi lần upload/retry có attempt_id, document_id, operation, thời điểm bắt đầu/kết thúc, outcome và error_code an toàn; lịch sử mới nhất trước; tối đa 20 mục/lần và có phân trang; ready no-op không tạo attempt; bản ghi legacy không có lịch sử hiển thị trung thực |
| FR-05 | Sau recovery, tài liệu ready phải tham gia luồng hỏi đáp hiện có | AC-05: dữ liệu failed/pending không tham gia retrieval; UI hiển thị mode và cho mở contexts/source; nêu nguồn được truy hồi, không khẳng định mọi câu trong answer đã được nguồn xác nhận |
| FR-06 | Khi xử lý lỗi sau khi tạo document, hệ thống phải cung cấp thông tin để người dùng tìm lại nó | AC-06: response lỗi có document_id và attempt_id khi đã có attempt; UI làm mới danh sách và giữ thông báo lỗi; không tạo vòng retry tự động hoặc upload trùng vì timeout |

**Quy ước retry:** failed + file hợp lệ có thể được xử lý; ready + cùng file/pipeline trả 200 với `reused=true`, không gọi provider và không thêm attempt; ready + file khác trả 409. Pending chưa đủ điều kiện retry, trả 409 sau khi lấy khóa và kiểm tra trạng thái. Hai yêu cầu retry đồng thời phải được tuần tự hóa tại cùng document; nếu yêu cầu trước hoàn tất ready, yêu cầu sau trả no-op.

File sai nội dung không được sửa bằng cách đổi tên rồi retry. Nếu tài liệu failed vì nội dung gốc không đọc được, người dùng cần chuẩn bị nội dung hợp lệ và upload thành document mới. Không đưa nút retry như một lời hứa chữa mọi loại lỗi.

### Ví dụ lỗi tạm thời phục vụ học tập

Giảng viên cung cấp test fixture/mock cho embedding provider trả lỗi ở lần đầu rồi thành công. Không thêm endpoint công khai cho phép bật lỗi, không đưa API key thật vào test. Dùng dependency injection/test doubles để tạo dữ liệu failed có checksum hợp lệ.

## 6. Yêu cầu phi chức năng

| ID | Yêu cầu và mức nghiệm thu trong lab |
|---|---|
| NFR-01 - Nhất quán | Số chunk không tăng khi gọi lại cùng tài liệu ready; retry đồng thời không tạo hai bộ chunk; lỗi giữa quá trình ghi không để lại chunk một phần; test kiểm trạng thái DB, số lần provider được gọi và kết quả API |
| NFR-02 - An toàn ứng dụng | Giới hạn file/body được áp dụng cả upload và retry; không lộ key/raw exception; ngăn mutation từ browser origin ngoài danh sách; không render HTML không tin cậy từ tài liệu/answer; không coi document text là quyền thực thi tool |
| NFR-03 - Dễ kiểm thử và bảo trì | API/validation tách khỏi ingestion; có unit, integration, contract và browser E2E cho J1-J3; ít nhất một regression test tái hiện lỗi trước sửa và characterization test trước refactor; không đặt tỷ lệ coverage thay cho hành vi cần chứng minh |
| NFR-04 - Bàn giao | Có migration forward trên DB đang có dữ liệu, kế hoạch quay về app trước và giữ lịch sử; ghi phiên bản code, môi trường, chế độ, câu lệnh và kết quả; smoke chỉ thao tác dữ liệu do chính test tạo |
| NFR-05 - Minh bạch và phản hồi | UI khóa nút khi đang gửi, có loading/error/empty; timeout yêu cầu làm mới trạng thái trước khi thao tác tiếp; fixture hiển thị rõ; log/attempt không chứa raw file hoặc nội dung câu hỏi |

Không xác lập SLO hay benchmark production. Bài kiểm tra hiệu năng trong lớp dùng fixture, một corpus cố định và cùng môi trường; học viên ghi phép đo trước/sau và giải thích giới hạn. Cảnh báo quan trọng: timeout của từng provider request hiện không phải deadline toàn bộ upload nhiều batch.

## 7. Trạng thái, dữ liệu và lịch sử

- Document: `pending -> ready | failed`; retry hợp lệ từ failed kết thúc ready hoặc failed. Cùng ID, filename và checksum đã ghi giữ nguyên.
- Baseline giữ checksum trước savepoint xử lý, kể cả khi provider lỗi. Không cần lưu lại file gốc để thực hiện core retry; người dùng cung cấp lại file.
- Một attempt biểu diễn một lần xử lý đã qua kiểm tra đủ điều kiện. Từ chối 404/409/413 trước xử lý không sinh attempt. Kết quả xử lý lỗi validation nội dung sau khi bắt đầu có thể là failed/invalid_document.
- Thời gian lưu là UTC; UI chuyển hiển thị nhất quán. Không ghi nội dung tài liệu, key, câu hỏi hoặc raw exception vào attempt.
- Lịch sử chỉ cam kết với các lần kết thúc có commit. Nếu tiến trình bị kill trước commit, không giả tạo bản ghi hoàn tất. Pending treo phải được ghi là giới hạn và tình huống phân tích; tự phục hồi sau crash ngoài core.
- Khi xóa document bằng API hiện có, chunks và lịch sử tương ứng được xóa cùng giao dịch hoặc cascade. Không còn lịch sử mồ côi.

## 8. Phân bổ thực hiện và bằng chứng

| Mốc | Công việc bắt buộc | Đầu ra |
|---|---|---|
| M1, B1-3 | Chạy starter, đọc code, sử dụng AI có kiểm soát, Git/PR/CI ứng dụng | Baseline test; context/instructions; PR review |
| M2, B4-5 | Làm rõ J1-J4/AC; API/data design; so sánh giải pháp; chia task | Spec, contract, ERD/sequence, ADR, test plan |
| M3, B6-7 | TDD retry/history/UI, giữ hành vi baseline, refactor có characterization test | Code, test, PR/diff; ASG01 trên cùng repo |
| M4, B8 | Test lỗi biên/đồng thời/E2E, threat model, sửa và retest | Evidence test/security, traceability |
| M5, B9 | Migration, release local, smoke, chẩn đoán và sửa lỗi ứng dụng | Release pack, migration evidence, defect note |
| Capstone, B10 | Demo thành công/lỗi/recovery, bảo vệ cá nhân, kế hoạch áp dụng | Một sản phẩm tích hợp M1-M5 |

Ước lượng thiết kế ban đầu cho phần mở rộng: API/service/test 8-10 giờ; history/migration 4-6 giờ; UI/E2E 6-8 giờ; review/security/release 4-6 giờ. Tổng 22-30 giờ là giả định để chạy pilot, nằm trong phần tự học 38 giờ của C02 và lab có giám sát; không cộng thành giờ bắt buộc mới. Nếu pilot vượt tải, cung cấp scaffold migration/UI trước khi bỏ bất kỳ pha SDLC nào.

## 9. Definition of Done và giới hạn xác nhận

1. FR/NFR được ánh xạ tới test hoặc evidence; có kết quả cho cả luồng thành công và lỗi.
2. Baseline regression suite còn chạy; contract thay đổi có chủ đích và được giải thích.
3. Reviewer tái lập release local từ hướng dẫn; dữ liệu đã có đi qua migration được kiểm chứng.
4. Cá nhân giải thích được code quan trọng do AI hỗ trợ, lỗi đã sửa và trade-off.
5. Không trình bày fixture như đánh giá real AI; không trình bày starter như production-ready.

Đặc tả đủ để bắt đầu thiết kế/lab và pilot. Tình hình công cụ được phép tại Samsung SDS, năng lực stack của học viên, quy mô nhóm và quyền dùng provider vẫn cần đối soát trong chuẩn bị lớp; không cản trở xây học liệu với fixture. Chưa có kết quả pilot tính năng mở rộng hoặc phê duyệt từ khách.
