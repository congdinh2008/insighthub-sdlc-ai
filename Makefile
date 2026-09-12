COMPOSE ?= docker compose
PYTHON ?= python3
API_URL ?= http://127.0.0.1:8107
WEB_URL ?= http://127.0.0.1:3107

.PHONY: up down build test test-backend test-web smoke
up:
	$(COMPOSE) up --build -d --wait

down:
	$(COMPOSE) --profile ollama --profile checks down

build:
	$(COMPOSE) build api web

test-backend:
	$(COMPOSE) run --rm --no-deps -e RUN_DB_TESTS=1 -e TEST_SCHEMA_PATH=/tmp/init.sql -v "$(CURDIR)/infra/db/init.sql:/tmp/init.sql:ro" api python -m unittest discover -s tests -v

test-web:
	$(COMPOSE) build web-check
	$(COMPOSE) --profile checks run --rm --no-deps web-check

test: test-backend test-web

smoke:
	$(PYTHON) scripts/smoke.py --api-url "$(API_URL)" --web-url "$(WEB_URL)"
