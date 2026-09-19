# START HERE - InsightHub Starter

Mục tiêu của gói này là cung cấp một RAG baseline chạy được, kiểm thử được và đủ điểm mở rộng cho Running Project. Học viên không cần tự dựng lại ingestion, vector index, retrieval, citation, idempotency hoặc provider abstraction từ đầu.

## Một file cấu hình

Chỉ tạo `.env` từ `.env.example` một lần. Không có file env riêng cho từng provider hoặc reranker.

| Nhu cầu | Cấu hình trong `.env` | Reranker |
| --- | --- | --- |
| Học flow và chạy test không cần API key | `RAG_MODE=fixture` | Tắt |
| Hỏi đáp DeepSeek, embedding Gemini | `RAG_MODE=real` và hai key `DEEPSEEK_API_KEY`, `GEMINI_API_KEY` | Tắt |

Cấu hình hỏi đáp theo lựa chọn của instructor: DeepSeek. Chỉ bật reranker sau khi AEV cho thấy retrieval baseline chưa đạt. Mọi profile thật phải chạy AEV-01 trước khi dùng làm baseline lớp.

## Chạy lần đầu

```sh
cp .env.example .env
docker compose --env-file .env -p insighthub-c07-starter up --build -d --wait
python3 scripts/smoke.py --api-url http://127.0.0.1:8107 --web-url http://127.0.0.1:3107
```

- Web: http://localhost:3107
- API docs: http://localhost:8107/docs
- Runtime profile: http://localhost:8107/system/profile

Nếu nhận ZIP, khởi tạo Git theo [GETTING_STARTED.md](GETTING_STARTED.md) trước. Đọc [Learning Contract/PRE](docs/learner/00_START_LEARNING.md), [Model Profiles and Reranking](docs/Model_Profiles_And_Reranking.md) và [Runbook](docs/Runbook_Starter_v1.md).

## Ranh giới starter

Starter đã có luồng RAG từ upload tới câu trả lời có nguồn. Fixture kiểm chứng luồng kỹ thuật; chất lượng AI thật cần AEV. Auth, Notebook, ownership, lưu hội thoại, AI Tools và product quota là phần học viên triển khai theo SRS 2.4. Dùng bộ tài liệu thực hành được phép gửi tới provider.
