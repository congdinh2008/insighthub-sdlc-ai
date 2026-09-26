# Requirements - Dự án cá nhân InsightHub

B2B C07 - SDLC with AI | Phiên bản 1.0 | Revision hướng dẫn 26/09/2026
Học trực tuyến, thực hiện cá nhân | 10 buổi, 25 giờ trên lớp và 45 giờ tự học

Tài liệu xác định các chức năng InsightHub học viên phải xây, cách áp dụng SDLC và AI vào 29 công việc, cùng kết quả cần đạt qua 10 buổi. Phạm vi, thiết kế và tích hợp, rubric, cách nộp bài và mẫu evidence được trình bày trong cùng tài liệu. Học viên bắt đầu tại mục 1-2, thực hiện milestone tương ứng và tra các mục chuyên đề ngay trong tài liệu.

**Mục lục**

| Nội dung | Vị trí |
| --- | --- |
| Chín nhóm chức năng bắt buộc và trách nhiệm | [1. Phạm vi sản phẩm](#san-pham) |
| Khởi động, lộ trình, cách nộp và điểm số | [2. Hướng dẫn thực hiện](#bat-dau) |
| Chức năng và cách kiểm từng milestone | [Ma trận tiến độ sản phẩm](#ma-tran-chuc-nang), [đầu vào và cách đo](#do-ket-qua-milestone) |
| Buổi 1-2 | [M0.1](#m01), [M0.2](#m02) |
| Buổi 3-5 | [M1](#m1), [M2.1](#m21), [M2](#m2) |
| Buổi 6-7 | [M3.1](#m31), [M3](#m3) |
| Buổi 8-10 | [M4](#m4), [M5](#m5), [Capstone](#capstone) |
| Thiết kế dữ liệu, schema, API và tích hợp | [13. Data và API](#data-api) |
| Auth, Google và email | [14. Thử tích hợp và kiểm chứng](#auth-email) |
| Phạm vi áp dụng và bảng truy vết 163 AC | [15. Phạm vi và truy vết](#pham-vi-truy-vet) |
| Bảng kết quả và mẫu evidence | [16. Hồ sơ kiểm chứng](#evidence) |
| Thuật ngữ và ví dụ test case | [17. Glossary](#glossary) |

**Tệp đính kèm để tra cứu**

- [SRS InsightHub v1.0](02_SRS_InsightHub_v1.0.md): hành vi sản phẩm và tiêu chí chấp nhận chi tiết. Tra theo mã yêu cầu khi phân tích, thiết kế hoặc kiểm thử.
- [API và Schema Reference](03_API_Schema_Reference_v1.0.zip): gói kỹ thuật chứa OpenAPI, JSON Schema, ví dụ và công cụ kiểm cấu trúc. Chỉ mở khi cần sử dụng các tệp kỹ thuật ở M2 trở đi. Các quy tắc học viên cần biết và cách áp dụng được trình bày tại mục 13; gói này không tạo thêm bài nộp.

<a id="san-pham"></a>

## 1. Sản phẩm cần hoàn thiện

Mỗi học viên xây dựng sản phẩm InsightHub hoàn chỉnh trong phạm vi bài tập từ Starter do giảng viên cung cấp. Người dùng có thể đăng nhập, quản lý Notebook và tài liệu, hỏi đáp có nguồn, lưu hội thoại và ghi chú, tạo bản Tóm tắt và làm Quiz từ tài liệu.

### 1.1. Chức năng bắt buộc của sản phẩm bài tập

Học viên hoàn thiện mỗi nhóm chức năng qua các phần UI, API và dữ liệu liên quan theo SRS, sử dụng thư viện và phần nền được cung cấp. Các nhóm là cách tổ chức đề bài, không bắt buộc tách thành service, module hoặc màn hình quản trị riêng.

| Nhóm chức năng | Người dùng phải làm được gì trong bản hoàn thiện | Trách nhiệm của học viên | Yêu cầu và công việc liên quan |
| --- | --- | --- | --- |
| **Auth và Account** | Đăng ký, xác minh email, đăng nhập bằng mật khẩu và Google, liên kết danh tính, khôi phục/đổi mật khẩu, quản lý profile, session và logout. | Xây nghiệp vụ tài khoản và tích hợp thư viện hoặc dịch vụ Auth; kiểm quyền tại server. Starter chưa có chức năng này. | IH-AUTH-001 đến IH-AUTH-010; [LR-09](#lr-09), [LR-12](#lr-12), [LR-14](#lr-14). |
| **Transactional Email** | Nhận email xác minh, reset mật khẩu, thông báo liên kết Google, hướng dẫn tài khoản chỉ dùng Google và thông báo đổi/reset mật khẩu. | Tạo đúng sự kiện EML-001 đến EML-005, nội dung, link và trạng thái gửi; kiểm thư nhận thật và lỗi chuyển giao. | IH-MSG-003; [LR-09](#lr-09), [LR-14](#lr-14), [danh mục email](#auth-email). |
| **Notebook** | Tạo, xem danh sách, mở, đổi tên/mô tả và xóa Notebook thuộc quyền; nhận thông báo khi vượt giới hạn hoặc có version conflict. | Xây UI/API/data cho Notebook, ownership, pagination, giới hạn và quy tắc xóa tài nguyên con. | IH-NB-001 đến IH-NB-004; [LR-12](#lr-12), [LR-15](#lr-15). |
| **Document** | Upload TXT, Markdown và PDF có văn bản; xem trạng thái, retry khi lỗi, mở nội dung/citation và xóa tài liệu. | Tái sử dụng ingestion, extraction và index của Starter; tích hợp Notebook, quyền, hạn mức, chống trùng, trạng thái và vòng đời. | IH-DOC-001 đến IH-DOC-006; [LR-12](#lr-12), [LR-15](#lr-15). |
| **Chat và Conversation** | Hỏi đáp theo nguồn, mở citation, phân biệt thiếu căn cứ với lỗi; tạo, xem, đổi tên và xóa conversation; đọc lại lịch sử. | Tích hợp RAG nền với quyền và phạm vi nguồn; xây persistence và quản lý conversation độc lập với operation TTL. | IH-CHAT-001 đến IH-CHAT-005; [LR-12](#lr-12), [LR-15](#lr-15). |
| **Note** | Tạo, mở, sửa, xóa Note; lưu câu trả lời hoặc Summary hợp lệ thành bản sao độc lập. | Xây UI/API/data, validation, version conflict và provenance; bảo toàn Note theo quy tắc xóa của SRS. | IH-NOTE-001, IH-NOTE-002, IH-SUM-002; [LR-15](#lr-15), [LR-16](#lr-16). |
| **Summary (Tóm tắt)** | Chọn nguồn và độ dài, tạo Summary có căn cứ, xem nguồn, mở lại và lưu thành Note. | Xây cấu hình, prompt/schema/parser, UI, persistence và kiểm chất lượng nội dung trên kết nối model đã có. | IH-SUM-001, IH-SUM-002; [LR-16](#lr-16). |
| **Quiz** | Tạo đề, chọn câu trả lời, nộp bài, xem điểm/giải thích, mở lại lần đã nộp và làm lại. | Xây schema công khai/nội bộ, UI và chấm tại server; bảo vệ đáp án, lưu QuizAttempt, xử lý nộp lặp. | IH-QUIZ-001, IH-QUIZ-002, IH-DATA-002; [LR-17](#lr-17). |
| **AI Job và Output** | Theo dõi tác vụ, xem/lọc kết quả, đổi tên, regenerate và xóa kết quả thuộc quyền. | Tích hợp trạng thái, schema validation, citation, shared quota, idempotency, deadline và xử lý nguồn bị xóa cho Chat, Summary, Quiz. | IH-AI-001 đến IH-AI-004, IH-OUT-001 đến IH-OUT-003, IH-INT-004; [LR-18](#lr-18). |

### 1.2. Yêu cầu áp dụng xuyên các chức năng

- **UI/UX:** thiết kế và triển khai theo Figma trong phạm vi bài tập; có trạng thái loading, empty, success, error, hết session và conflict, cùng thao tác bàn phím theo SRS.
- **Quyền và dữ liệu:** server xác định người dùng từ session, kiểm ownership của đúng đối tượng trước mọi thao tác; dữ liệu còn sau reload/restart theo vòng đời quy định. Không dùng `owner_id` do client gửi để cấp quyền.
- **Chất lượng và tích hợp:** validation, API contract, lỗi an toàn, giới hạn xử lý và cấu hình provider phải nhất quán giữa UI, API và dữ liệu. Kết quả fixture, tích hợp thật và đánh giá nội dung AI được ghi riêng.
- **Bàn giao:** bản R1 của bài tập có test, CI, migration, hướng dẫn cài/chạy, backup/restore và một thay đổi sau phát hành thành R1.1. Học viên thực hiện trên local hoặc sandbox.

Starter cung cấp Next.js, FastAPI, PostgreSQL/pgvector, Docker Compose, ingestion, embedding/index, RAG cơ bản, dữ liệu mẫu và công cụ kiểm. Học viên kiểm lại các phần này sau khi tích hợp; kết quả của Starter không tự xác nhận phần mở rộng đã đạt.

[SRS InsightHub v1.0](02_SRS_InsightHub_v1.0.md) là đặc tả hành vi sản phẩm. Bài tập áp dụng **151 tiêu chí chấp nhận** cho phạm vi trên; [bảng phạm vi](#pham-vi-truy-vet) chỉ rõ 12 tiêu chí ngoài phạm vi bắt buộc. Mindmap, Slide và Báo cáo không bắt buộc. Không yêu cầu triển khai hạ tầng cloud cho vận hành thực tế hoặc Kubernetes.

Phần [thiết kế dữ liệu và API](#data-api) xác định đầu ra cần thực hiện và cách tích hợp Starter. Tra [glossary](#glossary) để phân biệt các thuật ngữ như test case, test scenario, schema và migration.

### 1.3. Công cụ, dữ liệu và trách nhiệm

**Công cụ phát triển:** công ty cấp tài khoản Claude cho học viên; Claude là công cụ AI chính của khóa học. ChatGPT là phương án bổ sung, chỉ sử dụng nếu học viên có tài khoản và muốn dùng; không bắt buộc có hoặc mua tài khoản ChatGPT. Học viên tự phân tích, kiểm chứng và giải thích quyết định, dù sử dụng công cụ nào. Quyền dùng Claude Code, MCP và kết nối repository được kiểm tra theo tài khoản thực tế; nếu chưa có quyền phù hợp, thực hành agent trên sandbox do lớp cung cấp.

**Dịch vụ AI của sản phẩm:** InsightHub dùng DeepSeek để sinh nội dung và Gemini để tạo embedding theo cấu hình Starter; reranker tắt. Các dịch vụ này khác tài khoản AI dùng hỗ trợ phát triển.

**Cách học:** trước buổi học, đọc tài liệu và thực hiện các việc của milestone trong khả năng hiện tại; ghi phần đã làm và câu hỏi cần hỗ trợ. Trên lớp, trao đổi các điểm khó của dự án gắn với nội dung buổi học. Sau buổi học, cập nhật bài theo phản hồi và hoàn thiện trước hạn. Tổng 45 giờ tự học đã bao gồm đọc, thực hành, kiểm thử, sửa bài và chuẩn bị bảo vệ.

**Cách làm với AI:** tự xác định yêu cầu và kết quả kỳ vọng, cung cấp ngữ cảnh, yêu cầu AI đề xuất kế hoạch, thực hiện từng thay đổi nhỏ rồi tự kiểm tra. Lưu một vài quyết định tiêu biểu đã giữ, sửa hoặc bác bỏ đề xuất AI và lý do; không cần nộp toàn bộ hội thoại. Không đưa bí mật xác thực, tệp `.env` thật hoặc dữ liệu công ty chưa được phép vào Git hay công cụ AI.

<a id="bat-dau"></a>

## 2. Lộ trình, cách nộp bài và cách tính điểm

### 2.1. Lộ trình và thời hạn

| Buổi | Milestone | Kết quả chính | Tự học | Hạn hoàn thiện |
| --- | --- | --- | --- | --- |
| 1 | M0.1 | Starter chạy upload, hỏi đáp và citation; một phân tích yêu cầu bằng AI đã được kiểm | 3 giờ | Trước buổi 2 ít nhất 12 giờ |
| 2 | M0.2 | Agent workflow trên InsightHub có giới hạn quyền, xử lý lỗi và chạy lại được | 4 giờ | Trước buổi 3 ít nhất 12 giờ |
| 3 | M1 | Backlog chín nhóm chức năng, dependency, kế hoạch cá nhân và Git/CI | 4 giờ | Trước buổi 4 ít nhất 12 giờ |
| 4 | M2.1 | Yêu cầu và test case theo chức năng; kết quả spike Google, email và AI | 5 giờ | Trước buổi 5 ít nhất 12 giờ |
| 5 | M2 | Figma, API, schema và ADR cho các chức năng bài tập | 4 giờ | Trước buổi 6 ít nhất 12 giờ |
| 6 | M3.1 | Đăng nhập → Notebook → upload → hỏi đáp → citation → mở lại conversation | 5 giờ | Trước buổi 7 ít nhất 12 giờ |
| 7 | M3 | Đủ Auth, năm email, Notebook/Document/Conversation/Note, Summary, Quiz và AI Output; refactor | 6 giờ | Chức năng: trước buổi 8 ít nhất 12 giờ; bài refactor: trước buổi 9 ít nhất 12 giờ |
| 8 | M4 | Kết quả kiểm từng chức năng, quyền, AI và lỗi đã sửa | 6 giờ | Trước buổi 9 ít nhất 12 giờ |
| 9 | M5 | R1 cài được, dữ liệu khôi phục được và thay đổi R1.1 có regression test | 4 giờ | Trước buổi 10 ít nhất 12 giờ |
| 10 | Capstone | Demo sản phẩm hoàn chỉnh, truy vết quyết định và kế hoạch áp dụng 30 ngày | 4 giờ | Hồ sơ trước buổi 10 ít nhất 12 giờ; sửa theo review trong 24 giờ sau khi kết thúc buổi 10 |

Bản chuẩn bị của buổi 1-9 gửi trước giờ bắt đầu buổi học ít nhất 2 giờ. Đây là tiến độ thực tế để nhận hỗ trợ, chưa yêu cầu hoàn tất cả milestone. Ngày, giờ cụ thể và kênh nộp bài do giảng viên công bố theo lịch lớp, múi giờ Việt Nam (UTC+07:00); không suy ra ngày học từ ngày trên tài liệu.

<a id="ma-tran-chuc-nang"></a>

#### 2.1.1. Chức năng cần đạt qua từng milestone

M1 lập backlog cho tất cả nhóm; M2.1 phân tích yêu cầu và spike rủi ro; M2 hoàn thiện thiết kế. M3.1 triển khai hành trình đầu tiên, M3 hoàn thiện phạm vi chức năng, M4 tổng hợp kiểm chứng và sửa lỗi, M5 kiểm bản phát hành. Công việc phát triển và test được tích lũy giữa các buổi theo ngân sách tự học.

| Nhóm | Chuẩn bị tại M2.1 và M2 | Phần phải chạy tại M3.1 | Phần phải hoàn thiện tại M3 | Kết quả tại M4 và M5 |
| --- | --- | --- | --- | --- |
| Auth và Account | Phân tích các Auth flow, thử Google, linking và session; thiết kế UI/API/data. | Một Auth flow hợp lệ của SRS tạo session thực cho hai tài khoản A/B. | Cả mật khẩu và Google, linking, profile, recovery, đổi mật khẩu, session và logout. | Kiểm đủ nhánh, rate limit, session và lỗi; kiểm đăng nhập/quyền sau cài mới và restore. |
| Transactional Email | Thử gửi/nhận thật; xác định trigger, nội dung, link và trạng thái của năm email. | Nếu chọn email/mật khẩu để đăng nhập, phải có EML-001 và xác minh hợp lệ. Nếu chọn Google, chưa yêu cầu tích hợp đủ email vào sản phẩm ở mốc này. | Tích hợp đủ EML-001 đến EML-005 với đúng Auth flow. | Có thư nhận thật, kết quả hành động và kiểm lỗi gửi; cấu hình bàn giao không chứa secret. |
| Notebook | Đặc tả thao tác, quyền, giới hạn; thiết kế trang danh sách và workspace. | Tạo, liệt kê và mở Notebook đúng owner trong hành trình đầu tiên. | Hoàn thiện cập nhật, pagination, giới hạn, version conflict và xóa cùng tài nguyên con. | Test quyền A/B, thao tác và vòng đời; kiểm dữ liệu/quyền sau restore. |
| Document | Đối chiếu ingestion có sẵn, định dạng và trạng thái; thiết kế tích hợp Notebook. | Upload tài liệu hợp lệ vào đúng Notebook, xử lý `Ready`, đọc nội dung và mở citation. | Đủ định dạng, lỗi, retry, chống trùng, hạn mức, xóa và ảnh hưởng tới nguồn. | Test đầu vào hợp lệ/lỗi, quyền, deadline và xóa khi đang xử lý; kiểm dữ liệu/index sau restore. |
| Chat và Conversation | Đặc tả nguồn, citation, trạng thái và persistence; thiết kế API/lịch sử. | Hỏi đáp có nguồn, lưu lượt và mở lại conversation sau reload/restart; chặn tài khoản B. | Quản lý danh sách, đổi tên, xóa; `NoEvidence`, retry và quy tắc nguồn/lịch sử đầy đủ. | Kiểm UAT, nguồn bị xóa, idempotency và chất lượng câu trả lời; kiểm lịch sử sau restore. |
| Note | Thiết kế nội dung, version và liên kết xuất xứ. | Chưa yêu cầu Note hoạt động trong hành trình đầu tiên. | Tạo, đọc, sửa, xóa; lưu câu trả lời/Summary thành bản sao độc lập. | Kiểm conflict, quyền và quan hệ sau xóa; kiểm nội dung sau restore. |
| Summary | Xác định input, output schema, nội dung kỳ vọng và giao diện. | Thiết kế đã có; chưa yêu cầu Summary chạy ở mốc này. | Tạo Summary ngắn/chi tiết, citation, xem lại và lưu Note. | Kiểm schema, độ dài, từng claim và nguồn; giữ kết quả hợp lệ qua phát hành/restore. |
| Quiz | Thiết kế đề, nội dung công khai/nội bộ, QuizAttempt và cách chấm. | Thiết kế đã có; chưa yêu cầu Quiz chạy ở mốc này. | Sinh đề, làm/nộp/chấm, xem kết quả, nộp lặp và làm lại. | Kiểm không lộ đáp án, nội dung câu hỏi và chấm điểm; giữ lịch sử sau restart/restore. |
| AI Job và Output | Thiết kế trạng thái, shared quota, idempotency, deadline và schema version. | Tích hợp cơ chế áp dụng cho luồng Chat của hành trình đầu tiên. | Hoàn thiện cho Summary/Quiz, danh sách, lọc, rename, regenerate và delete. | Kiểm concurrency, restart, ba thứ tự xóa/công bố và phản hồi muộn; kiểm bản phát hành. |

Mỗi ô là mức hoàn thành được yêu cầu, không phải kết quả đã đạt. Nếu một AC có nhiều nhánh, phần kiểm tại M3.1 chỉ ghi kết quả nhánh đã chạy; chỉ kết luận AC đạt khi toàn bộ điều kiện áp dụng đều đạt. Checklist chức năng dẫn tới cùng [bảng truy vết](#bang-ket-qua), không tạo bảng kết luận thứ hai.

#### 2.1.2. Cách sử dụng yêu cầu theo milestone

Mỗi milestone được trình bày theo sáu phần: kết quả InsightHub cần đạt; chức năng và công việc cần thực hiện; điều kiện hoàn thành; cách áp dụng SDLC và AI; evidence/cách nộp; rubric. M0-M2 tạo kết quả khởi động, phân tích, thử khả thi và thiết kế; các mốc này chưa yêu cầu toàn bộ chức năng hoạt động. Từ M3.1, các chức năng được triển khai phải có kết quả chạy và test trên phiên bản xác định.

Bắt đầu từ checklist chức năng, tự xác định hành vi và test case, rồi dùng AI hỗ trợ phần công việc cụ thể. Các điều kiện hoàn thành giúp tự rà soát tiến độ; cách tính điểm và điều kiện hoàn thành khóa học vẫn theo mục 2.4-2.8. Khi thiếu quyền dịch vụ hoặc phát sinh chênh lệch thời gian, ghi rõ phần bị ảnh hưởng và bước xử lý, không tự bỏ chức năng hoặc tính thêm giờ ngoài ngân sách.

<a id="do-ket-qua-milestone"></a>

#### 2.1.3. Đầu vào, output và cách đo từng milestone

Dùng bảng dưới để tự kiểm và ghi kết quả trong cùng bản nộp ở mục 2.3; chi tiết hành vi và rubric nằm tại milestone tương ứng. Không tạo thêm bài nộp hoặc điểm số. Ghi rõ phiên bản đã kiểm, input, expected, actual và link evidence; phần chưa làm hoặc bị chặn không được ghi đạt.

| Milestone | Đầu vào cần có | Output quan sát được và cách kiểm |
| --- | --- | --- |
| M0.1 / LR-01..03 | Fork đúng Starter, môi trường fixture và yêu cầu hiện hành. | Upload, Chat và mở đúng citation; JSON qua validator và đối chiếu ý nghĩa với nguồn; một lỗi AI có căn cứ, bản sửa và kiểm lại. Ghi giới hạn fixture, không kết luận chất lượng model thật. |
| M0.2 / LR-04..05 | Repo chạy được; sandbox/tool và quyền thực hành do lớp xác nhận. | Workflow thực chạy, có success, lỗi công cụ và thao tác vượt quyền bị môi trường từ chối; làm lại được theo hướng dẫn. Lưu event/response thật, không chỉ lời AI. |
| M1 / LR-06..07 | Baseline M0 và phạm vi chín nhóm chức năng. | Backlog nối LR/AC và dependency; commit/PR/review; kết quả kiểm chất lượng đúng SHA theo LR-07. Mở artifact/log để xác nhận phép kiểm thực chạy. |
| M2.1 / LR-08..09 | Backlog, SRS và quyền Google/email/AI trước spike. | Một bảng 163 AC phân biệt 151 áp dụng/12 ngoài phạm vi, có input/expected; spike có actual và quyết định giải pháp. Không coi spike là hoàn thiện toàn Auth. |
| M2 / LR-10..11 | Kết quả spike, UI/UX nguồn đã chốt và hợp đồng tham khảo. | Handoff nối flow-state-AC-API-data, hai viewport/keyboard, schema và ADR; giảng viên mở được thiết kế. Xác định module nền cần characterization trước khi sửa. |
| M3.1 / LR-12..13 | Thiết kế lát cắt; characterization của module nền trước lần sửa đầu. | Auth-Notebook-Document-Chat/citation và mở lại conversation; API chặn tài khoản B truy dữ liệu A, persistence qua restart, quy tắc operation áp dụng cho Chat. TDD có red đúng nguyên nhân, green và regression. Phạm vi Auth theo mục 2.1.1, chưa yêu cầu đủ năm email ở đây. |
| M3 / LR-14..19 | Lát cắt M3.1 và thiết kế phần dùng chung cho hai tool. | Chín nhóm chức năng hoạt động, full Auth/năm email, Summary/Quiz, Output và lifecycle; test UI/API/data theo nhánh. Refactor có baseline/diff/regression, hoàn thiện ASG01 trước B9 theo hạn nguồn. |
| M4 / LR-20..24 | Test/evidence tích lũy cùng feature, corpus/oracle hai tool. | Tổng hợp kết quả AC đến hạn, mapping 21 UAT, 12 lượt nội dung AI cùng ngoại lệ, UI/performance/security và retest. AC phát hành ở M5 ghi chưa kiểm/chưa đến hạn, không ghi Pass sớm. |
| M5 / LR-25..27 | Candidate đã kiểm và dữ liệu nghiệp vụ bài làm. | R1 cài được, populated restore giữ dữ liệu/quyền A-B; CR thực hiện sau R1 thành R1.1 có regression. Cập nhật AC M5 và các kết quả chịu ảnh hưởng, không lấy restore của Starter thay phần mở rộng. |
| Capstone / LR-28..29 | Tag phát hành, source và evidence thống nhất. | Demo đúng phiên bản, truy một yêu cầu qua SDLC, giải thích quyết định kỹ thuật/AI và kế hoạch áp dụng 30 ngày. Kế hoạch này không giao thêm 30 ngày triển khai bắt buộc. |

Phân biệt ba kết quả: output milestone đạt/chưa đạt; verdict từng AC theo mục 16.1; điểm phản hồi theo rubric. M0-M2 có thể hoàn thành output phân tích/thiết kế trong khi AC runtime chưa kiểm. Không lấy điểm rubric thay verdict AC hoặc dùng một nhánh đã đạt để kết luận toàn bộ AC đạt.

### 2.2. Khởi động và trách nhiệm

1. Kiểm tra tài khoản Claude do công ty cấp và quyền truy cập repository Starter, Google, email và dịch vụ AI theo hướng dẫn lớp. Ghi phần chưa được cấp quyền để giảng viên hỗ trợ.
2. Fork và clone Starter theo mục 2.3; ghi commit xuất phát rồi chạy chế độ fixture theo [GETTING_STARTED](../../GETTING_STARTED.md).
3. Thử tải tài liệu, hỏi đáp và mở nguồn; ghi kết quả hoặc lỗi. Fixture hỗ trợ kiểm hành vi phần mềm, chưa chứng minh chất lượng nội dung của model thật.
4. Đọc milestone đang thực hiện, lập bảng truy vết theo mục 15 và bổ sung kết quả dần theo mẫu tại mục 16. Không viết lại toàn bộ SRS hoặc tạo hồ sơ riêng cho từng mẫu.
5. Giữ test và evidence cùng thay đổi code. Trước khi tích hợp phần phụ thuộc, thực hiện thử khả thi tại mục 14 và ghi quyết định thiết kế tại mục 13.

Giảng viên cung cấp Starter, dữ liệu mẫu, hướng dẫn và môi trường hoặc quyền thực hành cần thiết. Học viên tự hoàn thiện toàn bộ project và chịu trách nhiệm về kết quả. Peer review giúp phản biện; nếu chưa có bài phù hợp của bạn học, dùng mẫu giảng viên cung cấp để tiếp tục.

### 2.3. Repository cá nhân và quy trình nộp bài

**Fork** là tạo một repository thuộc tài khoản của học viên từ repository starter, giữ lại mã nguồn và lịch sử ban đầu. Học viên làm bài và lưu thay đổi trong repository của mình. Giảng viên đọc bài qua đường dẫn được gửi.

1. Mở đường dẫn starter giảng viên cấp, chọn **Fork** và chọn tài khoản cá nhân hoặc tổ chức được lớp chỉ định. Cấp quyền xem cho giảng viên nếu repository là private. Clone repository vừa tạo về máy theo [hướng dẫn khởi động](../../GETTING_STARTED.md).
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
Output milestone: <đạt/chưa đạt, phạm vi đến hạn và lý do>
Đã kiểm tra: <lệnh hoặc bước chạy, kỳ vọng, thực tế, link log>
Quyết định với AI: <đề xuất đã giữ/sửa/bác bỏ và lý do>
Còn thiếu hoặc cần hỗ trợ:
```

Lấy link commit từ mục Commits của PR. Kiểm tra đúng phiên bản đó; nếu sửa mã nguồn sau khi kiểm, chạy lại phần bị ảnh hưởng và cập nhật link. Giữ log đã lọc thông tin nhạy cảm, ghi rõ chạy mô phỏng hay dịch vụ thật. Không cần lập một tài liệu riêng cho từng loại minh chứng.

<a id="danh-gia"></a>

### 2.4. Cách đọc rubric

Mỗi milestone có **rubric 100 điểm để phản hồi tiến độ**. Cột cách chấm chia điểm thành các phần cụ thể: có kết quả và minh chứng đúng thì nhận điểm phần đó; phần chưa làm, chưa đúng hoặc chưa kiểm được nhận 0. Các điểm này không tạo thêm thành phần điểm khóa.

Tài liệu kiến thức (KC) và hướng dẫn công cụ (TG) theo từng buổi được giảng viên cấp qua kênh học liệu lớp. Các liên kết ở từng milestone trỏ tới đặc tả, hướng dẫn thiết kế và tài liệu kỹ thuật cần dùng. Dùng [mẫu minh chứng tích lũy](#evidence) trong hồ sơ hiện có, không lập lại thông tin ở nhiều bảng. Chọn module dự kiến refactor và giữ kiểm thử trước lần sửa đầu tại M3.1; buổi 8 tổng hợp kiểm chứng đã tích lũy và bổ sung phần còn thiếu. Bản thiết kế Figma do học viên tạo tại M2 và dùng tiếp cho triển khai, kiểm thử.

### 2.5. Cơ cấu điểm khóa

| Thành phần | Trọng số | Cách xác định |
| --- | --- | --- |
| Quiz | 10% | Trung bình 10 quiz theo syllabus; tự làm, không dùng AI. Quiz buổi 8 chia chất lượng/bảo mật 50/50 |
| Chuẩn bị trước buổi học | 15% | Trung bình 10 bản chuẩn bị; chấm theo tiến độ và nội dung của buổi tương ứng |
| Assignment refactor | 25% | Bài refactor một module trong dự án; giao buổi 7, nộp trước buổi 9 ít nhất 12 giờ. Rubric 30/30/20/20 tại M3 |
| Capstone | 35% | Chấm toàn sản phẩm và bảo vệ cá nhân theo rubric tại Capstone |
| Chuyên cần và review | 15% | Tham dự và hai lần review bất đồng bộ tại M2/M4 |

Quy tất cả điểm thành phần về thang 10. Điểm khóa bằng `0,10 × Quiz + 0,15 × Chuẩn bị + 0,25 × Assignment + 0,35 × Capstone + 0,15 × Chuyên cần/review`.

Điều kiện hoàn thành: tổng điểm và Capstone từ 6/10, không thành phần nguồn nào bằng 0, tham dự ít nhất 8/10 buổi. Rubric tiến độ M0.1-M5 dùng phản hồi, không cộng thêm vào công thức. Assignment và phần refactor trong Capstone được chấm theo phiên bản/phạm vi riêng, không sao chép điểm.

### 2.6. Bài chuẩn bị trước buổi học

Mỗi tiêu chí tối đa 25 điểm. Chọn mức cao nhất đáp ứng đầy đủ mô tả; nhân điểm tối đa với 0/40/70/100%, cộng bốn dòng rồi chia 10. Điểm chuẩn bị của khóa là trung bình 10 buổi.

| Tiêu chí | Chưa có (0%) | Một phần (40%) | Đạt cốt lõi (70%) | Đầy đủ (100%) |
| --- | --- | --- | --- | --- |
| Phần tự thực hiện và câu hỏi | Chưa có bài | Chưa xác định phần đã tự làm | Có kết quả tự học/thực hành phù hợp buổi và phần cần hỗ trợ | Kết quả mở được, xác định rõ phụ thuộc và cách đã thử xử lý |
| Tính đúng | Không kiểm được nội dung | Có lỗi cơ bản chưa nhận diện | Phần đã thực hiện đúng với tài liệu và phạm vi chuẩn bị | Kiểm thêm tình huống biên liên quan và sửa sai có căn cứ |
| Giải thích cách làm và sử dụng AI | Chỉ chép đầu ra | Có kết luận thiếu lý do | Nêu cách tự phân tích, phần AI hỗ trợ và quyết định | So sánh giả định/phương án, nêu giới hạn và câu hỏi cụ thể |
| Minh chứng | Không có căn cứ | Chỉ khẳng định hoặc ảnh thiếu ngữ cảnh | Có đầu vào, kỳ vọng và kết quả thực tế phù hợp nhiệm vụ | Người khác kiểm lại được, đúng phiên bản và rõ phần chưa kiểm |

Bài chuẩn bị không cần hoàn tất sản phẩm cuối milestone. Buổi 1 chưa bắt có CI hoặc Auth; khó khăn về quyền truy cập cần được ghi để giảng viên hỗ trợ. Mốc chuẩn bị buổi 1-9: trước giờ học ít nhất 2 giờ; hồ sơ Capstone: trước buổi 10 ít nhất 12 giờ.

### 2.7. Chuyên cần và review

Phân bổ trong đề bài: tham dự chiếm 10 điểm phần trăm toàn khóa, chất lượng hai review chiếm 5 điểm phần trăm. Giữ tổng 15% đã quy định trong chương trình.

- Điểm tham dự trên thang 10 bằng số buổi tham dự hợp lệ, tối đa 10; điều kiện hoàn thành vẫn là ít nhất 8 buổi.
- Mỗi review chấm 0/4/7/10: không nộp / nhận xét chung / nhận xét gắn yêu cầu và minh chứng, có đề xuất kiểm / nhận xét đã được đối chiếu, giải thích tác động và có kết quả theo dõi.
- Điểm review bằng trung bình hai lần. Điểm chuyên cần/review bằng `(2 × điểm tham dự + điểm review) / 3`.
- Không buộc tìm lỗi nếu sản phẩm đúng; xác nhận có phép kiểm và căn cứ vẫn được ghi nhận. Nếu chưa có bài bạn học, dùng mẫu tương đương do giảng viên cấp; không phụ thuộc tiến độ người khác.

### 2.8. Nguyên tắc phản hồi

- Ghi tên tiêu chí, điểm, căn cứ và việc cần sửa. Không chấm bằng số commit, số dòng code, số prompt hoặc số công cụ AI.
- Điểm học tập, mức năng lực đã chứng minh và trạng thái sản phẩm là ba kết quả riêng. Điểm đạt không biến tiêu chí sản phẩm chưa kiểm thành đạt.
- Lỗi chặn phát hành phải sửa và kiểm lại trước khi kết luận bàn giao. Dịch vụ hoặc quyền hoặc thông tin truy cập dịch vụ của lớp bị chặn được ghi rõ để hỗ trợ; dịch vụ mô phỏng không thay kết quả tích hợp thật.
- Thời điểm nhận bài dựa trên kênh nộp của lớp. Không tự đặt mức trừ điểm mới vì nộp muộn; áp dụng chính sách lớp đã công bố và giữ lịch sử phản hồi.

<a id="m01"></a>

## 3. M0.1 - Chạy Starter và phân tích một yêu cầu InsightHub bằng AI

### 3.1 Kết quả InsightHub cần đạt

Starter chạy được hành trình upload tài liệu → hỏi đáp → mở citation trong chế độ fixture. Học viên xác định được phần nền đã có và kiểm chứng một đầu ra phân tích yêu cầu do AI tạo; chưa phải triển khai Auth, Notebook hoặc AI Tools ở mốc này.

### 3.2 Chức năng và công việc cần thực hiện

<a id="lr-01"></a>

1. **Khởi động starter.** Fork, clone, ghi link commit nền và chạy chế độ fixture. Thử tải một tệp hợp lệ và một tệp lỗi, hỏi đáp và mở nguồn. Ghi lệnh, kết quả và lỗi gặp phải; giải thích vì sao fixture chưa chứng minh chất lượng AI thật.

<a id="lr-02"></a>

2. **Tạo đầu ra có cấu trúc.** Chọn một tiêu chí chấp nhận trong SRS, tự xác định điều kiện ban đầu, hành vi và kết quả kỳ vọng. Cung cấp cho Claude phần SRS cùng ngữ cảnh cần thiết, loại thông tin nhạy cảm và phần không liên quan; ghi lý do lựa chọn. Yêu cầu đầu ra JSON gồm tình huống thành công và lỗi. Kiểm bằng schema, sau đó đối chiếu từng nội dung với yêu cầu gốc. JSON hợp lệ chưa chứng minh phân tích đúng.

<a id="lr-03"></a>

3. **Phát hiện và sửa một lỗi AI.** Dùng một đề xuất sai thực tế hoặc lỗi có chủ đích do lớp cung cấp. Chỉ ra sai ở đâu bằng tài liệu, mã nguồn hoặc phép thử độc lập; sửa và kiểm lại. Ghi rõ nếu dùng lỗi có chủ đích.

### 3.3 Điều kiện hoàn thành

- Tệp hợp lệ được xử lý và dùng để hỏi đáp; tệp lỗi có kết quả được ghi nhận, không bị coi là thành công.
- Một AC của InsightHub được chuyển thành tình huống thành công/lỗi, có JSON hợp lệ và nội dung đúng với SRS.
- Một lỗi AI được chỉ ra bằng căn cứ độc lập, sửa và kiểm lại; học viên giải thích được giới hạn của fixture.

### 3.4 Áp dụng SDLC và AI

**Kiến thức áp dụng:**

- Cách mô hình ngôn ngữ xử lý ngữ cảnh và vì sao đầu ra có thể sai.
- Viết prompt có mục tiêu, dữ liệu đầu vào và yêu cầu đầu ra; JSON và kiểm tra schema.
- Cấu trúc Web, API, cơ sở dữ liệu; luồng tải tài liệu, truy xuất, trả lời có nguồn.

| Bước áp dụng | Công việc trên InsightHub | Kết quả cần kiểm |
| --- | --- | --- |
| Khảo sát hệ thống | Chạy luồng tài liệu và hỏi đáp; xác định Web, API, DB và provider tham gia ở đâu. | Log và kết quả trên đúng commit Starter. |
| Phân tích yêu cầu | Tự đọc một AC, sau đó dùng Claude đề xuất tình huống và JSON. | Điều kiện ban đầu, hành động, kỳ vọng khớp AC. |
| Kiểm chứng | Kiểm schema và đối chiếu nội dung, sửa một đề xuất AI sai. | Phân biệt lỗi cấu trúc với lỗi hiểu nghiệp vụ. |

Đưa cho Claude một yêu cầu cụ thể và các trường đầu ra cần có. Yêu cầu giải thích giả định; không coi JSON đúng định dạng là nội dung đúng. Khi AI đề xuất sửa setup, kiểm nguyên nhân từ log trước khi chạy lệnh.

**Tài liệu dùng cho milestone:** [Khởi động starter](../../GETTING_STARTED.md); [kiến trúc ứng dụng](../Architecture_Starter_v1.md); [tài liệu mẫu](../../sample-docs/README.md).

### 3.5 Evidence, cách nộp bài và thời hạn

**Hạn hoàn thiện:** trước buổi 2 ít nhất 12 giờ. Push nhánh `milestone/m0.1`, mở PR vào `main` của repository cá nhân và gửi link PR kèm bản ghi nộp bài cho giảng viên. Bài gồm kết quả setup, prompt, JSON và schema, trường hợp AI sai và kết quả kiểm lại.

Dùng cùng tài liệu mẫu cho demo Starter và phân tích nếu phù hợp. Evidence phải cho thấy input, kết quả upload/hỏi đáp/citation và phép kiểm độc lập; ảnh ứng dụng mở được chưa đủ.

### 3.6 Rubric đánh giá

| Tiêu chí | Điểm tối đa | Cách chấm điểm |
| --- | --- | --- |
| Môi trường và thao tác nền | 30 | Khởi động được ứng dụng: 10; tải tệp hợp lệ và hỏi đáp có nguồn: 10; nhận diện đúng tệp lỗi: 10. |
| Prompt và đầu ra JSON | 25 | Prompt đủ mục tiêu và ngữ cảnh: 5; kiểm schema: 10; đối chiếu đầy đủ nội dung với yêu cầu gốc: 10. |
| Kiểm chứng và sửa lỗi AI | 30 | Tái hiện lỗi: 10; căn cứ độc lập: 10; sửa và kiểm lại đúng: 10. |
| Bài nộp và giải thích | 15 | Commit và PR truy cập được: 5; kết quả kiểm có phiên bản: 5; giải thích được giới hạn của fixture: 5. |
| **Tổng** | **100** | |

Đối chiếu tiêu chí môi trường với hành trình Document - Chat; tiêu chí prompt/JSON với AC đã chọn. Không tính đầu ra phân tích yêu cầu thành chức năng đã triển khai.

<a id="m02"></a>

## 4. M0.2 - Xây workflow AI Agent cho một tác vụ InsightHub

### 4.1 Kết quả InsightHub cần đạt

Có một workflow agent thực chạy trên repository InsightHub, được giới hạn quyền, xử lý được lỗi công cụ và chạy lại được từ hướng dẫn. Workflow phục vụ một công việc của project, chẳng hạn đối chiếu API upload với test hiện có; mốc này chưa yêu cầu thêm chức năng sản phẩm.

Trước buổi 2, giảng viên xác nhận công cụ/sandbox, repository thử, thư mục/lệnh và dữ liệu được phép; học viên kiểm truy cập rồi thiết kế workflow. Có thể dùng tool tích hợp hoặc MCP theo quyền được cấp, không bắt buộc cài mọi công cụ. Nếu thiếu quyền, ghi lỗi và đề nghị môi trường lớp; tiếp tục chuẩn bị quy tắc/task brief, chưa kết luận workflow đạt. Dùng thao tác vô hại và dữ liệu giả để kiểm từ chối.

### 4.2 Chức năng và công việc cần thực hiện

<a id="lr-04"></a>

1. **Viết quy tắc dùng AI cho dự án.** Xác định dữ liệu được sử dụng, thư mục và lệnh được phép, người quyết định, cách dừng và khôi phục. Thử một thao tác ngoài quyền bằng dữ liệu giả trong môi trường thực hành được cấp. Minh chứng phải cho thấy công cụ hoặc môi trường đã từ chối thao tác; câu trả lời “không được phép” của mô hình chưa chứng minh giới hạn quyền được thực thi.

<a id="lr-05"></a>

2. **Thực hành một quy trình agent có dùng công cụ hoặc MCP.** Chọn công việc nhỏ như đọc API và chạy một nhóm kiểm thử. Ghi mục tiêu, phạm vi, kế hoạch, checkpoint và kết quả kỳ vọng trước khi chạy trên công cụ được cấp hoặc môi trường lớp. Lưu thao tác thực tế cùng kết quả; thử một lỗi công cụ và xử lý hoặc dừng đúng. Đóng gói quy trình đã kiểm thành hướng dẫn hoặc skill có thể chạy lại.

### 4.3 Điều kiện hoàn thành

- Hướng dẫn AI xác định đúng repository, dữ liệu, quyền, checkpoint và cách dừng/khôi phục.
- Workflow tạo ra kết quả có thể đối chiếu với mục tiêu đã ghi trước, qua thao tác công cụ hoặc MCP thực tế.
- Có kết quả thử lỗi công cụ và một thao tác vượt quyền bị môi trường từ chối; không dùng lời từ chối của AI thay kiểm soát thực tế.
- Chạy lại được workflow đã chuẩn hóa bằng hướng dẫn hoặc skill.

### 4.4 Áp dụng SDLC và AI

**Kiến thức áp dụng:**

- Vòng làm việc của agent: lập kế hoạch, dùng công cụ, quan sát kết quả, điều chỉnh.
- MCP, giới hạn quyền, ngữ cảnh không tin cậy và điểm khôi phục.
- Hướng dẫn dự án cho AI và chuẩn hóa một tác vụ lặp.

| Bước áp dụng | Công việc trên InsightHub | Kết quả cần kiểm |
| --- | --- | --- |
| Xác định tác vụ | Chọn một việc có input/output rõ, trong API, test hoặc tài liệu của project. | Mục tiêu và phạm vi đủ nhỏ để kiểm độc lập. |
| Thiết kế workflow | Dùng Claude đề xuất bước và công cụ; học viên xác định quyền và checkpoint. | Mỗi quyền gắn với một thao tác cần thiết. |
| Chạy và cải tiến | Thực chạy, thử lỗi/vượt quyền, đối chiếu kết quả và sửa hướng dẫn. | Workflow lặp lại được, không phụ thuộc suy đoán của AI. |

Để Claude đề xuất kế hoạch trước khi cấp quyền chạy. Bắt đầu bằng quyền đọc và lệnh kiểm tra cụ thể; chỉ mở quyền sửa khi tác vụ cần. Chuẩn hóa thao tác đã chạy thành hướng dẫn tái sử dụng, tránh viết quy tắc chung không gắn với dự án.

**Tài liệu dùng cho milestone:** [Kiến trúc và ranh giới hệ thống](../Architecture_Starter_v1.md); [API để chọn tác vụ thực hành](../API_Contract_Starter_v1.md).

### 4.5 Evidence, cách nộp bài và thời hạn

**Hạn hoàn thiện:** trước buổi 3 ít nhất 12 giờ. Gửi link PR của nhánh `milestone/m0.2` trong repository cá nhân và bản ghi nộp bài. Đính kèm quy tắc AI, hướng dẫn hoặc skill, log thực hành và kết quả kiểm giới hạn quyền.

Giữ đường dẫn input, kết quả tác vụ và log đã lọc secret trong cùng hồ sơ. Ghi rõ phần nào chạy bằng công cụ thực, phần nào dùng dữ liệu giả để kiểm lỗi.

### 4.6 Rubric đánh giá

| Tiêu chí | Điểm tối đa | Cách chấm điểm |
| --- | --- | --- |
| Hướng dẫn dự án và quyền | 25 | Quy tắc gắn đúng repository: 10; dữ liệu và quyền rõ: 10; có cách dừng và khôi phục: 5. |
| Quy trình agent thực chạy | 30 | Kế hoạch rõ: 10; thao tác công cụ hoặc MCP có log: 10; đối chiếu kết quả với mục tiêu: 10. |
| Xử lý lỗi và giới hạn | 25 | Thử yêu cầu vượt phạm vi: 10; nhận diện và xử lý lỗi công cụ: 10; khôi phục từ checkpoint: 5. |
| Tái sử dụng và nộp bài | 20 | Hướng dẫn hoặc skill chạy lại được: 10; PR và minh chứng đủ để giải thích: 10. |
| **Tổng** | **100** | |

Rubric đánh giá workflow giải quyết công việc cụ thể trong InsightHub, cùng kết quả thực thi và kiểm quyền; một bộ quy tắc AI chung chưa chứng minh workflow đã hoạt động.

<a id="m1"></a>

## 5. M1 - Lập backlog chức năng InsightHub và thiết lập Git/CI

### 5.1 Kết quả InsightHub cần đạt

Có kế hoạch cá nhân cho đầy đủ chín nhóm chức năng tại mục 1.1, chỉ rõ phần Starter cung cấp, phần phải xây và phụ thuộc giữa các phần. Repository cá nhân có issue, Pull Request, tự review và CI thực chạy. Đầu vào là kết quả khảo sát Starter và workflow của M0.

### 5.2 Chức năng và công việc cần thực hiện

<a id="lr-06"></a>

1. **Lập hồ sơ dự án và backlog.** Ghi người dùng, hành trình chính và phần cần bổ sung vào Starter cho cả chín nhóm chức năng tại mục 1.1. Phạm vi AI Tools bắt buộc là Summary và Quiz; Auth, Email, Notebook, Document, Chat/Conversation, Note và AI Job/Output vẫn thuộc bài tập. Chia công việc theo kết quả chức năng rồi gắn các bước phân tích, thiết kế, code, test và release tương ứng. Mỗi công việc có kết quả cần đạt, tiêu chí chấp nhận, phụ thuộc, ước lượng và cách kiểm. Đối chiếu ước lượng với ngân sách 45 giờ tự học, bao gồm đọc tài liệu, phát triển, kiểm thử, sửa lỗi và chuẩn bị bảo vệ. Ghi phần vượt ngân sách và căn cứ để trao đổi với giảng viên; không giảm ước lượng hoặc bỏ tiêu chí để làm kế hoạch có vẻ vừa thời gian. Ưu tiên xác thực và quyền trước luồng nhiều người dùng.

<a id="lr-07"></a>

2. **Thiết lập quy trình phát triển.** Tạo issue, Pull Request và danh sách tự rà soát theo bốn góc: tính đúng, bảo mật, quy ước mã nguồn và thiết kế. Chạy Continuous Integration (CI) trên repository cá nhân, gồm kiểm thử, lint, bí mật và thư viện phụ thuộc cho cả Web và API theo công nghệ thực tế. Lưu liên kết lần chạy và đúng commit được kiểm; phân biệt lỗi quy trình CI với lỗi ứng dụng. Không yêu cầu tìm đủ một lỗi cho mỗi góc rà soát.

### 5.3 Điều kiện hoàn thành

- Backlog bao phủ Auth, Email, Notebook, Document, Chat/Conversation, Note, Summary, Quiz và AI Job/Output; có công việc UI, dữ liệu, test và release liên quan.
- Mỗi công việc có AC liên quan, kết quả, dependency, ước lượng và cách kiểm; phân biệt phần cần chạy tại M3.1 với phần hoàn thiện tại M3.
- Kế hoạch đối chiếu đủ 45 giờ tự học, ghi chênh lệch và căn cứ; không bỏ yêu cầu để làm vừa thời gian.
- CI chạy trên đúng commit, có kết quả kiểm Web/API và xử lý phát hiện phù hợp.

### 5.4 Áp dụng SDLC và AI

**Kiến thức áp dụng:**

- Xác định người dùng, phạm vi, mục tiêu và chênh lệch giữa starter với sản phẩm cần xây.
- Chia backlog, ưu tiên, phụ thuộc và ước lượng.
- Git, Pull Request, tự review và Continuous Integration (CI).

| Bước áp dụng | Công việc trên InsightHub | Kết quả cần kiểm |
| --- | --- | --- |
| Phân rã phạm vi | Dùng Claude đề xuất backlog từ chín nhóm chức năng; học viên đối chiếu SRS và Starter. | Không bỏ Auth/Email hoặc nhầm phần nền với phần bài làm đã hoàn thành. |
| Xếp dependency | Lập chuỗi Auth/session → ownership → Notebook → Document/Chat → Note/Summary/Quiz → release. | Mỗi công việc có đầu vào sẵn sàng trước khi triển khai. |
| Thiết lập kiểm soát thay đổi | Tạo issue/PR, tự review và chạy CI; điều chỉnh kế hoạch theo kết quả. | Yêu cầu, thay đổi và lần kiểm cùng truy được về commit. |

Dùng Claude phân rã backlog rồi tự kiểm phạm vi và thứ tự. Yêu cầu AI phản biện việc ước lượng quá thấp hoặc bỏ sót phụ thuộc. Lưu ít nhất một điều chỉnh có căn cứ từ starter hoặc kết quả chạy CI.

**Tài liệu dùng cho milestone:** [Phạm vi SRS](02_SRS_InsightHub_v1.0.md#sec-1-2); [kiến trúc starter](../Architecture_Starter_v1.md); [hướng dẫn tích hợp](#data-api).

### 5.5 Evidence, cách nộp bài và thời hạn

**Hạn hoàn thiện:** trước buổi 4 ít nhất 12 giờ. Gửi link PR nhánh `milestone/m1` và bản ghi nộp bài, gồm hồ sơ dự án, backlog, link issue và lần chạy CI. Tài liệu có thể gộp trong một file Markdown.

Trong backlog hiện có, dùng trường nhóm chức năng và milestone để thể hiện tiến độ; không cần tạo thêm báo cáo kế hoạch riêng. Chỉ rõ một điều chỉnh do học viên quyết định sau khi phản biện đề xuất AI.

### 5.6 Rubric đánh giá

| Tiêu chí | Điểm tối đa | Cách chấm điểm |
| --- | --- | --- |
| Phạm vi và phân tích starter | 25 | Người dùng và hành trình rõ: 5; phạm vi đúng: 10; chỉ rõ phần có sẵn và phải xây: 10. |
| Backlog có thể thực hiện | 30 | Công việc gắn yêu cầu và kết quả: 10; ưu tiên và phụ thuộc đúng: 10; ước lượng có căn cứ, đối chiếu ngân sách và nhận diện chênh lệch: 10. |
| Git và CI | 30 | Issue, Pull Request và tự review: 10; kiểm thử và lint thực chạy: 10; quét bí mật, kiểm thư viện và xử lý kết quả: 10. |
| Quyết định với AI và bài nộp | 15 | Phản biện được kế hoạch do AI đề xuất: 5; cập nhật kế hoạch theo bằng chứng: 5; hồ sơ có thể kiểm lại: 5. |
| **Tổng** | **100** | |

Tiêu chí phạm vi và backlog được đối chiếu theo chín nhóm chức năng, dependency và ngân sách thực tế; số lượng issue hoặc số trang kế hoạch không thay tính đầy đủ.

<a id="m21"></a>

## 6. M2.1 - Làm rõ nghiệp vụ và thử tích hợp Auth, Email, AI

### 6.1 Kết quả InsightHub cần đạt

Có yêu cầu, test case và kỳ vọng cho từng nhóm chức năng, cùng kết quả spike các phụ thuộc có rủi ro: Google Auth, transactional email, account linking/session và cấu hình AI. Đầu vào là backlog M1; kết quả dùng để quyết định thiết kế tại M2, chưa thay nghiệm thu chức năng.

### 6.2 Chức năng và công việc cần thực hiện

<a id="lr-08"></a>

1. **Lập bảng truy vết yêu cầu và test case.** Dùng danh mục 163 tiêu chí trong bảng phạm vi để quản lý 151 tiêu chí áp dụng và 12 tiêu chí ngoài bài tập. Ghi phiên bản SRS, mã yêu cầu thành phần nếu có, điều kiện hoặc nhánh cần kiểm, công việc triển khai, đầu vào và kết quả kỳ vọng. Chọn 1-2 yêu cầu có rủi ro để phân tích sâu, sau đó rà đủ phần còn lại; không viết lại toàn bộ SRS. Bao phủ luồng chính, edge case, sai quyền, đồng thời và lỗi dịch vụ. Yêu cầu về thời gian và giao diện phải có môi trường, cách đo. Dùng một bảng xuyên khóa theo [mẫu kết quả](#bang-ket-qua); chỉ kết luận một AC đạt khi mọi điều kiện áp dụng của AC đó đạt.

<a id="lr-09"></a>

2. **Thử tích hợp trước khi chốt thiết kế.** Tại M2.1, thử các khả năng có thể làm thay đổi lựa chọn giải pháp: đăng nhập Google với tài khoản thử, gửi và nhận email thật, liên kết tài khoản trùng email, xử lý tài khoản chờ xác minh và thu hồi phiên. Ghi phần thư viện đã hỗ trợ, phần phải bổ sung và phụ thuộc cần giảng viên xử lý theo [hướng dẫn thử khả thi](#auth-email). Thử cấu hình DeepSeek và embedding với đầu vào sát giới hạn 60.000 ký tự; ghi số token thực tế, giới hạn ngữ cảnh, thời gian và mức sử dụng. Phân biệt kết quả thật với mô phỏng. Hoàn thiện chức năng tại M3 và kiểm đầy đủ tại M4; kết quả thử sớm không thay nghiệm thu.

### 6.3 Điều kiện hoàn thành

- Một bảng truy vết chứa đủ 163 AC, phân biệt 151 AC áp dụng và 12 AC ngoài phạm vi; các nhánh có input và expected result.
- Làm rõ quyền, trạng thái và lỗi theo từng chức năng; không chỉ liệt kê mã AC hoặc ghi chung “CRUD”.
- Spike Google/email/AI có cấu hình, kết quả và giới hạn kiểm; phần bị chặn có evidence và bước xử lý, không được ghi Pass.
- Các giả định còn mở được nối tới thiết kế hoặc công việc cần xử lý trước khi triển khai phần phụ thuộc.

### 6.4 Áp dụng SDLC và AI

**Kiến thức áp dụng:**

- Phân tích yêu cầu, tiêu chí chấp nhận, luồng ngoại lệ và yêu cầu phi chức năng.
- Spec-Driven Development: dùng đặc tả làm căn cứ thiết kế, triển khai và kiểm thử.
- Mô tả tình huống theo Given/When/Then và thử nghiệm kỹ thuật để xử lý giả định.

| Nhóm cần phân tích | Câu hỏi phải trả lời trước thiết kế |
| --- | --- |
| Auth và Email | Khi nào tài khoản được Active? Khi nào phải xác minh hoặc tái xác thực? Email nào phát sinh? Lỗi gửi ảnh hưởng thế nào tới giao dịch đã hoàn tất? |
| Notebook và Document | Ai được truy cập? Upload nào hợp lệ, trùng hoặc cần retry? Xóa Notebook/nguồn ảnh hưởng dữ liệu nào? |
| Conversation và Note | Lịch sử và bản sao được giữ đến khi nào? Xóa conversation có làm mất Note không? |
| Summary, Quiz và AI Output | Input, schema, nguồn, quota, deadline và idempotency là gì? Khi nào được trả đáp án hoặc công bố kết quả? |

Học viên tự xác lập expected result từ SRS, dùng Claude tìm thiếu sót và viết nháp test case, rồi kiểm lại từng đề xuất. Dùng kết quả spike để lựa chọn giải pháp; lưu quyết định giữ, sửa hoặc bác bỏ đề xuất AI cùng căn cứ.

Cho Claude tìm mâu thuẫn, thiếu điều kiện và edge case trong từng nhóm yêu cầu. Tự quyết định kỳ vọng trước khi nhờ AI viết test. Thử nghiệm cấu hình AI ở mốc này phục vụ quyết định thiết kế, không thay bộ đánh giá chất lượng nội dung tại M4.

**Tài liệu dùng cho milestone:** [SRS: giới hạn và nghiệp vụ](02_SRS_InsightHub_v1.0.md#sec-3-2); [bảng phạm vi từng tiêu chí](#pham-vi-truy-vet); [thử tích hợp xác thực, Google và email](#auth-email); [cấu hình mô hình](../Model_Profiles_And_Reranking.md).

### 6.5 Evidence, cách nộp bài và thời hạn

**Hạn hoàn thiện:** trước buổi 5 ít nhất 12 giờ. Gửi link PR nhánh `milestone/m2.1` và bản ghi nộp bài. Đính kèm bảng yêu cầu và test case, kết quả thử tích hợp, quyết định kỹ thuật và cấu hình mẫu không chứa bí mật. Phụ thuộc bị chặn có minh chứng được ghi nhận về kỹ năng phân tích; không được đánh dấu tích hợp đã đạt khi chưa chạy thật.

Các phân tích theo nhóm bổ sung vào cùng bảng truy vết và hồ sơ spike. Đánh dấu rõ test case đã thiết kế, đã chạy, chưa chạy hoặc bị chặn; chưa có sản phẩm hoàn chỉnh ở M2.1 không đồng nghĩa mọi test case đã được thực thi.

### 6.6 Rubric đánh giá

| Tiêu chí | Điểm tối đa | Cách chấm điểm |
| --- | --- | --- |
| Độ đầy đủ của yêu cầu | 30 | Đủ tiêu chí áp dụng và phân biệt phần mở rộng: 10; luồng chính và ngoại lệ rõ: 10; liên kết công việc và ước lượng: 10. |
| Test case và căn cứ kỳ vọng | 30 | Đầu vào và kỳ vọng cụ thể: 10; có edge case, sai quyền và xử lý đồng thời: 10; yêu cầu phi chức năng đo được: 10. |
| Thử nghiệm tích hợp | 30 | Google và email có kết quả thật hoặc phụ thuộc bị chặn có minh chứng: 10; kiểm cấu hình AI và giới hạn đầu vào: 10; quyết định thiết kế dựa trên kết quả: 10. |
| Lập luận và hồ sơ | 10 | Chỉ ra một phát hiện từ phản biện với AI: 5; bảng yêu cầu và log có thể kiểm lại: 5. |
| **Tổng** | **100** | |

Rubric yêu cầu và test case được đối chiếu trực tiếp với hành vi chín nhóm chức năng. Điểm phân tích phụ thuộc bị chặn không xác nhận Google/email đã tích hợp thành công.

<a id="m2"></a>

## 7. M2 - Thiết kế UI, API và schema cho các chức năng InsightHub

### 7.1 Kết quả InsightHub cần đạt

Có thiết kế nối được từ hành trình người dùng đến UI, API, schema và test case cho phạm vi bài tập. Đầu vào là yêu cầu và kết quả spike M2.1; thiết kế đủ rõ để triển khai hành trình M3.1 và các chức năng còn lại tại M3.

### 7.2 Chức năng và công việc cần thực hiện

<a id="lr-10"></a>

1. **Thiết kế Figma.** Hoàn thiện màn hình UI-01 đến UI-08 trong phạm vi Tóm tắt và Quiz; nối prototype cho các hành trình chính. Thiết kế tại 1440 × 900 và 390 × 844 pixel CSS, với trạng thái đang xử lý, chưa có dữ liệu, lỗi, không đủ căn cứ (`NoEvidence`), hết phiên, xung đột và nguồn đã xóa. Ghi hành vi Tab, Shift+Tab, Enter, Space và phím mũi tên theo loại điều khiển; thể hiện thứ tự focus, giữ focus trong dialog và trả lại khi đóng. Gắn nhãn, thông báo lỗi đúng trường. Thiết kế thông tin nhà cung cấp và phạm vi dữ liệu gửi dịch vụ AI trước thao tác tương ứng theo IH-INT-002-AC03. Liên kết trạng thái giao diện với yêu cầu, API và dữ liệu; cấp quyền xem cho giảng viên.

<a id="lr-11"></a>

2. **Thiết kế API và dữ liệu.** Dựa trên mục 3.3 và 3.7 của SRS, lập sơ đồ quan hệ, từ điển dữ liệu và OpenAPI cho phạm vi bài tập. Với mỗi đối tượng, xác định trường, kiểu dữ liệu, điều kiện bắt buộc, giá trị mặc định, quan hệ, quyền đọc hoặc sửa và vòng đời. Phân biệt schema dữ liệu logic, schema trao đổi qua API và schema lưu trữ vật lý; không mặc định mỗi đối tượng logic phải có một bảng riêng.

   Xác định dữ liệu máy chủ quyết định, dữ liệu người dùng được nhập và dữ liệu nội bộ không được trả về. Tách nội dung Quiz trước và sau khi nộp. Phân biệt phiên bản cấu trúc `schema_version`, phiên bản thông tin mô tả `metadata_version`, tiêu đề nội dung `content.title` và tên hiển thị `display_name`. Thiết kế cách xử lý phiên bản không hỗ trợ, dữ liệu sai cấu trúc và cập nhật từ phiên bản cũ.

   Chọn module nền dự kiến phải sửa khi tích hợp hoặc refactor; xác định hành vi cần giữ và phép characterization cần chạy trước lần sửa đầu. Việc này là phần kế hoạch tích hợp, không yêu cầu hoàn thành ASG01 tại M2.

   Mô tả giao dịch và các điều kiện phải luôn đúng khi gửi lặp, nộp Quiz, xóa nguồn, công bố kết quả và khởi động lại. Bản ghi chống gửi lặp hết hạn không được làm mất dữ liệu nghiệp vụ. Có ví dụ dữ liệu hợp lệ và không hợp lệ cho những nhánh đang thiết kế, kế hoạch migration, cùng ít nhất một ADR so sánh hai phương án. Đối chiếu [hướng dẫn thiết kế và tích hợp](#data-api) trước khi chọn cách áp dụng hợp đồng tham khảo vào Starter.

### 7.3 Điều kiện hoàn thành

- Figma bao phủ các Auth flow, Notebook/workspace, Document, Conversation, Note, Summary, Quiz và quản lý Output trong UI-01 đến UI-08, với các trạng thái áp dụng.
- API và schema thể hiện input/output, lỗi, session, ownership, pagination, version và dữ liệu nội bộ; không lộ đáp án Quiz trước khi nộp.
- Thiết kế thể hiện quan hệ, transaction, persistence, xóa, gửi lặp và dữ liệu qua restart/migration; các lựa chọn giữ đúng hành vi SRS.
- Có ADR so sánh phương án và một nhận xét review có căn cứ; khác biệt giữa Figma, API và dữ liệu được xử lý trước code phần liên quan.

### 7.4 Áp dụng SDLC và AI

**Kiến thức áp dụng:**

- Luồng người dùng, thiết kế trạng thái và khả năng sử dụng trên hai kích thước màn hình được quy định.
- Domain-Driven Design ở mức phù hợp: thuật ngữ, thực thể, quyền sở hữu và ranh giới nghiệp vụ.
- API contract, mô hình dữ liệu, migration và ADR.

| Nhóm chức năng | Phần thiết kế cần đối chiếu |
| --- | --- |
| Auth và Email | Màn hình và callback, trạng thái account/session/identity, trigger email và link/token; dữ liệu do Auth provider quản lý. |
| Notebook, Document, Conversation, Note | Quan hệ và ownership, API thao tác, danh sách, xử lý lỗi/conflict, nguồn và quy tắc xóa. |
| Summary và Quiz | Cấu hình người dùng, schema output, nguồn, bản sao Note, QuizAttempt và dữ liệu công khai trước/sau nộp. |
| AI Job và Output | State machine, deadline, quota, idempotency, version và thời điểm công bố kết quả. |

Chọn một hành trình, đi từ Figma → request/response → transaction/data → test case. Dùng Claude phản biện điểm không nhất quán; học viên quyết định giải pháp và cập nhật đồng thời các phần bị ảnh hưởng. Đây là cách áp dụng thiết kế domain và contract vào sản phẩm, không chỉ vẽ ERD.

Nhờ Claude đóng vai người dùng và reviewer API để tìm hành trình chưa xử lý. Tự đối chiếu Figma, API và dữ liệu trên cùng một tình huống. Nếu nhập dữ liệu nền chưa có chủ sở hữu, người vận hành phải chọn tài khoản và Notebook đích, kiểm quan hệ và quyền trước khi đưa vào sử dụng. Không tự gán cho người đăng ký đầu tiên; R1 không có chức năng chuyển chủ sở hữu Notebook. Review bất đồng bộ một thiết kế của bạn học hoặc mẫu lớp và ghi nhận xét có căn cứ; không phải chờ bạn học để tiếp tục.

**Tài liệu dùng cho milestone:** [SRS: dữ liệu](02_SRS_InsightHub_v1.0.md#sec-3-7); [SRS: giao diện](02_SRS_InsightHub_v1.0.md#sec-3-5); [API starter](../API_Contract_Starter_v1.md); [tích hợp xác thực và Notebook](#data-api).

### 7.5 Evidence, cách nộp bài và thời hạn

**Hạn hoàn thiện:** trước buổi 6 ít nhất 12 giờ. Gửi link PR nhánh `milestone/m2`, bản ghi nộp bài và link Figma có quyền xem. Trong repository lưu API, sơ đồ quan hệ, từ điển dữ liệu, ví dụ hợp lệ và không hợp lệ, migration dự kiến, quyết định kiến trúc và nhận xét review. Có thể gộp các phần trong cùng hồ sơ thiết kế; không tạo bài nộp riêng cho từng loại minh chứng.

Dùng cùng hồ sơ thiết kế để liên kết flow - state - AC - API - data. Một liên kết đến đúng phần thiết kế đủ thay cho việc chép lại nội dung vào nhiều file; vẫn giữ link Figma có quyền xem.

### 7.6 Rubric đánh giá

| Tiêu chí | Điểm tối đa | Cách chấm điểm |
| --- | --- | --- |
| Figma và hành trình | 30 | Đủ màn hình và hành trình: 10; trạng thái chính và ngoại lệ: 10; hai kích thước cùng bàn phím và quản lý focus: 10. |
| API và mô hình dữ liệu | 30 | API nhất quán với UI và cách tích hợp Starter đã chọn: 10; từ điển dữ liệu, quan hệ, trạng thái và phiên bản rõ: 10; quyền sở hữu và dữ liệu Quiz trước/sau nộp đúng: 10. |
| Độ an toàn của thiết kế | 25 | Migration có kiểm soát: 10; gửi lặp, xử lý đồng thời và phản hồi muộn: 10; phương án xử lý lỗi và khôi phục: 5. |
| Quyết định và review | 15 | So sánh hai phương án có căn cứ: 5; rà soát mẫu hoặc bài bạn học có đối chiếu: 5; link và phiên bản thiết kế kiểm được: 5. |
| **Tổng** | **100** | |

Đánh giá tính nhất quán trên hành trình cụ thể, đặc biệt Auth/Email, quyền Notebook và Quiz trước/sau nộp; không đánh giá bằng số frame, endpoint hoặc bảng dữ liệu.

<a id="m31"></a>

## 8. M3.1 - Chạy hành trình Auth - Notebook - Document - Chat bằng TDD

### 8.1 Kết quả InsightHub cần đạt

Tài khoản A đăng nhập, tạo/mở Notebook, upload tài liệu, hỏi đáp và mở citation; conversation đọc lại được sau reload/restart. Tài khoản B bị chặn khi truy cập dữ liệu của A. Đây là hành trình tích hợp đầu tiên trên thiết kế M2; toàn bộ Auth, năm email, Note, Summary và Quiz được hoàn thiện tại M3.

### 8.2 Chức năng và công việc cần thực hiện

<a id="lr-12"></a>

1. **Triển khai hành trình Auth - Notebook - Document - Chat.** Hoàn thiện và kiểm lần lượt các bước dưới đây trên cùng một phiên bản:

| Bước | Chức năng học viên triển khai | Kết quả phải quan sát được |
| --- | --- | --- |
| Đăng nhập | Chọn một Auth flow hợp lệ của SRS để tạo session thực cho hai tài khoản A/B. Nếu dùng email/mật khẩu, hoàn thiện đăng ký, EML-001 và xác minh email; nếu dùng Google, xác minh phản hồi và email theo IH-AUTH-004. | Tài khoản `Active` truy cập nghiệp vụ; server xác định đúng người dùng từ session. Không dùng tài khoản giả lập để thay Auth. |
| Notebook | A tạo, liệt kê và mở Notebook của mình. | Dữ liệu đúng owner; tài khoản B không có quyền xem hoặc sửa qua UI/API. |
| Document | A upload một tài liệu hợp lệ vào Notebook, theo dõi xử lý đến `Ready`, mở nội dung. | Document thuộc đúng Notebook; ingestion/index của Starter được dùng qua kiểm quyền. |
| Chat và citation | A hỏi trên nguồn hợp lệ, nhận câu trả lời và mở vị trí nguồn tương ứng. | Kiểm nguồn trước retrieval, citation mở đúng tài liệu và vị trí còn quyền truy cập. |
| Conversation | Lưu lượt hỏi đáp và mở lại conversation. | Nội dung còn sau reload/restart; tài khoản B không đọc được bằng cách thay ID. |

Khi không chỉ định nguồn, lưu tập tài liệu `Ready` tại lần tiếp nhận đầu; nguồn được thêm sau đó không tham gia thao tác cũ. Danh sách rỗng hoặc không hợp lệ bị từ chối, không tự đổi phạm vi. Dữ liệu nghiệp vụ được lưu độc lập với operation TTL. Tích hợp các quy tắc idempotency, quota, deadline và kiểm quyền áp dụng cho luồng Chat theo SRS; kiểm tổng hợp tiếp tại M4. Trước lần sửa đầu tiên vào module nền dự kiến dùng cho bài refactor, lưu characterization test. Nếu sửa nền trong M3.1, phải giữ test và kết quả baseline trước diff đó, không chờ tới B7. ASG01 vẫn giao B7 và hoàn thiện trước B9 theo hạn tại mục 2.1.

<a id="lr-13"></a>

2. **Thực hiện TDD cho một hành vi có rủi ro.** Tự xác định kỳ vọng từ yêu cầu, kiểm xem assertion trong test có bỏ lọt lỗi hay không. Viết test cho trường hợp hợp lệ và sai quyền hoặc xung đột; ghi lần thất bại vì thiếu hoặc sai hành vi, sau đó triển khai và ghi lần đạt cùng regression test. Giữ lịch sử đúng trình tự; không dựng lại test thất bại sau khi chức năng đã hoàn thành.

### 8.3 Điều kiện hoàn thành

- Hành trình LR-12 chạy qua UI, API và DB, với Auth/session thực; không lấy dữ liệu mock hoặc `owner_id` phía client thay xác thực.
- Nguồn được chọn và lưu đúng tại lần tiếp nhận; có test nguồn không hợp lệ và tài khoản B truy cập qua API.
- Conversation còn sau reload/restart và không phụ thuộc thời hạn bản ghi thao tác.
- Có một chu trình TDD với test thất bại đúng nguyên nhân, code làm test đạt và regression test; characterization test được giữ trước lần sửa module nền.

### 8.4 Áp dụng SDLC và AI

**Kiến thức áp dụng:**

- Tích hợp giao diện, API và cơ sở dữ liệu cho một hành trình hoàn chỉnh.
- Test-Driven Development: viết test thất bại đúng nguyên nhân, triển khai để test đạt, rồi cải thiện cấu trúc.
- Kiểm quyền phía máy chủ và sử dụng mô phỏng đúng ranh giới.

1. Chọn một Auth flow hợp lệ và các API/schema cần cho hành trình từ thiết kế M2. Tự viết expected result cho quyền A/B và tập nguồn.
2. Dùng Claude đề xuất test, kiểm assertion, chạy test để thấy hành vi còn thiếu hoặc sai. Lưu kết quả trước khi triển khai.
3. Triển khai từng đoạn UI - API - DB, tái sử dụng ingestion và RAG của Starter; chạy lại test và kiểm trực tiếp hành trình.
4. Review diff về quyền, truy vấn và persistence; kiểm regression phần nền bị ảnh hưởng, cập nhật cùng bảng truy vết.

Yêu cầu Claude đề xuất test từ tiêu chí chấp nhận trước khi sửa code. Kiểm rằng test thất bại vì hành vi cần xây, không vì môi trường hỏng. Cho AI thực hiện từng thay đổi nhỏ và review phần truy vấn và quyền; không chỉ kiểm nút trên UI.

**Tài liệu dùng cho milestone:** [Tích hợp xác thực và Notebook](#data-api); [quyết định về nguồn](../adr/ADR-002-Source-Provenance.md); [xử lý gửi lặp](../adr/ADR-003-Operation-Idempotency.md); Figma và API đã thiết kế tại M2.

### 8.5 Evidence, cách nộp bài và thời hạn

**Hạn hoàn thiện:** trước buổi 7 ít nhất 12 giờ. Gửi link PR nhánh `milestone/m3.1` và bản ghi nộp bài. Nộp mã nguồn, kiểm thử và migration, kết quả chạy hành trình của hai tài khoản A và B và link các commit cùng log thể hiện test thất bại rồi đạt.

Evidence cần nối được lần đăng nhập, Notebook, Document và Conversation trong cùng hành trình của A, cùng request bị từ chối của B. Che token/secret. Ghi nhánh Auth đã thực hiện; không kết luận toàn bộ IH-AUTH hoặc một AC nhiều nhánh đã đạt từ một lần đăng nhập.

### 8.6 Rubric đánh giá

| Tiêu chí | Điểm tối đa | Cách chấm điểm |
| --- | --- | --- |
| Luồng tích hợp thực tế | 35 | Đăng nhập và Notebook: 10; tải tài liệu/hỏi đáp/nguồn: 15; hội thoại bền vững sau khởi động lại: 10. |
| Phạm vi và phân quyền | 25 | Nguồn mặc định, tập con và đầu vào sai: 10; chặn tài khoản B qua API: 10; UI xử lý lỗi quyền: 5. |
| TDD có lịch sử | 25 | Test thất bại đúng nguyên nhân: 10; test đạt sau triển khai: 10; có test case sai quyền hoặc xung đột: 5. |
| Tái kiểm và giải thích | 15 | Pull Request, commit và log xác định được: 5; lệnh chạy lại rõ: 5; giải thích quyết định với AI và mô phỏng: 5. |
| **Tổng** | **100** | |

Điểm luồng tích hợp dựa trên hành trình hoạt động qua UI/API/DB; điểm quyền dựa trên server và nguồn thực tế. Phần Auth chưa thuộc hành trình này vẫn phải hoàn thiện tại M3.

<a id="m3"></a>

## 9. M3 - Hoàn thiện Auth, Email, dữ liệu nghiệp vụ, Summary và Quiz

### 9.1 Kết quả InsightHub cần đạt

Bản phát triển có đầy đủ chín nhóm chức năng bắt buộc, tích hợp qua UI/API/DB và giữ đúng các quy tắc của SRS. Học viên tiếp tục từ hành trình M3.1, bổ sung các nhánh còn thiếu, test cùng chức năng và thực hiện refactor. M4 tổng hợp nghiệm thu, đánh giá AI, bảo mật và sửa lỗi còn phát hiện; không chờ M4 mới bắt đầu test.

### 9.2 Chức năng và công việc cần thực hiện

Các mã LR dùng để truy vết, không phải thứ tự coding cứng. Thiết kế và tích hợp cơ chế dùng chung LR-18 trước hoặc cùng LR-16/17: trạng thái, quyền nguồn, quota/idempotency, deadline, schema validation và lưu kết quả. Tái dùng phần đã kiểm cho Chat ở M3.1; không chờ hai tool xong mới bổ sung quyền hoặc persistence.

Các checklist dưới đây làm rõ phần chức năng phải hoàn thiện, không thay AC chi tiết và giới hạn của SRS. Đối chiếu mã yêu cầu tại mục 1.1 và [mapping từng AC](#pham-vi-truy-vet), cập nhật kết quả trong cùng bảng truy vết.

<a id="lr-14"></a>

1. **Hoàn thiện Auth và năm transactional email.** Bổ sung các nhánh chưa làm ở M3.1, tích hợp với dữ liệu Notebook và kiểm qua UI/API.

| Chức năng Auth | Công việc và kết quả cần hoàn thiện |
| --- | --- |
| Đăng ký và xác minh email | Kiểm input, tạo `PendingVerification`, gửi EML-001; link hợp lệ chuyển `Active`, link sai/hết hạn/đã dùng không kích hoạt. Gửi lại tuân rate limit. Session chờ xác minh chỉ cho xem trạng thái, gửi lại email và logout; luồng recovery công khai vẫn được phép theo UC-02.A4. |
| Đăng nhập email/mật khẩu | Tài khoản `Active` đăng nhập và mở danh sách Notebook của mình; email hoặc mật khẩu sai có cùng thông báo. Kiểm rate limit cả qua UI và API. |
| Đăng nhập Google | Danh tính mới có email được Google xác minh tạo tài khoản `Active`; lần sau vào đúng tài khoản/dữ liệu. Hủy đăng nhập hoặc phản hồi/token/email không hợp lệ không tạo session hay hoàn tất tài khoản. |
| Liên kết Google cùng email | Với tài khoản `Active`, kiểm phản hồi Google và mật khẩu hiện tại trong cùng giao dịch theo LIM-19. Với `PendingVerification`, hoàn tất UC-02.A4 để vô hiệu mật khẩu, session và link cũ trước khi cấp quyền nghiệp vụ; sau đó bắt đầu lại Google và xác nhận mật khẩu mới. Không tự liên kết chỉ vì trùng email. |
| Quên/reset mật khẩu | Phản hồi công khai không tiết lộ tài khoản. Tài khoản có mật khẩu nhận EML-002; tài khoản chỉ dùng Google nhận EML-004. Link hợp lệ đổi mật khẩu và thu hồi session cũ; sai/hết hạn/đã dùng không đổi dữ liệu. Reset tài khoản chờ xác minh không tự cấp session hoặc liên kết Google. |
| Profile và đổi mật khẩu | Xem email, tên, phương thức và trạng thái xác minh; sửa tên, dùng avatar mặc định hoặc Google theo SRS. Đổi mật khẩu có tái xác thực và thu hồi session cũ; tài khoản chỉ dùng Google không có chức năng đổi mật khẩu ứng dụng. R1 không đổi email hoặc upload avatar. |
| Session và logout | Reload vẫn đúng người dùng khi session hợp lệ; logout/hết hạn/thu hồi chặn request cũ và dọn dữ liệu riêng trên client. Kiểm lại session, quyền và trạng thái trước khi hiển thị phản hồi AI muộn. |

Kiểm giới hạn theo tài khoản và IP trong cửa sổ trượt tại LIM-09; đăng nhập thành công không xóa các lần sai còn hiệu lực, yêu cầu bị chặn không kéo dài cửa sổ bằng cách ghi thêm lỗi. Kiểm tái xác thực và thu hồi session theo LIM-07/LIM-19. Nhánh tiếp nhận tài khoản chờ xác minh phải vô hiệu mật khẩu, session và link cũ trước khi cấp quyền nghiệp vụ.

| Email | Trigger và kết quả phải kiểm |
| --- | --- |
| EML-001 - Xác minh email | Đăng ký hoặc gửi lại xác minh; người dùng nhận thư, mở link đúng account và xác minh theo thời hạn/quy tắc dùng một lần. |
| EML-002 - Reset mật khẩu | Yêu cầu recovery hợp lệ cho tài khoản có mật khẩu; nhận thư và dùng link để reset, kiểm link sai/hết hạn/đã dùng. |
| EML-003 - Thông báo liên kết Google | Liên kết thành công; thư thông báo đúng sự kiện, không dùng thư này để cấp quyền liên kết. Lỗi chuyển giao không làm mất liên kết đã hoàn tất. |
| EML-004 - Hướng dẫn tài khoản Google | Yêu cầu recovery cho tài khoản chỉ dùng Google; thư hướng dẫn đúng phương thức, không tự tạo mật khẩu ứng dụng. |
| EML-005 - Thông báo thay đổi mật khẩu | Reset hoặc đổi mật khẩu thành công; thư thông báo đúng sự kiện. Lỗi gửi không hoàn tác mật khẩu hoặc khôi phục session đã thu hồi. |

Kiểm đủ năm email bằng cấu hình thật và hộp thư nhận theo [hướng dẫn Auth/Email](#auth-email), gồm nội dung, link, lỗi, thời hạn và rate limit áp dụng. Provider chấp nhận gửi chưa chứng minh đã nhận thư; fixture chỉ bổ sung kiểm lỗi, không thay bằng chứng tích hợp thật.

<a id="lr-15"></a>

2. **Hoàn thiện Notebook, Document, Conversation và Note.** Triển khai các thao tác được quy định riêng cho từng đối tượng, cùng UI, API và persistence tương ứng.

| Đối tượng | Checklist chức năng | Kết quả cần kiểm |
| --- | --- | --- |
| **Notebook** | Tạo, liệt kê/phân trang, mở; đổi tên/mô tả có validation/version conflict; xóa có xác nhận và hủy; áp dụng hạn mức. | Owner lấy từ session; dữ liệu, thứ tự và thời điểm đúng SRS. Xóa Notebook chặn mọi tài nguyên con, lịch sử và tác vụ đang chạy; thực hiện chính sách xóa vật lý theo LIM-13. |
| **Document** | Upload TXT, Markdown và PDF có văn bản; xem `Processing`, `Ready`, `Failed`; retry lỗi, xem metadata/nội dung, mở citation và xóa. | Kiểm nội dung thực, định dạng và giới hạn; xử lý tệp rỗng, PDF ảnh/mã hóa và byte trùng theo SRS. Retry tạo lần xử lý mới cho cùng Document, không nhân bản Document/chunk; chống trùng trong đúng Notebook. Không tự thêm chức năng sửa nội dung tệp gốc. |
| **Chat và Conversation** | Hỏi trên nguồn hợp lệ; phân biệt `Answered`, `NoEvidence`, `Failed`; tạo, liệt kê, mở lịch sử, đổi tên có version và xóa có xác nhận. | Lượt lưu câu hỏi, kết quả, trạng thái, nguồn và thời điểm; thứ tự đúng, còn sau reload/restart. Mỗi câu hỏi được xử lý độc lập, UI làm rõ giới hạn ngữ cảnh. Retry/gửi lặp đúng SRS; mất nguồn không cấm xem/đổi tên/xóa lịch sử hợp lệ, nhưng không cho hỏi trên tập nguồn rỗng. |
| **Note** | Tạo, liệt kê, mở, sửa tiêu đề/nội dung có version conflict; xóa có xác nhận/hủy; lưu câu trả lời hoặc Summary hợp lệ thành Note. | Không lưu `NoEvidence`/`Failed` thành câu trả lời thành công. Bản sao độc lập có provenance, sửa Note không sửa nội dung gốc; xóa conversation/output không xóa Note đã sao chép. Xóa Note không xóa nguồn, nhưng xóa Notebook vẫn chặn Note. |

Server kiểm quyền đối tượng thực sự được truy cập, không tin `owner_id` hoặc Notebook do client gửi. Kiểm tài khoản B thay ID để đọc/sửa/xóa tài nguyên của A. Giữ persistence, thứ tự danh sách, pagination ở nơi SRS quy định và thời điểm cập nhật theo mục 3.7.3. Nguồn đã xóa không được đọc lại qua citation hoặc cache; lịch sử hợp lệ được giữ với trạng thái nguồn không còn khả dụng theo BR-08. Kiểm ảnh hưởng xóa khi AI đang chạy theo LR-18.

<a id="lr-16"></a>

3. **Xây dựng Tóm tắt.** Cho chọn bản ngắn 150-250 từ hoặc chi tiết 400-600 từ, mặc định ngắn. Nội dung có tổng quan, ý chính gắn nguồn và điểm cần chú ý; phản ánh các tài liệu đã chọn và nêu mâu thuẫn nếu có. Nếu không ghi nhận điểm đặc biệt, nêu rõ thay vì tạo mâu thuẫn giả. Kiểm cấu trúc, độ dài và tham chiếu trước khi lưu; đánh giá tính đúng của nội dung riêng theo bộ dữ liệu nghiệm thu. Lưu thành ghi chú tạo bản sao độc lập; nếu vượt giới hạn ghi chú, cho người dùng sửa trước khi lưu, không cắt ngầm.

<a id="lr-17"></a>

4. **Xây dựng Quiz.** Cho chọn 5 hoặc 10 câu, mặc định 5; mỗi câu có bốn lựa chọn khác nhau và đúng một đáp án đúng. Trước khi nộp, mọi đường đọc phục vụ làm bài chỉ trả câu hỏi và lựa chọn, không trả đáp án, giải thích hoặc điểm; chỉ ẩn ở giao diện là chưa đủ. Máy chủ kiểm câu và lựa chọn thuộc đúng đề, từ chối điểm do client gửi, tính câu bỏ trống là sai và làm tròn điểm phần trăm đến một chữ số thập phân.

   Chấm và lưu lựa chọn, điểm, thời điểm nộp một lần nhất quán. Khi nộp lại cùng định danh lần làm đã nộp, trả kết quả đã lưu nếu còn quyền, kể cả khi dữ liệu lựa chọn gửi lại khác; không chấm lại hoặc ghi đè. Làm lại tạo lần làm mới; các lần đã nộp mở lại được sau khởi động lại. Định danh lần làm Quiz khác mã chống gửi lặp của tác vụ tạo nội dung. R1 không lưu nháp từng lựa chọn trước khi nộp; giao diện thông báo giới hạn này.

<a id="lr-18"></a>

5. **Hoàn thiện vòng đời công cụ AI.** Chọn 1-3 nguồn `Ready` cùng Notebook, tổng tối đa 60.000 ký tự; kiểm cấu trúc, định danh, nguồn, quyền và thời hạn trước khi công bố. Có danh sách, lọc theo loại, xem, đổi tên, tạo lại và xóa. Tạo lại sinh bản độc lập liên kết bản gốc; đổi tên chỉ đổi `display_name` và phiên bản thông tin mô tả, giữ nội dung AI đã lưu.

   Hỏi đáp, Tóm tắt và Quiz dùng chung hạn mức theo người dùng: tối đa một tác vụ AI đang chạy và 10 yêu cầu mới được tiếp nhận trong 60 giây. Đối soát mã thao tác trước khi tính lượt mới. Gửi lại cùng mã sử dụng nguồn, cấu hình và giá trị mặc định đã lưu từ lần đầu; không tính lại theo dữ liệu hiện tại. Cùng mã với dữ liệu khác trả xung đột, đổi thứ tự cùng tập nguồn không tạo yêu cầu khác, ID nguồn lặp bị từ chối. Kiểm và lưu hạn mức phải nhất quán khi yêu cầu đến đồng thời.

   Phân biệt `NoEvidence`, `Failed` và kết quả thành công. Khởi động lại hoặc thử lại nội bộ không đặt lại thời hạn: tác vụ hết hạn phải kết thúc trước khi tiếp tục xử lý hoặc trả như đang chạy hợp lệ; giải phóng suất khi kết thúc. Khi xóa nguồn, kiểm riêng ba trường hợp BR-08 theo thứ tự hoàn tất giao dịch trên máy chủ: xóa trước công bố thì chặn thành công; công bố trước xóa thì giữ lịch sử với nguồn không còn khả dụng; phản hồi đến muộn phải đối soát phiên, quyền và trạng thái trước khi hiển thị. Xóa Notebook chặn cả lịch sử; xóa kết quả Quiz xóa các lần làm liên quan. Kiểm giới hạn ở đúng biên và vượt biên, không cắt dữ liệu ngầm.

<a id="lr-19"></a>

6. **Refactor một module và tự động hóa một tác vụ.** Chọn vấn đề cụ thể trong module hiện hữu, sử dụng kiểm thử đã lưu trước lần sửa đầu và bổ sung phần còn thiếu. Lập kế hoạch, refactor, kiểm hồi quy và so sánh trước/sau. Chuẩn hóa một tác vụ lặp thành hướng dẫn hoặc skill kết hợp script hay hook đã thực chạy; hook cần có sự kiện kích hoạt và log, không lấy chạy tay làm bằng chứng hook. Đây là bài Assignment trong cùng dự án, được giao chính thức ở buổi 7; việc giữ kiểm thử trước thay đổi từ buổi 6 không tạo bài tập riêng.

### 9.3 Điều kiện hoàn thành

- Auth và năm transactional email hoạt động theo LR-14; có kết quả tích hợp thật, sai/hết hạn link, giới hạn và session liên quan.
- Notebook, Document, Conversation và Note có các thao tác, trạng thái, quyền và vòng đời tại LR-15.
- Summary và Quiz chạy từ chọn nguồn đến lưu/xem lại; Quiz được chấm tại server, bảo vệ đáp án và xử lý nộp lặp đúng.
- AI Job/Output có trạng thái, quota, idempotency, deadline, version, regenerate và xóa; UI xử lý lỗi tương ứng.
- Code, test, migration và CI được cập nhật; phần chưa đạt được ghi rõ. Refactor có characterization test, diff và regression test, tiếp tục hoàn thiện đến hạn Assignment.

### 9.4 Áp dụng SDLC và AI

**Kiến thức áp dụng:**

- Triển khai theo đặc tả, quản lý trạng thái, giao dịch, giới hạn và tính nhất quán dữ liệu.
- Characterization test để ghi nhận hành vi hiện hữu trước thay đổi, refactor và regression test.
- Đầu ra AI có cấu trúc, kiểm nguồn và tự động hóa tác vụ phát triển.

| Vòng phát triển | Áp dụng vào chức năng | Cách dùng AI và tự kiểm |
| --- | --- | --- |
| Chọn hành vi | Lấy một dòng checklist LR-14 đến LR-18, nối với AC và thiết kế M2. | Claude hỗ trợ phân rã thay đổi; học viên xác nhận dependency và expected result. |
| Triển khai và test | Hoàn thiện UI, API, data và test cho cùng hành vi; kiểm nhánh thành công, lỗi/quyền liên quan. | Review diff nhỏ, kiểm request/response và dữ liệu thay vì chỉ nhìn màn hình. |
| Tích hợp | Chạy lại hành trình M3.1, nối thêm Note, Summary, Quiz và quản lý Output. | Dùng AI phân tích lỗi; giữ căn cứ độc lập và regression test. |
| Refactor | Cải thiện một module đã có hành vi được characterization test ghi nhận. | So sánh trước/sau, giữ quy tắc nghiệp vụ và tự động hóa tác vụ đã kiểm. |

Dùng Claude triển khai theo từng hành vi và review diff nhỏ. Với refactor, yêu cầu chỉ ra vấn đề có bằng chứng trước khi đề xuất thay cấu trúc; đổi tên hoặc định dạng đơn thuần chưa đủ. Script có thể chạy test, lint và các bước kiểm tra trong terminal hoặc CI, không bắt buộc dùng agent tự động. UI cần trạng thái đang xử lý, rỗng, lỗi và khôi phục; ghi khác biệt hợp lý so với Figma.

**Tài liệu dùng cho milestone:** [SRS: yêu cầu chức năng](02_SRS_InsightHub_v1.0.md#sec-3-4); [SRS: dữ liệu và giới hạn](02_SRS_InsightHub_v1.0.md#sec-3-7); [danh mục email](02_SRS_InsightHub_v1.0.md#email-catalog); Figma và API của bài làm tại M2.

### 9.5 Evidence, cách nộp bài và thời hạn

**Hạn chức năng:** trước buổi 8 ít nhất 12 giờ. Gửi link PR nhánh `milestone/m3` và bản ghi nộp bài với mã nguồn, kiểm thử, migration, kết quả chạy các luồng và kiểm quyền. **Hạn Assignment refactor:** trước buổi 9 ít nhất 12 giờ; bổ sung kiểm thử ở M4, gửi link PR refactor riêng cùng kết quả trước/sau để giảng viên chấm bài Assignment.

Trong cùng bảng truy vết, dẫn tới test hoặc demo của từng nhóm chức năng, kết quả gửi/nhận năm email và migration trên dữ liệu đã có. Tái dùng evidence cho nhiều AC nếu chứng minh được từng điều kiện; không tạo chín bài nộp riêng.

### 9.6 Rubric đánh giá

| Tiêu chí | Điểm tối đa | Cách chấm điểm |
| --- | --- | --- |
| Tài khoản và dữ liệu nghiệp vụ | 25 | Đủ Auth và năm transactional email: 10; thao tác Notebook/Document/Conversation/Note, hạn mức và pagination theo SRS: 10; persistence và ownership: 5. |
| Tóm tắt và Quiz | 25 | Tóm tắt đúng độ dài, nội dung và nguồn: 10; Quiz đúng cấu trúc và chấm tại server: 10; ghi chú độc lập và lịch sử lần làm: 5. |
| Vòng đời và ngoại lệ | 25 | Trạng thái, hạn mức và giới hạn: 10; gửi lặp, đồng thời, xóa và phản hồi muộn: 10; UI và khôi phục: 5. |
| Refactor và tự động hóa | 15 | Có test trước thay đổi và hồi quy: 5; cải thiện có căn cứ: 5; script hoặc skill thực chạy: 5. |
| Chất lượng bài nộp | 10 | Mã nguồn, kiểm thử, migration và CI được cập nhật: 5; giải thích quyết định và phần chưa hoàn tất: 5. |
| **Tổng** | **100** | |

**Rubric Assignment refactor: 100 điểm, chiếm 25% điểm khóa.** Chấm bốn mức cho từng dòng: 0% nếu chưa có minh chứng; 40% nếu mới làm một phần, chưa đạt mô tả cốt lõi; 70% khi đạt mô tả cốt lõi; 100% khi đạt cả cốt lõi và phần đầy đủ. Điểm mỗi dòng bằng điểm tối đa nhân tỷ lệ tương ứng.

| Tiêu chí | Điểm tối đa | Đạt cốt lõi (70%) | Đầy đủ (100%) |
| --- | --- | --- | --- |
| Bảo toàn hành vi | 30 | Có test trước thay đổi, giữ quy tắc nghiệp vụ; hành vi mới có yêu cầu rõ | Tái chạy trước/sau với edge case và giải thích tác dụng phụ |
| Kiểm thử theo rủi ro | 30 | Chọn unit test, integration test, contract test hoặc E2E test phù hợp module; kỳ vọng độc lập, nhật ký đúng phiên bản | Chứng minh test bắt lỗi; xử lý thiếu sót hoặc test không ổn định và kiểm lại |
| Chất lượng refactor | 20 | Thay đổi có mục tiêu, giảm trùng lặp hoặc phụ thuộc hoặc làm rõ ranh giới; CI đạt | So sánh trước/sau chứng minh cải thiện, giải thích đánh đổi và khôi phục |
| Minh chứng và giải thích | 20 | Kế hoạch, diff, test, review và quyết định với AI liên kết được | Truy từ yêu cầu đến test, phản biện được đề xuất AI không phù hợp |
| **Tổng** | **100** | | |

Dòng tài khoản/dữ liệu đối chiếu riêng checklist Auth, năm email và bốn đối tượng LR-15. Dòng AI đối chiếu cả nội dung Summary, quy trình Quiz và vòng đời Output; màn hình có dữ liệu mẫu chưa chứng minh chức năng đạt.

<a id="m4"></a>

## 10. M4 - Kiểm từng chức năng, chất lượng AI và bảo mật InsightHub

### 10.1 Kết quả InsightHub cần đạt

Có kết luận kiểm chứng trên bản tích hợp M3: từng AC áp dụng có kết quả, lỗi được sửa và retest; chất lượng Chat/Summary/Quiz được đánh giá bằng model thật. Học viên chứng minh sản phẩm hoạt động, cách ly dữ liệu và xử lý ngoại lệ đúng, cùng các giới hạn còn tồn tại.

### 10.2 Chức năng và công việc cần thực hiện

<a id="lr-20"></a>

1. **Kiểm toàn bộ phạm vi bài tập.** Cập nhật bảng truy vết cho từng tiêu chí áp dụng và các điều kiện thành phần; thực hiện 21 hành trình nghiệm thu trong phạm vi hai công cụ. Tái dùng kiểm thử đã tích lũy ở M3.1-M3 khi còn đúng phiên bản, bổ sung phần còn thiếu và hồi quy bị ảnh hưởng. Có tình huống diễn đạt theo điều kiện ban đầu, hành động và kết quả (Given/When/Then), nối với test thực chạy. Ghi kỳ vọng, thực tế, phiên bản và lỗi; test case chưa chạy, bỏ qua hoặc bị chặn không được tính là đạt.

<a id="lr-21"></a>

2. **Kiểm giao diện và hiệu năng.** Dùng Chrome hoặc Edge có ghi phiên bản, tại 1440 × 900 và 390 × 844 pixel CSS. Kiểm các trạng thái, phím theo loại điều khiển, thứ tự focus, dialog và thông báo theo thiết kế. Chọn trước 10 thao tác không gọi AI, ít nhất hai thao tác mỗi nhóm danh sách, chi tiết, tạo, sửa và xóa; từng thao tác tối đa 3 giây. Kiểm thời hạn tài liệu 120 giây, hỏi đáp 60 giây và công cụ AI 120 giây, gồm khởi động lại trước hoặc sau thời hạn; ghi cả lỗi và điều kiện môi trường. Hai kích thước này là phạm vi kiểm của bài tập, không chứng minh hỗ trợ mọi thiết bị di động.

<a id="lr-22"></a>

3. **Kiểm phân quyền và vòng đời dữ liệu.** Dùng hai tài khoản, mỗi tài khoản có Notebook với ba tài liệu TXT, Markdown và PDF có văn bản; bộ nguồn có tiếng Việt và tiếng Anh. Với từng loại tài nguyên, kiểm đọc và sửa qua API trực tiếp, thay ID, nguồn, trạng thái, bộ nhớ đệm, hết phiên và xung đột phiên bản. Kiểm ba thứ tự xóa và công bố của BR-08, xóa Notebook, hội thoại, kết quả Quiz và tác vụ tạo lại đã được tiếp nhận. Kiểm gửi lặp sau thay mặc định hoặc thêm nguồn, hai yêu cầu cạnh tranh hạn mức, thời hạn qua khởi động lại và dữ liệu nghiệp vụ còn sau khi bản ghi chống gửi lặp hết hiệu lực. Nêu kỳ vọng và kết quả cho từng điều kiện, không chỉ ghi “đã kiểm đồng thời”.

<a id="lr-23"></a>

4. **Đánh giá AI bằng mô hình thật.** Thực hiện bộ lượt trong bảng dưới và giữ mọi lượt chạy, kể cả thất bại. Trước khi chạy, xác định 3-5 ý kỳ vọng và đoạn nguồn hỗ trợ cho test case có nội dung. Ghi nhà cung cấp, mô hình sinh nội dung, mô hình embedding, phiên bản prompt và schema, hash nguồn, vị trí tham chiếu, commit, thời gian và mức sử dụng. Ngoài các ý kỳ vọng, kiểm từng phát biểu về dữ kiện và từng câu hỏi, lựa chọn, đáp án, giải thích của Quiz; đối chiếu đủ phạm vi nguồn đã chọn. Không dùng JSON hợp lệ hoặc điểm mô hình tự chấm làm bằng chứng duy nhất về nội dung đúng. Các phép đánh giá thủ công này áp dụng cho bộ nghiệm thu, không yêu cầu người duyệt mọi đầu ra trong luồng sử dụng sản phẩm.

<a id="lr-24"></a>

5. **Kiểm bảo mật và sửa lỗi.** Lập threat model, quét bí mật và thư viện của cả Web và API, tạo danh mục thành phần phần mềm (SBOM). Kiểm xác thực, liên kết danh tính, phiên, quyền trên mọi tài nguyên, nội dung Markdown hoặc mã gây XSS, chỉ dẫn độc hại trong tài liệu, tệp tải lên, nhật ký và quyền công cụ hoặc MCP. Xác minh mỗi phát hiện trước khi kết luận; ghi tác động, xử lý và kiểm lại. Phân biệt lỗi sản phẩm, dữ liệu, thời điểm và lỗi test; tăng số lần thử lại hoặc bỏ test không thay việc tìm nguyên nhân. Review một test hoặc đầu ra AI của bạn học hay mẫu lớp; nếu dùng lỗi cài có chủ đích phải ghi rõ.

**Bộ đánh giá AI phải thực hiện:**

| Nhóm | Số lượt/tình huống | Nội dung |
| --- | --- | --- |
| Hỏi đáp | 6 lượt | Ba câu có căn cứ, gồm tiếng Anh và tổng hợp nhiều tài liệu; hai câu thiếu căn cứ; một nguồn có chỉ dẫn gây nhiễu nhưng câu hỏi vẫn trả lời được |
| Tóm tắt | 2 lượt | Một nguồn với bản ngắn; nhiều nguồn với bản chi tiết có thông tin mâu thuẫn |
| Quiz | 2 lượt | Một nguồn với 5 câu; nhiều nguồn với 10 câu; kiểm câu hỏi, lựa chọn, đáp án, giải thích và nguồn |
| Lặp lại | 2 lượt | Chọn trước một câu hỏi đáp có căn cứ và một test case Tóm tắt hoặc Quiz; đánh giá cả hai lần |
| **Tổng nội dung** | **12 lượt** | Dùng mô hình thật; không tính embedding, lượt bổ sung PDF hoặc chạy lại sau sửa vào số này |
| Ngoại lệ, ngoài 12 lượt | Ba nhóm cho cả hai công cụ | Thiếu căn cứ, vượt giới hạn đầu vào, đầu ra sai schema; kiểm thêm lỗi dịch vụ bên ngoài và thời gian chờ bằng mô phỏng có kiểm soát |
| Cách ly, ngoài 12 lượt | Bốn tình huống đại diện | Dữ liệu người khác; nguồn sai Notebook; xóa nguồn khi xử lý; đọc qua API, liên kết và bộ nhớ đệm sau mất quyền. Không thay bộ kiểm quyền từng tài nguyên |

Một lượt có nội dung đạt khi đủ ý kỳ vọng, các dữ kiện đều có căn cứ, tham chiếu hợp lệ và đáp ứng cấu trúc, giới hạn, trạng thái, thời hạn. Ý kỳ vọng không thay việc kiểm các phát biểu khác do mô hình tạo ra. Quiz phải có đúng một đáp án đúng, không mơ hồ. Hai câu thiếu căn cứ phải trả `NoEvidence`; test case có căn cứ không được trả `NoEvidence` hoặc `Failed`. Nếu căn cứ kỳ vọng sai, ghi lý do sửa và phiên bản mới trước khi chạy lại. Không còn lỗi chặn phát hành theo SRS mới kết luận sẵn sàng bàn giao.

### 10.3 Điều kiện hoàn thành

- Bảng truy vết giữ đủ 151 AC áp dụng và 12 AC ngoài phạm vi. Tổng hợp kết quả đã kiểm và phần còn thiếu cho từng nhánh, liên kết 21 UAT trong phạm vi hai tool. Các AC của IH-NFR-009, IH-NFR-010 và IH-REL-001..003 được gán M5: tại M4 ghi “chưa kiểm, chưa đến hạn M5” nếu chưa có evidence; không coi đây là phần đã Pass hoặc tự kéo toàn bộ M5 về M4. Output M4 được kiểm theo LR-20..24; các lỗi của phạm vi đến hạn vẫn phải được ghi và xử lý. Chưa chạy/bị chặn không được tính đạt.
- Có test UI, API, data, quyền A/B, lifecycle, giới hạn và số đo theo LR-20 đến LR-22; lỗi đã sửa có regression test/retest.
- Đủ 12 lượt nội dung AI và các ngoại lệ theo LR-23, lưu cả lượt lỗi; từng claim và câu hỏi Quiz được đối chiếu nguồn.
- Kết quả kiểm bảo mật, SBOM, review và Assignment refactor được cập nhật. Chỉ kết luận sẵn sàng phát hành khi đáp ứng điều kiện SRS; điểm học tập không thay kết quả sản phẩm.

### 10.4 Áp dụng SDLC và AI

**Kiến thức áp dụng:**

- Kiểm thử đa tầng, nghiệm thu theo hành trình người dùng, hồi quy và đo yêu cầu phi chức năng.
- Đánh giá nội dung AI dựa trên nguồn và kết quả kỳ vọng xác lập trước.
- Mô hình mối đe dọa, kiểm quyền, bí mật xác thực, thư viện phụ thuộc và an toàn công cụ AI.

| Nhóm chức năng | Trọng tâm kiểm ở M4 |
| --- | --- |
| Auth và Email | Các nhánh tài khoản, linking/recovery, năm email, session, tái xác thực và rate limit. |
| Notebook và Document | Thao tác, upload/duplicate/retry, ownership, hạn mức, trạng thái, xóa và deadline. |
| Conversation và Note | Persistence, nguồn/citation, version conflict, xóa và bản sao độc lập. |
| Summary và Quiz | Schema, nội dung/nguồn, độ dài/số câu, không lộ đáp án, chấm và nộp lặp/làm lại. |
| AI Job và Output | Shared quota, idempotency, restart, regenerate, ba thứ tự xóa/công bố và phản hồi muộn. |

Tái dùng test đã tích lũy khi còn phù hợp bản nộp, bổ sung khoảng trống theo rủi ro. Dùng Claude đề xuất edge case và phân tích nguyên nhân; học viên xác nhận lỗi, sửa và chạy lại, giữ expected result có căn cứ độc lập.

Dùng Claude tìm edge case và phân tích nguyên nhân lỗi; tự xác lập kỳ vọng trước. Không sửa kỳ vọng hoặc bỏ điều kiện kiểm chỉ để test báo đạt. Có thể dùng mô phỏng thời gian và lỗi nhà cung cấp để kiểm hết thời gian chờ và phiên; chất lượng nội dung phải chạy mô hình thật. Tái dùng dữ liệu và minh chứng giữa các phép kiểm khi phù hợp.

**Tài liệu dùng cho milestone:** [SRS: yêu cầu phi chức năng](02_SRS_InsightHub_v1.0.md#sec-3-10); [SRS: đánh giá AI](02_SRS_InsightHub_v1.0.md#sec-4-2); [SRS: nghiệm thu](02_SRS_InsightHub_v1.0.md#sec-4-3); [công cụ đánh giá nền](../../evaluation/README.md).

### 10.5 Evidence, cách nộp bài và thời hạn

**Hạn hoàn thiện:** trước buổi 9 ít nhất 12 giờ. Gửi link PR nhánh `milestone/m4` và bản ghi nộp bài, gồm bảng kết quả từng yêu cầu, kiểm thử và nghiệm thu, số đo, nguồn và kết quả đánh giá AI, báo cáo bảo mật và danh mục thành phần phần mềm, lỗi đã sửa và nhận xét review. Đồng thời gửi bản hoàn thiện Assignment refactor của M3.

Mỗi kết luận cần chỉ ra chức năng, AC/nhánh, input, expected/actual, môi trường và commit. Dẫn lại cùng test/log nếu dùng cho UAT, bảo mật hoặc regression; không nhập lại kết quả vào nhiều bảng.

### 10.6 Rubric đánh giá

| Tiêu chí | Điểm tối đa | Cách chấm điểm |
| --- | --- | --- |
| Bao phủ nghiệp vụ và nghiệm thu | 25 | Mỗi tiêu chí có kết quả: 10; hành trình nghiệm thu đủ phạm vi: 10; lỗi được sửa và kiểm lại: 5. |
| Giao diện và hiệu năng | 15 | Hai kích thước và trạng thái UI: 5; đủ 10 thao tác có số đo: 5; kiểm thời hạn của tài liệu, hỏi đáp và công cụ AI: 5. |
| Chất lượng AI | 25 | Đủ 12 lượt nội dung và lưu cả lỗi: 10; đối chiếu ý nghĩa, nguồn và câu hỏi Quiz: 10; kiểm ngoại lệ và lượt lặp: 5. |
| Quyền và bảo mật | 25 | Kiểm hai tài khoản A và B trên từng tài nguyên và vòng đời: 10; mô hình đe dọa, kết quả quét và SBOM: 5; sửa và kiểm lại: 5; quyền công cụ AI: 5. |
| Hồ sơ có thể tái kiểm | 10 | Môi trường, phiên bản, lệnh và kết quả rõ: 5; review có căn cứ và cập nhật bài refactor: 5. |
| **Tổng** | **100** | |

Độ bao phủ được kiểm theo chức năng và từng điều kiện AC; tỷ lệ test Pass cao không thay các nhánh còn thiếu. Rubric AI dùng cả ý nghĩa nội dung và nguồn, không chỉ kiểm JSON/schema.

<a id="m5"></a>

## 11. M5 - Phát hành R1, kiểm restore và thực hiện thay đổi R1.1

### 11.1 Kết quả InsightHub cần đạt

Có bản R1 của bài tập cài được trên môi trường sạch, dữ liệu và quyền được kiểm sau migration/restore, sau đó có một thay đổi thành R1.1 cùng regression test. Đầu vào là bản đã kiểm tại M4; chỉ gọi sẵn sàng bàn giao khi đáp ứng điều kiện phát hành của SRS.

### 11.2 Chức năng và công việc cần thực hiện

<a id="lr-25"></a>

1. **Phát hành bản R1 của bài tập.** Gắn phiên bản và Git tag cho sản phẩm trong phạm vi 151 tiêu chí áp dụng, Tóm tắt và Quiz. Đóng gói kèm checksum, cấu hình mẫu và hướng dẫn cài, chạy, xử lý lỗi; kiểm cài đặt trên môi trường sạch và các luồng chính. Ghi giới hạn, lỗi còn mở và kết quả đúng bản phát hành. Hồ sơ không được kết luận đã hoàn thành toàn bộ năm công cụ của SRS. Không bàn giao bí mật hoặc dữ liệu riêng.

<a id="lr-26"></a>

2. **Kiểm nâng cấp và khôi phục dữ liệu.** Chạy migration trên dữ liệu đã có; sao lưu và khôi phục sang môi trường cách ly. Kiểm số lượng, quan hệ, nội dung, phiên bản cấu trúc và quyền của tài khoản, Notebook, tài liệu, hội thoại, ghi chú, kết quả AI và các lần làm Quiz. Nếu xác thực được lưu ở dịch vụ bên ngoài, ghi dữ liệu nào nằm ngoài bản sao lưu ứng dụng, điều kiện khôi phục hoặc tái liên kết và phép kiểm đăng nhập, quyền sau khôi phục. Không tuyên bố khôi phục đầy đủ chỉ từ việc phục hồi cơ sở dữ liệu. Không xóa volume để thay cho nâng cấp và không tự gán dữ liệu chưa có chủ sở hữu cho tài khoản đầu tiên.

<a id="lr-27"></a>

3. **Thực hiện một thay đổi sau R1.** Sau khi đã ghi nhận bản R1 và kết quả kiểm của nó, chọn một yêu cầu thay đổi hoặc lỗi có thể tái hiện. Ghi hành vi trước và sau, tác động tới yêu cầu, giao diện, API, dữ liệu, test và rủi ro. Triển khai thành R1.1, kiểm hồi quy, cập nhật cùng bảng truy vết, hướng dẫn và ghi chú phát hành. Nêu cách quay lại ứng dụng cùng điều kiện bảo toàn dữ liệu; không sửa tag R1 để thay lịch sử.

### 11.3 Điều kiện hoàn thành

- R1 có tag, checksum, hướng dẫn, cấu hình mẫu an toàn và kết quả cài sạch trên đúng phiên bản.
- Kiểm Auth, Notebook, Document/Chat, Note, Summary, Quiz và Output sau cài mới; restore kiểm nội dung, quan hệ và quyền trên dữ liệu đã có.
- Phạm vi backup bao gồm dữ liệu bài làm; nếu dùng Auth provider bên ngoài, mô tả và kiểm phần phục hồi/tái liên kết tương ứng.
- R1 tồn tại và được kiểm trước CR; R1.1 có thay đổi, phân tích tác động, regression test và cách rollback bảo toàn dữ liệu, không sửa tag R1.

### 11.4 Áp dụng SDLC và AI

**Kiến thức áp dụng:**

- Đóng gói phiên bản, cài sạch, migration, sao lưu và khôi phục.
- Hướng dẫn vận hành và ghi chú phát hành.
- Phân tích tác động của yêu cầu thay đổi, kiểm hồi quy và phương án rollback.

1. Chốt candidate từ kết quả M4, kiểm điều kiện phát hành rồi đóng gói R1 với thông tin tái lập.
2. Cài mới theo runbook; chạy hành trình đăng nhập → Notebook → Document/Chat → Note → Summary/Quiz và kiểm quyền.
3. Migration/restore trên môi trường cách ly; so sánh dữ liệu, quan hệ, version và ownership, mở lại conversation/output/QuizAttempt đã lưu.
4. Chọn CR sau R1 trên một chức năng đã có. Dùng Claude phân tích tác động; học viên xác nhận hành vi trước/sau, triển khai, kiểm regression và phát hành R1.1.

Cho Claude rà soát runbook như người mới nhận dự án và phân tích tác động của thay đổi. Tự chạy toàn bộ bước cài đặt và khôi phục; AI không được suy đoán kết quả. Với thao tác dữ liệu, xác định môi trường và bản sao lưu trước khi thực hiện.

**Tài liệu dùng cho milestone:** [Runbook starter](../Runbook_Starter_v1.md); [SRS: điều kiện phát hành](02_SRS_InsightHub_v1.0.md#sec-4-4); [hướng dẫn tích hợp và dữ liệu cũ](#data-api).

### 11.5 Evidence, cách nộp bài và thời hạn

**Hạn hoàn thiện:** trước buổi 10 ít nhất 12 giờ. Gửi link PR nhánh `milestone/m5`, bản ghi nộp bài, link hai tag R1/R1.1 và gói phát hành có checksum. Giữ nguyên tag đã gửi; lần sửa tiếp theo tạo phiên bản mới. Đính kèm kết quả cài đặt mới, nâng cấp và khôi phục và hồ sơ thay đổi.

Hồ sơ release nối tag/checksum với kết quả cài, migration, restore và test chức năng. Hồ sơ CR dùng cùng yêu cầu, thiết kế và bảng truy vết đang quản lý; không tạo sản phẩm thứ hai hoặc thêm hạ tầng cloud bắt buộc.

### 11.6 Rubric đánh giá

| Tiêu chí | Điểm tối đa | Cách chấm điểm |
| --- | --- | --- |
| Bản phát hành tái cài được | 30 | Phiên bản, tag và checksum: 10; cài sạch và kiểm luồng chính: 10; hướng dẫn và cấu hình mẫu đầy đủ: 10. |
| Nâng cấp và khôi phục | 30 | Migration trên dữ liệu đã có: 10; restore cách ly thành công: 10; nội dung và quyền sau restore đúng: 10. |
| Thay đổi sau phát hành | 25 | Phân tích tác động: 5; hành vi mới đúng: 10; hồi quy và phương án quay lại: 10. |
| Bàn giao và giải thích | 15 | Ghi chú R1/R1.1 rõ: 5; kết quả thực chạy có phiên bản: 5; giải thích quyết định với AI: 5. |
| **Tổng** | **100** | |

Rubric release/restore dựa trên hành trình và dữ liệu thật của bài làm. Khởi động container hoặc restore một DB rỗng chưa chứng minh Auth, ownership và dữ liệu nghiệp vụ được khôi phục.

<a id="capstone"></a>

## 12. Capstone - Demo InsightHub và bảo vệ quyết định xuyên SDLC

### 12.1 Kết quả InsightHub cần đạt

Học viên tự demo bản phát hành đã nộp và giải thích được cách chuyển một yêu cầu thành thiết kế, code, test, release và thay đổi. Kết quả sử dụng AI được chứng minh bằng sản phẩm và quyết định cá nhân; kế hoạch 30 ngày chuyển bài học sang công việc thực tế.

### 12.2 Chức năng và công việc cần thực hiện

<a id="lr-28"></a>

1. **Demo và bảo vệ cá nhân.** Chạy bản đã nộp: đăng nhập, Notebook, Document, Chat có citation, Note, Summary, Quiz và một tình huống lỗi/quyền. Mở lại conversation/output/QuizAttempt đã lưu, chỉ ra evidence cho các Auth flow và đủ năm transactional email. Giải thích một yêu cầu xuyên qua thiết kế, mã nguồn và kiểm thử, refactor đã làm, kết quả đánh giá AI và cách khôi phục dữ liệu. Thực hiện hoặc phân tích chính xác thay đổi nhỏ giảng viên đưa; chỉ rõ phần AI hỗ trợ và quyết định của bản thân.

<a id="lr-29"></a>

2. **Lập kế hoạch áp dụng AI trong 30 ngày.** Chọn một quy trình công việc thực tế, ghi hiện trạng, chỉ số đo, mục tiêu, các mốc ngày 7/14/30 và rủi ro. Nêu cách thu dữ liệu, điều kiện tiếp tục hoặc dừng. Đây là bản kế hoạch cần nộp, không yêu cầu làm thêm 30 ngày để hoàn thành khóa.

### 12.3 Điều kiện hoàn thành

- Demo hành trình có Auth, Notebook, Document/Chat, Note, Summary và Quiz; mở kết quả đã lưu và kiểm một tình huống lỗi/quyền.
- Chỉ ra evidence của đủ năm email và các nhánh Auth, quản lý Output, lifecycle và bảo mật; không cần chạy lại mọi test trong thời gian bảo vệ.
- Truy được yêu cầu đến thiết kế/code/test/tag; giải thích refactor, đánh giá AI, restore và CR R1.1, cùng giới hạn đã ghi.
- Tự xử lý hoặc phân tích chính xác thay đổi nhỏ được giao; có kế hoạch áp dụng AI 30 ngày với chỉ số và điều kiện kiểm.

### 12.4 Áp dụng SDLC và AI

**Kiến thức áp dụng:**

- Demo theo hành trình người dùng và giải thích quyết định kỹ thuật.
- Truy từ yêu cầu đến thiết kế, mã nguồn, test và phiên bản phát hành.
- Đánh giá hiệu quả ứng dụng AI bằng chất lượng, thời gian và rủi ro.

| Phần bảo vệ | Kết quả ứng dụng vào Running Project |
| --- | --- |
| Demo sản phẩm | Chứng minh các chức năng nối thành hành trình người dùng, giữ quyền và dữ liệu. |
| Giải thích một yêu cầu | Mở AC → Figma/API/schema → code → test → bản phát hành; giải thích quyết định và trade-off. |
| Phản biện việc dùng AI | Chỉ ra đề xuất đã giữ/sửa/bác bỏ, căn cứ kiểm độc lập và ảnh hưởng tới sản phẩm. |
| Xử lý thay đổi | Phân tích tác động của yêu cầu mới trên chức năng đã có, chọn test và cách bảo toàn dữ liệu. |

Dùng Claude đóng vai reviewer để luyện phản biện và tìm điểm chưa có minh chứng. Học viên tự demo, giải thích và quyết định; không đọc lại câu trả lời AI để thay vấn đáp. Chuẩn bị dữ liệu mẫu và đường dẫn mở nhanh trong repository.

**Tài liệu dùng cho milestone:** [SRS: tiêu chí nghiệm thu](02_SRS_InsightHub_v1.0.md#sec-4-3); [SRS: bàn giao](02_SRS_InsightHub_v1.0.md#sec-4-4); Figma, API, hướng dẫn vận hành và hồ sơ đã xây dựng trong dự án.

### 12.5 Evidence, cách nộp bài và thời hạn

**Hạn hồ sơ:** trước buổi 10 ít nhất 12 giờ. Gửi link PR `milestone/capstone`, bản ghi nộp bài, tag phát hành đã kiểm, link Figma, hướng dẫn demo, bảng kết quả yêu cầu, kiểm thử, AI và bảo mật và kế hoạch 30 ngày. **Hạn sửa sau bảo vệ:** trong 24 giờ sau khi buổi 10 kết thúc; gửi link cập nhật và danh sách phản hồi đã xử lý. Nếu sửa code, kiểm lại và tạo tag phát hành mới, giữ bản đã bảo vệ.

Chuẩn bị đường dẫn mở nhanh đến evidence đã tích lũy và dữ liệu demo, không biên soạn lại toàn bộ hồ sơ. Demo dùng đúng tag được nộp; phần sửa sau bảo vệ có phiên bản và kết quả kiểm mới theo hạn quy định.

### 12.6 Rubric đánh giá

**Rubric Capstone: 100 điểm, chiếm 35% điểm khóa.** Mỗi tiêu chí nhận 0% khi không có minh chứng hoặc vi phạm nghiêm trọng hành vi cần đánh giá; 40% khi mới làm một phần, chưa đạt mô tả cốt lõi; 70% khi đạt đầy đủ cột cốt lõi; 100% khi đạt thêm cột đầy đủ. Điểm bằng điểm tối đa nhân tỷ lệ, cộng các dòng rồi chia 10 để có điểm Capstone trên thang 10. Ví dụ: tiêu chí tối đa 10 điểm đạt cốt lõi nhận 7 điểm.

| Tiêu chí | Điểm tối đa | Đạt cốt lõi (70%) | Đầy đủ (100%) |
| --- | --- | --- | --- |
| Phạm vi và kế hoạch | 5 | Mục tiêu, phạm vi và backlog nhất quán với phần cần bổ sung vào starter; PR đã tự review, CI đúng phiên bản; trách nhiệm với AI rõ | Ưu tiên và phụ thuộc hợp lý; kế hoạch cập nhật theo kết quả thực tế; giải thích được cách xử lý phát hiện review |
| Đặc tả và truy vết yêu cầu | 10 | Tiêu chí chấp nhận có luồng chính và ngoại lệ; yêu cầu phi chức năng có cách đo; công việc, ước lượng và test case liên kết được; thử tích hợp ghi rõ phần đã/chưa kiểm | Truy từ yêu cầu đến test và từ test về yêu cầu; xử lý giả định quan trọng; cập nhật bảng truy vết sau thay đổi |
| Thiết kế giao diện, API và dữ liệu | 10 | Figma, API, từ điển dữ liệu, phiên bản cấu trúc và quyền sở hữu nhất quán; quyết định kiến trúc có phương án và căn cứ; có thiết kế migration và trạng thái lỗi | Triển khai khớp thiết kế hoặc giải thích khác biệt; kiểm hai kích thước/bàn phím; liên kết quyết định thiết kế với yêu cầu và test |
| Chức năng và TDD | 12 | Auth, năm transactional email, Notebook, Document/Chat, Note, Summary, Quiz và AI Output hoạt động qua các lớp tích hợp tương ứng; tiêu chí bắt buộc đạt; có test thất bại trước sửa rồi đạt sau sửa; xử lý trạng thái và lỗi | Tái chạy được bản nộp; mọi tiêu chí áp dụng có minh chứng; giải thích ranh giới mô phỏng; dữ liệu còn sau khởi động lại, thao tác lặp đúng |
| Refactor và tự động hóa | 8 | Có test ghi nhận hành vi module trước thay đổi; diff đúng phạm vi, hồi quy giữ quy tắc nghiệp vụ; tác vụ tự động thực chạy và giới hạn rõ | So sánh trước/sau chứng minh cải thiện; chạy lại từ checkpoint hoặc khôi phục; mọi thay đổi hành vi có căn cứ yêu cầu |
| Kiểm thử và nghiệm thu | 8 | Chọn tầng test theo yêu cầu/rủi ro; nghiệm thu có kỳ vọng và thực tế; lỗi quan trọng được kiểm lại; điều kiện đo rõ | Người khác chạy lại được; phân tích thiếu sót và test không ổn định; chứng minh test bắt lỗi và truy vết đầy đủ trên bản nộp |
| Chất lượng nội dung AI | 7 | Đủ 12 lượt nội dung cho hỏi đáp/Tóm tắt và Quiz; đối chiếu ý và nguồn; ghi mô hình, dữ liệu, phiên bản và cả lượt lỗi; thiếu căn cứ/chỉ dẫn gây nhiễu/ngoại lệ được xử lý đúng | Tái lập cấu hình và nguồn; đánh giá cả lượt lặp; giải thích sai lệch, kết luận và kiểm lại; không dùng AI tự chấm làm căn cứ duy nhất |
| Bảo mật ứng dụng | 10 | Có mô hình đe dọa, quét và danh mục thành phần; kiểm hai tài khoản trên từng tài nguyên; kiểm phiên và nội dung độc hại, sửa và kiểm lại; không còn lỗi chặn phát hành | Tái hiện test case bị từ chối qua API, nguồn và bộ nhớ đệm, sau xóa và hết phiên; đánh giá tác động có căn cứ và chứng minh lỗi không tái phát |
| An toàn quy trình AI | 5 | Giới hạn quyền công cụ hoặc MCP, dữ liệu và secret; thử một tình huống bị chặn; có người kiểm và log đã lọc | Tái hiện dừng và khôi phục từ checkpoint; giải thích cách xử lý chỉ dẫn độc hại và chỉ cấp quyền cần cho tác vụ |
| Phát hành và khôi phục | 5 | Có version/tag/checksum; cài sạch, kiểm luồng chính, nâng cấp và restore cách ly dữ liệu đầy đủ; hướng dẫn sử dụng/xử lý lỗi rõ | Người khác tái cài được theo hướng dẫn; kiểm nội dung và quyền sau restore; giải thích giới hạn và cách quay lại bản trước |
| Thay đổi sau phát hành | 5 | Có thay đổi sau R1, phân tích tác động đến yêu cầu, thiết kế, dữ liệu và kiểm thử; bản cập nhật, ghi chú phát hành và hồi quy đúng phạm vi | Tái hiện trước/sau; giải thích rủi ro và cách quay lại; cập nhật truy vết, không gây hồi quy hoặc mất dữ liệu |
| Demo và vấn đáp | 10 | Tự demo chức năng và ngoại lệ; truy một yêu cầu qua mã nguồn và kiểm thử; giải thích quyết định/refactor; thực hiện hoặc phân tích đúng một thay đổi nhỏ | Xử lý được tình huống biến đổi giảng viên đưa; chẩn đoán từ minh chứng, bảo vệ lựa chọn và chỉ rõ giới hạn |
| Kế hoạch áp dụng 30 ngày | 5 | Chọn một quy trình công việc, có số liệu hiện trạng/chỉ số đo, trách nhiệm cá nhân, mốc ngày 7/14/30 và rủi ro | Kế hoạch khả thi; cách thu dữ liệu và điều kiện tiếp tục/dừng rõ, dựa trên bài học trong dự án |
| **Tổng** | **100** | | |

Các nhóm tiêu chí giữ cơ cấu điểm của chương trình: yêu cầu/kế hoạch 15; thiết kế 10; triển khai và tự động hóa 20; kiểm thử/chất lượng AI 15; bảo mật 15; phát hành/bảo trì 10; vấn đáp/kế hoạch áp dụng 15. Không lấy điểm Assignment thay cho đánh giá refactor trong bản sản phẩm cuối. Lỗi lộ dữ liệu chéo, chiếm quyền hoặc mất dữ liệu nghiêm trọng chưa sửa khiến tiêu chí bảo mật tương ứng nhận 0 và sản phẩm chưa đủ điều kiện bàn giao.

Giữ cơ cấu đánh giá theo giai đoạn SDLC. Mỗi tiêu chí phải được giải thích bằng chức năng hoặc quyết định thực tế của InsightHub; hình thức trình bày không thay kết quả chạy và khả năng bảo vệ cá nhân.

<a id="data-api"></a>

## 13. Thiết kế dữ liệu, schema, API và tích hợp

Phần này hướng dẫn chuyển yêu cầu của [SRS](02_SRS_InsightHub_v1.0.md) thành thiết kế và kiểm chứng cho bài tập Tóm tắt và Quiz. Các đầu ra được lưu trong hồ sơ LR-11 và sử dụng tiếp khi phát triển; không tạo thêm Assignment hoặc bài nộp riêng.

### 13.1. Phân biệt yêu cầu, thiết kế và phần nền

| Lớp thông tin | Nội dung đã được xác định | Phần học viên cần quyết định |
| --- | --- | --- |
| SRS | Hành vi, dữ liệu logic, quan hệ, quyền, trạng thái, giới hạn và điều kiện chấp nhận. | Giải pháp thực hiện phải giữ các ràng buộc này; không tự đổi nghiệp vụ theo mặc định thư viện. |
| Hợp đồng tham khảo | Một phương án OpenAPI, JSON Schema, dữ liệu mẫu và tình huống kiểm ngoài schema. | Chọn phần phù hợp, điều chỉnh cho phạm vi bài tập và giải thích thay đổi thiết kế. |
| API Starter | Giao tiếp và dữ liệu của phần nền được cung cấp. | Xác định nơi cần mở rộng, chuyển đổi hoặc bọc tích hợp; kiểm hồi quy phần bị ảnh hưởng. |
| Thiết kế bài làm | API, cấu trúc lưu trữ, giao dịch, bảo mật và migration của giải pháp cá nhân. | Học viên chịu trách nhiệm hoàn thiện, thực thi và kiểm chứng. |

Không bắt buộc một bảng cơ sở dữ liệu cho mỗi đối tượng logic. Một đối tượng có thể được lưu trong nhiều bảng, một trường có thể suy ra, hoặc dữ liệu xác thực có thể do dịch vụ quản lý. Thiết kế phải giải thích nơi thực thi từng quy tắc và chứng minh hành vi còn đúng sau khởi động lại.

### 13.2. Đầu ra thiết kế tại LR-11

#### 13.2.1. Mô hình và từ điển dữ liệu

Đọc SRS mục 3.7, đặc biệt 3.7.3 và 3.7.7-3.7.9. Xác định các đối tượng thuộc bài tập: người dùng, danh tính, phiên, Notebook, tài liệu, lần xử lý tài liệu, hội thoại, lượt hỏi đáp, ghi chú, tác vụ tạo nội dung, kết quả AI, lần làm Quiz, tham chiếu nguồn, bản ghi thao tác và dữ liệu vận hành cần thiết.

Với mỗi đối tượng, ghi các trường cần lưu hoặc suy ra; kiểu dữ liệu; điều kiện bắt buộc; mặc định; giới hạn; nguồn tạo; quyền đọc, sửa; trạng thái và chính sách xóa. Sơ đồ quan hệ phải thể hiện số lượng liên kết và chủ sở hữu. Mô tả các điều kiện phải luôn đúng, chẳng hạn một lần làm Quiz chỉ thuộc một đề, chủ sở hữu tài nguyên con phải phù hợp với Notebook và một tác vụ thành công chỉ tạo một kết quả.

| Tình huống | Điều phải phân biệt trong thiết kế |
| --- | --- |
| Trường không có, `null`, chuỗi rỗng hoặc số 0 | Không dùng thay nhau. Trường không áp dụng phải tuân hợp đồng; ghi chú được phép có nội dung rỗng, điểm chưa nộp không được biểu diễn bằng điểm 0. |
| Dữ liệu do máy chủ quản lý | Chủ sở hữu, trạng thái, thời điểm, điểm Quiz và phiên bản không được nhận từ client để tự cấp quyền hoặc xác lập kết quả. |
| Kết quả AI | Nội dung đã sinh bất biến; đổi tên chỉ đổi `display_name` và `metadata_version`. `schema_version` xác định cấu trúc nội dung, không phải số lần đổi tên. |
| Quiz | Cấu trúc lưu nội bộ có đáp án; phản hồi trước khi nộp chỉ có câu hỏi và lựa chọn. Lần đã nộp có lựa chọn, điểm, thời điểm và quyền xem giải thích. |
| Nguồn đã xóa | Nội dung kết quả lịch sử được giữ theo BR-08, nhưng tham chiếu không được trả đoạn trích hoặc vị trí để đọc lại nguồn đã xóa. |
| Bản ghi chống gửi lặp | Có thời hạn riêng; xóa bản ghi kỹ thuật không làm mất hội thoại, kết quả AI hoặc lần làm Quiz. |

#### 13.2.2. API và schema trao đổi

Mô tả đầu vào, phản hồi thành công, lỗi, phiên, quyền, phân trang, phiên bản cập nhật và cách đọc trạng thái. Xác định schema nào dùng khi nhận yêu cầu, kiểm đầu ra mô hình, trả dữ liệu công khai và lưu nội bộ. Không đưa đối tượng nội bộ chứa đáp án Quiz thẳng vào phản hồi API.

Máy chủ chọn cặp `(tool_type, schema_version)` từ cấu hình được hỗ trợ, không tin phiên bản do mô hình tự khai. Khi đọc nội dung lưu có phiên bản chưa hỗ trợ, trả lỗi an toàn và giữ dữ liệu; không tự đổi cách hiểu hoặc xóa dữ liệu. Nếu phát hành cấu trúc mới, chọn bộ đọc tương thích hoặc migration có kiểm chứng cho các phiên bản đang lưu.

Ví dụ hợp lệ và không hợp lệ phải bao phủ những nhánh đang thiết kế: thiếu trường, sai kiểu, trường thừa, phiên bản không hỗ trợ, sai trạng thái và dữ liệu ngoài quyền. JSON Schema kiểm hình dạng; quan hệ nguồn, quyền, số từ, đáp án thuộc lựa chọn, điểm và thứ tự xóa/công bố cần kiểm ở lớp nghiệp vụ.

#### 13.2.3. Giao dịch và vòng đời

Mô tả cách tiếp nhận nhất quán giữa bản ghi thao tác, dữ liệu nghiệp vụ, bộ đếm và tác vụ đang chạy. Giải thích cách ngăn hai yêu cầu cùng vượt hạn mức, cùng nộp một lần Quiz hoặc cùng công bố kết quả trùng.

Thiết kế cần xử lý ba thứ tự BR-08: xóa hoàn tất trước công bố; công bố hoàn tất trước xóa; phản hồi đến sau khi trình duyệt đã biết nguồn bị xóa. Thứ tự được xác lập bằng giao dịch trên máy chủ, không bằng thời điểm nhấn nút. Xóa Notebook chặn toàn bộ tài nguyên con, kể cả lịch sử đã lưu.

Lưu thời hạn tuyệt đối của tác vụ. Sau khởi động lại, tác vụ còn hạn chỉ được dùng phần thời gian còn lại; tác vụ hết hạn phải kết thúc trước khi chạy tiếp hoặc được trả như một tác vụ đang chạy hợp lệ. Kết thúc tác vụ giải phóng suất đồng thời nhưng không hoàn lại lượt đã tính trong cửa sổ tần suất.

#### 13.2.4. Minh chứng và quyết định

Trong cùng hồ sơ M2, lưu sơ đồ quan hệ, từ điển dữ liệu, OpenAPI, ví dụ, kế hoạch migration và ít nhất một ADR. Hồ sơ quyết định nêu yêu cầu chi phối, hai phương án, đánh đổi, lựa chọn và cách kiểm. Gắn thiết kế với mã yêu cầu và điều kiện kiểm trong bảng truy vết; không chỉ nộp ảnh sơ đồ không có giải thích.

### 13.3. Sử dụng API contract tham khảo

[API contract tham khảo](03_API_Schema_Reference_v1.0.zip) mô tả toàn sản phẩm năm công cụ. Trong bài tập, chọn các phần dùng chung cùng Tóm tắt và Quiz theo bảng phạm vi. Không triển khai ba công cụ ngoài bài tập chỉ vì chúng xuất hiện trong `schemas.json` hoặc OpenAPI.

Học viên có thể sử dụng cấu trúc tham khảo hoặc chọn cách biểu diễn khác nếu giữ hành vi SRS. Giải nén gói kỹ thuật ngay trong thư mục chứa Requirements để tạo thư mục `API_Schema_Reference`. `openapi.json`, `schemas.json` và `examples.json` là các tệp dùng khi thiết kế; `Domain_Checks.md` bổ sung kiểm tra ngoài schema. Chạy công cụ kiểm theo `README.md` trong gói nếu cần kiểm cấu trúc.

Việc sao chép tệp OpenAPI chưa hoàn thành LR-11: phải giải thích cách áp dụng vào bài làm và kiểm API thực tế khớp thiết kế.

| Điểm tích hợp | API Starter | Hợp đồng tham khảo | Yêu cầu đối với bài làm |
| --- | --- | --- | --- |
| Tiếp nhận tài liệu | `/documents` xử lý đồng bộ, trả HTTP 201 khi tài liệu `Ready`. | Có tiền tố `/api/r1`, trả HTTP 202 sau khi tiếp nhận thao tác và cho đọc trạng thái. | Giữ cách xử lý đồng bộ của Starter làm điểm xuất phát. Nếu chọn đổi sang giao tiếp bất đồng bộ, phải ghi quyết định thiết kế, bổ sung lưu trạng thái và kiểm tích hợp trước khi thay luồng. SRS không bắt buộc một hệ thống hàng đợi riêng. |
| Xác thực và quyền | Chưa có nghiệp vụ Auth và Notebook. | Đề xuất phiên phía máy chủ, cơ chế bảo vệ yêu cầu và tài nguyên theo quyền. | Học viên triển khai xác thực, xác định chủ sở hữu ở máy chủ và kiểm quyền trước mọi thao tác. Thư viện hoặc cơ chế cụ thể phải đáp ứng SRS. |
| Tham chiếu nguồn | Có định danh và cấu trúc phản hồi của nền; nguồn mất hiệu lực có thể được biểu diễn bằng `available: false` và `excerpt: null`. | Nguồn không còn khả dụng bỏ trường vị trí và đoạn trích. | Không giả định hai dạng phản hồi tương thích. Định nghĩa phép chuyển đổi hoặc cập nhật API/giao diện nhất quán; giao tiếp đích tuân quy tắc trường hiện diện tại SRS 3.7.7 và không trả dữ liệu nguồn đã xóa. |
| Lịch sử hỏi đáp | Kết quả phục vụ đối soát có trong bản ghi thao tác. | Có Conversation và ChatTurn tồn tại như dữ liệu nghiệp vụ. | Bổ sung lưu hội thoại độc lập với thời hạn bản ghi thao tác; kiểm đọc lại sau khởi động lại và sau hết thời hạn chống gửi lặp. |
| Chống trùng tài liệu | Phạm vi dữ liệu nền. | Tài liệu thuộc Notebook và người dùng. | Giới hạn chống trùng theo Notebook, kiểm quyền, không để tải cùng tệp làm lộ dữ liệu người khác. |

API Starter và hợp đồng tham khảo là đầu vào thiết kế. Hợp đồng của bài làm phải là nguồn thống nhất giữa Web, API và kiểm thử sau khi học viên chọn phương án. Định danh kỹ thuật, đường dẫn và cách lưu có thể khác; quy tắc nghiệp vụ và các giới hạn SRS vẫn giữ nguyên.

<a id="tich-hop-starter"></a>

### 13.4. Quyền sở hữu và nhập dữ liệu nền

Máy chủ suy ra người dùng từ phiên hợp lệ, xác định Notebook thật sự chứa đối tượng rồi kiểm quyền. Không sử dụng `owner_id` hoặc Notebook do client tự khai làm bằng chứng cấp quyền. Tập tài liệu được phép phải được xác định trước khi truy xuất, không đợi đến phản hồi mới lọc dữ liệu người khác.

Nếu cần nhập dữ liệu nền chưa có chủ sở hữu, người vận hành chỉ định tài khoản và Notebook đích bằng thao tác có kiểm soát. Kiểm dữ liệu mất liên kết và quan hệ sai chủ sở hữu trước khi đưa vào sử dụng. Không tự gán cho người đăng ký đầu tiên. Đây là nhập dữ liệu nền, không phải chức năng chuyển chủ sở hữu Notebook hoặc chuyển tài nguyên giữa các Notebook.

Migration thực hiện trên dữ liệu đã có, theo hướng tiến tới cấu trúc mới. Có bản sao lưu và phương án phục hồi ứng dụng; không dùng xóa volume để thay cho chuyển đổi dữ liệu. Khóa ngoại, chỉ mục, cách lưu phiên hoặc bộ đếm là quyết định của thiết kế, không phải danh sách bảng bắt buộc do đề bài cung cấp.

**Điểm đọc code trước khi tích hợp:** bảng sau chỉ rõ nền cần mở rộng, không cung cấp lời giải nghiệp vụ. Dùng ADR để chọn cấu trúc cụ thể, giữ hành vi SRS.

| Vị trí Starter | Giới hạn nền hiện tại | Phần học viên tự thiết kế và kiểm |
| --- | --- | --- |
| `api/app/routers/documents.py`, `chat.py` và `operations.py` | Endpoint local chưa có session/Notebook/ownership của bài tập. | Xác lập session phía server và quyền của đúng đối tượng tại mọi đường đọc/ghi, source/citation và reconciliation; thử tài khoản A/B. |
| `api/app/services/retrieval.py` | `ready_document_ids(None)` chọn tài liệu Ready của thư viện chung; danh sách ID chỉ được kiểm trạng thái. | Xác định Notebook/owner và lọc tập nguồn trước retrieval; mặc định lấy snapshot nguồn ở lần tiếp nhận đầu, replay không thêm nguồn mới. |
| `infra/db/init.sql`, `api/app/core/operations.py` | Operation record có TTL và khóa dùng cho replay nền, chưa là Conversation/Output của bài làm. | Thiết kế scope operation/quota và persistence nghiệp vụ; kiểm gửi lặp, restart và dữ liệu còn sau operation TTL. |
| `api/app/core/locks.py`, `api/migrations/` | Có cơ chế khóa và migration nền; chưa thay quy tắc vòng đời toàn bộ child resource của Notebook. | Giữ invariant trước khi mở rộng; migration forward trên dữ liệu có sẵn và kiểm các thứ tự xóa/công bố của SRS. |

Tại M2 xác định module và test baseline; tại M3.1 kiểm phần đến hạn của lát cắt Chat, tại M3 mở rộng cho Summary/Quiz và lifecycle còn lại, M4 kiểm tổng hợp. Không chờ M4 mới viết test quyền hoặc characterization; không yêu cầu hoàn thiện toàn bộ phần mở rộng tại M3.1.

### 13.5. Tình huống dùng để rà thiết kế và kiểm triển khai

| Tình huống | Kết quả phải chứng minh |
| --- | --- |
| Dùng ID đối tượng của tài khoản khác, dù Notebook trong request thuộc tài khoản đang đăng nhập. | Không đọc hoặc thay đổi được tài nguyên; phản hồi không tiết lộ sự tồn tại. |
| Gửi lại cùng mã sau khi thêm nguồn hoặc đổi mặc định. | Cùng tác vụ và cấu hình của lần đầu; không tạo thêm kết quả hoặc tăng lượt sử dụng. |
| Hai yêu cầu mới tranh hạn mức hoặc suất AI. | Chỉ tiếp nhận số lượng được phép; dữ liệu thao tác và hạn mức nhất quán. |
| Nộp cùng lần làm Quiz đồng thời hoặc gửi lại lựa chọn khác sau nộp. | Chỉ chấm và lưu một lần; trả kết quả đã lưu nếu còn quyền. |
| Đổi tên kết quả rồi mở lại; đọc dữ liệu có phiên bản cấu trúc chưa hỗ trợ. | Nội dung và nguồn không đổi; phiên bản chưa hỗ trợ báo lỗi an toàn, giữ dữ liệu. |
| Xóa nguồn, Notebook hoặc hội thoại khi tác vụ chưa công bố; nhận phản hồi muộn. | Hành vi đúng thứ tự BR-08/BR-09 và quyền hiện tại; không tái tạo dữ liệu đã xóa. |
| Khởi động lại trước hoặc sau thời hạn; bản ghi chống gửi lặp hết hiệu lực. | Không đặt lại thời hạn, không mất lịch sử nghiệp vụ và không giữ suất của tác vụ đã kết thúc. |
| Khôi phục bản sao lưu ở môi trường riêng. | Quan hệ, nội dung, phiên bản và quyền được kiểm; ghi rõ phụ thuộc Auth ngoài cơ sở dữ liệu nếu có. |

Các tình huống trên cụ thể hóa tiêu chí đã được giao. Ghi kết quả trong cùng bảng truy vết của LR-20 đến LR-22, không tạo thêm bộ kết luận độc lập. Tham khảo `Domain_Checks.md` trong [gói API/Schema](03_API_Schema_Reference_v1.0.zip), chọn phần thuộc bài tập và kiểm trên sản phẩm thực tế.

### 13.6. Điều kiện để bắt đầu tích hợp

Trước phần phát triển phụ thuộc, học viên cần giải thích được: đối tượng thuộc ai; trường nào được phép đọc hoặc sửa ở từng trạng thái; API nào được giữ hoặc thay; giao dịch nào bảo vệ tính nhất quán; dữ liệu được chuyển đổi ra sao; và dùng phép kiểm nào chứng minh các lựa chọn đó. Ghi điểm chưa có căn cứ cùng bước kiểm tiếp theo để giảng viên hỗ trợ. Không tự suy đoán nghiệp vụ còn chưa rõ từ mã nguồn nền hoặc mặc định của thư viện.

<a id="auth-email"></a>

## 14. Auth, Google và email: thử tích hợp và kiểm chứng

Mục tiêu là chọn giải pháp xác thực có bằng chứng đáp ứng SRS trước khi phát triển phần phụ thuộc. Thử khả thi tại M2.1 tập trung rủi ro của giải pháp; hoàn thiện nghiệp vụ ở M3 và tổng hợp kiểm đầy đủ tại M4. Starter chưa cung cấp nghiệp vụ tài khoản của bài tập.

### 14.1. Chuẩn bị và trách nhiệm

| Đầu vào | Trách nhiệm |
| --- | --- |
| Quyền Google, tài khoản thử và cấu hình nhận kết quả xác thực | Giảng viên hoặc quản trị lớp cấp môi trường được phép. Học viên cấu hình đúng địa chỉ callback của giải pháp đã chọn. |
| Dịch vụ email và hộp thư nhận thử | Lớp cung cấp quyền hoặc phương án sử dụng được phép. Hộp thư mô phỏng tại máy chỉ phục vụ phát triển; phép kiểm thật phải có thư tới hộp thư bên ngoài. |
| Thư viện hoặc dịch vụ xác thực | Học viên so sánh khả năng đăng nhập mật khẩu, Google, xác minh, liên kết danh tính, tái xác thực và thu hồi phiên; ghi phiên bản và phần cần bổ sung. |
| Chính sách nghiệp vụ | Dùng BR-02/BR-03, LIM-01, LIM-07 đến LIM-09, LIM-19 và mục 3.2.4/3.2.6 của [SRS](02_SRS_InsightHub_v1.0.md). Giá trị mặc định của thư viện không thay yêu cầu. |
| Dữ liệu thử | Hai tài khoản độc lập; các trường hợp có mật khẩu, chờ xác minh và chỉ dùng Google. Chỉ sử dụng email được phép và dữ liệu giả. |
| Bí mật cấu hình | Chỉ ghi tên biến trong `.env.example`; giá trị thật ở `.env` hoặc kho bí mật của lớp. Không lưu liên kết xác thực còn hiệu lực vào hồ sơ nộp. |

Trước M2.1, học viên kiểm truy cập các đầu vào được cấp; giảng viên/quản trị lớp xử lý quyền, mạng hoặc tenant thiếu. Học viên vẫn phải cấu hình giải pháp đã chọn và thực hiện spike theo mục 14.2-14.3, rồi xây đầy đủ tại M3. Quyền truy cập dịch vụ không đồng nghĩa nghiệp vụ Auth/email đã được làm sẵn. Không tự mua dịch vụ hoặc gửi dữ liệu ngoài phạm vi được phép để vượt phần bị chặn.

Chọn thành phần xác thực đã có thay vì tự viết thuật toán mật mã. Học viên vẫn chịu trách nhiệm kiểm quyền nghiệp vụ tại máy chủ theo [hướng dẫn tích hợp](#data-api).

### 14.2. Thực hiện theo mốc

| Mốc | Công việc và đầu ra |
| --- | --- |
| M2.1 | Lập bảng yêu cầu, khả năng giải pháp, phần phải bổ sung và phép thử. Chạy luồng Google và gửi/nhận email thật; thử khả năng liên kết tài khoản trùng email, xử lý chờ xác minh, thu hồi phiên. Chưa yêu cầu toàn bộ giao diện hoàn chỉnh. |
| M2 | Chọn phương án qua ADR, ghi ít nhất hai phương án và căn cứ. Thiết kế phiên, danh tính, dữ liệu điều khiển và quyền phù hợp kết quả thử. |
| M3.1 | Tích hợp một Auth flow hợp lệ và session thực cho hành trình Notebook - Document - Chat. Nếu chọn email/mật khẩu, phải có EML-001 và xác minh email; hoàn thiện cả hai phương thức và các email còn lại ở M3. |
| M3 | Hoàn thiện các luồng tài khoản cùng năm email giao dịch; tích hợp với Notebook và giao diện. Ghi kiểm chứng cùng chức năng. |
| M4 | Kiểm đủ điều kiện áp dụng, các trường hợp lỗi, biên thời gian, API trực tiếp, trình duyệt và tích hợp thật. Kiểm lại phần thay đổi sau thử sớm. |

### 14.3. Ma trận hành vi cần kiểm

M2.1 chọn phép thử đủ để quyết định giải pháp ở các rủi ro đã nêu; mọi dòng sau phải được hoàn thiện và có kết quả trước khi kết luận đạt phần xác thực tại M4.

| Tình huống | Kết quả kỳ vọng |
| --- | --- |
| Đăng ký và xác minh email | Tạo `PendingVerification`; liên kết đúng mục đích, có thời hạn và dùng một lần. Chưa xác minh thì không đọc dữ liệu Notebook. |
| Phiên chờ xác minh | Chỉ đọc trạng thái xác minh, gửi lại email hoặc đăng xuất. Luồng khôi phục công khai UC-02.A4 vẫn được sử dụng. |
| Google hợp lệ hoặc callback bị sửa, hết hạn, sai giao dịch hay bị hủy | Máy chủ kiểm bằng chứng của nhà cung cấp và giao dịch. Chỉ trường hợp hợp lệ mới tạo danh tính hoặc phiên phù hợp. |
| Email trùng tài khoản có mật khẩu đang hoạt động | Chỉ liên kết sau khi Google hợp lệ và mật khẩu hiện tại được xác nhận trong cùng giao dịch, tối đa 5 phút và một lần. Email trùng không tự cho phép hợp nhất. |
| Email trùng tài khoản chờ xác minh | Hoàn tất UC-02.A4: đặt mật khẩu mới, vô hiệu mật khẩu, phiên và liên kết cũ trước khi cấp quyền. Sau đó bắt đầu lại Google và xác nhận mật khẩu mới; không tự liên kết từ việc xác minh email. |
| Khôi phục hoặc đổi mật khẩu | Phản hồi công khai không tiết lộ tài khoản tồn tại. Liên kết sai, hết hạn hoặc đã dùng bị từ chối. Thành công thu hồi phiên cũ trong tối đa 60 giây. |
| Tài khoản chỉ dùng Google | Không tự tạo mật khẩu hoặc cấp liên kết đặt mật khẩu; email EML-004 hướng dẫn đăng nhập Google. |
| Hết hạn, đăng xuất, polling và khởi động lại | Phiên hết hạn sau 2 giờ không hoạt động hoặc 24 giờ tuyệt đối. Đọc trạng thái định kỳ không gia hạn; khởi động lại không khôi phục phiên bị thu hồi. |
| Giới hạn thử mật khẩu | Đếm chung đăng nhập và tái xác thực trong cửa sổ trượt 15 phút: tối đa 5 lần sai theo tài khoản và 20 theo IP. Chặn lần tiếp theo khi đạt ngưỡng; lần đúng không xóa lỗi còn hiệu lực, yêu cầu bị chặn không làm tăng bộ đếm. |
| Giới hạn yêu cầu gửi email | Cửa sổ trượt 60 phút: tối đa 3 yêu cầu theo tài khoản và 20 theo IP. Tính lần đã tiếp nhận dù email không có tài khoản phù hợp hoặc gửi thất bại. Email thông báo EML-003/005 và thử lại vận chuyển cùng sự kiện không tính thành yêu cầu mới. |
| Biên cửa sổ và xử lý đồng thời | Sự kiện đúng mốc đầu cửa sổ đã hết hiệu lực. Kiểm cả giới hạn tài khoản/IP và hai yêu cầu đồng thời; khởi động lại không làm mất bộ đếm còn hiệu lực. |
| Gửi lại liên kết | Khi phát hành liên kết mới thành công, liên kết trước cùng mục đích hết hiệu lực. Yêu cầu bị chặn trước phát hành không làm mất hiệu lực liên kết đang dùng. |
| Email lỗi sau thay đổi đã lưu | Ghi trạng thái và mã tra cứu để gửi lại theo chính sách; không hoàn tác liên kết danh tính hoặc mật khẩu, không phục hồi phiên cũ. |
| Quyền qua API trực tiếp | Tài khoản B không đọc, sửa hoặc xóa đối tượng của A khi thay ID. Chủ sở hữu được xác định từ phiên và quan hệ dữ liệu, không từ trường client tự khai. |

Có thể mô phỏng lỗi provider và thời gian để kiểm ngoại lệ; phải ghi rõ chế độ chạy. Không đánh dấu đăng nhập Google hoặc email thật đã đạt chỉ từ kết quả mô phỏng.

### 14.4. Kiểm năm email giao dịch

| Mã | Tình huống | Kết quả cần quan sát |
| --- | --- | --- |
| EML-001 | Đăng ký hoặc gửi lại xác minh | Nhận thư đúng hộp thư, liên kết có hiệu lực đúng quy tắc và hoàn tất xác minh. |
| EML-002 | Khôi phục tài khoản có mật khẩu | Nhận liên kết đặt lại dùng một lần; mật khẩu chỉ thay sau khi hoàn tất thao tác hợp lệ. |
| EML-003 | Liên kết Google thành công | Nhận thông báo và hướng dẫn hỗ trợ; thư không có liên kết cấp quyền. |
| EML-004 | Khôi phục tài khoản chỉ dùng Google | Nhận hướng dẫn đăng nhập Google, không có liên kết tạo mật khẩu. |
| EML-005 | Đặt lại hoặc đổi mật khẩu thành công | Nhận thông báo và hướng dẫn đăng nhập lại; không chứa mật khẩu hoặc liên kết cấp phiên. |

Minh chứng ghi loại thư, tài khoản đã che địa chỉ, thời điểm, mã chuyển giao an toàn, thư thực nhận và kết quả hành động. Nhật ký “dịch vụ đã nhận yêu cầu” chưa chứng minh thư tới hộp thư. Che liên kết và token còn hiệu lực trong ảnh hoặc log.

### 14.5. Hồ sơ và phụ thuộc chưa hoàn tất

Ghi kết quả kỳ vọng, thực tế, chế độ chạy, phiên bản mã nguồn, cấu hình không chứa bí mật và quyết định giải pháp vào hồ sơ LR-09/LR-14. Bảng truy vết ghi từng điều kiện đã kiểm, chưa kiểm hoặc bị chặn.

Nếu thiếu quyền Google, email hoặc kết nối, nêu yêu cầu bị ảnh hưởng, cách đã thử, người cần hỗ trợ và bước kiểm lại. Tiếp tục phần thiết kế, hộp thư mô phỏng và các kiểm thử không phụ thuộc dịch vụ. Không tự bỏ tiêu chí hoặc coi mô phỏng là tích hợp thật; phần phụ thuộc phải được giải quyết trước khi kết luận nghiệm thu.

<a id="pham-vi-truy-vet"></a>

## 15. Phạm vi và truy vết SRS

Bảng này là phạm vi giao bài, không phải kết quả kiểm thử. [SRS InsightHub v1.0](02_SRS_InsightHub_v1.0.md) xác định hành vi sản phẩm; học viên đọc AC cùng yêu cầu thành phần, quy tắc, giới hạn và dữ liệu được dẫn. Việc cần làm và rubric nằm tại mục 3-12 của tài liệu này. Mã LR chỉ dùng để truy vết trong bảng này; danh mục bên dưới dẫn đến đúng công việc, học viên không cần ghi nhớ mã.

### 15.1. Quy tắc phạm vi

Có **72 mã yêu cầu gốc hoặc nhóm yêu cầu và 163 tiêu chí chấp nhận (AC)** được truy vết. Trong đó, **66 mã gốc với 151 AC thuộc bài tập**, **6 mã gốc với 12 AC ngoài bài tập**. SRS phân rã 39 nhóm thành 169 yêu cầu thành phần và giữ 33 yêu cầu trực tiếp; mã gốc không đồng nghĩa một nghĩa vụ đơn nhất. AC điều chỉnh vẫn thuộc 151 AC phải kiểm. Đây là số AC được giao, không phải số test case hoặc số AC đã đạt.

| Mã | Cách áp dụng |
| --- | --- |
| A | Giữ hành vi, giới hạn và ngoại lệ đối với các đối tượng thuộc bài tập. Có 136 tiêu chí thuộc nhóm này. |
| D1 | Danh mục công cụ, cấu hình, schema, nguồn, API và lọc theo loại chỉ áp dụng Tóm tắt và Quiz. Bỏ nhánh riêng của Mindmap, Slide và Báo cáo; giữ yêu cầu về dữ liệu, nguồn, trạng thái và an toàn. |
| D2 | Thiết kế Figma và màn hình UI-01 đến UI-08 có đầy đủ hành trình Tóm tắt và Quiz; không phải triển khai ba công cụ mở rộng. Giữ trạng thái, kích thước hiển thị, thao tác bàn phím và các tiêu chí trải nghiệm khác. |
| D3 | Kiểm tích hợp và nội dung AI thật cho hỏi đáp, Tóm tắt và Quiz: AEV-01, AEV-03, AEV-05 cùng hai lượt lặp, tổng 12 lượt nội dung. Google và email vẫn kiểm bằng dịch vụ thật. |
| D4 | Nghiệm thu R1 của bài tập hai công cụ, với 151 AC áp dụng và phần tương ứng trong UAT-01 đến UAT-21. Không kết luận đạt toàn bộ sản phẩm năm công cụ. |
| N | Ngoài bài tập bắt buộc: Mindmap, Slide và Báo cáo. Ghi ngoài phạm vi (`OutOfScope`), không ghi đạt. Nếu tự làm thêm, bổ sung kiểm thử và đánh giá AI riêng. |

Các nhóm D1-D4 gồm 15 tiêu chí và đã nằm trong tổng 151 tiêu chí áp dụng; không phải phần được miễn kiểm. Các quy tắc nghiệp vụ, giới hạn, use case, dữ liệu, yêu cầu phi chức năng và thông báo vẫn áp dụng cho phần được giao. Giữ đủ năm email EML-001 đến EML-005, xác thực, quyền, các lần làm Quiz và ngoại lệ.

- UAT-11 kiểm Tóm tắt, Quiz và vòng đời kết quả; không yêu cầu ba công cụ mở rộng.
- UAT-15 kiểm màn hình UI-01 đến UI-08 trong phạm vi D2. UAT-14, UAT-20 và AEV-07 kiểm cấu trúc Tóm tắt và Quiz cùng các ngoại lệ liên quan.
- AEV-02, AEV-04 và AEV-06 ngoài bài tập. AEV-08 giữ bốn tình huống đại diện; không thay kiểm quyền của từng loại tài nguyên.
- Giới hạn 1-3 nguồn của LIM-05 áp dụng cho công cụ AI. Hỏi đáp không chỉ định nguồn sử dụng tập tài liệu `Ready` của Notebook tại lần tiếp nhận đầu theo BR-05 và IH-CHAT-001.
- Mỗi AC có kết luận riêng dù dùng chung test case. Liên kết UAT chỉ dẫn tới kịch bản tổng hợp, không thay điều kiện kiểm chi tiết.

### 15.2. Từ yêu cầu học tập tới năng lực và rubric

Mã khóa học, đơn vị và chủ đề có tiền tố B2BC07. PLO là chuẩn đầu ra chương trình, CLO là chuẩn đầu ra khóa học; các mã theo chương trình được giảng viên cung cấp. Một dòng có khoảng LR áp dụng cho từng công việc trong khoảng đó.

| Công việc | Chuẩn đầu ra chương trình/khóa học | Đơn vị/chủ đề | Đầu ra | Nhóm đánh giá |
| --- | --- | --- | --- | --- |
| LR-01..03 | PLO-1 / C01-CLO-1,2 | C01-U01 T01-T04 | Môi trường, prompt và kết quả kiểm AI | Kiểm chứng đầu ra AI |
| LR-04..05 | PLO-1 / C01-CLO-3,4 | C01-U02 T01-T04 | Hướng dẫn AI và quy trình agent | Quy trình agent và kiểm soát quyền |
| LR-06..07 | PLO-1 / C02-CLO-1 | C02-U01 T01-T04 | Hồ sơ dự án, backlog và CI | Phạm vi và kế hoạch |
| LR-08..09 | PLO-2 / C02-CLO-2 | C02-U02 T01-T04 | Yêu cầu, test case và thử tích hợp | Đặc tả và truy vết yêu cầu |
| LR-10..11 | PLO-3 / C02-CLO-3 | C02-U03 T01-T04 | Figma, API, dữ liệu và quyết định kiến trúc | Thiết kế giao diện, API và dữ liệu |
| LR-12..13 | PLO-4 / C02-CLO-4 | C02-U04 T01-T04 | Hành trình Auth - Notebook - Document - Chat và TDD | Chức năng và TDD |
| LR-14..18 | PLO-4 / C02-CLO-4 | C02-U04 T05-T08 | Đủ Auth, Email, Notebook/Document/Conversation/Note, Summary, Quiz và AI Output | Chức năng sản phẩm |
| LR-19 | PLO-4 / C02-CLO-4 | C02-U04 T05-T08 | Module refactor và tác vụ tự động | Refactor, tự động hóa và Assignment |
| LR-20..22 | PLO-5 / C02-CLO-5 | C02-U05 T01-T08 | Kết quả test và nghiệm thu | Kiểm thử, nghiệm thu và phân quyền |
| LR-23 | PLO-5 / C02-CLO-5 | C02-U05 T01-T08 | Nguồn, kỳ vọng và kết quả AI | Chất lượng nội dung AI |
| LR-24 | PLO-1,5 / C01-CLO-4, C02-CLO-5 | C02-U05 T01-T08 | Mô hình đe dọa, scan và kiểm bảo mật | Bảo mật ứng dụng và quy trình AI |
| LR-25..26 | PLO-6 / C02-CLO-6 | C02-U06 T01-T04 | Bản phát hành, runbook và restore | Phát hành và khôi phục |
| LR-27 | PLO-6 / C02-CLO-6 | C02-U06 T01-T04 | Hồ sơ thay đổi và hồi quy | Thay đổi sau phát hành |
| LR-28 | PLO-1..6 / C02-CLO-1..6 | C02-U07 T01-T04 | Demo và vấn đáp | Demo và vấn đáp |
| LR-29 | PLO-6 / C02-CLO-6 | C02-U07 T01-T04 | Kế hoạch áp dụng 30 ngày | Kế hoạch áp dụng 30 ngày |

LR-01 đến LR-11 là chuẩn bị, phân tích và thiết kế; LR-20..24 kiểm các AC đã triển khai ở LR-12..18. Vì vậy một AC có thể tham chiếu thêm nhiều LR trong bảng truy vết bài làm. Các hoạt động Foundation, TDD, refactor và vấn đáp không bị ép thành yêu cầu sản phẩm mới.

Mã LR là công việc học tập; mã IH là yêu cầu sản phẩm; AC là tiêu chí chấp nhận; UAT là kịch bản nghiệm thu tổng hợp; AEV là test case đánh giá AI. Các mã phục vụ tra cứu, không thay nội dung nhiệm vụ.

#### 15.2.1. Tra công việc theo mã truy vết

| Mã trong bảng | Milestone | Việc cần làm |
| --- | --- | --- |
| LR-01 | M0.1 | [Khởi động starter](#lr-01) |
| LR-02 | M0.1 | [Tạo đầu ra có cấu trúc](#lr-02) |
| LR-03 | M0.1 | [Phát hiện và sửa một lỗi AI](#lr-03) |
| LR-04 | M0.2 | [Viết quy tắc dùng AI cho dự án](#lr-04) |
| LR-05 | M0.2 | [Thực hành một quy trình agent có dùng công cụ hoặc MCP](#lr-05) |
| LR-06 | M1 | [Lập hồ sơ dự án và backlog](#lr-06) |
| LR-07 | M1 | [Thiết lập quy trình phát triển](#lr-07) |
| LR-08 | M2.1 | [Lập bảng yêu cầu và test case](#lr-08) |
| LR-09 | M2.1 | [Thử tích hợp trước khi chốt thiết kế](#lr-09) |
| LR-10 | M2 | [Thiết kế Figma](#lr-10) |
| LR-11 | M2 | [Thiết kế API và dữ liệu](#lr-11) |
| LR-12 | M3.1 | [Triển khai Auth - Notebook - Document - Chat](#lr-12) |
| LR-13 | M3.1 | [Thực hiện TDD cho một hành vi có rủi ro](#lr-13) |
| LR-14 | M3 | [Hoàn thiện Auth và năm transactional email](#lr-14) |
| LR-15 | M3 | [Hoàn thiện Notebook, Document, Conversation và Note](#lr-15) |
| LR-16 | M3 | [Xây dựng Tóm tắt](#lr-16) |
| LR-17 | M3 | [Xây dựng Quiz](#lr-17) |
| LR-18 | M3 | [Hoàn thiện vòng đời công cụ AI](#lr-18) |
| LR-19 | M3 | [Refactor một module và tự động hóa một tác vụ](#lr-19) |
| LR-20 | M4 | [Kiểm toàn bộ phạm vi bài tập](#lr-20) |
| LR-21 | M4 | [Kiểm giao diện và hiệu năng](#lr-21) |
| LR-22 | M4 | [Kiểm phân quyền và vòng đời dữ liệu](#lr-22) |
| LR-23 | M4 | [Đánh giá AI bằng mô hình thật](#lr-23) |
| LR-24 | M4 | [Kiểm bảo mật và sửa lỗi](#lr-24) |
| LR-25 | M5 | [Phát hành bản R1 của bài tập](#lr-25) |
| LR-26 | M5 | [Kiểm nâng cấp và khôi phục dữ liệu](#lr-26) |
| LR-27 | M5 | [Thực hiện một thay đổi sau R1](#lr-27) |
| LR-28 | Capstone | [Demo và bảo vệ cá nhân](#lr-28) |
| LR-29 | Capstone | [Lập kế hoạch áp dụng AI trong 30 ngày](#lr-29) |

### 15.3. Trách nhiệm kế thừa và phát triển

| Nhóm | Trách nhiệm |
| --- | --- |
| AUTH, NB, NOTE, SUM, QUIZ, OUT; CHAT-004 | Học viên xây nghiệp vụ giao diện, API, cơ sở dữ liệu và kiểm đầy đủ. |
| DOC; CHAT còn lại; nền thao tác và tích hợp dịch vụ | Giảng viên cung cấp nền; học viên tích hợp Notebook, quyền sở hữu, hạn mức, vòng đời và kiểm hồi quy phần bị ảnh hưởng. |
| AI, DATA, INT | Sử dụng điểm mở rộng của nền; học viên thiết kế dữ liệu, chính sách và tích hợp xác thực, email, Tóm tắt, Quiz. |
| UX, MSG | Học viên thiết kế và triển khai giao diện, thông báo và email; minh chứng thể hiện cả hành vi và trạng thái. |
| NFR, REL | Học viên kiểm trên bản cuối, cập nhật kiểm thử, vận hành, sao lưu và gói bàn giao theo dữ liệu bài làm. |

### 15.4. Danh mục từng AC

Cột mốc ghi thời điểm hoàn thiện và kiểm tổng hợp của AC. Phần triển khai trước đó, gồm hành trình M3.1, được xác định tại [ma trận chức năng](#ma-tran-chuc-nang); các bước chuẩn bị không bị bỏ qua chỉ vì không xuất hiện trong cột mốc. Tại M2.1, rà đầy đủ phạm vi và phân tích sâu yêu cầu đại diện; tại M2, hoàn thiện thiết kế; khi phát triển và xử lý thay đổi, cập nhật cùng bảng truy vết. Dùng danh mục dưới đây làm khung, thêm mã yêu cầu thành phần, điều kiện kiểm và liên kết kết quả theo [mẫu kết quả](#bang-ket-qua). Mỗi AC có kết luận tổng hợp riêng, chỉ đạt khi mọi điều kiện áp dụng đều đạt. Không ghi đạt cho điều kiện chưa chạy.

| Mã yêu cầu gốc | Tiêu chí chấp nhận | Phạm vi | Công việc hoàn thiện | Mốc hoàn thiện/kiểm tổng hợp | Nghiệm thu liên quan |
| --- | --- | --- | --- | --- | --- |
| IH-AUTH-001 | IH-AUTH-001-AC01 | A | LR-14 | M3 → M4 | UAT-01 |
| IH-AUTH-001 | IH-AUTH-001-AC02 | A | LR-14 | M3 → M4 | UAT-01 |
| IH-AUTH-002 | IH-AUTH-002-AC01 | A | LR-14 | M3 → M4 | UAT-01, UAT-03 |
| IH-AUTH-002 | IH-AUTH-002-AC02 | A | LR-14 | M3 → M4 | UAT-01, UAT-03 |
| IH-AUTH-003 | IH-AUTH-003-AC01 | A | LR-14 | M3 → M4 | UAT-01 |
| IH-AUTH-003 | IH-AUTH-003-AC02 | A | LR-14 | M3 → M4 | UAT-01 |
| IH-AUTH-004 | IH-AUTH-004-AC01 | A | LR-14 | M3 → M4 | UAT-02 |
| IH-AUTH-004 | IH-AUTH-004-AC02 | A | LR-14 | M3 → M4 | UAT-02 |
| IH-AUTH-005 | IH-AUTH-005-AC01 | A | LR-14 | M3 → M4 | UAT-02, UAT-03 |
| IH-AUTH-005 | IH-AUTH-005-AC02 | A | LR-14 | M3 → M4 | UAT-02, UAT-03 |
| IH-AUTH-005 | IH-AUTH-005-AC03 | A | LR-14 | M3 → M4 | UAT-02, UAT-03 |
| IH-AUTH-005 | IH-AUTH-005-AC04 | A | LR-14 | M3 → M4 | UAT-02, UAT-03 |
| IH-AUTH-006 | IH-AUTH-006-AC01 | A | LR-14 | M3 → M4 | UAT-03 |
| IH-AUTH-006 | IH-AUTH-006-AC02 | A | LR-14 | M3 → M4 | UAT-03 |
| IH-AUTH-007 | IH-AUTH-007-AC01 | A | LR-14 | M3 → M4 | UAT-03 |
| IH-AUTH-007 | IH-AUTH-007-AC02 | A | LR-14 | M3 → M4 | UAT-03 |
| IH-AUTH-007 | IH-AUTH-007-AC03 | A | LR-14 | M3 → M4 | UAT-03 |
| IH-AUTH-008 | IH-AUTH-008-AC01 | A | LR-14 | M3 → M4 | UAT-04 |
| IH-AUTH-008 | IH-AUTH-008-AC02 | A | LR-14 | M3 → M4 | UAT-04 |
| IH-AUTH-009 | IH-AUTH-009-AC01 | A | LR-14 | M3 → M4 | UAT-04 |
| IH-AUTH-009 | IH-AUTH-009-AC02 | A | LR-14 | M3 → M4 | UAT-04 |
| IH-AUTH-010 | IH-AUTH-010-AC01 | A | LR-14 | M3 → M4 | UAT-03 |
| IH-AUTH-010 | IH-AUTH-010-AC02 | A | LR-14 | M3 → M4 | UAT-03 |
| IH-NB-001 | IH-NB-001-AC01 | A | LR-15 | M3 → M4 | UAT-05 |
| IH-NB-001 | IH-NB-001-AC02 | A | LR-15 | M3 → M4 | UAT-05 |
| IH-NB-002 | IH-NB-002-AC01 | A | LR-15 | M3 → M4 | UAT-05 |
| IH-NB-002 | IH-NB-002-AC02 | A | LR-15 | M3 → M4 | UAT-05 |
| IH-NB-003 | IH-NB-003-AC01 | A | LR-15 | M3 → M4 | UAT-12 |
| IH-NB-003 | IH-NB-003-AC02 | A | LR-15 | M3 → M4 | UAT-12 |
| IH-NB-004 | IH-NB-004-AC01 | A | LR-15 | M3 → M4 | UAT-13 |
| IH-NB-004 | IH-NB-004-AC02 | A | LR-15 | M3 → M4 | UAT-13 |
| IH-DOC-001 | IH-DOC-001-AC01 | A | LR-15 | M3 → M4 | UAT-06 |
| IH-DOC-001 | IH-DOC-001-AC02 | A | LR-15 | M3 → M4 | UAT-06 |
| IH-DOC-002 | IH-DOC-002-AC01 | A | LR-15 | M3 → M4 | UAT-06 |
| IH-DOC-002 | IH-DOC-002-AC02 | A | LR-15 | M3 → M4 | UAT-06 |
| IH-DOC-003 | IH-DOC-003-AC01 | A | LR-15 | M3 → M4 | UAT-07 |
| IH-DOC-003 | IH-DOC-003-AC02 | A | LR-15 | M3 → M4 | UAT-07 |
| IH-DOC-004 | IH-DOC-004-AC01 | A | LR-15 | M3 → M4 | UAT-07 |
| IH-DOC-004 | IH-DOC-004-AC02 | A | LR-15 | M3 → M4 | UAT-07 |
| IH-DOC-005 | IH-DOC-005-AC01 | A | LR-15 | M3 → M4 | UAT-06, UAT-08, UAT-12 |
| IH-DOC-005 | IH-DOC-005-AC02 | A | LR-15 | M3 → M4 | UAT-06, UAT-08, UAT-12 |
| IH-DOC-006 | IH-DOC-006-AC01 | A | LR-15 | M3 → M4 | UAT-12 |
| IH-DOC-006 | IH-DOC-006-AC02 | A | LR-15 | M3 → M4 | UAT-12 |
| IH-CHAT-001 | IH-CHAT-001-AC01 | A | LR-15 | M3 → M4 | UAT-08 |
| IH-CHAT-001 | IH-CHAT-001-AC02 | A | LR-15 | M3 → M4 | UAT-08 |
| IH-CHAT-002 | IH-CHAT-002-AC01 | A | LR-15 | M3 → M4 | UAT-08 |
| IH-CHAT-002 | IH-CHAT-002-AC02 | A | LR-15 | M3 → M4 | UAT-08 |
| IH-CHAT-003 | IH-CHAT-003-AC01 | A | LR-15 | M3 → M4 | UAT-09 |
| IH-CHAT-003 | IH-CHAT-003-AC02 | A | LR-15 | M3 → M4 | UAT-09 |
| IH-CHAT-004 | IH-CHAT-004-AC01 | A | LR-15 | M3 → M4 | UAT-08, UAT-12 |
| IH-CHAT-004 | IH-CHAT-004-AC02 | A | LR-15 | M3 → M4 | UAT-08, UAT-12 |
| IH-CHAT-004 | IH-CHAT-004-AC03 | A | LR-15 | M3 → M4 | UAT-08, UAT-12 |
| IH-CHAT-004 | IH-CHAT-004-AC04 | A | LR-15 | M3 → M4 | UAT-08, UAT-12 |
| IH-CHAT-004 | IH-CHAT-004-AC05 | A | LR-15 | M3 → M4 | UAT-08, UAT-12 |
| IH-CHAT-005 | IH-CHAT-005-AC01 | A | LR-15 | M3 → M4 | UAT-09, UAT-12 |
| IH-CHAT-005 | IH-CHAT-005-AC02 | A | LR-15 | M3 → M4 | UAT-09, UAT-12 |
| IH-NOTE-001 | IH-NOTE-001-AC01 | A | LR-15 | M3 → M4 | UAT-10 |
| IH-NOTE-001 | IH-NOTE-001-AC02 | A | LR-15 | M3 → M4 | UAT-10 |
| IH-NOTE-001 | IH-NOTE-001-AC03 | A | LR-15 | M3 → M4 | UAT-10 |
| IH-NOTE-001 | IH-NOTE-001-AC04 | A | LR-15 | M3 → M4 | UAT-10 |
| IH-NOTE-002 | IH-NOTE-002-AC01 | A | LR-15 | M3 → M4 | UAT-10, UAT-12 |
| IH-NOTE-002 | IH-NOTE-002-AC02 | A | LR-15 | M3 → M4 | UAT-10, UAT-12 |
| IH-AI-001 | IH-AI-001-AC01 | D1 | LR-18 | M3 → M4 | UAT-11 |
| IH-AI-001 | IH-AI-001-AC02 | D1 | LR-18 | M3 → M4 | UAT-11 |
| IH-AI-002 | IH-AI-002-AC01 | A | LR-18 | M3 → M4 | UAT-11 |
| IH-AI-002 | IH-AI-002-AC02 | A | LR-18 | M3 → M4 | UAT-11 |
| IH-AI-003 | IH-AI-003-AC01 | D1 | LR-18 | M3 → M4 | UAT-11, UAT-14 |
| IH-AI-003 | IH-AI-003-AC02 | A | LR-18 | M3 → M4 | UAT-11, UAT-14 |
| IH-AI-004 | IH-AI-004-AC01 | D1 | LR-18 | M3 → M4 | UAT-11, UAT-12 |
| IH-AI-004 | IH-AI-004-AC02 | A | LR-18 | M3 → M4 | UAT-11, UAT-12 |
| IH-MM-001 | IH-MM-001-AC01 | N | - | Mở rộng | UAT-11 |
| IH-MM-001 | IH-MM-001-AC02 | N | - | Mở rộng | UAT-11 |
| IH-MM-002 | IH-MM-002-AC01 | N | - | Mở rộng | UAT-11, UAT-15 |
| IH-MM-002 | IH-MM-002-AC02 | N | - | Mở rộng | UAT-11, UAT-15 |
| IH-SUM-001 | IH-SUM-001-AC01 | A | LR-16 | M3 → M4 | UAT-11 |
| IH-SUM-001 | IH-SUM-001-AC02 | A | LR-16 | M3 → M4 | UAT-11 |
| IH-SUM-002 | IH-SUM-002-AC01 | A | LR-16 | M3 → M4 | UAT-10, UAT-11 |
| IH-SUM-002 | IH-SUM-002-AC02 | A | LR-16 | M3 → M4 | UAT-10, UAT-11 |
| IH-SLD-001 | IH-SLD-001-AC01 | N | - | Mở rộng | UAT-11 |
| IH-SLD-001 | IH-SLD-001-AC02 | N | - | Mở rộng | UAT-11 |
| IH-SLD-002 | IH-SLD-002-AC01 | N | - | Mở rộng | UAT-11, UAT-15 |
| IH-SLD-002 | IH-SLD-002-AC02 | N | - | Mở rộng | UAT-11, UAT-15 |
| IH-QUIZ-001 | IH-QUIZ-001-AC01 | A | LR-17 | M3 → M4 | UAT-11 |
| IH-QUIZ-001 | IH-QUIZ-001-AC02 | A | LR-17 | M3 → M4 | UAT-11 |
| IH-QUIZ-002 | IH-QUIZ-002-AC01 | A | LR-17 | M3 → M4 | UAT-11 |
| IH-QUIZ-002 | IH-QUIZ-002-AC02 | A | LR-17 | M3 → M4 | UAT-11 |
| IH-RPT-001 | IH-RPT-001-AC01 | N | - | Mở rộng | UAT-11 |
| IH-RPT-001 | IH-RPT-001-AC02 | N | - | Mở rộng | UAT-11 |
| IH-RPT-002 | IH-RPT-002-AC01 | N | - | Mở rộng | UAT-11, UAT-13 |
| IH-RPT-002 | IH-RPT-002-AC02 | N | - | Mở rộng | UAT-11, UAT-13 |
| IH-OUT-001 | IH-OUT-001-AC01 | D1 | LR-18 | M3 → M4 | UAT-11, UAT-13 |
| IH-OUT-001 | IH-OUT-001-AC02 | A | LR-18 | M3 → M4 | UAT-11, UAT-13 |
| IH-OUT-002 | IH-OUT-002-AC01 | A | LR-18 | M3 → M4 | UAT-11, UAT-12 |
| IH-OUT-002 | IH-OUT-002-AC02 | A | LR-18 | M3 → M4 | UAT-11, UAT-12 |
| IH-OUT-003 | IH-OUT-003-AC01 | A | LR-18 | M3 → M4 | UAT-12 |
| IH-OUT-003 | IH-OUT-003-AC02 | A | LR-18 | M3 → M4 | UAT-12 |
| IH-DATA-001 | IH-DATA-001-AC01 | D1 | LR-15/LR-18 | M3 → M4 | UAT-05, UAT-06, UAT-08, UAT-10, UAT-11, UAT-20 |
| IH-DATA-001 | IH-DATA-001-AC02 | D1 | LR-15/LR-18 | M3 → M4 | UAT-05, UAT-06, UAT-08, UAT-10, UAT-11, UAT-20 |
| IH-DATA-001 | IH-DATA-001-AC03 | D1 | LR-15/LR-18 | M3 → M4 | UAT-05, UAT-06, UAT-08, UAT-10, UAT-11, UAT-20 |
| IH-DATA-001 | IH-DATA-001-AC04 | A | LR-15/LR-18 | M3 → M4 | UAT-05, UAT-06, UAT-08, UAT-10, UAT-11, UAT-20 |
| IH-DATA-001 | IH-DATA-001-AC05 | A | LR-15/LR-18 | M3 → M4 | UAT-05, UAT-06, UAT-08, UAT-10, UAT-11, UAT-20 |
| IH-DATA-001 | IH-DATA-001-AC06 | A | LR-15/LR-18 | M3 → M4 | UAT-05, UAT-06, UAT-08, UAT-10, UAT-11, UAT-20 |
| IH-DATA-002 | IH-DATA-002-AC01 | A | LR-17 | M3 → M4 | UAT-10, UAT-11, UAT-12, UAT-20 |
| IH-DATA-002 | IH-DATA-002-AC02 | A | LR-22 | M3 → M4 | UAT-10, UAT-11, UAT-12, UAT-20 |
| IH-DATA-002 | IH-DATA-002-AC03 | A | LR-17 | M3 → M4 | UAT-10, UAT-11, UAT-12, UAT-20 |
| IH-DATA-002 | IH-DATA-002-AC04 | A | LR-22 | M3 → M4 | UAT-10, UAT-11, UAT-12, UAT-20 |
| IH-UX-001 | IH-UX-001-AC01 | D2 | LR-10/LR-21 | M2 → M4 | UAT-15 |
| IH-UX-001 | IH-UX-001-AC02 | D2 | LR-10/LR-21 | M2 → M4 | UAT-15 |
| IH-UX-002 | IH-UX-002-AC01 | D2 | LR-10/LR-21 | M2 → M4 | UAT-15 |
| IH-UX-002 | IH-UX-002-AC02 | A | LR-10/LR-21 | M2 → M4 | UAT-15 |
| IH-UX-003 | IH-UX-003-AC01 | A | LR-10/LR-21 | M2 → M4 | UAT-15 |
| IH-UX-003 | IH-UX-003-AC02 | A | LR-10/LR-21 | M2 → M4 | UAT-15 |
| IH-UX-004 | IH-UX-004-AC01 | A | LR-10/LR-21 | M2 → M4 | UAT-07, UAT-09, UAT-14, UAT-15 |
| IH-UX-004 | IH-UX-004-AC02 | A | LR-10/LR-21 | M2 → M4 | UAT-07, UAT-09, UAT-14, UAT-15 |
| IH-MSG-001 | IH-MSG-001-AC01 | A | LR-15/LR-18 | M3 → M4 | UAT-18 |
| IH-MSG-001 | IH-MSG-001-AC02 | A | LR-15/LR-18 | M3 → M4 | UAT-18 |
| IH-MSG-002 | IH-MSG-002-AC01 | A | LR-15/LR-18 | M3 → M4 | UAT-15, UAT-18 |
| IH-MSG-002 | IH-MSG-002-AC02 | A | LR-15/LR-18 | M3 → M4 | UAT-15, UAT-18 |
| IH-MSG-003 | IH-MSG-003-AC01 | A | LR-14/LR-24 | M3 → M4 | UAT-01, UAT-02, UAT-03, UAT-19 |
| IH-MSG-003 | IH-MSG-003-AC02 | A | LR-14/LR-24 | M3 → M4 | UAT-01, UAT-02, UAT-03, UAT-19 |
| IH-MSG-003 | IH-MSG-003-AC03 | A | LR-14/LR-24 | M3 → M4 | UAT-01, UAT-02, UAT-03, UAT-19 |
| IH-MSG-004 | IH-MSG-004-AC01 | A | LR-15/LR-18 | M3 → M4 | UAT-07, UAT-09, UAT-14, UAT-18 |
| IH-MSG-004 | IH-MSG-004-AC02 | A | LR-15/LR-18 | M3 → M4 | UAT-07, UAT-09, UAT-14, UAT-18 |
| IH-INT-001 | IH-INT-001-AC01 | D1 | LR-11/LR-18 | M2.1 → M4 | UAT-16 |
| IH-INT-001 | IH-INT-001-AC02 | A | LR-11/LR-18 | M2.1 → M4 | UAT-16 |
| IH-INT-002 | IH-INT-002-AC01 | A | LR-11/LR-18 | M2.1 → M4 | UAT-06, UAT-11, UAT-15, UAT-16 |
| IH-INT-002 | IH-INT-002-AC02 | A | LR-11/LR-18 | M2.1 → M4 | UAT-06, UAT-11, UAT-15, UAT-16 |
| IH-INT-002 | IH-INT-002-AC03 | A | LR-11/LR-18 | M2.1 → M4 | UAT-06, UAT-11, UAT-15, UAT-16 |
| IH-INT-003 | IH-INT-003-AC01 | D3 | LR-09/LR-23 | M2.1 → M4 | UAT-01, UAT-02, UAT-03, UAT-11, UAT-16 |
| IH-INT-003 | IH-INT-003-AC02 | A | LR-09/LR-23 | M2.1 → M4 | UAT-01, UAT-02, UAT-03, UAT-11, UAT-16 |
| IH-INT-004 | IH-INT-004-AC01 | A | LR-11/LR-18 | M2.1 → M4 | UAT-07, UAT-09, UAT-12, UAT-16, UAT-17, UAT-20 |
| IH-INT-004 | IH-INT-004-AC02 | A | LR-11/LR-18 | M2.1 → M4 | UAT-07, UAT-09, UAT-12, UAT-16, UAT-17, UAT-20 |
| IH-NFR-001 | IH-NFR-001-AC01 | A | LR-20/LR-24 | M4 | UAT-01, UAT-02, UAT-03, UAT-04 |
| IH-NFR-001 | IH-NFR-001-AC02 | A | LR-20/LR-24 | M4 | UAT-01, UAT-02, UAT-03, UAT-04 |
| IH-NFR-001 | IH-NFR-001-AC03 | A | LR-20/LR-24 | M4 | UAT-01, UAT-02, UAT-03, UAT-04 |
| IH-NFR-001 | IH-NFR-001-AC04 | A | LR-20/LR-24 | M4 | UAT-01, UAT-02, UAT-03, UAT-04 |
| IH-NFR-001 | IH-NFR-001-AC05 | A | LR-20/LR-24 | M4 | UAT-01, UAT-02, UAT-03, UAT-04 |
| IH-NFR-002 | IH-NFR-002-AC01 | A | LR-20/LR-24 | M4 | UAT-12, UAT-13 |
| IH-NFR-002 | IH-NFR-002-AC02 | A | LR-20/LR-24 | M4 | UAT-12, UAT-13 |
| IH-NFR-003 | IH-NFR-003-AC01 | A | LR-20/LR-24 | M4 | UAT-13, UAT-14 |
| IH-NFR-003 | IH-NFR-003-AC02 | A | LR-20/LR-24 | M4 | UAT-13, UAT-14 |
| IH-NFR-004 | IH-NFR-004-AC01 | A | LR-20/LR-24 | M4 | UAT-07, UAT-12, UAT-16 |
| IH-NFR-004 | IH-NFR-004-AC02 | A | LR-20/LR-24 | M4 | UAT-07, UAT-12, UAT-16 |
| IH-NFR-005 | IH-NFR-005-AC01 | A | LR-20/LR-24 | M4 | UAT-07, UAT-09, UAT-14, UAT-16 |
| IH-NFR-005 | IH-NFR-005-AC02 | A | LR-20/LR-24 | M4 | UAT-07, UAT-09, UAT-14, UAT-16 |
| IH-NFR-006 | IH-NFR-006-AC01 | A | LR-21 | M4 | UAT-17 |
| IH-NFR-006 | IH-NFR-006-AC02 | A | LR-21 | M4 | UAT-17 |
| IH-NFR-007 | IH-NFR-007-AC01 | D3 | LR-21/LR-23 | M4 | UAT-17 |
| IH-NFR-007 | IH-NFR-007-AC02 | A | LR-21/LR-23 | M4 | UAT-17 |
| IH-NFR-008 | IH-NFR-008-AC01 | A | LR-20/LR-24 | M4 | UAT-16 |
| IH-NFR-008 | IH-NFR-008-AC02 | A | LR-20/LR-24 | M4 | UAT-16 |
| IH-NFR-009 | IH-NFR-009-AC01 | A | LR-26 | M5 | UAT-16 |
| IH-NFR-009 | IH-NFR-009-AC02 | A | LR-26 | M5 | UAT-16 |
| IH-NFR-010 | IH-NFR-010-AC01 | A | LR-25 | M5 | UAT-16 |
| IH-NFR-010 | IH-NFR-010-AC02 | A | LR-25 | M5 | UAT-16 |
| IH-NFR-011 | IH-NFR-011-AC01 | A | LR-14/LR-24 | M4 | UAT-04, UAT-13, UAT-21 |
| IH-NFR-011 | IH-NFR-011-AC02 | A | LR-14/LR-24 | M4 | UAT-04, UAT-13, UAT-21 |
| IH-REL-001 | IH-REL-001-AC01 | D4 | LR-25 | M5 | UAT-01, UAT-21 |
| IH-REL-001 | IH-REL-001-AC02 | A | LR-25 | M5 | UAT-01, UAT-21 |
| IH-REL-002 | IH-REL-002-AC01 | A | LR-25/LR-26 | M5 | UAT-16 |
| IH-REL-002 | IH-REL-002-AC02 | A | LR-25/LR-26 | M5 | UAT-16 |
| IH-REL-003 | IH-REL-003-AC01 | A | LR-27 | M5 | UAT-16 |
| IH-REL-003 | IH-REL-003-AC02 | A | LR-27 | M5 | UAT-16 |

<a id="evidence"></a>

## 16. Bảng kết quả và mẫu evidence

Dùng các mẫu phù hợp ngay trong hồ sơ đang thực hiện. Một kết quả chỉ lưu ở một nơi và được dẫn lại khi cần; không bắt buộc tạo một file cho mỗi mẫu.

<a id="bang-ket-qua"></a>

### 16.1. Bảng truy vết và kết quả theo yêu cầu

Ghi một lần ở đầu bảng: tên và phiên bản SRS được sử dụng, phiên bản bảng phạm vi, môi trường và chế độ kiểm. Ghi rõ thay đổi phiên bản nếu có. Danh mục lấy từ [bảng phạm vi](#pham-vi-truy-vet), gồm 151 AC áp dụng và 12 AC ngoài bài tập.

| AC và yêu cầu thành phần | Phạm vi | Điều kiện hoặc nhánh | Công việc và thiết kế | Test case | Kỳ vọng | Thực tế | Commit đã kiểm | Minh chứng | Kết luận hoặc lỗi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Mã AC, mã thành phần nếu có | Mã A/D1-D4/N | Trạng thái, biến thể hoặc quy tắc cần kiểm | LR, giao diện, API và dữ liệu liên quan | Mã hoặc tên | Theo yêu cầu và nguồn | Quan sát được | Liên kết commit | Hồ sơ hoặc log | Đạt/chưa đạt/chưa kiểm/bị chặn/ngoài phạm vi |

Mỗi AC có một kết luận tổng hợp. Các điều kiện hoặc yêu cầu thành phần có thể ghi trong ô tương ứng hoặc liên kết tới test case chi tiết của cùng bảng. Không tạo bảng kết luận thứ hai cho cùng phạm vi. Chỉ ghi AC đạt khi mọi điều kiện áp dụng đều đạt; dùng chung test không được làm mất kết luận riêng của từng AC. Điều kiện chưa kiểm, bị chặn hoặc ngoài phạm vi không ghi đạt.

Có thể dùng Markdown, CSV hoặc công cụ quản lý của lớp. M2.1 ghi yêu cầu và kỳ vọng; M2 nối thiết kế; M3.1-M3 bổ sung kiểm cùng chức năng; M4 tổng hợp kết quả đến hạn; M5 bổ sung kết quả release/restore/CR và cập nhật phần bị ảnh hưởng ở R1.1. Dùng [mẫu minh chứng](#evidence) ngay trong hồ sơ hiện có.

**Ví dụ cách ghi ở M4, không phải kết quả kiểm sẵn:** một nhánh upload đã chạy ghi actual/log/commit và kết luận của nhánh; nếu AC còn nhánh chưa chạy thì verdict AC vẫn chưa đạt đủ. Với `IH-REL-001-AC01` chưa kiểm bản release, ghi kết luận “chưa kiểm”, ghi chú “chưa đến hạn M5”, task LR-25 và bước kiểm dự kiến. Giữ AC này trong 151 AC áp dụng, không chuyển sang ngoài phạm vi. Khi có evidence M5 mới cập nhật verdict; điều kiện phát hành không được giảm.

### 16.2. Nội dung cần ghi theo loại công việc

| Loại | Nội dung |
| --- | --- |
| Test/nghiệm thu | Yêu cầu, điều kiện, bước chạy, kỳ vọng/thực tế, môi trường, commit, kết quả và lỗi liên quan |
| Đánh giá AI | Test case/lượt chạy, nguồn và hash/vị trí, ý kỳ vọng, mô hình sinh nội dung, mô hình embedding, phiên bản prompt và schema, kết quả đối chiếu, thời gian/mức sử dụng và người kiểm |
| Lỗi | Bước tái hiện, kỳ vọng/thực tế, tác động, phiên bản lỗi, bản sửa, kết quả kiểm lại và hồi quy |
| Quyết định kiến trúc | Vấn đề, yêu cầu chi phối, các phương án, lựa chọn, đánh đổi, căn cứ và hệ quả |
| Thay đổi sau phát hành | Lý do, hành vi trước/sau, tác động tới yêu cầu/thiết kế/dữ liệu/test, rủi ro, cách quay lại và kết quả kiểm |
| Quyết định với AI | Ngữ cảnh, đề xuất, phép kiểm, phần giữ/sửa/bác bỏ và lý do |
| Review | Sản phẩm/phiên bản, yêu cầu đối chiếu, nhận xét có căn cứ, đề xuất và phản hồi nếu có |

Có thể gộp nội dung cùng loại trong một file; không bắt tạo tài liệu riêng cho mỗi bản ghi. Phân biệt dữ liệu kiểm thử cố định và dịch vụ mô phỏng với dịch vụ thật. Không đưa bí mật xác thực hay dữ liệu chưa được phép vào hồ sơ.

### 16.3. Phân tích ngữ cảnh và quyết định với AI

| Nội dung | Cách ghi |
| --- | --- |
| Công việc và yêu cầu | Mã LR, AC và điều kiện đang xử lý. |
| Phân tích trước khi dùng AI | Kỳ vọng, ngoại lệ và giả định do học viên tự xác định. |
| Ngữ cảnh cung cấp | Phần SRS, thiết kế, mã nguồn hoặc test cần thiết; lý do chọn. |
| Ngữ cảnh loại bỏ | Bí mật, dữ liệu chưa được phép hoặc phần không liên quan; lý do không gửi. |
| Đề xuất của AI | Trích phần cần quyết định hoặc dẫn đoạn trao đổi đã loại thông tin nhạy cảm. |
| Quyết định của học viên | Giữ, sửa hoặc bác bỏ; giải thích bằng yêu cầu và bằng chứng. |
| Kiểm độc lập | Đầu vào, kỳ vọng, thực tế, commit, log hoặc nguồn đối chiếu. |

Không cần lưu mọi câu hỏi hoặc toàn bộ hội thoại. Chọn các quyết định đủ để giải thích cách sử dụng AI và kiểm kết quả.

### 16.4. Quy trình agent và rà soát thay đổi

```text
Công việc, mục tiêu và tiêu chí hoàn thành:
Phạm vi tệp, quyền thực thi và dữ liệu được phép:
Đầu vào, thiết kế và yêu cầu liên quan:
Kế hoạch, điểm có thể dừng và khôi phục:
Lệnh hoặc phép kiểm, kết quả kỳ vọng:
Thao tác thực tế, sự kiện công cụ và kết quả:
Phát hiện: vị trí, tình huống kích hoạt, tác động và căn cứ:
Xử lý, kiểm lại, phần chưa kiểm và quyết định tiếp theo:
```

Rà soát tính đúng, bảo mật, quy ước mã nguồn và thiết kế. Không bắt tìm lỗi ở mọi nhóm; kết luận chưa phát hiện vấn đề phải có căn cứ. Khi kiểm giới hạn quyền, ghi phản hồi từ công cụ hoặc môi trường thực thi. Nếu dùng hook, ghi sự kiện kích hoạt và log của hook; lệnh chạy tay chưa chứng minh hook hoạt động.

### 16.5. Liên kết thiết kế với yêu cầu

Mỗi lựa chọn thiết kế cần chỉ ra yêu cầu chi phối, API, dữ liệu và điều kiện phải luôn đúng, cùng cách kiểm. Sử dụng các cột trong bảng truy vết và liên kết tới sơ đồ, từ điển dữ liệu hoặc hồ sơ quyết định của LR-11; không tạo một bảng yêu cầu khác.

**Ví dụ minh họa:** lần làm Quiz đã nộp giữ nguyên kết quả. Thiết kế phải nêu nơi kiểm quyền và trạng thái, cách chấm rồi lưu nhất quán, và phản hồi khi nhận lại cùng định danh lần làm. Test case dùng hai lần nộp đồng thời hoặc dữ liệu gửi lại khác; kết quả kỳ vọng là một lần chấm và trả bản đã lưu. Ví dụ này là căn cứ thiết kế, không phải kết quả kiểm của bài làm.

| Trạng thái giao diện | Yêu cầu | API và dữ liệu được phép trả | Dữ liệu và phiên bản | Thao tác bàn phím | Phép kiểm |
| --- | --- | --- | --- | --- | --- |
| Tên hành trình hoặc trạng thái | Mã IH/AC | Phản hồi thành công, lỗi và quyền | Đối tượng, trạng thái và phiên bản | Thứ tự focus và phím | Kỳ vọng, test case và minh chứng |

Dùng thành phần giao diện tái sử dụng và chú thích cho trạng thái dùng chung. Liên kết Figma phải là tệp và phiên bản thực có quyền xem; khi triển khai khác thiết kế, cập nhật và giải thích.

### 16.6. TDD, characterization test trước refactor và kiểm hành trình

- **TDD:** lưu kỳ vọng độc lập, test thất bại đúng hành vi, thay đổi triển khai, test đạt và kết quả hồi quy theo trình tự thực tế. Kiểm xem assertion trong test có thực sự phát hiện lỗi.
- **Characterization test trước refactor:** ghi module và vấn đề, phiên bản trước lần sửa đầu, hành vi cần giữ, thay đổi, kết quả trước/sau và phương án khôi phục. Không dựng lại lịch sử để có minh chứng.
- **Kiểm hành trình:** mô tả điều kiện ban đầu, hành động và kết quả; nối với test thực chạy. Ví dụ: khi tài khoản B gọi trực tiếp API của tài nguyên A, phải bị từ chối và không nhận nội dung nguồn.
- **Flaky test:** ghi lần lỗi, căn cứ phân loại nguyên nhân từ sản phẩm, dữ liệu, thời gian hay test, cách sửa và kết quả kiểm lại. Bỏ test hoặc tăng số lần chạy lại không thay việc tìm nguyên nhân.

### 16.7. Đánh giá nội dung AI

```text
Mã test case và lượt chạy; liên kết lượt gốc nếu lặp hoặc kiểm lại:
Commit, ngày chạy, người kiểm và chế độ mô phỏng/dịch vụ thật:
Định danh nguồn, hash, vị trí và phiên bản kỳ vọng:
Công cụ, ngôn ngữ, cấu hình đầu vào:
Nhà cung cấp, mô hình sinh nội dung và mô hình embedding:
Phiên bản prompt, schema và cấu hình truy xuất:
Định danh thao tác, tác vụ hoặc kết quả; trạng thái, thời gian, mức sử dụng:
Tệp đầu ra được phép lưu và hash; phần nhạy cảm đã loại bỏ:
Đối chiếu từng dữ kiện hoặc từng câu, lựa chọn, đáp án, giải thích của Quiz:
Kỳ vọng, thực tế, kết luận, lỗi và liên kết kết quả kiểm lại:
```

Cố định nguồn và kỳ vọng trước khi chạy. Ba đến năm ý kỳ vọng không thay kiểm các phát biểu khác xuất hiện trong đầu ra. ID trích dẫn đúng chưa chứng minh nội dung có căn cứ. Giữ lượt thất bại và lượt kiểm lại riêng; hai lượt lặp được chọn trước trong bộ 12 lượt không thay bằng chạy lại sau sửa lỗi. Nếu không có số đo sử dụng, ghi rõ không thu được thay vì điền số giả.

### 16.8. Phát hành, khôi phục và thay đổi

| Hồ sơ | Nội dung cần ghi |
| --- | --- |
| Phát hành R1 bài tập | Tag, commit, checksum, cấu hình, migration, hướng dẫn cài, dữ liệu và kết quả của đúng bản đã kiểm. |
| Sao lưu và khôi phục | Môi trường nguồn và đích cách ly; dữ liệu trước/sau; số lượng, quan hệ, nội dung, phiên bản và quyền; phụ thuộc Auth ngoài cơ sở dữ liệu ứng dụng; lỗi và giới hạn. |
| Thay đổi R1.1 | Tình huống phát sinh sau R1, hành vi trước/sau, tác động tới yêu cầu, API, dữ liệu và test; thay đổi, hồi quy, phương án phục hồi và tag mới. |

Bản ghi nộp bài dùng mẫu tại mục 2.3. Bổ sung thời gian thực tế, phần còn thiếu và hỗ trợ cần thiết. Nếu sửa code sau khi kiểm, chạy lại phần bị ảnh hưởng, cập nhật commit và kết quả; không điền dữ liệu minh họa thành kết quả cá nhân.

<a id="glossary"></a>

## 17. Glossary và cách dùng thuật ngữ

Bảng dưới giải thích thuật ngữ trong ngữ cảnh project. Tên trường, trạng thái và mã yêu cầu giữ nguyên để truy vết; yêu cầu nghiệp vụ chi tiết nằm trong SRS.

| Thuật ngữ | Ý nghĩa trong bài tập |
| --- | --- |
| Starter | Mã nguồn nền do giảng viên cung cấp để học viên mở rộng thành sản phẩm. |
| Running Project | Dự án dùng xuyên khóa, tích lũy từ yêu cầu đến phát hành và bảo trì. |
| SDLC, SDD | Vòng đời phát triển phần mềm từ yêu cầu đến bảo trì; phát triển dựa trên đặc tả được dùng làm căn cứ thiết kế, code và test. |
| Milestone | Mốc công việc có đầu ra, tiêu chí đánh giá và thời hạn. |
| LR | Mã công việc học tập, từ LR-01 đến LR-29. |
| SRS | Đặc tả yêu cầu phần mềm, xác định hành vi và ràng buộc sản phẩm. |
| IH, BR, LIM, UC | Mã yêu cầu InsightHub, quy tắc nghiệp vụ, giới hạn và use case trong SRS. |
| AC, UAT, AEV | Tiêu chí chấp nhận, kịch bản nghiệm thu tổng hợp và test case đánh giá chất lượng AI. |
| PLO, CLO | Chuẩn đầu ra chương trình và chuẩn đầu ra khóa học. |
| PRE, KC, TG | Phần chuẩn bị trước buổi học, tài liệu kiến thức và hướng dẫn công cụ. |
| R1, R1.1 | Bản phát hành bài tập và bản có thay đổi sau đó; phạm vi bắt buộc gồm Tóm tắt và Quiz. |
| Rubric | Bảng tiêu chí và cách tính điểm để đánh giá đầu ra. |
| Minh chứng (evidence) | Dữ liệu cho phép kiểm lại kết luận, như mã nguồn, đầu vào, kết quả và log đúng phiên bản. |
| Repository, fork, commit, branch, tag | Kho mã nguồn; bản sao kho thuộc tài khoản học viên; mốc lưu thay đổi; nhánh làm việc; nhãn định danh bản phát hành. |
| Pull Request (PR) | Đề nghị đưa thay đổi từ nhánh làm việc vào nhánh đích, dùng để rà soát và nộp bài. |
| Backlog, issue | Danh sách công việc có ưu tiên; bản ghi một công việc hoặc vấn đề cần xử lý. |
| Dependency, spike | Điều kiện hoặc công việc cần có trước; thử nghiệm có giới hạn để kiểm một giả định kỹ thuật trước khi chọn giải pháp. |
| CI, lint | Tích hợp liên tục để tự chạy kiểm tra; kiểm quy ước hoặc vấn đề mã nguồn bằng công cụ. |
| Schema | Mô tả cấu trúc dữ liệu, kiểu, trường và ràng buộc. Cần phân biệt logic nghiệp vụ, API và lưu trữ vật lý. |
| OpenAPI, JSON Schema | Định dạng mô tả giao tiếp API và định dạng mô tả cấu trúc dữ liệu JSON. |
| Entity, ERD | Thực thể nghiệp vụ và sơ đồ quan hệ giữa các thực thể. |
| Invariant | Điều kiện phải luôn đúng trong phạm vi nghiệp vụ, kể cả khi lỗi hoặc xử lý đồng thời. |
| DTO, projection | Cấu trúc dữ liệu trao đổi và tập trường được phép đưa vào một phản hồi; có thể khác đối tượng lưu nội bộ. |
| Metadata | Thông tin quản lý như tên hiển thị hoặc phiên bản, phân biệt nội dung AI đã sinh. |
| Migration | Chuyển cấu trúc hoặc dữ liệu lưu trữ có kiểm soát khi giải pháp thay đổi. |
| ADR (Architecture Decision Record) | Bản ghi quyết định kiến trúc, gồm vấn đề, phương án, lựa chọn, căn cứ và đánh đổi. |
| Auth, authentication, authorization | Nhóm chức năng tài khoản; xác thực danh tính; kiểm quyền thực hiện hành động trên tài nguyên. |
| Transactional email, trigger | Email được gửi do một sự kiện nghiệp vụ, như xác minh hoặc reset mật khẩu; sự kiện kích hoạt hành vi tương ứng. |
| Ownership, persistence, provenance | Quyền sở hữu tài nguyên; khả năng giữ dữ liệu qua reload/restart theo vòng đời quy định; thông tin xuất xứ để truy về nội dung hoặc nguồn đã tạo dữ liệu. |
| Citation, claim | Tham chiếu đến nguồn và vị trí hỗ trợ nội dung; một phát biểu về dữ kiện cần được đối chiếu với nguồn. |
| Session, token, callback | Phiên đăng nhập; bằng chứng xác thực; địa chỉ nhận kết quả từ dịch vụ xác thực. |
| OAuth, OIDC | Giao thức ủy quyền và lớp xác thực danh tính thường dùng khi tích hợp Google; chọn thư viện phù hợp và kiểm ở máy chủ. |
| Client, server, request, response | Thành phần gửi, thành phần xử lý, thông điệp yêu cầu xử lý và phản hồi. |
| Idempotency key, replay, retry | Mã nhận diện thao tác; gửi lại thao tác đã nhận để đối soát; thử xử lý lại sau lỗi. Các trường hợp có quy tắc khác nhau trong SRS. |
| Rate limit, quota, concurrency limit | Giới hạn tần suất, hạn mức sử dụng và giới hạn số tác vụ chạy đồng thời. |
| Sliding window | Khoảng thời gian tính lùi từ lúc máy chủ kiểm tra, không đặt lại theo phút hoặc giờ lịch. |
| Deadline, timeout, TTL | Thời hạn tuyệt đối của tác vụ; hết thời gian chờ; thời gian hiệu lực hoặc lưu giữ của bản ghi kỹ thuật. |
| Transaction, commit, race condition | Giao dịch dữ liệu; hoàn tất ghi giao dịch; lỗi do thứ tự thực thi đồng thời không được kiểm soát. Commit giao dịch khác commit Git. |
| Snapshot, fingerprint | Dữ liệu được giữ tại một thời điểm; giá trị dùng đối chiếu đầu vào để phát hiện yêu cầu gửi lại khác nội dung. |
| RAG, ingestion, embedding, reranker | Sinh câu trả lời có truy xuất nguồn; tiếp nhận và xử lý tài liệu; biểu diễn văn bản bằng véc-tơ; sắp xếp lại kết quả truy xuất. |
| Provider, model, prompt, output parser | Nhà cung cấp dịch vụ, mô hình, chỉ dẫn/ngữ cảnh gửi mô hình và thành phần phân tích đầu ra. |
| Fixture, mock, dịch vụ thật | Dữ liệu kiểm thử cố định; thành phần mô phỏng; tích hợp với hệ thống bên ngoài thực tế. Mô phỏng không chứng minh chất lượng AI hoặc email thật. |
| Test case | Đặc tả kiểm thử cụ thể, gồm điều kiện ban đầu, dữ liệu, bước thực hiện và kết quả kỳ vọng. Khi chạy, bổ sung kết quả thực tế và trạng thái. |
| Test scenario | Mô tả hành vi hoặc hành trình cần kiểm ở mức tổng quát; một scenario có thể cần nhiều test case. |
| Test script | Code hoặc chuỗi bước dùng thực thi test case; có script không đồng nghĩa test đã chạy hoặc đã đạt. |
| Use case | Mô tả tương tác giữa người dùng và hệ thống để đạt một mục tiêu nghiệp vụ; không đồng nghĩa test case. |
| TDD, characterization, regression | Phát triển theo kiểm thử; kiểm ghi nhận hành vi trước thay đổi; kiểm để phát hiện tác dụng phụ làm hỏng hành vi cần giữ. |
| BDD, Given/When/Then | Diễn đạt hành vi theo điều kiện ban đầu, hành động và kết quả kỳ vọng. |
| Assertion | Điều kiện test kiểm tra để đối chiếu actual result với expected result; nếu điều kiện không đúng, test báo lỗi. |
| Flaky test | Test có kết quả pass/fail không ổn định dù code không đổi, thường do trạng thái dữ liệu, thời gian hoặc phụ thuộc chưa được kiểm soát. |
| Rollback, restore | Rollback đưa ứng dụng về phiên bản trước; restore khôi phục dữ liệu từ bản backup. Cần xác định tương thích schema và quyền sau mỗi thao tác. |
| Checksum, hash | Giá trị tính từ nội dung để kiểm tra toàn vẹn hoặc nhận diện dữ liệu. Hash khớp không chứng minh nội dung đúng về nghiệp vụ. |
| Threat model | Phân tích tài sản, ranh giới tin cậy, mối đe dọa và biện pháp kiểm soát để chọn các kiểm tra bảo mật phù hợp. |
| Unit, integration, contract, E2E | Kiểm đơn vị, tích hợp, hợp đồng giao tiếp và hành trình xuyên các thành phần. |
| Hook, checkpoint, sandbox | Tác vụ được kích hoạt bởi sự kiện; trạng thái được lưu để tiếp tục hoặc khôi phục quy trình; môi trường thực hành có giới hạn. |
| Agent, MCP, skill | Hệ thống AI thực hiện các bước với công cụ; giao thức kết nối công cụ/ngữ cảnh; hướng dẫn hoặc quy trình tái sử dụng. |
| Viewport, focus, prototype | Vùng trình duyệt hiển thị trang; trạng thái xác định phần tử đang nhận thao tác bàn phím; bản mẫu cho phép thử tương tác trước khi triển khai. |
| SBOM, secret, XSS | Danh mục thành phần phần mềm; bí mật như mật khẩu/khóa dịch vụ; chèn mã độc thực thi trong trình duyệt. |
| Runbook, restore, CR | Hướng dẫn vận hành; khôi phục dữ liệu; bản ghi yêu cầu thay đổi. |
| Blocked, Pending, OutOfScope | Bị chặn bởi phụ thuộc; chưa thực hiện hoặc chưa có kết quả; ngoài phạm vi. Đều khác kết luận đạt. |

### 17.1. Ví dụ phân biệt test scenario và test case

**Test scenario:** người dùng chỉ được truy cập Notebook thuộc quyền của mình.

**Test case minh họa cho một nhánh bị từ chối:**

| Thành phần | Nội dung |
| --- | --- |
| Mã test case | TC-NB-ACCESS-01, mã minh họa do học viên tự quản lý |
| Yêu cầu liên quan | IH-NB-004-AC01 và BR-01; test case này kiểm nhánh đọc Notebook của tài khoản khác |
| Điều kiện ban đầu | Tài khoản A có một Notebook; tài khoản B đang đăng nhập hợp lệ và không có quyền trên Notebook đó |
| Dữ liệu | Notebook ID của A và session của B; chỉ dùng dữ liệu thử được phép |
| Bước thực hiện | Dùng session B gọi trực tiếp API đọc Notebook của A |
| Kết quả kỳ vọng | Request bị từ chối theo API contract đã chọn; không trả dữ liệu của A và không tiết lộ sự tồn tại của Notebook |
| Kết quả thực tế và trạng thái | Điền sau khi chạy test trên commit xác định; trước khi chạy ghi Pending |

Scenario này còn cần test case cho nhánh được phép, session hết hạn và các thao tác sửa/xóa. Một test case đạt chưa chứng minh toàn bộ scenario hoặc AC đã đạt.
