# Phát hành gói Starter (dành cho người bảo trì)

Tài liệu này dành cho người bảo trì Starter (giảng viên, Academic Owner). **Học viên và coding agent của học viên không chạy các bước dưới đây.** Bài làm của học viên dùng [App CI](../../.github/workflows/app-ci.yml) và các lệnh trong [Getting Started](../../GETTING_STARTED.md).

## Khi nào dùng

- Chuẩn bị một revision Starter mới để phát cho lớp.
- Cập nhật bộ tài liệu học viên (Requirements, SRS, ZIP API/Schema) hoặc version runtime.

## Gate phát hành

| Bước | Lệnh | Kiểm gì |
| --- | --- | --- |
| 1 | `python3 scripts/check_project.py` | Version đồng bộ (manifest, web, lockfile, SBOM, API, README, Readiness); hash SRS khớp manifest trong ZIP API/Schema; 73 yêu cầu/165 AC (153 áp dụng, 12 ngoài phạm vi) được mapping; link Markdown nội bộ hợp lệ |
| 2 | `make test` và `make test-release` | Test ứng dụng; `test-release` bật thêm delivery regression (`STARTER_RELEASE_CHECKS=1`) |
| 3 | `make smoke`, `make test-e2e`, `make test-pw` | Smoke, E2E cũ và Playwright Test trên fixture |
| 4 | `python3 scripts/seed_recovery_fixture.py --api-url http://127.0.0.1:8107` rồi `COMPOSE_PROJECT_NAME=insighthub-c07-starter ENV_FILE=.env make backup-restore-check` | Restore drill trên corpus có dữ liệu, một chat thành công và một failed attempt |
| 5 | `make sbom` | Sinh lại SBOM |
| 6 | Commit thay đổi đã review | `make package` chỉ chạy trên working tree sạch |
| 7 | `make package` rồi `make verify-package` | Đóng gói ZIP có manifest; kiểm path, file bắt buộc, secret, hash từng file và checksum |

Trình tự lệnh:

```sh
python3 scripts/check_project.py
make test && make test-release
COMPOSE_PROJECT_NAME=insighthub-c07-starter ENV_FILE=.env make backup-restore-check
make sbom
git add <các file đã review>
git commit -m "chore(release): prepare reviewed delivery package"
make package
make verify-package
```

Nếu không có thay đổi để commit, bỏ qua lệnh commit; không tạo commit rỗng. Tên gói chứa phiên bản runtime và revision tài liệu, ví dụ `insighthub-starter-v1.0.0-rc.3-docs20260927.zip`; manifest định danh đúng commit và bộ Requirements/SRS đi kèm. Tài liệu lưu trữ cũ không nằm trong repo học viên; `package_starter.py` và `verify_package.py` vẫn loại mọi đường dẫn `archive`.

Trên GitHub, chạy workflow [Starter release gate](../../.github/workflows/starter-release.yml) bằng `workflow_dispatch` trên repository gốc. Workflow này không tự chạy trên fork của học viên.

## Phát hành repository học viên

Không cho học viên fork repository tác giả: lịch sử Git còn tài liệu đã loại (ví dụ `docs/archive`). Repository học viên là `insighthub-starter`, có lịch sử riêng bắt đầu từ snapshot `learner-r1.0`.

**Lần đầu (learner-r1.0):** tạo repository học viên từ snapshot một commit đã qua gate. `scripts/maintainer/` chỉ có trong repository tác giả, không nằm trong repository học viên:

```sh
python3 scripts/maintainer/build_trace_skeleton.py      # khi Requirements đổi bảng AC, tier hoặc mức rủi ro
python3 scripts/trace_check.py
bash scripts/maintainer/make_learner_snapshot.sh <commit-hoặc-tag> ../insighthub-learner learner-r1.0
cd ../insighthub-learner
git remote add origin <URL repository học viên>
git push -u origin main --tags
```

Script dùng `git archive` (chỉ file đã track), bỏ `scripts/maintainer/`, `dist/`, `docs/archive`, kiểm không có `.env` hoặc chuỗi giống API key, tạo một commit và tag. Công bố URL và tag cho lớp; học viên fork repository này.

**Revision tiếp theo (learner-r1.1 trở đi):** làm trên nhánh `release/learner-rX.Y` tách từ `main` của `insighthub-starter`, chạy gate, review rồi fast-forward `main` và gắn tag annotated. Không tạo lại snapshot vì học viên đã fork và cần `git fetch upstream` để nhận diff:

```sh
cd insighthub-starter
git fetch <nguồn nhánh release> release/learner-r1.3:release/learner-r1.3
git checkout main && git merge --ff-only release/learner-r1.3
python3 scripts/check_project.py && python3 scripts/trace_check.py
git push origin main
git tag -a learner-r1.3 -m "Starter learner-r1.3: Requirements 1.5"
git push origin learner-r1.3
```

Khi tầng Core/Extended đổi ở repository học viên, đồng bộ lại bản đồ trong `scripts/maintainer/build_trace_skeleton.py` của repository tác giả để lần sinh skeleton sau không ghi đè tầng mới.

## Lưu ý khi đổi tài liệu học viên

- Đổi SRS phải cập nhật `sha256` trong `API_Schema_Reference/Manifest_Reference.json` của ZIP API/Schema, nếu không `check_project.py` báo `Reference SRS hash drift`.
- `.gitattributes` giữ SRS, `evaluation/corpus/` và `sample-docs/` ở dạng byte-exact (`-text`) để hash không đổi trên Windows.
- Tài liệu học viên nằm tại `docs/learner/` (không gắn version vào tên thư mục). Đổi vị trí phải cập nhật `starter.manifest.json` (`requirements_baseline`, `learner_requirements`, `api_schema_reference`, `documentation_revision`).
- Đổi mức rủi ro gợi ý hoặc danh sách Core/Extended: sửa bản đồ trong `scripts/maintainer/build_trace_skeleton.py` và cột Tầng ở Requirements mục 15.4 (script dừng nếu hai nơi lệch), chạy lại script và công bố cho lớp trước milestone liên quan.
- Giữ nhãn version cho tới khi Academic Owner quyết định baseline lớp.
