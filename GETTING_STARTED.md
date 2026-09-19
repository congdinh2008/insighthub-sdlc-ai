# Chạy InsightHub Starter

## Yêu cầu

- Docker Desktop có Docker Compose v2.
- RAM trống tối thiểu khoảng 2 GiB.
- Cổng 8107 và 3107 trống, hoặc đặt `API_PORT`/`WEB_PORT` khác.

## Khởi động offline fixture

```sh
cp .env.example .env
docker compose --env-file .env -p insighthub-c07-starter up --build -d --wait
```

- Web: http://localhost:3107
- API docs: http://localhost:8107/docs
- Readiness: http://localhost:8107/readyz

Upload riêng từng file trong `sample-docs/`. Fixture trả trích đoạn có nhãn để kiểm flow. Nó không chứng minh câu trả lời AI có chất lượng.

## Kiểm tra

```sh
make COMPOSE="docker compose --env-file .env.example -p insighthub-c07-check" test
make API_URL=http://127.0.0.1:8107 WEB_URL=http://127.0.0.1:3107 smoke
git diff --check
```

Backend integration tests tạo PostgreSQL schema ngẫu nhiên và tự xóa. Smoke test chỉ xóa document do chính lần chạy tạo.

## Migration dữ liệu cũ

API tự chạy migration forward-only trong `api/migrations/` khi startup. Có thể chạy riêng:

```sh
make COMPOSE="docker compose --env-file .env -p insighthub-c07-starter" migrate
```

Không xóa volume để xử lý schema mismatch. Sao lưu trước khi thay embedding dimension hoặc identity; vector cũ không được diễn giải bằng model mới.

## Provider thật

Chọn một profile mẫu:

```sh
# Setup ít nhất, không reranker
cp .env.classroom-gemini.example .env

# Hoặc Gemini + local reranker
make reranker-local-up
cp .env.classroom-gemini-local-reranker.example .env

# Hoặc Gemini + Cohere reranker
cp .env.classroom-gemini-cohere.example .env
```

Điền khóa vào `.env`, không sửa file `.example` và không commit credential. Sau khi start, kiểm profile:

```sh
curl -fsS http://127.0.0.1:8107/system/profile
python3 scripts/run_aev.py --api-url http://127.0.0.1:8107
```

Provider lỗi không fallback sang fixture. Dùng index riêng khi đổi embedding identity. Bật hoặc tắt reranker không đổi embedding identity nhưng vẫn phải chạy lại AEV. Chi tiết tại [Model Profiles và Reranking](docs/Model_Profiles_And_Reranking.md).

## Backup và package

```sh
COMPOSE_PROJECT_NAME=insighthub-c07-starter ENV_FILE=.env make backup-restore-check
make package
make verify-package
```

Đọc [Runbook](docs/Runbook_Starter_v1.md) trước khi giữ dữ liệu lớp học.

## Dừng

```sh
docker compose --env-file .env -p insighthub-c07-starter down
```

Lệnh trên giữ volume. Chỉ dùng `down -v` với namespace test có thể hủy và sau khi đã kiểm đúng project.
