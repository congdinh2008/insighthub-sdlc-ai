# Dự án cá nhân InsightHub - Yêu cầu theo milestone

B2B C07 - SDLC with AI | Phiên bản 2.2 | 19/09/2026
Học online, thực hiện cá nhân | 10 buổi, 25 giờ trên lớp và 45 giờ tự học

## 1. Sản phẩm cần hoàn thiện

Mỗi học viên xây dựng một ứng dụng InsightHub hoàn chỉnh từ starter do giảng viên cung cấp. Người dùng có thể đăng nhập, quản lý Notebook và tài liệu, hỏi đáp có nguồn, lưu hội thoại và ghi chú, tạo bản Tóm tắt và làm Quiz từ tài liệu.

| Thành phần | Starter cung cấp | Học viên hoàn thiện |
| --- | --- | --- |
| Nền ứng dụng | Next.js, FastAPI, PostgreSQL/pgvector, Docker Compose, dữ liệu mẫu và công cụ kiểm tra | Cấu hình, tích hợp và kiểm lại sau thay đổi |
| Tài khoản | Hướng dẫn tích hợp | Đăng ký, xác minh email, đăng nhập mật khẩu/Google, liên kết danh tính, quản lý phiên, khôi phục/đổi mật khẩu, hồ sơ và email giao dịch |
| Notebook và dữ liệu | Nền tải tài liệu, trích xuất, embedding, hỏi đáp và nguồn trích dẫn | Notebook, phân quyền sở hữu, hội thoại, ghi chú; vòng đời dữ liệu, hạn mức và xử lý đồng thời |
| Công cụ AI | Kết nối mô hình và nền xử lý | Tóm tắt, Quiz, quản lý tác vụ/kết quả và kiểm chất lượng nội dung |
| Bàn giao | Kiến trúc, API và hướng dẫn vận hành nền | Thiết kế Figma, kiểm thử, đánh giá AI, bảo mật, phát hành, khôi phục dữ liệu và một thay đổi sau phát hành |

[SRS 2.4](../../requirements/SRS_InsightHub_v2.4.md) là đặc tả hành vi sản phẩm. Bài tập áp dụng **151 tiêu chí chấp nhận** cho phạm vi trên; [bảng phạm vi](02_SRS_Assignment_Map.md) chỉ rõ 12 tiêu chí mở rộng còn lại. Mindmap, Slide và Báo cáo không bắt buộc. Không yêu cầu triển khai cloud production hoặc Kubernetes.

**Công cụ AI:** dùng Claude là chính; ChatGPT do công ty cung cấp để bổ trợ khi cần. DeepSeek là mô hình trả lời trong ứng dụng; embedding theo cấu hình starter. Không mặc định tài khoản Claude chat có Claude Code hoặc MCP; bài thực hành agent dùng sandbox của lớp nếu chưa có quyền trên máy cá nhân.

**Cách học:** trước buổi học, đọc tài liệu và thực hiện các việc của milestone trong khả năng hiện tại; ghi phần đã làm và câu hỏi cần hỗ trợ. Trên lớp, trao đổi các điểm khó của dự án gắn với nội dung buổi học. Sau buổi học, cập nhật bài theo phản hồi và hoàn thiện trước hạn. Tổng 45 giờ tự học đã bao gồm đọc, thực hành, kiểm thử, sửa bài và chuẩn bị bảo vệ.

**Cách làm với AI:** tự xác định yêu cầu và kết quả kỳ vọng, cung cấp ngữ cảnh, yêu cầu AI đề xuất kế hoạch, thực hiện từng thay đổi nhỏ rồi tự kiểm tra. Lưu một vài quyết định tiêu biểu đã giữ, sửa hoặc bác bỏ đề xuất AI và lý do; không cần nộp toàn bộ hội thoại. Không đưa secret, tệp `.env` thật hoặc dữ liệu công ty chưa được phép vào Git hay công cụ AI.

## 2. Lộ trình, cách nộp bài và cách tính điểm

### Lộ trình và thời hạn

| Buổi | Milestone | Kết quả chính | Tự học | Hạn hoàn thiện |
| --- | --- | --- | --- | --- |
| 1 | M0.1 | Khởi động dự án và kiểm chứng đầu ra AI | 3 giờ | Trước buổi 2 ít nhất 12 giờ |
| 2 | M0.2 | Quy trình AI Agent có kiểm soát | 4 giờ | Trước buổi 3 ít nhất 12 giờ |
| 3 | M1 | Phạm vi, kế hoạch và quy trình Git/CI | 4 giờ | Trước buổi 4 ít nhất 12 giờ |
| 4 | M2.1 | Yêu cầu, ca kiểm thử và thử nghiệm tích hợp | 5 giờ | Trước buổi 5 ít nhất 12 giờ |
| 5 | M2 | Thiết kế Figma, API và dữ liệu | 4 giờ | Trước buổi 6 ít nhất 12 giờ |
| 6 | M3.1 | Luồng nghiệp vụ đầu tiên với TDD | 5 giờ | Trước buổi 7 ít nhất 12 giờ |
| 7 | M3 | Hoàn thiện chức năng và refactor | 6 giờ | Chức năng: trước buổi 8 ít nhất 12 giờ; bài refactor: trước buổi 9 ít nhất 12 giờ |
| 8 | M4 | Kiểm thử, chất lượng AI và bảo mật | 6 giờ | Trước buổi 9 ít nhất 12 giờ |
| 9 | M5 | Phát hành và thay đổi sau phát hành | 4 giờ | Trước buổi 10 ít nhất 12 giờ |
| 10 | Capstone | Demo, bảo vệ và kế hoạch áp dụng | 4 giờ | Hồ sơ trước buổi 10 ít nhất 12 giờ; sửa theo review trong 24 giờ sau khi kết thúc buổi 10 |

Bản chuẩn bị của buổi 1-9 gửi trước giờ bắt đầu buổi học ít nhất 2 giờ. Đây là tiến độ thực tế để nhận hỗ trợ, chưa yêu cầu hoàn tất cả milestone. Ngày, giờ cụ thể và kênh nộp bài do giảng viên công bố theo lịch lớp, múi giờ Việt Nam (UTC+07:00); không suy ra ngày học từ ngày trên tài liệu.

### Nộp bài qua repository cá nhân nghĩa là gì?

**Fork** là tạo một repository thuộc tài khoản của học viên từ repository starter, giữ lại mã nguồn và lịch sử ban đầu. Học viên làm bài và lưu thay đổi trong repository của mình. Giảng viên đọc bài qua đường dẫn được gửi.

1. Mở đường dẫn starter giảng viên cấp, chọn **Fork** và chọn tài khoản cá nhân hoặc tổ chức được lớp chỉ định. Cấp quyền xem cho giảng viên nếu repository là private. Clone repository vừa tạo về máy theo [hướng dẫn khởi động](../../../../../GETTING_STARTED.md).
2. Mỗi milestone tạo một nhánh làm việc, ví dụ `milestone/m0.1`. Commit đầy đủ mã nguồn, tài liệu và test của phần đã làm; push nhánh lên repository cá nhân.
3. Tạo **Pull Request (PR)** để đề nghị đưa nhánh làm việc vào nhánh `main` của **chính repository cá nhân**. Kiểm tra cả repository đích và nhánh đích khi tạo PR. Không gửi PR vào starter của giảng viên. Tiêu đề ví dụ: `M0.1 - Thiết lập môi trường và kiểm chứng đầu ra AI`.
4. Trong PR, ghi phần đã hoàn thành, kết quả kiểm tra, phần cần hỗ trợ và đường dẫn tài liệu liên quan. Gửi **link PR và link bản ghi nộp bài** qua kênh nộp bài của lớp. Chỉ push lên Git chưa được coi là đã gửi bài cho giảng viên.
5. Sau trao đổi trên lớp, commit và push bản sửa lên cùng nhánh; PR tự cập nhật. Gửi lại link kèm trạng thái “Bản hoàn thiện”. Giữ nguyên lịch sử bản đã gửi, không force-push hoặc xóa PR để thay bài.
6. Khi tự rà soát xong và các kiểm tra đạt, merge PR vào `main` của mình. Giảng viên chấm theo phiên bản đã ghi trong bản nộp, kể cả PR đã merge. Milestone tiếp theo tạo nhánh từ `main` đã cập nhật.

**Ví dụ:** ở buổi 1, học viên tạo `milestone/m0.1`, push kết quả setup và mở PR vào `main` của repository cá nhân. Gửi link PR trước buổi 1 để giảng viên biết lỗi cần hỗ trợ. Sau buổi học, sửa lỗi trên nhánh đó, cập nhật kết quả kiểm tra và gửi bản hoàn thiện trước buổi 2 ít nhất 12 giờ.

**Commit chuyên nghiệp:** mỗi commit giải quyết một thay đổi có ý nghĩa; dùng dạng `type(scope): mô tả thay đổi`. Ví dụ `docs(setup): document verified local setup`, `feat(notebook): enforce owner access`, `test(quiz): reject answers outside the question`. Tránh thông điệp `update`, `fix all`, `done`. Không chấm theo số lượng commit. Tag chỉ bắt buộc cho bản phát hành ở M5.

Mỗi milestone có một bản ghi ngắn, gợi ý đặt tại `evidence/M0.1/submission.md` và đổi tên thư mục theo milestone. Có thể dùng mẫu sau; không bắt tạo thêm manifest:

```text
Milestone: M0.1
Link Pull Request:
Phiên bản mã nguồn đã kiểm tra: <link commit trên Git>
Đã hoàn thành: <việc và đường dẫn file/Figma/kết quả>
Đã kiểm tra: <lệnh hoặc bước chạy, kỳ vọng, thực tế, link log>
Quyết định với AI: <đề xuất đã giữ/sửa/bác bỏ và lý do>
Còn thiếu hoặc cần hỗ trợ:
```

Lấy link commit từ mục Commits của PR. Kiểm tra đúng phiên bản đó; nếu sửa mã nguồn sau khi kiểm, chạy lại phần bị ảnh hưởng và cập nhật link. Giữ log đã lọc thông tin nhạy cảm, ghi rõ chạy mô phỏng hay dịch vụ thật. Không cần lập một tài liệu riêng cho từng loại minh chứng.

### Cách đọc rubric và điểm khóa học

- Mỗi milestone có **rubric 100 điểm để phản hồi tiến độ**. Cột cách chấm chia điểm thành các phần cụ thể: có kết quả và minh chứng đúng thì nhận điểm phần đó; phần chưa làm, chưa đúng hoặc chưa kiểm được nhận 0. Các điểm này không tạo thêm thành phần điểm khóa.
- Bài chuẩn bị trước buổi học được chấm riêng theo bốn tiêu chí, mỗi tiêu chí 25 điểm: có phần tự thực hiện và câu hỏi; nội dung đúng trong phần đã làm; giải thích được cách làm và quyết định với AI; minh chứng có thể mở và kiểm lại. Chấm theo mức 0/40/70/100%: chưa có / một phần / đạt yêu cầu cơ bản / đầy đủ, rõ ràng và tái kiểm được. Không yêu cầu bản chuẩn bị đạt sản phẩm cuối milestone.
- Bài refactor ở M3 và Capstone có rubric riêng ngay tại phần tương ứng. Điểm khóa giữ nguyên: Quiz 10%, chuẩn bị trước buổi học 15%, bài refactor 25%, Capstone 35%, chuyên cần và review 15%. Điểm trên thang 100 chia 10 để quy về thang 10.
- Điều kiện hoàn thành khóa: điểm tổng và Capstone từ 6/10, không thành phần điểm nào bằng 0 và tham dự ít nhất 8/10 buổi. Điểm học tập không thay thế kết luận phần mềm đã đạt mọi yêu cầu.

Tài liệu kiến thức (KC) và hướng dẫn công cụ (TG) theo từng buổi được giảng viên cấp qua kênh học liệu lớp. Các liên kết ở từng milestone dưới đây trỏ tới tài liệu hiện có trong starter. Bản thiết kế Figma do học viên tạo tại M2 và dùng tiếp cho triển khai, kiểm thử.

## 3. M0.1 - Thiết lập môi trường và kiểm chứng đầu ra AI có cấu trúc

### 3.1 Kiến thức liên quan

- Cách mô hình ngôn ngữ xử lý ngữ cảnh và vì sao đầu ra có thể sai.
- Viết prompt có mục tiêu, dữ liệu đầu vào và yêu cầu đầu ra; JSON và kiểm tra schema.
- Cấu trúc Web/API/cơ sở dữ liệu và luồng tải tài liệu, truy xuất, trả lời có nguồn.

### 3.2 Việc cần làm

<a id="lr-01"></a>

1. **Khởi động starter.** Fork, clone, ghi link commit nền và chạy chế độ fixture. Thử tải một tệp hợp lệ và một tệp lỗi, hỏi đáp và mở nguồn. Ghi lệnh, kết quả và lỗi gặp phải; giải thích vì sao fixture chưa chứng minh chất lượng AI thật.

<a id="lr-02"></a>

2. **Tạo đầu ra có cấu trúc.** Chọn một tiêu chí chấp nhận trong SRS, nhờ Claude chuyển thành JSON gồm điều kiện ban đầu, hành vi, tình huống thành công và tình huống lỗi. Kiểm JSON bằng schema, sau đó tự đối chiếu ý nghĩa với yêu cầu gốc.

<a id="lr-03"></a>

3. **Phát hiện và sửa một lỗi AI.** Dùng một đề xuất sai thực tế hoặc lỗi có chủ đích do lớp cung cấp. Chỉ ra sai ở đâu bằng tài liệu, mã nguồn hoặc phép thử độc lập; sửa và kiểm lại. Ghi rõ nếu dùng lỗi có chủ đích.

### 3.3 Gợi ý thực hiện và ứng dụng AI

Đưa cho Claude một yêu cầu cụ thể và các trường đầu ra cần có. Yêu cầu giải thích giả định; không coi JSON đúng định dạng là nội dung đúng. Khi AI đề xuất sửa setup, kiểm nguyên nhân từ log trước khi chạy lệnh.

### 3.4 Rubric đánh giá

| Tiêu chí | Điểm tối đa | Cách chấm điểm |
| --- | --- | --- |
| Môi trường và thao tác nền | 30 | Khởi động được ứng dụng: 10; tải tệp hợp lệ và hỏi đáp có nguồn: 10; nhận diện đúng tệp lỗi: 10. |
| Prompt và đầu ra JSON | 25 | Prompt đủ mục tiêu/ngữ cảnh: 5; kiểm schema: 10; đối chiếu đầy đủ nội dung với yêu cầu gốc: 10. |
| Kiểm chứng và sửa lỗi AI | 30 | Tái hiện lỗi: 10; căn cứ độc lập: 10; sửa và kiểm lại đúng: 10. |
| Bài nộp và giải thích | 15 | Commit và PR truy cập được: 5; kết quả kiểm có phiên bản: 5; giải thích được giới hạn của fixture: 5. |
| **Tổng** | **100** | |

### 3.5 Cách nộp bài và thời hạn

**Hạn hoàn thiện:** trước buổi 2 ít nhất 12 giờ. Push nhánh `milestone/m0.1`, mở PR vào `main` của repository cá nhân và gửi link PR kèm bản ghi nộp bài cho giảng viên. Bài gồm kết quả setup, prompt/JSON/schema, trường hợp AI sai và kết quả kiểm lại.

### 3.6 Tài liệu sử dụng

[Khởi động starter](../../../../../GETTING_STARTED.md); [kiến trúc ứng dụng](../../../../Architecture_Starter_v1.md); [tài liệu mẫu](../../../../../sample-docs/README.md).

## 4. M0.2 - Thiết lập quy trình AI Agent có kiểm soát và khả năng tái sử dụng

### 4.1 Kiến thức liên quan

- Vòng làm việc của agent: lập kế hoạch, dùng công cụ, quan sát kết quả, điều chỉnh.
- MCP, giới hạn quyền, ngữ cảnh không tin cậy và điểm khôi phục.
- Hướng dẫn dự án cho AI và chuẩn hóa một tác vụ lặp.

### 4.2 Việc cần làm

<a id="lr-04"></a>

1. **Viết quy tắc dùng AI cho dự án.** Bổ sung hướng dẫn phù hợp repository: dữ liệu được sử dụng, đường dẫn/lệnh được phép, người quyết định, cách dừng và khôi phục. Thử một yêu cầu ngoài phạm vi bằng dữ liệu giả và ghi cách bị chặn.

<a id="lr-05"></a>

2. **Thực hành một quy trình agent có dùng công cụ/MCP.** Chọn việc nhỏ như đọc API và chạy một nhóm test. Thực hiện trên công cụ được cấp hoặc sandbox lớp, lưu kế hoạch, thao tác thật và kết quả. Thử một lỗi công cụ, xử lý hoặc dừng đúng; lưu checkpoint và đóng gói thành hướng dẫn/skill có thể chạy lại.

### 4.3 Gợi ý thực hiện và ứng dụng AI

Để Claude đề xuất kế hoạch trước khi cấp quyền chạy. Bắt đầu bằng quyền đọc và lệnh kiểm tra cụ thể; chỉ mở quyền sửa khi tác vụ cần. Chuẩn hóa thao tác đã chạy thành hướng dẫn tái sử dụng, tránh viết quy tắc chung không gắn với dự án.

### 4.4 Rubric đánh giá

| Tiêu chí | Điểm tối đa | Cách chấm điểm |
| --- | --- | --- |
| Hướng dẫn dự án và quyền | 25 | Quy tắc gắn đúng repo: 10; dữ liệu/quyền rõ: 10; có cách dừng/khôi phục: 5. |
| Quy trình agent thực chạy | 30 | Kế hoạch rõ: 10; thao tác công cụ/MCP có log: 10; đối chiếu kết quả với mục tiêu: 10. |
| Xử lý lỗi và giới hạn | 25 | Thử yêu cầu vượt phạm vi: 10; nhận diện và xử lý lỗi công cụ: 10; khôi phục từ checkpoint: 5. |
| Tái sử dụng và nộp bài | 20 | Hướng dẫn/skill chạy lại được: 10; PR và minh chứng đủ để giải thích: 10. |
| **Tổng** | **100** | |

### 4.5 Cách nộp bài và thời hạn

**Hạn hoàn thiện:** trước buổi 3 ít nhất 12 giờ. Gửi link PR của nhánh `milestone/m0.2` trong repository cá nhân và bản ghi nộp bài. Đính kèm quy tắc AI, hướng dẫn/skill, log thực hành và kết quả kiểm giới hạn quyền.

### 4.6 Tài liệu sử dụng

[Kiến trúc và ranh giới hệ thống](../../../../Architecture_Starter_v1.md); [API để chọn tác vụ thực hành](../../../../API_Contract_Starter_v1.md).

## 5. M1 - Lập kế hoạch dự án và thiết lập quy trình phát triển có AI hỗ trợ

### 5.1 Kiến thức liên quan

- Xác định người dùng, phạm vi, mục tiêu và chênh lệch giữa starter với sản phẩm cần xây.
- Chia backlog, ưu tiên, phụ thuộc và ước lượng.
- Git, Pull Request, tự review và tích hợp liên tục (CI).

### 5.2 Việc cần làm

<a id="lr-06"></a>

1. **Lập hồ sơ dự án và backlog.** Ghi người dùng, hành trình chính, phạm vi Tóm tắt/Quiz và phần cần bổ sung vào starter. Mỗi công việc có kết quả cần đạt, tiêu chí chấp nhận, phụ thuộc, ước lượng và cách kiểm. Phân bổ trong 45 giờ tự học; ưu tiên nền xác thực và quyền trước luồng nhiều người dùng.

<a id="lr-07"></a>

2. **Thiết lập quy trình phát triển.** Tạo issue, PR và checklist tự review. Chạy CI trên repository cá nhân gồm test, kiểm quy ước mã nguồn, quét secret và kiểm thư viện phụ thuộc phù hợp stack. Lưu lần chạy thật; phân biệt lỗi pipeline với lỗi ứng dụng.

### 5.3 Gợi ý thực hiện và ứng dụng AI

Dùng Claude phân rã backlog rồi tự kiểm phạm vi và thứ tự. Yêu cầu AI phản biện việc ước lượng quá thấp hoặc bỏ sót phụ thuộc. Lưu ít nhất một điều chỉnh có căn cứ từ starter hoặc kết quả chạy CI.

### 5.4 Rubric đánh giá

| Tiêu chí | Điểm tối đa | Cách chấm điểm |
| --- | --- | --- |
| Phạm vi và phân tích starter | 25 | Người dùng/hành trình rõ: 5; phạm vi đúng: 10; chỉ rõ phần có sẵn và phải xây: 10. |
| Backlog có thể thực hiện | 30 | Công việc gắn yêu cầu/kết quả: 10; ưu tiên và phụ thuộc đúng: 10; ước lượng trong ngân sách thời gian: 10. |
| Git và CI | 30 | Issue/PR và tự review: 10; test/lint thực chạy: 10; kiểm secret/thư viện và xử lý kết quả: 10. |
| Quyết định với AI và bài nộp | 15 | Phản biện được kế hoạch AI: 5; cập nhật kế hoạch theo bằng chứng: 5; hồ sơ có thể kiểm lại: 5. |
| **Tổng** | **100** | |

### 5.5 Cách nộp bài và thời hạn

**Hạn hoàn thiện:** trước buổi 4 ít nhất 12 giờ. Gửi link PR nhánh `milestone/m1` và bản ghi nộp bài, gồm hồ sơ dự án, backlog, link issue và lần chạy CI. Tài liệu có thể gộp trong một file Markdown.

### 5.6 Tài liệu sử dụng

[Phạm vi SRS](../../requirements/SRS_InsightHub_v2.4.md#muc-1); [kiến trúc starter](../../../../Architecture_Starter_v1.md); [hướng dẫn tích hợp](../Integration_Guide_Auth_Notebook.md).

## 6. M2.1 - Đặc tả yêu cầu và xây dựng ca kiểm thử với AI phản biện

### 6.1 Kiến thức liên quan

- Phân tích yêu cầu, tiêu chí chấp nhận, luồng ngoại lệ và yêu cầu phi chức năng.
- Spec-Driven Development: dùng đặc tả làm căn cứ thiết kế, triển khai và kiểm thử.
- Mô tả tình huống theo Given/When/Then và thử nghiệm kỹ thuật để xử lý giả định.

### 6.2 Việc cần làm

<a id="lr-08"></a>

1. **Lập bảng yêu cầu và ca kiểm thử.** Với 151 tiêu chí áp dụng, ghi công việc triển khai, đầu vào, kết quả kỳ vọng và cách kiểm. Bao gồm luồng chính, ca biên, sai quyền, đồng thời và lỗi dịch vụ. Các yêu cầu về thời gian/giao diện phải có môi trường và cách đo. Lấy kết quả kỳ vọng từ yêu cầu và nguồn dữ liệu, không suy từ code hiện có.

<a id="lr-09"></a>

2. **Thử tích hợp trước khi chốt thiết kế.** Chạy thử Google OAuth và email thật theo hướng dẫn Auth; ghi phần thư viện đã hỗ trợ và phần cần bổ sung. Thử cấu hình DeepSeek/embedding, kiểm đầu vào sát giới hạn 60.000 ký tự, số token thực tế, giới hạn ngữ cảnh, thời gian và mức sử dụng. Phân biệt kết quả thật với mô phỏng; ghi rõ dịch vụ bị chặn và người cần hỗ trợ.

### 6.3 Gợi ý thực hiện và ứng dụng AI

Cho Claude tìm mâu thuẫn, thiếu điều kiện và ca biên trong từng nhóm yêu cầu. Tự quyết định kỳ vọng trước khi nhờ AI viết test. Thử nghiệm cấu hình AI ở mốc này phục vụ quyết định thiết kế, không thay bộ đánh giá chất lượng nội dung tại M4.

### 6.4 Rubric đánh giá

| Tiêu chí | Điểm tối đa | Cách chấm điểm |
| --- | --- | --- |
| Độ đầy đủ của yêu cầu | 30 | Đủ tiêu chí áp dụng và phân biệt phần mở rộng: 10; luồng chính/ngoại lệ rõ: 10; liên kết công việc và ước lượng: 10. |
| Ca kiểm thử và căn cứ kỳ vọng | 30 | Đầu vào/kỳ vọng cụ thể: 10; có ca biên/sai quyền/đồng thời: 10; yêu cầu phi chức năng đo được: 10. |
| Thử nghiệm tích hợp | 30 | Google/email có kết quả thật hoặc blocker được chứng minh: 10; kiểm cấu hình AI và giới hạn đầu vào: 10; quyết định thiết kế dựa trên kết quả: 10. |
| Lập luận và hồ sơ | 10 | Chỉ ra một phát hiện từ phản biện với AI: 5; bảng yêu cầu và log có thể kiểm lại: 5. |
| **Tổng** | **100** | |

### 6.5 Cách nộp bài và thời hạn

**Hạn hoàn thiện:** trước buổi 5 ít nhất 12 giờ. Gửi link PR nhánh `milestone/m2.1` và bản ghi nộp bài. Đính kèm bảng yêu cầu/ca kiểm thử, kết quả thử tích hợp, quyết định kỹ thuật và cấu hình mẫu không chứa bí mật. Blocker có minh chứng được ghi nhận về kỹ năng phân tích; không được đánh dấu tích hợp đã đạt khi chưa chạy thật.

### 6.6 Tài liệu sử dụng

[SRS: giới hạn và nghiệp vụ](../../requirements/SRS_InsightHub_v2.4.md#muc-5); [bảng phạm vi từng tiêu chí](02_SRS_Assignment_Map.md); [thử tích hợp Auth/Google/email](04_Auth_Email_Feasibility.md); [cấu hình mô hình](../../../../Model_Profiles_And_Reranking.md).

## 7. M2 - Thiết kế trải nghiệm và kiến trúc giải pháp với AI phản biện

### 7.1 Kiến thức liên quan

- Luồng người dùng, thiết kế trạng thái và khả năng sử dụng trên desktop/mobile.
- Domain-Driven Design ở mức phù hợp: thuật ngữ, thực thể, quyền sở hữu và ranh giới nghiệp vụ.
- API contract, mô hình dữ liệu, migration và hồ sơ quyết định kiến trúc.

### 7.2 Việc cần làm

<a id="lr-10"></a>

1. **Thiết kế Figma.** Hoàn thiện các màn hình UI-01 đến UI-08 trong phạm vi Tóm tắt/Quiz và nối prototype hành trình chính. Thiết kế tại 1440 × 900 và 390 × 844; thể hiện loading, rỗng, lỗi, NoEvidence, hết phiên, xung đột và nguồn bị xóa. Ghi hành vi bàn phím, focus và lỗi trường; cấp quyền xem cho giảng viên.

<a id="lr-11"></a>

2. **Thiết kế API và dữ liệu.** Viết/cập nhật OpenAPI, sơ đồ quan hệ dữ liệu, trạng thái và quy tắc quyền sở hữu. Xác định migration cho dữ liệu cũ, giao dịch, chống gửi lặp và chặn kết quả đến muộn sau xóa. Quiz phải tách dữ liệu trước/sau nộp để không lộ đáp án. Ghi ít nhất một quyết định kiến trúc so sánh hai phương án và căn cứ lựa chọn.

### 7.3 Gợi ý thực hiện và ứng dụng AI

Nhờ Claude đóng vai người dùng và reviewer API để tìm hành trình chưa xử lý. Tự đối chiếu Figma, API và dữ liệu trên cùng một tình huống. Không tự gán toàn bộ dữ liệu cũ cho người đăng nhập đầu tiên; thiết kế chuyển quyền sở hữu bằng thao tác có chủ đích. Review bất đồng bộ một thiết kế của bạn học hoặc mẫu lớp và ghi nhận xét có căn cứ; không phải chờ bạn học để tiếp tục.

### 7.4 Rubric đánh giá

| Tiêu chí | Điểm tối đa | Cách chấm điểm |
| --- | --- | --- |
| Figma và hành trình | 30 | Đủ màn hình/hành trình: 10; trạng thái chính và ngoại lệ: 10; hai kích thước cùng bàn phím/focus: 10. |
| API và mô hình dữ liệu | 30 | API nhất quán với UI: 10; quan hệ/trạng thái dữ liệu rõ: 10; quyền sở hữu và dữ liệu Quiz đúng: 10. |
| Độ an toàn của thiết kế | 25 | Migration có kiểm soát: 10; gửi lặp/đồng thời/kết quả muộn: 10; phương án lỗi và khôi phục: 5. |
| Quyết định và review | 15 | So sánh hai phương án có căn cứ: 5; review mẫu/bài bạn có đối chiếu: 5; link và phiên bản thiết kế kiểm được: 5. |
| **Tổng** | **100** | |

### 7.5 Cách nộp bài và thời hạn

**Hạn hoàn thiện:** trước buổi 6 ít nhất 12 giờ. Gửi link PR nhánh `milestone/m2`, bản ghi nộp bài và link Figma có quyền xem. Trong repo lưu API, sơ đồ dữ liệu, migration dự kiến, quyết định kiến trúc và nhận xét review.

### 7.6 Tài liệu sử dụng

[SRS: dữ liệu](../../requirements/SRS_InsightHub_v2.4.md#muc-8); [SRS: giao diện](../../requirements/SRS_InsightHub_v2.4.md#muc-9); [API starter](../../../../API_Contract_Starter_v1.md); [tích hợp Auth/Notebook](../Integration_Guide_Auth_Notebook.md).

## 8. M3.1 - Phát triển luồng nghiệp vụ xuyên suốt bằng TDD với AI

### 8.1 Kiến thức liên quan

- Tích hợp giao diện, API và cơ sở dữ liệu cho một hành trình hoàn chỉnh.
- Test-Driven Development: viết test thất bại đúng nguyên nhân, triển khai để test đạt, rồi cải thiện cấu trúc.
- Kiểm quyền phía máy chủ và sử dụng mô phỏng đúng ranh giới.

### 8.2 Việc cần làm

<a id="lr-12"></a>

1. **Triển khai hành trình đầu tiên.** Tài khoản A đăng nhập thật, tạo Notebook, tải tài liệu, hỏi đáp, mở đúng nguồn và đọc lại hội thoại. Dữ liệu còn sau tải lại trang và khởi động lại. Khi không chỉ định nguồn, dùng các nguồn Ready mặc định đúng SRS; danh sách nguồn rỗng hoặc không hợp lệ được xử lý đúng, không tự đổi phạm vi. Tài khoản B không đọc được dữ liệu của A qua giao diện hoặc API.

<a id="lr-13"></a>

2. **Thực hiện TDD cho một hành vi có rủi ro.** Viết test cho trường hợp hợp lệ và sai quyền hoặc xung đột; ghi lần test thất bại vì thiếu/sai hành vi, sau đó triển khai và ghi lần đạt. Giữ lịch sử trước/sau, không dựng lại test thất bại sau khi đã viết xong chức năng.

### 8.3 Gợi ý thực hiện và ứng dụng AI

Yêu cầu Claude đề xuất test từ tiêu chí chấp nhận trước khi sửa code. Kiểm rằng test thất bại vì hành vi cần xây, không vì môi trường hỏng. Cho AI thực hiện từng thay đổi nhỏ và review phần truy vấn/quyền; không chỉ kiểm nút trên UI.

### 8.4 Rubric đánh giá

| Tiêu chí | Điểm tối đa | Cách chấm điểm |
| --- | --- | --- |
| Luồng tích hợp thực tế | 35 | Đăng nhập và Notebook: 10; tải tài liệu/hỏi đáp/nguồn: 15; hội thoại bền vững sau restart: 10. |
| Phạm vi và phân quyền | 25 | Nguồn mặc định/tập con/đầu vào sai: 10; chặn tài khoản B qua API: 10; UI xử lý lỗi quyền: 5. |
| TDD có lịch sử | 25 | Test thất bại đúng nguyên nhân: 10; test đạt sau triển khai: 10; có ca sai quyền hoặc xung đột: 5. |
| Tái kiểm và giải thích | 15 | PR/commit/log xác định được: 5; lệnh chạy lại rõ: 5; giải thích quyết định với AI và mô phỏng: 5. |
| **Tổng** | **100** | |

### 8.5 Cách nộp bài và thời hạn

**Hạn hoàn thiện:** trước buổi 7 ít nhất 12 giờ. Gửi link PR nhánh `milestone/m3.1` và bản ghi nộp bài. Nộp code/test/migration, kết quả chạy hành trình A/B và link các commit cùng log thể hiện test thất bại rồi đạt.

### 8.6 Tài liệu sử dụng

[Tích hợp Auth/Notebook](../Integration_Guide_Auth_Notebook.md); [quyết định về nguồn](../../../../adr/ADR-002-Source-Provenance.md); [xử lý gửi lặp](../../../../adr/ADR-003-Operation-Idempotency.md); Figma và API đã thiết kế tại M2.

## 9. M3 - Hoàn thiện sản phẩm và tái cấu trúc an toàn với AI

### 9.1 Kiến thức liên quan

- Triển khai theo đặc tả, quản lý trạng thái, giao dịch, giới hạn và tính nhất quán dữ liệu.
- Kiểm thử ghi nhận hành vi hiện hữu trước thay đổi (characterization testing), refactor và kiểm thử hồi quy.
- Đầu ra AI có cấu trúc, kiểm nguồn và tự động hóa tác vụ phát triển.

### 9.2 Việc cần làm

<a id="lr-14"></a>

1. **Hoàn thiện tài khoản và email.** Đăng ký/xác minh, đăng nhập mật khẩu và Google, liên kết danh tính, hồ sơ, khôi phục/đổi mật khẩu và đăng xuất. Xử lý tài khoản chờ xác minh/chỉ dùng Google, giới hạn thử, tái xác thực và thu hồi phiên theo SRS. Kiểm đủ năm email giao dịch trong danh mục SRS bằng cấu hình thật; không dùng mock để kết luận email đã hoạt động.

<a id="lr-15"></a>

2. **Hoàn thiện Notebook, tài liệu, hội thoại và ghi chú.** Tạo/đọc/sửa/xóa, phân trang, hạn mức, xung đột phiên bản và chọn nguồn đúng quyền. Dữ liệu lưu bền vững. Xóa Notebook ngăn truy cập mọi tài nguyên con; xóa hội thoại không xóa ghi chú đã sao chép. Nguồn đã xóa không được đọc lại qua liên kết hoặc cache dù nội dung lịch sử được giữ theo quy tắc SRS.

<a id="lr-16"></a>

3. **Xây dựng Tóm tắt.** Chọn bản ngắn 150-250 từ hoặc chi tiết 400-600 từ; mặc định ngắn. Nội dung có tổng quan, ý chính gắn nguồn và điểm cần chú ý, phản ánh mâu thuẫn giữa tài liệu. Cho phép sao chép thành ghi chú độc lập.

<a id="lr-17"></a>

4. **Xây dựng Quiz.** Chọn 5 hoặc 10 câu; mặc định 5. Mỗi câu có bốn lựa chọn và đúng một đáp án. Kiểm và chấm điểm tại máy chủ; API không lộ đáp án trước nộp. Từ chối câu/lựa chọn ngoài đề và điểm do client gửi; xử lý câu bỏ trống đúng đặc tả. Lưu các lần làm bài bất biến, mở lại sau restart; nộp lặp cùng lần làm trả kết quả đã lưu.

<a id="lr-18"></a>

5. **Hoàn thiện vòng đời công cụ AI.** Chọn 1-3 nguồn Ready cùng Notebook, kiểm giới hạn 60.000 ký tự, cấu trúc và nguồn trước khi công bố thành công. Có danh sách/lọc/mở/đổi tên/tạo lại/xóa; tạo lại sinh bản mới liên kết bản cũ. Phân biệt thiếu căn cứ, lỗi và hết thời gian; xử lý quota, gửi lặp, đồng thời và kết quả muộn. Xóa kết quả Quiz thì xóa các lần làm gắn với nó; xóa nguồn trong khi xử lý phải chặn công bố. Kiểm giới hạn ở máy chủ tại đúng biên và vượt biên, không cắt dữ liệu ngầm.

<a id="lr-19"></a>

6. **Refactor một module và tự động hóa một tác vụ.** Chọn vấn đề cụ thể trong module hiện hữu; ghi nhận hành vi bằng test trước khi sửa, lập kế hoạch, refactor, kiểm hồi quy và so sánh trước/sau. Chuẩn hóa một tác vụ lặp thành hướng dẫn/skill kết hợp script hoặc hook đã chạy thật. Đây chính là bài Assignment refactor, không tạo dự án khác.

### 9.3 Gợi ý thực hiện và ứng dụng AI

Dùng Claude triển khai theo từng hành vi và review diff nhỏ. Với refactor, yêu cầu chỉ ra vấn đề có bằng chứng trước khi đề xuất thay cấu trúc; đổi tên/format đơn thuần chưa đủ. Script có thể chạy test/lint/checklist trong terminal hoặc CI, không bắt buộc agent tự động. UI cần trạng thái đang xử lý, rỗng, lỗi và khôi phục; ghi khác biệt hợp lý so với Figma.

### 9.4 Rubric đánh giá

| Tiêu chí | Điểm tối đa | Cách chấm điểm |
| --- | --- | --- |
| Tài khoản và dữ liệu nghiệp vụ | 25 | Đủ luồng tài khoản/email: 10; CRUD/hạn mức/phân trang: 10; dữ liệu bền vững và quyền: 5. |
| Tóm tắt và Quiz | 25 | Tóm tắt đúng độ dài/nội dung/nguồn: 10; Quiz đúng cấu trúc và chấm tại server: 10; ghi chú độc lập và lịch sử lần làm: 5. |
| Vòng đời và ngoại lệ | 25 | Trạng thái/quota/giới hạn: 10; gửi lặp/đồng thời/xóa/kết quả muộn: 10; UI và khôi phục: 5. |
| Refactor và tự động hóa | 15 | Có test trước thay đổi và hồi quy: 5; cải thiện có căn cứ: 5; script/skill thực chạy: 5. |
| Chất lượng bài nộp | 10 | Code/test/migration và CI cập nhật: 5; giải thích quyết định và phần chưa hoàn tất: 5. |
| **Tổng** | **100** | |

**Rubric Assignment refactor: 100 điểm, chiếm 25% điểm khóa.** Chấm bốn mức cho từng dòng: 0% nếu chưa có minh chứng; 40% nếu mới làm một phần, chưa đạt mô tả cốt lõi; 70% khi đạt mô tả cốt lõi; 100% khi đạt cả cốt lõi và phần đầy đủ. Điểm mỗi dòng bằng điểm tối đa nhân tỷ lệ tương ứng.

| Tiêu chí | Điểm tối đa | Đạt cốt lõi (70%) | Đầy đủ (100%) |
| --- | --- | --- | --- |
| Bảo toàn hành vi | 30 | Có test trước thay đổi, giữ quy tắc nghiệp vụ; hành vi mới có yêu cầu rõ | Tái chạy trước/sau với ca biên và giải thích tác dụng phụ |
| Kiểm thử theo rủi ro | 30 | Chọn unit/integration/contract/E2E phù hợp module; kỳ vọng độc lập, log đúng phiên bản | Chứng minh test bắt lỗi; xử lý thiếu sót hoặc test không ổn định và kiểm lại |
| Chất lượng refactor | 20 | Thay đổi có mục tiêu, giảm trùng lặp/phụ thuộc hoặc làm rõ ranh giới; CI đạt | So sánh trước/sau chứng minh cải thiện, giải thích đánh đổi và khôi phục |
| Minh chứng và giải thích | 20 | Kế hoạch, diff, test, review và quyết định với AI liên kết được | Truy từ yêu cầu đến test, phản biện được đề xuất AI không phù hợp |
| **Tổng** | **100** | | |

### 9.5 Cách nộp bài và thời hạn

**Hạn chức năng:** trước buổi 8 ít nhất 12 giờ. Gửi link PR nhánh `milestone/m3` và bản ghi nộp bài với code, test, migration, kết quả chạy các luồng và kiểm quyền. **Hạn Assignment refactor:** trước buổi 9 ít nhất 12 giờ; bổ sung kiểm thử ở M4, gửi link PR refactor riêng cùng kết quả trước/sau để giảng viên chấm bài Assignment.

### 9.6 Tài liệu sử dụng

[SRS: yêu cầu chức năng](../../requirements/SRS_InsightHub_v2.4.md#muc-7); [SRS: dữ liệu và giới hạn](../../requirements/SRS_InsightHub_v2.4.md#muc-8); [danh mục email](../../requirements/SRS_InsightHub_v2.4.md#email-catalog); Figma và API của bài làm tại M2.

## 10. M4 - Kiểm thử sản phẩm, đánh giá AI và kiểm tra bảo mật có AI hỗ trợ

### 10.1 Kiến thức liên quan

- Kiểm thử đa tầng, nghiệm thu theo hành trình người dùng, hồi quy và đo yêu cầu phi chức năng.
- Đánh giá nội dung AI dựa trên nguồn và kết quả kỳ vọng xác lập trước.
- Mô hình mối đe dọa, kiểm quyền, secret, thư viện phụ thuộc và an toàn công cụ AI.

### 10.2 Việc cần làm

<a id="lr-20"></a>

1. **Kiểm toàn bộ phạm vi bài tập.** Cập nhật kết quả cho từng tiêu chí áp dụng; thực hiện 21 hành trình nghiệm thu trong SRS theo phạm vi hai tool. Chọn tầng test theo rủi ro, ghi kỳ vọng/thực tế/phiên bản/lỗi; sửa và kiểm lại cả ca lỗi lẫn phần hồi quy liên quan. Ca bị bỏ qua hoặc bị chặn không được tính là đạt.

<a id="lr-21"></a>

2. **Kiểm giao diện và hiệu năng.** Dùng Chrome hoặc Edge có ghi phiên bản, tại 1440 × 900 và 390 × 844. Chọn trước 10 thao tác không AI, ít nhất hai thao tác mỗi nhóm danh sách/chi tiết/tạo/sửa/xóa; từng thao tác tối đa 3 giây. Kiểm thời hạn xử lý tài liệu 120 giây, hỏi đáp 60 giây, công cụ AI 120 giây; ghi môi trường, thời gian và cả lỗi.

<a id="lr-22"></a>

3. **Kiểm phân quyền và vòng đời dữ liệu.** Chuẩn bị hai tài khoản, mỗi tài khoản có Notebook và ba tài liệu TXT/MD/PDF có văn bản; dữ liệu gồm tiếng Việt và tiếng Anh. Với từng loại tài nguyên, thử đổi định danh, đọc API/nguồn/trạng thái/cache, hết phiên, xóa trước/trong/sau xử lý, xung đột phiên bản và gửi lặp. Kết quả đến muộn không được khôi phục dữ liệu đã xóa.

<a id="lr-23"></a>

4. **Đánh giá AI bằng mô hình thật.** Thực hiện đủ bộ lượt trong bảng dưới, lưu tất cả lượt chạy kể cả lỗi. Trước ca có nội dung, viết 3-5 ý kỳ vọng và đoạn nguồn tương ứng. Ghi mã băm nguồn, vị trí trích dẫn, provider/model/embedding, phiên bản prompt/schema, commit, thời gian và mức sử dụng. Tự đối chiếu ý nghĩa và nguồn, không dùng điểm AI tự chấm làm kết luận duy nhất.

<a id="lr-24"></a>

5. **Kiểm bảo mật và sửa lỗi.** Lập mô hình mối đe dọa, quét secret/thư viện và tạo danh mục thành phần phần mềm (SBOM). Kiểm xác thực/liên kết danh tính/phiên, quyền mọi tài nguyên, nội dung Markdown/XSS, prompt injection, tệp tải lên, log và quyền công cụ/MCP. Phân loại phát hiện, sửa và kiểm lại; nếu dùng lỗi cài có chủ đích phải ghi rõ. Review một test hoặc đầu ra AI của bạn học/mẫu lớp với căn cứ yêu cầu.

**Bộ đánh giá AI phải thực hiện:**

| Nhóm | Số lượt/tình huống | Nội dung |
| --- | --- | --- |
| Hỏi đáp | 6 lượt | Ba câu có căn cứ, gồm tiếng Anh và tổng hợp nhiều tài liệu; hai câu thiếu căn cứ; một nguồn có chỉ dẫn gây nhiễu nhưng câu hỏi vẫn trả lời được |
| Tóm tắt | 2 lượt | Một nguồn/bản ngắn; nhiều nguồn/bản chi tiết có thông tin mâu thuẫn |
| Quiz | 2 lượt | Một nguồn/5 câu; nhiều nguồn/10 câu; kiểm câu hỏi, lựa chọn, đáp án, giải thích và nguồn |
| Lặp lại | 2 lượt | Chọn trước một câu hỏi đáp có căn cứ và một ca Tóm tắt hoặc Quiz; đánh giá cả hai lần |
| **Tổng nội dung** | **12 lượt** | Dùng mô hình thật; không tính embedding, lượt bổ sung PDF hoặc chạy lại sau sửa vào số này |
| Ngoại lệ, ngoài 12 lượt | Ba nhóm cho cả hai tool | Thiếu căn cứ, vượt giới hạn đầu vào, đầu ra sai schema; kiểm thêm lỗi provider/timeout bằng mô phỏng có kiểm soát |
| Cách ly, ngoài 12 lượt | Bốn tình huống đại diện | Dữ liệu người khác; nguồn sai Notebook; xóa nguồn khi xử lý; đọc API/link/cache sau mất quyền. Không thay bộ kiểm quyền từng tài nguyên |

Một lượt có nội dung đạt khi đủ ý kỳ vọng, nguồn hợp lệ, không có dữ kiện thiếu căn cứ, đúng cấu trúc/giới hạn/trạng thái/thời hạn. Quiz phải có đúng một đáp án đúng, không mơ hồ. Hai câu thiếu căn cứ phải trả NoEvidence; ca có căn cứ không được trả NoEvidence hoặc Failed. Nếu căn cứ kỳ vọng sai, ghi lý do sửa và phiên bản mới trước khi chạy lại. Không còn lỗi chặn phát hành theo SRS mới kết luận sẵn sàng bàn giao.

### 10.3 Gợi ý thực hiện và ứng dụng AI

Dùng Claude tìm ca biên và phân tích nguyên nhân lỗi; tự xác lập kỳ vọng trước. Không sửa kỳ vọng hoặc bỏ assertion chỉ để test xanh. Có thể dùng mô phỏng thời gian/lỗi provider để kiểm timeout và phiên; chất lượng nội dung phải chạy mô hình thật. Tái dùng dữ liệu và minh chứng giữa các phép kiểm khi phù hợp.

### 10.4 Rubric đánh giá

| Tiêu chí | Điểm tối đa | Cách chấm điểm |
| --- | --- | --- |
| Bao phủ nghiệp vụ và nghiệm thu | 25 | Mỗi tiêu chí có kết quả: 10; hành trình nghiệm thu đủ phạm vi: 10; lỗi được sửa và kiểm lại: 5. |
| Giao diện và hiệu năng | 15 | Hai kích thước và trạng thái UI: 5; đủ 10 thao tác có số đo: 5; kiểm thời hạn tài liệu/chat/tool: 5. |
| Chất lượng AI | 25 | Đủ 12 lượt nội dung và lưu cả lỗi: 10; đối chiếu ý nghĩa/nguồn/Quiz: 10; kiểm ngoại lệ và lượt lặp: 5. |
| Quyền và bảo mật | 25 | Kiểm A/B từng tài nguyên và vòng đời: 10; mô hình đe dọa/scan/SBOM: 5; sửa và kiểm lại: 5; quyền công cụ AI: 5. |
| Hồ sơ có thể tái kiểm | 10 | Môi trường/phiên bản/lệnh/kết quả rõ: 5; review có căn cứ và cập nhật bài refactor: 5. |
| **Tổng** | **100** | |

### 10.5 Cách nộp bài và thời hạn

**Hạn hoàn thiện:** trước buổi 9 ít nhất 12 giờ. Gửi link PR nhánh `milestone/m4` và bản ghi nộp bài, gồm bảng kết quả từng yêu cầu, test/UAT, số đo, nguồn và kết quả đánh giá AI, báo cáo bảo mật/SBOM, lỗi đã sửa và nhận xét review. Đồng thời gửi bản hoàn thiện Assignment refactor của M3.

### 10.6 Tài liệu sử dụng

[SRS: yêu cầu phi chức năng](../../requirements/SRS_InsightHub_v2.4.md#muc-11); [SRS: đánh giá AI](../../requirements/SRS_InsightHub_v2.4.md#muc-12); [SRS: nghiệm thu](../../requirements/SRS_InsightHub_v2.4.md#muc-13); [công cụ đánh giá nền](../../../../../evaluation/README.md).

## 11. M5 - Phát hành, khôi phục và bảo trì sản phẩm với AI hỗ trợ

### 11.1 Kiến thức liên quan

- Đóng gói phiên bản, cài sạch, migration, sao lưu và khôi phục.
- Hướng dẫn vận hành và ghi chú phát hành.
- Phân tích tác động của yêu cầu thay đổi, kiểm hồi quy và phương án quay lại phiên bản trước.

### 11.2 Việc cần làm

<a id="lr-25"></a>

1. **Phát hành bản R1.** Gắn version và Git tag, đóng gói kèm checksum, cấu hình mẫu, hướng dẫn cài/chạy/xử lý lỗi. Thử cài ở môi trường sạch và chạy kiểm tra luồng chính; ghi giới hạn và lỗi còn mở. Không bàn giao secret hoặc dữ liệu riêng.

<a id="lr-26"></a>

2. **Kiểm nâng cấp và khôi phục dữ liệu.** Chạy migration trên dữ liệu đã có; sao lưu và khôi phục sang môi trường cách ly. Kiểm nội dung và quyền của tài khoản, Notebook, tài liệu, hội thoại, ghi chú, kết quả AI và các lần làm Quiz. Không xóa volume để làm giả một lần nâng cấp thành công; không tự chuyển dữ liệu cũ cho tài khoản đầu tiên.

<a id="lr-27"></a>

3. **Thực hiện một thay đổi sau R1.** Chọn yêu cầu thay đổi hoặc lỗi làm thay đổi hành vi thực tế. Ghi tác động đến yêu cầu, UI/API/dữ liệu/test và rủi ro; triển khai thành R1.1, kiểm hồi quy, cập nhật tài liệu/ghi chú phát hành và cách quay lại bản trước.

### 11.3 Gợi ý thực hiện và ứng dụng AI

Cho Claude rà soát runbook như người mới nhận dự án và phân tích tác động của thay đổi. Tự chạy toàn bộ bước cài/restore; AI không được suy đoán kết quả. Với thao tác dữ liệu, xác định môi trường và bản sao lưu trước khi thực hiện.

### 11.4 Rubric đánh giá

| Tiêu chí | Điểm tối đa | Cách chấm điểm |
| --- | --- | --- |
| Bản phát hành tái cài được | 30 | Version/tag/checksum: 10; cài sạch và kiểm luồng chính: 10; hướng dẫn/cấu hình mẫu đầy đủ: 10. |
| Nâng cấp và khôi phục | 30 | Migration trên dữ liệu đã có: 10; restore cách ly thành công: 10; nội dung và quyền sau restore đúng: 10. |
| Thay đổi sau phát hành | 25 | Phân tích tác động: 5; hành vi mới đúng: 10; hồi quy và phương án quay lại: 10. |
| Bàn giao và giải thích | 15 | Ghi chú R1/R1.1 rõ: 5; kết quả thực chạy có phiên bản: 5; giải thích quyết định với AI: 5. |
| **Tổng** | **100** | |

### 11.5 Cách nộp bài và thời hạn

**Hạn hoàn thiện:** trước buổi 10 ít nhất 12 giờ. Gửi link PR nhánh `milestone/m5`, bản ghi nộp bài, link hai tag R1/R1.1 và gói phát hành có checksum. Giữ nguyên tag đã gửi; lần sửa tiếp theo tạo phiên bản mới. Đính kèm kết quả cài sạch/nâng cấp/restore và hồ sơ thay đổi.

### 11.6 Tài liệu sử dụng

[Runbook starter](../../../../Runbook_Starter_v1.md); [SRS: điều kiện phát hành](../../requirements/SRS_InsightHub_v2.4.md#muc-14); [hướng dẫn tích hợp và dữ liệu cũ](../Integration_Guide_Auth_Notebook.md).

## 12. Capstone - Bảo vệ sản phẩm và chứng minh năng lực phát triển phần mềm với AI

### 12.1 Kiến thức liên quan

- Demo theo hành trình người dùng và giải thích quyết định kỹ thuật.
- Truy từ yêu cầu đến thiết kế, mã nguồn, test và phiên bản phát hành.
- Đánh giá hiệu quả ứng dụng AI bằng chất lượng, thời gian và rủi ro.

### 12.2 Việc cần làm

<a id="lr-28"></a>

1. **Demo và bảo vệ cá nhân.** Chạy bản đã nộp: đăng nhập, Notebook, tài liệu, hỏi đáp có nguồn, ghi chú, Tóm tắt, Quiz và một tình huống lỗi/quyền. Giải thích một yêu cầu xuyên qua thiết kế/code/test, refactor đã làm, kết quả đánh giá AI và cách khôi phục dữ liệu. Thực hiện hoặc phân tích chính xác thay đổi nhỏ giảng viên đưa; chỉ rõ phần AI hỗ trợ và quyết định của bản thân.

<a id="lr-29"></a>

2. **Lập kế hoạch áp dụng AI trong 30 ngày.** Chọn một quy trình công việc thực tế, ghi hiện trạng, chỉ số đo, mục tiêu, các mốc ngày 7/14/30 và rủi ro. Nêu cách thu dữ liệu, điều kiện tiếp tục hoặc dừng. Đây là bản kế hoạch cần nộp, không yêu cầu làm thêm 30 ngày để hoàn thành khóa.

### 12.3 Gợi ý thực hiện và ứng dụng AI

Dùng Claude đóng vai reviewer để luyện phản biện và tìm điểm chưa có minh chứng. Học viên tự demo, giải thích và quyết định; không đọc lại câu trả lời AI để thay vấn đáp. Chuẩn bị dữ liệu mẫu và đường dẫn mở nhanh trong repository.

### 12.4 Rubric đánh giá

**Rubric Capstone: 100 điểm, chiếm 35% điểm khóa.** Mỗi tiêu chí nhận 0% khi không có minh chứng hoặc vi phạm nghiêm trọng hành vi cần đánh giá; 40% khi mới làm một phần, chưa đạt mô tả cốt lõi; 70% khi đạt đầy đủ cột cốt lõi; 100% khi đạt thêm cột đầy đủ. Điểm bằng điểm tối đa nhân tỷ lệ, cộng các dòng rồi chia 10 để có điểm Capstone trên thang 10. Ví dụ: tiêu chí tối đa 10 điểm đạt cốt lõi nhận 7 điểm.

| Tiêu chí | Điểm tối đa | Đạt cốt lõi (70%) | Đầy đủ (100%) |
| --- | --- | --- | --- |
| Phạm vi và kế hoạch | 5 | Mục tiêu, phạm vi và backlog nhất quán với phần cần bổ sung vào starter; PR đã tự review, CI đúng phiên bản; trách nhiệm với AI rõ | Ưu tiên và phụ thuộc hợp lý; kế hoạch cập nhật theo kết quả thực tế; giải thích được cách xử lý phát hiện review |
| Đặc tả và truy vết yêu cầu | 10 | Tiêu chí chấp nhận có luồng chính/ngoại lệ; yêu cầu phi chức năng có cách đo; công việc, ước lượng và ca kiểm liên kết được; thử tích hợp ghi rõ phần đã/chưa kiểm | Truy từ yêu cầu đến test và từ test về yêu cầu; xử lý giả định quan trọng; cập nhật bảng truy vết sau thay đổi |
| Thiết kế UI/API/dữ liệu | 10 | Figma, API, dữ liệu và quyền sở hữu nhất quán; quyết định kiến trúc có phương án và căn cứ; có thiết kế migration và trạng thái lỗi | Triển khai khớp thiết kế hoặc giải thích khác biệt; kiểm hai kích thước/bàn phím; liên kết quyết định thiết kế với yêu cầu và test |
| Chức năng và TDD | 12 | Tài khoản, Notebook, hỏi đáp, ghi chú, Tóm tắt và Quiz chạy qua UI/API/cơ sở dữ liệu; tiêu chí bắt buộc đạt; có test thất bại trước sửa rồi đạt sau sửa; xử lý trạng thái và lỗi | Tái chạy được bản nộp; mọi tiêu chí áp dụng có minh chứng; giải thích ranh giới mô phỏng; dữ liệu còn sau restart, thao tác lặp đúng |
| Refactor và tự động hóa | 8 | Có test ghi nhận hành vi module trước thay đổi; diff đúng phạm vi, hồi quy giữ quy tắc nghiệp vụ; tác vụ tự động thực chạy và giới hạn rõ | So sánh trước/sau chứng minh cải thiện; chạy lại từ checkpoint hoặc khôi phục; mọi thay đổi hành vi có căn cứ yêu cầu |
| Kiểm thử và nghiệm thu | 8 | Chọn tầng test theo yêu cầu/rủi ro; nghiệm thu có kỳ vọng và thực tế; lỗi quan trọng được kiểm lại; điều kiện đo rõ | Người khác chạy lại được; phân tích thiếu sót và test không ổn định; chứng minh test bắt lỗi và truy vết đầy đủ trên bản nộp |
| Chất lượng nội dung AI | 7 | Đủ 12 lượt nội dung cho hỏi đáp/Tóm tắt/Quiz; đối chiếu ý và nguồn; ghi mô hình, dữ liệu, phiên bản và cả lượt lỗi; thiếu căn cứ/chỉ dẫn gây nhiễu/ngoại lệ được xử lý đúng | Tái lập cấu hình và nguồn; đánh giá cả lượt lặp; giải thích sai lệch, kết luận và kiểm lại; không dùng AI tự chấm làm căn cứ duy nhất |
| Bảo mật ứng dụng | 10 | Có mô hình đe dọa, quét và danh mục thành phần; kiểm hai tài khoản trên từng tài nguyên; kiểm phiên/nội dung độc hại, sửa và kiểm lại; không còn lỗi chặn phát hành | Tái hiện ca từ chối qua API/nguồn/cache, sau xóa và hết phiên; đánh giá tác động có căn cứ và chứng minh lỗi không tái phát |
| An toàn quy trình AI | 5 | Giới hạn quyền công cụ/MCP, dữ liệu và secret; thử một tình huống bị chặn; có người kiểm và log đã lọc | Tái hiện dừng/khôi phục từ checkpoint; giải thích cách xử lý chỉ dẫn độc hại và chỉ cấp quyền cần cho tác vụ |
| Phát hành và khôi phục | 5 | Có version/tag/checksum; cài sạch, kiểm luồng chính, nâng cấp và restore cách ly dữ liệu đầy đủ; hướng dẫn sử dụng/xử lý lỗi rõ | Người khác tái cài được theo hướng dẫn; kiểm nội dung và quyền sau restore; giải thích giới hạn và cách quay lại bản trước |
| Thay đổi sau phát hành | 5 | Có thay đổi sau R1, phân tích tác động đến yêu cầu/thiết kế/dữ liệu/test; bản cập nhật, ghi chú phát hành và hồi quy đúng phạm vi | Tái hiện trước/sau; giải thích rủi ro và cách quay lại; cập nhật truy vết, không gây hồi quy hoặc mất dữ liệu |
| Demo và vấn đáp | 10 | Tự demo chức năng và ngoại lệ; truy một yêu cầu qua code/test; giải thích quyết định/refactor; thực hiện hoặc phân tích đúng một thay đổi nhỏ | Xử lý được tình huống biến đổi giảng viên đưa; chẩn đoán từ minh chứng, bảo vệ lựa chọn và chỉ rõ giới hạn |
| Kế hoạch áp dụng 30 ngày | 5 | Chọn một quy trình công việc, có số liệu hiện trạng/chỉ số đo, trách nhiệm cá nhân, mốc ngày 7/14/30 và rủi ro | Kế hoạch khả thi; cách thu dữ liệu và điều kiện tiếp tục/dừng rõ, dựa trên bài học trong dự án |
| **Tổng** | **100** | | |

Điểm nhóm giữ cơ cấu chương trình: yêu cầu/kế hoạch 15; thiết kế 10; triển khai và tự động hóa 20; kiểm thử/chất lượng AI 15; bảo mật 15; phát hành/bảo trì 10; vấn đáp/kế hoạch áp dụng 15. Không lấy điểm Assignment thay cho đánh giá refactor trong bản sản phẩm cuối. Lỗi lộ dữ liệu chéo, chiếm quyền hoặc mất dữ liệu nghiêm trọng chưa sửa khiến tiêu chí bảo mật tương ứng nhận 0 và sản phẩm chưa đủ điều kiện bàn giao.

### 12.5 Cách nộp bài và thời hạn

**Hạn hồ sơ:** trước buổi 10 ít nhất 12 giờ. Gửi link PR `milestone/capstone`, bản ghi nộp bài, tag phát hành đã kiểm, link Figma, hướng dẫn demo, bảng kết quả yêu cầu/test/AI/bảo mật và kế hoạch 30 ngày. **Hạn sửa sau bảo vệ:** trong 24 giờ sau khi buổi 10 kết thúc; gửi link cập nhật và danh sách phản hồi đã xử lý. Nếu sửa code, kiểm lại và tạo tag phát hành mới, giữ bản đã bảo vệ.

### 12.6 Tài liệu sử dụng

[SRS: tiêu chí nghiệm thu](../../requirements/SRS_InsightHub_v2.4.md#muc-13); [SRS: bàn giao](../../requirements/SRS_InsightHub_v2.4.md#muc-14); Figma, API, runbook và hồ sơ đã xây dựng trong dự án.
