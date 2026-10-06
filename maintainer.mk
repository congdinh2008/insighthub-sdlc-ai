# Maintainer only. File này không được xuất bản sang insighthub-starter (scripts/maintainer/publish-exclude.txt).
# Dùng: make -f maintainer.mk <target>. Mọi target của Makefile vẫn dùng được qua file này.
include Makefile

.PHONY: test-release package verify-package publish-starter trace-skeleton

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
