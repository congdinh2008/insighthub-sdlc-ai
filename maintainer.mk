# Maintainer only. File này không được xuất bản sang insighthub-starter (scripts/maintainer/publish-exclude.txt).
# Dùng: make -f maintainer.mk <target>. Mọi target của Makefile vẫn dùng được qua file này.
include Makefile

.PHONY: test-release package verify-package publish-starter trace-skeleton compare-starter link-starter

# Delivery/package regression.
test-release:
	STARTER_RELEASE_CHECKS=1 $(PYTHON) -m unittest discover -s scripts/tests -v

package: sbom
	$(PYTHON) scripts/package_starter.py

verify-package:
	$(PYTHON) scripts/verify_package.py

# Sinh lại trace/ac-trace.csv khi Requirements mục 15.4 đổi. CHECK=1 chỉ so sánh.
trace-skeleton:
	$(PYTHON) scripts/maintainer/build_trace_skeleton.py $(if $(CHECK),--check,)

# Xuất bản một ref của Source sang nhánh release của Starter (không push).
# Ví dụ: make -f maintainer.mk publish-starter REF=src-r1.3 STARTER=../insighthub-starter REVISION=learner-r1.3
publish-starter:
	bash scripts/maintainer/publish_starter.sh "$${REF:?Set REF}" "$${STARTER:?Set STARTER}" "$${REVISION:?Set REVISION}"

# So cây file với Starter: chỉ được khác ở file người bảo trì. Chạy trước và sau mỗi lần xuất bản.
# Ví dụ: make -f maintainer.mk compare-starter STARTER=../insighthub-starter STARTER_REF=learner-r1.3.1
compare-starter:
	bash scripts/maintainer/compare_starter.sh "$${STARTER:?Set STARTER}" "$${STARTER_REF:-main}" "$${REF:-HEAD}"

# Nối lịch sử sau khi đã push tag Starter: commit Starter thành tổ tiên của Source, cây file Source không đổi.
# Ví dụ: make -f maintainer.mk link-starter STARTER=../insighthub-starter TAG=learner-r1.3.1
link-starter:
	git fetch --no-tags "$${STARTER:?Set STARTER}" "refs/tags/$${TAG:?Set TAG}:refs/tags/$${TAG}"
	git merge -s ours --no-ff -m "chore(release): link Starter $${TAG} history" "$${TAG}^{commit}"
