# Chạy InsightHub Starter

## Yêu cầu

- Docker có Docker Compose v2: Docker Desktop (macOS/Windows) hoặc Docker Engine (Linux, WSL2). Windows xem mục [Windows (WSL2)](#windows-wsl2).
- RAM trống khoảng 3 GiB: tổng `mem_limit` của postgres, api, web là khoảng 2,3 GiB (768 MiB + 1 GiB + 512 MiB), cộng thêm khi build image.
- Cổng 8107 và 3107 trống, hoặc đặt `API_PORT`/`WEB_PORT` khác.
- Git, Python 3.11+ và Make để dùng công cụ kiểm/đóng gói. Browser E2E cần Node 24.20.0 và Playwright trong lockfile; chạy ứng dụng chỉ cần Docker.

## Windows (WSL2)

WSL2 là đường chính thức trên Windows vì Makefile và script cần bash, GNU make và python3. Chạy trực tiếp trên PowerShell/CMD không được hỗ trợ.

1. Cài WSL2 và Ubuntu (PowerShell quyền Admin): `wsl --install -d Ubuntu-24.04`, khởi động lại máy, tạo user Linux. Kiểm `wsl -l -v` hiển thị `VERSION 2`.
2. Chọn một cách chạy Docker:
   - Docker Desktop for Windows, bật `Settings > Resources > WSL integration` cho distro Ubuntu.
   - Docker Engine cài trong Ubuntu WSL theo hướng dẫn Docker cho Ubuntu; bật `systemd=true` trong `/etc/wsl.conf`.

   Kiểm trong terminal Ubuntu: `docker compose version`. Docker Desktop yêu cầu subscription trả phí với doanh nghiệp lớn (theo điều khoản Docker: từ 250 nhân viên hoặc doanh thu từ 10 triệu USD/năm). **Công ty xác nhận license trước khi cài**; nếu chưa có, dùng Docker Engine trong WSL.
3. Cài công cụ trong Ubuntu: `sudo apt update && sudo apt install -y git make python3 python3-venv curl`. Node.js 24.20.0 chỉ cần khi chạy browser E2E trên máy (cài qua nvm hoặc fnm).
4. Clone repository **trong filesystem của WSL** (ví dụ `~/work/insighthub`), không clone vào `/mnt/c/...` vì I/O chậm, lỗi quyền file và file watcher. Mở bằng VS Code extension WSL (`code .` trong thư mục repo).
5. Đặt `git config --global core.autocrlf input`. Repository có `.gitattributes` giữ LF và giữ nguyên byte của SRS, corpus, tài liệu mẫu.
6. Nếu mạng công ty dùng proxy, cấu hình proxy cho Docker, apt và npm; báo mentor trước buổi B1 nếu build image bị chặn.

**Phương án dự phòng: devcontainer.** Khi không cài được công cụ trong WSL, mở repo bằng VS Code Dev Containers (`Reopen in Container`). [`.devcontainer/devcontainer.json`](.devcontainer/devcontainer.json) cung cấp Python 3.12, Node 24.20.0, make và Docker-in-Docker; máy host vẫn cần Docker (Docker Desktop hoặc Docker Engine trong WSL). Cấu hình này chưa được pilot trên máy học viên; ghi lại lỗi gặp phải để mentor xử lý.

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

Bật workflow `.github/workflows/app-ci.yml` trên fork nếu dùng GitHub Actions. Workflow chạy trên push vào `main` và trên pull request, dùng fixture, không cần khóa AI. Workflow `starter-release.yml` dành cho người bảo trì Starter, chỉ chạy thủ công; học viên không cần chạy. Xác nhận kết quả khi workflow thực chạy; không giả định quyền Actions hoặc secret của repository gốc được chuyển sang fork.

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

Ghi SHA mã nguồn và hash tệp mẫu đã dùng trong hồ sơ milestone. Khi chạy lại trên dữ liệu còn tồn tại, cùng byte của tài liệu `Ready` được dedup; cùng byte của tài liệu `Failed` trả `409 document_conflict` theo [API Contract](docs/API_Contract_Starter_v1.md). Đổi `Idempotency-Key` không đổi danh tính nội dung. Với ca kiểm validation cho tệp mới, dùng nội dung thử riêng; với ca dedup/retry, giữ nguyên nội dung để kiểm đúng hành vi. Không xóa volume hoặc nới expected result để làm test đạt.

Nếu giảng viên cung cấp revision Starter mới, giữ commit nền cũ, review diff trước khi tích hợp vào fork và kiểm lại phần bị ảnh hưởng. Không reset mất bài làm; evidence của lần chạy trước vẫn thuộc SHA/corpus trước đó.

## Email local với Mailpit (tùy chọn)

Starter cấp hạ tầng tối thiểu cho phần Auth/Email của bài làm: mail catcher Mailpit (Compose profile `mail`) và adapter SMTP [`api/app/core/mailer.py`](api/app/core/mailer.py). Starter **không** có luồng xác minh email hoặc reset mật khẩu; học viên tự thiết kế và kiểm các luồng này theo Requirements.

```sh
make COMPOSE="docker compose --env-file .env -p insighthub-c07-starter" mail-up
```

- SMTP: `127.0.0.1:1025` từ máy; `mailpit:1025` từ container API (mặc định của `SMTP_HOST`/`SMTP_PORT`).
- Giao diện xem thư: http://127.0.0.1:8025
- Đổi cổng khi bị chiếm: `MAIL_SMTP_PORT`, `MAIL_UI_PORT`. Đổi người gửi: `MAIL_FROM`.

Mailpit giữ thư trong máy, không gửi ra Internet. Chỉ dùng địa chỉ email test; không dùng email hoặc dữ liệu thật của công ty. Dừng bằng `make ... mail-down`.

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

## Backup và restore

```sh
COMPOSE_PROJECT_NAME=insighthub-c07-starter ENV_FILE=.env make backup-restore-check
```

Backup drill yêu cầu corpus có dữ liệu, một chat thành công và một failed attempt; xem lệnh seed riêng và cách thêm bảng mới của bài làm vào drill trong [Runbook](docs/Runbook_Starter_v1.md#backup-và-restore-drill).

Đóng gói và phát hành gói Starter (`make package`, `make verify-package`, `make test-release`) là việc của người bảo trì, xem [Release Starter](docs/maintainer/Release_Starter.md). Học viên và coding agent không chạy các lệnh này.

## Dừng

```sh
docker compose --env-file .env -p insighthub-c07-starter down
```

Lệnh trên giữ volume. Chỉ dùng `down -v` với namespace test có thể hủy và sau khi đã kiểm đúng project.
