# API Contract InsightHub Starter v1

## Quy ước chung

- Mutation upload, retry và chat yêu cầu header `Idempotency-Key`, dài 1-128 ký tự.
- Cùng key/cùng payload trả lại response đã lưu. Cùng key/khác payload trả `409 idempotency_conflict`.
- Response lỗi có `detail`, `code`; header có `X-Request-ID`.
- UI/API local chưa có Auth. Học viên phải thêm ownership server-side trước khi dùng đa người dùng.

## Endpoints

| Method | Path | Kết quả chính |
| --- | --- | --- |
| `POST` | `/documents` | Multipart một file; HTTP 201 sau khi `Ready`; lỗi ingestion trả `document_id` và `operation_id` |
| `GET` | `/documents` | Danh sách trạng thái bền vững |
| `GET` | `/documents/{id}` | Metadata và ingestion attempt history |
| `GET` | `/documents/{id}/source` | Toàn văn hoặc `segment_id` cụ thể |
| `POST` | `/documents/{id}/retry` | Multipart đúng file của document failed; tạo attempt mới |
| `DELETE` | `/documents/{id}` | HTTP 204; xóa source, segments và chunks theo cascade |
| `POST` | `/chat` | `question`, `document_ids` tùy chọn, `top_k` tùy chọn |
| `GET` | `/operations/{type}/{key}` | Đối soát trạng thái/kết quả sau khi client mất response |
| `GET` | `/healthz`, `/readyz`, `/metrics` | Liveness, readiness và metrics |

## Chat response

```json
{
  "status": "Answered",
  "answer": "...",
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
  "contexts": [],
  "mode": "real",
  "provider": "openai",
  "model": "...",
  "usage": {"input_tokens": 10, "output_tokens": 8, "source": "provider"},
  "latency_ms": 1234
}
```

`NoEvidence` trả HTTP 200, `answer: null`, `citations: []`. Provider error, deadline hoặc citation invalid là lỗi kỹ thuật, không chuyển thành `NoEvidence`.
