# Model Profiles và Reranking

## Quyết định mặc định

Baseline lớp học là `gemini-embedding-2` và `gemini-3.1-flash-lite`, không reranker. Cấu hình này ít thành phần, dễ debug và đủ để học viên hiểu retrieval trước khi tối ưu. Google hiện công bố Free Tier cho cả hai model; Free Tier có giới hạn và dữ liệu có thể được dùng để cải thiện sản phẩm, vì vậy UI luôn hiển thị disclosure. Reranker là option, không phải dependency bắt buộc.

Nguồn kiểm chứng: [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing), [Gemini embeddings](https://ai.google.dev/gemini-api/docs/embeddings) và [Gemini billing tiers](https://ai.google.dev/gemini-api/docs/billing).

| Profile | Embedding | Generation | Reranker | Candidate chunks gửi ra ngoài |
| --- | --- | --- | --- | --- |
| `fixture-offline` | Fixture | Fixture | Không | Không |
| `classroom-gemini` | Gemini | Gemini | Không | Chỉ Gemini nhận dữ liệu cần xử lý |
| `classroom-gemini-local-reranker` | Gemini | Gemini | TEI local | Không gửi tới dịch vụ rerank |
| `classroom-gemini-cohere` | Gemini | Gemini | Cohere | Có, gửi query và candidate chunks tới Cohere |

Fixture chỉ kiểm tra luồng kỹ thuật. Nó không dùng để kết luận chất lượng semantic.

## Tắt reranker

```env
RERANKER_PROVIDER=none
RETRIEVAL_CANDIDATE_K=20
RETRIEVAL_TOP_K=5
```

Dense retrieval lọc theo `RETRIEVAL_MIN_SIMILARITY`, giới hạn số chunk trên mỗi tài liệu và context token budget trước khi đưa vào LLM.

## Reranker local

Starter dùng Text Embeddings Inference với model multilingual:

```sh
make reranker-local-up
cp .env.classroom-gemini-local-reranker.example .env
# Điền GEMINI_API_KEY, sau đó chạy application stack
docker compose --env-file .env -p insighthub-c07-starter up --build -d --wait
```

TEI tải model ở lần chạy đầu. Cần thêm disk, RAM và thời gian download. Image CPU được chọn theo kiến trúc `arm64` hoặc `x86_64`. Endpoint local chỉ được phép trỏ tới `localhost`, `127.0.0.1`, `host.docker.internal` hoặc service `reranker` để tránh biến cấu hình thành HTTP proxy tùy ý. Model và schema top-level array của `/rerank` được đối chiếu với [TEI README](https://github.com/huggingface/text-embeddings-inference) và [TEI OpenAPI](https://huggingface.github.io/text-embeddings-inference/openapi.json).

```sh
make reranker-local-down
```

## Reranker Cohere

```sh
cp .env.classroom-gemini-cohere.example .env
# Điền GEMINI_API_KEY và COHERE_API_KEY
docker compose --env-file .env -p insighthub-c07-starter up --build -d --wait
```

Cohere chỉ là provider rerank. Profile chọn `rerank-v4.0-fast`, biến thể multilingual tối ưu low latency và throughput. Trial API key hiện được Cohere công bố là miễn phí; production key tính phí theo search, nên đây là option để học và benchmark thay vì dependency bắt buộc. Xem [Cohere Rerank models](https://docs.cohere.com/docs/rerank), [Rerank v2 API](https://docs.cohere.com/reference/rerank) và [Cohere pricing](https://cohere.com/pricing).

Embedding identity không thay đổi khi bật hoặc tắt reranker, nên không cần re-index nếu embedding provider, model, dimension, endpoint và revision giữ nguyên. Tuy vậy phải chạy lại AEV vì ranking và context đưa vào LLM đã thay đổi.

## Tuning có kiểm soát

1. Giữ corpus và bộ câu hỏi AEV cố định.
2. Chạy baseline không reranker.
3. Chỉ thay một nhóm biến: threshold, candidate K hoặc reranker.
4. So sánh answer correctness, citation/source scope, NoEvidence, injection, p95 latency và chi phí.
5. Ghi profile, model, corpus hash và report vào hồ sơ release.

Các biến chính:

| Biến | Vai trò | Baseline |
| --- | --- | --- |
| `RETRIEVAL_CANDIDATE_K` | Số candidate lấy từ pgvector | 20 |
| `RETRIEVAL_MIN_SIMILARITY` | Evidence gate trước generation | 0.20 với profile Gemini mẫu |
| `RERANKER_TOP_N` | Số kết quả giữ sau rerank | 5 |
| `RETRIEVAL_MAX_CHUNKS_PER_DOCUMENT` | Giảm việc một tài liệu chiếm toàn bộ context | 3 |
| `CONTEXT_MAX_TOKENS` | Ngân sách context ước lượng | 4000 |

Không hạ evidence threshold chỉ để tăng tỷ lệ Answered. `NoEvidence` đúng là kết quả cần thiết của một hệ thống RAG an toàn.

## Failure behavior

- Provider bị timeout, rate limit, lỗi transport hoặc trả response sai contract sẽ tạo lỗi kỹ thuật có mã chuẩn hóa.
- Không tự fallback từ provider thật sang fixture hoặc từ reranker sang dense-only.
- Retry có giới hạn và luôn nằm trong deadline tổng của operation.
- UI có runtime disclosure để học viên biết provider/model nào đang nhận dữ liệu.
