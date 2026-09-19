# Model Profiles và Reranking

Cập nhật: 19/09/2026. DeepSeek cho hỏi đáp theo lựa chọn của instructor; embedding giữ Gemini. Chất lượng AI cần được kiểm chứng AEV trên corpus sử dụng.

## Một file `.env`

Tạo `.env` từ `.env.example` một lần. Chỉ ba biến cần cấu hình để chạy AI thật:

```env
RAG_MODE=real
DEEPSEEK_API_KEY=<key DeepSeek>
GEMINI_API_KEY=<key Gemini>
```

`RAG_MODE=fixture` chạy hoàn toàn offline, kể cả khi đã điền key. `RAG_MODE=real` mặc định chọn DeepSeek cho generation, Gemini cho embedding và tắt reranker. Thiếu key sẽ dừng startup, không tự chuyển sang fixture.

| Cấu hình | Mặc định trong code | Biến override nếu cần |
| --- | --- | --- |
| Chat model | `deepseek-flash` | `DEEPSEEK_CHAT_MODEL` |
| DeepSeek endpoint | `https://api.deepseek.com` | `DEEPSEEK_BASE_URL` |
| Embedding model | `gemini-embedding-2` | `GEMINI_EMBEDDING_MODEL` |
| Embedding dimension | 1024 | `EMBEDDING_DIM` |
| Reranker | Tắt | `RERANKER_PROVIDER` |
| Cổng API/Web | 8107 / 3107 | `API_PORT` / `WEB_PORT` |

Adapter DeepSeek dùng `/chat/completions`, JSON output, `max_tokens` và tắt thinking cho luồng trả lời ngắn có nguồn. Chỉ nhận completion kết thúc bằng `stop`; output rỗng, bị cắt, sai JSON hoặc citation không hợp lệ bị từ chối. Không đưa reasoning content vào câu trả lời. Endpoint, model và tham số được đối chiếu với [DeepSeek API](https://api-docs.deepseek.com/) và [Chat Completion](https://api-docs.deepseek.com/api/create-chat-completion/) ngày 19/09/2026. Chọn model mặc định chưa phải kết quả đánh giá chất lượng hoặc chi phí.

Các giới hạn và tham số tuning nằm trong [Settings](../api/app/core/config.py); không phải điền lại trong `.env`. Compose chuyển biến override vào API, giá trị rỗng dùng mặc định của Settings. Biến đặt trong shell có thể ghi đè giá trị ở env file theo cơ chế Compose, nên kiểm `/system/profile` sau mỗi lần áp dụng cấu hình.

## Dữ liệu và profile thực thi

| Profile tự sinh | Embedding | Generation | Reranker |
| --- | --- | --- | --- |
| `fixture-offline` | Fixture | Fixture | Không |
| `classroom-deepseek-gemini` | Gemini | DeepSeek | Không |
| `classroom-deepseek-gemini-local-reranker` | Gemini | DeepSeek | TEI local |
| `classroom-deepseek-gemini-cohere` | Gemini | DeepSeek | Cohere |

Nội dung tài liệu và câu hỏi dùng tạo embedding được gửi tới Gemini. Câu hỏi và các đoạn nguồn được chọn được gửi tới DeepSeek để trả lời. Khi bật Cohere, câu hỏi và candidate chunks còn được gửi tới Cohere để rerank. UI hiển thị thông tin này qua runtime profile. Chỉ dùng dữ liệu thực hành được phép gửi tới các provider đã chọn.

Các adapter Gemini generation, OpenAI-compatible, Anthropic, Voyage và Ollama vẫn được giữ cho bài học mở rộng. Chúng không yêu cầu key khi không được chọn. Muốn sử dụng, khai báo tường minh `LLM_PROVIDER`/`EMBEDDING_PROVIDER` cùng key, model và endpoint tương ứng; profile tự sinh là `custom` khi ngoài cấu hình lớp. `LLM_MODEL` và `EMBEDDING_MODEL` là override chung có ưu tiên cao hơn model riêng từng provider, chỉ dùng khi có chủ đích.

## Reranker tùy chọn

Chỉ bật sau khi đo baseline. Không có file env riêng; thêm biến vào chính `.env` hiện tại.

**Local TEI:**

```env
RERANKER_PROVIDER=local
LOCAL_RERANKER_URL=http://host.docker.internal:8187
```

```sh
make reranker-local-up
docker compose --env-file .env -p insighthub-c07-starter up --build -d --wait
```

TEI dùng `Alibaba-NLP/gte-multilingual-reranker-base`, tải model ở lần chạy đầu. Cần thêm disk, RAM và thời gian download. Script chọn image CPU theo kiến trúc máy. Endpoint local bị giới hạn vào `localhost`, `127.0.0.1`, `host.docker.internal` hoặc service `reranker`. Dừng TEI bằng `make reranker-local-down`.

**Cohere:**

```env
RERANKER_PROVIDER=cohere
COHERE_API_KEY=<key Cohere>
```

Áp dụng lại Compose. Adapter dùng model mặc định `rerank-v4.0-fast`; `COHERE_RERANKER_MODEL` chỉ cần đặt khi đổi model. Key Cohere không cần cho cấu hình mặc định.

Bật/tắt reranker hoặc đổi chat model không đổi embedding identity. Thay embedding provider, model, dimension, endpoint hoặc revision cần ingest lại tài liệu trong không gian vector tương ứng. Không xóa volume để né kiểm tra identity.

## Kiểm chứng và tuning

1. Chạy fixture để kiểm setup và regression.
2. Điền hai key, đổi `RAG_MODE=real`, áp dụng lại Compose và kiểm `/system/profile`.
3. Chạy `python3 scripts/run_aev.py --api-url http://127.0.0.1:8107` trên corpus mẫu.
4. Đọc câu trả lời và đoạn nguồn của từng claim, kiểm `NoEvidence`, injection, citation, latency và token. Runner tự động không thay thế review grounding.
5. Chỉ thay một nhóm biến mỗi lần, ghi model, corpus hash, prompt version và kết quả đánh giá.

| Biến tuning | Vai trò | Mặc định |
| --- | --- | --- |
| `RETRIEVAL_CANDIDATE_K` | Số candidate lấy từ pgvector | 20 |
| `RETRIEVAL_TOP_K` | Số chunk tối đa đưa vào context | 5 |
| `RETRIEVAL_MIN_SIMILARITY` | Evidence gate trước generation | 0,20 với Gemini embedding real; -1 với fixture |
| `RERANKER_TOP_N` | Số kết quả giữ sau rerank | 5 |
| `RETRIEVAL_MAX_CHUNKS_PER_DOCUMENT` | Giới hạn chunk trên một tài liệu | 3 |
| `CONTEXT_MAX_TOKENS` | Ngân sách context ước lượng | 4000 |

Threshold 0,20 chưa được hiệu chỉnh bằng real AEV của lớp. Không hạ threshold chỉ để tăng tỷ lệ `Answered`. Provider lỗi, timeout hoặc response sai contract là lỗi kỹ thuật; không fallback sang fixture hoặc tự tắt reranker. Fixture không chứng minh chất lượng semantic.
