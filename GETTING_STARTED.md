# Chạy InsightHub Starter

## Yêu cầu

- Docker Desktop có Docker Compose v2.
- RAM trống tối thiểu khoảng 2 GiB.
- Cổng 8107 và 3107 trống, hoặc đặt `API_PORT`/`WEB_PORT` khác.
- Git, Python 3.11+ và Make để dùng công cụ kiểm/đóng gói. Browser E2E cần Node 24.20.0 và Playwright trong lockfile; chạy ứng dụng chỉ cần Docker.

## Nếu nhận ZIP

Giải nén vào một thư mục riêng, kiểm SHA-256 bên cạnh ZIP trước khi chạy. Gói có SRS tại `requirements/`, không cần kho học liệu của instructor.

```sh
git init -b main
git add .
git commit -m "Initialize InsightHub starter"
```

Git cần `user.name` và `user.email` của chính học viên. Lưu `PACKAGE_MANIFEST.json` làm biên nhận nguồn; file này được ignore và không đưa vào nguồn của gói xây lại. `.env` cũng được ignore. Đọc [Learning Contract](docs/learner/00_START_LEARNING.md) và PRE B1-B2 trước khi phát triển.

Đẩy repository riêng lên dịch vụ Git của lớp và bật workflow `.github/workflows/starter.yml` nếu dùng GitHub Actions. Workflow mặc định chạy fixture và không cần secret AI. Kết quả CI trên nền tảng của lớp chỉ được xác nhận sau khi workflow thực sự chạy ở đó.

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

Sửa ngay file `.env` đã tạo, không copy thêm profile:

```env
RAG_MODE=real
DEEPSEEK_API_KEY=<key DeepSeek>
GEMINI_API_KEY=<key Gemini>
```

Đây là ba biến cần cấu hình. DeepSeek trả lời bằng `deepseek-flash`; Gemini tạo embedding bằng `gemini-embedding-2`, 1024 chiều. Không cần key OpenAI, Anthropic, Voyage hoặc Cohere cho cấu hình này. Reranker mặc định tắt.

Điền khóa vào `.env` tại máy, không sửa file `.example`, gửi key trong chat hoặc commit credential. Nếu chuyển từ env cũ, bỏ các dòng `LLM_PROVIDER`, `EMBEDDING_PROVIDER`, `LLM_MODEL`, `EMBEDDING_MODEL`, `RAG_PROFILE`, `AI_DATA_USAGE_NOTICE` và `AI_DATA_POLICY_URL` để dùng mặc định mới. Thay model khi cần bằng hai biến được chú thích trong `.env.example`.

Áp dụng lại cấu hình và kiểm profile:

```sh
API_PORT=8117 WEB_PORT=3117 docker compose --env-file .env -p insighthub-c07-real up --build -d --wait
curl -fsS http://127.0.0.1:8117/system/profile
python3 scripts/run_aev.py --api-url http://127.0.0.1:8117
```

Profile đúng là `classroom-deepseek-gemini`, generation `deepseek`, embedding `gemini`, reranker `none`. Thiếu key sẽ báo lỗi khi khởi động; provider lỗi không fallback sang fixture. Kiểm thử real AEV gửi bộ tài liệu mẫu và câu hỏi tới hai provider.

Ví dụ trên giữ fixture ở 8107/3107 và real ở 8117/3117 với volume riêng. Upload lại tài liệu gốc vào real runtime; không dùng vector fixture cho real. Chỉ đổi model hỏi đáp không làm thay đổi embedding identity. Chi tiết về reranker và tuning tại [Model Profiles và Reranking](docs/Model_Profiles_And_Reranking.md).

## Backup và package

```sh
COMPOSE_PROJECT_NAME=insighthub-c07-starter ENV_FILE=.env make backup-restore-check
python3 scripts/check_project.py
make sbom
git add .
git commit -m "Prepare reviewed starter release"
make package
make verify-package
```

Backup drill yêu cầu corpus có dữ liệu, một chat thành công và một failed attempt; xem lệnh seed riêng trong [Runbook](docs/Runbook_Starter_v1.md). `make package` chỉ chạy trên working tree sạch, có SRS và SBOM khớp version. Nếu không có thay đổi để commit, bỏ qua lệnh commit; không tạo commit rỗng.

## Dừng

```sh
docker compose --env-file .env -p insighthub-c07-starter down
```

Lệnh trên giữ volume. Chỉ dùng `down -v` với namespace test có thể hủy và sau khi đã kiểm đúng project.
