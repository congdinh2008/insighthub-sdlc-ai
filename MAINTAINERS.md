# InsightHub: repository nguồn

File này chỉ có ở repository nguồn `insighthub-sdlc-ai`, không xuất bản sang Starter học viên.

## Vai trò repository

| Repository | Vai trò | Hiển thị |
| --- | --- | --- |
| `insighthub-sdlc-ai` (repository này) | Nguồn sự thật của Running Project InsightHub: code, tài liệu học viên, công cụ người bảo trì | Public trong giai đoạn review, sau đó Private |
| [`insighthub-starter`](https://github.com/congdinh2008/insighthub-starter) | Bản phát hành cho học viên, sinh từ repository này. Học viên fork repository đó | Public |
| `insighthub-sdlc-ai-solution` | Bài làm tham chiếu của mentor | Private |

Cây file của repository này bằng Starter cộng các file người bảo trì liệt kê trong [`scripts/maintainer/publish-exclude.txt`](scripts/maintainer/publish-exclude.txt). Kiểm bằng:

```sh
make -f maintainer.mk compare-starter STARTER=https://github.com/congdinh2008/insighthub-starter.git
```

## Góp ý review

| Phạm vi | Đọc |
| --- | --- |
| Đề bài, milestone, rubric | [Requirements học viên](docs/learner/01_Requirements_InsightHub.md), [SRS v1.1](docs/learner/02_SRS_InsightHub_v1.1.md) |
| Kiến trúc và hợp đồng | [Architecture](docs/Architecture_Starter_v1.md), [API Contract](docs/API_Contract_Starter_v1.md), [ADR](docs/adr/) |
| Scaffold cho học viên | [Auth](docs/Auth_Integration_Guide.md), [AI Job Framework](docs/AI_Job_Framework.md), [UI Foundation](docs/UI_Foundation.md) |
| Làm việc với AI | [`AGENTS.md`](AGENTS.md), [`CLAUDE.md`](CLAUDE.md), [AI Engineering Kit](docs/ai/README.md) |
| Phát hành | [Release Starter](docs/maintainer/Release_Starter.md) |

Gửi góp ý bằng issue, ghi file và dòng hoặc mục cụ thể. Không gửi PR sửa trực tiếp Starter. Không đưa dữ liệu thật, `.env`, API key vào issue.

## Lưu ý

- Ứng dụng chạy ở chế độ fixture mặc định, không cần khóa AI. Cài đặt theo [Getting Started](GETTING_STARTED.md).
- Lịch sử Git trước ngày 28/09/2026 có tài liệu soạn thảo đã thay thế (`docs/archive/`, SRS v2.4). Bản hiện hành là các file trong cây hiện tại.
