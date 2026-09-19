"""InsightHub synchronous starter API."""

import logging
import json
import time
import uuid
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, Response
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest
from starlette.concurrency import run_in_threadpool

from app.core.config import get_settings
from app.core.db import close_pool, get_conn, initialize_database
from app.core.errors import ServiceError
from app.core.metrics import documents_total, http_requests_total
from app.core.upload_limit import UploadLimitMiddleware
from app.routers import chat, documents, health, operations, system

settings = get_settings()
logging.basicConfig(level=settings.log_level)
request_logger = logging.getLogger("insighthub.requests")
# SDK/transport debugging can expose URLs and headers. Keep it out of lab logs.
for name in ("httpx", "httpcore", "pypdf", "psycopg.pool"):
    logging.getLogger(name).setLevel(logging.CRITICAL)


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await run_in_threadpool(initialize_database)
        yield
    finally:
        await run_in_threadpool(close_pool)


app = FastAPI(title=settings.app_name, version="1.0.0-rc.2", lifespan=lifespan)
app.add_middleware(UploadLimitMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(ServiceError)
async def service_error_handler(request: Request, exc: ServiceError):
    return JSONResponse(
        {"detail": exc.message, "code": exc.code, "request_id": getattr(request.state, "request_id", None)},
        status_code=exc.status_code,
    )


@app.exception_handler(RequestValidationError)
async def validation_error_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        {"detail": "Dữ liệu yêu cầu không hợp lệ.", "code": "validation_error", "request_id": getattr(request.state, "request_id", None)},
        status_code=422,
    )


@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    request.state.request_id = request.headers.get("X-Request-ID") or str(uuid.uuid4())
    started = time.perf_counter()
    status = 500
    try:
        origin = request.headers.get("origin")
        if (request.method in {"POST", "PUT", "PATCH", "DELETE"}
                and origin is not None and origin not in settings.cors_origins):
            status = 403
            return JSONResponse(
                {"detail": "Origin không được phép.", "code": "origin_not_allowed", "request_id": request.state.request_id},
                403,
                headers={"X-Request-ID": request.state.request_id},
            )
        response = await call_next(request)
        status = response.status_code
        response.headers["X-Request-ID"] = request.state.request_id
        return response
    except Exception:
        # Never expose uncaught driver/provider exception text to clients.
        return JSONResponse(
            {"detail": "Không thể xử lý yêu cầu.", "code": "internal_error", "request_id": request.state.request_id},
            500,
            headers={"X-Request-ID": request.state.request_id},
        )
    finally:
        route = request.scope.get("route")
        endpoint = getattr(route, "path", "__unmatched__")
        method = (
            request.method
            if request.method
            in {
                "GET",
                "POST",
                "PUT",
                "PATCH",
                "DELETE",
                "HEAD",
                "OPTIONS",
                "TRACE",
                "CONNECT",
            }
            else "OTHER"
        )
        http_requests_total.labels(method, endpoint, str(status)).inc()
        request_logger.info(json.dumps({
            "event": "http_request",
            "request_id": request.state.request_id,
            "method": method,
            "endpoint": endpoint,
            "status": status,
            "duration_ms": int((time.perf_counter() - started) * 1000),
            "rag_mode": settings.rag_mode,
            "llm_provider": settings.llm_provider,
            "llm_model": settings.resolved_chat_model,
            "embedding_provider": settings.embedding_provider,
            "embedding_model": settings.resolved_embedding_model,
            "reranker_provider": settings.reranker_provider,
        }, ensure_ascii=True, separators=(",", ":")))


@app.get("/metrics")
def metrics():
    with get_conn() as conn:
        counts = dict(
            conn.execute(
                "SELECT status, count(*) FROM documents GROUP BY status"
            ).fetchall()
        )
    for status in ("pending", "ready", "failed"):
        documents_total.labels(status).set(counts.get(status, 0))
    return Response(generate_latest(), headers={"Content-Type": CONTENT_TYPE_LATEST})


app.include_router(health.router)
app.include_router(documents.router)
app.include_router(chat.router)
app.include_router(operations.router)
app.include_router(system.router)


@app.get("/")
def root():
    return {
        "service": settings.app_name,
        "version": "1.0.0-rc.2",
        "docs": "/docs",
        "mode": settings.rag_mode,
    }
