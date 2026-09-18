COMPOSE ?= docker compose
PYTHON ?= python3
API_URL ?= http://127.0.0.1:8107
WEB_URL ?= http://127.0.0.1:3107

.PHONY: up down build test test-db test-backend test-web smoke migrate package verify-package
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

package:
	$(PYTHON) scripts/package_starter.py

verify-package:
	$(PYTHON) scripts/verify_package.py
