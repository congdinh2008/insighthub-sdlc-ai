# AI Engineering Kit của InsightHub

Kit là phần repository ghi lại **cách dự án làm việc với AI**: quy tắc, ngữ cảnh, quyền, skill, hook, subagent, quy trình review, spec, đánh giá và số đo. Mỗi milestone thêm hoặc hoàn thiện một thành phần trong output của LR hiện có; không tạo bài nộp riêng. Đến Capstone, học viên trình bày Kit như một tài sản có thể mang sang dự án thật (với công cụ và dữ liệu được Samsung SDS phê duyệt).

## Bản đồ theo milestone

| Kit | Artifact | Milestone / LR | Starter cấp | Học viên hoàn thành |
| --- | --- | --- | --- | --- |
| K1 Repository instructions | `AGENTS.md`, `CLAUDE.md` | M0.1 LR-03; M2 LR-11; M3.1 LR-13 | Bản nền | M0.1: biến lỗi AI ở LR-03 thành rule có cách kiểm. M2: glossary, invariant. M3.1: rule test-as-spec |
| K2 Context pack | `docs/ai/context-pack.md` | M0.1 LR-02 | [Template](templates/context-pack.md) | Nguồn/phiên bản, invariant, phần loại bỏ; một lượt A/B có token |
| K3 Charter và quyền | `docs/ai/AI_Usage_Charter.md`, `.claude/settings.json` | M0.2 LR-04 | [Template](templates/AI_Usage_Charter.md), `settings.json` | Phân loại dữ liệu, quyền, cách dừng/khôi phục, pháp lý Việt Nam |
| K4 Skills | `.claude/skills/<tên>/SKILL.md` | M0.2 LR-05; M2.1 LR-08 | [Template](templates/SKILL.template.md) | Skill workflow (M0.2); skill `ac-drafter` viết nháp bảng trace (M2.1) |
| K5 Hooks | `.claude/hooks/`, `.claude/approved-tests.txt` | M0.2 demo; M3.1 LR-13; M3 LR-19; M4 LR-26 | `block_secrets.py`, `protect_approved_tests.py` | Thêm test đã duyệt vào danh sách; hook tự động hóa ở LR-19; hook hoặc rule `deny` chặn lệnh phá dữ liệu ở LR-26; log tại `reports/hooks/events.jsonl` |
| K6 Subagent | `.claude/agents/design-reviewer.md` | M2 LR-11; M4 LR-24 | [Template](templates/subagent.template.md) | Reviewer chỉ có tool đọc; finding được xác minh |
| K7 Review pipeline | PR template, [Review Workflow](Review_Workflow.md) | M1 LR-07 trở đi | `.github/pull_request_template.md`, issue templates | `/code-review --comment`, `/security-review`, triage finding |
| K8 Spec chain | `specs/quiz/{spec,plan,tasks}.md` | M2.1 spec; M2 plan, tasks; M3 task brief | [`specs/_template`](../../specs/_template/spec.md) | Bắt buộc cho Quiz; tính năng khác dùng lại nếu muốn |
| K9 Eval harness | `evaluation/harness/`, `make eval` | M3 LR-19 (hỏi đáp); M4 LR-23 | Skeleton golden set, grader, pass^k, `ChatAdapter` | Golden set hỏi đáp 4 case chạy k = 2 (M3); case và grader cho Summary/Quiz, adapter gọi API bài làm (M4) |
| K10 AI Delivery Log | `docs/ai/delivery-log.csv` | Từ M1, mỗi PR một dòng; Capstone LR-29 | Header CSV, `scripts/delivery_report.py` | Ghi số đo thật; báo cáo baseline KPI |
| K11 AI-BOM | `docs/ai/ai-bom.json` | M4 LR-24 | `scripts/generate_ai_bom.py`, `scripts/generate_sbom.py` | Sinh tự động trong CI cùng SBOM, bổ sung phần script không tự biết |
| K12 MCP chỉ đọc | `tools/mcp/insighthub_db_readonly.py`, `.mcp.json.example` | M0.2 LR-05 | Role `insighthub_readonly`, server MCP, `make mcp-role`, `make mcp-check` | Ba lượt evidence: truy vấn hợp lệ, lỗi tool, lệnh ghi bị database từ chối |
| K13 Trace sampling | `trace/sampling-log.csv` | M2.1 LR-08; M4 LR-20 | `scripts/trace_sample.py`, `scripts/trace_check.py` | Lấy mẫu có seed trên AC Core, chấm OK/Error, tính tỉ lệ lỗi |
| K14 CI cho AI | `.github/workflows/app-ci.yml` (bước `eval-fixture`) | M1 LR-07 kiểm; M4 LR-23 bắt buộc | Bước báo cáo `continue-on-error` | Bỏ `continue-on-error`, chạy suite Summary/Quiz với `--min-pass-hat-k` |
| K15 Test plan và E2E | `docs/release/Test_Plan.md`, `web/e2e/`, `web/playwright.config.ts` | M3 LR-19; M4 LR-20, LR-21 | [Test Plan Template](../release/Test_Plan_Template.md), spec mẫu, `npm run test:pw`, bước CI | Test plan có exit criteria, test report có NotRun, E2E hành trình M3.1 (planner, generator; healer không sửa test đã duyệt), mutation trên code tự viết |
| K16 Release và vận hành | `docs/release/Release_Checklist_Template.md`, `Release_Notes_Template.md`, `Operations_Template.md` | M4 LR-25, LR-26; M5 LR-27 | Template checklist, ghi chú phát hành, hồ sơ vận hành | Go/no-go có ký, điền theo đúng tag và commit phát hành; SLI, SLO, incident, postmortem |
| K17 Bảo trì với agent | Module map, PR refactor của agent, checklist review migration | M5 LR-27 | [Module legacy](../Legacy_Modules.md), [checklist review migration và CI](templates/Review_Checklist_Migration_CI.md) | Agent chỉ đọc lập module map, refactor trong worktree, review PR 4 lớp |

Truy vết yêu cầu (`trace/ac-trace.csv`) có cột nguồn gốc bản nháp và người kiểm; xem [trace/README](../../trace/README.md).

## Mức AI và cột `agent_mode`

Delivery Log ghi mức tự chủ giao cho AI ở cột `agent_mode`. Chọn mức theo hậu quả khi sai và khả năng rollback, không theo năng lực agent.

| Mức AI | Cách dùng | Giá trị `agent_mode` |
| --- | --- | --- |
| 1 | Trợ lý hội thoại viết nháp từ thông tin được đưa vào | `chat` |
| 2 | Agent đọc repo và đề xuất ở plan mode, không sửa file | `plan` |
| 3 | Agent sửa file, chạy lệnh trong quyền và thư mục được giới hạn | `edit` |
| 4 | Agent chạy trong CI hoặc nền, không theo dõi từng bước | `auto` |

## Quy tắc chung

- Kit phục vụ dự án InsightHub cụ thể. Quy tắc chung chung không gắn repo, lệnh hoặc cách kiểm không được tính.
- Hướng dẫn phải có cơ chế thực thi khi có thể: quyền `deny`, hook, CI check, test. Chỉ viết lời nhắc cho model là chưa đủ.
- Không đưa `.env`, API key, token, dữ liệu Samsung SDS hoặc khách hàng vào Kit, log hay transcript.
- Số đo trong Delivery Log là số thật. Nếu không đo được, để trống và ghi lý do; không điền ước đoán.
