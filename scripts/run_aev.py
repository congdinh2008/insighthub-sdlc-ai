"""Run release RAG evaluation against an isolated real-provider runtime."""

import argparse
import hashlib
import json
import time
import unicodedata
import uuid
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "evaluation" / "corpus"


def call(base, path, method="GET", data=None, headers=None, timeout=130):
    request = Request(base + path, data=data, method=method, headers=headers or {})
    try:
        with urlopen(request, timeout=timeout) as response:
            return response.status, response.read(), dict(response.headers)
    except HTTPError as exc:
        return exc.code, exc.read(), dict(exc.headers)


def upload(base: str, path: Path):
    boundary = "----aev" + uuid.uuid4().hex
    mime = "application/pdf" if path.suffix == ".pdf" else "text/plain"
    body = (
        f'--{boundary}\r\nContent-Disposition: form-data; name="file"; filename="{path.name}"\r\n'
        f"Content-Type: {mime}\r\n\r\n"
    ).encode() + path.read_bytes() + f"\r\n--{boundary}--\r\n".encode()
    return call(
        base,
        "/documents",
        "POST",
        body,
        {
            "Content-Type": "multipart/form-data; boundary=" + boundary,
            "Idempotency-Key": "aev-upload-" + uuid.uuid4().hex,
        },
    )


def normalized(value: str) -> str:
    return unicodedata.normalize("NFC", value).casefold()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--api-url", default="http://127.0.0.1:8107")
    parser.add_argument("--output")
    args = parser.parse_args()
    base = args.api_url.rstrip("/")
    status, raw_profile, _ = call(base, "/system/profile")
    if status != 200:
        raise SystemExit("Runtime profile is unavailable")
    profile = json.loads(raw_profile)
    if profile["mode"] != "real":
        raise SystemExit("AEV requires RAG_MODE=real; fixture results are invalid")

    spec = json.loads((ROOT / "evaluation" / "AEV-01.json").read_text())
    source_names = sorted({name for case in spec["cases"] for name in case["sources"]})
    documents, created, corpus_hashes = {}, [], {}
    try:
        for name in source_names:
            path = CORPUS / name
            corpus_hashes[name] = hashlib.sha256(path.read_bytes()).hexdigest()
            status, body, _ = upload(base, path)
            if status != 201:
                raise SystemExit(f"Upload failed for {name}: HTTP {status}")
            document = json.loads(body)
            documents[name] = document["id"]
            if not document.get("deduplicated", False):
                created.append(document["id"])

        results = []
        passed = 0
        for case in spec["cases"]:
            for run in range(1, case.get("repeat", 1) + 1):
                payload = json.dumps({
                    "question": case["question"],
                    "document_ids": [documents[name] for name in case["sources"]],
                }, ensure_ascii=False).encode()
                started = time.perf_counter()
                status, body, headers = call(
                    base,
                    "/chat",
                    "POST",
                    payload,
                    {"Content-Type": "application/json", "Idempotency-Key": "aev-chat-" + uuid.uuid4().hex},
                )
                latency_ms = int((time.perf_counter() - started) * 1000)
                response = json.loads(body)
                answer = response.get("answer") or ""
                allowed_ids = {documents[name] for name in case["sources"]}
                citations = response.get("citations") or []
                checks = {
                    "http_200": status == 200,
                    "status": response.get("status") == case["expected_status"],
                    "concepts": all(normalized(term) in normalized(answer) for term in case.get("must_include_concepts", [])),
                    "forbidden": all(normalized(term) not in normalized(answer) for term in case.get("forbidden", [])),
                    "citation_scope": all(item.get("document_id") in allowed_ids for item in citations),
                    "citation_presence": bool(citations) if case["expected_status"] == "Answered" else not citations,
                    "claim_grounding": all(claim.get("citation_ids") for claim in response.get("claims", [])) if case["expected_status"] == "Answered" else not response.get("claims"),
                }
                verdict = all(checks.values())
                passed += int(verdict)
                results.append({
                    "case_id": case["id"],
                    "run": run,
                    "passed": verdict,
                    "checks": checks,
                    "http_status": status,
                    "response_status": response.get("status"),
                    "answer": answer,
                    "citations": citations,
                    "latency_ms": latency_ms,
                    "request_id": headers.get("X-Request-ID"),
                    "usage": response.get("usage"),
                    "retrieval": response.get("retrieval"),
                })
        artifact = {
            "schema_version": 1,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "api_url": base,
            "profile": profile,
            "corpus_sha256": corpus_hashes,
            "summary": {"passed": passed, "total": len(results), "success": passed == len(results)},
            "results": results,
        }
        output = Path(args.output) if args.output else ROOT / "reports" / "evaluation" / f"AEV-01-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(artifact, ensure_ascii=False, indent=2) + "\n")
        print(output)
        print(f"PASS={passed}/{len(results)}")
        if passed != len(results):
            raise SystemExit(1)
    finally:
        for document_id in created:
            call(
                base,
                f"/documents/{document_id}",
                "DELETE",
                headers={"Idempotency-Key": "aev-delete-" + uuid.uuid4().hex},
            )


if __name__ == "__main__":
    main()
