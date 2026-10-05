# Requirements - Dự án cá nhân InsightHub

B2B C07 - SDLC with AI | Phiên bản 1.4, 06/10/2026 (tầng Core/Extended công bố 29/09/2026, cân tải tự học 04/10/2026, đồng bộ Mốc với Curriculum 0.9.2 ngày 06/10/2026). Thay đổi sau khi phát hành áp dụng [chính sách thay đổi đề bài](#chinh-sach-thay-doi)
Học trực tuyến, thực hiện cá nhân | 10 buổi, 25 giờ trên lớp và khoảng 59 giờ tự học (2 đến 2,5 giờ mỗi ngày, trần 3 giờ)

Tài liệu xác định các chức năng InsightHub học viên phải xây, cách áp dụng SDLC và AI vào 29 công việc, cùng kết quả cần đạt qua 10 buổi. Phạm vi, thiết kế và tích hợp, rubric, cách nộp bài và mẫu evidence được trình bày trong cùng tài liệu. Học viên bắt đầu tại mục 1-2, thực hiện milestone tương ứng và tra các mục chuyên đề ngay trong tài liệu.

> **Thay đổi so với bản 1.3 (06/10/2026):**
>
> - Bảng 2.1 thêm cột Mốc theo Curriculum. Slide và Knowledge Content dùng tên Mốc, tài liệu này giữ mã milestone và LR.
> - M1: kế hoạch cá nhân có bảng gate 6 pha và bản đồ AI theo pha, Charter cập nhật RACI và 2 stop condition enforced, baseline từ AI Delivery Log. Rubric M1 thêm tiêu chí Lifecycle Board 20 điểm. Timebox không đổi vì phần nháp làm ở Lab buổi 3 (mục 5).
> - M2.1: `spec.md` của Quiz có yêu cầu EARS, AC 3 nhánh, NFR có số đo và clarification log (mục 6). Lab buổi 4 luyện trên ví dụ Tóm tắt, không chấm.
> - M2: hồ sơ thiết kế có C4 Context và Container, bảng khớp prototype, sequence, OpenAPI, ERD, AC cho một hành trình. ADR có mục Điều kiện xem lại. Threat model có cột điều kiện lethal trifecta đã cắt (mục 7).
> - Không đổi phạm vi AC, tầng Core/Extended, timebox và trọng số điểm khóa.

> **Thay đổi so với bản 1.2 (04/10/2026):**
>
> - Phạm vi: 14 AC Core chuyển Extended, gồm khôi phục, đặt lại, đổi mật khẩu và hồ sơ, xóa Notebook và xóa kết quả AI, chặn công bố câu trả lời Chat và trạng thái tác vụ khi nguồn đổi giữa chừng, đo 10 thao tác không gọi AI. Core còn 92 AC, email tầng Core còn EML-001 (mục 1.1, 2.1.5).
> - Chat giữ cơ chế operation của Starter, không chuyển vào AI Job scaffold. LIM-10 áp dụng cho Tóm tắt và Quiz (mã D8). Thêm mã D9 cho đường truy cập cũ của tài liệu đã xóa (mục 15.1).
> - Gọn đầu ra ở các LR: backlog 8 đến 10 issue, một ADR hai phương án, 19 UAT tầng Core, bốn ca hardening, review bất đồng bộ một lần ở M2. Không bỏ LR nào (mục 3 đến 12).
> - Tự học khoảng 59 giờ, đã gồm Quiz và bản chuẩn bị. Học theo nhịp "đi trước một buổi" với nhịp tuần mẫu (mục 1.3, 2.1).
> - Hồ sơ Capstone nộp trước buổi 10 ít nhất 2 giờ, không trùng hạn M5 (mục 2.1, 12.5).

**Mục lục**

| Nội dung | Vị trí |
| --- | --- |
| Chín nhóm chức năng bắt buộc và trách nhiệm | [1. Phạm vi sản phẩm](#san-pham) |
| Khởi động, lộ trình, cách nộp, điểm số và chính sách thay đổi đề bài | [2. Hướng dẫn thực hiện](#bat-dau), [2.9. Chính sách thay đổi](#chinh-sach-thay-doi) |
| Phạm vi, kết quả và cách review milestone theo SDLC | [Ma trận tiến độ sản phẩm](#ma-tran-chuc-nang), [bản đồ milestone](#do-ket-qua-milestone), [cách làm xuyên SDLC](#sdlc-xuyen-milestone), [Core và Extended](#core-extended) |
| AI Engineering Kit và kiểm chứng theo rủi ro | [2.1.6. AI Engineering Kit](#ai-kit), [2.1.7. Kiểm chứng theo rủi ro](#kiem-chung-rui-ro) |
| Buổi 1-2 | [M0.1](#m01), [M0.2](#m02) |
| Buổi 3-5 | [M1](#m1), [M2.1](#m21), [M2](#m2) |
| Buổi 6-7 | [M3.1](#m31), [M3](#m3) |
| Buổi 8-10 | [M4](#m4), [M5](#m5), [Capstone](#capstone) |
| Thiết kế dữ liệu, schema, API và tích hợp | [13. Data và API](#data-api) |
| Auth, Google và email | [14. Thử tích hợp và kiểm chứng](#auth-email) |
| Phạm vi áp dụng và traceability matrix (bảng truy vết) 165 AC | [15. Phạm vi và truy vết](#pham-vi-truy-vet) |
| Bảng kết quả và mẫu evidence | [16. Hồ sơ kiểm chứng](#evidence) |
| Thuật ngữ và ví dụ test case | [17. Glossary](#glossary) |

**File đính kèm để tra cứu**

- [SRS InsightHub v1.1](02_SRS_InsightHub_v1.1.md): hành vi sản phẩm và acceptance criteria (AC, tiêu chí chấp nhận) chi tiết. Tra theo mã yêu cầu khi phân tích, thiết kế hoặc test.
- [API và Schema Reference](03_API_Schema_Reference_v1.1.zip): gói kỹ thuật chứa OpenAPI, JSON Schema, ví dụ và công cụ kiểm cấu trúc. Chỉ mở khi cần sử dụng các file kỹ thuật ở M2 trở đi. Các quy tắc học viên cần biết và cách áp dụng được trình bày tại mục 13; gói này không tạo thêm bài nộp.

<a id="san-pham"></a>

## 1. Sản phẩm cần hoàn thiện

Mỗi học viên xây dựng sản phẩm InsightHub hoàn chỉnh trong phạm vi bài tập từ Starter do giảng viên cung cấp. Người dùng có thể đăng nhập, quản lý Notebook và tài liệu, hỏi đáp có nguồn, lưu hội thoại và ghi chú, tạo bản Tóm tắt và làm Quiz từ tài liệu.

### 1.1. Chức năng của sản phẩm bài tập: Core và Extended

**Bắt buộc (Core):** Auth cơ bản (đăng ký, xác minh email, đăng nhập, phiên, đăng xuất), Notebook (gồm Document và Chat/Conversation trong Notebook), hai AI Tools Summary và Quiz, cùng phần AI Job/Output đủ để hai công cụ chạy, kiểm chứng ở M4 và phát hành ở M5. **Làm thêm (Extended):** khôi phục và đổi mật khẩu, hồ sơ, Note, xóa Notebook, quản lý kết quả AI (xóa, đổi tên, tạo lại), đăng nhập và liên kết Google và các nhánh nâng cao. Extended không trừ điểm khi chưa làm; danh sách từng AC tại [mục 2.1.5](#core-extended).

Học viên hoàn thiện mỗi nhóm chức năng qua các phần UI, API và dữ liệu liên quan theo SRS, sử dụng thư viện và phần nền được cung cấp. Các nhóm là cách tổ chức đề bài, không bắt buộc tách thành service, module hoặc màn hình quản trị riêng.

| Nhóm chức năng | Người dùng phải làm được gì trong bản hoàn thiện | Trách nhiệm của học viên | Yêu cầu và công việc liên quan | Tầng |
| --- | --- | --- | --- | --- |
| **Auth và Account** | Đăng ký, xác minh email, đăng nhập bằng mật khẩu, session và logout. Khôi phục/đổi mật khẩu, profile và Google là Extended. | Starter cấp **Auth scaffold**: Better Auth email và mật khẩu, bảng user/session, dependency `current_user` ở API, trang `/login` tối thiểu ([Auth Integration Guide](../Auth_Integration_Guide.md)). Học viên xây nghiệp vụ tài khoản, chính sách theo SRS và kiểm quyền tại server. | IH-AUTH-001 đến IH-AUTH-010; [LR-09](#lr-09), [LR-12](#lr-12), [LR-14](#lr-14). | Core: đăng ký, xác minh, đăng nhập email và mật khẩu, phiên, đăng xuất; Extended: khôi phục, đặt lại và đổi mật khẩu, profile, đăng nhập và liên kết Google, phiên chờ xác minh, giới hạn thử, avatar |
| **Transactional Email** | Nhận email xác minh (EML-001). Extended: reset mật khẩu, thông báo liên kết Google, hướng dẫn tài khoản chỉ dùng Google và thông báo đổi/reset mật khẩu. | Tạo đúng sự kiện, nội dung, link và trạng thái gửi của EML-001 (cùng các email Extended đã làm); kiểm thư nhận thật và lỗi chuyển giao. | IH-MSG-003; [LR-09](#lr-09), [LR-14](#lr-14), [danh mục email](#auth-email). | Core: EML-001; Extended: EML-002 (gắn khôi phục mật khẩu), EML-003, EML-004 (gắn đăng nhập Google), EML-005 |
| **Notebook** | Tạo, xem danh sách, mở, đổi tên/mô tả Notebook thuộc quyền; nhận thông báo khi vượt giới hạn. Extended: xóa Notebook, thông báo version conflict. | Xây UI/API/data cho Notebook, ownership, pagination và giới hạn; quy tắc xóa tài nguyên con khi làm Extended. | IH-NB-001 đến IH-NB-004; [LR-12](#lr-12), [LR-15](#lr-15). | Core: tạo, liệt kê, mở, đổi tên/mô tả, ownership; Extended: xóa Notebook (gồm hộp xác nhận), version conflict khi sửa |
| **Document** | Upload TXT, Markdown và PDF có văn bản; xem trạng thái, retry khi lỗi, mở nội dung/citation và xóa tài liệu. | Tái sử dụng ingestion, extraction và index của Starter; tích hợp Notebook, quyền, quota, chống trùng, trạng thái và vòng đời. | IH-DOC-001 đến IH-DOC-006; [LR-12](#lr-12), [LR-15](#lr-15). | Core (phần lớn Starter đã có, kiểm lại sau tích hợp); Extended: retry trên UI, trang chi tiết, dọn dữ liệu sau xóa |
| **Chat và Conversation** | Hỏi đáp theo nguồn, mở citation, phân biệt thiếu căn cứ với lỗi; tạo, xem conversation và đọc lại lịch sử. Extended: đổi tên, xóa conversation. | Tích hợp RAG nền với quyền và phạm vi nguồn; giữ cơ chế operation của Starter (idempotency, deadline) đã scope theo người dùng; xây persistence và quản lý conversation độc lập với operation TTL. | IH-CHAT-001 đến IH-CHAT-005; [LR-12](#lr-12), [LR-15](#lr-15). | Core; Extended: đổi tên, xóa conversation, conversation mất nguồn cuối, chặn công bố câu trả lời khi nguồn hoặc quyền đổi giữa chừng |
| **Note** | Tạo, mở, sửa, xóa Note; lưu câu trả lời hoặc Summary hợp lệ thành bản sao độc lập. | Xây UI/API/data, validation, version conflict và provenance; bảo toàn Note theo quy tắc xóa của SRS. | IH-NOTE-001, IH-NOTE-002, IH-SUM-002; [LR-15](#lr-15), [LR-16](#lr-16). | **Extended** |
| **Summary (Tóm tắt)** | Chọn nguồn và độ dài, tạo Summary có căn cứ, xem nguồn, mở lại và lưu thành Note. | Xây cấu hình, prompt/schema/parser, UI, persistence và kiểm chất lượng nội dung trên kết nối model đã có. | IH-SUM-001, IH-SUM-002; [LR-16](#lr-16). | Core; Extended: lưu thành Note |
| **Quiz** | Tạo đề, chọn câu trả lời, nộp bài, xem điểm/giải thích, mở lại lần đã nộp và làm lại. | Xây schema công khai/nội bộ, UI và chấm tại server; bảo vệ đáp án, lưu QuizAttempt, xử lý nộp lặp. | IH-QUIZ-001, IH-QUIZ-002, IH-DATA-002; [LR-17](#lr-17). | Core |
| **AI Job và Output** | Theo dõi AI job (tác vụ AI), xem và lọc kết quả theo loại. Đổi tên, regenerate và xóa kết quả là Extended. | Starter cấp **AI Job scaffold** (cơ chế job theo người dùng, quota, idempotency, deadline, publish fence, policy mặc định từ chối; [AI Job Framework](../AI_Job_Framework.md)). Học viên viết policy, executor, schema, Output, fallback và ghi usage (IH-AI-005) cho Summary và Quiz. | IH-AI-001 đến IH-AI-005, IH-OUT-001 đến IH-OUT-003, IH-INT-004; [LR-18](#lr-18). | Core: trạng thái, schema, quota, idempotency, deadline, fallback, usage, danh sách, lọc theo loại, mở lại; Extended: xóa, đổi tên, tạo lại |

### 1.2. Yêu cầu áp dụng xuyên các chức năng

- **UI/UX:** thiết kế và triển khai theo prototype thiết kế đã chốt phiên bản (Figma hoặc HTML, học viên chọn một ở [LR-10](#lr-10)) trong phạm vi bài tập, dùng nền UI của Starter ([UI Foundation](../UI_Foundation.md): token, component, app shell). Hành trình M3.1 và màn làm Quiz có đủ trạng thái loading, empty, success, error, hết session và conflict, hai kích thước màn hình và thao tác bàn phím theo SRS (IH-UX-003-AC01, mã D6). Summary và quản lý Output dùng UI tối thiểu (danh sách, xem) có trạng thái đang xử lý, rỗng và lỗi.
- **Quyền và dữ liệu:** server xác định người dùng từ session, kiểm ownership của đúng đối tượng trước mọi thao tác; dữ liệu còn sau reload/restart theo vòng đời quy định. Không dùng `owner_id` do client gửi để cấp quyền.
- **Chất lượng và tích hợp:** validation, API contract, lỗi an toàn, giới hạn xử lý và cấu hình provider phải nhất quán giữa UI, API và dữ liệu. Kết quả fixture, tích hợp thật và đánh giá nội dung AI được ghi riêng.
- **Bàn giao:** bản R1 của bài tập có test, CI, migration, hướng dẫn cài/chạy, backup/restore và một thay đổi sau phát hành thành R1.1. Học viên thực hiện trên máy cá nhân.

Starter `learner-r1.3` cung cấp Next.js, FastAPI, PostgreSQL/pgvector, Docker Compose, ingestion, embedding/index, RAG cơ bản, dữ liệu mẫu và công cụ kiểm, cùng ba phần nền: **Auth scaffold**, **AI Job scaffold** và **nền UI**. Các scaffold chỉ là cơ chế dùng chung, không chứa nghiệp vụ và không làm AC nào tự đạt. Starter được cấp một lần trước buổi 1; trong khóa chỉ có hotfix cho lỗi chặn theo [mục 2.9](#chinh-sach-thay-doi). Học viên kiểm lại các phần này sau khi tích hợp; kết quả của Starter không tự xác nhận phần mở rộng đã đạt.

[SRS InsightHub v1.1](02_SRS_InsightHub_v1.1.md) là spec (đặc tả) hành vi sản phẩm. Bài tập áp dụng **153 AC** cho phạm vi trên, gồm **92 AC Core** và **61 AC Extended**; [bảng phạm vi](#pham-vi-truy-vet) chỉ rõ 12 tiêu chí ngoài phạm vi bắt buộc. Các AC áp dụng được phân tầng Core và Extended theo [mục 2.1.5](#core-extended). Mindmap, Slide và Báo cáo không bắt buộc. Không yêu cầu triển khai hạ tầng cloud cho vận hành thực tế hoặc Kubernetes.

Phần [thiết kế dữ liệu và API](#data-api) xác định đầu ra cần thực hiện và cách tích hợp Starter. Tra [glossary](#glossary) để phân biệt các thuật ngữ như test case, test scenario, schema và migration.

### 1.3. Công cụ, dữ liệu và trách nhiệm

**Công cụ phát triển:** công ty cấp tài khoản Claude Pro/Max cho học viên, chỉ dùng cho học tập; Claude (Claude.ai, Claude Code) là công cụ AI chính của khóa học. ChatGPT/Codex là phương án bổ sung nếu học viên có tài khoản và muốn dùng; không bắt buộc có hoặc mua tài khoản ChatGPT. Mỗi Tool Guideline (TG) viết theo Claude và có mục **Mapping ChatGPT/Codex** ở cuối để tra thao tác tương đương. Học viên tự phân tích, kiểm chứng và giải thích quyết định, dù sử dụng công cụ nào. Công cụ làm việc chính là Claude App for Desktop và Claude Code trên máy cá nhân. MCP bắt buộc từ M0.2 với role cơ sở dữ liệu chỉ đọc của Starter; máy không chạy được MCP dùng phương án dự phòng tại [LR-05](#lr-05). Tuần 3 (buổi 6 đến 8) dùng Claude Code nhiều nhất: chia task nhỏ, mở session mới cho mỗi task, dùng `/compact` hoặc `/clear` khi đổi chủ đề, theo dõi hạn mức sử dụng và chạy task dài sớm để không bị gián đoạn sát hạn nộp.

**Dịch vụ AI của sản phẩm:** học viên dùng **API key tự mua**: DeepSeek để sinh nội dung theo cấu hình mặc định của Starter, hoặc một provider tùy chọn được Starter hỗ trợ (Gemini, Anthropic, gateway OpenAI-compatible, Ollama local); embedding do học viên cấu hình, mặc định Gemini; reranker tắt. Chọn provider theo [cấu hình mô hình](../Model_Profiles_And_Reranking.md). Các dịch vụ này khác tài khoản Claude dùng hỗ trợ phát triển. Học viên tự chịu chi phí và đặt spending limit trên tài khoản provider; chỉ giữ key trong `.env`, không commit, không dán key vào Claude hay công cụ AI khác. Dữ liệu gửi tới provider bên ngoài có thể đi ra nước ngoài, vì vậy chỉ gửi corpus giả và dữ liệu thử.

**Tài khoản và dữ liệu khi dùng AI:**

- Trước buổi 1, mở `claude.ai/settings/data-privacy-controls` và **tắt** thiết lập cho phép dùng dữ liệu để cải thiện model (training). Khi tắt, dữ liệu không dùng để training và được lưu tối đa 30 ngày. Kiểm lại và ghi xác nhận trong checklist setup buổi 1.
- Chỉ đưa vào Claude: Starter, corpus giả và bài làm của chính mình. Không đưa mã nguồn, tài liệu, dữ liệu hoặc credential của Samsung SDS hay khách hàng; không đưa `.env`, API key, token. Giữ các rule deny trong `.claude/settings.json` của Starter.
- Không dùng `/feedback` hoặc chia sẻ transcript khi có nội dung bài làm chưa công khai.
- Dùng tài khoản Google và email test riêng cho khóa học khi làm Auth/Email của InsightHub; không dùng tài khoản công ty.
- Học trên máy cá nhân; tự chuẩn bị Docker phù hợp theo [GETTING_STARTED](../../GETTING_STARTED.md). Máy Windows dùng WSL2.
- Khi áp dụng vào dự án thật sau khóa học, chỉ dùng công cụ AI và dữ liệu được Samsung SDS phê duyệt.

**Cách học (nhịp "đi trước một buổi"):** trước buổi n, đọc KC/TG buổi n, làm Quiz, làm phần milestone n trong khả năng và gửi bản chuẩn bị gồm phần đã làm và câu hỏi cần hỗ trợ. Trên lớp, trao đổi các điểm khó của dự án gắn với nội dung buổi học. Sau buổi n, sửa theo phản hồi (5 đến 15 phút), hoàn thiện milestone n trước hạn và tiếp tục đọc, làm phần của buổi kế tiếp chưa làm. Học liệu phát hành sớm nên có tuần học viên đi trước hơn một buổi; đó là mức an toàn, không phải yêu cầu thêm. Tổng khoảng 59 giờ tự học đã bao gồm đọc, Quiz, bản chuẩn bị, thực hành, test, sửa bài và chuẩn bị bảo vệ; mức gợi ý 2 giờ vào ngày có lớp, 2,5 giờ vào ngày không có lớp, trần 3 giờ ([nhịp tuần mẫu](#nhip-tuan-mau)). Tuần 3 (buổi 6 đến 8) nặng nhất; bắt đầu M3.1 trước buổi 6 theo nhịp trên để không dồn việc.

**Cách làm với AI:** được dùng AI Agent xuyên quá trình đọc nguồn, phân tích, lập kế hoạch, thiết kế, code, test, review và soạn hồ sơ. Học viên đối chiếu và chốt yêu cầu/expected result (kết quả kỳ vọng) theo nguồn, kiểm thay đổi và giải thích quyết định; không bắt gõ thủ công toàn bộ bảng AC hoặc tự viết mọi dòng code trước khi dùng AI. Với bước nền, cần tự giải thích được mục tiêu, input, expected và cách kiểm trước khi giao agent thực hiện. Lưu một vài quyết định tiêu biểu đã giữ, sửa hoặc bác bỏ đề xuất AI và lý do; không cần nộp toàn bộ hội thoại. Cách làm với AI được ghi lại trong repository qua [AI Engineering Kit](#ai-kit): quy tắc agent, quyền và hook, template, quy trình review, spec, eval và số đo; mỗi milestone hoàn thiện thêm một phần trong output hiện có. Quiz vẫn tự làm theo mục 2.5. Không commit secret xác thực hoặc file `.env` thật vào Git.

<a id="bat-dau"></a>

## 2. Lộ trình, cách nộp bài và cách tính điểm

### 2.1. Lộ trình và thời hạn

| Buổi | Milestone | Mốc (Curriculum) | Kết quả chính | Tự học | Hạn hoàn thiện |
| --- | --- | --- | --- | --- | --- |
| 1 | M0.1 | Mốc 0 | Starter chạy upload, hỏi đáp và citation; một phân tích yêu cầu bằng AI đã được kiểm | 4,3 giờ | Trước buổi 2 ít nhất 12 giờ |
| 2 | M0.2 | Mốc 0 | Agent workflow trên InsightHub có giới hạn quyền, xử lý lỗi và chạy lại được | 4,9 giờ | Trước buổi 3 ít nhất 12 giờ |
| 3 | M1 | Mốc 1 | Backlog chín nhóm chức năng, dependency, kế hoạch cá nhân có bảng gate và bản đồ AI, Charter cập nhật, Git/CI | 4,4 giờ | Trước buổi 4 ít nhất 12 giờ |
| 4 | M2.1 | Mốc 2 | Yêu cầu và test case theo chức năng, spec của Quiz; kết quả spike chính sách Auth, email EML-001 và AI (Google tùy chọn) | 5,5 giờ | Trước buổi 5 ít nhất 12 giờ |
| 5 | M2 | Mốc 3 | Prototype thiết kế (Figma hoặc HTML), API, schema, ADR và threat model sơ bộ cho các chức năng bài tập | 6,1 giờ | Trước buổi 6 ít nhất 12 giờ |
| 6 | M3.1 | Mốc 4 | Đăng nhập → Notebook → upload → hỏi đáp → citation → mở lại conversation | 8 giờ | Trước buổi 7 ít nhất 12 giờ |
| 7 | M3 | Mốc 5 | Auth và email tầng Core, Notebook/Document/Conversation, Summary, Quiz và AI Output tầng Core; refactor. Extended theo mục 2.1.5 (ví dụ khôi phục và đổi mật khẩu, hồ sơ, Note, xóa Notebook, quản lý Output, đăng nhập và liên kết Google) khi Core đã đạt | 8,9 giờ | Chức năng: trước buổi 8 ít nhất 12 giờ; bài refactor: trước buổi 9 ít nhất 12 giờ |
| 8 | M4 | Mốc 6 | Kết quả kiểm từng chức năng, quyền, hardening AI Job, eval AI, threat model cập nhật và lỗi đã sửa | 9,3 giờ | Trước buổi 9 ít nhất 12 giờ |
| 9 | M5 | Mốc 7 | R1 cài được, dữ liệu khôi phục được và thay đổi R1.1 có regression test | 4,6 giờ | Trước buổi 10 ít nhất 12 giờ |
| 10 | Capstone | Capstone | Demo sản phẩm hoàn chỉnh, truy vết quyết định và kế hoạch áp dụng 30 ngày | 2,8 giờ | Hồ sơ trước buổi 10 ít nhất 2 giờ; sửa theo review trong 24 giờ sau khi kết thúc buổi 10 |

Bản chuẩn bị của buổi 1-9 gửi trước giờ bắt đầu buổi học ít nhất 2 giờ. Đây là tiến độ thực tế để nhận hỗ trợ, chưa yêu cầu hoàn tất cả milestone. Ngày, giờ cụ thể và kênh nộp bài do giảng viên công bố theo lịch lớp, múi giờ Việt Nam (UTC+07:00); không suy ra ngày học từ ngày trên tài liệu.

Học liệu phát hành theo bốn đợt để học viên đi trước được một buổi. Ngày phát hành từng đợt công bố trên kênh lớp.

| Đợt | Nội dung |
| --- | --- |
| 1 | Trước buổi 1: Starter `learner-r1.3`, tài liệu này, KC/TG/Quiz buổi 1 và 2 |
| 2 | KC/TG/Quiz buổi 3 đến 5 |
| 3 | KC/TG/Quiz buổi 6 đến 8 |
| 4 | KC/TG/Quiz buổi 9 và 10 |

<a id="timebox"></a>

**Timebox gợi ý theo công việc.** Tổng giờ tự học theo bảng trên là khoảng 58,9 giờ, gồm đọc KC/TG 20 giờ, Quiz và bản chuẩn bị khoảng 5,6 giờ, Running Project khoảng 33,3 giờ. Theo nhóm buổi, tải lần lượt khoảng 9,3 giờ (buổi 1 và 2), 16 giờ (buổi 3 đến 5), 26,3 giờ (buổi 6 đến 8) và 7,4 giờ (buổi 9 và 10). Nhờ nhịp đi trước một buổi, tải theo tuần lịch dàn đều hơn tải theo nhóm buổi (xem nhịp tuần mẫu bên dưới). Cột "Đọc KC/TG" gồm đọc, tìm hiểu KC và đọc hiểu TG. Cột "Quiz, chuẩn bị" gồm làm Quiz (khoảng 20 phút) và soạn bản chuẩn bị (khoảng 15 phút); bản chuẩn bị buổi 10 là hồ sơ Capstone, đã tính trong LR-28, LR-29. Phần làm theo TG (walkthrough) tạo một phần đầu ra của LR nên nằm trong timebox LR; timebox LR đã gồm phần sửa theo phản hồi sau buổi học.

| Buổi | Tự học | Đọc KC/TG | Quiz, chuẩn bị | Timebox LR (phút) |
| --- | --- | --- | --- | --- |
| 1 | 4,3 giờ | 120 phút | 35 phút | LR-01: 45<br>LR-02: 35<br>LR-03: 20<br>sửa theo phản hồi: 5 |
| 2 | 4,9 giờ | 125 phút | 35 phút | LR-04: 45<br>LR-05: 80<br>sửa theo phản hồi: 10 |
| 3 | 4,4 giờ | 95 phút | 35 phút | LR-06: 60<br>LR-07: 60<br>sửa theo phản hồi: 15 |
| 4 | 5,5 giờ | 130 phút | 35 phút | LR-08: 85<br>LR-09: 65<br>sửa theo phản hồi: 15 |
| 5 | 6,1 giờ | 150 phút | 35 phút | LR-10: 55<br>LR-11: 90, gồm threat model sơ bộ, AI job và ADR<br>review bất đồng bộ: 20<br>sửa theo phản hồi: 15 |
| 6 | 8 giờ | 110 phút | 35 phút | LR-12: 275, gồm tích hợp Auth scaffold và Conversation bền vững<br>LR-13: 45<br>sửa theo phản hồi: 15 |
| 7 | 8,9 giờ | 130 phút | 35 phút | LR-14: 25<br>LR-15: 55<br>LR-16: 50<br>LR-17: 95<br>LR-18: 85, gồm IH-AI-005<br>LR-19: 45<br>sửa theo phản hồi: 15 |
| 8 | 9,3 giờ | 180 phút | 35 phút | LR-20: 65<br>LR-21: 20<br>LR-22: 65, gồm hardening AI Job<br>LR-23: 85<br>LR-24: 50<br>hoàn thiện Assignment refactor: 45<br>sửa theo phản hồi: 15 |
| 9 | 4,6 giờ | 100 phút | 35 phút | LR-25: 40<br>LR-26: 40<br>LR-27: 45<br>sửa theo phản hồi: 15 |
| 10 | 2,8 giờ | 60 phút | 20 phút (Quiz) | Trước buổi, LR-28: 40<br>Trước buổi, LR-29: 20<br>Sau buổi, sửa hồ sơ theo review: 30 |

<a id="nhip-tuan-mau"></a>

**Nhịp tuần mẫu.** Lịch 3 buổi mỗi tuần, lớp học buổi tối. Mức chuẩn là 2 giờ vào ngày có lớp và 2,5 giờ vào ngày không có lớp; trần 3 giờ chỉ dùng cho hai ngày không có lớp liền trước buổi 6 (dồn M3.1) hoặc khi cần bù. Bảng dưới lấy ví dụ tuần có buổi 3, 4 và 5, ngày ghi tương đối; lịch theo ngày của lớp do giảng viên công bố trên kênh lớp.

| Ngày | Lớp | Tự học | Việc theo nhịp đi trước một buổi | Mốc |
| --- | --- | --- | --- | --- |
| Ngày 1 | Không | 2,5 giờ | M2.1 (LR-08, LR-09): 150 phút | Hạn M0.2 |
| Ngày 2 | Buổi 3 | 2 giờ | Hoàn tất M2.1: 10 phút<br>Đọc KC/TG buổi 5: 110 phút | |
| Ngày 3 | Không | 2,5 giờ | Đọc KC/TG buổi 5: 40 phút<br>Quiz, bản chuẩn bị buổi 5: 35 phút<br>M2 (LR-10, LR-11): 75 phút | Hạn M1 |
| Ngày 4 | Buổi 4 | 2 giờ | M2 (LR-10, LR-11): 105 phút<br>Đọc KC/TG buổi 6: 15 phút | |
| Ngày 5 | Không | 2,5 giờ | Đọc KC/TG buổi 6: 95 phút<br>Quiz, bản chuẩn bị buổi 6: 35 phút<br>M3.1 (LR-12, LR-13): 20 phút | Hạn M2.1 |
| Ngày 6 | Buổi 5 | 2 giờ | M3.1 (LR-12, LR-13): 120 phút | |
| Ngày 7 | Không | 3 giờ | M3.1 (LR-12, LR-13): 180 phút | |

Trong ví dụ, phần lớn M1 cùng đọc KC/TG và Quiz của buổi 4 đã làm ở tuần trước, nên khi dự buổi 3 học viên đang làm M2.1 của buổi 4. Phần sửa theo phản hồi (ví dụ sửa M1 sau buổi 3) đã tính trong khối milestone; ngày có lớp, làm phần này ngay sau buổi học và đổi chỗ với phần đọc trước cùng ngày. Bản chuẩn bị có thể soạn sớm nhưng cập nhật tiến độ mới nhất trước khi gửi. Nếu một ngày bị lỡ, bù bằng mức trần 3 giờ ở các ngày không có lớp kế tiếp đến khi đủ; phần chưa bù ghi trong bản chuẩn bị, không bỏ Quiz hoặc bản chuẩn bị.

Timebox là mốc tự kiểm tiến độ, không thay hạn nộp hoặc rubric. Timebox LR-14..18 áp cho AC Core; AC Extended làm khi còn thời gian. Phần hoàn thiện Assignment refactor trước buổi 9 dùng timebox LR-19 và khối 45 phút của buổi 8, cùng test tích lũy ở LR-20. Timebox M2 đến M5 là giả định ban đầu; timebox M3.1, M3 được hiệu chỉnh sau diễn tập M3.1 trên bản lời giải và công bố theo [mục 2.9](#chinh-sach-thay-doi), sau đó theo số đo thực tế của lớp; học viên ghi thời gian thực tế vào [AI Delivery Log](#ai-kit) để làm căn cứ. Khi một công việc vượt timebox khoảng 50% mà chưa có hướng xử lý, dừng lại, ghi phần đã làm, phần bị chặn và thời gian thực tế trong bản chuẩn bị để giảng viên hỗ trợ; không bỏ AC Core hoặc hạ expected để kịp giờ. Số phút được điều chỉnh theo số đo thực tế của lớp.

<a id="ma-tran-chuc-nang"></a>

#### 2.1.1. Chức năng cần đạt qua từng milestone

M1 lập backlog cho tất cả nhóm; M2.1 phân tích yêu cầu và spike rủi ro; M2 hoàn thiện thiết kế. M3.1 triển khai hành trình đầu tiên, M3 hoàn thiện phạm vi chức năng, M4 tổng hợp kiểm chứng và sửa lỗi, M5 kiểm bản phát hành. Công việc phát triển và test được tích lũy giữa các buổi theo ngân sách tự học.

| Nhóm | Chuẩn bị tại M2.1 và M2 | Phần phải chạy tại M3.1 | Phần phải hoàn thiện tại M3 | Kết quả tại M4 và M5 |
| --- | --- | --- | --- | --- |
| Auth và Account | Phân tích các Auth flow trên Auth scaffold (email và mật khẩu); spike khoảng cách chính sách SRS với scaffold; thiết kế UI/API/data. Google là tùy chọn (Extended). | Đăng nhập email và mật khẩu qua Auth scaffold tạo session thực cho hai tài khoản A/B. | Đăng ký, xác minh, session và logout tầng Core; recovery, đổi mật khẩu, profile, Google và linking là Extended. | Kiểm đủ nhánh tầng Core, session và lỗi (recovery, rate limit và Google nếu đã làm Extended); kiểm đăng nhập/quyền sau cài mới và restore. |
| Transactional Email | Thử gửi/nhận thật; xác định trigger, nội dung, link và trạng thái của email tầng Core (EML-001). | Hành trình đăng nhập email và mật khẩu có EML-001 và xác minh hợp lệ. | Kiểm lại EML-001 (Core) sau tích hợp; EML-002 cùng khôi phục mật khẩu, EML-003, EML-004 cùng đăng nhập Google và EML-005 là Extended. | Có thư nhận thật, kết quả hành động và kiểm lỗi gửi; cấu hình bàn giao không chứa secret. |
| Notebook | Spec thao tác, quyền, giới hạn; thiết kế trang danh sách và workspace. | Tạo, liệt kê và mở Notebook đúng owner trong hành trình đầu tiên. | Hoàn thiện cập nhật, pagination và giới hạn (xóa Notebook cùng tài nguyên con và version conflict là Extended). | Test quyền A/B và thao tác tầng Core; kiểm dữ liệu/quyền sau restore. |
| Document | Đối chiếu ingestion có sẵn, định dạng và trạng thái; thiết kế tích hợp Notebook. | Upload tài liệu hợp lệ vào đúng Notebook, xử lý `Ready`, đọc nội dung và mở citation. | Đủ định dạng, lỗi, retry, chống trùng, quota, xóa và ảnh hưởng tới nguồn. | Test đầu vào hợp lệ/lỗi, quyền, deadline và xóa khi đang xử lý; kiểm dữ liệu/index sau restore. |
| Chat và Conversation | Spec nguồn, citation, trạng thái và persistence; thiết kế API/lịch sử. | Hỏi đáp có nguồn trên cơ chế operation của Starter đã scope theo người dùng, lưu lượt và mở lại conversation sau reload/restart; chặn tài khoản B. | Danh sách, `NoEvidence`, retry và quy tắc nguồn/lịch sử (Core); đổi tên, xóa conversation, chặn công bố khi nguồn đổi giữa chừng (Extended). | Kiểm UAT, nguồn bị xóa, idempotency và chất lượng câu trả lời; kiểm lịch sử sau restore. |
| Note (Extended) | Không bắt buộc thiết kế. | Không yêu cầu. | Extended: tạo, đọc, sửa, xóa; lưu câu trả lời/Summary thành bản sao độc lập. | Nếu đã làm: kiểm conflict, quyền và quan hệ sau xóa. |
| Summary | Xác định input, output schema, nội dung kỳ vọng và giao diện. | Thiết kế đã có; chưa yêu cầu Summary chạy ở mốc này. | Tạo Summary ngắn/chi tiết, citation, xem lại (lưu thành Note là Extended). | Kiểm schema, độ dài, từng claim và nguồn; giữ kết quả hợp lệ qua phát hành/restore. |
| Quiz | Thiết kế đề, nội dung công khai/nội bộ, QuizAttempt và cách chấm. | Thiết kế đã có; chưa yêu cầu Quiz chạy ở mốc này. | Sinh đề, làm/nộp/chấm, xem kết quả, nộp lặp và làm lại. | Kiểm không lộ đáp án, nội dung câu hỏi và chấm điểm; giữ lịch sử sau restart/restore. |
| AI Job và Output | Đọc ADR-004 và [AI Job Framework](../AI_Job_Framework.md); thiết kế policy BR-08/BR-09 cho Summary và Quiz, contract Output ở mức schema, schema version, chiến lược fallback và usage. | Không yêu cầu ở mốc này. Chat giữ cơ chế operation của Starter, không chuyển vào AI Job scaffold (mã D8). | Summary/Quiz trên AI Job scaffold với policy của học viên, danh sách, lọc theo loại, mở lại, fallback và usage IH-AI-005 (Core); xóa, rename, regenerate (Extended). Đường chính của xóa tài liệu và phản hồi muộn chạy đúng. | Hardening test-first: cạnh tranh quota, restart, quyền A/B qua API, xóa tài liệu khi tác vụ đang chạy (ba thứ tự BR-08, phản hồi muộn), ca fallback giả lập; kiểm bản phát hành. |

Mỗi ô là mức hoàn thành được yêu cầu, không phải kết quả đã đạt. Nếu một AC có nhiều nhánh, phần kiểm tại M3.1 chỉ ghi kết quả nhánh đã chạy; chỉ kết luận AC đạt khi toàn bộ điều kiện áp dụng đều đạt. Checklist chức năng dẫn tới cùng [traceability matrix](#bang-ket-qua), không tạo bảng kết luận thứ hai.

#### 2.1.2. Cách sử dụng yêu cầu theo milestone

Mỗi milestone được trình bày theo sáu phần: vai trò trong SDLC và kết quả cần đạt; chức năng và công việc cần thực hiện; điều kiện hoàn thành; cách áp dụng SDLC và AI; evidence/cách nộp; rubric. Trước khi làm, xác định đầu vào, công việc đến hạn, kết quả cần trình bày và phần bàn giao cho mốc sau trong bảng dưới. Tra checklist mục 2.1.1 để biết chức năng nào phải chạy, rồi đọc milestone tương ứng để thực hiện.

M0-M2 có đầu ra chạy nền, workflow, phân tích, spike và thiết kế. M3.1 là mốc đầu tiên phải trình bày hành trình nghiệp vụ mới qua UI/API/DB; M3 hoàn thiện các chức năng còn lại. Các điều kiện hoàn thành giúp tự rà soát tiến độ; cách tính điểm và điều kiện hoàn thành khóa học vẫn theo mục 2.4-2.8.

<a id="do-ket-qua-milestone"></a>

#### 2.1.3. Đầu vào, output và cách đo từng milestone

Dùng bảng này để trình bày kết quả trong PR/bản nộp hiện có, không tạo thêm báo cáo hoặc video bắt buộc. “Trình bày” có thể là mở thiết kế, chạy task hoặc đối chiếu log đúng phiên bản, tùy loại đầu ra. Ghi input, expected, actual và evidence; phần chưa làm hoặc bị chặn không được ghi đạt.

| Milestone / công việc | Trọng tâm SDLC và đầu vào | Học viên cần làm và trình bày được | Bàn giao và ranh giới kết quả |
| --- | --- | --- | --- |
| **M0.1 / B1 / LR-01..03** | Khảo sát hệ thống và kiểm chứng AI. Fork Starter, môi trường fixture, SRS. | Chạy upload → Chat → mở citation; đăng nhập thử tài khoản seed A và B; context pack và một lượt A/B có token; kiểm JSON và ý nghĩa của một phân tích AC; chỉ ra, sửa và kiểm lại một lỗi AI rồi biến nó thành rule `AGENTS.md` có cách kiểm. | Có baseline chạy được và hiểu phần nền để lập kế hoạch. Chưa xây Auth/Notebook/tool; fixture chưa chứng minh chất lượng model thật. |
| **M0.2 / B2 / LR-04..05** | Thiết lập cách làm việc với agent. Repo chạy được, Claude Code và MCP PostgreSQL bằng role chỉ đọc. | AI Usage Charter và workflow cho một task project thực chạy qua MCP; chỉ ra success, lỗi công cụ, lệnh ghi bị database từ chối và cách chạy lại. | Có workflow/quy tắc dùng tiếp xuyên khóa. Chưa yêu cầu feature mới hoặc tự xây một nền tảng agent. |
| **M1 / B3 / LR-06..07** | Khởi tạo, lập kế hoạch và kiểm soát thay đổi. Baseline M0 và chín nhóm chức năng. | Mở backlog để giải thích phần kế thừa/phải xây, dependency, AC, estimate; kế hoạch cá nhân có bảng gate 6 pha và bản đồ AI theo pha; Charter có RACI và 2 stop condition enforced; mở PR theo PR template có tự review và AI review (`/code-review`), kết quả CI (test, lint, scan) đúng commit; dòng đầu tiên của AI Delivery Log. | Backlog và quy trình Git/CI làm đầu vào M2.1. Kế hoạch được cập nhật theo phân tích/spike; chưa kết luận chức năng đã hoàn thành. |
| **M2.1 / B4 / LR-08..09** | Phân tích yêu cầu, thiết kế test và giảm rủi ro. Backlog, SRS, quyền email/AI (Google nếu làm Extended). | Bảng trace 165 AC (153 áp dụng/12 ngoài phạm vi) từ khung giảng viên cấp: AI viết nháp, 100% AC R1 của hành trình M3.1 được kiểm, phần còn lại lấy mẫu có seed và tỷ lệ lỗi; `spec.md` của Quiz có yêu cầu EARS, AC 3 nhánh, NFR có số đo và clarification log; giải thích 1-2 yêu cầu rủi ro kèm Gherkin; trình bày kết quả spike (chính sách Auth, EML-001, AI) và quyết định có căn cứ. | Bàn giao yêu cầu, test design, khả năng/giới hạn giải pháp và việc còn mở cho M2. Code giới hạn ở spike; chưa cần UI sản phẩm hoặc toàn bộ test tự động. |
| **M2 / B5 / LR-10..11** | Thiết kế giải pháp. Yêu cầu/test design, spike và hợp đồng tham khảo. | Đi xuyên prototype (Figma hoặc HTML) → flow/state → AC → API → dữ liệu bằng bảng khớp một hành trình; C4 Context và Container; kiểm hai viewport/keyboard; OpenAPI và ERD dạng phần chênh so với Reference 1.1; giải thích một ADR hai phương án có điều kiện xem lại, fit-gap Auth scaffold, migration và module cần characterization; threat model sơ bộ có trust boundary và luồng dữ liệu ra nước ngoài; `plan.md`/`tasks.md` của Quiz; finding của subagent `design-reviewer` đã xác minh. | Thiết kế đủ để triển khai hành trình M3.1 và phần còn lại M3. Prototype thiết kế, kể cả prototype HTML, chưa phải chức năng đã chạy trên ứng dụng. |
| **M3.1 / B6 / LR-12..13** | Triển khai và test hành trình đầu tiên. Thiết kế M2; characterization trước lần sửa nền. | A đăng nhập thật → Notebook → upload → Chat/citation → mở lại conversation sau reload/restart; API chặn B; trình bày TDD red-green-regression; test đã duyệt được hook và CI bảo vệ. | Có hành trình mới chạy qua UI/API/DB trên Auth scaffold; Chat giữ cơ chế operation của Starter đã scope theo người dùng (mã D8). Phần Auth tầng Core còn lại (phiên, đăng xuất), Summary/Quiz trên AI Job scaffold hoàn thiện tại M3. |
| **M3 / B7 / LR-14..19** | Hoàn thiện chức năng, tích hợp và refactor. Hành trình M3.1 và thiết kế phần dùng chung. | Chín nhóm chức năng hoạt động theo tầng Core/Extended, Auth và email theo tầng đã chốt, Summary/Quiz, Output/lifecycle; test theo nhánh; refactor có baseline/diff/regression; review một PR do agent tạo. | Bản tích hợp và evidence cho M4. ASG01 vẫn hoàn thiện trước B9; có đủ tính năng chưa đồng nghĩa đã nghiệm thu mọi AC. |
| **M4 / B8 / LR-20..24** | Kiểm tổng hợp, chất lượng và bảo mật. Bản M3, test tích lũy, corpus/oracle. | Kết luận từng AC đến hạn (`trace_check --gate M4`), nối 19 UAT tầng Core (UAT-02 Google và UAT-03 khôi phục, đổi mật khẩu là Extended); bốn ca hardening AI Job test-first; 12 lượt nội dung AI chạy qua eval harness cùng ngoại lệ và ca fallback; `eval-fixture` làm CI đỏ khi không đạt; threat model cập nhật, `/security-review`, AI-BOM sinh tự động, UI, thời hạn xử lý và security, defect và retest có căn cứ. | Candidate cùng kết luận đủ/chưa đủ điều kiện phát hành. AC release/restore thuộc M5 còn ghi chưa kiểm/chưa đến hạn nếu chưa có evidence. |
| **M5 / B9 / LR-25..27** | Phát hành, vận hành local trên máy cá nhân và bảo trì. Candidate đã kiểm, dữ liệu nghiệp vụ. | Cài sạch R1; restore dữ liệu có sẵn và kiểm quyền A/B; sau R1 thực hiện CR thành R1.1, có regression và rollback bảo toàn dữ liệu. | Tag, gói, runbook và evidence R1/R1.1 cho Capstone. Kiểm cả dữ liệu phần mở rộng; phạm vi triển khai là local trên máy cá nhân. |
| **Capstone / B10 / LR-28..29** | Nghiệm thu, bàn giao và phản tư. Tag, source, sản phẩm và evidence thống nhất. | Demo sản phẩm đúng phiên bản; truy một yêu cầu qua các bước SDLC; trình bày AI Engineering Kit của dự án; bảo vệ quyết định kỹ thuật/AI và kế hoạch áp dụng 30 ngày có baseline và KPI lấy từ AI Delivery Log. | Bàn giao project/evidence cá nhân, giới hạn và kế hoạch áp dụng. Kế hoạch 30 ngày không giao thêm 30 ngày triển khai bắt buộc. |

Phân biệt ba kết quả: output milestone đạt/chưa đạt; verdict từng AC theo mục 16.1; điểm phản hồi theo rubric. M0-M2 có thể hoàn thành output phân tích/thiết kế trong khi AC runtime chưa kiểm. Không lấy điểm rubric thay verdict AC hoặc dùng một nhánh đã đạt để kết luận toàn bộ AC đạt.

<a id="sdlc-xuyen-milestone"></a>

#### 2.1.4. Cách làm xuyên SDLC và xử lý phần chưa hoàn tất

Milestone là điểm kiểm tiến độ học tập và sản phẩm. Trong mỗi mốc, thực hiện vòng làm việc: **đọc yêu cầu → xác lập expected → lập kế hoạch/thử phương án → thực hiện → kiểm và review → cập nhật kết quả, quyết định và việc tiếp theo**. Khi phát hiện sai hoặc thiếu, quay lại phần yêu cầu/thiết kế bị ảnh hưởng, ghi căn cứ và kiểm lại. Các quyết định nghiệp vụ đã chốt chỉ thay khi có yêu cầu thay đổi được xác nhận.

- **Yêu cầu và test phát triển cùng sản phẩm:** M2.1 xác định đủ hành vi/nhánh/input/expected và cách đo; M2 bổ sung chi tiết API/data; M3.1-M3 bổ sung test thực chạy theo thay đổi; M4 tổng hợp và kiểm phần còn thiếu. Không chờ M4 mới test hoặc kiểm quyền.
- **Thiết kế phục vụ triển khai:** spike được dùng thiết kế tối thiểu để kiểm giả định; M2 hoàn thiện thiết kế tích hợp. Khi code khác thiết kế đã chọn, giải thích lý do và cập nhật các phần liên quan trong cùng PR.
- **Chuyển tiếp theo dependency:** phần độc lập có đầu vào đủ được tiếp tục. Phần bị chặn ghi yêu cầu bị ảnh hưởng, cách đã thử, vai trò cần hỗ trợ và mốc/bước kiểm tiếp theo trong bản nộp; chưa được ghi hoàn thành hoặc tích hợp Pass. Không tự miễn AC.
- **Thời gian có AI (estimate theo công kiểm chứng):** agent rút ngắn thời gian viết code, không rút ngắn thời gian học viên xác lập expected và review. Ước lượng mỗi công việc bằng tổng: xác lập và kiểm expected của AC (gợi ý R1 6 phút, R2 3 phút, R3 1 phút mỗi AC; AC Starter đã có chỉ cần kiểm lại 1 phút), viết brief và duyệt plan (khoảng 8 phút), theo dõi agent (khoảng 5 phút, chỉ tính lúc cần chú ý), review diff (khoảng 15 phút cho PR 300 dòng, nhân 1,5 với rủi ro R1), sửa lại (khoảng 30% thời gian review) và ghi evidence (khoảng 5 phút). Các tham số là mặc định để hiệu chỉnh bằng số đo trong AI Delivery Log, không phải định mức. Tái dùng kết quả đã làm trên lớp; ghi chênh lệch và việc còn lại để giảng viên hỗ trợ trong ngân sách tại mục 2.1. Tốc độ sinh code hoặc thời gian chạy test không đại diện thời gian hoàn thành của học viên.
- **Ví dụ đối chiếu ngân sách khoảng 59 giờ:** ngân sách gồm đọc KC/TG 20 giờ, Quiz và bản chuẩn bị khoảng 5,6 giờ, Running Project khoảng 33 giờ (mục 2.1). Một issue "Notebook và quyền A/B" có 5 AC Core (2 R1, 3 R2) được ước lượng bằng 21 phút kiểm expected (2 × 6 + 3 × 3) + 8 phút brief và plan + 5 phút theo dõi agent + 23 phút review diff khoảng 300 dòng có R1 (15 × 1,5) + 7 phút sửa lại + 5 phút evidence, tổng khoảng 70 phút. Cộng các issue của M3.1 rồi so với timebox LR-12 (275 phút); chênh quá 20% thì ghi lý do, phần đã thử và trao đổi trong bản chuẩn bị, không cắt AC Core.

Khi review, dùng hồ sơ hiện có để trả lời: yêu cầu nào chi phối; expected lấy từ đâu; kết quả được kiểm bằng gì; vì sao chọn hoặc sửa giải pháp; phần còn mở ảnh hưởng bước tiếp theo thế nào. Đây là cách giải thích công việc theo SDLC, không thêm bài nộp, trọng số hoặc thủ tục phê duyệt cho mọi bước.

<a id="core-extended"></a>

#### 2.1.5. Phân tầng AC Core và Extended (D7)

AC áp dụng được chia hai tầng để học viên tập trung vào sản phẩm cốt lõi và vừa ngân sách tự học. **Danh sách công bố ngày 29/09/2026, cập nhật ngày 04/10/2026** (Requirements 1.2: Google sang Extended, thêm IH-AI-005, IH-UX-003-AC01 lên Core với phạm vi D6; Requirements 1.3: 14 AC chuyển Extended, thêm mã D8, D9), có hiệu lực từ M1; cột `tier` trong `trace/ac-trace.csv` và cột Tầng tại [mục 15.4](#pham-vi-truy-vet) ghi tầng của từng AC.

| Tầng | Ý nghĩa | Cách chấm |
| --- | --- | --- |
| **Core (92 AC)** | Auth email và mật khẩu ở mức đăng ký, xác minh, đăng nhập, phiên và đăng xuất, Notebook (gồm Document, Chat/Conversation), Summary, Quiz, phần AI Job/Output để hai công cụ chạy (gồm fallback và usage IH-AI-005), bàn phím và focus trên hành trình M3.1 và màn làm Quiz, cùng yêu cầu bảo mật, dữ liệu, kiểm chứng và phát hành cần cho M4, M5. Trong đó khoảng 20 AC Starter đã có sẵn, học viên chỉ cần kiểm lại sau khi tích hợp. | Được chấm trong rubric chức năng M3, M4 và Capstone. |
| **Extended (61 AC)** | Khôi phục, đặt lại, đổi mật khẩu và tái xác thực, hồ sơ, Note, xóa Notebook, quản lý kết quả AI (xóa, đổi tên, tạo lại), đăng nhập và liên kết Google và các nhánh tài khoản nâng cao, EML-002 đến EML-005, version conflict, chặn công bố câu trả lời Chat khi nguồn đổi giữa chừng, đo 10 thao tác không gọi AI, các yêu cầu UX, thông báo và contract test mở rộng. Làm khi phần Core đã đạt. | Không trừ điểm khi chưa làm. Nếu làm, ghi evidence như Core; nếu chưa làm, traceability matrix ghi `Extended-NotDone`, không ghi đạt. |

**Danh sách AC Extended:**

| Nhóm | AC |
| --- | --- |
| AUTH | AUTH-002-AC02, AUTH-003-AC02, AUTH-004-AC01, AUTH-004-AC02, AUTH-005-AC01, AUTH-005-AC02, AUTH-005-AC03, AUTH-005-AC04, AUTH-006-AC01, AUTH-006-AC02, AUTH-007-AC01, AUTH-007-AC02, AUTH-007-AC03, AUTH-009-AC01, AUTH-009-AC02, AUTH-010-AC01, AUTH-010-AC02 |
| MSG | MSG-001-AC01, MSG-001-AC02, MSG-002-AC01, MSG-002-AC02, MSG-003-AC03, MSG-004-AC02 |
| NB | NB-002-AC02, NB-003-AC01, NB-003-AC02 |
| DOC | DOC-003-AC02, DOC-005-AC01, DOC-006-AC02 |
| CHAT | CHAT-004-AC03, CHAT-004-AC04, CHAT-004-AC05, CHAT-005-AC02 |
| NOTE | NOTE-001-AC01, NOTE-001-AC02, NOTE-001-AC03, NOTE-001-AC04, NOTE-002-AC01, NOTE-002-AC02 |
| SUM | SUM-002-AC01, SUM-002-AC02 |
| AI | AI-003-AC02 |
| OUT | OUT-002-AC01, OUT-002-AC02, OUT-003-AC01, OUT-003-AC02 |
| DATA | DATA-001-AC01, DATA-001-AC03, DATA-001-AC05, DATA-001-AC06, DATA-002-AC02 |
| UX | UX-001-AC02, UX-002-AC02, UX-003-AC02, UX-004-AC01 |
| INT | INT-001-AC01, INT-001-AC02, INT-004-AC01 |
| NFR | NFR-001-AC04, NFR-006-AC01, NFR-006-AC02 |

- Mọi AC áp dụng không có trong bảng trên thuộc Core. Khi checklist ở các milestone mô tả một phần thuộc Extended, bảng này có hiệu lực.
- M2.1 và M2 phân tích và thiết kế phần Core; phần Extended chỉ cần ghi giả định và điểm mở rộng. Không thiết kế chi tiết Note, quản lý Output, khôi phục mật khẩu hay xóa Notebook nếu không làm.
- Khôi phục, đặt lại và đổi mật khẩu cùng tái xác thực (IH-AUTH-006-AC01, IH-AUTH-007-AC01, IH-AUTH-007-AC02, IH-AUTH-010, IH-NFR-001-AC04), hồ sơ (IH-AUTH-009) và EML-002 là Extended. IH-NFR-011-AC02 giữ Core cho phần chặn yêu cầu thay đổi dữ liệu giả mạo và bằng chứng cấu hình cookie, CSRF (UAT-21); nhánh bằng chứng tái xác thực của AC này ghi "không áp dụng khi chưa làm Extended". Không nới cấu hình cookie của Auth scaffold. Khi chưa làm, giao diện không hiển thị các chức năng này và traceability matrix ghi `Extended-NotDone`; chống lộ tài khoản ở đăng nhập (IH-NFR-001-AC05) vẫn Core.
- Đăng nhập Google và liên kết danh tính là Extended. Khi không làm, ứng dụng không hiển thị đăng nhập Google. Nếu làm đăng nhập Google mà chưa làm liên kết, email trùng tài khoản có mật khẩu phải bị từ chối an toàn, không tự liên kết và không cấp phiên (IH-AUTH-005-AC02). Hướng dẫn thư viện và fit-gap tại [Auth Integration Guide](../Auth_Integration_Guide.md).
- Email tầng Core là EML-001 (mã D5, mục 15.1). EML-002 đi cùng khôi phục mật khẩu, EML-004 đi cùng đăng nhập Google nên thuộc Extended.
- Xóa tài liệu (IH-DOC-006-AC01) vẫn Core vì LR-21, LR-22 kiểm nguồn đã xóa và dữ liệu cũ; IH-DATA-002-AC04 áp dụng cho tài liệu đã xóa (mã D9). Xóa Notebook, xóa kết quả AI kèm lần làm Quiz và xóa dữ liệu phụ thuộc (IH-NB-003, IH-OUT-003-AC01, IH-DATA-002-AC02) là Extended.
- LIM-10 áp dụng cho Tóm tắt và Quiz qua AI Job scaffold (mã D8, IH-INT-004-AC02); hỏi đáp giữ cơ chế operation của Starter. Chặn công bố câu trả lời Chat khi nguồn hoặc quyền đổi giữa chừng (IH-CHAT-005-AC02) và trạng thái tác vụ khi mất nguồn (IH-MSG-004-AC02) là Extended; publish fence được học trên Tóm tắt và Quiz (IH-DOC-006-AC01, IH-NFR-002-AC02). Với hỏi đáp, phần Core gồm loại tài liệu đã xóa khỏi yêu cầu mới, không trả đoạn trích của tài liệu đã xóa qua citation, cache hoặc replay `operation_records` (IH-DOC-006-AC01, D9); nhánh "tác vụ chưa commit kết quả" của IH-DOC-006-AC01 và IH-NFR-002-AC02 kiểm trên Tóm tắt và Quiz.
- IH-NFR-001-AC02 là Core cho token và liên kết xác minh email, hiệu lực và thu hồi phiên LIM-07. Nhánh liên kết đặt lại mật khẩu (LIM-08) và giới hạn thử LIM-09 đi cùng phần Extended nên ghi "không áp dụng khi chưa làm Extended" trong traceability matrix. Starter đã tắt endpoint đặt lại, đổi mật khẩu và cập nhật hồ sơ của Better Auth (`disabledPaths` trong `web/lib/auth/config.ts`); khi làm Extended, học viên bỏ đường dẫn tương ứng khỏi danh sách này và kiểm lại.
- Đo 10 thao tác không gọi AI (IH-NFR-006) là Extended; thời hạn xử lý tài liệu, hỏi đáp và công cụ AI (IH-NFR-007) vẫn Core.
- IH-UX-003-AC01 (bàn phím, focus, nhãn và lỗi đúng trường) là Core với phạm vi D6: bắt buộc trên hành trình M3.1 và màn làm Quiz; các màn khác kiểm khi làm Extended.
- IH-AI-005 (retry, nhà cung cấp dự phòng, usage, trần token) là Core R2, triển khai ở LR-18 trên AI Job scaffold.
- Phân tầng không đổi quy tắc kết luận AC tại mục 16.1. Backlog M1 nên có khoảng 8 đến 10 issue theo hành trình (xem [LR-06](#lr-06)), không tách mỗi AC thành một issue.

<a id="ai-kit"></a>

#### 2.1.6. AI Engineering Kit xuyên milestone

Repository ghi lại cách dự án làm việc với AI. Mỗi thành phần gắn vào output LR hiện có, không tạo bài nộp riêng; bản đồ đầy đủ tại [docs/ai/README.md](../ai/README.md).

| Milestone | Thành phần Kit hoàn thiện | Starter cấp |
| --- | --- | --- |
| M0.1 | Context pack và A/B token; rule `AGENTS.md` có cách kiểm | Template context pack |
| M0.2 | AI Usage Charter; cấu hình MCP chỉ đọc; skill workflow; hook demo | Template Charter, skill; hook `block-secrets`; role `insighthub_readonly`, `tools/mcp/`, `.mcp.json.example` |
| M1 | PR theo template (AI usage, DoD); `/code-review --comment`; AI Delivery Log; kiểm bước `eval-fixture` | PR/issue template, [Review Workflow](../ai/Review_Workflow.md), header CSV, bước `eval-fixture` trong job `application` (báo cáo) |
| M2.1 | Skill `ac-drafter`; bảng trace có nguồn gốc bản nháp; `spec.md` Quiz | `trace/ac-trace.csv`, `trace_sample.py` |
| M2 | Subagent `design-reviewer`; `plan.md`, `tasks.md` Quiz; rule domain trong `AGENTS.md` | Template subagent, spec, ADR, threat model |
| M3.1 | Danh sách test đã duyệt; hook bảo vệ test; task brief từ `tasks.md` | Hook `protect-approved-tests`, CI trailer check; Auth scaffold, AI Job scaffold, nền UI |
| M3 | Policy AI Job đầu tiên (Summary, Quiz); review PR do agent tạo; hook hoặc skill tự động hóa (LR-19) | Issue template task giao agent; `DenyAllPolicy` của AI Job scaffold |
| M4 | Golden set, grader, adapter Summary/Quiz; `eval-fixture` làm CI đỏ khi không đạt; E2E `@playwright/test` (`npm run test:pw`); AI-BOM; security review | Eval harness, giả lập lỗi provider, `generate_ai_bom.py`, `web/e2e/` |
| M5 | Release note có nhãn AI; checklist release có eval; số đo usage trước và sau CR; review migration/CI do agent sinh | Template release note, checklist review |
| Capstone | Báo cáo KPI từ Delivery Log; walkthrough Kit | `delivery_report.py` |

Số đo trong Delivery Log là số thật; nếu không đo được, để trống và ghi lý do.

<a id="kiem-chung-rui-ro"></a>

#### 2.1.7. Kiểm chứng theo rủi ro

AI viết nháp nhanh hơn khả năng người kiểm từng dòng. Khóa học dạy cách kiểm có kiểm soát thay vì chấp nhận nguyên bản nháp:

1. **Theo rủi ro:** mỗi AC có mức R1 (Auth/session, ownership, lộ hoặc mất dữ liệu, đáp án Quiz, grounding, secret), R2 (vòng đời, trạng thái, idempotency, CRUD, UI chính) hoặc R3 (thông báo, avatar, tài liệu). Giảng viên gợi ý mức trong `trace/ac-trace.csv`; hạ mức phải ghi lý do.
2. **Đúng lúc cần:** expected của AC phải `Human-verified` trước khi giao agent triển khai AC đó; không dồn kiểm 153 AC vào M2.1.
3. **Đo độ tin cậy bản nháp:** lấy mẫu có seed trên phần AI viết nháp; tỷ lệ lỗi từ 20% trở lên thì sửa ngữ cảnh hoặc prompt, sinh lại và lấy mẫu vòng mới.

| Mốc | Mức kiểm |
| --- | --- |
| M2.1 | 100% AC R1 của hành trình M3.1; 1-2 AC rủi ro phân tích sâu kèm Gherkin; mẫu 10 dòng phân tầng theo nhóm chức năng. AC R2 của hành trình kiểm đúng lúc ở dòng M3.1-M3 |
| M3.1-M3 | AC R1/R2 của task được `Human-verified` trước khi giao agent (mục DoD của PR) |
| M4 | AC Core R1: evidence trực tiếp riêng, có `test_ids`. R2: dùng chung evidence được nếu mapping rõ. R3: checklist hoặc lấy mẫu |

Cách ghi và lệnh kiểm tại [trace/README](../../trace/README.md).

### 2.2. Khởi động và trách nhiệm

1. Kiểm tài khoản Claude Pro/Max do công ty cấp và tắt thiết lập cho phép training theo mục 1.3; kiểm quyền truy cập repository Starter, tài khoản Google/email test; tạo API key provider AI tự mua (DeepSeek hoặc provider tùy chọn), đặt spending limit và chỉ lưu key trong `.env`. Ghi xác nhận privacy và phần chưa được cấp quyền vào checklist setup buổi 1 để giảng viên hỗ trợ.
2. Fork và clone Starter `learner-r1.3` theo mục 2.3; thiết lập remote `upstream` để nhận hotfix nếu có; ghi commit xuất phát rồi chạy chế độ fixture theo [GETTING_STARTED](../../GETTING_STARTED.md), tạo hai tài khoản thử bằng `make seed-users` và đăng nhập tại `/login`. Máy Windows dùng WSL2 theo [hướng dẫn Windows](../../GETTING_STARTED.md#windows-wsl2).
3. Thử tải tài liệu, hỏi đáp và mở nguồn; ghi kết quả hoặc lỗi. Fixture hỗ trợ kiểm hành vi phần mềm, chưa chứng minh chất lượng nội dung của model thật.
4. Đọc milestone đang thực hiện, lập traceability matrix theo mục 15 và bổ sung kết quả dần theo mẫu tại mục 16. Không viết lại toàn bộ SRS hoặc tạo hồ sơ riêng cho từng mẫu.
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
Đã hoàn thành: <việc và đường dẫn file/prototype/kết quả>
Output milestone: <đạt/chưa đạt, phạm vi đến hạn và lý do>
Đã kiểm tra: <lệnh hoặc bước chạy, kỳ vọng, thực tế, link log>
Quyết định với AI: <đề xuất đã giữ/sửa/bác bỏ và lý do; chi tiết trong mục AI usage của PR>
AI Delivery Log: <các dòng đã ghi cho PR của milestone>
Còn thiếu hoặc cần hỗ trợ:
```

Lấy link commit từ mục Commits của PR. Kiểm tra đúng phiên bản đó; nếu sửa mã nguồn sau khi kiểm, chạy lại phần bị ảnh hưởng và cập nhật link. Giữ log đã lọc thông tin nhạy cảm, ghi rõ chạy mô phỏng hay dịch vụ thật. Không cần lập một tài liệu riêng cho từng loại minh chứng.

<a id="danh-gia"></a>

### 2.4. Cách đọc rubric

Mỗi milestone có **rubric 100 điểm để phản hồi tiến độ**. Cột cách chấm chia điểm thành các phần cụ thể: có kết quả và minh chứng đúng thì nhận điểm phần đó; phần chưa làm, chưa đúng hoặc chưa kiểm được nhận 0. Các điểm này không tạo thêm thành phần điểm khóa.

Tài liệu kiến thức (KC) và hướng dẫn công cụ (TG) theo từng buổi được giảng viên cấp qua kênh học liệu lớp. Các liên kết ở từng milestone trỏ tới spec, hướng dẫn thiết kế và tài liệu kỹ thuật cần dùng. Dùng [mẫu minh chứng tích lũy](#evidence) trong hồ sơ hiện có, không lập lại thông tin ở nhiều bảng. Chọn module dự kiến refactor và giữ test trước lần sửa đầu tại M3.1; buổi 8 tổng hợp kiểm chứng đã tích lũy và bổ sung phần còn thiếu. Prototype thiết kế (Figma hoặc HTML) do học viên tạo tại M2 và dùng tiếp cho triển khai, test.

### 2.5. Cơ cấu điểm khóa

| Thành phần | Trọng số | Cách xác định |
| --- | --- | --- |
| Quiz | 10% | Trung bình 10 quiz theo syllabus. Mỗi quiz làm một lần trước buổi học, tự làm, không dùng AI. Quiz là reading-gate: đạt từ 70% (4/5 câu) cho thấy đã đọc KC/TG của buổi; dưới 70% thì đọc lại phần liên quan trước buổi học. Reading-gate không thêm điều kiện hoàn thành khóa. Quiz buổi 8 gồm hai block Quality và Eval, Security verification, mỗi block 50% |
| Chuẩn bị trước buổi học | 15% | Trung bình 10 bản chuẩn bị; chấm theo tiến độ và nội dung của buổi tương ứng |
| Assignment refactor | 25% | Bài refactor một module trong dự án; giao buổi 7, nộp trước buổi 9 ít nhất 12 giờ. Rubric 30/30/20/20 tại M3 |
| Capstone | 35% | Chấm toàn sản phẩm và bảo vệ cá nhân theo rubric tại Capstone |
| Chuyên cần và review | 15% | Tham dự và một lần review bất đồng bộ tại M2 |

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

Bài chuẩn bị không cần hoàn tất sản phẩm cuối milestone. Buổi 1 chưa bắt có CI hoặc Auth; khó khăn về quyền truy cập cần được ghi để giảng viên hỗ trợ. Bản chuẩn bị cùng Quiz dự kiến khoảng 35 phút mỗi buổi (cột "Quiz, chuẩn bị" tại mục 2.1): dẫn tới PR và bản ghi nộp bài đang làm, ghi phần đã làm, phần bị chặn và câu hỏi; không soạn tài liệu riêng. Mốc chuẩn bị buổi 1-9: trước giờ học ít nhất 2 giờ. Bản chuẩn bị buổi 10 là hồ sơ Capstone, nộp trước buổi 10 ít nhất 2 giờ.

### 2.7. Chuyên cần và review

Phân bổ trong đề bài: tham dự chiếm 10 điểm phần trăm toàn khóa, chất lượng review bất đồng bộ tại M2 chiếm 5 điểm phần trăm. Giữ tổng 15% đã quy định trong chương trình.

- Điểm tham dự trên thang 10 bằng số buổi tham dự hợp lệ, tối đa 10; điều kiện hoàn thành vẫn là ít nhất 8 buổi.
- Mỗi review chấm 0/4/7/10: không nộp / nhận xét chung / nhận xét gắn yêu cầu và minh chứng, có đề xuất kiểm / nhận xét đã được đối chiếu, giải thích tác động và có kết quả theo dõi.
- Điểm review là điểm của lần review tại M2. Điểm chuyên cần/review bằng `(2 × điểm tham dự + điểm review) / 3`.
- Không buộc tìm lỗi nếu sản phẩm đúng; xác nhận có phép kiểm và căn cứ vẫn được ghi nhận. Nếu chưa có bài bạn học, dùng mẫu tương đương do giảng viên cấp; không phụ thuộc tiến độ người khác.

### 2.8. Nguyên tắc phản hồi

- Ghi tên tiêu chí, điểm, căn cứ và việc cần sửa. Không chấm bằng số commit, số dòng code, số prompt hoặc số công cụ AI.
- Điểm học tập, mức năng lực đã chứng minh và trạng thái sản phẩm là ba kết quả riêng. Điểm đạt không biến tiêu chí sản phẩm chưa kiểm thành đạt.
- Lỗi chặn phát hành phải sửa và kiểm lại trước khi kết luận bàn giao. Dịch vụ hoặc quyền hoặc thông tin truy cập dịch vụ của lớp bị chặn được ghi rõ để hỗ trợ; dịch vụ mô phỏng không thay kết quả tích hợp thật.
- Thời điểm nhận bài dựa trên kênh nộp của lớp. Không tự đặt mức trừ điểm mới vì nộp muộn; áp dụng chính sách lớp đã công bố và giữ lịch sử phản hồi.

<a id="chinh-sach-thay-doi"></a>

### 2.9. Chính sách thay đổi đề bài

Requirements 1.4, SRS v1.1 và Starter `learner-r1.3` là baseline của lớp từ buổi 1. Thay đổi sau đó được xử lý như một yêu cầu thay đổi (CR), đúng cách học viên làm ở M5:

| Loại thay đổi | Cách công bố | Ảnh hưởng tới bài làm |
| --- | --- | --- |
| Hiệu chỉnh timebox, phân tầng AC hoặc rubric (ví dụ sau diễn tập M3.1) | Thông báo trên kênh lớp kèm phân tích tác động: AC, LR, timebox, rubric bị ảnh hưởng và ngày hiệu lực | Áp dụng từ milestone chưa đến hạn. Không chấm lại milestone đã nộp theo quy tắc mới bất lợi cho học viên |
| Hotfix Starter cho lỗi chặn | Tag hotfix trên Starter kèm ghi chú phát hành | Merge qua một PR `chore/sync-starter`, chạy lại test. Hotfix chỉ thêm file hoặc sửa lỗi chặn, không chạm `AGENTS.md`, `.claude/`, `trace/`, CI và lockfile của học viên trừ khi lỗi nằm ở đó |
| Sửa lỗi văn bản không đổi yêu cầu | Ghi trong nhật ký phiên bản | Không phải làm gì thêm |

Học viên phát hiện điểm mâu thuẫn hoặc thiếu trong đề bài thì ghi vào bản chuẩn bị kèm căn cứ; không tự đổi yêu cầu. Quyết định của giảng viên được công bố theo bảng trên.

<a id="m01"></a>

## 3. M0.1 - Chạy Starter và phân tích một yêu cầu InsightHub bằng AI

### 3.1 Vai trò trong SDLC và kết quả cần đạt

**Trọng tâm:** khảo sát baseline và thực hành kiểm chứng AI trước khi lập kế hoạch phát triển.

Starter chạy được hành trình upload tài liệu → hỏi đáp → mở citation trong chế độ fixture. Học viên xác định được phần nền đã có và kiểm chứng một đầu ra phân tích yêu cầu do AI tạo; chưa phải triển khai Auth, Notebook hoặc AI Tools ở mốc này.

### 3.2 Chức năng và công việc cần thực hiện

<a id="lr-01"></a>

1. **Khởi động starter.** Fork, clone, thiết lập remote `upstream`, ghi link commit nền và chạy chế độ fixture. Tạo hai tài khoản thử bằng `make seed-users`, đăng nhập lần lượt A và B tại `/login` rồi đăng xuất. Thử tải một file hợp lệ và một file lỗi, hỏi đáp và mở nguồn. Ghi lệnh, kết quả và lỗi gặp phải; giải thích vì sao fixture chưa chứng minh chất lượng AI thật. Trước khi dùng Claude, kiểm thiết lập privacy theo mục 1.3.

<a id="lr-02"></a>

2. **Tạo đầu ra có cấu trúc.** Chọn một AC trong SRS, tự xác định điều kiện ban đầu, hành vi và expected result. Cung cấp cho Claude phần SRS cùng ngữ cảnh cần thiết, loại thông tin nhạy cảm và phần không liên quan; ghi lý do lựa chọn vào context pack `docs/ai/context-pack.md` theo [template](../ai/templates/context-pack.md). Chạy một lượt A/B có và không có một quy tắc ngữ cảnh, so kết quả với expected và ghi số token (từ `/context` hoặc mức sử dụng). Tự viết JSON Schema cho đầu ra (trường, kiểu, trường bắt buộc) và rà schema với AC trong SRS. Yêu cầu Claude trả JSON gồm tình huống thành công và lỗi, kiểm bằng validator như `jsonschema` (Python) hoặc `ajv` (Node), sau đó đối chiếu từng nội dung với yêu cầu gốc. JSON hợp lệ chưa chứng minh phân tích đúng.

<a id="lr-03"></a>

3. **Phát hiện và sửa một lỗi AI.** Dùng một đề xuất sai thực tế hoặc lỗi có chủ đích do lớp cung cấp. Chỉ ra sai ở đâu bằng tài liệu, mã nguồn hoặc phép thử độc lập; sửa và kiểm lại. Ghi rõ nếu dùng lỗi có chủ đích. Biến bài học thành một rule trong `AGENTS.md` kèm cách kiểm (lệnh, test hoặc cơ chế chặn) để lỗi tương tự không lặp lại.

### 3.3 Điều kiện hoàn thành

- File hợp lệ được xử lý và dùng để hỏi đáp; file lỗi có kết quả được ghi nhận, không bị coi là thành công. Hai tài khoản seed đăng nhập và đăng xuất được.
- Một AC của InsightHub được chuyển thành tình huống thành công/lỗi, có JSON hợp lệ và nội dung đúng với SRS.
- Một lỗi AI được chỉ ra bằng căn cứ độc lập, sửa và kiểm lại, kèm rule `AGENTS.md` có cách kiểm; học viên giải thích được giới hạn của fixture.
- Context pack có nguồn/phiên bản, invariant, phần loại bỏ và kết quả A/B có token.

### 3.4 Áp dụng SDLC và AI

**Kiến thức áp dụng:**

- Cách mô hình ngôn ngữ xử lý ngữ cảnh và vì sao đầu ra có thể sai.
- Viết prompt có mục tiêu, dữ liệu đầu vào và yêu cầu đầu ra; JSON và kiểm tra schema.
- Repository instructions (`AGENTS.md`, `CLAUDE.md`) và chọn ngữ cảnh cho agent.
- Cấu trúc Web, API, cơ sở dữ liệu; luồng tải tài liệu, truy xuất, trả lời có nguồn.

| Bước áp dụng | Công việc trên InsightHub | Kết quả cần kiểm |
| --- | --- | --- |
| Khảo sát hệ thống | Chạy luồng tài liệu và hỏi đáp; xác định Web, API, DB và provider tham gia ở đâu. | Log và kết quả trên đúng commit Starter. |
| Repository instructions | Đọc `AGENTS.md`, `CLAUDE.md`, `.claude/settings.json` của Starter; phân biệt quy tắc chỉ là lời nhắc với quy tắc có cơ chế thực thi (deny, hook, test, CI). | Bổ sung rule từ lỗi LR-03 kèm cách kiểm; không tạo bài nộp riêng. |
| Phân tích yêu cầu | Tự đọc một AC, sau đó dùng Claude đề xuất tình huống và JSON. | Điều kiện ban đầu, hành động, kỳ vọng khớp AC. |
| Kiểm chứng | Kiểm schema và đối chiếu nội dung, sửa một đề xuất AI sai. | Phân biệt lỗi cấu trúc với lỗi hiểu nghiệp vụ. |

Đưa cho Claude một yêu cầu cụ thể và các trường đầu ra cần có. Yêu cầu giải thích giả định; không coi JSON đúng định dạng là nội dung đúng. Khi AI đề xuất sửa setup, kiểm nguyên nhân từ log trước khi chạy lệnh.

**Tài liệu dùng cho milestone:** [Khởi động starter](../../GETTING_STARTED.md); [kiến trúc ứng dụng](../Architecture_Starter_v1.md); [tài liệu mẫu](../../sample-docs/README.md).

### 3.5 Evidence, cách nộp bài và thời hạn

**Hạn hoàn thiện:** trước buổi 2 ít nhất 12 giờ. Push nhánh `milestone/m0.1`, mở PR vào `main` của repository cá nhân và gửi link PR kèm bản ghi nộp bài cho giảng viên. Bài gồm kết quả setup, context pack, prompt, JSON và schema, trường hợp AI sai, kết quả kiểm lại và rule đã thêm vào `AGENTS.md`.

Dùng cùng tài liệu mẫu cho demo Starter và phân tích nếu phù hợp. Evidence phải cho thấy input, kết quả upload/hỏi đáp/citation và phép kiểm độc lập; ảnh ứng dụng mở được chưa đủ.

### 3.6 Rubric đánh giá

| Tiêu chí | Điểm tối đa | Cách chấm điểm |
| --- | --- | --- |
| Môi trường và thao tác nền | 30 | Khởi động được ứng dụng: 10; tải file hợp lệ và hỏi đáp có nguồn: 10; nhận diện đúng file lỗi: 10. |
| Prompt và đầu ra JSON | 25 | Context pack và lượt A/B có token: 5; kiểm schema: 10; đối chiếu đầy đủ nội dung với yêu cầu gốc: 10. |
| Kiểm chứng và sửa lỗi AI | 30 | Tái hiện lỗi: 10; căn cứ độc lập: 10; sửa và kiểm lại đúng: 5; rule `AGENTS.md` rút ra từ lỗi có cách kiểm: 5. |
| Bài nộp và giải thích | 15 | Commit và PR truy cập được: 5; kết quả kiểm có phiên bản: 5; giải thích được giới hạn của fixture: 5. |
| **Tổng** | **100** | |

Đối chiếu tiêu chí môi trường với hành trình Document - Chat; tiêu chí prompt/JSON với AC đã chọn. Không tính đầu ra phân tích yêu cầu thành chức năng đã triển khai.

<a id="m02"></a>

## 4. M0.2 - Xây workflow AI Agent cho một task InsightHub

### 4.1 Vai trò trong SDLC và kết quả cần đạt

**Trọng tâm:** thiết lập workflow và giới hạn quyền cho cách làm việc với agent xuyên dự án.

Có một workflow agent thực chạy trên repository InsightHub, được giới hạn quyền, xử lý được lỗi công cụ và chạy lại được từ hướng dẫn. Workflow phục vụ một công việc của project, chẳng hạn đối chiếu API upload với test hiện có; mốc này chưa yêu cầu thêm chức năng sản phẩm.

Trước buổi 2, cấu hình **MCP PostgreSQL chỉ đọc** của Starter theo [GETTING_STARTED](../../GETTING_STARTED.md): role `insighthub_readonly` (migration 003), server `tools/mcp/insighthub_db_readonly.py`, file `.mcp.json` tạo từ `.mcp.json.example` và không commit. Ranh giới quyền nằm ở database (role chỉ có `SELECT`, giao dịch chỉ đọc, không đọc bảng phiên), không dựa vào lời hứa của MCP server hay của mô hình. **Phương án dự phòng:** máy không chạy được MCP dùng tool Bash của Claude Code gọi `psql` bằng chính role chỉ đọc; evidence vẫn phải có lỗi do database trả về. Nếu cả hai cách đều bị chặn, ghi lỗi và bước đã thử để giảng viên hỗ trợ; tiếp tục chuẩn bị quy tắc/task brief, chưa kết luận workflow đạt. Dùng thao tác vô hại và dữ liệu giả để kiểm từ chối.

### 4.2 Chức năng và công việc cần thực hiện

<a id="lr-04"></a>

1. **Viết AI Usage Charter cho dự án.** Charter là quy tắc dùng AI của InsightHub, gồm: phân loại dữ liệu 4 mức (Public, Internal, Confidential, Personal/Sensitive) và mức nào được đưa vào công cụ AI; thư mục và lệnh được phép; người quyết định; cách dừng và khôi phục; ghi chú pháp lý ở mức áp dụng cho dự án theo pháp luật Việt Nam (Luật Trí tuệ nhân tạo 134/2025/QH15, Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15). Phần pháp lý là nội dung đào tạo, không phải tư vấn pháp lý. Dùng [template Charter](../ai/templates/AI_Usage_Charter.md), lưu tại `docs/ai/AI_Usage_Charter.md`. Thử một thao tác ngoài quyền bằng dữ liệu giả trên máy cá nhân, ví dụ lệnh ghi qua MCP chỉ đọc. Minh chứng phải cho thấy công cụ hoặc môi trường đã từ chối thao tác; câu trả lời “không được phép” của mô hình chưa chứng minh giới hạn quyền được thực thi. Đọc tình huống prompt injection trong [`evaluation/corpus/04_injection_vi.md`](../../evaluation/corpus/04_injection_vi.md) và xác định control nào trong Charter hoặc quyền công cụ chặn được instruction (chỉ dẫn) độc hại; phần này không cần nộp riêng.

<a id="lr-05"></a>

2. **Thực hành một quy trình agent có dùng công cụ và MCP.** Chọn công việc nhỏ như đọc API, chạy một nhóm test và đối chiếu dữ liệu trong database qua MCP. Evidence MCP bắt buộc gồm ba lượt: một lượt gọi tool hợp lệ (ví dụ đếm tài liệu theo trạng thái để đối chiếu với API), một lỗi tool (ví dụ truy vấn bảng không tồn tại) và một lệnh ghi bị database từ chối (ví dụ `cannot execute INSERT in a read-only transaction` hoặc `permission denied`). Ghi mục tiêu, phạm vi, kế hoạch, checkpoint và expected result trước khi chạy trên công cụ được cấp hoặc môi trường lớp. Lưu thao tác thực tế cùng kết quả; thử một lỗi công cụ và xử lý hoặc dừng đúng. Đóng gói quy trình đã kiểm thành hướng dẫn hoặc skill có thể chạy lại, đặt tại `.claude/skills/<tên>/SKILL.md` theo [template](../ai/templates/SKILL.template.md). Đọc hai hook có sẵn trong `.claude/hooks/` là tùy chọn, giúp thấy một quy tắc được thực thi bằng sự kiện `PreToolUse`. Có thể thêm một hook ở mức demo (ví dụ ghi log hoặc chặn một lệnh trước khi chạy) để quan sát hook kích hoạt theo sự kiện; hook cho tự động hóa hoàn chỉnh thuộc LR-19.

### 4.3 Điều kiện hoàn thành

- AI Usage Charter xác định đúng repository, phân loại dữ liệu, quyền, checkpoint, cách dừng/khôi phục và ghi chú pháp lý.
- Workflow tạo ra kết quả có thể đối chiếu với mục tiêu đã ghi trước, qua thao tác công cụ và MCP thực tế (hoặc phương án dự phòng `psql` có ghi lý do).
- Có đủ ba lượt evidence MCP: gọi hợp lệ, lỗi tool, lệnh ghi bị database từ chối; `.mcp.json` không nằm trong commit.
- Có kết quả thử lỗi công cụ và một thao tác vượt quyền bị môi trường từ chối; không dùng lời từ chối của AI thay kiểm soát thực tế.
- Chạy lại được workflow đã chuẩn hóa bằng hướng dẫn hoặc skill.

### 4.4 Áp dụng SDLC và AI

**Kiến thức áp dụng:**

- Vòng làm việc của agent: lập kế hoạch, dùng công cụ, quan sát kết quả, điều chỉnh.
- MCP, giới hạn quyền, prompt injection từ ngữ cảnh không tin cậy và điểm khôi phục.
- AI Usage Charter: phân loại dữ liệu, quy tắc tài khoản và pháp lý Việt Nam ở mức áp dụng.
- Hướng dẫn dự án cho AI, skill, hook và chuẩn hóa một task lặp.

| Bước áp dụng | Công việc trên InsightHub | Kết quả cần kiểm |
| --- | --- | --- |
| Xác định task | Chọn một việc có input/output rõ, trong API, test hoặc tài liệu của project. | Mục tiêu và phạm vi đủ nhỏ để kiểm độc lập. |
| Thiết kế workflow | Dùng Claude đề xuất bước và công cụ; học viên xác định quyền và checkpoint. | Mỗi quyền gắn với một thao tác cần thiết. |
| Chạy và cải tiến | Thực chạy, thử lỗi/vượt quyền, đối chiếu kết quả và sửa hướng dẫn. | Workflow lặp lại được, không phụ thuộc suy đoán của AI. |

Để Claude đề xuất kế hoạch trước khi cấp quyền chạy. Bắt đầu bằng quyền đọc và lệnh kiểm tra cụ thể; chỉ mở quyền sửa khi task cần. Chuẩn hóa thao tác đã chạy thành hướng dẫn tái sử dụng, tránh viết quy tắc chung không gắn với dự án.

**Tài liệu dùng cho milestone:** [Kiến trúc và ranh giới hệ thống](../Architecture_Starter_v1.md); [API để chọn task thực hành](../API_Contract_Starter_v1.md).

### 4.5 Evidence, cách nộp bài và thời hạn

**Hạn hoàn thiện:** trước buổi 3 ít nhất 12 giờ. Gửi link PR của nhánh `milestone/m0.2` trong repository cá nhân và bản ghi nộp bài. Đính kèm AI Usage Charter, hướng dẫn hoặc skill, log thực hành, ba lượt evidence MCP và kết quả kiểm giới hạn quyền. Không commit `.mcp.json` hoặc mật khẩu role.

Giữ đường dẫn input, kết quả task và log đã lọc secret trong cùng hồ sơ. Ghi rõ phần nào chạy bằng công cụ thực, phần nào dùng dữ liệu giả để kiểm lỗi.

### 4.6 Rubric đánh giá

| Tiêu chí | Điểm tối đa | Cách chấm điểm |
| --- | --- | --- |
| AI Usage Charter và quyền | 25 | Charter gắn đúng repository: 10; phân loại dữ liệu và quyền rõ: 10; có cách dừng và khôi phục: 5. |
| Quy trình agent thực chạy | 30 | Kế hoạch rõ: 10; thao tác công cụ và MCP (hoặc phương án dự phòng) có log: 10; đối chiếu kết quả với mục tiêu: 10. |
| Xử lý lỗi và giới hạn | 25 | Thử yêu cầu vượt phạm vi: 10; nhận diện và xử lý lỗi công cụ: 10; khôi phục từ checkpoint: 5. |
| Tái sử dụng và nộp bài | 20 | Hướng dẫn hoặc skill chạy lại được: 10; PR và minh chứng đủ để giải thích: 10. |
| **Tổng** | **100** | |

Rubric đánh giá workflow giải quyết công việc cụ thể trong InsightHub, cùng kết quả thực thi và kiểm quyền; một bộ quy tắc AI chung chưa chứng minh workflow đã hoạt động.

<a id="m1"></a>

## 5. M1 - Lập backlog chức năng InsightHub và thiết lập Git/CI

### 5.1 Vai trò trong SDLC và kết quả cần đạt

**Trọng tâm:** khởi tạo dự án, lập kế hoạch và thiết lập kiểm soát thay đổi/chất lượng.

Có kế hoạch cá nhân cho đầy đủ chín nhóm chức năng tại mục 1.1, chỉ rõ phần Starter cung cấp, phần phải xây và phụ thuộc giữa các phần. Repository cá nhân có issue, Pull Request, tự review và CI thực chạy. Đầu vào là kết quả khảo sát Starter và workflow của M0.

### 5.2 Chức năng và công việc cần thực hiện

<a id="lr-06"></a>

1. **Lập hồ sơ dự án và backlog.** Ghi người dùng, hành trình chính và phần cần bổ sung vào Starter cho các nhóm chức năng tại mục 1.1, tách phần Core và Extended theo mục 2.1.5. Chia công việc theo **hành trình và kết quả chức năng**, khoảng 8 đến 10 issue tầng Core cho toàn dự án theo mục 2.1.5 (ví dụ: Auth cơ bản và EML-001; Notebook và quyền A/B; Document và Chat trong Notebook; AI Job và Output; Summary; Quiz; kiểm M4; phát hành M5) cộng 1 đến 2 issue `extended`, mỗi issue có checklist AC bên trong; không tạo mỗi AC một issue. Phần Extended gom vào vài issue có nhãn `extended`. Gắn các bước phân tích, thiết kế, code, test và release tương ứng. Mỗi công việc có kết quả cần đạt, AC, phụ thuộc, ước lượng theo công kiểm chứng (mục 2.1.4) và cách kiểm. Trong fit-gap, ghi phần Starter đã cấp: Auth scaffold (plumbing email và mật khẩu), AI Job scaffold (cơ chế, chưa có policy, executor, Output) và nền UI là Fit hoặc Partial, không phải phần đã hoàn thành. Đối chiếu ước lượng với ngân sách tự học khoảng 59 giờ tại mục 2.1, bao gồm đọc tài liệu, phát triển, test, sửa lỗi và chuẩn bị bảo vệ. Ghi phần vượt ngân sách và căn cứ để trao đổi với giảng viên; không giảm ước lượng hoặc bỏ tiêu chí để làm kế hoạch có vẻ vừa thời gian. Ưu tiên xác thực và quyền trước luồng nhiều người dùng.

   Kế hoạch cá nhân gồm **bảng gate 6 pha** (entry, exit criteria kiểm được, evidence, người duyệt) và **bản đồ AI theo pha** (việc AI làm, Mức AI 1 đến 4 chọn theo hậu quả và khả năng rollback, sensor, người duyệt). Hai bảng làm bản nháp ở Lab buổi 3 và hoàn thiện trong timebox LR-06. Cập nhật `docs/ai/AI_Usage_Charter.md` đã lập ở M0.2: RACI cho các quyết định chính ở mục 3 (mỗi dòng đúng một người chịu trách nhiệm cuối, coding agent không giữ vai này) và 2 stop condition có cơ chế công cụ chặn (`deny`, hook hoặc CI) ở mục 2 và 4. Ghi giá trị khởi điểm của số đo trong AI Delivery Log (thời gian review, số vòng sửa, kết quả CI lần đầu) làm baseline cho các mốc sau.

<a id="lr-07"></a>

2. **Thiết lập quy trình phát triển.** Tạo issue theo [issue template](../../.github/ISSUE_TEMPLATE/feature.md) và Pull Request theo [PR template](../../.github/pull_request_template.md) (tự rà soát bốn góc tính đúng, bảo mật, quy ước mã nguồn, thiết kế; mục AI usage; Definition of Done). Giữ mỗi PR khoảng 400 dòng diff trở xuống, không tính file sinh tự động, để vừa khả năng review; PR lớn hơn phải tách hoặc ghi lý do. Chạy Continuous Integration (CI) trên repository cá nhân, gồm test, lint, secret scan và dependency scan cho cả Web và API theo công nghệ thực tế. Workflow [`app-ci.yml`](../../.github/workflows/app-ci.yml) của Starter đã chạy test, smoke, E2E và `npm audit`; học viên thêm lint, secret scan và dependency scan bằng action có sẵn theo [hướng dẫn lint và scan M1](../M1_Lint_Scan_Guide.md), dùng một cấu hình chung cho Web và API, khoanh phạm vi vào file thay đổi và triage finding có sẵn của Starter. Kiểm bước `eval-fixture` (trong job `application` của App CI) chạy được trên fork (chế độ báo cáo `continue-on-error`; chuyển thành bước bắt buộc ở LR-23). Lưu liên kết lần chạy và đúng commit được kiểm; phân biệt lỗi quy trình CI với lỗi ứng dụng. Chạy AI reviewer theo [Review Workflow](../ai/Review_Workflow.md): tự review trước, sau đó `/code-review --comment <số PR>` trong session Claude Code mới (tách writer và reviewer); phân loại finding Fix, Reject hoặc Defer; tự xác minh một finding bằng phép kiểm độc lập. Không yêu cầu tìm đủ một lỗi cho mỗi góc rà soát. Với dependency mới do AI đề xuất, kiểm package tồn tại thật theo [hướng dẫn](../M1_Lint_Scan_Guide.md). Từ PR này, ghi mỗi PR một dòng vào `docs/ai/delivery-log.csv` với số đo thật (thời gian, finding AI, vòng sửa, kết quả CI lần đầu).

### 5.3 Điều kiện hoàn thành

- Backlog bao phủ Auth, Email, Notebook, Document, Chat/Conversation, Note, Summary, Quiz và AI Job/Output; có công việc UI, dữ liệu, test và release liên quan.
- Mỗi công việc có AC liên quan, kết quả, dependency, ước lượng và cách kiểm; phân biệt phần cần chạy tại M3.1 với phần hoàn thiện tại M3.
- Kế hoạch đối chiếu ngân sách tự học khoảng 59 giờ, ghi chênh lệch và căn cứ; không bỏ yêu cầu để làm vừa thời gian.
- CI chạy trên đúng commit, có kết quả test, lint và scan Web/API và xử lý phát hiện phù hợp; một PR theo template có AI review với một finding đã được xác minh.
- AI Delivery Log có dòng cho các PR của M1 và giá trị khởi điểm làm baseline.
- Bảng gate 6 pha có tiêu chí kiểm được, evidence và người duyệt cho từng pha. Bản đồ AI theo pha có Mức AI và sensor.
- Charter có RACI, mỗi quyết định đúng một người chịu trách nhiệm cuối, và 2 stop condition có cơ chế công cụ chặn.

### 5.4 Áp dụng SDLC và AI

**Kiến thức áp dụng:**

- Xác định người dùng, phạm vi, mục tiêu và chênh lệch giữa starter với sản phẩm cần xây.
- Chia backlog, ưu tiên, phụ thuộc và ước lượng.
- Git, Pull Request, tự review, AI code review và Continuous Integration (CI) có linter, scanner.

| Bước áp dụng | Công việc trên InsightHub | Kết quả cần kiểm |
| --- | --- | --- |
| Phân rã phạm vi | Dùng Claude đề xuất backlog từ chín nhóm chức năng; học viên đối chiếu SRS và Starter. | Không bỏ Auth/Email hoặc nhầm phần nền với phần bài làm đã hoàn thành. |
| Xếp dependency | Lập chuỗi Auth/session → ownership → Notebook → Document/Chat → Note/Summary/Quiz → release. | Mỗi công việc có đầu vào sẵn sàng trước khi triển khai. |
| Thiết lập kiểm soát thay đổi | Tạo issue/PR, tự review và chạy CI; điều chỉnh kế hoạch theo kết quả. | Yêu cầu, thay đổi và lần kiểm cùng truy được về commit. |

Dùng Claude phân rã backlog rồi tự kiểm phạm vi và thứ tự. Yêu cầu AI phản biện việc ước lượng quá thấp hoặc bỏ sót phụ thuộc. Lưu ít nhất một điều chỉnh có căn cứ từ starter hoặc kết quả chạy CI.

**Tài liệu dùng cho milestone:** [Phạm vi SRS](02_SRS_InsightHub_v1.1.md#sec-1-2); [kiến trúc starter](../Architecture_Starter_v1.md); [hướng dẫn tích hợp](#data-api).

### 5.5 Evidence, cách nộp bài và thời hạn

**Hạn hoàn thiện:** trước buổi 4 ít nhất 12 giờ. Gửi link PR nhánh `milestone/m1` và bản ghi nộp bài, gồm hồ sơ dự án, backlog, kế hoạch cá nhân (bảng gate, bản đồ AI), Charter đã cập nhật, link issue, PR có AI review và lần chạy CI. Tài liệu có thể gộp trong một file Markdown.

Trong backlog hiện có, dùng trường nhóm chức năng và milestone để thể hiện tiến độ; không cần tạo thêm báo cáo kế hoạch riêng. Chỉ rõ một điều chỉnh do học viên quyết định sau khi phản biện đề xuất AI.

### 5.6 Rubric đánh giá

| Tiêu chí | Điểm tối đa | Cách chấm điểm |
| --- | --- | --- |
| Phạm vi và phân tích starter | 20 | Người dùng và hành trình rõ: 5; phạm vi đúng: 5; chỉ rõ phần có sẵn và phải xây: 10. |
| Backlog có thể thực hiện | 20 | Công việc gắn yêu cầu và kết quả: 5; ưu tiên và phụ thuộc đúng: 5; ước lượng có căn cứ, đối chiếu ngân sách và nhận diện chênh lệch: 10. |
| Lifecycle Board và governance | 20 | Bảng gate 6 pha có tiêu chí kiểm được, evidence và người duyệt: 10; bản đồ AI theo pha có Mức AI theo rủi ro và sensor: 5; Charter có RACI đúng một người chịu trách nhiệm cuối và 2 stop condition enforced: 5. |
| Git và CI | 25 | Issue, Pull Request theo template (AI usage, DoD), tự review và `/code-review` có finding được xác minh: 10; test và lint thực chạy: 10; secret scan, dependency scan và xử lý kết quả: 5. |
| Quyết định với AI và bài nộp | 15 | Phản biện được kế hoạch do AI đề xuất: 5; AI Delivery Log đã ghi, có giá trị khởi điểm và dùng để đối chiếu estimate: 5; hồ sơ có thể kiểm lại: 5. |
| **Tổng** | **100** | |

Tiêu chí phạm vi và backlog được đối chiếu theo chín nhóm chức năng, dependency và ngân sách thực tế; số lượng issue hoặc số trang kế hoạch không thay tính đầy đủ.

<a id="m21"></a>

## 6. M2.1 - Làm rõ nghiệp vụ và thử tích hợp Auth, Email, AI

### 6.1 Vai trò trong SDLC và kết quả cần đạt

**Trọng tâm:** phân tích yêu cầu, thiết kế test và thử rủi ro kỹ thuật trước quyết định thiết kế tích hợp.

Có yêu cầu và test design cho chín nhóm chức năng, cùng evidence để quyết định thiết kế Auth, email và AI tại M2. Học viên trình bày được: cần xây hành vi nào, sẽ kiểm ra sao, giải pháp đã thử hỗ trợ đến đâu và còn việc gì phải xử lý. Đầu vào là backlog M1 và SRS; công việc gồm LR-08 phân tích/thiết kế test và LR-09 thử khả thi.

Sản phẩm của mốc này là **bảng yêu cầu/test case và kết quả spike có quyết định**. Có thể chạy code thử nghiệm độc lập, dùng script hoặc giao diện tối thiểu. Chưa yêu cầu ghép Auth, Notebook, Summary hoặc Quiz vào ứng dụng chính; hành trình sản phẩm đầu tiên đến hạn ở M3.1.

### 6.2 Chức năng và công việc cần thực hiện

<a id="lr-08"></a>

1. **Lập traceability matrix yêu cầu và test case.** Dùng khung [`trace/ac-trace.csv`](../../trace/README.md) giảng viên cấp (165 AC, mức rủi ro gợi ý, tầng Core/Extended đã chốt) để quản lý 153 tiêu chí áp dụng và 12 tiêu chí ngoài bài tập; không tự dựng bảng khác. Xây skill `ac-drafter` để AI viết nháp nhánh, input và expected từ SRS, ghi `draft_by=AI`. Kiểm theo [mục 2.1.7](#kiem-chung-rui-ro): 100% AC R1 của hành trình M3.1 chuyển `Human-verified`, AC R2 của hành trình kiểm đúng lúc trong DoD của PR giao agent; phần còn lại lấy mẫu 10 dòng bằng `python3 scripts/trace_sample.py --seed <mã học viên + ngày>`, ghi OK/Error cho từng dòng mẫu và chạy `--evaluate`; tỷ lệ lỗi từ 20% trở lên thì sửa context pack hoặc prompt của skill, sinh lại nhóm lỗi và lấy mẫu vòng mới. Ghi phiên bản SRS, mã yêu cầu thành phần nếu có, điều kiện hoặc nhánh cần kiểm, công việc triển khai, đầu vào và expected result. Chọn 1-2 yêu cầu có rủi ro để phân tích sâu, sau đó rà đủ phần còn lại; không viết lại toàn bộ SRS. Viết AC của 1-2 yêu cầu phân tích sâu theo Gherkin (Given/When/Then); kịch bản này được dùng lại làm E2E tại M4. Lập `specs/quiz/spec.md` theo [template](../../specs/_template/spec.md) cho Quiz làm đầu vào của plan và task ở M2: yêu cầu viết theo mẫu EARS kèm nguồn SRS, AC 3 nhánh (thành công, lỗi, sai quyền) cho yêu cầu rủi ro cao, NFR có điều kiện và số đo, clarification log ghi câu hỏi mở và người quyết định. Lab buổi 4 luyện các kỹ thuật này trên ví dụ Tóm tắt với brief mô phỏng; phần đó không chấm. Bao phủ luồng chính, edge case, sai quyền, đồng thời và lỗi dịch vụ. Yêu cầu về thời gian và giao diện phải có môi trường, cách đo. Dùng một bảng xuyên khóa theo [mẫu kết quả](#bang-ket-qua); chỉ kết luận một AC đạt khi mọi điều kiện áp dụng của AC đó đạt.

   Ở mốc này, test case mô tả điều kiện, dữ liệu, hành động và kết quả ở mức nghiệp vụ đủ để kiểm được. Chi tiết endpoint, selector UI, schema lưu trữ và script tự động bổ sung theo thiết kế M2 và triển khai M3.1-M3. Giữ đầy đủ nhánh cần kiểm dù chưa có code; đánh dấu đã thiết kế/chưa chạy thay vì tạo kết quả giả. Một test có thể dùng chung cho nhiều AC khi chỉ rõ điều kiện nào được chứng minh.

<a id="lr-09"></a>

2. **Thử tích hợp trước khi chốt thiết kế.** Tại M2.1, thử các khả năng có thể làm thay đổi lựa chọn giải pháp, mặc định là Auth scaffold của Starter (Better Auth email và mật khẩu) và bảng fit-gap trong [Auth Integration Guide](../Auth_Integration_Guide.md) (phương án khác cần ADR). Spike Auth chỉ tập trung khoảng cách chính sách SRS với scaffold: tài khoản chờ xác minh không truy cập dữ liệu nghiệp vụ, độ dài mật khẩu (LIM-01), thời hạn và thu hồi phiên (LIM-07). Spike email chỉ cần gửi, nhận và hành động xác minh EML-001 thật. Khôi phục mật khẩu, đăng nhập Google và liên kết tài khoản trùng email là tùy chọn (Extended). Ghi phần thư viện đã hỗ trợ, phần phải bổ sung và phụ thuộc cần giảng viên xử lý theo [hướng dẫn thử khả thi](#auth-email). Thử cấu hình DeepSeek và embedding với đầu vào sát giới hạn 60.000 ký tự; ghi số token thực tế, giới hạn ngữ cảnh, thời gian và mức sử dụng. Giả lập lỗi provider chính bằng `inject_provider_faults` của Starter ([AI Job Framework](../AI_Job_Framework.md) mục 6) làm đầu vào cho IH-AI-005; thử fallback giữa hai provider thật là tùy chọn. Phân biệt kết quả thật với mô phỏng. Hoàn thiện chức năng tại M3 và kiểm đầy đủ tại M4; kết quả thử sớm không thay nghiệm thu.

   Trước mỗi spike, ghi câu hỏi/giả thuyết, phép thử, expected và khoảng thời gian dự kiến trong kế hoạch hiện có. Dừng vòng thử khi đủ căn cứ quyết định hoặc khi xác định được phụ thuộc chặn; ghi việc còn mở và bước xử lý. Thử phương án ưu tiên trước, chỉ mở rộng thử nghiệm khi kết quả chưa giải quyết rủi ro chi phối. So sánh phương án có thể dựa trên tài liệu chính thức và kết quả thử, không bắt xây hai giải pháp hoàn chỉnh.

| Phần cần thử ở LR-09 | Kết quả học viên cần trình bày | Giới hạn và việc ở mốc sau |
| --- | --- | --- |
| Google (tùy chọn, Extended) | Đăng nhập bằng tài khoản thử được phép; server kiểm bằng chứng identity của nhà cung cấp; có phép kiểm từ chối phản hồi không hợp lệ theo rủi ro của giải pháp. | Chứng minh tích hợp identity. Account/session và quyền Notebook trong ứng dụng được thiết kế M2, triển khai M3.1-M3. |
| Email | Dịch vụ thật gửi tới inbox thử được phép; đối chiếu thư nhận và hành động xác minh EML-001 theo mục 14. Một lỗi gửi có thể kiểm bằng mô phỏng có kiểm soát. | Phân biệt kết nối/đăng nhập SMTP, dịch vụ chấp nhận gửi, thư nhận và kết quả hành động. EML-001 tích hợp tại M3.1; email Extended tích hợp tại M3 nếu làm. |
| Pending, mật khẩu và session | Dùng Auth scaffold và trạng thái thử để kiểm chặn tài khoản chờ xác minh, độ dài mật khẩu LIM-01, thời hạn và thu hồi phiên cũ (recovery và liên kết cùng email nếu làm Extended); ghi phần scaffold/thư viện hỗ trợ và phần app phải xây. | Được dùng kho dữ liệu thử và mô phỏng lỗi/thời gian cho policy. Kết quả này chưa chứng minh transaction, cạnh tranh request hoặc session của ứng dụng chính. |
| AI và embedding | Thử provider đã chọn (DeepSeek hoặc provider tùy chọn; embedding mặc định Gemini) với nguồn sát giới hạn 60.000 ký tự, cấu hình cho Summary/Quiz; kiểm output với expected từ nguồn, ghi tokens, thời gian và mức sử dụng; giả lập lỗi provider chính bằng công cụ có sẵn. | Corpus giả/tổng hợp phải có nhãn. Kết quả chỉ xác nhận phép thử đã chạy; chất lượng trên bộ nghiệm thu và 12 lượt nội dung thuộc M4. |

Tái sử dụng SDK/thư viện, phần nền và dữ liệu mẫu được cấp; tự viết phần thử cần thiết để kiểm giả thuyết. Chọn unit, API hoặc browser test theo rủi ro cần chứng minh. Số test/checkpoint, số trình duyệt và mức hoàn thiện giao diện của một bộ spike tham khảo không trở thành yêu cầu bổ sung; phạm vi UI/browser của sản phẩm vẫn theo LR-10/LR-21.

### 6.3 Điều kiện hoàn thành

- `trace/ac-trace.csv` đủ 165 AC, phân biệt 153 AC áp dụng và 12 AC ngoài phạm vi, ghi đúng nguồn gốc bản nháp; AC R1 của hành trình M3.1 `Human-verified`; có vòng lấy mẫu với seed, tỷ lệ lỗi và hành động theo ngưỡng; `python3 scripts/trace_check.py` đạt.
- `specs/quiz/spec.md` dẫn mã AC, có yêu cầu EARS kèm nguồn, AC 3 nhánh và Gherkin cho AC rủi ro cao, NFR có số đo, clarification log có người quyết định.
- Làm rõ quyền, trạng thái và lỗi theo từng chức năng; không chỉ liệt kê mã AC hoặc ghi chung “CRUD”.
- Spike Auth policy, email EML-001, AI (Google nếu làm) có giả thuyết, cấu hình, expected/actual, evidence đúng phiên bản/chế độ chạy và giới hạn; kết luận nêu rõ giữ, sửa hoặc cần thử lại phương án vì căn cứ nào.
- Phần bị chặn có evidence và bước xử lý, không được ghi tích hợp Pass. Phân tích đã làm vẫn được ghi nhận theo rubric; kết quả tích hợp còn mở phải thể hiện riêng trong output milestone.
- Cập nhật backlog/estimate và bàn giao cho M2: quyết định đã có căn cứ, phần thư viện/app chịu trách nhiệm, giả định còn mở, vai trò cần hỗ trợ và mốc kiểm tiếp. Chỉ tiếp tục phần thiết kế có đầu vào đủ theo mục 2.1.4.

### 6.4 Áp dụng SDLC và AI

**Kiến thức áp dụng:**

- Phân tích yêu cầu, AC, luồng ngoại lệ và yêu cầu phi chức năng.
- Spec-Driven Development: dùng spec làm căn cứ thiết kế, triển khai và test.
- Viết AC theo EARS và Gherkin (Given/When/Then); thử nghiệm kỹ thuật để xử lý giả định.

| Nhóm cần phân tích | Câu hỏi phải trả lời trước thiết kế |
| --- | --- |
| Auth và Email | Khi nào tài khoản được Active? Khi nào phải xác minh hoặc tái xác thực? Email nào phát sinh? Lỗi gửi ảnh hưởng thế nào tới giao dịch đã hoàn tất? |
| Notebook và Document | Ai được truy cập? Upload nào hợp lệ, trùng hoặc cần retry? Xóa Notebook/nguồn ảnh hưởng dữ liệu nào? |
| Conversation và Note | Lịch sử và bản sao được giữ đến khi nào? Xóa conversation có làm mất Note không? |
| Summary, Quiz và AI Output | Input, schema, nguồn, quota, deadline và idempotency là gì? Khi nào được trả đáp án hoặc công bố kết quả? |

Học viên tự xác lập expected result từ SRS, dùng Claude tìm thiếu sót và viết nháp test case, rồi kiểm lại từng đề xuất. Dùng kết quả spike để lựa chọn giải pháp; lưu quyết định giữ, sửa hoặc bác bỏ đề xuất AI cùng căn cứ.

Cho Claude tìm mâu thuẫn, thiếu điều kiện và edge case trong từng nhóm yêu cầu. Tự quyết định kỳ vọng trước khi nhờ AI viết test. Thử nghiệm cấu hình AI ở mốc này phục vụ quyết định thiết kế, không thay bộ đánh giá chất lượng nội dung tại M4.

**Tài liệu dùng cho milestone:** [SRS: giới hạn và nghiệp vụ](02_SRS_InsightHub_v1.1.md#sec-3-2); [bảng phạm vi từng tiêu chí](#pham-vi-truy-vet); [thử tích hợp xác thực, Google và email](#auth-email); [cấu hình mô hình](../Model_Profiles_And_Reranking.md).

### 6.5 Evidence, cách nộp bài và thời hạn

**Hạn hoàn thiện:** trước buổi 5 ít nhất 12 giờ. Gửi link PR nhánh `milestone/m2.1` và bản ghi nộp bài. Đính kèm bảng yêu cầu và test case, kết quả thử tích hợp, quyết định kỹ thuật và cấu hình mẫu không chứa secret. Phụ thuộc bị chặn có minh chứng được ghi nhận về kỹ năng phân tích; không được đánh dấu tích hợp đã đạt khi chưa chạy thật.

Trong hồ sơ hiện có, cần mở được ba phần: **bảng trace/test design (`trace/ac-trace.csv`, `trace/sampling-log.csv`, `specs/quiz/spec.md`); kết quả spike và giới hạn; quyết định/việc bàn giao M2**. Có thể gộp vào cùng file và dẫn tới log/code; không bắt tạo ba báo cáo riêng. Khi review, chọn yêu cầu đã phân tích sâu, đối chiếu expected với SRS rồi chỉ ra một kết quả spike đã ảnh hưởng quyết định thiết kế thế nào. Đánh dấu rõ test case đã thiết kế, đã chạy, chưa chạy hoặc bị chặn.

### 6.6 Rubric đánh giá

| Tiêu chí | Điểm tối đa | Cách chấm điểm |
| --- | --- | --- |
| Độ đầy đủ của yêu cầu | 30 | Trace đủ 153/12 AC, nguồn gốc bản nháp và trạng thái kiểm đúng: 5; AC R1 hành trình M3.1 kiểm 100%, luồng chính và ngoại lệ rõ: 10; lấy mẫu có seed, tỷ lệ lỗi và hành động khi vượt ngưỡng: 10; liên kết công việc và ước lượng: 5. |
| Test case và căn cứ kỳ vọng | 30 | Đầu vào và kỳ vọng cụ thể: 10; có edge case, sai quyền và xử lý đồng thời: 10; yêu cầu phi chức năng đo được: 10. |
| Thử nghiệm tích hợp | 30 | Email và khoảng cách chính sách Auth có kết quả thật (Google nếu làm), hoặc phụ thuộc bị chặn có minh chứng: 10; kiểm cấu hình AI và giới hạn đầu vào: 10; quyết định thiết kế dựa trên kết quả: 10. |
| Lập luận và hồ sơ | 10 | Chỉ ra một phát hiện từ phản biện với AI: 5; bảng yêu cầu và log có thể kiểm lại: 5. |
| **Tổng** | **100** | |

Rubric yêu cầu và test case được đối chiếu trực tiếp với hành vi chín nhóm chức năng. Điểm phân tích phụ thuộc bị chặn không xác nhận email (hoặc Google) đã tích hợp thành công.

<a id="m2"></a>

## 7. M2 - Thiết kế UI, API và schema cho các chức năng InsightHub

### 7.1 Vai trò trong SDLC và kết quả cần đạt

**Trọng tâm:** thiết kế giải pháp, đối chiếu phương án và chuẩn bị triển khai từ yêu cầu đã làm rõ.

Có thiết kế nối được từ hành trình người dùng đến UI, API, schema và test case cho phạm vi bài tập. Đầu vào là yêu cầu và kết quả spike M2.1; thiết kế đủ rõ để triển khai hành trình M3.1 và các chức năng còn lại tại M3.

### 7.2 Chức năng và công việc cần thực hiện

<a id="lr-10"></a>

1. **Prototype thiết kế (chọn Figma hoặc HTML).** Hoàn thiện màn hình UI-01 đến UI-08 trong phạm vi Tóm tắt và Quiz, chỉ cho chức năng tầng Core; nối prototype cho các hành trình chính. Tóm tắt và quản lý Output dùng màn danh sách tối thiểu ghép từ component có sẵn của nền UI (card, status, empty, skeleton). Chọn **một** trong hai hình thức, ghi lựa chọn và lý do trong bản ghi nộp bài; hai hình thức chấm cùng rubric, không cộng điểm vì chọn công cụ:

   - **Figma:** file có quyền xem cho giảng viên, ghi phiên bản đã chốt trong version history. Figma MCP là tùy chọn, không bắt buộc; tài khoản miễn phí có hạn mức lượt gọi MCP rất thấp mỗi tháng, xem hướng dẫn công cụ trước khi dùng.
   - **HTML:** prototype tĩnh có tương tác (HTML, CSS, JavaScript tối thiểu, dữ liệu giả) đặt trong thư mục `design/prototype/` của repository, mở được bằng trình duyệt mà không cần backend; điều hướng giữa các màn thể hiện hành trình chính; phiên bản là commit hoặc tag ghi trong bản ghi nộp bài. Được dùng AI dựng bản nháp từ SRS và AC, nhưng học viên phải tự đối chiếu từng màn và trạng thái với AC, ghi phần đã sửa sau review. Prototype HTML là artifact thiết kế: không import vào `web/`, không gọi API thật, không chứa secret hoặc dữ liệu thật; không merge nguyên prototype thành code production ở M3, phần markup hoặc style tái dùng được review như code mới.

   Yêu cầu chung cho cả hai hình thức: Thiết kế tại 1440 × 900 và 390 × 844 pixel CSS. Thể hiện đủ bảy trạng thái (đang xử lý, chưa có dữ liệu, lỗi, không đủ căn cứ `NoEvidence`, hết phiên, xung đột, nguồn đã xóa) cho **hành trình M3.1** Notebook - Document - Chat và màn làm Quiz; các màn còn lại thể hiện trạng thái áp dụng chính và dùng component, trạng thái dùng chung thay vì nhân bản frame. Dùng token và component của nền UI Starter: prototype HTML nhúng `design/prototype/_base/` (`tokens.css`, `base.css`); Figma dùng cùng giá trị token theo [UI Foundation](../UI_Foundation.md). Có thể bổ sung UI kit hoặc wireframe giảng viên cấp, hoặc thư viện component công khai; ghi nguồn đã dùng. Giảng viên review prototype qua link Figma có quyền xem hoặc thư mục HTML trong PR. Ghi hành vi Tab, Shift+Tab, Enter, Space và phím mũi tên theo loại điều khiển cho hành trình M3.1 và màn làm Quiz (IH-UX-003-AC01, mã D6); thể hiện thứ tự focus, giữ focus trong dialog và trả lại khi đóng. Gắn nhãn, thông báo lỗi đúng trường. Thiết kế thông tin nhà cung cấp và phạm vi dữ liệu gửi dịch vụ AI trước thao tác tương ứng theo IH-INT-002-AC03. Liên kết trạng thái giao diện với yêu cầu, API và dữ liệu; với Figma, cấp quyền xem cho giảng viên.

<a id="lr-11"></a>

2. **Thiết kế API và dữ liệu.** Mở đầu hồ sơ thiết kế bằng bảng architecture drivers và quality attributes (quyền dữ liệu, độ tin cậy nguồn, latency, maintainability) kèm cách đo, rồi sơ đồ C4 Context và Container của InsightHub đối chiếu [kiến trúc Starter](../Architecture_Starter_v1.md). Chọn một hành trình của Quiz, lập bảng khớp prototype, sequence, OpenAPI, ERD và AC; mỗi điểm lệch là finding phải xử lý trước khi code. Dựa trên mục 3.3 và 3.7 của SRS, lập sơ đồ quan hệ, từ điển dữ liệu và OpenAPI cho phạm vi bài tập, viết dạng phần chênh so với [API/Schema Reference 1.1](03_API_Schema_Reference_v1.1.zip): chỉ bảng, endpoint và trường mới hoặc khác, kèm lý do. Contract Tóm tắt và Quiz ở mức schema (input, output, lỗi). Với mỗi đối tượng, xác định trường, kiểu dữ liệu, điều kiện bắt buộc, giá trị mặc định, quan hệ, quyền đọc hoặc sửa và vòng đời. AI job và kết quả AI ghi nhà cung cấp và mô hình thực tế, usage và `finish_reason` theo IH-AI-005; xuất phát từ bảng `ai_jobs` của AI Job scaffold và nêu phần giữ, mở rộng. Phân biệt schema dữ liệu logic, schema trao đổi qua API và schema lưu trữ vật lý; không mặc định mỗi đối tượng logic phải có một bảng riêng.

   Xác định dữ liệu máy chủ quyết định, dữ liệu người dùng được nhập và dữ liệu nội bộ không được trả về. Tách nội dung Quiz trước và sau khi nộp. Phân biệt phiên bản cấu trúc `schema_version`, phiên bản thông tin mô tả `metadata_version`, tiêu đề nội dung `content.title` và tên hiển thị `display_name`. Thiết kế cách xử lý phiên bản không hỗ trợ, dữ liệu sai cấu trúc và cập nhật từ phiên bản cũ.

   Chọn module nền dự kiến phải sửa khi tích hợp hoặc refactor, ưu tiên [module legacy chỉ định](../Legacy_Modules.md); xác định hành vi cần giữ và phép characterization cần chạy trước lần sửa đầu. Việc này là phần kế hoạch tích hợp, không yêu cầu hoàn thành ASG01 tại M2.

   Mô tả giao dịch và các điều kiện phải luôn đúng khi gửi lặp, nộp Quiz, xóa nguồn, công bố kết quả và khởi động lại. Bản ghi chống gửi lặp hết hạn không được làm mất dữ liệu nghiệp vụ. Có ví dụ dữ liệu hợp lệ và không hợp lệ cho những nhánh đang thiết kế, kế hoạch migration, cùng một ADR so sánh hai phương án. Đối chiếu [hướng dẫn thiết kế và tích hợp](#data-api) trước khi chọn cách áp dụng hợp đồng tham khảo vào Starter.

   **Threat model sơ bộ.** Trong cùng hồ sơ thiết kế, vẽ data flow và trust boundary giữa trình duyệt, API, DB, tài liệu upload, RAG, provider AI, coding agent và MCP. Áp STRIDE cho các endpoint OpenAPI và thực thể ERD chính, ưu tiên Auth, ownership và Quiz. Đánh dấu luồng dữ liệu ra nước ngoài (Claude, provider AI chính và provider dự phòng học viên đã chọn như DeepSeek, Gemini, Anthropic hoặc gateway OpenAI-compatible; Ollama local nếu dùng thì không đi ra ngoài; Firebase hoặc dịch vụ Auth bên ngoài nếu dùng) và loại dữ liệu được phép đi qua theo AI Usage Charter. Tự phân loại mức rủi ro AI của InsightHub có lập luận. Ghi điều kiện lethal trifecta (dữ liệu riêng tư, nội dung không tin cậy, kênh gửi ra ngoài) đã cắt cho từng threat AI. Threat model dùng [template](../security/Threat_Model_Template.md) và được cập nhật tại LR-24.

   **Spec chain và review thiết kế bằng subagent.** Từ `specs/quiz/spec.md`, lập `plan.md` và `tasks.md` của Quiz theo [template](../../specs/README.md); mỗi task đủ nhỏ cho một PR và có AC, lệnh kiểm, stop condition (điều kiện dừng). Tạo subagent `design-reviewer` chỉ có quyền đọc theo [template](../ai/templates/subagent.template.md), chạy review OpenAPI/ERD/threat model và xác minh ít nhất một finding. Bổ sung glossary và invariant nghiệp vụ vào `AGENTS.md`. Đánh giá cơ chế kế thừa (Auth scaffold) so với SRS ghi trong bảng fit-gap của hồ sơ thiết kế: cách API xác định người dùng, thời hạn và thu hồi phiên, phần giữ, sửa hoặc thay, theo [Auth Integration Guide](../Auth_Integration_Guide.md); chỉ viết ADR Auth riêng khi thay scaffold. Viết một ADR theo [template](../adr/ADR-000-Template.md) so sánh hai phương án trên architecture driver, có mục Điều kiện xem lại, gợi ý chiến lược fallback provider hoặc mở rộng AI Job scaffold ([ADR-004](../adr/ADR-004-AI-Job-Framework.md)).

### 7.3 Điều kiện hoàn thành

- Prototype (Figma hoặc HTML) bao phủ các Auth flow tầng Core, Notebook/workspace, Document, Conversation, Summary, Quiz, danh sách và xem Output trong UI-01 đến UI-08, với các trạng thái áp dụng. Note và thao tác quản lý Output (xóa, đổi tên, tạo lại) là Extended, chỉ ghi giả định theo mục 2.1.5.
- API và schema thể hiện input/output, lỗi, session, ownership, pagination, version và dữ liệu nội bộ; không lộ đáp án Quiz trước khi nộp.
- Thiết kế thể hiện quan hệ, transaction, persistence, xóa, gửi lặp và dữ liệu qua restart/migration; các lựa chọn giữ đúng hành vi SRS.
- Có threat model sơ bộ với trust boundary, STRIDE trên API/dữ liệu, luồng dữ liệu ra nước ngoài và điều kiện lethal trifecta đã cắt.
- Hồ sơ thiết kế có C4 Context và Container, bảng khớp prototype, sequence, OpenAPI, ERD và AC cho một hành trình Quiz.
- Có ADR so sánh phương án, có điều kiện xem lại, và một nhận xét review có căn cứ; khác biệt giữa prototype, API và dữ liệu được xử lý trước code phần liên quan.
- `specs/quiz/plan.md`, `tasks.md` nối thiết kế với task; subagent `design-reviewer` có một finding đã xác minh.

### 7.4 Áp dụng SDLC và AI

**Kiến thức áp dụng:**

- Luồng người dùng, thiết kế trạng thái và khả năng sử dụng trên hai kích thước màn hình được quy định.
- Domain-Driven Design ở mức phù hợp: thuật ngữ, thực thể, quyền sở hữu và ranh giới nghiệp vụ.
- API contract, mô hình dữ liệu, migration và ADR.
- Architecture drivers, quality attributes và threat modeling của ứng dụng AI và coding agent.

| Nhóm chức năng | Phần thiết kế cần đối chiếu |
| --- | --- |
| Auth và Email | Màn hình và callback, trạng thái account/session/identity, trigger email và link/token; dữ liệu do Auth provider quản lý. |
| Notebook, Document, Conversation, Note | Quan hệ và ownership, API thao tác, danh sách, xử lý lỗi/conflict, nguồn và quy tắc xóa. |
| Summary và Quiz | Cấu hình người dùng, schema output, nguồn, bản sao Note, QuizAttempt và dữ liệu công khai trước/sau nộp. |
| AI Job và Output | State machine, deadline, quota, idempotency, version và thời điểm công bố kết quả. |

Chọn một hành trình, đi từ prototype → request/response → transaction/data → test case. Dùng Claude phản biện điểm không nhất quán; học viên quyết định giải pháp và cập nhật đồng thời các phần bị ảnh hưởng. Đây là cách áp dụng thiết kế domain và contract vào sản phẩm, không chỉ vẽ ERD.

Nhờ Claude đóng vai người dùng và reviewer API để tìm hành trình chưa xử lý. Tự đối chiếu prototype, API và dữ liệu trên cùng một tình huống. Nếu nhập dữ liệu nền chưa có chủ sở hữu, người vận hành phải chọn tài khoản và Notebook đích, kiểm quan hệ và quyền trước khi đưa vào sử dụng. Không tự gán cho người đăng ký đầu tiên; R1 không có chức năng chuyển chủ sở hữu Notebook. Review bất đồng bộ một thiết kế của bạn học hoặc mẫu lớp và ghi nhận xét có căn cứ; không phải chờ bạn học để tiếp tục.

**Tài liệu dùng cho milestone:** [SRS: dữ liệu](02_SRS_InsightHub_v1.1.md#sec-3-7); [SRS: giao diện](02_SRS_InsightHub_v1.1.md#sec-3-5); [API starter](../API_Contract_Starter_v1.md); [tích hợp xác thực và Notebook](#data-api).

### 7.5 Evidence, cách nộp bài và thời hạn

**Hạn hoàn thiện:** trước buổi 6 ít nhất 12 giờ. Gửi link PR nhánh `milestone/m2`, bản ghi nộp bài và link prototype: link Figma có quyền xem kèm phiên bản, hoặc đường dẫn `design/prototype/` kèm commit. Trong repository lưu API, sơ đồ quan hệ, từ điển dữ liệu, ví dụ hợp lệ và không hợp lệ, migration dự kiến, quyết định kiến trúc, threat model sơ bộ và nhận xét review. Có thể gộp các phần trong cùng hồ sơ thiết kế; không tạo bài nộp riêng cho từng loại minh chứng.

Dùng cùng hồ sơ thiết kế để liên kết flow - state - AC - API - data. Một liên kết đến đúng phần thiết kế đủ thay cho việc chép lại nội dung vào nhiều file; vẫn giữ link tới prototype đã chốt.

### 7.6 Rubric đánh giá

| Tiêu chí | Điểm tối đa | Cách chấm điểm |
| --- | --- | --- |
| Prototype thiết kế và hành trình | 30 | Đủ màn hình và hành trình: 10; trạng thái chính và ngoại lệ: 10; hai kích thước cùng bàn phím và quản lý focus: 10. |
| API và mô hình dữ liệu | 30 | API nhất quán với UI và cách tích hợp Starter đã chọn: 10; từ điển dữ liệu, quan hệ, trạng thái và phiên bản rõ: 10; quyền sở hữu và dữ liệu Quiz trước/sau nộp đúng: 10. |
| Độ an toàn của thiết kế | 25 | Migration có kiểm soát: 10; gửi lặp, xử lý đồng thời và phản hồi muộn: 10; phương án xử lý lỗi, khôi phục, threat model sơ bộ và finding `design-reviewer` đã xác minh: 5. |
| Quyết định và review | 15 | So sánh hai phương án có căn cứ: 5; rà soát mẫu hoặc bài bạn học có đối chiếu: 5; `plan.md`/`tasks.md` Quiz có link phiên bản thiết kế kiểm được: 5. |
| **Tổng** | **100** | |

Đánh giá tính nhất quán trên hành trình cụ thể, đặc biệt Auth/Email, quyền Notebook và Quiz trước/sau nộp; không đánh giá bằng số frame, endpoint hoặc bảng dữ liệu. Dòng API và mô hình dữ liệu chấm phần học viên điều chỉnh so với [API/Schema Reference](03_API_Schema_Reference_v1.1.zip): chọn, bỏ hoặc sửa phần nào và vì sao theo Starter và SRS. Sao chép Reference không kèm giải thích không nhận điểm cho phần điều chỉnh.

<a id="m31"></a>

## 8. M3.1 - Chạy hành trình Auth - Notebook - Document - Chat bằng TDD

### 8.1 Vai trò trong SDLC và kết quả cần đạt

**Trọng tâm:** triển khai hành trình đầu tiên, TDD và kiểm tích hợp trên ứng dụng chính.

Tài khoản A đăng nhập, tạo/mở Notebook, upload tài liệu, hỏi đáp và mở citation; conversation đọc lại được sau reload/restart. Tài khoản B bị chặn khi truy cập dữ liệu của A. Đây là hành trình tích hợp đầu tiên trên thiết kế M2, dùng Auth scaffold, cơ chế operation và nền UI của Starter; phần Auth tầng Core còn lại cùng Summary và Quiz trên AI Job scaffold được hoàn thiện tại M3.

### 8.2 Chức năng và công việc cần thực hiện

<a id="lr-12"></a>

1. **Triển khai hành trình Auth - Notebook - Document - Chat.** Hoàn thiện và kiểm lần lượt các bước dưới đây trên cùng một phiên bản:

| Bước | Chức năng học viên triển khai | Kết quả phải quan sát được |
| --- | --- | --- |
| Đăng nhập | Dùng Auth scaffold (email và mật khẩu) tạo session thực cho hai tài khoản A/B; hoàn thiện đăng ký, EML-001 và xác minh email theo chính sách SRS (chính sách là việc của học viên). Google là Extended. | Tài khoản `Active` truy cập nghiệp vụ; server xác định đúng người dùng từ session. Không dùng tài khoản giả lập để thay Auth. |
| Notebook | A tạo, liệt kê và mở Notebook của mình. | Dữ liệu đúng owner; tài khoản B không có quyền xem hoặc sửa qua UI/API. |
| Document | A upload một tài liệu hợp lệ vào Notebook, theo dõi xử lý đến `Ready`, mở nội dung. | Document thuộc đúng Notebook; ingestion/index của Starter được dùng qua kiểm quyền. |
| Chat và citation | A hỏi trên nguồn hợp lệ, nhận câu trả lời và mở vị trí nguồn tương ứng. | Kiểm nguồn trước retrieval, citation mở đúng tài liệu và vị trí còn quyền truy cập. |
| Conversation | Lưu lượt hỏi đáp và mở lại conversation. | Nội dung còn sau reload/restart; tài khoản B không đọc được bằng cách thay ID. |

Khi không chỉ định nguồn, lưu tập tài liệu `Ready` tại lần tiếp nhận đầu; nguồn được thêm sau đó không tham gia thao tác cũ. Danh sách rỗng hoặc không hợp lệ bị từ chối, không tự đổi phạm vi. Dữ liệu nghiệp vụ được lưu độc lập với operation TTL. Chat giữ cơ chế operation của Starter (idempotency, deadline LIM-11) và không chuyển vào AI Job scaffold (mã D8); học viên chỉ thêm Notebook, chủ sở hữu và Conversation bền vững. Scope `operation_records` của upload, retry, delete và chat theo người dùng (key của Starter đang toàn cục). Bảo vệ các endpoint và trang demo kế thừa (công khai ở M0.1) bằng phiên và quyền. Sau bước này, smoke, eval harness và AEV của Starter cần phiên đăng nhập: lấy cookie bằng `scripts/session_cookie.py` (tài khoản seed A hoặc B) rồi đặt `INSIGHTHUB_SESSION_COOKIE` theo [Runbook](../Runbook_Starter_v1.md#kiem-tra-sau-khi-bao-ve-endpoint); không dán cookie vào công cụ AI hoặc evidence. Kiểm tổng hợp tiếp tại M4. Trước lần sửa đầu tiên vào module nền dự kiến dùng cho bài refactor, lưu characterization test. Nếu sửa nền trong M3.1, phải giữ test và kết quả baseline trước diff đó, không chờ tới B7. ASG01 vẫn giao B7 và hoàn thiện trước B9 theo hạn tại mục 2.1.

<a id="lr-13"></a>

2. **Thực hiện TDD cho một hành vi có rủi ro.** Tự xác định kỳ vọng từ yêu cầu, kiểm xem assertion trong test có bỏ lọt lỗi hay không. Viết test cho trường hợp hợp lệ và sai quyền hoặc xung đột; ghi lần thất bại vì thiếu hoặc sai hành vi, sau đó triển khai và ghi lần đạt cùng regression test. Giữ lịch sử đúng trình tự; không dựng lại test thất bại sau khi chức năng đã hoàn thành.

   **Test-as-spec:** expected do học viên viết và duyệt trước khi giao agent triển khai. Agent không được sửa test đã duyệt (assertion, expected, fixture) để làm test đạt; nếu test sai, học viên tự sửa trong commit riêng và ghi lý do. Trong PR, ghi agent có chạm vào file test hay không, kiểm bằng diff theo thư mục test. Thêm test đã duyệt vào `.claude/approved-tests.txt`: hook `protect-approved-tests` chặn agent sửa các file này và CI (`scripts/check_approved_tests.py`) yêu cầu mọi commit sửa chúng có trailer `Test-Change-Approved: <lý do>`. Rule test-as-spec được bổ sung vào `AGENTS.md`.

### 8.3 Điều kiện hoàn thành

- Hành trình LR-12 chạy qua UI, API và DB, với Auth/session thực; không lấy dữ liệu mock hoặc `owner_id` phía client thay xác thực.
- Nguồn được chọn và lưu đúng tại lần tiếp nhận; có test nguồn không hợp lệ và tài khoản B truy cập qua API.
- Conversation còn sau reload/restart và không phụ thuộc thời hạn bản ghi thao tác.
- Chat chạy trên cơ chế operation của Starter; `operation_records` và endpoint kế thừa đã scope theo người dùng.
- PR có checklist DoD và agent task brief; ghi rõ agent có sửa test đã duyệt hay không; test đã duyệt nằm trong `.claude/approved-tests.txt`, log hook và job CI `governance` đạt.
- AC R1 và R2 của hành trình trong `trace/ac-trace.csv` đã `Human-verified` trước khi giao agent task tương ứng.
- Có một chu trình TDD với test thất bại đúng nguyên nhân, code làm test đạt và regression test; characterization test được giữ trước lần sửa module nền.

### 8.4 Áp dụng SDLC và AI

**Kiến thức áp dụng:**

- Tích hợp giao diện, API và cơ sở dữ liệu cho một hành trình hoàn chỉnh.
- Test-Driven Development: viết test thất bại đúng nguyên nhân, triển khai để test đạt, rồi cải thiện cấu trúc.
- Test-as-spec, agent task brief và Definition of Done (DoD).
- Kiểm quyền phía máy chủ và sử dụng mô phỏng đúng ranh giới.

1. Chọn Auth flow email và mật khẩu trên Auth scaffold và các API/schema cần cho hành trình từ thiết kế M2. Tự viết expected result cho quyền A/B và tập nguồn.
2. Dùng Claude đề xuất test, kiểm assertion, chạy test để thấy hành vi còn thiếu hoặc sai. Lưu kết quả trước khi triển khai.
3. Triển khai từng đoạn UI - API - DB, tái sử dụng ingestion và RAG của Starter; chạy lại test và kiểm trực tiếp hành trình.
4. Review diff về quyền, truy vấn và persistence; kiểm regression phần nền bị ảnh hưởng, cập nhật cùng traceability matrix.

Yêu cầu Claude đề xuất test từ AC trước khi sửa code. Kiểm rằng test thất bại vì hành vi cần xây, không vì môi trường hỏng. Cho AI thực hiện từng thay đổi nhỏ và review phần truy vấn và quyền; không chỉ kiểm nút trên UI. Giao việc cho agent bằng agent task brief theo mẫu mục 16.4 (mục tiêu, phạm vi file, expected, lệnh kiểm, stop condition); mỗi PR có checklist DoD: test đạt, lint/scan, kiểm quyền A/B, migration, evidence và traceability matrix được cập nhật.

**Tài liệu dùng cho milestone:** [Tích hợp xác thực và Notebook](#data-api); [Auth Integration Guide](../Auth_Integration_Guide.md); [AI Job Framework](../AI_Job_Framework.md); [UI Foundation](../UI_Foundation.md); [quyết định về nguồn](../adr/ADR-002-Source-Provenance.md); [xử lý gửi lặp](../adr/ADR-003-Operation-Idempotency.md); prototype và API đã thiết kế tại M2.

### 8.5 Evidence, cách nộp bài và thời hạn

**Hạn hoàn thiện:** trước buổi 7 ít nhất 12 giờ. Gửi link PR nhánh `milestone/m3.1` và bản ghi nộp bài. Nộp mã nguồn, test và migration, kết quả chạy hành trình của hai tài khoản A và B và link các commit cùng log thể hiện test thất bại rồi đạt.

Evidence cần nối được lần đăng nhập, Notebook, Document và Conversation trong cùng hành trình của A, cùng request bị từ chối của B. Che token/secret. Ghi nhánh Auth đã thực hiện; không kết luận toàn bộ IH-AUTH hoặc một AC nhiều nhánh đã đạt từ một lần đăng nhập.

### 8.6 Rubric đánh giá

| Tiêu chí | Điểm tối đa | Cách chấm điểm |
| --- | --- | --- |
| Luồng tích hợp thực tế | 35 | Đăng nhập và Notebook: 10; tải tài liệu/hỏi đáp/nguồn: 15; hội thoại bền vững sau khởi động lại: 10. |
| Phạm vi và phân quyền | 25 | Nguồn mặc định, tập con và đầu vào sai: 10; chặn tài khoản B qua API: 10; UI xử lý lỗi quyền: 5. |
| TDD có lịch sử | 25 | Test thất bại đúng nguyên nhân: 10; test đạt sau triển khai: 10; có test case sai quyền hoặc xung đột: 5. |
| Tái kiểm và giải thích | 15 | PR có checklist DoD, agent task brief và test đã duyệt được hook/CI bảo vệ, commit và log xác định được: 5; lệnh chạy lại rõ: 5; giải thích quyết định với AI và mô phỏng: 5. |
| **Tổng** | **100** | |

Điểm luồng tích hợp dựa trên hành trình hoạt động qua UI/API/DB; điểm quyền dựa trên server và nguồn thực tế. Phần Auth chưa thuộc hành trình này vẫn phải hoàn thiện tại M3.

<a id="m3"></a>

## 9. M3 - Hoàn thiện Auth, Email, dữ liệu nghiệp vụ, Summary và Quiz

### 9.1 Vai trò trong SDLC và kết quả cần đạt

**Trọng tâm:** phát triển tăng dần, tích hợp đủ chức năng và refactor có kiểm regression.

Bản phát triển có đầy đủ chín nhóm chức năng bắt buộc, tích hợp qua UI/API/DB và giữ đúng các quy tắc của SRS. Học viên tiếp tục từ hành trình M3.1, bổ sung các nhánh còn thiếu, test cùng chức năng và thực hiện refactor. M4 tổng hợp nghiệm thu, đánh giá AI, bảo mật và sửa lỗi còn phát hiện; không chờ M4 mới bắt đầu test.

### 9.2 Chức năng và công việc cần thực hiện

Các mã LR dùng để truy vết, không phải thứ tự coding cứng. Thiết kế và tích hợp cơ chế dùng chung LR-18 trước hoặc cùng LR-16/17: trạng thái, quyền nguồn, quota/idempotency, deadline, schema validation và lưu kết quả. Tái dùng phần quyền nguồn và persistence đã kiểm cho Chat ở M3.1; Tóm tắt và Quiz dùng AI Job scaffold. Không chờ hai tool xong mới bổ sung quyền hoặc persistence.

Các checklist dưới đây làm rõ phần chức năng phải hoàn thiện, không thay AC chi tiết và giới hạn của SRS. Đối chiếu mã yêu cầu tại mục 1.1 và [mapping từng AC](#pham-vi-truy-vet), cập nhật kết quả trong cùng traceability matrix. Phần được chấm theo tầng Core/Extended tại [mục 2.1.5](#core-extended) (công bố 29/09/2026, cập nhật 04/10/2026).

<a id="lr-14"></a>

1. **Hoàn thiện Auth và transactional email tầng Core.** Bổ sung phần tầng Core chưa làm ở M3.1: thời hạn và thu hồi phiên LIM-07, đăng xuất xóa dữ liệu riêng trên client; kiểm lại đăng ký, xác minh và EML-001 sau tích hợp với dữ liệu Notebook qua UI/API. Phạm vi chấm theo tầng Auth đã chốt tại [mục 2.1.5](#core-extended); nhánh Extended làm khi Core đã đạt. Auth scaffold của Starter cấp plumbing email và mật khẩu (Better Auth, bảng user/session, `current_user`, `/login` tối thiểu); fit-gap theo [Auth Integration Guide](../Auth_Integration_Guide.md). Starter cấp hạ tầng email tối thiểu: mail catcher Mailpit (Compose profile `mail`) và adapter SMTP `api/app/core/mailer.py` theo [hướng dẫn Mailpit](../../GETTING_STARTED.md#email-local-với-mailpit-tùy-chọn). Trigger, nội dung, link/token và trạng thái gửi của email tầng Core (EML-001) do học viên xây; evidence thư nhận thật theo mục 14. Các phần Extended trong bảng dưới: khôi phục, đặt lại và đổi mật khẩu cùng EML-002, EML-005 (AUTH-006-AC01, AUTH-007-AC01/02, AUTH-010-AC01/02), hồ sơ (AUTH-009-AC01), gửi lại xác minh và phiên chờ xác minh (AUTH-002-AC02), rate limit (AUTH-003-AC02, AUTH-006-AC02), đăng nhập Google (AUTH-004-AC01/02), liên kết Google cùng email và từ chối liên kết không an toàn (AUTH-005-AC01..04), EML-003, EML-004, reset tài khoản chờ xác minh (AUTH-007-AC03), avatar (AUTH-009-AC02).

| Chức năng Auth | Công việc và kết quả cần hoàn thiện |
| --- | --- |
| Đăng ký và xác minh email | Kiểm input, tạo `PendingVerification`, gửi EML-001; link hợp lệ chuyển `Active`, link sai/hết hạn/đã dùng không kích hoạt; tài khoản chờ xác minh không truy cập dữ liệu nghiệp vụ. Extended: gửi lại tuân rate limit; session chờ xác minh chỉ cho xem trạng thái, gửi lại email và logout; luồng recovery công khai theo UC-02.A4. |
| Đăng nhập email/mật khẩu | Tài khoản `Active` đăng nhập và mở danh sách Notebook của mình; email hoặc mật khẩu sai có cùng thông báo. Rate limit (Extended) kiểm cả qua UI và API nếu làm. |
| Đăng nhập Google (Extended) | Danh tính mới có email được Google xác minh tạo tài khoản `Active`; lần sau vào đúng tài khoản/dữ liệu. Hủy đăng nhập hoặc phản hồi/token/email không hợp lệ không tạo session hay hoàn tất tài khoản. |
| Liên kết Google cùng email (Extended) | Với tài khoản `Active`, kiểm phản hồi Google và mật khẩu hiện tại trong cùng giao dịch theo LIM-19. Với `PendingVerification`, hoàn tất UC-02.A4 để vô hiệu mật khẩu, session và link cũ trước khi cấp quyền nghiệp vụ; sau đó bắt đầu lại Google và xác nhận mật khẩu mới. Không tự liên kết chỉ vì trùng email. |
| Quên/reset mật khẩu (Extended) | Phản hồi công khai không tiết lộ tài khoản. Tài khoản có mật khẩu nhận EML-002; tài khoản chỉ dùng Google nhận EML-004 (Extended, khi đã làm Google). Link hợp lệ đổi mật khẩu và thu hồi session cũ; sai/hết hạn/đã dùng không đổi dữ liệu. Reset tài khoản chờ xác minh không tự cấp session hoặc liên kết Google. |
| Profile và đổi mật khẩu (Extended) | Xem email, tên, phương thức và trạng thái xác minh; sửa tên, dùng avatar mặc định hoặc Google theo SRS. Đổi mật khẩu có tái xác thực và thu hồi session cũ; tài khoản chỉ dùng Google không có chức năng đổi mật khẩu ứng dụng. R1 không đổi email hoặc upload avatar. |
| Session và logout | Reload vẫn đúng người dùng khi session hợp lệ; logout/hết hạn/thu hồi chặn request cũ và dọn dữ liệu riêng trên client. Kiểm lại session, quyền và trạng thái trước khi hiển thị phản hồi AI muộn. |

Rate limit LIM-09 là Extended: nếu làm, kiểm giới hạn theo tài khoản và IP trong cửa sổ trượt; đăng nhập thành công không xóa các lần sai còn hiệu lực, yêu cầu bị chặn không kéo dài cửa sổ bằng cách ghi thêm lỗi. Thu hồi session khi logout theo LIM-07 là Core; tái xác thực LIM-19 đi cùng đổi mật khẩu và liên kết Google nên là Extended. Nếu làm Extended, nhánh tiếp nhận tài khoản chờ xác minh phải vô hiệu mật khẩu, session và link cũ trước khi cấp quyền nghiệp vụ.

| Email | Trigger và kết quả phải kiểm |
| --- | --- |
| EML-001 - Xác minh email | Đăng ký (gửi lại xác minh nếu làm Extended); người dùng nhận thư, mở link đúng account và xác minh theo thời hạn/quy tắc dùng một lần. |
| EML-002 - Reset mật khẩu (Extended) | Yêu cầu recovery hợp lệ cho tài khoản có mật khẩu; nhận thư và dùng link để reset, kiểm link sai/hết hạn/đã dùng. |
| EML-003 - Thông báo liên kết Google (Extended) | Liên kết thành công; thư thông báo đúng sự kiện, không dùng thư này để cấp quyền liên kết. Lỗi chuyển giao không làm mất liên kết đã hoàn tất. |
| EML-004 - Hướng dẫn tài khoản Google (Extended) | Yêu cầu recovery cho tài khoản chỉ dùng Google; thư hướng dẫn đúng phương thức, không tự tạo mật khẩu ứng dụng. |
| EML-005 - Thông báo thay đổi mật khẩu (Extended) | Reset hoặc đổi mật khẩu thành công; thư thông báo đúng sự kiện. Lỗi gửi không hoàn tác mật khẩu hoặc khôi phục session đã thu hồi. |

Kiểm các email tầng Core (và Extended nếu làm) bằng cấu hình thật và hộp thư nhận theo [hướng dẫn Auth/Email](#auth-email), gồm nội dung, link, lỗi, thời hạn và rate limit áp dụng. Provider chấp nhận gửi chưa chứng minh đã nhận thư; fixture chỉ bổ sung kiểm lỗi, không thay evidence tích hợp thật.

<a id="lr-15"></a>

2. **Hoàn thiện Notebook, Document, Conversation (Core) và Note (Extended).** Triển khai các thao tác được quy định riêng cho từng đối tượng, cùng UI, API và persistence tương ứng. Phần Extended trong bảng dưới: version conflict và xóa Notebook cùng dữ liệu phụ thuộc (NB-002-AC02, NB-003-AC01, NB-003-AC02, DATA-002-AC02); retry trên UI, trang chi tiết và dọn dữ liệu sau xóa Document (DOC-003-AC02, DOC-005-AC01, DOC-006-AC02); đổi tên, xóa và conversation mất nguồn cuối (CHAT-004-AC03..05); toàn bộ Note.

| Đối tượng | Checklist chức năng | Kết quả cần kiểm |
| --- | --- | --- |
| **Notebook** | Tạo, liệt kê/phân trang, mở; đổi tên/mô tả có validation; áp dụng quota. Extended: version conflict; xóa có xác nhận và hủy. | Owner lấy từ session; dữ liệu, thứ tự và thời điểm đúng SRS. Nếu làm xóa Notebook: chặn mọi tài nguyên con, lịch sử và job đang chạy; thực hiện chính sách xóa vật lý theo LIM-13. |
| **Document** | Upload TXT, Markdown và PDF có văn bản; xem `Processing`, `Ready`, `Failed`; retry lỗi, xem metadata/nội dung, mở citation và xóa. | Kiểm nội dung thực, định dạng và giới hạn; xử lý file rỗng, PDF ảnh/mã hóa và byte trùng theo SRS. Retry tạo lần xử lý mới cho cùng Document, không nhân bản Document/chunk; chống trùng trong đúng Notebook. Không tự thêm chức năng sửa nội dung file gốc. |
| **Chat và Conversation** | Hỏi trên nguồn hợp lệ; phân biệt `Answered`, `NoEvidence`, `Failed`; tạo, liệt kê, mở lịch sử. Extended: đổi tên có version, xóa có xác nhận, conversation mất nguồn cuối (CHAT-004-AC03..05). | Lượt lưu câu hỏi, kết quả, trạng thái, nguồn và thời điểm; thứ tự đúng, còn sau reload/restart. Mỗi câu hỏi được xử lý độc lập, UI làm rõ giới hạn ngữ cảnh. Retry/gửi lặp đúng SRS; mất nguồn không cấm xem/đổi tên/xóa lịch sử hợp lệ, nhưng không cho hỏi trên tập nguồn rỗng. |
| **Note (Extended)** | Tạo, liệt kê, mở, sửa tiêu đề/nội dung có version conflict; xóa có xác nhận/hủy; lưu câu trả lời hoặc Summary hợp lệ thành Note. | Không lưu `NoEvidence`/`Failed` thành câu trả lời thành công. Bản sao độc lập có provenance, sửa Note không sửa nội dung gốc; xóa conversation/output không xóa Note đã sao chép. Xóa Note không xóa nguồn, nhưng xóa Notebook vẫn chặn Note. |

Server kiểm quyền đối tượng thực sự được truy cập, không tin `owner_id` hoặc Notebook do client gửi. Kiểm tài khoản B thay ID để đọc/sửa/xóa tài nguyên của A. Giữ persistence, thứ tự danh sách, pagination ở nơi SRS quy định và thời điểm cập nhật theo mục 3.7.3. Nguồn đã xóa không được đọc lại qua citation hoặc cache; lịch sử hợp lệ được giữ với trạng thái nguồn không còn khả dụng theo BR-08. Kiểm ảnh hưởng xóa tài liệu khi AI đang chạy theo LR-18.

<a id="lr-16"></a>

3. **Xây dựng Tóm tắt.** Cho chọn bản ngắn 150-250 từ hoặc chi tiết 400-600 từ, mặc định ngắn. Nội dung có tổng quan, ý chính gắn nguồn và điểm cần chú ý; phản ánh các tài liệu đã chọn và nêu mâu thuẫn nếu có. Nếu không ghi nhận điểm đặc biệt, nêu rõ thay vì tạo mâu thuẫn giả. Kiểm cấu trúc, độ dài và tham chiếu trước khi lưu; đánh giá tính đúng của nội dung riêng theo bộ dữ liệu nghiệm thu. Prompt và schema output đặt trong file hoặc hằng có phiên bản (theo mẫu `PROMPT_VERSION` của Starter) và lưu phiên bản vào kết quả để AI-BOM và eval truy được. Ghi usage cho mỗi lời gọi model bằng `record_usage` (IH-AI-005-AC02). Extended (SUM-002): lưu thành ghi chú tạo bản sao độc lập; nếu vượt giới hạn ghi chú, cho người dùng sửa trước khi lưu, không cắt ngầm.

<a id="lr-17"></a>

4. **Xây dựng Quiz.** Cho chọn 5 hoặc 10 câu, mặc định 5; mỗi câu có bốn lựa chọn khác nhau và đúng một đáp án đúng. Trước khi nộp, mọi đường đọc phục vụ làm bài chỉ trả câu hỏi và lựa chọn, không trả đáp án, giải thích hoặc điểm; chỉ ẩn ở giao diện là chưa đủ. Máy chủ kiểm câu và lựa chọn thuộc đúng đề, từ chối điểm do client gửi, tính câu bỏ trống là sai và làm tròn điểm phần trăm đến một chữ số thập phân.

   Chấm và lưu lựa chọn, điểm, thời điểm nộp một lần nhất quán. Khi nộp lại cùng định danh lần làm đã nộp, trả kết quả đã lưu nếu còn quyền, kể cả khi dữ liệu lựa chọn gửi lại khác; không chấm lại hoặc ghi đè. Làm lại tạo lần làm mới; các lần đã nộp mở lại được sau khởi động lại. Định danh lần làm Quiz khác mã chống gửi lặp của AI job tạo nội dung. R1 không lưu nháp từng lựa chọn trước khi nộp; giao diện thông báo giới hạn này. Tạo đề Quiz chạy qua AI Job scaffold và ghi usage như Tóm tắt. Màn làm Quiz đáp ứng bàn phím, focus và nhãn theo IH-UX-003-AC01 (mã D6).

<a id="lr-18"></a>

5. **Hoàn thiện vòng đời công cụ AI trên AI Job scaffold.** Starter cấp cơ chế dùng chung ([AI Job Framework](../AI_Job_Framework.md), [ADR-004](../adr/ADR-004-AI-Job-Framework.md)): tiếp nhận có idempotency theo người dùng, quota LIM-10, deadline LIM-11, publish fence, đọc trạng thái, envelope lỗi có `Retry-After`. Học viên viết policy BR-08/BR-09, executor, schema, Output và các kiểm bên dưới; scaffold không làm AC nào tự đạt. Chọn 1-3 nguồn `Ready` cùng Notebook, tổng tối đa 60.000 ký tự; kiểm cấu trúc, định danh, nguồn, quyền và thời hạn trước khi công bố. Có danh sách, lọc theo loại Tóm tắt/Quiz và xem (Core, IH-OUT-001). Extended (IH-OUT-002, IH-OUT-003): xóa kết quả kèm các lần làm Quiz liên quan, đổi tên và tạo lại; tạo lại sinh bản độc lập liên kết bản gốc, đổi tên chỉ đổi `display_name` và phiên bản thông tin mô tả, giữ nội dung AI đã lưu.

   Tóm tắt và Quiz dùng chung quota theo người dùng (mã D8): tối đa một AI job đang chạy và 10 yêu cầu mới được tiếp nhận trong 60 giây. Hỏi đáp giữ cơ chế operation của Starter và không tính vào quota này trong bài tập. Đối soát mã thao tác trước khi tính lượt mới. Gửi lại cùng mã sử dụng nguồn, cấu hình và giá trị mặc định đã lưu từ lần đầu; không tính lại theo dữ liệu hiện tại. Cùng mã với dữ liệu khác trả xung đột, đổi thứ tự cùng tập nguồn không tạo yêu cầu khác, ID nguồn lặp bị từ chối. Kiểm và lưu quota phải nhất quán khi yêu cầu đến đồng thời.

   Phân biệt `NoEvidence`, `Failed` và kết quả thành công. Khởi động lại hoặc thử lại nội bộ không đặt lại thời hạn: job hết hạn phải kết thúc trước khi tiếp tục xử lý hoặc trả như đang chạy hợp lệ; giải phóng suất khi kết thúc. Khi xóa nguồn, kiểm riêng ba trường hợp BR-08 theo thứ tự hoàn tất giao dịch trên máy chủ: xóa trước công bố thì chặn thành công; công bố trước xóa thì giữ lịch sử với nguồn không còn khả dụng; phản hồi đến muộn phải đối soát phiên, quyền và trạng thái trước khi hiển thị. Xóa Notebook (chặn cả lịch sử) và xóa kết quả Quiz (xóa các lần làm liên quan) là Extended. Kiểm giới hạn ở đúng biên và vượt biên, không cắt dữ liệu ngầm. Tại M3, đường chính của các quy tắc trên phải chạy đúng; bốn ca hardening (cạnh tranh quota, restart giữa tác vụ, quyền A/B qua API, xóa tài liệu khi tác vụ đang chạy theo ba thứ tự BR-08) viết test-first và hoàn thiện ở M4 cùng [LR-22](#lr-22).

   **Lỗi nhà cung cấp và ngân sách token (IH-AI-005).** Retry có giới hạn đã có trong `providers.post_json` và nằm trong deadline của job. Học viên bổ sung chuyển sang provider dự phòng đã cấu hình khi provider chính vẫn lỗi khả dụng (timeout, 429, 5xx, lỗi kết nối); không fallback sang fixture; kết quả từ provider dự phòng qua cùng bước kiểm schema, grounding và citation. Lỗi sai schema hoặc thiếu căn cứ không kích hoạt fallback. Ghi usage mỗi lời gọi model (provider, model, `prompt_version`, token vào, token ra, latency, `finish_reason`, chi phí ước tính), không chứa prompt hay nội dung nguồn. Áp trần token đầu ra; đầu ra bị cắt vì chạm trần không lưu là `Succeeded`. Kiểm bằng giả lập lỗi provider của Starter, không cần gọi dịch vụ trả phí.

<a id="lr-19"></a>

6. **Refactor một module và tự động hóa một task.** Chọn một [module legacy chỉ định](../Legacy_Modules.md): `api/app/core/config.py` (`validate_configuration`) hoặc `api/app/services/ingestion.py` (`extract_source`); được chọn module khác nếu nêu lý do theo tài liệu đó. Không chọn các module đã làm ví dụ trong học liệu (`reranking.py`, `chunking.py`, `retrieval._pack_contexts`, `embeddings._real_embed`) và phần scaffold của `learner-r1.3`. Chọn vấn đề cụ thể trong module, sử dụng test đã lưu trước lần sửa đầu và bổ sung phần còn thiếu. Lập kế hoạch, refactor, kiểm regression và so sánh trước/sau. Để chứng minh test bắt lỗi, chạy mutation testing giới hạn trong một file của module và phân tích mutant sống theo [Module legacy](../Legacy_Modules.md). Chuẩn hóa một task lặp thành hướng dẫn hoặc skill kết hợp script hay hook đã thực chạy, ưu tiên dùng lại và mở rộng skill từ M0.2; hook cần có sự kiện kích hoạt và log, không lấy chạy tay làm evidence hook. Đây là bài Assignment trong cùng dự án, được giao chính thức ở buổi 7; việc giữ test trước thay đổi từ buổi 6 không tạo bài tập riêng.

   **Bắt buộc:** review một PR do coding agent tạo trong bài làm (task giao qua issue template "Task giao agent" hoặc `tasks.md`): kiểm diff, test và phạm vi file, chạy quy trình [Review Workflow](../ai/Review_Workflow.md), ghi finding và quyết định merge, sửa hoặc bác bỏ. **Stretch, không trừ điểm:** giao một task cho background agent chạy trên nhánh hoặc worktree riêng, review PR kết quả và ghi thời gian, chi phí.

### 9.3 Điều kiện hoàn thành

- Auth và email tầng Core (đăng ký, xác minh, đăng nhập, phiên, đăng xuất, EML-001) hoạt động theo LR-14; có kết quả tích hợp thật, link sai/hết hạn và session liên quan.
- Notebook, Document và Conversation có các thao tác, trạng thái, quyền và vòng đời tầng Core tại LR-15; Note nếu làm (Extended).
- Summary và Quiz chạy từ chọn nguồn đến lưu/xem lại; Quiz được chấm tại server, bảo vệ đáp án và xử lý nộp lặp đúng.
- AI Job/Output của Tóm tắt và Quiz chạy trên AI Job scaffold với policy của học viên: trạng thái, quota, idempotency, deadline, danh sách và mở lại; fallback, usage và trần token theo IH-AI-005. UI hành trình M3.1 và màn làm Quiz đủ trạng thái và bàn phím; Summary và quản lý Output có UI tối thiểu. Xóa, đổi tên và tạo lại là Extended.
- Code, test, migration và CI được cập nhật; phần chưa đạt được ghi rõ. Refactor có characterization test, diff và regression test, tiếp tục hoàn thiện đến hạn Assignment; có một PR do agent tạo đã được review và ghi quyết định.

### 9.4 Áp dụng SDLC và AI

**Kiến thức áp dụng:**

- Triển khai theo spec, quản lý trạng thái, giao dịch, giới hạn và tính nhất quán dữ liệu.
- Characterization test để ghi nhận hành vi hiện hữu trước thay đổi, refactor và regression test.
- Đầu ra AI có cấu trúc, kiểm nguồn và tự động hóa task phát triển.
- Review PR do agent tạo; ủy quyền task cho background agent.

| Vòng phát triển | Áp dụng vào chức năng | Cách dùng AI và tự kiểm |
| --- | --- | --- |
| Chọn hành vi | Lấy một dòng checklist LR-14 đến LR-18, nối với AC và thiết kế M2. | Claude hỗ trợ phân rã thay đổi; học viên xác nhận dependency và expected result. |
| Triển khai và test | Hoàn thiện UI, API, data và test cho cùng hành vi; kiểm nhánh thành công, lỗi/quyền liên quan. | Review diff nhỏ, kiểm request/response và dữ liệu thay vì chỉ nhìn màn hình. |
| Tích hợp | Chạy lại hành trình M3.1, nối thêm Summary, Quiz và quản lý Output (Note nếu làm Extended). | Dùng AI phân tích lỗi; giữ căn cứ độc lập và regression test. |
| Refactor | Cải thiện một module đã có hành vi được characterization test ghi nhận. | So sánh trước/sau, giữ quy tắc nghiệp vụ và tự động hóa task đã kiểm. |

Dùng Claude triển khai theo từng hành vi và review diff nhỏ. Với refactor, yêu cầu chỉ ra vấn đề có evidence trước khi đề xuất thay cấu trúc; đổi tên hoặc định dạng đơn thuần chưa đủ. Script có thể chạy test, lint và các bước kiểm tra trong terminal hoặc CI, không bắt buộc dùng agent tự động. UI cần trạng thái đang xử lý, rỗng, lỗi và khôi phục; ghi khác biệt hợp lý so với prototype thiết kế.

**Tài liệu dùng cho milestone:** [SRS: yêu cầu chức năng](02_SRS_InsightHub_v1.1.md#sec-3-4); [SRS: dữ liệu và giới hạn](02_SRS_InsightHub_v1.1.md#sec-3-7); [danh mục email](02_SRS_InsightHub_v1.1.md#email-catalog); prototype và API của bài làm tại M2.

### 9.5 Evidence, cách nộp bài và thời hạn

**Hạn chức năng:** trước buổi 8 ít nhất 12 giờ. Gửi link PR nhánh `milestone/m3` và bản ghi nộp bài với mã nguồn, test, migration, kết quả chạy các luồng và kiểm quyền. **Hạn Assignment refactor:** trước buổi 9 ít nhất 12 giờ; bổ sung test ở M4, gửi link PR refactor riêng cùng kết quả trước/sau để giảng viên chấm bài Assignment.

Trong cùng traceability matrix, dẫn tới test hoặc demo của từng nhóm chức năng, kết quả gửi/nhận các email đã tích hợp và migration trên dữ liệu đã có. Tái dùng evidence cho nhiều AC nếu chứng minh được từng điều kiện; không tạo chín bài nộp riêng.

### 9.6 Rubric đánh giá

| Tiêu chí | Điểm tối đa | Cách chấm điểm |
| --- | --- | --- |
| Tài khoản và dữ liệu nghiệp vụ | 25 | Auth và transactional email tầng Core: 10; thao tác Notebook/Document/Conversation tầng Core, quota và pagination theo SRS: 10; persistence và ownership: 5. |
| Tóm tắt và Quiz | 25 | Tóm tắt đúng độ dài, nội dung và nguồn: 10; Quiz đúng cấu trúc và chấm tại server: 10; lịch sử lần làm Quiz và mở lại kết quả đã lưu: 5. |
| Vòng đời và ngoại lệ | 25 | Trạng thái, quota, giới hạn, fallback và usage (IH-AI-005): 10; gửi lặp, đồng thời, xóa tài liệu và phản hồi muộn trên đường chính (hardening đầy đủ chấm ở M4): 10; UI và khôi phục: 5. |
| Refactor và tự động hóa | 15 | Có test trước thay đổi và regression: 5; cải thiện có căn cứ: 5; script hoặc skill thực chạy: 5. |
| Chất lượng bài nộp | 10 | Mã nguồn, test, migration và CI được cập nhật, phần chưa hoàn tất được ghi: 5; review PR do agent tạo có finding và quyết định: 5. |
| **Tổng** | **100** | |

**Rubric Assignment refactor: 100 điểm, chiếm 25% điểm khóa.** Chấm bốn mức cho từng dòng: 0% nếu chưa có minh chứng; 40% nếu mới làm một phần, chưa đạt mô tả cốt lõi; 70% khi đạt mô tả cốt lõi; 100% khi đạt cả cốt lõi và phần đầy đủ. Điểm mỗi dòng bằng điểm tối đa nhân tỷ lệ tương ứng.

| Tiêu chí | Điểm tối đa | Đạt cốt lõi (70%) | Đầy đủ (100%) |
| --- | --- | --- | --- |
| Bảo toàn hành vi | 30 | Có test trước thay đổi, giữ quy tắc nghiệp vụ; hành vi mới có yêu cầu rõ | Tái chạy trước/sau với edge case và giải thích tác dụng phụ |
| Test theo rủi ro | 30 | Chọn unit test, integration test, contract test hoặc E2E test phù hợp module; kỳ vọng độc lập, nhật ký đúng phiên bản | Chứng minh test bắt lỗi; xử lý thiếu sót hoặc test không ổn định và kiểm lại |
| Chất lượng refactor | 20 | Thay đổi có mục tiêu, giảm trùng lặp hoặc phụ thuộc hoặc làm rõ ranh giới; CI đạt | So sánh trước/sau chứng minh cải thiện, giải thích đánh đổi và khôi phục |
| Minh chứng và giải thích | 20 | Kế hoạch, diff, test, review và quyết định với AI liên kết được | Truy từ yêu cầu đến test, phản biện được đề xuất AI không phù hợp |
| **Tổng** | **100** | | |

Dòng tài khoản/dữ liệu đối chiếu riêng checklist Auth, email theo tầng và ba đối tượng Core của LR-15. Dòng AI đối chiếu cả nội dung Summary, quy trình Quiz và vòng đời Output; màn hình có dữ liệu mẫu chưa chứng minh chức năng đạt. Dòng Refactor và tự động hóa chấm tiến độ tại hạn M3 (trước buổi 8): characterization test, kế hoạch và các bước refactor đã có; bài refactor hoàn chỉnh chấm theo rubric Assignment trước buổi 9. Các dòng chức năng chấm theo AC Core (mục 2.1.5); phần Extended đã làm được ghi nhận trong nhận xét, không cộng thêm điểm.

<a id="m4"></a>

## 10. M4 - Kiểm từng chức năng, chất lượng AI và bảo mật InsightHub

### 10.1 Vai trò trong SDLC và kết quả cần đạt

**Trọng tâm:** tổng hợp kiểm chứng chức năng, chất lượng AI, bảo mật và đánh giá điều kiện phát hành.

Có kết luận kiểm chứng trên bản tích hợp M3: từng AC đến hạn M4 có kết quả, lỗi được sửa và retest; chất lượng Chat/Summary/Quiz được đánh giá bằng model thật. Bảng vẫn giữ đủ 153 AC áp dụng, với các AC release/restore đến hạn M5 ghi đúng trạng thái theo mục 10.3. Học viên chứng minh sản phẩm hoạt động, cách ly dữ liệu và xử lý ngoại lệ đúng, cùng các giới hạn còn tồn tại.

### 10.2 Chức năng và công việc cần thực hiện

<a id="lr-20"></a>

1. **Kiểm toàn bộ phạm vi bài tập.** Cập nhật traceability matrix cho từng tiêu chí áp dụng và các điều kiện thành phần; thực hiện 19 hành trình nghiệm thu tầng Core trong phạm vi hai công cụ (UAT-02 đăng nhập Google và UAT-03 khôi phục, đổi mật khẩu thuộc Extended, làm nếu đã làm phần đó). UAT-04 kiểm phần phiên, UAT-12 kiểm xóa tài liệu và đường truy cập cũ, UAT-17 kiểm thời hạn xử lý theo tầng Core. Tái dùng test đã tích lũy ở M3.1-M3 khi còn đúng phiên bản, bổ sung phần còn thiếu và regression bị ảnh hưởng. Có tình huống diễn đạt theo điều kiện ban đầu, hành động và kết quả (Given/When/Then), nối với test thực chạy. Ghi kỳ vọng, thực tế, phiên bản và lỗi; test case chưa chạy, bỏ qua hoặc bị chặn không được tính là đạt. Có ít nhất một E2E test tự động viết bằng `@playwright/test` trong `web/e2e/` (cấu hình `web/playwright.config.ts` của Starter, chạy bằng `npm run test:pw` khi stack fixture đang chạy; App CI đã có bước chạy lệnh này) cho hành trình M3.1, tái dùng kịch bản Gherkin từ M2.1. Spec mẫu `web/e2e/smoke.spec.ts` và script cũ `web/tests/e2e.mjs` (`npm run test:e2e`) viết cho trang công khai của rc.3; sau M3.1 cần đăng nhập trước hoặc thay bằng E2E của bài làm. Được dùng test agents planner và generator; healer không được sửa test đã duyệt (hook `protect-approved-tests`). Chạy `python3 scripts/trace_check.py --gate M4`; AC Core mức R1 cần evidence trực tiếp riêng có `test_ids`, R2 và R3 kết luận qua mapping tới test đã tích lũy, R3 có thể dùng checklist hoặc lấy mẫu (mục 2.1.7). Chẩn đoán một test không ổn định nếu gặp theo mục 16.6; nếu không gặp, ghi cách đã kiểm độ ổn định (ví dụ chạy lặp bộ E2E).

<a id="lr-21"></a>

2. **Kiểm giao diện và hiệu năng.** Dùng Chrome hoặc Edge có ghi phiên bản, tại 1440 × 900 và 390 × 844 pixel CSS. Kiểm các trạng thái, phím theo loại điều khiển, thứ tự focus, dialog và thông báo theo thiết kế; bàn phím bắt buộc trên hành trình M3.1 và màn làm Quiz (mã D6). Đo 10 thao tác không gọi AI (IH-NFR-006) là Extended. Kiểm thời hạn tài liệu 120 giây, hỏi đáp 60 giây và công cụ AI 120 giây, gồm khởi động lại trước hoặc sau thời hạn; ghi cả lỗi và điều kiện môi trường. Hai kích thước này là phạm vi kiểm của bài tập, không chứng minh hỗ trợ mọi thiết bị di động.

<a id="lr-22"></a>

3. **Kiểm phân quyền và vòng đời dữ liệu.** Dùng hai tài khoản, mỗi tài khoản có Notebook với ba tài liệu TXT, Markdown và PDF có văn bản; bộ nguồn có tiếng Việt và tiếng Anh. Với từng loại tài nguyên tầng Core, kiểm đọc và sửa qua API trực tiếp bằng tài khoản B: thay ID, nguồn, cache và hết phiên. Bốn ca hardening AI Job dời từ M3 là bắt buộc, làm theo test-first (viết test thất bại đúng nguyên nhân, sửa, chạy lại): (1) hai yêu cầu Tóm tắt hoặc Quiz đồng thời tranh quota LIM-10; (2) khởi động lại giữa tác vụ, thời hạn không đặt lại; (3) quyền A/B gọi trực tiếp API job và kết quả AI; (4) xóa tài liệu khi tác vụ đang chạy theo ba thứ tự BR-08, gồm phản hồi đến muộn và đường truy cập cũ (mã D9). Dùng mẫu `test_ai_job_*` của Starter làm điểm xuất phát nhưng test phải chạy trên endpoint tích hợp của bài làm. Gửi lặp sau khi thêm nguồn và dữ liệu nghiệp vụ còn sau khi bản ghi chống gửi lặp hết hiệu lực được kết luận qua mapping tới test đã có từ M3. Xóa Notebook, hội thoại, kết quả Quiz và AI job tạo lại kiểm khi đã làm Extended. Nêu kỳ vọng và kết quả cho từng điều kiện, không chỉ ghi “đã kiểm đồng thời”.

<a id="lr-23"></a>

4. **Đánh giá AI bằng mô hình thật.** Thực hiện bộ lượt trong bảng dưới và giữ mọi lượt chạy, kể cả thất bại. Trước khi chạy, xác định 3-5 ý kỳ vọng và đoạn nguồn hỗ trợ cho test case có nội dung. Ghi nhà cung cấp thực tế (kể cả khi có fallback), mô hình sinh nội dung, mô hình embedding, phiên bản prompt và schema, hash nguồn, vị trí tham chiếu, commit, thời gian và mức sử dụng lấy từ bản ghi usage của IH-AI-005. Ngoài các ý kỳ vọng, kiểm từng phát biểu về dữ kiện và từng câu hỏi, lựa chọn, đáp án, giải thích của Quiz; đối chiếu đủ phạm vi nguồn đã chọn. Không dùng JSON hợp lệ hoặc điểm mô hình tự chấm làm evidence duy nhất về nội dung đúng. Các phép đánh giá thủ công này áp dụng cho bộ nghiệm thu, không yêu cầu người duyệt mọi đầu ra trong luồng sử dụng sản phẩm.

   Tổ chức bộ lượt thành **golden set** có version trong [eval harness](../../evaluation/harness/README.md) của Starter (`make eval`), tối thiểu 4 case cho mỗi tính năng Tóm tắt và Quiz: nguồn, câu hỏi hoặc cấu hình, ý kỳ vọng và đoạn nguồn hỗ trợ; học viên viết adapter Summary/Quiz và grader bổ sung. Dùng **grader bằng code** cho phần kiểm được bằng máy: schema, số từ của Summary, số câu và đáp án Quiz thuộc lựa chọn, citation trỏ đúng nguồn đã chọn. Với lượt lặp, báo **pass^k** (k = 2: đạt khi cả hai lần chạy đều đạt) thay vì chỉ lấy lần tốt nhất. LLM-as-judge chỉ hỗ trợ tìm vấn đề: có thể thiên lệch, không ổn định giữa các lần chạy và phải được đối chiếu với người chấm; không dùng làm căn cứ duy nhất. Khi golden set Summary/Quiz đã có, chuyển bước `eval-fixture` trong App CI sang **bắt buộc**: bỏ `continue-on-error`, chạy suite của bài làm với `--min-pass-hat-k`, để job `application` đỏ khi eval không đạt. Quy tắc nhóm: không merge PR khi CI đỏ. Nếu repository hỗ trợ branch protection hoặc ruleset (repository công khai hoặc gói trả phí), đặt `application` làm required status check; nếu không, ghi quy tắc trong PR template và evidence lần chạy đỏ, xanh.

<a id="lr-24"></a>

5. **Kiểm bảo mật và sửa lỗi.** Cập nhật threat model từ M2 theo bản đã triển khai, chạy secret scan và dependency scan cho cả Web và API (dùng lại cấu hình CI của M1), tạo danh mục thành phần phần mềm (SBOM) bằng script có sẵn của Starter và AI-BOM (provider chính và dự phòng, model sinh nội dung và embedding, phiên bản prompt và schema, corpus đánh giá) bằng `make ai-bom`, bổ sung phần script không tự biết. Chạy `/security-review` trên diff của bài làm và dùng lại subagent `design-reviewer` cho threat model đã cập nhật. Kiểm xác thực, liên kết danh tính, phiên, quyền trên mọi tài nguyên, nội dung Markdown hoặc mã gây XSS, instruction độc hại trong tài liệu, file tải lên, nhật ký và quyền công cụ hoặc MCP. Xác minh mỗi phát hiện trước khi kết luận; ghi tác động, xử lý và kiểm lại. Với ít nhất một phát hiện, để AI đề xuất bản vá, học viên review diff, chạy retest và phê duyệt hoặc bác bỏ có căn cứ. Phân biệt lỗi sản phẩm, dữ liệu, thời điểm và lỗi test; tăng số lần thử lại hoặc bỏ test không thay việc tìm nguyên nhân. Nếu dùng lỗi cài có chủ đích phải ghi rõ.

**Bộ đánh giá AI phải thực hiện:**

| Nhóm | Số lượt/tình huống | Nội dung |
| --- | --- | --- |
| Hỏi đáp | 6 lượt | Ba câu có căn cứ, gồm tiếng Anh và tổng hợp nhiều tài liệu; hai câu thiếu căn cứ; một nguồn có instruction gây nhiễu nhưng câu hỏi vẫn trả lời được |
| Tóm tắt | 2 lượt | Một nguồn với bản ngắn; nhiều nguồn với bản chi tiết có thông tin mâu thuẫn |
| Quiz | 2 lượt | Một nguồn với 5 câu; nhiều nguồn với 10 câu; kiểm câu hỏi, lựa chọn, đáp án, giải thích và nguồn |
| Lặp lại | 2 lượt | Chọn trước một câu hỏi đáp có căn cứ và một test case Tóm tắt hoặc Quiz; đánh giá cả hai lần |
| **Tổng nội dung** | **12 lượt** | Dùng mô hình thật; không tính embedding, lượt bổ sung PDF hoặc chạy lại sau sửa vào số này |
| Ngoại lệ, ngoài 12 lượt | Ba nhóm cho cả hai công cụ, cộng một ca fallback | Thiếu căn cứ, vượt giới hạn đầu vào, đầu ra sai schema; kiểm thêm lỗi dịch vụ bên ngoài, thời gian chờ và fallback sang provider dự phòng bằng giả lập lỗi provider có kiểm soát |
| Cách ly, ngoài 12 lượt | Bốn tình huống đại diện | Dữ liệu người khác; nguồn sai Notebook; xóa nguồn khi xử lý; đọc qua API, liên kết và cache sau mất quyền. Không thay bộ kiểm quyền từng tài nguyên |

Một lượt có nội dung đạt khi đủ ý kỳ vọng, các dữ kiện đều có căn cứ, tham chiếu hợp lệ và đáp ứng cấu trúc, giới hạn, trạng thái, thời hạn. Ý kỳ vọng không thay việc kiểm các phát biểu khác do mô hình tạo ra. Quiz phải có đúng một đáp án đúng, không mơ hồ. Hai câu thiếu căn cứ phải trả `NoEvidence`; test case có căn cứ không được trả `NoEvidence` hoặc `Failed`. Nếu căn cứ kỳ vọng sai, ghi lý do sửa và phiên bản mới trước khi chạy lại. Không còn lỗi chặn phát hành theo SRS mới kết luận sẵn sàng bàn giao.

### 10.3 Điều kiện hoàn thành

- Traceability matrix giữ đủ 153 AC áp dụng và 12 AC ngoài phạm vi. Tổng hợp kết quả đã kiểm và phần còn thiếu cho từng nhánh, liên kết 19 UAT tầng Core trong phạm vi hai tool. Các AC của IH-NFR-009, IH-NFR-010 và IH-REL-001..003 được gán M5: tại M4 ghi “chưa kiểm, chưa đến hạn M5” nếu chưa có evidence; không coi đây là phần đã Pass hoặc tự kéo toàn bộ M5 về M4. Output M4 được kiểm theo LR-20..24; các lỗi của phạm vi đến hạn vẫn phải được ghi và xử lý. Chưa chạy/bị chặn không được tính đạt.
- Có test UI, API, data, quyền A/B, lifecycle, giới hạn và số đo theo LR-20 đến LR-22; lỗi đã sửa có regression test/retest; có ít nhất một E2E cho hành trình M3.1.
- Đủ 12 lượt nội dung AI và các ngoại lệ theo LR-23 (gồm ca fallback), lưu cả lượt lỗi; có golden set, grader bằng code và pass^k cho lượt lặp; từng claim và câu hỏi Quiz được đối chiếu nguồn; bước `eval-fixture` đã bắt buộc (CI đỏ khi không đạt).
- Kết quả kiểm bảo mật, threat model cập nhật, SBOM, AI-BOM và Assignment refactor được cập nhật. Chỉ kết luận sẵn sàng phát hành khi đáp ứng điều kiện SRS; điểm học tập không thay kết quả sản phẩm.

### 10.4 Áp dụng SDLC và AI

**Kiến thức áp dụng:**

- Test đa tầng, nghiệm thu theo hành trình người dùng, regression và đo yêu cầu phi chức năng.
- Eval-driven development: golden set, grader bằng code, pass^k và giới hạn của LLM-as-judge; kỳ vọng xác lập trước từ nguồn.
- Threat model, kiểm quyền, secret, dependency, SBOM/AI-BOM và an toàn công cụ AI.

| Nhóm chức năng | Trọng tâm kiểm ở M4 |
| --- | --- |
| Auth và Email | Đăng ký, xác minh, session, đăng xuất và EML-001; recovery, tái xác thực, linking và rate limit nếu đã làm Extended. |
| Notebook và Document | Thao tác, upload/duplicate/retry, ownership, quota, trạng thái, xóa tài liệu và deadline. |
| Conversation (Note nếu làm) | Persistence, nguồn/citation; xóa conversation, version conflict và bản sao độc lập nếu đã làm Extended. |
| Summary và Quiz | Schema, nội dung/nguồn, độ dài/số câu, không lộ đáp án, chấm và nộp lặp/làm lại. |
| AI Job và Output | Quota LIM-10 của Tóm tắt và Quiz (mã D8), idempotency, restart, ba thứ tự BR-08 khi xóa tài liệu, phản hồi muộn, fallback và usage; xóa và regenerate nếu đã làm Extended. |

Tái dùng test đã tích lũy khi còn phù hợp bản nộp, bổ sung khoảng trống theo rủi ro. Dùng Claude đề xuất edge case và phân tích nguyên nhân; học viên xác nhận lỗi, sửa và chạy lại, giữ expected result có căn cứ độc lập.

Dùng Claude tìm edge case và phân tích nguyên nhân lỗi; tự xác lập kỳ vọng trước. Không sửa kỳ vọng hoặc bỏ điều kiện kiểm chỉ để test báo đạt. Có thể dùng mô phỏng thời gian và lỗi nhà cung cấp để kiểm hết thời gian chờ và phiên; chất lượng nội dung phải chạy mô hình thật. Tái dùng dữ liệu và minh chứng giữa các phép kiểm khi phù hợp.

**Tài liệu dùng cho milestone:** [SRS: yêu cầu phi chức năng](02_SRS_InsightHub_v1.1.md#sec-3-10); [SRS: đánh giá AI](02_SRS_InsightHub_v1.1.md#sec-4-2); [SRS: nghiệm thu](02_SRS_InsightHub_v1.1.md#sec-4-3); [công cụ đánh giá nền](../../evaluation/README.md).

### 10.5 Evidence, cách nộp bài và thời hạn

**Hạn hoàn thiện:** trước buổi 9 ít nhất 12 giờ. Gửi link PR nhánh `milestone/m4` và bản ghi nộp bài, gồm bảng kết quả từng yêu cầu, test và nghiệm thu, số đo, nguồn và kết quả đánh giá AI, báo cáo bảo mật, threat model cập nhật, SBOM và AI-BOM, lỗi đã sửa. Đồng thời gửi bản hoàn thiện Assignment refactor của M3.

Mỗi kết luận cần chỉ ra chức năng, AC/nhánh, input, expected/actual, môi trường và commit. Dẫn lại cùng test/log nếu dùng cho UAT, bảo mật hoặc regression; không nhập lại kết quả vào nhiều bảng.

### 10.6 Rubric đánh giá

| Tiêu chí | Điểm tối đa | Cách chấm điểm |
| --- | --- | --- |
| Bao phủ nghiệp vụ và nghiệm thu | 25 | AC Core mức R1 có evidence trực tiếp riêng: 10; AC R2/R3 có evidence và mapping, UAT đủ phạm vi: 10; lỗi được sửa và kiểm lại: 5. |
| Giao diện và thời hạn | 15 | Hai kích thước và trạng thái UI: 5; bàn phím và focus trên hành trình M3.1 và màn làm Quiz: 5; kiểm thời hạn của tài liệu, hỏi đáp và công cụ AI: 5. |
| Chất lượng AI | 25 | Đủ 12 lượt nội dung chạy qua eval harness (golden set, grader bằng code) và lưu cả lỗi: 10; đối chiếu ý nghĩa, nguồn và câu hỏi Quiz: 10; kiểm ngoại lệ (gồm ca fallback) và pass^k của lượt lặp: 5. |
| Quyền và bảo mật | 25 | Kiểm hai tài khoản A và B trên từng tài nguyên và vòng đời: 10; threat model cập nhật, kết quả scan, SBOM và AI-BOM: 5; sửa và kiểm lại, gồm bản vá AI được người duyệt: 5; quyền công cụ AI và `/security-review` có finding đã xác minh: 5. |
| Hồ sơ có thể tái kiểm | 10 | Môi trường, phiên bản, lệnh và kết quả rõ: 5; defect có căn cứ và cập nhật bài refactor: 5. |
| **Tổng** | **100** | |

Độ bao phủ được kiểm theo chức năng và từng điều kiện AC; tỷ lệ test Pass cao không thay các nhánh còn thiếu. Rubric AI dùng cả ý nghĩa nội dung và nguồn, không chỉ kiểm JSON/schema.

<a id="m5"></a>

## 11. M5 - Phát hành R1, kiểm restore và thực hiện thay đổi R1.1

### 11.1 Vai trò trong SDLC và kết quả cần đạt

**Trọng tâm:** phát hành, kiểm vận hành/khôi phục và xử lý thay đổi sau R1.

Có bản R1 của bài tập cài được trên môi trường sạch, dữ liệu và quyền được kiểm sau migration/restore, sau đó có một thay đổi thành R1.1 cùng regression test. Đầu vào là bản đã kiểm tại M4; chỉ gọi sẵn sàng bàn giao khi đáp ứng điều kiện phát hành của SRS.

### 11.2 Chức năng và công việc cần thực hiện

<a id="lr-25"></a>

1. **Phát hành bản R1 của bài tập.** Gắn phiên bản và Git tag cho sản phẩm trong phạm vi 153 tiêu chí áp dụng, Tóm tắt và Quiz. Đóng gói kèm checksum, cấu hình mẫu và hướng dẫn cài, chạy, xử lý lỗi; kiểm cài đặt trên môi trường sạch và các luồng chính. Dùng [checklist release mẫu](../release/Release_Checklist_Template.md) của Starter, có dòng "eval fixture đạt trên đúng commit phát hành". Ghi giới hạn, lỗi còn mở và kết quả đúng bản phát hành. Ghi chú phát hành theo [template](../release/Release_Notes_Template.md) có mục tính năng AI: gắn nhãn nội dung do AI tạo cho Chat, Summary và Quiz, nêu giới hạn đã biết, yêu cầu người dùng kiểm lại và kênh báo sự cố. Khi chỉ dùng nội bộ, InsightHub được miễn nghĩa vụ gắn nhãn theo Luật Trí tuệ nhân tạo 134/2025/QH15 và Nghị định 142/2026/NĐ-CP của Việt Nam; vẫn gắn nhãn như best practice để sẵn sàng khi mở rộng. Đây là nội dung đào tạo, không phải tư vấn pháp lý. Hồ sơ không được kết luận đã hoàn thành toàn bộ năm công cụ của SRS. Không bàn giao secret hoặc dữ liệu riêng.

<a id="lr-26"></a>

2. **Kiểm nâng cấp và khôi phục dữ liệu.** Chạy migration trên dữ liệu đã có; sao lưu và khôi phục sang môi trường cách ly. Kiểm số lượng, quan hệ, nội dung, phiên bản cấu trúc và quyền của tài khoản, Notebook, tài liệu, hội thoại, kết quả AI, các lần làm Quiz và ghi chú (nếu đã làm Extended). Phạm vi backup gồm các bảng Auth của scaffold (`auth_user`, `auth_session`, `auth_account`, `auth_verification`) và `ai_jobs`. Nếu xác thực được lưu ở dịch vụ bên ngoài, ghi dữ liệu nào nằm ngoài bản sao lưu ứng dụng, điều kiện khôi phục hoặc tái liên kết và phép kiểm đăng nhập, quyền sau khôi phục. Không tuyên bố khôi phục đầy đủ chỉ từ việc phục hồi cơ sở dữ liệu. Khi thêm bảng mới, mở rộng drill bằng `scripts/backup_restore_check.py --extra-tables` theo [Runbook](../Runbook_Starter_v1.md) để kiểm cả dữ liệu bài làm, gồm `auth_user,auth_session,auth_account,auth_verification,ai_jobs`. Sau M3.1, phần kiểm đọc qua API của drill cần phiên đăng nhập: cập nhật probe theo endpoint đã bảo vệ (ví dụ dùng `dependency_overrides[current_user]` trong `TestClient`) và ghi cách kiểm vào evidence. Không xóa volume để thay cho nâng cấp và không tự gán dữ liệu chưa có chủ sở hữu cho tài khoản đầu tiên.

<a id="lr-27"></a>

3. **Thực hiện một thay đổi sau R1.** Sau khi đã ghi nhận bản R1 và kết quả kiểm của nó, dùng yêu cầu thay đổi nhỏ do giảng viên công bố hoặc một lỗi có thể tái hiện. Với defect, tái hiện và chẩn đoán từ log ứng dụng (request, trạng thái operation, lỗi provider) trước khi sửa; lưu đoạn log đã lọc secret làm căn cứ. Ghi hành vi trước và sau, tác động tới yêu cầu, giao diện, API, dữ liệu, test và rủi ro. Triển khai thành R1.1, kiểm regression, cập nhật cùng traceability matrix, hướng dẫn và ghi chú phát hành. So sánh số đo usage (token, latency, chi phí ước tính) trước và sau CR; nếu CR chạm prompt, model hoặc provider thì chạy lại golden set và ghi kết quả. Nêu cách quay lại ứng dụng cùng điều kiện bảo toàn dữ liệu; không sửa tag R1 để thay lịch sử. Migration, workflow CI hoặc cấu hình build/test do agent sinh trong M5 được review theo [checklist](../ai/templates/Review_Checklist_Migration_CI.md) trước khi merge.

### 11.3 Điều kiện hoàn thành

- R1 có tag, checksum, hướng dẫn, cấu hình mẫu an toàn và kết quả cài sạch trên đúng phiên bản; eval fixture đạt trên đúng commit; ghi chú phát hành có nhãn và giới hạn của tính năng AI.
- Kiểm Auth, Notebook, Document/Chat, Summary, Quiz và Output (Note nếu đã làm Extended) sau cài mới; restore kiểm nội dung, quan hệ và quyền trên dữ liệu đã có.
- Phạm vi backup bao gồm dữ liệu bài làm; nếu dùng Auth provider bên ngoài, mô tả và kiểm phần phục hồi/tái liên kết tương ứng.
- R1 tồn tại và được kiểm trước CR; R1.1 có thay đổi, phân tích tác động, số đo usage trước và sau, regression test và cách rollback bảo toàn dữ liệu, không sửa tag R1.

### 11.4 Áp dụng SDLC và AI

**Kiến thức áp dụng:**

- Đóng gói phiên bản, cài sạch, migration, sao lưu và khôi phục.
- Hướng dẫn vận hành, ghi chú phát hành và nhãn tính năng AI.
- Debug từ log, phân tích tác động của yêu cầu thay đổi, kiểm regression và phương án rollback.

1. Chốt candidate từ kết quả M4, kiểm điều kiện phát hành rồi đóng gói R1 với thông tin tái lập.
2. Cài mới theo runbook; chạy hành trình đăng nhập → Notebook → Document/Chat → Summary/Quiz (Note nếu đã làm Extended) và kiểm quyền.
3. Migration/restore trên môi trường cách ly; so sánh dữ liệu, quan hệ, version và ownership, mở lại conversation/output/QuizAttempt đã lưu.
4. Chọn CR sau R1 trên một chức năng đã có. Dùng Claude phân tích tác động; học viên xác nhận hành vi trước/sau, triển khai, kiểm regression và phát hành R1.1.

Cho Claude rà soát runbook như người mới nhận dự án và phân tích tác động của thay đổi. Tự chạy toàn bộ bước cài đặt và khôi phục; AI không được suy đoán kết quả. Với thao tác dữ liệu, xác định môi trường và bản sao lưu trước khi thực hiện.

**Tài liệu dùng cho milestone:** [Runbook starter](../Runbook_Starter_v1.md); [SRS: điều kiện phát hành](02_SRS_InsightHub_v1.1.md#sec-4-4); [hướng dẫn tích hợp và dữ liệu cũ](#data-api).

### 11.5 Evidence, cách nộp bài và thời hạn

**Hạn hoàn thiện:** trước buổi 10 ít nhất 12 giờ. Gửi link PR nhánh `milestone/m5`, bản ghi nộp bài, link hai tag R1/R1.1 và gói phát hành có checksum. Giữ nguyên tag đã gửi; lần sửa tiếp theo tạo phiên bản mới. Đính kèm kết quả cài đặt mới, nâng cấp và khôi phục và hồ sơ thay đổi. Hồ sơ Capstone dùng lại hồ sơ M5 và có hạn riêng tại mục 12.5.

Hồ sơ release nối tag/checksum với kết quả cài, migration, restore và test chức năng. Hồ sơ CR dùng cùng yêu cầu, thiết kế và traceability matrix đang quản lý; không tạo sản phẩm thứ hai hoặc thêm hạ tầng cloud bắt buộc.

### 11.6 Rubric đánh giá

| Tiêu chí | Điểm tối đa | Cách chấm điểm |
| --- | --- | --- |
| Bản phát hành tái cài được | 30 | Phiên bản, tag và checksum: 10; cài sạch và kiểm luồng chính: 10; hướng dẫn và cấu hình mẫu đầy đủ: 10. |
| Nâng cấp và khôi phục | 30 | Migration trên dữ liệu đã có: 10; restore cách ly thành công: 10; nội dung và quyền sau restore đúng: 10. |
| Thay đổi sau phát hành | 25 | Phân tích tác động: 5; hành vi mới đúng: 10; regression và phương án quay lại: 10. |
| Bàn giao và giải thích | 15 | Ghi chú R1/R1.1 rõ, có nhãn tính năng AI: 5; kết quả thực chạy có phiên bản: 5; review migration hoặc cấu hình CI do agent sinh theo checklist, có finding và quyết định: 5. |
| **Tổng** | **100** | |

Rubric release/restore dựa trên hành trình và dữ liệu thật của bài làm. Khởi động container hoặc restore một DB rỗng chưa chứng minh Auth, ownership và dữ liệu nghiệp vụ được khôi phục.

<a id="capstone"></a>

## 12. Capstone - Demo InsightHub và bảo vệ quyết định xuyên SDLC

### 12.1 Vai trò trong SDLC và kết quả cần đạt

**Trọng tâm:** nghiệm thu, bàn giao và giải thích quyết định xuyên vòng đời sản phẩm.

Học viên tự demo bản phát hành đã nộp và giải thích được cách chuyển một yêu cầu thành thiết kế, code, test, release và thay đổi. Kết quả sử dụng AI được chứng minh bằng sản phẩm và quyết định cá nhân; kế hoạch 30 ngày chuyển bài học sang công việc thực tế.

### 12.2 Chức năng và công việc cần thực hiện

<a id="lr-28"></a>

1. **Demo và bảo vệ cá nhân.** Chạy bản đã nộp: đăng nhập, Notebook, Document, Chat có citation, Summary, Quiz và một tình huống lỗi/quyền (Note và phần Extended nếu đã làm). Mở lại conversation/output/QuizAttempt đã lưu, chỉ ra evidence cho các Auth flow và transactional email tầng Core (Extended nếu đã làm). Giải thích một yêu cầu xuyên qua thiết kế, mã nguồn và test, refactor đã làm, kết quả đánh giá AI và cách khôi phục dữ liệu. Thực hiện hoặc phân tích chính xác thay đổi nhỏ giảng viên đưa; chỉ rõ phần AI hỗ trợ và quyết định của bản thân. Trình bày AI Engineering Kit của dự án: quy tắc, quyền, cấu hình MCP, hook, skill, subagent, quy trình review, spec, eval và số đo đã dùng thật.

<a id="lr-29"></a>

2. **Lập kế hoạch áp dụng AI trong 30 ngày.** Chọn một quy trình công việc thực tế; ghi baseline hiện trạng, mục tiêu, các mốc ngày 7/14/30 và rủi ro. Dùng `make delivery-report` trên AI Delivery Log của dự án làm baseline tham chiếu và bài học về cách đo. KPI dùng năm DORA metrics (change lead time, deployment frequency, change fail rate, failed deployment recovery time, deployment rework rate) cùng review load và cost per accepted change; không dùng số dòng code (LOC) hoặc số token làm KPI chính. Số liệu của `make delivery-report` là proxy đo theo PR trong dự án cá nhân (ví dụ CI lần đầu fail, PR rework rate), không phải DORA metrics đo theo lần triển khai production; ghi nhãn proxy khi trình bày. Nêu cách thu dữ liệu, điều kiện tiếp tục hoặc dừng; có thể nêu hướng mở rộng 60/90 ngày. Có mục **Công cụ và dữ liệu được phép**: chỉ dùng công cụ AI được Samsung SDS phê duyệt và loại dữ liệu được phép theo phân loại trong AI Usage Charter. Đây là bản kế hoạch cần nộp, không yêu cầu làm thêm 30 ngày để hoàn thành khóa.

### 12.3 Điều kiện hoàn thành

- Demo hành trình có Auth, Notebook, Document/Chat, Summary và Quiz; mở kết quả đã lưu và kiểm một tình huống lỗi/quyền.
- Chỉ ra evidence của các email và nhánh Auth tầng Core, vòng đời Output tầng Core, lifecycle và bảo mật; không cần chạy lại mọi test trong thời gian bảo vệ.
- Truy được yêu cầu đến thiết kế/code/test/tag; giải thích refactor, đánh giá AI, restore và CR R1.1, cùng giới hạn đã ghi.
- Kết luận nghiệm thu ghi đúng phạm vi D4 (mục 15.1): đạt hay chưa đạt các AC áp dụng của bài tập hai công cụ, AC Extended đã làm hoặc `Extended-NotDone`; không kết luận đạt nghiệm thu toàn bộ sản phẩm năm công cụ của SRS.
- Tự xử lý hoặc phân tích chính xác thay đổi nhỏ được giao; có kế hoạch áp dụng AI 30 ngày với baseline, KPI, điều kiện kiểm và công cụ, dữ liệu được phép.

### 12.4 Áp dụng SDLC và AI

**Kiến thức áp dụng:**

- Demo theo hành trình người dùng và giải thích quyết định kỹ thuật.
- Truy từ yêu cầu đến thiết kế, mã nguồn, test và phiên bản phát hành.
- Đánh giá hiệu quả ứng dụng AI bằng baseline, DORA metrics (gồm deployment rework rate), review load và chi phí, phân biệt chỉ số chuẩn với proxy của dự án.

| Phần bảo vệ | Kết quả ứng dụng vào Running Project |
| --- | --- |
| Demo sản phẩm | Chứng minh các chức năng nối thành hành trình người dùng, giữ quyền và dữ liệu. |
| Giải thích một yêu cầu | Mở AC → prototype/API/schema → code → test → bản phát hành; giải thích quyết định và trade-off. |
| Phản biện việc dùng AI | Chỉ ra đề xuất đã giữ/sửa/bác bỏ, căn cứ kiểm độc lập và ảnh hưởng tới sản phẩm. |
| Xử lý thay đổi | Phân tích tác động của yêu cầu mới trên chức năng đã có, chọn test và cách bảo toàn dữ liệu. |

Dùng Claude đóng vai reviewer để luyện phản biện và tìm điểm chưa có minh chứng. Học viên tự demo, giải thích và quyết định; không đọc lại câu trả lời AI để thay vấn đáp. Chuẩn bị dữ liệu mẫu và đường dẫn mở nhanh trong repository.

**Tài liệu dùng cho milestone:** [SRS: tiêu chí nghiệm thu](02_SRS_InsightHub_v1.1.md#sec-4-3); [SRS: bàn giao](02_SRS_InsightHub_v1.1.md#sec-4-4); prototype, API, hướng dẫn vận hành và hồ sơ đã xây dựng trong dự án.

### 12.5 Evidence, cách nộp bài và thời hạn

**Hạn hồ sơ:** trước buổi 10 ít nhất 2 giờ, sau hạn M5. Gửi link PR `milestone/capstone`, bản ghi nộp bài, tag phát hành đã kiểm, link prototype (Figma hoặc HTML), hướng dẫn demo, bảng kết quả yêu cầu, test, AI và bảo mật và kế hoạch 30 ngày. **Hạn sửa sau bảo vệ:** trong 24 giờ sau khi buổi 10 kết thúc; chỉ sửa các mục giảng viên đánh dấu bắt buộc, gửi link cập nhật và danh sách phản hồi đã xử lý. Nếu sửa code, kiểm lại và tạo tag phát hành mới, giữ bản đã bảo vệ.

Chuẩn bị đường dẫn mở nhanh đến evidence đã tích lũy ở M4, M5 và dữ liệu demo, không biên soạn lại toàn bộ hồ sơ. Demo dùng đúng tag được nộp; phần sửa sau bảo vệ có phiên bản và kết quả kiểm mới theo hạn quy định.

### 12.6 Rubric đánh giá

**Rubric Capstone: 100 điểm, chiếm 35% điểm khóa.** Mỗi tiêu chí nhận 0% khi không có minh chứng hoặc vi phạm nghiêm trọng hành vi cần đánh giá; 40% khi mới làm một phần, chưa đạt mô tả cốt lõi; 70% khi đạt đầy đủ cột cốt lõi; 100% khi đạt thêm cột đầy đủ. Điểm bằng điểm tối đa nhân tỷ lệ, cộng các dòng rồi chia 10 để có điểm Capstone trên thang 10. Ví dụ: tiêu chí tối đa 10 điểm đạt cốt lõi nhận 7 điểm.

| Tiêu chí | Điểm tối đa | Đạt cốt lõi (70%) | Đầy đủ (100%) |
| --- | --- | --- | --- |
| Phạm vi và kế hoạch | 5 | Mục tiêu, phạm vi và backlog nhất quán với phần cần bổ sung vào starter; PR đã tự review, CI đúng phiên bản; trách nhiệm với AI rõ | Ưu tiên và phụ thuộc hợp lý; kế hoạch cập nhật theo kết quả thực tế; giải thích được cách xử lý phát hiện review |
| Spec và truy vết yêu cầu | 10 | AC có luồng chính và ngoại lệ; yêu cầu phi chức năng có cách đo; công việc, ước lượng và test case liên kết được; thử tích hợp ghi rõ phần đã/chưa kiểm | Truy từ yêu cầu đến test và từ test về yêu cầu; xử lý giả định quan trọng; cập nhật traceability matrix sau thay đổi |
| Thiết kế giao diện, API và dữ liệu | 10 | Prototype, API, từ điển dữ liệu, phiên bản cấu trúc và quyền sở hữu nhất quán; quyết định kiến trúc có phương án và căn cứ; có thiết kế migration và trạng thái lỗi | Triển khai khớp thiết kế hoặc giải thích khác biệt; kiểm hai kích thước/bàn phím; liên kết quyết định thiết kế với yêu cầu và test |
| Chức năng và TDD | 12 | Auth và transactional email tầng Core, Notebook, Document/Chat, Summary, Quiz và AI Output tầng Core hoạt động qua các lớp tích hợp tương ứng; tiêu chí bắt buộc đạt; có test thất bại trước sửa rồi đạt sau sửa; xử lý trạng thái và lỗi | Tái chạy được bản nộp; mọi AC Core có minh chứng; giải thích ranh giới mô phỏng; dữ liệu còn sau khởi động lại, thao tác lặp đúng |
| Refactor và tự động hóa | 8 | Có test ghi nhận hành vi module trước thay đổi; diff đúng phạm vi, regression giữ quy tắc nghiệp vụ; task tự động thực chạy và giới hạn rõ; AI Engineering Kit (hook, skill, subagent, bảo vệ test) được dùng thật | So sánh trước/sau chứng minh cải thiện; chạy lại từ checkpoint hoặc khôi phục; mọi thay đổi hành vi có căn cứ yêu cầu |
| Test và nghiệm thu | 8 | Chọn tầng test theo yêu cầu/rủi ro; nghiệm thu có kỳ vọng và thực tế; lỗi quan trọng được kiểm lại; điều kiện đo rõ | Người khác chạy lại được; phân tích thiếu sót và test không ổn định; chứng minh test bắt lỗi và truy vết đầy đủ trên bản nộp |
| Chất lượng nội dung AI | 7 | Đủ 12 lượt nội dung cho hỏi đáp/Tóm tắt và Quiz; đối chiếu ý và nguồn; ghi mô hình, dữ liệu, phiên bản và cả lượt lỗi; thiếu căn cứ/instruction gây nhiễu/ngoại lệ được xử lý đúng | Tái lập cấu hình và nguồn; đánh giá cả lượt lặp; giải thích sai lệch, kết luận và kiểm lại; không dùng AI tự chấm làm căn cứ duy nhất |
| Bảo mật ứng dụng | 10 | Có threat model, quét và danh mục thành phần; kiểm hai tài khoản trên từng tài nguyên; kiểm phiên và nội dung độc hại, sửa và kiểm lại; không còn lỗi chặn phát hành | Tái hiện test case bị từ chối qua API, nguồn và cache, sau xóa và hết phiên; đánh giá tác động có căn cứ và chứng minh lỗi không tái phát |
| An toàn quy trình AI | 5 | Giới hạn quyền công cụ hoặc MCP, dữ liệu và secret; thử một tình huống bị chặn; có người kiểm và log đã lọc | Tái hiện dừng và khôi phục từ checkpoint; giải thích cách xử lý instruction độc hại và chỉ cấp quyền cần cho task |
| Phát hành và khôi phục | 5 | Có version/tag/checksum; cài sạch, kiểm luồng chính, nâng cấp và restore cách ly dữ liệu đầy đủ; hướng dẫn sử dụng/xử lý lỗi rõ | Người khác tái cài được theo hướng dẫn; kiểm nội dung và quyền sau restore; giải thích giới hạn và cách quay lại bản trước |
| Thay đổi sau phát hành | 5 | Có thay đổi sau R1, phân tích tác động đến yêu cầu, thiết kế, dữ liệu và test; bản cập nhật, ghi chú phát hành và regression đúng phạm vi | Tái hiện trước/sau; giải thích rủi ro và cách quay lại; cập nhật truy vết, không gây regression hoặc mất dữ liệu |
| Demo và vấn đáp | 10 | Tự demo chức năng và ngoại lệ; truy một yêu cầu qua mã nguồn và test; giải thích quyết định/refactor; thực hiện hoặc phân tích đúng một thay đổi nhỏ | Xử lý được tình huống biến đổi giảng viên đưa; chẩn đoán từ minh chứng, bảo vệ lựa chọn và chỉ rõ giới hạn |
| Kế hoạch áp dụng 30 ngày | 5 | Chọn một quy trình công việc, có baseline và KPI (không lấy LOC/token làm KPI chính) đối chiếu số đo thật từ AI Delivery Log, trách nhiệm cá nhân, mốc ngày 7/14/30, rủi ro và công cụ, dữ liệu được phép | Kế hoạch khả thi; cách thu dữ liệu và điều kiện tiếp tục/dừng rõ, dựa trên bài học trong dự án |
| **Tổng** | **100** | | |

Các nhóm tiêu chí giữ cơ cấu điểm của chương trình: yêu cầu/kế hoạch 15; thiết kế 10; triển khai và tự động hóa 20; test/chất lượng AI 15; bảo mật 15; phát hành/bảo trì 10; vấn đáp/kế hoạch áp dụng 15. Không lấy điểm Assignment thay cho đánh giá refactor trong bản sản phẩm cuối. Lỗi lộ dữ liệu chéo, chiếm quyền hoặc mất dữ liệu nghiêm trọng chưa sửa khiến tiêu chí bảo mật tương ứng nhận 0 và sản phẩm chưa đủ điều kiện bàn giao.

Giữ cơ cấu đánh giá theo giai đoạn SDLC. Mỗi tiêu chí phải được giải thích bằng chức năng hoặc quyết định thực tế của InsightHub; hình thức trình bày không thay kết quả chạy và khả năng bảo vệ cá nhân.

<a id="data-api"></a>

## 13. Thiết kế dữ liệu, schema, API và tích hợp

Phần này hướng dẫn chuyển yêu cầu của [SRS](02_SRS_InsightHub_v1.1.md) thành thiết kế và kiểm chứng cho bài tập Tóm tắt và Quiz. Các đầu ra được lưu trong hồ sơ LR-11 và sử dụng tiếp khi phát triển; không tạo thêm Assignment hoặc bài nộp riêng.

### 13.1. Phân biệt yêu cầu, thiết kế và phần nền

| Lớp thông tin | Nội dung đã được xác định | Phần học viên cần quyết định |
| --- | --- | --- |
| SRS | Hành vi, dữ liệu logic, quan hệ, quyền, trạng thái, giới hạn và điều kiện chấp nhận. | Giải pháp thực hiện phải giữ các ràng buộc này; không tự đổi nghiệp vụ theo mặc định thư viện. |
| Hợp đồng tham khảo | Một phương án OpenAPI, JSON Schema, dữ liệu mẫu và tình huống kiểm ngoài schema. | Chọn phần phù hợp, điều chỉnh cho phạm vi bài tập và giải thích thay đổi thiết kế. |
| API Starter | Giao tiếp và dữ liệu của phần nền được cung cấp. | Xác định nơi cần mở rộng, chuyển đổi hoặc bọc tích hợp; kiểm regression phần bị ảnh hưởng. |
| Thiết kế bài làm | API, cấu trúc lưu trữ, giao dịch, bảo mật và migration của giải pháp cá nhân. | Học viên chịu trách nhiệm hoàn thiện, thực thi và kiểm chứng. |

Không bắt buộc một bảng cơ sở dữ liệu cho mỗi đối tượng logic. Một đối tượng có thể được lưu trong nhiều bảng, một trường có thể suy ra, hoặc dữ liệu xác thực có thể do dịch vụ quản lý. Thiết kế phải giải thích nơi thực thi từng quy tắc và chứng minh hành vi còn đúng sau khởi động lại.

### 13.2. Đầu ra thiết kế tại LR-11

#### 13.2.1. Mô hình và từ điển dữ liệu

Đọc SRS mục 3.7, đặc biệt 3.7.3 và 3.7.7-3.7.9. Xác định các đối tượng thuộc bài tập: người dùng, danh tính, phiên, Notebook, tài liệu, lần xử lý tài liệu, hội thoại, lượt hỏi đáp, ghi chú, AI job tạo nội dung, kết quả AI, lần làm Quiz, tham chiếu nguồn, bản ghi thao tác và dữ liệu vận hành cần thiết.

Với mỗi đối tượng, ghi các trường cần lưu hoặc suy ra; kiểu dữ liệu; điều kiện bắt buộc; mặc định; giới hạn; nguồn tạo; quyền đọc, sửa; trạng thái và chính sách xóa. Sơ đồ quan hệ phải thể hiện số lượng liên kết và chủ sở hữu. Mô tả các điều kiện phải luôn đúng, chẳng hạn một lần làm Quiz chỉ thuộc một đề, chủ sở hữu tài nguyên con phải phù hợp với Notebook và một AI job thành công chỉ tạo một kết quả.

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

Mô tả cách tiếp nhận nhất quán giữa bản ghi thao tác, dữ liệu nghiệp vụ, bộ đếm và job đang chạy. Giải thích cách ngăn hai yêu cầu cùng vượt quota, cùng nộp một lần Quiz hoặc cùng công bố kết quả trùng.

Thiết kế cần xử lý ba thứ tự BR-08: xóa hoàn tất trước công bố; công bố hoàn tất trước xóa; phản hồi đến sau khi trình duyệt đã biết nguồn bị xóa. Thứ tự được xác lập bằng giao dịch trên máy chủ, không bằng thời điểm nhấn nút. Nếu làm Extended, xóa Notebook chặn toàn bộ tài nguyên con, kể cả lịch sử đã lưu.

Lưu thời hạn tuyệt đối của job. Sau khởi động lại, job còn hạn chỉ được dùng phần thời gian còn lại; job hết hạn phải kết thúc trước khi chạy tiếp hoặc được trả như một job đang chạy hợp lệ. Kết thúc job giải phóng suất đồng thời nhưng không hoàn lại lượt đã tính trong cửa sổ tần suất.

#### 13.2.4. Minh chứng và quyết định

Trong cùng hồ sơ M2, lưu sơ đồ quan hệ, từ điển dữ liệu, OpenAPI, ví dụ, kế hoạch migration và một ADR. Hồ sơ quyết định nêu yêu cầu chi phối, hai phương án, đánh đổi, lựa chọn và cách kiểm. Gắn thiết kế với mã yêu cầu và điều kiện kiểm trong traceability matrix; không chỉ nộp ảnh sơ đồ không có giải thích.

### 13.3. Sử dụng API contract tham khảo

[API contract tham khảo](03_API_Schema_Reference_v1.1.zip) mô tả toàn sản phẩm năm công cụ. Trong bài tập, chọn các phần dùng chung cùng Tóm tắt và Quiz theo bảng phạm vi. Không triển khai ba công cụ ngoài bài tập chỉ vì chúng xuất hiện trong `schemas.json` hoặc OpenAPI.

Học viên có thể sử dụng cấu trúc tham khảo hoặc chọn cách biểu diễn khác nếu giữ hành vi SRS. Giải nén gói kỹ thuật ngay trong thư mục chứa Requirements để tạo thư mục `API_Schema_Reference`. `openapi.json`, `schemas.json` và `examples.json` là các file dùng khi thiết kế; `Domain_Checks.md` bổ sung kiểm tra ngoài schema. Chạy công cụ kiểm theo `README.md` trong gói nếu cần kiểm cấu trúc.

Việc sao chép file OpenAPI chưa hoàn thành LR-11: phải giải thích cách áp dụng vào bài làm và kiểm API thực tế khớp thiết kế.

| Điểm tích hợp | API Starter | Hợp đồng tham khảo | Yêu cầu đối với bài làm |
| --- | --- | --- | --- |
| Tiếp nhận tài liệu | `/documents` xử lý đồng bộ, trả HTTP 201 khi tài liệu `Ready`. | Có tiền tố `/api/r1`, trả HTTP 202 sau khi tiếp nhận thao tác và cho đọc trạng thái. | Giữ cách xử lý đồng bộ của Starter làm điểm xuất phát. Nếu chọn đổi sang giao tiếp bất đồng bộ, phải ghi quyết định thiết kế, bổ sung lưu trạng thái và kiểm tích hợp trước khi thay luồng. SRS không bắt buộc một hệ thống hàng đợi riêng. |
| Xác thực và quyền | Auth scaffold: phiên Better Auth email và mật khẩu, `current_user` ở API, `requireSession` ở web. Chưa có Notebook, ownership và chính sách tài khoản. | Đề xuất phiên phía máy chủ, cơ chế bảo vệ yêu cầu và tài nguyên theo quyền. | Học viên hoàn thiện nghiệp vụ tài khoản, xác định chủ sở hữu ở máy chủ và kiểm quyền trước mọi thao tác. Cơ chế kế thừa phải được đánh giá so với SRS trong bảng fit-gap; thay scaffold thì ghi ADR. |
| Tham chiếu nguồn | Có định danh và cấu trúc phản hồi của nền; nguồn mất hiệu lực có thể được biểu diễn bằng `available: false` và `excerpt: null`. | Nguồn không còn khả dụng bỏ trường vị trí và đoạn trích. | Không giả định hai dạng phản hồi tương thích. Định nghĩa phép chuyển đổi hoặc cập nhật API/giao diện nhất quán; giao tiếp đích tuân quy tắc trường hiện diện tại SRS 3.7.7 và không trả dữ liệu nguồn đã xóa. |
| Lịch sử hỏi đáp | Kết quả phục vụ đối soát có trong bản ghi thao tác. | Có Conversation và ChatTurn tồn tại như dữ liệu nghiệp vụ. | Hỏi đáp giữ bảng operation của Starter cho idempotency và deadline, bổ sung bảng Conversation và lượt hỏi đáp độc lập với thời hạn bản ghi thao tác; không dùng `ai_jobs` cho hỏi đáp (mã D8). Kiểm đọc lại sau khởi động lại và sau hết thời hạn chống gửi lặp. |
| Chống trùng tài liệu | Phạm vi dữ liệu nền. | Tài liệu thuộc Notebook và người dùng. | Giới hạn chống trùng theo Notebook, kiểm quyền, không để tải cùng file làm lộ dữ liệu người khác. |
| AI job | AI Job scaffold: bảng `ai_jobs` theo người dùng, `GET /ai-jobs/{id}`, policy mặc định từ chối, envelope lỗi có `fields` và `retry_after_seconds`. | `GenerationJob` và `ExecutionProfile` có `provider_id`, `fallback_used`. | Giữ hoặc mở rộng cơ chế kế thừa qua ADR; thêm endpoint tạo job, Output, khóa ngoại Notebook và policy của bài làm cho Tóm tắt và Quiz. |

API Starter và hợp đồng tham khảo là đầu vào thiết kế. Hợp đồng của bài làm phải là nguồn thống nhất giữa Web, API và test sau khi học viên chọn phương án. Định danh kỹ thuật, đường dẫn và cách lưu có thể khác; quy tắc nghiệp vụ và các giới hạn SRS vẫn giữ nguyên.

<a id="tich-hop-starter"></a>

### 13.4. Quyền sở hữu và nhập dữ liệu nền

Máy chủ suy ra người dùng từ phiên hợp lệ, xác định Notebook thật sự chứa đối tượng rồi kiểm quyền. Không sử dụng `owner_id` hoặc Notebook do client tự khai làm căn cứ cấp quyền. Tập tài liệu được phép phải được xác định trước khi truy xuất, không đợi đến phản hồi mới lọc dữ liệu người khác.

Nếu cần nhập dữ liệu nền chưa có chủ sở hữu, người vận hành chỉ định tài khoản và Notebook đích bằng thao tác có kiểm soát. Kiểm dữ liệu mất liên kết và quan hệ sai chủ sở hữu trước khi đưa vào sử dụng. Không tự gán cho người đăng ký đầu tiên. Đây là nhập dữ liệu nền, không phải chức năng chuyển chủ sở hữu Notebook hoặc chuyển tài nguyên giữa các Notebook.

Migration thực hiện trên dữ liệu đã có, theo hướng tiến tới cấu trúc mới. Có bản sao lưu và phương án phục hồi ứng dụng; không dùng xóa volume để thay cho chuyển đổi dữ liệu. Khóa ngoại, chỉ mục, cách lưu phiên hoặc bộ đếm là quyết định của thiết kế, không phải danh sách bảng bắt buộc do đề bài cung cấp.

**Điểm đọc code trước khi tích hợp:** bảng sau chỉ rõ nền cần mở rộng, không cung cấp lời giải nghiệp vụ. Dùng ADR để chọn cấu trúc cụ thể, giữ hành vi SRS.

| Vị trí Starter | Giới hạn nền hiện tại | Phần học viên tự thiết kế và kiểm |
| --- | --- | --- |
| `api/app/routers/documents.py`, `chat.py` và `operations.py` | Endpoint demo kế thừa còn công khai, chưa kiểm phiên/Notebook/ownership; `current_user` của Auth scaffold đã sẵn để dùng. | Xác lập session phía server và quyền của đúng đối tượng tại mọi đường đọc/ghi, source/citation và reconciliation; thử tài khoản A/B. |
| `api/app/services/retrieval.py` | `ready_document_ids(None)` chọn tài liệu Ready của thư viện chung; danh sách ID chỉ được kiểm trạng thái. | Xác định Notebook/owner và lọc tập nguồn trước retrieval; mặc định lấy snapshot nguồn ở lần tiếp nhận đầu, replay không thêm nguồn mới. |
| `infra/db/init.sql`, `api/app/core/operations.py` | Operation record (upload, retry, delete, chat của Starter) có TTL, key toàn cục, chưa là Conversation/Output của bài làm. | Scope operation theo người dùng (hỏi đáp tiếp tục dùng cơ chế này); persistence nghiệp vụ; kiểm gửi lặp, restart và dữ liệu còn sau operation TTL. |
| `api/app/core/ai_jobs.py`, `api/migrations/005_ai_jobs.sql` | AI Job scaffold: idempotency theo người dùng, LIM-10, LIM-11, publish fence, `DenyAllPolicy`; chưa có executor, Output, fallback. | Policy BR-08/BR-09, executor, Output, fallback và usage cho Tóm tắt và Quiz; test trên endpoint tích hợp. Chat không chuyển vào cơ chế này (mã D8). |
| `api/app/core/locks.py`, `api/migrations/` | Có cơ chế khóa và migration nền; chưa thay quy tắc vòng đời toàn bộ child resource của Notebook. | Giữ invariant trước khi mở rộng; migration forward trên dữ liệu có sẵn và kiểm các thứ tự xóa/công bố của SRS. |

Tại M2 xác định module và test baseline; tại M3.1 kiểm phần đến hạn của lát cắt Chat, tại M3 mở rộng cho Summary/Quiz và lifecycle còn lại, M4 kiểm tổng hợp. Không chờ M4 mới viết test quyền hoặc characterization; không yêu cầu hoàn thiện toàn bộ phần mở rộng tại M3.1.

### 13.5. Tình huống dùng để rà thiết kế và kiểm triển khai

| Tình huống | Kết quả phải chứng minh |
| --- | --- |
| Dùng ID đối tượng của tài khoản khác, dù Notebook trong request thuộc tài khoản đang đăng nhập. | Không đọc hoặc thay đổi được tài nguyên; phản hồi không tiết lộ sự tồn tại. |
| Gửi lại cùng mã sau khi thêm nguồn hoặc đổi mặc định. | Cùng job và cấu hình của lần đầu; không tạo thêm kết quả hoặc tăng lượt sử dụng. |
| Hai yêu cầu mới tranh quota hoặc suất AI. | Chỉ tiếp nhận số lượng được phép; dữ liệu thao tác và quota nhất quán. |
| Nộp cùng lần làm Quiz đồng thời hoặc gửi lại lựa chọn khác sau nộp. | Chỉ chấm và lưu một lần; trả kết quả đã lưu nếu còn quyền. |
| Đọc dữ liệu có phiên bản cấu trúc chưa hỗ trợ; đổi tên kết quả rồi mở lại (nếu làm Extended). | Nội dung và nguồn không đổi; phiên bản chưa hỗ trợ báo lỗi an toàn, giữ dữ liệu. |
| Xóa tài liệu nguồn khi job chưa công bố (xóa Notebook hoặc hội thoại nếu làm Extended); nhận phản hồi muộn. | Hành vi đúng thứ tự BR-08/BR-09 và quyền hiện tại; không tái tạo dữ liệu đã xóa. |
| Khởi động lại trước hoặc sau thời hạn; bản ghi chống gửi lặp hết hiệu lực. | Không đặt lại thời hạn, không mất lịch sử nghiệp vụ và không giữ suất của job đã kết thúc. |
| Khôi phục bản sao lưu ở môi trường riêng. | Quan hệ, nội dung, phiên bản và quyền được kiểm; ghi rõ phụ thuộc Auth ngoài cơ sở dữ liệu nếu có. |

Các tình huống trên cụ thể hóa tiêu chí đã được giao. Ghi kết quả trong cùng traceability matrix của LR-20 đến LR-22, không tạo thêm bộ kết luận độc lập. Tham khảo `Domain_Checks.md` trong [gói API/Schema](03_API_Schema_Reference_v1.1.zip), chọn phần thuộc bài tập và kiểm trên sản phẩm thực tế.

### 13.6. Điều kiện để bắt đầu tích hợp

Trước phần phát triển phụ thuộc, học viên cần giải thích được: đối tượng thuộc ai; trường nào được phép đọc hoặc sửa ở từng trạng thái; API nào được giữ hoặc thay; giao dịch nào bảo vệ tính nhất quán; dữ liệu được chuyển đổi ra sao; và dùng phép kiểm nào chứng minh các lựa chọn đó. Ghi điểm chưa có căn cứ cùng bước kiểm tiếp theo để giảng viên hỗ trợ. Không tự suy đoán nghiệp vụ còn chưa rõ từ mã nguồn nền hoặc mặc định của thư viện.

<a id="auth-email"></a>

## 14. Auth, Google và email: thử tích hợp và kiểm chứng

Mục tiêu là chọn giải pháp xác thực có evidence đáp ứng SRS trước khi phát triển phần phụ thuộc. Thử khả thi tại M2.1 tập trung rủi ro của giải pháp; hoàn thiện nghiệp vụ ở M3 và tổng hợp kiểm đầy đủ tại M4. Starter cấp Auth scaffold (plumbing email và mật khẩu); nghiệp vụ tài khoản và chính sách theo SRS là bài của học viên. Khôi phục và đổi mật khẩu, đăng nhập Google và liên kết danh tính là Extended.

### 14.1. Chuẩn bị và trách nhiệm

| Đầu vào | Trách nhiệm |
| --- | --- |
| Quyền Google, tài khoản thử và cấu hình nhận kết quả xác thực (khi làm Extended) | Giảng viên hoặc quản trị lớp cấp môi trường được phép. Học viên cấu hình đúng địa chỉ callback của giải pháp đã chọn. |
| Dịch vụ email và hộp thư nhận thử | Lớp cung cấp quyền hoặc phương án sử dụng được phép. Hộp thư mô phỏng tại máy (Mailpit của Starter) chỉ phục vụ phát triển; phép kiểm thật phải có thư tới hộp thư bên ngoài. |
| Thư viện hoặc dịch vụ xác thực | Học viên so sánh khả năng đăng nhập mật khẩu, xác minh và thu hồi phiên (Google, liên kết danh tính, tái xác thực nếu làm Extended); ghi phiên bản và phần cần bổ sung. |
| Chính sách nghiệp vụ | Dùng BR-02/BR-03, LIM-01, LIM-07 đến LIM-09, LIM-19 và mục 3.2.4/3.2.6 của [SRS](02_SRS_InsightHub_v1.1.md). Giá trị mặc định của thư viện không thay yêu cầu. |
| Dữ liệu thử | Hai tài khoản độc lập; các trường hợp có mật khẩu, chờ xác minh và chỉ dùng Google. Chỉ sử dụng email được phép và dữ liệu giả. |
| Secret cấu hình | Chỉ ghi tên biến trong `.env.example`; giá trị thật ở `.env` hoặc kho secret của lớp. Không lưu liên kết xác thực còn hiệu lực vào hồ sơ nộp. |

Trước M2.1, học viên kiểm truy cập các đầu vào được cấp; giảng viên/quản trị lớp xử lý quyền, mạng hoặc tenant thiếu. Học viên vẫn phải cấu hình giải pháp đã chọn và thực hiện spike theo mục 14.2-14.3, rồi xây đầy đủ tại M3. Quyền truy cập dịch vụ không đồng nghĩa nghiệp vụ Auth/email đã được làm sẵn. Ngoài API key AI tự mua theo mục 1.3, không tự mua thêm dịch vụ hoặc gửi dữ liệu ngoài phạm vi được phép để vượt phần bị chặn.

Chọn thành phần xác thực đã có thay vì tự viết thuật toán mật mã. Mặc định của lớp là Better Auth; fit-gap giữa mặc định thư viện và SRS, kiến trúc cần ADR và điểm kiểm tối thiểu tại [Auth Integration Guide](../Auth_Integration_Guide.md). Học viên vẫn chịu trách nhiệm kiểm quyền nghiệp vụ tại máy chủ theo [hướng dẫn tích hợp](#data-api).

### 14.2. Thực hiện theo mốc

| Mốc | Công việc và đầu ra |
| --- | --- |
| M2.1 | Spike theo mục 6.2: khoảng cách chính sách SRS với Auth scaffold (Pending, LIM-01, thời hạn và thu hồi phiên), gửi/nhận/hành động EML-001 thật; Google và linking nếu làm Extended. Ghi capability, actual, giới hạn và quyết định. Chưa yêu cầu ghép vào UI/API/DB nghiệp vụ chính. |
| M2 | Bảng fit-gap đánh giá cơ chế kế thừa (Auth scaffold) so với SRS, ghi phần giữ, sửa, thay và căn cứ; ADR khi thay scaffold. Thiết kế phiên, danh tính, dữ liệu điều khiển và quyền phù hợp kết quả thử. |
| M3.1 | Dùng Auth scaffold tích hợp đăng nhập email và mật khẩu, session thực cho hành trình Notebook - Document - Chat; có EML-001 và xác minh email. Hoàn thiện phần Core còn lại (phiên, đăng xuất) ở M3. |
| M3 | Hoàn thiện các luồng tài khoản cùng email giao dịch tầng Core (EML-001); tích hợp với Notebook và giao diện; luồng Extended nếu còn thời gian. Ghi kiểm chứng cùng chức năng. |
| M4 | Kiểm đủ điều kiện áp dụng, các trường hợp lỗi, biên thời gian, API trực tiếp, trình duyệt và tích hợp thật. Kiểm lại phần thay đổi sau thử sớm. |

### 14.3. Ma trận hành vi cần kiểm

M2.1 chọn phép thử đại diện trong các nhóm email EML-001, Pending và session (Google, linking nếu làm Extended) để quyết định giải pháp theo mục 6.2. Bảng dưới là phạm vi hành vi tích lũy tới M4, không phải yêu cầu triển khai toàn bộ Auth trong spike. Mọi dòng tầng Core phải được hoàn thiện và có kết quả trước khi kết luận đạt phần xác thực tại M4.

| Tình huống | Expected result |
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

Các dòng Google, liên kết Google với tài khoản có mật khẩu hoặc chờ xác minh, khôi phục hoặc đổi mật khẩu, tài khoản chỉ dùng Google, phiên chờ xác minh, giới hạn thử mật khẩu và giới hạn yêu cầu gửi email thuộc AC tầng Extended (mục 2.1.5); khi chưa làm, ghi `Extended-NotDone`, không hiển thị chức năng trên giao diện và không mở endpoint nghiệp vụ tương ứng của bài làm; vẫn kiểm phần Core liên quan, ví dụ tài khoản `PendingVerification` không truy cập Notebook (IH-AUTH-001-AC01). Có thể mô phỏng lỗi provider và thời gian để kiểm ngoại lệ; phải ghi rõ chế độ chạy. Không đánh dấu đăng nhập Google hoặc email thật đã đạt chỉ từ kết quả mô phỏng.

### 14.4. Kiểm email giao dịch theo tầng

M2.1 dùng luồng xác minh EML-001 để kiểm dịch vụ và hành động trong spike. M3 tích hợp các loại dưới đây vào đúng nghiệp vụ ứng dụng theo tầng (EML-002 đến EML-005 thuộc Extended); M4 tổng hợp kết quả các nhánh, lỗi và giới hạn. Giữ evidence spike riêng với evidence của chức năng đã tích hợp.

| Mã | Tình huống | Kết quả cần quan sát |
| --- | --- | --- |
| EML-001 | Đăng ký (gửi lại xác minh nếu làm Extended) | Nhận thư đúng hộp thư, liên kết có hiệu lực đúng quy tắc và hoàn tất xác minh. |
| EML-002 | Khôi phục tài khoản có mật khẩu (Extended) | Nhận liên kết đặt lại dùng một lần; mật khẩu chỉ thay sau khi hoàn tất thao tác hợp lệ. |
| EML-003 | Liên kết Google thành công (Extended) | Nhận thông báo và hướng dẫn hỗ trợ; thư không có liên kết cấp quyền. |
| EML-004 | Khôi phục tài khoản chỉ dùng Google (Extended) | Nhận hướng dẫn đăng nhập Google, không có liên kết tạo mật khẩu. |
| EML-005 | Đặt lại hoặc đổi mật khẩu thành công (Extended) | Nhận thông báo và hướng dẫn đăng nhập lại; không chứa mật khẩu hoặc liên kết cấp phiên. |

Minh chứng ghi loại thư, tài khoản đã che địa chỉ, thời điểm, mã chuyển giao an toàn, thư thực nhận và kết quả hành động. Nhật ký “dịch vụ đã nhận yêu cầu” chưa chứng minh thư tới hộp thư. Che liên kết và token còn hiệu lực trong ảnh hoặc log.

### 14.5. Hồ sơ và phụ thuộc chưa hoàn tất

Ghi expected result, actual result, chế độ chạy, phiên bản mã nguồn, cấu hình không chứa secret và quyết định giải pháp vào hồ sơ LR-09/LR-14. Traceability matrix ghi từng điều kiện đã kiểm, chưa kiểm hoặc bị chặn.

Nếu thiếu quyền Google, email hoặc kết nối, nêu yêu cầu bị ảnh hưởng, cách đã thử, người cần hỗ trợ và bước kiểm lại. Tiếp tục phần thiết kế, hộp thư mô phỏng và các test không phụ thuộc dịch vụ. Không tự bỏ tiêu chí hoặc coi mô phỏng là tích hợp thật; phần phụ thuộc phải được giải quyết trước khi kết luận nghiệm thu.

<a id="pham-vi-truy-vet"></a>

## 15. Phạm vi và truy vết SRS

Bảng này là phạm vi giao bài, không phải kết quả test. [SRS InsightHub v1.1](02_SRS_InsightHub_v1.1.md) xác định hành vi sản phẩm; học viên đọc AC cùng yêu cầu thành phần, quy tắc, giới hạn và dữ liệu được dẫn. Việc cần làm và rubric nằm tại mục 3-12 của tài liệu này. Mã LR chỉ dùng để truy vết trong bảng này; danh mục bên dưới dẫn đến đúng công việc, học viên không cần ghi nhớ mã.

### 15.1. Quy tắc phạm vi

Có **73 mã yêu cầu gốc hoặc nhóm yêu cầu và 165 acceptance criteria (AC)** được truy vết. Trong đó, **67 mã gốc với 153 AC thuộc bài tập** (134 AC mã A và 19 AC mã điều chỉnh D1-D6, D8, D9), **6 mã gốc với 12 AC ngoài bài tập**. SRS phân rã 40 nhóm thành 174 yêu cầu thành phần và giữ 33 yêu cầu trực tiếp; mã gốc không đồng nghĩa một nghĩa vụ đơn nhất. AC điều chỉnh vẫn thuộc 153 AC phải kiểm. Đây là số AC được giao, không phải số test case hoặc số AC đã đạt.

| Mã | Cách áp dụng |
| --- | --- |
| A | Giữ hành vi, giới hạn và ngoại lệ đối với các đối tượng thuộc bài tập. Có 134 tiêu chí thuộc nhóm này. |
| D1 | Danh mục công cụ, cấu hình, schema, nguồn, API và lọc theo loại chỉ áp dụng Tóm tắt và Quiz. Bỏ nhánh riêng của Mindmap, Slide và Báo cáo; giữ yêu cầu về dữ liệu, nguồn, trạng thái và an toàn. |
| D2 | Prototype thiết kế (Figma hoặc HTML, theo [LR-10](#lr-10)) và màn hình UI-01 đến UI-08 có đầy đủ hành trình Tóm tắt và Quiz. Trong phạm vi bài tập, yêu cầu "thiết kế Figma" của SRS (OBJ-04, IH-UX-001, IH-REL-002-R07, UAT-15, REF-06) được đáp ứng bằng prototype đã chốt phiên bản: link Figma và phiên bản, hoặc đường dẫn HTML trong repository và commit/tag; không phải triển khai ba công cụ mở rộng. Giữ trạng thái, kích thước hiển thị, thao tác bàn phím và các tiêu chí trải nghiệm khác. |
| D3 | Kiểm tích hợp và nội dung AI thật cho hỏi đáp, Tóm tắt và Quiz: AEV-01, AEV-03, AEV-05 cùng hai lượt lặp, tổng 12 lượt nội dung. Email (và Google nếu làm Extended) vẫn kiểm bằng dịch vụ thật. |
| D4 | Nghiệm thu R1 của bài tập hai công cụ, với 153 AC áp dụng và phần tương ứng trong UAT-01 đến UAT-21 (UAT-02, UAT-03 thuộc Extended). Không kết luận đạt toàn bộ sản phẩm năm công cụ. |
| D5 | IH-MSG-003-AC01 kiểm bằng dịch vụ thật email tầng Core EML-001. EML-002 đi cùng khôi phục mật khẩu (IH-AUTH-006-AC01), EML-003 phụ thuộc liên kết Google (IH-AUTH-005-AC04), EML-004 đi cùng đăng nhập Google và EML-005 (IH-MSG-003-AC03) thuộc Extended. Giữ yêu cầu về liên kết, thời hạn, dùng một lần và lỗi gửi. |
| D6 | IH-UX-003-AC01 (bàn phím, focus, nhãn và lỗi đúng trường) kiểm bắt buộc trên hành trình M3.1 (đăng nhập, Notebook, Document, Chat, mở lại Conversation) và màn làm Quiz. Các màn khác kiểm khi làm Extended. Giữ đủ quy tắc phím và focus của SRS trong phạm vi này. |
| D8 | IH-INT-004-AC02 (tiếp nhận đồng thời đúng hạn mức và quy tắc ghi nhận mục 3.3.2): LIM-10 (một tác vụ AI đang chạy, 10 yêu cầu mới trong 60 giây, tính chung) áp dụng cho Tóm tắt và Quiz qua AI Job scaffold. Hỏi đáp giữ cơ chế operation của Starter (idempotency, deadline LIM-11), không tính vào LIM-10 trong bài tập. UAT-20 kiểm hai yêu cầu đồng thời trên Tóm tắt, Quiz. Giữ quy tắc idempotency mục 3.3.2 cho cả hỏi đáp (IH-CHAT-005-AC01). Nhánh xóa hội thoại, Notebook trong lúc xử lý chỉ kiểm khi đã làm Extended; nhánh xóa tài liệu kiểm theo D9. |
| D9 | IH-DATA-002-AC04 (kết quả muộn và đường truy cập cũ không tái tạo hoặc phục vụ nội dung đã xóa) áp dụng cho tài liệu đã xóa (IH-DOC-006): kết quả muộn của Tóm tắt, Quiz và đường truy cập cũ của hỏi đáp (citation, cache, replay `operation_records`). Chặn công bố câu trả lời hỏi đáp đang xử lý là IH-CHAT-005-AC02 (Extended). Xóa Notebook, kết quả AI và hội thoại là Extended; khi làm các thao tác đó, kiểm thêm theo AC này. |
| N | Ngoài bài tập bắt buộc: Mindmap, Slide và Báo cáo. Ghi ngoài phạm vi (`OutOfScope`), không ghi đạt. Nếu tự làm thêm, bổ sung test và đánh giá AI riêng. |

Các nhóm D1-D6, D8, D9 gồm 19 tiêu chí và đã nằm trong tổng 153 tiêu chí áp dụng; không phải phần được miễn kiểm. D7 là quyết định phân tầng Core/Extended tại mục 2.1.5, không phải mã phạm vi. Các quy tắc nghiệp vụ, giới hạn, use case, dữ liệu, yêu cầu phi chức năng và thông báo vẫn áp dụng cho phần được giao. Giữ yêu cầu của email EML-001 đến EML-005 theo tầng tại mục 2.1.5 và mã D5, xác thực, quyền, các lần làm Quiz và ngoại lệ.

- UAT-11 kiểm Tóm tắt, Quiz và vòng đời kết quả; không yêu cầu ba công cụ mở rộng.
- UAT-15 kiểm màn hình UI-01 đến UI-08 trong phạm vi D2 và D6. UAT-14, UAT-20 và AEV-07 kiểm cấu trúc Tóm tắt và Quiz cùng các ngoại lệ liên quan; UAT-14 có thêm ca fallback của IH-AI-005; UAT-20 kiểm xử lý đồng thời và LIM-10 trên Tóm tắt và Quiz theo D8.
- UAT-03 (khôi phục, đổi mật khẩu) thuộc Extended. Ở tầng Core, UAT-04 kiểm phần phiên, UAT-10 chỉ kiểm dữ liệu Core (IH-DATA-001-AC02, IH-DATA-001-AC04, IH-DATA-002-AC01, IH-DATA-002-AC03, IH-DATA-002-AC04) và không yêu cầu Note, UAT-12 kiểm xóa tài liệu và đường truy cập cũ theo D9, UAT-17 kiểm thời hạn xử lý tài liệu, hỏi đáp và công cụ AI (10 thao tác không gọi AI là Extended), UAT-18 kiểm IH-MSG-004-AC01, UAT-19 kiểm EML-001 và lỗi gửi.
- AC Core có gắn UAT-02, UAT-03 trong bảng 15.4 (ví dụ IH-AUTH-002-AC01, IH-NFR-001-AC05) kết luận qua UAT-01, UAT-19 hoặc test riêng của AC đó.
- AEV-02, AEV-04 và AEV-06 ngoài bài tập. AEV-08 giữ bốn tình huống đại diện; không thay kiểm quyền của từng loại tài nguyên.
- Giới hạn 1-3 nguồn của LIM-05 áp dụng cho công cụ AI. Hỏi đáp không chỉ định nguồn sử dụng tập tài liệu `Ready` của Notebook tại lần tiếp nhận đầu theo BR-05 và IH-CHAT-001.
- Mỗi AC có kết luận riêng dù dùng chung test case. Liên kết UAT trỏ tới kịch bản tổng hợp, không thay điều kiện kiểm chi tiết.

### 15.2. Từ yêu cầu học tập tới năng lực và rubric

Mã khóa học, đơn vị và chủ đề có tiền tố B2BC07. PLO là chuẩn đầu ra chương trình, CLO là chuẩn đầu ra khóa học; các mã theo chương trình được giảng viên cung cấp. Một dòng có khoảng LR áp dụng cho từng công việc trong khoảng đó.

| Công việc | Chuẩn đầu ra chương trình/khóa học | Đơn vị/chủ đề | Đầu ra | Nhóm đánh giá |
| --- | --- | --- | --- | --- |
| LR-01..03 | PLO-1 / C01-CLO-1,2 | C01-U01 T01-T04 | Môi trường, prompt và kết quả kiểm AI | Kiểm chứng đầu ra AI |
| LR-04..05 | PLO-1 / C01-CLO-3,4 | C01-U02 T01-T04 | Hướng dẫn AI và quy trình agent | Quy trình agent và kiểm soát quyền |
| LR-06..07 | PLO-1 / C02-CLO-1 | C02-U01 T01-T04 | Hồ sơ dự án, backlog và CI | Phạm vi và kế hoạch |
| LR-08..09 | PLO-2 / C02-CLO-2 | C02-U02 T01-T04 | Yêu cầu, test case và thử tích hợp | Spec và truy vết yêu cầu |
| LR-10..11 | PLO-3 / C02-CLO-3 | C02-U03 T01-T05 | Prototype (Figma hoặc HTML), API, dữ liệu, quyết định kiến trúc và threat model sơ bộ | Thiết kế giao diện, API và dữ liệu |
| LR-12..13 | PLO-4 / C02-CLO-4 | C02-U04 T01-T03 | Hành trình Auth - Notebook - Document - Chat và TDD | Chức năng và TDD |
| LR-14..18 | PLO-4 / C02-CLO-4 | C02-U04 T01-T04; C02-U03-T02 | Auth, Email, Notebook/Document/Conversation, Summary, Quiz và AI Output tầng Core; Extended khi còn thời gian | Chức năng sản phẩm |
| LR-19 | PLO-4 / C02-CLO-4 | C02-U04 T05-T08 | Module refactor và task tự động | Refactor, tự động hóa và Assignment |
| LR-20..22 | PLO-5 / C02-CLO-5 | C02-U05 T01-T03 | Kết quả test và nghiệm thu | Test, nghiệm thu và phân quyền |
| LR-23 | PLO-5 / C02-CLO-5 | C02-U05-T04 | Golden set, grader và kết quả eval AI | Chất lượng nội dung AI |
| LR-24 | PLO-1,5 / C01-CLO-4, C02-CLO-5 | C02-U05 T05-T06; C02-U03-T05; C01-U02-T04 | Threat model cập nhật, scan, SBOM/AI-BOM và kiểm bảo mật | Bảo mật ứng dụng và quy trình AI |
| LR-25..26 | PLO-6 / C02-CLO-6 | C02-U06 T01-T04 | Bản phát hành, runbook và restore | Phát hành và khôi phục |
| LR-27 | PLO-6 / C02-CLO-6 | C02-U06 T01-T04 | Hồ sơ thay đổi và regression | Thay đổi sau phát hành |
| LR-28 | PLO-1..6 / C02-CLO-1..6 | C02-U07 T01-T04 | Demo và vấn đáp | Demo và vấn đáp |
| LR-29 | PLO-6 / C02-CLO-6 | C02-U07 T01-T04 | Kế hoạch áp dụng 30 ngày | Kế hoạch áp dụng 30 ngày |

LR-01 đến LR-11 là chuẩn bị, phân tích và thiết kế; LR-20..24 kiểm các AC đã triển khai ở LR-12..18. Vì vậy một AC có thể tham chiếu thêm nhiều LR trong traceability matrix bài làm. Các hoạt động Foundation, TDD, refactor và vấn đáp không bị ép thành yêu cầu sản phẩm mới.

Mã LR là công việc học tập; mã IH là yêu cầu sản phẩm; AC là acceptance criteria (tiêu chí chấp nhận); UAT là kịch bản nghiệm thu tổng hợp; AEV là test case đánh giá AI. Các mã phục vụ tra cứu, không thay nội dung nhiệm vụ.

#### 15.2.1. Tra công việc theo mã truy vết

| Mã trong bảng | Milestone | Việc cần làm |
| --- | --- | --- |
| LR-01 | M0.1 | [Khởi động starter](#lr-01) |
| LR-02 | M0.1 | [Tạo đầu ra có cấu trúc](#lr-02) |
| LR-03 | M0.1 | [Phát hiện và sửa một lỗi AI](#lr-03) |
| LR-04 | M0.2 | [Viết AI Usage Charter cho dự án](#lr-04) |
| LR-05 | M0.2 | [Thực hành một quy trình agent có dùng công cụ và MCP](#lr-05) |
| LR-06 | M1 | [Lập hồ sơ dự án và backlog](#lr-06) |
| LR-07 | M1 | [Thiết lập quy trình phát triển](#lr-07) |
| LR-08 | M2.1 | [Lập bảng yêu cầu và test case](#lr-08) |
| LR-09 | M2.1 | [Thử tích hợp trước khi chốt thiết kế](#lr-09) |
| LR-10 | M2 | [Prototype thiết kế (Figma hoặc HTML)](#lr-10) |
| LR-11 | M2 | [Thiết kế API và dữ liệu](#lr-11) |
| LR-12 | M3.1 | [Triển khai Auth - Notebook - Document - Chat](#lr-12) |
| LR-13 | M3.1 | [Thực hiện TDD cho một hành vi có rủi ro](#lr-13) |
| LR-14 | M3 | [Hoàn thiện Auth và transactional email tầng Core](#lr-14) |
| LR-15 | M3 | [Hoàn thiện Notebook, Document, Conversation (Core) và Note (Extended)](#lr-15) |
| LR-16 | M3 | [Xây dựng Tóm tắt](#lr-16) |
| LR-17 | M3 | [Xây dựng Quiz](#lr-17) |
| LR-18 | M3 | [Hoàn thiện vòng đời công cụ AI](#lr-18) |
| LR-19 | M3 | [Refactor một module và tự động hóa một task](#lr-19) |
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
| DOC; CHAT còn lại; nền thao tác và tích hợp dịch vụ | Giảng viên cung cấp nền; học viên tích hợp Notebook, quyền sở hữu, quota, vòng đời và kiểm regression phần bị ảnh hưởng. |
| AI, DATA, INT | Sử dụng điểm mở rộng của nền; học viên thiết kế dữ liệu, chính sách và tích hợp xác thực, email, Tóm tắt, Quiz. |
| UX, MSG | Học viên thiết kế và triển khai giao diện, thông báo và email; minh chứng thể hiện cả hành vi và trạng thái. |
| NFR, REL | Học viên kiểm trên bản cuối, cập nhật test, vận hành, sao lưu và gói bàn giao theo dữ liệu bài làm. |

### 15.4. Danh mục từng AC

Cột mốc ghi thời điểm hoàn thiện và kiểm tổng hợp của AC. Phần triển khai trước đó, gồm hành trình M3.1, được xác định tại [ma trận chức năng](#ma-tran-chuc-nang); các bước chuẩn bị không bị bỏ qua chỉ vì không xuất hiện trong cột mốc. Tại M2.1, rà đầy đủ phạm vi và phân tích sâu yêu cầu đại diện; tại M2, hoàn thiện thiết kế; khi phát triển và xử lý thay đổi, cập nhật cùng traceability matrix. Dùng danh mục dưới đây làm khung, thêm mã yêu cầu thành phần, điều kiện kiểm và liên kết kết quả theo [mẫu kết quả](#bang-ket-qua). Mỗi AC có kết luận tổng hợp riêng, chỉ đạt khi mọi điều kiện áp dụng đều đạt. Không ghi đạt cho điều kiện chưa chạy.

| Mã yêu cầu gốc | AC | Phạm vi | Tầng | Công việc hoàn thiện | Mốc hoàn thiện/kiểm tổng hợp | Nghiệm thu liên quan |
| --- | --- | --- | --- | --- | --- | --- |
| IH-AUTH-001 | IH-AUTH-001-AC01 | A | Core | LR-14 | M3 → M4 | UAT-01 |
| IH-AUTH-001 | IH-AUTH-001-AC02 | A | Core | LR-14 | M3 → M4 | UAT-01 |
| IH-AUTH-002 | IH-AUTH-002-AC01 | A | Core | LR-14 | M3 → M4 | UAT-01, UAT-03 |
| IH-AUTH-002 | IH-AUTH-002-AC02 | A | Extended | LR-14 | M3 → M4 | UAT-01, UAT-03 |
| IH-AUTH-003 | IH-AUTH-003-AC01 | A | Core | LR-14 | M3 → M4 | UAT-01 |
| IH-AUTH-003 | IH-AUTH-003-AC02 | A | Extended | LR-14 | M3 → M4 | UAT-01 |
| IH-AUTH-004 | IH-AUTH-004-AC01 | A | Extended | LR-14 | M3 → M4 | UAT-02 |
| IH-AUTH-004 | IH-AUTH-004-AC02 | A | Extended | LR-14 | M3 → M4 | UAT-02 |
| IH-AUTH-005 | IH-AUTH-005-AC01 | A | Extended | LR-14 | M3 → M4 | UAT-02, UAT-03 |
| IH-AUTH-005 | IH-AUTH-005-AC02 | A | Extended | LR-14 | M3 → M4 | UAT-02, UAT-03 |
| IH-AUTH-005 | IH-AUTH-005-AC03 | A | Extended | LR-14 | M3 → M4 | UAT-02, UAT-03 |
| IH-AUTH-005 | IH-AUTH-005-AC04 | A | Extended | LR-14 | M3 → M4 | UAT-02, UAT-03 |
| IH-AUTH-006 | IH-AUTH-006-AC01 | A | Extended | LR-14 | M3 → M4 | UAT-03 |
| IH-AUTH-006 | IH-AUTH-006-AC02 | A | Extended | LR-14 | M3 → M4 | UAT-03 |
| IH-AUTH-007 | IH-AUTH-007-AC01 | A | Extended | LR-14 | M3 → M4 | UAT-03 |
| IH-AUTH-007 | IH-AUTH-007-AC02 | A | Extended | LR-14 | M3 → M4 | UAT-03 |
| IH-AUTH-007 | IH-AUTH-007-AC03 | A | Extended | LR-14 | M3 → M4 | UAT-03 |
| IH-AUTH-008 | IH-AUTH-008-AC01 | A | Core | LR-14 | M3 → M4 | UAT-04 |
| IH-AUTH-008 | IH-AUTH-008-AC02 | A | Core | LR-14 | M3 → M4 | UAT-04 |
| IH-AUTH-009 | IH-AUTH-009-AC01 | A | Extended | LR-14 | M3 → M4 | UAT-04 |
| IH-AUTH-009 | IH-AUTH-009-AC02 | A | Extended | LR-14 | M3 → M4 | UAT-04 |
| IH-AUTH-010 | IH-AUTH-010-AC01 | A | Extended | LR-14 | M3 → M4 | UAT-03 |
| IH-AUTH-010 | IH-AUTH-010-AC02 | A | Extended | LR-14 | M3 → M4 | UAT-03 |
| IH-NB-001 | IH-NB-001-AC01 | A | Core | LR-15 | M3 → M4 | UAT-05 |
| IH-NB-001 | IH-NB-001-AC02 | A | Core | LR-15 | M3 → M4 | UAT-05 |
| IH-NB-002 | IH-NB-002-AC01 | A | Core | LR-15 | M3 → M4 | UAT-05 |
| IH-NB-002 | IH-NB-002-AC02 | A | Extended | LR-15 | M3 → M4 | UAT-05 |
| IH-NB-003 | IH-NB-003-AC01 | A | Extended | LR-15 | M3 → M4 | UAT-12 |
| IH-NB-003 | IH-NB-003-AC02 | A | Extended | LR-15 | M3 → M4 | UAT-12 |
| IH-NB-004 | IH-NB-004-AC01 | A | Core | LR-15 | M3 → M4 | UAT-13 |
| IH-NB-004 | IH-NB-004-AC02 | A | Core | LR-15 | M3 → M4 | UAT-13 |
| IH-DOC-001 | IH-DOC-001-AC01 | A | Core | LR-15 | M3 → M4 | UAT-06 |
| IH-DOC-001 | IH-DOC-001-AC02 | A | Core | LR-15 | M3 → M4 | UAT-06 |
| IH-DOC-002 | IH-DOC-002-AC01 | A | Core | LR-15 | M3 → M4 | UAT-06 |
| IH-DOC-002 | IH-DOC-002-AC02 | A | Core | LR-15 | M3 → M4 | UAT-06 |
| IH-DOC-003 | IH-DOC-003-AC01 | A | Core | LR-15 | M3 → M4 | UAT-07 |
| IH-DOC-003 | IH-DOC-003-AC02 | A | Extended | LR-15 | M3 → M4 | UAT-07 |
| IH-DOC-004 | IH-DOC-004-AC01 | A | Core | LR-15 | M3 → M4 | UAT-07 |
| IH-DOC-004 | IH-DOC-004-AC02 | A | Core | LR-15 | M3 → M4 | UAT-07 |
| IH-DOC-005 | IH-DOC-005-AC01 | A | Extended | LR-15 | M3 → M4 | UAT-06, UAT-08, UAT-12 |
| IH-DOC-005 | IH-DOC-005-AC02 | A | Core | LR-15 | M3 → M4 | UAT-06, UAT-08, UAT-12 |
| IH-DOC-006 | IH-DOC-006-AC01 | A | Core | LR-15 | M3 → M4 | UAT-12 |
| IH-DOC-006 | IH-DOC-006-AC02 | A | Extended | LR-15 | M3 → M4 | UAT-12 |
| IH-CHAT-001 | IH-CHAT-001-AC01 | A | Core | LR-15 | M3 → M4 | UAT-08 |
| IH-CHAT-001 | IH-CHAT-001-AC02 | A | Core | LR-15 | M3 → M4 | UAT-08 |
| IH-CHAT-002 | IH-CHAT-002-AC01 | A | Core | LR-15 | M3 → M4 | UAT-08 |
| IH-CHAT-002 | IH-CHAT-002-AC02 | A | Core | LR-15 | M3 → M4 | UAT-08 |
| IH-CHAT-003 | IH-CHAT-003-AC01 | A | Core | LR-15 | M3 → M4 | UAT-09 |
| IH-CHAT-003 | IH-CHAT-003-AC02 | A | Core | LR-15 | M3 → M4 | UAT-09 |
| IH-CHAT-004 | IH-CHAT-004-AC01 | A | Core | LR-15 | M3 → M4 | UAT-08, UAT-12 |
| IH-CHAT-004 | IH-CHAT-004-AC02 | A | Core | LR-15 | M3 → M4 | UAT-08, UAT-12 |
| IH-CHAT-004 | IH-CHAT-004-AC03 | A | Extended | LR-15 | M3 → M4 | UAT-08, UAT-12 |
| IH-CHAT-004 | IH-CHAT-004-AC04 | A | Extended | LR-15 | M3 → M4 | UAT-08, UAT-12 |
| IH-CHAT-004 | IH-CHAT-004-AC05 | A | Extended | LR-15 | M3 → M4 | UAT-08, UAT-12 |
| IH-CHAT-005 | IH-CHAT-005-AC01 | A | Core | LR-15 | M3 → M4 | UAT-09, UAT-12 |
| IH-CHAT-005 | IH-CHAT-005-AC02 | A | Extended | LR-15 | M3 → M4 | UAT-09, UAT-12 |
| IH-NOTE-001 | IH-NOTE-001-AC01 | A | Extended | LR-15 | M3 → M4 | UAT-10 |
| IH-NOTE-001 | IH-NOTE-001-AC02 | A | Extended | LR-15 | M3 → M4 | UAT-10 |
| IH-NOTE-001 | IH-NOTE-001-AC03 | A | Extended | LR-15 | M3 → M4 | UAT-10 |
| IH-NOTE-001 | IH-NOTE-001-AC04 | A | Extended | LR-15 | M3 → M4 | UAT-10 |
| IH-NOTE-002 | IH-NOTE-002-AC01 | A | Extended | LR-15 | M3 → M4 | UAT-10, UAT-12 |
| IH-NOTE-002 | IH-NOTE-002-AC02 | A | Extended | LR-15 | M3 → M4 | UAT-10, UAT-12 |
| IH-AI-001 | IH-AI-001-AC01 | D1 | Core | LR-18 | M3 → M4 | UAT-11 |
| IH-AI-001 | IH-AI-001-AC02 | D1 | Core | LR-18 | M3 → M4 | UAT-11 |
| IH-AI-002 | IH-AI-002-AC01 | A | Core | LR-18 | M3 → M4 | UAT-11 |
| IH-AI-002 | IH-AI-002-AC02 | A | Core | LR-18 | M3 → M4 | UAT-11 |
| IH-AI-003 | IH-AI-003-AC01 | D1 | Core | LR-18 | M3 → M4 | UAT-11, UAT-14 |
| IH-AI-003 | IH-AI-003-AC02 | A | Extended | LR-18 | M3 → M4 | UAT-11, UAT-14 |
| IH-AI-004 | IH-AI-004-AC01 | D1 | Core | LR-18 | M3 → M4 | UAT-11, UAT-12 |
| IH-AI-004 | IH-AI-004-AC02 | A | Core | LR-18 | M3 → M4 | UAT-11, UAT-12 |
| IH-AI-005 | IH-AI-005-AC01 | A | Core | LR-18 | M3 → M4 | UAT-14 |
| IH-AI-005 | IH-AI-005-AC02 | A | Core | LR-18 | M3 → M4 | UAT-14 |
| IH-MM-001 | IH-MM-001-AC01 | N | Ngoài phạm vi | - | Mở rộng | UAT-11 |
| IH-MM-001 | IH-MM-001-AC02 | N | Ngoài phạm vi | - | Mở rộng | UAT-11 |
| IH-MM-002 | IH-MM-002-AC01 | N | Ngoài phạm vi | - | Mở rộng | UAT-11, UAT-15 |
| IH-MM-002 | IH-MM-002-AC02 | N | Ngoài phạm vi | - | Mở rộng | UAT-11, UAT-15 |
| IH-SUM-001 | IH-SUM-001-AC01 | A | Core | LR-16 | M3 → M4 | UAT-11 |
| IH-SUM-001 | IH-SUM-001-AC02 | A | Core | LR-16 | M3 → M4 | UAT-11 |
| IH-SUM-002 | IH-SUM-002-AC01 | A | Extended | LR-16 | M3 → M4 | UAT-10, UAT-11 |
| IH-SUM-002 | IH-SUM-002-AC02 | A | Extended | LR-16 | M3 → M4 | UAT-10, UAT-11 |
| IH-SLD-001 | IH-SLD-001-AC01 | N | Ngoài phạm vi | - | Mở rộng | UAT-11 |
| IH-SLD-001 | IH-SLD-001-AC02 | N | Ngoài phạm vi | - | Mở rộng | UAT-11 |
| IH-SLD-002 | IH-SLD-002-AC01 | N | Ngoài phạm vi | - | Mở rộng | UAT-11, UAT-15 |
| IH-SLD-002 | IH-SLD-002-AC02 | N | Ngoài phạm vi | - | Mở rộng | UAT-11, UAT-15 |
| IH-QUIZ-001 | IH-QUIZ-001-AC01 | A | Core | LR-17 | M3 → M4 | UAT-11 |
| IH-QUIZ-001 | IH-QUIZ-001-AC02 | A | Core | LR-17 | M3 → M4 | UAT-11 |
| IH-QUIZ-002 | IH-QUIZ-002-AC01 | A | Core | LR-17 | M3 → M4 | UAT-11 |
| IH-QUIZ-002 | IH-QUIZ-002-AC02 | A | Core | LR-17 | M3 → M4 | UAT-11 |
| IH-RPT-001 | IH-RPT-001-AC01 | N | Ngoài phạm vi | - | Mở rộng | UAT-11 |
| IH-RPT-001 | IH-RPT-001-AC02 | N | Ngoài phạm vi | - | Mở rộng | UAT-11 |
| IH-RPT-002 | IH-RPT-002-AC01 | N | Ngoài phạm vi | - | Mở rộng | UAT-11, UAT-13 |
| IH-RPT-002 | IH-RPT-002-AC02 | N | Ngoài phạm vi | - | Mở rộng | UAT-11, UAT-13 |
| IH-OUT-001 | IH-OUT-001-AC01 | D1 | Core | LR-18 | M3 → M4 | UAT-11, UAT-13 |
| IH-OUT-001 | IH-OUT-001-AC02 | A | Core | LR-18 | M3 → M4 | UAT-11, UAT-13 |
| IH-OUT-002 | IH-OUT-002-AC01 | A | Extended | LR-18 | M3 → M4 | UAT-11, UAT-12 |
| IH-OUT-002 | IH-OUT-002-AC02 | A | Extended | LR-18 | M3 → M4 | UAT-11, UAT-12 |
| IH-OUT-003 | IH-OUT-003-AC01 | A | Extended | LR-18 | M3 → M4 | UAT-12 |
| IH-OUT-003 | IH-OUT-003-AC02 | A | Extended | LR-18 | M3 → M4 | UAT-12 |
| IH-DATA-001 | IH-DATA-001-AC01 | D1 | Extended | LR-15/LR-18 | M3 → M4 | UAT-05, UAT-06, UAT-08, UAT-10, UAT-11, UAT-20 |
| IH-DATA-001 | IH-DATA-001-AC02 | D1 | Core | LR-15/LR-18 | M3 → M4 | UAT-05, UAT-06, UAT-08, UAT-10, UAT-11, UAT-20 |
| IH-DATA-001 | IH-DATA-001-AC03 | D1 | Extended | LR-15/LR-18 | M3 → M4 | UAT-05, UAT-06, UAT-08, UAT-10, UAT-11, UAT-20 |
| IH-DATA-001 | IH-DATA-001-AC04 | A | Core | LR-15/LR-18 | M3 → M4 | UAT-05, UAT-06, UAT-08, UAT-10, UAT-11, UAT-20 |
| IH-DATA-001 | IH-DATA-001-AC05 | A | Extended | LR-15/LR-18 | M3 → M4 | UAT-05, UAT-06, UAT-08, UAT-10, UAT-11, UAT-20 |
| IH-DATA-001 | IH-DATA-001-AC06 | A | Extended | LR-15/LR-18 | M3 → M4 | UAT-05, UAT-06, UAT-08, UAT-10, UAT-11, UAT-20 |
| IH-DATA-002 | IH-DATA-002-AC01 | A | Core | LR-17 | M3 → M4 | UAT-10, UAT-11, UAT-12, UAT-20 |
| IH-DATA-002 | IH-DATA-002-AC02 | A | Extended | LR-22 | M3 → M4 | UAT-10, UAT-11, UAT-12, UAT-20 |
| IH-DATA-002 | IH-DATA-002-AC03 | A | Core | LR-17 | M3 → M4 | UAT-10, UAT-11, UAT-12, UAT-20 |
| IH-DATA-002 | IH-DATA-002-AC04 | D9 | Core | LR-22 | M3 → M4 | UAT-10, UAT-11, UAT-12, UAT-20 |
| IH-UX-001 | IH-UX-001-AC01 | D2 | Core | LR-10/LR-21 | M2 → M4 | UAT-15 |
| IH-UX-001 | IH-UX-001-AC02 | D2 | Extended | LR-10/LR-21 | M2 → M4 | UAT-15 |
| IH-UX-002 | IH-UX-002-AC01 | D2 | Core | LR-10/LR-21 | M2 → M4 | UAT-15 |
| IH-UX-002 | IH-UX-002-AC02 | A | Extended | LR-10/LR-21 | M2 → M4 | UAT-15 |
| IH-UX-003 | IH-UX-003-AC01 | D6 | Core | LR-10/LR-21 | M2 → M4 | UAT-15 |
| IH-UX-003 | IH-UX-003-AC02 | A | Extended | LR-10/LR-21 | M2 → M4 | UAT-15 |
| IH-UX-004 | IH-UX-004-AC01 | A | Extended | LR-10/LR-21 | M2 → M4 | UAT-07, UAT-09, UAT-14, UAT-15 |
| IH-UX-004 | IH-UX-004-AC02 | A | Core | LR-10/LR-21 | M2 → M4 | UAT-07, UAT-09, UAT-14, UAT-15 |
| IH-MSG-001 | IH-MSG-001-AC01 | A | Extended | LR-15/LR-18 | M3 → M4 | UAT-18 |
| IH-MSG-001 | IH-MSG-001-AC02 | A | Extended | LR-15/LR-18 | M3 → M4 | UAT-18 |
| IH-MSG-002 | IH-MSG-002-AC01 | A | Extended | LR-15/LR-18 | M3 → M4 | UAT-15, UAT-18 |
| IH-MSG-002 | IH-MSG-002-AC02 | A | Extended | LR-15/LR-18 | M3 → M4 | UAT-15, UAT-18 |
| IH-MSG-003 | IH-MSG-003-AC01 | D5 | Core | LR-14/LR-24 | M3 → M4 | UAT-01, UAT-02, UAT-03, UAT-19 |
| IH-MSG-003 | IH-MSG-003-AC02 | A | Core | LR-14/LR-24 | M3 → M4 | UAT-01, UAT-02, UAT-03, UAT-19 |
| IH-MSG-003 | IH-MSG-003-AC03 | A | Extended | LR-14/LR-24 | M3 → M4 | UAT-01, UAT-02, UAT-03, UAT-19 |
| IH-MSG-004 | IH-MSG-004-AC01 | A | Core | LR-15/LR-18 | M3 → M4 | UAT-07, UAT-09, UAT-14, UAT-18 |
| IH-MSG-004 | IH-MSG-004-AC02 | A | Extended | LR-15/LR-18 | M3 → M4 | UAT-07, UAT-09, UAT-14, UAT-18 |
| IH-INT-001 | IH-INT-001-AC01 | D1 | Extended | LR-11/LR-18 | M2.1 → M4 | UAT-16 |
| IH-INT-001 | IH-INT-001-AC02 | A | Extended | LR-11/LR-18 | M2.1 → M4 | UAT-16 |
| IH-INT-002 | IH-INT-002-AC01 | A | Core | LR-11/LR-18 | M2.1 → M4 | UAT-06, UAT-11, UAT-15, UAT-16 |
| IH-INT-002 | IH-INT-002-AC02 | A | Core | LR-11/LR-18 | M2.1 → M4 | UAT-06, UAT-11, UAT-15, UAT-16 |
| IH-INT-002 | IH-INT-002-AC03 | A | Core | LR-11/LR-18 | M2.1 → M4 | UAT-06, UAT-11, UAT-15, UAT-16 |
| IH-INT-003 | IH-INT-003-AC01 | D3 | Core | LR-09/LR-23 | M2.1 → M4 | UAT-01, UAT-02, UAT-03, UAT-11, UAT-16 |
| IH-INT-003 | IH-INT-003-AC02 | A | Core | LR-09/LR-23 | M2.1 → M4 | UAT-01, UAT-02, UAT-03, UAT-11, UAT-16 |
| IH-INT-004 | IH-INT-004-AC01 | A | Extended | LR-11/LR-18 | M2.1 → M4 | UAT-07, UAT-09, UAT-12, UAT-16, UAT-17, UAT-20 |
| IH-INT-004 | IH-INT-004-AC02 | D8 | Core | LR-11/LR-18 | M2.1 → M4 | UAT-07, UAT-09, UAT-12, UAT-16, UAT-17, UAT-20 |
| IH-NFR-001 | IH-NFR-001-AC01 | A | Core | LR-20/LR-24 | M4 | UAT-01, UAT-02, UAT-03, UAT-04 |
| IH-NFR-001 | IH-NFR-001-AC02 | A | Core | LR-20/LR-24 | M4 | UAT-01, UAT-02, UAT-03, UAT-04 |
| IH-NFR-001 | IH-NFR-001-AC03 | A | Core | LR-20/LR-24 | M4 | UAT-01, UAT-02, UAT-03, UAT-04 |
| IH-NFR-001 | IH-NFR-001-AC04 | A | Extended | LR-20/LR-24 | M4 | UAT-01, UAT-02, UAT-03, UAT-04 |
| IH-NFR-001 | IH-NFR-001-AC05 | A | Core | LR-20/LR-24 | M4 | UAT-01, UAT-02, UAT-03, UAT-04 |
| IH-NFR-002 | IH-NFR-002-AC01 | A | Core | LR-20/LR-24 | M4 | UAT-12, UAT-13 |
| IH-NFR-002 | IH-NFR-002-AC02 | A | Core | LR-20/LR-24 | M4 | UAT-12, UAT-13 |
| IH-NFR-003 | IH-NFR-003-AC01 | A | Core | LR-20/LR-24 | M4 | UAT-13, UAT-14 |
| IH-NFR-003 | IH-NFR-003-AC02 | A | Core | LR-20/LR-24 | M4 | UAT-13, UAT-14 |
| IH-NFR-004 | IH-NFR-004-AC01 | A | Core | LR-20/LR-24 | M4 | UAT-07, UAT-12, UAT-16 |
| IH-NFR-004 | IH-NFR-004-AC02 | A | Core | LR-20/LR-24 | M4 | UAT-07, UAT-12, UAT-16 |
| IH-NFR-005 | IH-NFR-005-AC01 | A | Core | LR-20/LR-24 | M4 | UAT-07, UAT-09, UAT-14, UAT-16 |
| IH-NFR-005 | IH-NFR-005-AC02 | A | Core | LR-20/LR-24 | M4 | UAT-07, UAT-09, UAT-14, UAT-16 |
| IH-NFR-006 | IH-NFR-006-AC01 | A | Extended | LR-21 | M4 | UAT-17 |
| IH-NFR-006 | IH-NFR-006-AC02 | A | Extended | LR-21 | M4 | UAT-17 |
| IH-NFR-007 | IH-NFR-007-AC01 | D3 | Core | LR-21/LR-23 | M4 | UAT-17 |
| IH-NFR-007 | IH-NFR-007-AC02 | A | Core | LR-21/LR-23 | M4 | UAT-17 |
| IH-NFR-008 | IH-NFR-008-AC01 | A | Core | LR-20/LR-24 | M4 | UAT-16 |
| IH-NFR-008 | IH-NFR-008-AC02 | A | Core | LR-20/LR-24 | M4 | UAT-16 |
| IH-NFR-009 | IH-NFR-009-AC01 | A | Core | LR-26 | M5 | UAT-16 |
| IH-NFR-009 | IH-NFR-009-AC02 | A | Core | LR-26 | M5 | UAT-16 |
| IH-NFR-010 | IH-NFR-010-AC01 | A | Core | LR-25 | M5 | UAT-16 |
| IH-NFR-010 | IH-NFR-010-AC02 | A | Core | LR-25 | M5 | UAT-16 |
| IH-NFR-011 | IH-NFR-011-AC01 | A | Core | LR-14/LR-24 | M4 | UAT-04, UAT-13, UAT-21 |
| IH-NFR-011 | IH-NFR-011-AC02 | A | Core | LR-14/LR-24 | M4 | UAT-04, UAT-13, UAT-21 |
| IH-REL-001 | IH-REL-001-AC01 | D4 | Core | LR-25 | M5 | UAT-01, UAT-21 |
| IH-REL-001 | IH-REL-001-AC02 | A | Core | LR-25 | M5 | UAT-01, UAT-21 |
| IH-REL-002 | IH-REL-002-AC01 | A | Core | LR-25/LR-26 | M5 | UAT-16 |
| IH-REL-002 | IH-REL-002-AC02 | A | Core | LR-25/LR-26 | M5 | UAT-16 |
| IH-REL-003 | IH-REL-003-AC01 | A | Core | LR-27 | M5 | UAT-16 |
| IH-REL-003 | IH-REL-003-AC02 | A | Core | LR-27 | M5 | UAT-16 |

<a id="evidence"></a>

## 16. Bảng kết quả và mẫu evidence

Dùng các mẫu phù hợp ngay trong hồ sơ đang thực hiện. Một kết quả chỉ lưu ở một nơi và được dẫn lại khi cần; không bắt buộc tạo một file cho mỗi mẫu.

<a id="bang-ket-qua"></a>

### 16.1. Traceability matrix và kết quả theo yêu cầu

Ghi một lần ở đầu bảng: tên và phiên bản SRS được sử dụng, phiên bản bảng phạm vi, môi trường và chế độ kiểm. Ghi rõ thay đổi phiên bản nếu có. Danh mục lấy từ [bảng phạm vi](#pham-vi-truy-vet), gồm 153 AC áp dụng và 12 AC ngoài bài tập.

| AC và yêu cầu thành phần | Phạm vi | Điều kiện hoặc nhánh | Công việc và thiết kế | Test case | Kỳ vọng | Thực tế | Commit đã kiểm | Minh chứng | Kết luận hoặc lỗi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Mã AC, mã thành phần nếu có | Mã A, D1-D6, D8, D9 hoặc N | Trạng thái, biến thể hoặc quy tắc cần kiểm | LR, giao diện, API và dữ liệu liên quan | Mã hoặc tên | Theo yêu cầu và nguồn | Quan sát được | Liên kết commit | Hồ sơ hoặc log | Đạt/chưa đạt/chưa kiểm/bị chặn/ngoài phạm vi |

Mỗi AC có một kết luận tổng hợp. Các điều kiện hoặc yêu cầu thành phần có thể ghi trong ô tương ứng hoặc liên kết tới test case chi tiết của cùng bảng. Không tạo bảng kết luận thứ hai cho cùng phạm vi. Chỉ ghi AC đạt khi mọi điều kiện áp dụng đều đạt; dùng chung test không được làm mất kết luận riêng của từng AC. Điều kiện chưa kiểm, bị chặn hoặc ngoài phạm vi không ghi đạt.

Dùng [`trace/ac-trace.csv`](../../trace/README.md): cột ở bảng trên tương ứng `branches`, `design_ref`, `test_ids`, `expected`, `actual`, `commit`, `evidence`, `verdict`; thêm `risk`, `draft_by`, `verification`, `verified_by` để thể hiện kiểm chứng theo rủi ro. M2.1 ghi yêu cầu và kỳ vọng; M2 nối thiết kế; M3.1-M3 bổ sung kiểm cùng chức năng; M4 tổng hợp kết quả đến hạn; M5 bổ sung kết quả release/restore/CR và cập nhật phần bị ảnh hưởng ở R1.1. Dùng [mẫu minh chứng](#evidence) ngay trong hồ sơ hiện có.

“Đã thiết kế” mô tả mức chuẩn bị test case, không phải verdict AC. Khi chưa chạy, cột thực tế ghi “chưa chạy”, cột kết luận ghi “chưa kiểm”; nếu bị chặn thì ghi nguyên nhân/bước xử lý. Kết quả spike ghi trong hồ sơ LR-09 và dẫn vào quyết định thiết kế; chỉ dùng để kết luận AC sản phẩm khi đã kiểm đúng hành vi, phạm vi và phiên bản ứng dụng cần nghiệm thu. Số assertion hoặc lượt lặp cùng test trên nhiều viewport không phải số AC đạt.

**Ví dụ cách ghi ở M4, không phải kết quả kiểm sẵn:** một nhánh upload đã chạy ghi actual/log/commit và kết luận của nhánh; nếu AC còn nhánh chưa chạy thì verdict AC vẫn chưa đạt đủ. Với `IH-REL-001-AC01` chưa kiểm bản release, ghi kết luận “chưa kiểm”, ghi chú “chưa đến hạn M5”, task LR-25 và bước kiểm dự kiến. Giữ AC này trong 153 AC áp dụng, không chuyển sang ngoài phạm vi. Khi có evidence M5 mới cập nhật verdict; điều kiện phát hành không được giảm.

### 16.2. Nội dung cần ghi theo loại công việc

| Loại | Nội dung |
| --- | --- |
| Spike khả thi | Câu hỏi/giả thuyết, yêu cầu liên quan, phép thử/expected, thời gian dự kiến, actual/evidence và chế độ chạy; kết luận giữ/sửa/thử lại; giới hạn, phần app phải xây, việc còn mở, vai trò hỗ trợ và mốc kiểm tiếp |
| Test/nghiệm thu | Yêu cầu, điều kiện, bước chạy, kỳ vọng/thực tế, môi trường, commit, kết quả và lỗi liên quan |
| Đánh giá AI | Test case/lượt chạy, nguồn và hash/vị trí, ý kỳ vọng, nhà cung cấp thực tế (có fallback hay không), mô hình sinh nội dung, mô hình embedding, phiên bản prompt và schema, kết quả đối chiếu, thời gian/mức sử dụng và người kiểm |
| Lỗi | Bước tái hiện, kỳ vọng/thực tế, tác động, phiên bản lỗi, bản sửa, kết quả kiểm lại và regression |
| Quyết định kiến trúc | Vấn đề, yêu cầu chi phối, các phương án, lựa chọn, đánh đổi, căn cứ và hệ quả |
| Thay đổi sau phát hành | Lý do, hành vi trước/sau, tác động tới yêu cầu/thiết kế/dữ liệu/test, rủi ro, cách quay lại và kết quả kiểm |
| Quyết định với AI | Ngữ cảnh, đề xuất, phép kiểm, phần giữ/sửa/bác bỏ và lý do |
| Review | Sản phẩm/phiên bản, yêu cầu đối chiếu, nhận xét có căn cứ, đề xuất và phản hồi nếu có |

Có thể gộp nội dung cùng loại trong một file; không bắt tạo tài liệu riêng cho mỗi bản ghi. Phân biệt dữ liệu test cố định (fixture) và dịch vụ mô phỏng với dịch vụ thật. Không đưa secret xác thực hay dữ liệu chưa được phép vào hồ sơ.

### 16.3. Phân tích ngữ cảnh và quyết định với AI

| Nội dung | Cách ghi |
| --- | --- |
| Công việc và yêu cầu | Mã LR, AC và điều kiện đang xử lý. |
| Phân tích trước khi dùng AI | Kỳ vọng, ngoại lệ và giả định do học viên tự xác định. |
| Ngữ cảnh cung cấp | Phần SRS, thiết kế, mã nguồn hoặc test cần thiết; lý do chọn. |
| Ngữ cảnh loại bỏ | Secret, dữ liệu chưa được phép hoặc phần không liên quan; lý do không gửi. |
| Đề xuất của AI | Trích phần cần quyết định hoặc dẫn đoạn trao đổi đã loại thông tin nhạy cảm. |
| Quyết định của học viên | Giữ, sửa hoặc bác bỏ; giải thích bằng yêu cầu và evidence. |
| Kiểm độc lập | Đầu vào, kỳ vọng, thực tế, commit, log hoặc nguồn đối chiếu. |

Không cần lưu mọi câu hỏi hoặc toàn bộ hội thoại. Chọn các quyết định đủ để giải thích cách sử dụng AI và kiểm kết quả. Ghi ngắn trong mục AI usage của PR template; số đo ghi vào `docs/ai/delivery-log.csv`.

### 16.4. Quy trình agent và rà soát thay đổi

```text
Công việc, mục tiêu và tiêu chí hoàn thành:
Phạm vi file, quyền thực thi và dữ liệu được phép:
Đầu vào, thiết kế và yêu cầu liên quan:
Kế hoạch, stop condition và checkpoint để khôi phục:
Lệnh hoặc phép kiểm, expected result:
Thao tác thực tế, sự kiện công cụ và kết quả:
Phát hiện: vị trí, tình huống kích hoạt, tác động và căn cứ:
Xử lý, kiểm lại, phần chưa kiểm và quyết định tiếp theo:
```

Mẫu trên có sẵn dạng issue template "Task giao agent" trong `.github/ISSUE_TEMPLATE/`. Rà soát tính đúng, bảo mật, quy ước mã nguồn và thiết kế theo [Review Workflow](../ai/Review_Workflow.md). Không bắt tìm lỗi ở mọi nhóm; kết luận chưa phát hiện vấn đề phải có căn cứ. Khi kiểm giới hạn quyền, ghi phản hồi từ công cụ hoặc môi trường thực thi. Nếu dùng hook, ghi sự kiện kích hoạt và log của hook; lệnh chạy tay chưa chứng minh hook hoạt động.

### 16.5. Liên kết thiết kế với yêu cầu

Mỗi lựa chọn thiết kế cần chỉ ra yêu cầu chi phối, API, dữ liệu và điều kiện phải luôn đúng, cùng cách kiểm. Sử dụng các cột trong traceability matrix và liên kết tới sơ đồ, từ điển dữ liệu hoặc hồ sơ quyết định của LR-11; không tạo một bảng yêu cầu khác.

**Ví dụ minh họa:** lần làm Quiz đã nộp giữ nguyên kết quả. Thiết kế phải nêu nơi kiểm quyền và trạng thái, cách chấm rồi lưu nhất quán, và phản hồi khi nhận lại cùng định danh lần làm. Test case dùng hai lần nộp đồng thời hoặc dữ liệu gửi lại khác; expected result là một lần chấm và trả bản đã lưu. Ví dụ này là căn cứ thiết kế, không phải kết quả kiểm của bài làm.

| Trạng thái giao diện | Yêu cầu | API và dữ liệu được phép trả | Dữ liệu và phiên bản | Thao tác bàn phím | Phép kiểm |
| --- | --- | --- | --- | --- | --- |
| Tên hành trình hoặc trạng thái | Mã IH/AC | Phản hồi thành công, lỗi và quyền | Đối tượng, trạng thái và phiên bản | Thứ tự focus và phím | Kỳ vọng, test case và minh chứng |

Dùng thành phần giao diện tái sử dụng và chú thích cho trạng thái dùng chung. Liên kết Figma phải là file và phiên bản thực có quyền xem; prototype HTML phải nằm trong repository, mở được bằng trình duyệt không cần backend và gắn commit hoặc tag. Khi triển khai khác thiết kế, cập nhật và giải thích.

### 16.6. TDD, characterization test trước refactor và kiểm hành trình

- **TDD:** lưu kỳ vọng độc lập, test thất bại đúng hành vi, thay đổi triển khai, test đạt và kết quả regression theo trình tự thực tế. Kiểm xem assertion trong test có thực sự phát hiện lỗi.
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
Định danh operation, job hoặc kết quả; trạng thái, thời gian, mức sử dụng:
File đầu ra được phép lưu và hash; phần nhạy cảm đã loại bỏ:
Đối chiếu từng dữ kiện hoặc từng câu, lựa chọn, đáp án, giải thích của Quiz:
Kỳ vọng, thực tế, kết luận, lỗi và liên kết kết quả kiểm lại:
```

Cố định nguồn và kỳ vọng trước khi chạy. Ba đến năm ý kỳ vọng không thay kiểm các phát biểu khác xuất hiện trong đầu ra. ID trích dẫn đúng chưa chứng minh nội dung có căn cứ. Giữ lượt thất bại và lượt kiểm lại riêng; hai lượt lặp được chọn trước trong bộ 12 lượt không thay bằng chạy lại sau sửa lỗi. Nếu không có số đo sử dụng, ghi rõ không thu được thay vì điền số giả.

### 16.8. Phát hành, khôi phục và thay đổi

| Hồ sơ | Nội dung cần ghi |
| --- | --- |
| Phát hành R1 bài tập | Tag, commit, checksum, cấu hình, migration, hướng dẫn cài, dữ liệu và kết quả của đúng bản đã kiểm. |
| Sao lưu và khôi phục | Môi trường nguồn và đích cách ly; dữ liệu trước/sau; số lượng, quan hệ, nội dung, phiên bản và quyền; phụ thuộc Auth ngoài cơ sở dữ liệu ứng dụng; lỗi và giới hạn. |
| Thay đổi R1.1 | Tình huống phát sinh sau R1, hành vi trước/sau, tác động tới yêu cầu, API, dữ liệu và test; thay đổi, regression, phương án phục hồi và tag mới. |

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
| Fallback, usage, `finish_reason` | Chuyển sang provider dự phòng khi provider chính lỗi khả dụng sau retry; bản ghi mức sử dụng của một lời gọi model (token, latency, chi phí ước tính); lý do model dừng sinh, ví dụ chạm trần token (IH-AI-005). |
| Scaffold | Phần nền dùng chung Starter cấp sẵn (Auth scaffold, AI Job scaffold, nền UI): có cơ chế, không có nghiệp vụ; không làm AC nào tự đạt. |
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
| Expected result | Request bị từ chối theo API contract đã chọn; không trả dữ liệu của A và không tiết lộ sự tồn tại của Notebook |
| Actual result và trạng thái | Điền sau khi chạy test trên commit xác định; trước khi chạy ghi Pending |

Scenario này còn cần test case cho nhánh được phép, session hết hạn và các thao tác sửa/xóa. Một test case đạt chưa chứng minh toàn bộ scenario hoặc AC đã đạt.
