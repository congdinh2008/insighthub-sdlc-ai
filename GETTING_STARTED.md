# Chạy InsightHub Starter

## Yêu cầu

- Docker Desktop có Docker Compose v2.
- RAM trống tối thiểu khoảng 2 GiB.
- Cổng 8107 và 3107 trống, hoặc đặt `API_PORT`/`WEB_PORT` khác.
- Git, Python 3.11+ và Make để dùng công cụ kiểm/đóng gói. Browser E2E cần Node 24.20.0 và Playwright trong lockfile; chạy ứng dụng chỉ cần Docker.

## Fork starter và khởi tạo bài làm

Học viên C07 bắt buộc fork repository starter theo URL và phiên bản giảng viên công bố. Trên dịch vụ Git, tạo fork cá nhân hoặc trong không gian lớp được cấp, sau đó thay các giá trị ví dụ dưới đây bằng URL thực:

```sh
git clone 'URL_FORK_CA_NHAN' insighthub
cd insighthub
git remote add upstream 'URL_REPOSITORY_STARTER'
git remote -v
git rev-parse HEAD
git switch -c milestone/m0.1
```

`origin` phải trỏ tới fork cá nhân, `upstream` trỏ tới starter. Ghi commit nền và nguồn starter vào hồ sơ dự án; giữ nguyên lịch sử Git. Thiết lập `user.name` và `user.email` của học viên. Cách commit, tạo PR trong repository cá nhân, gửi bài cho giảng viên và thời hạn tại [Requirements](docs/learner_v1.0_20260923/01_Requirements_InsightHub.md).

Bật workflow `.github/workflows/starter.yml` trên fork nếu dùng GitHub Actions. Workflow mặc định dùng fixture, không cần khóa AI. Xác nhận kết quả khi workflow thực chạy; không giả định quyền Actions hoặc secret của repository gốc được chuyển sang fork.

## Khi nhận thêm gói ZIP

ZIP dùng để đối chiếu hoặc kiểm cài đặt sạch, không thay repository fork nộp bài. Giải nén vào thư mục riêng và kiểm SHA-256 trước khi chạy; không ghi đè bản fork đang phát triển. Nếu chưa có quyền fork, báo giảng viên cấp quyền và tiếp tục kiểm setup trên ZIP, ghi rõ phụ thuộc chưa hoàn tất. Không tạo lịch sử Git mới để giả lập nguồn starter.

[SRS của bài tập](docs/learner_v1.0_20260923/02_SRS_InsightHub_v1.0.md) và hợp đồng tham khảo nằm trong bộ tài liệu học viên. `PACKAGE_MANIFEST.json`, khi có trong gói Starter, là biên nhận của đúng gói mã nguồn đó; không thay bảng phạm vi hoặc kết quả kiểm của bài làm. Không đưa `.env` thật vào Git hoặc artifact. Đọc [Hướng dẫn bắt đầu](docs/learner_v1.0_20260923/01_Requirements_InsightHub.md) trước khi phát triển.

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
git commit -m "chore(release): prepare reviewed delivery package"
make package
make verify-package
```

Backup drill yêu cầu corpus có dữ liệu, một chat thành công và một failed attempt; xem lệnh seed riêng trong [Runbook](docs/Runbook_Starter_v1.md). `make package` chỉ chạy trên working tree sạch, có SRS và SBOM khớp version. Tên gói chứa cả phiên bản runtime và revision tài liệu, ví dụ `insighthub-starter-v1.0.0-rc.3-docs20260923.zip`; manifest định danh đúng commit và bộ Requirements/SRS đi kèm. Tài liệu trong `docs/archive/` không đưa vào gói học viên. Nếu không có thay đổi để commit, bỏ qua lệnh commit; không tạo commit rỗng.

## Dừng

```sh
docker compose --env-file .env -p insighthub-c07-starter down
```

Lệnh trên giữ volume. Chỉ dùng `down -v` với namespace test có thể hủy và sau khi đã kiểm đúng project.
