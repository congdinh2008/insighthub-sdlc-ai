# API Contract InsightHub Starter v1

## Quy ước chung

- Mutation upload, retry, delete và chat yêu cầu header `Idempotency-Key`, dài 1-128 ký tự.
- Cùng key/cùng payload trả lại response đã lưu. Cùng key/khác payload trả `409 idempotency_conflict`.
- Response lỗi có `detail`, `code`; header có `X-Request-ID`.
- UI/API local chưa có Auth. Học viên phải thêm ownership server-side trước khi dùng đa người dùng.
- Dedup theo bytes chỉ trả 201 khi tài liệu đã `ready`. Tài liệu trùng đang pending trả 409 `operation_in_progress`; failed trả 409 `document_conflict`, kèm `document_id` để retry đúng tài liệu.
- Operation lưu `deadline_at`; truy vấn reconciliation phục hồi operation quá hạn thành failed ngay khi tiến trình còn chạy. SQL/lock/pool wait và commit đều chịu ngân sách còn lại.
- Replay chat sau khi nguồn bị xóa giữ câu trả lời lịch sử, nhưng citation có `available: false`, `excerpt: null`, contexts không còn nội dung nguồn và response có `historical_sources_unavailable: true`.
- Browser giữ metadata operation key trong sessionStorage trước POST, tiếp tục poll qua reload và không POST lại khi chưa biết kết quả. Không lưu prompt/file/credential vào kho này.

## Endpoints

| Method | Path | Kết quả chính |
| --- | --- | --- |
| `POST` | `/documents` | Multipart một file; HTTP 201 sau khi `Ready`; lỗi ingestion trả `document_id` và `operation_id` |
| `GET` | `/documents` | Danh sách trạng thái bền vững |
| `GET` | `/documents/{id}` | Metadata và ingestion attempt history |
| `GET` | `/documents/{id}/source` | Toàn văn hoặc `segment_id` cụ thể |
| `POST` | `/documents/{id}/retry` | Multipart đúng file của document failed; tạo attempt mới |
| `DELETE` | `/documents/{id}` | HTTP 204; idempotent; xóa source, segments và chunks theo cascade |
| `POST` | `/chat` | `question`, `document_ids` tùy chọn, `top_k` tùy chọn |
| `GET` | `/operations/{type}/{key}` | Đối soát trạng thái/kết quả sau khi client mất response |
| `GET` | `/system/profile` | Profile/model/retrieval/disclosure hiện hành, không có credential |
| `GET` | `/healthz`, `/readyz`, `/metrics` | Liveness, readiness và metrics |

## Chat response

```json
{
  "status": "Answered",
  "answer": "...",
  "claims": [
    {"text": "...", "citation_ids": ["chunk:42"]}
  ],
  "citations": [
    {
      "citation_id": "chunk:42",
      "document_id": 7,
      "source_segment_id": 11,
      "source": "example.pdf",
      "locator": {"type": "page", "value": "3"},
      "excerpt": "..."
    }
  ],
  "sources": ["example.pdf"],
  "contexts": [
    {"context_id": "chunk:42", "source": "example.pdf", "similarity": 0.81, "rerank_score": 0.94}
  ],
  "mode": "real",
  "provider": "deepseek",
  "model": "deepseek-flash",
  "prompt_version": "rag-claims-v2",
  "profile": "classroom-deepseek-gemini-local-reranker",
  "retrieval": {"reranker_provider": "local", "reranker_model": "...", "context_count": 1},
  "usage": {"input_tokens": 10, "output_tokens": 8, "source": "provider"},
  "latency_ms": 1234
}
```

`NoEvidence` trả HTTP 200, `answer: null`, `claims: []`, `citations: []`. Evidence gate có thể trả kết quả này mà không gọi LLM. Provider error, deadline hoặc citation invalid là lỗi kỹ thuật, không chuyển thành `NoEvidence`.

Mặc định `contexts` chỉ chứa provenance và score, không trả raw chunk text. Chỉ bật `EXPOSE_DEBUG_CONTEXTS=true` trong môi trường debug được kiểm soát.
