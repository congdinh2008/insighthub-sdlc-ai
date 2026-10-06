# Phát hành Starter (dành cho người bảo trì)

Tài liệu chỉ có ở repository nguồn `insighthub-sdlc-ai`, không xuất bản sang `insighthub-starter`.

## Mô hình repository

| Repository | Vai trò | Hiển thị | Ghi |
| --- | --- | --- | --- |
| `insighthub-sdlc-ai` (Source) | Nguồn sự thật: code, tài liệu học viên, công cụ người bảo trì | Private | Người bảo trì, qua PR vào `main` |
| `insighthub-starter` (Starter) | Bản phát hành cho học viên. Học viên fork repository này | Public | Chỉ nhận commit xuất bản từ Source |
| `insighthub-sdlc-ai-solution` (Solution) | Bài làm tham chiếu theo milestone, `upstream` là Starter | Private | Mentor |

**Nguyên tắc:**

- Mọi thay đổi Starter và tài liệu học viên làm ở Source. Không sửa trực tiếp trên Starter.
- Mỗi revision Starter là một commit `Starter learner-rX.Y` ghi SHA nguồn. Học viên nhận bằng `git fetch upstream` rồi merge (Requirements mục 2.9).
- Tag `learner-r*` đã công bố cho học viên thì không dời. Hotfix phát hành thành `learner-rX.Y.Z`.
- Lỗi phát hiện khi diễn tập trên Solution được sửa ở Source rồi phát hành lại, không đẩy từ Solution sang Starter.

## File chỉ có ở Source

Danh sách đầy đủ: [`scripts/maintainer/publish-exclude.txt`](../../scripts/maintainer/publish-exclude.txt).

| File | Việc |
| --- | --- |
| `scripts/maintainer/publish_starter.sh` | Xuất bản một ref của Source sang nhánh `release/<revision>` của Starter |
| `scripts/maintainer/build_trace_skeleton.py` | Sinh lại `trace/ac-trace.csv` từ Requirements mục 15.4 |
| `scripts/package_starter.py`, `scripts/verify_package.py`, `scripts/tests/test_delivery.py` | Đóng gói ZIP có manifest và kiểm gói |
| `maintainer.mk` | Target `test-release`, `package`, `verify-package`, `trace-skeleton`, `publish-starter`. Gọi bằng `make -f maintainer.mk <target>`, file này nạp lại `Makefile` |
| `.github/workflows/starter-release.yml` | Release gate chạy thủ công trên Source |

Khi thêm công cụ người bảo trì mới, thêm đường dẫn vào `publish-exclude.txt`. Script xuất bản dừng nếu bản xuất bản còn tham chiếu tới `docs/maintainer`, `scripts/maintainer`, `maintainer.mk`, `package_starter`, `verify_package`, `starter-release.yml` hoặc `test-release`.

## Quy trình phát hành một revision

| Bước | Nơi làm | Việc |
| --- | --- | --- |
| 1 | Source | Nhánh `feat/*` hoặc `docs/*`, PR vào `main`. Khi Requirements mục 15.4 đổi, chạy `make -f maintainer.mk trace-skeleton` |
| 2 | Source | Release gate: `check_project.py`, `trace_check.py`, `make test`, `make -f maintainer.mk test-release`, smoke, E2E, restore drill, `make sbom` |
| 3 | Source | Tag nguồn `src-rX.Y` trên commit đã qua gate |
| 4 | Source | `make -f maintainer.mk publish-starter REF=src-rX.Y STARTER=../insighthub-starter REVISION=learner-rX.Y` |
| 5 | Starter | Trên `release/learner-rX.Y`: `make test`, smoke, E2E như bước 2 |
| 6 | Starter | `git merge --ff-only release/learner-rX.Y` vào `main`, tag annotated `learner-rX.Y`, push `main` và tag |
| 7 | Solution | `git fetch upstream --tags`, merge `learner-rX.Y` vào `main`, chạy lại test |
| 8 | Lớp | Công bố tag và tóm tắt thay đổi theo Requirements mục 2.9 |

Lệnh mẫu:

```sh
make -f maintainer.mk trace-skeleton CHECK=1
python3 scripts/check_project.py
make test && make -f maintainer.mk test-release
git tag -a src-r1.4 -m "Source for learner-r1.4"
make -f maintainer.mk publish-starter REF=src-r1.4 STARTER=../insighthub-starter REVISION=learner-r1.4
```

`publish_starter.sh` dùng `git worktree` tạm nên không đổi working tree hiện tại của Starter. Script không push và không tạo tag.

## Gói ZIP (tùy chọn)

Khi cần gửi Starter dạng file thay vì repository:

```sh
make -f maintainer.mk package
make -f maintainer.mk verify-package
```

`package` chỉ chạy trên working tree sạch. Tên gói chứa phiên bản runtime và revision tài liệu. Manifest định danh đúng commit và bộ Requirements, SRS đi kèm.

## Lưu ý khi đổi tài liệu học viên

- Đổi SRS phải cập nhật `sha256` trong `API_Schema_Reference/Manifest_Reference.json` của ZIP API/Schema, nếu không `check_project.py` báo `Reference SRS hash drift`.
- `.gitattributes` giữ SRS, `evaluation/corpus/` và `sample-docs/` ở dạng byte-exact (`-text`) để hash không đổi trên Windows.
- Tài liệu học viên nằm tại `docs/learner/`. Đổi vị trí phải cập nhật `starter.manifest.json` (`requirements_baseline`, `learner_requirements`, `api_schema_reference`, `documentation_revision`).
- Tầng Core/Extended lấy từ cột Tầng của Requirements mục 15.4. Mức rủi ro gợi ý giữ theo `trace/ac-trace.csv` hiện có. AC mới phải truyền `--risk <AC>=R1|R2|R3` cho `build_trace_skeleton.py`.
