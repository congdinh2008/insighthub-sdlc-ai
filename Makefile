COMPOSE ?= docker compose
PYTHON ?= python3
API_URL ?= http://127.0.0.1:8107
WEB_URL ?= http://127.0.0.1:3107

.PHONY: up down build test test-db test-backend test-web smoke migrate sbom package verify-package aev backup-restore-check reranker-local-up reranker-local-down
up:
	$(COMPOSE) up --build -d --wait

down:
	$(COMPOSE) --profile ollama --profile checks down

build:
	$(COMPOSE) build api web

test-db:
	$(COMPOSE) up -d --wait postgres

test-backend: test-db
	$(COMPOSE) build api
	$(COMPOSE) run --rm --no-deps -e RUN_DB_TESTS=1 -e TEST_SCHEMA_PATH=/tmp/init.sql -v "$(CURDIR)/infra/db/init.sql:/tmp/init.sql:ro" api python -m unittest discover -s tests -v

test-web:
	$(COMPOSE) build web-check
	$(COMPOSE) --profile checks run --rm --no-deps web-check

test: test-backend test-web

smoke:
	$(PYTHON) scripts/smoke.py --api-url "$(API_URL)" --web-url "$(WEB_URL)"

migrate:
	$(COMPOSE) run --rm api python -c "from app.core.db import initialize_database,close_pool; initialize_database(); close_pool()"

sbom:
	$(PYTHON) scripts/generate_sbom.py

package: sbom
	$(PYTHON) scripts/package_starter.py

verify-package:
	$(PYTHON) scripts/verify_package.py

aev:
	$(PYTHON) scripts/run_aev.py --api-url "$(API_URL)"

backup-restore-check:
	$(PYTHON) scripts/backup_restore_check.py --project "$${COMPOSE_PROJECT_NAME:?Set COMPOSE_PROJECT_NAME}" --env-file "$${ENV_FILE:-.env.example}"

reranker-local-up:
	TEI_IMAGE=$$(if [ "$$(uname -m)" = "arm64" ] || [ "$$(uname -m)" = "aarch64" ]; then echo ghcr.io/huggingface/text-embeddings-inference:cpu-arm64-1.9; else echo ghcr.io/huggingface/text-embeddings-inference:cpu-1.9; fi) docker compose -f infra/reranker/docker-compose.yml up -d

reranker-local-down:
	docker compose -f infra/reranker/docker-compose.yml down
