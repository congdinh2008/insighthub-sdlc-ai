# START HERE - InsightHub Starter

Mục tiêu của gói này là cung cấp một RAG baseline chạy được, kiểm thử được và đủ điểm mở rộng cho Running Project. Học viên không cần tự dựng lại ingestion, vector index, retrieval, citation, idempotency hoặc provider abstraction từ đầu.

## Chọn profile

| Nhu cầu | File bắt đầu | Reranker |
| --- | --- | --- |
| Học flow và chạy test không cần API key | `.env.example` | Tắt |
| Chi phí thấp, setup ít | `.env.classroom-gemini.example` | Tắt |
| Chất lượng retrieval cao hơn, không gửi candidate chunks tới dịch vụ rerank | `.env.classroom-gemini-local-reranker.example` | Local TEI |
| Setup nhẹ trên máy học viên, chấp nhận provider thứ ba | `.env.classroom-gemini-cohere.example` | Cohere |

Khuyến nghị lớp học bắt đầu bằng Gemini không reranker. Chỉ bật reranker sau khi AEV cho thấy retrieval baseline chưa đạt. Mọi profile thật phải chạy lại AEV-01 trước khi dùng làm baseline lớp.

## Chạy lần đầu

```sh
cp .env.example .env
docker compose --env-file .env -p insighthub-c07-starter up --build -d --wait
python3 scripts/smoke.py --api-url http://127.0.0.1:8107 --web-url http://127.0.0.1:3107
```

- Web: http://localhost:3107
- API docs: http://localhost:8107/docs
- Runtime profile: http://localhost:8107/system/profile

Đọc tiếp [GETTING_STARTED.md](GETTING_STARTED.md), [Model Profiles and Reranking](docs/Model_Profiles_And_Reranking.md) và [Runbook](docs/Runbook_Starter_v1.md).

## Ranh giới starter

Starter đã có vertical slice RAG thực tế từ upload tới grounded answer. Auth, Notebook, ownership, lưu hội thoại, AI Tools và product quota là phần học viên triển khai theo SRS 2.4. Không đưa dữ liệu thật hoặc dữ liệu nhạy cảm vào Free Tier khi chưa có policy phù hợp.
