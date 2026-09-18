"""Small REST adapters share bounded timeouts and sanitized transport errors."""

import logging
import httpx

from app.core.config import get_settings
from app.core.errors import ProviderError, ProviderTimeout
from app.core.deadline import check_deadline, remaining_timeout

logger = logging.getLogger("insighthub.providers")


def post_json(url: str, *, headers: dict, payload: dict) -> dict:
    try:
        # Do not inherit proxies, follow redirects, or log response bodies/URLs.
        with httpx.Client(
            timeout=remaining_timeout(get_settings().provider_timeout_seconds),
            trust_env=False,
            follow_redirects=False,
        ) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()
            if not isinstance(data, dict):
                raise ValueError("Invalid JSON object")
            return data
    except httpx.TimeoutException:
        logger.warning("AI provider request timed out")
        check_deadline()
        raise ProviderTimeout() from None
    except (httpx.HTTPError, ValueError):
        logger.warning("AI provider request failed")
        raise ProviderError() from None


def token_count(value) -> int | None:
    return value if type(value) is int and value >= 0 else None


def indexed_embeddings(data: dict, count: int) -> list:
    items = data["data"]
    if len(items) != count or any(type(item.get("index")) is not int for item in items):
        raise ProviderError()
    if sorted(item["index"] for item in items) != list(range(count)):
        raise ProviderError()
    return [item["embedding"] for item in sorted(items, key=lambda item: item["index"])]
