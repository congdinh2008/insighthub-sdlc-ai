# Runbook InsightHub Starter v1

## Preflight

```sh
docker version
docker compose version
git status --short
```

Không dùng cùng Compose project name cho lớp học và test. Không dùng `down -v` với namespace có dữ liệu cần giữ.

## Start và kiểm tra

```sh
docker compose --env-file .env -p insighthub-c07-starter up --build -d --wait
curl -fsS http://127.0.0.1:8107/readyz
curl -fsS http://127.0.0.1:8107/system/profile
python3 scripts/smoke.py --api-url http://127.0.0.1:8107 --web-url http://127.0.0.1:3107
```

`/system/profile` phải khớp file `.env` đang dùng. Endpoint này không trả credential.

## Regression

```sh
make COMPOSE="docker compose --env-file .env.example -p insighthub-c07-check" test
git diff --check
```

Fixture regression không gọi dịch vụ AI bên ngoài.

## AEV với provider thật

```sh
python3 scripts/run_aev.py --api-url http://127.0.0.1:8107
```

Runner upload corpus riêng, chạy `evaluation/AEV-01.json`, kiểm Answered/NoEvidence, source scope, claim citation và prompt injection, rồi xóa đúng các tài liệu nó vừa tạo. Report được ghi vào `reports/evaluation/` và không chứa API key.

## Backup và restore drill

```sh
COMPOSE_PROJECT_NAME=insighthub-c07-starter ENV_FILE=.env make backup-restore-check
```

Script từ chối database rỗng. Nó hash mọi giá trị của tám bảng, gồm bytes gốc, segments, vectors, attempts và operations; so sánh trước/restore/sau để phát hiện thay đổi đồng thời. API trên database restore phải đọc đúng toàn văn/locator, đối soát chat và retrieve đúng phạm vi. Database tạm và dump tự xóa sau drill; report hash được giữ trong `reports/backup-restore/`.

Tạo corpus fixture cho drill trong namespace test riêng:

```sh
API_PORT=8127 WEB_PORT=3127 docker compose --env-file .env.example -p insighthub-c07-recovery up --build -d --wait
python3 scripts/seed_recovery_fixture.py --api-url http://127.0.0.1:8127
python3 scripts/backup_restore_check.py --project insighthub-c07-recovery --env-file .env.example
docker compose --env-file .env.example -p insighthub-c07-recovery down
```

Dừng mutation trong khi kiểm hash. Seed gồm TXT/MD/PDF, một failed attempt và chat, không dùng dữ liệu người thật. Cần giữ dump để diễn tập thủ công thì thêm `--keep-backup`: quyền file 600, thư mục riêng 700, chỉ instructor truy cập, không commit/gửi cùng starter. Đề xuất giữ tối đa 7 ngày trong sandbox rồi xóa sau khi đã kiểm restore; dữ liệu lớp thật áp dụng policy lớp đã xác nhận. Không dùng backup fixture làm bằng chứng semantic của real embedding.

Backup production cần thêm retention, encryption, off-host storage, quyền truy cập và restore drill định kỳ. Starter chỉ cung cấp baseline có thể kiểm chứng tại local.

## Sự cố thường gặp

| Hiện tượng | Kiểm tra | Xử lý |
| --- | --- | --- |
| `/readyz` trả 503 | `docker compose logs api postgres` | Kiểm DB, migration và embedding identity |
| Upload 409 | Operation key hoặc file SHA-256 đã tồn tại | Đối soát operation, không đổi key để che lỗi |
| Chat `NoEvidence` | Threshold, source selection, corpus | Kiểm citation candidates và chạy AEV |
| Provider 429/502/504 | Log theo `X-Request-ID` | Chờ retry bounded, kiểm quota và policy |
| Local reranker không kết nối | `docker compose -f infra/reranker/docker-compose.yml ps` | Kiểm TEI health, model download và port 8187 |
| Index identity conflict | `/readyz`, config embedding | Dùng index/volume riêng hoặc migration có chủ đích |

## Stop

```sh
docker compose --env-file .env -p insighthub-c07-starter down
```

Lệnh này giữ volume. Chỉ xóa volume của namespace test khi đã kiểm đúng project name.
