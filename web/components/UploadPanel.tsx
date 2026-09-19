"use client";

import { useEffect, useState } from "react";
import type { Document } from "@/lib/api";
import { errorMessage } from "@/lib/errors";
import { reconcileOperation } from "@/lib/operations";

export default function UploadPanel({ initial, initialError = "" }: { initial: Document[]; initialError?: string }) {
  const [docs, setDocs] = useState<Document[]>(initial);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState(initialError);
  const [hasLoaded, setHasLoaded] = useState(!initialError);
  const [detail, setDetail] = useState<{ id: number; attempts: { id: number; status: string; error_code?: string | null }[] } | null>(null);
  const pending = docs.some((doc) => doc.status === "pending");

  useEffect(() => {
    if (!pending) return;
    const controller = new AbortController();
    let timer: ReturnType<typeof setTimeout>;
    let attempts = 0;
    async function poll() {
      try {
        const res = await fetch("/api/documents", { cache: "no-store", signal: controller.signal });
        if (!res.ok) throw new Error("Không đọc được trạng thái tài liệu.");
        const items: Document[] = await res.json();
        setDocs(items);
        if (items.some((doc) => doc.status === "pending") && ++attempts < 60) {
          timer = setTimeout(poll, 2000);
        } else if (items.some((doc) => doc.status === "pending")) {
          setError("Chưa hoàn tất sau 2 phút. Làm mới trạng thái hoặc thử lại sau.");
        }
      } catch (err) {
        if (!controller.signal.aborted) setError(err instanceof Error ? err.message : "Không đọc được trạng thái.");
      }
    }
    timer = setTimeout(poll, 2000);
    return () => { controller.abort(); clearTimeout(timer); };
  }, [pending]);

  async function refresh() {
    const res = await fetch("/api/documents", { cache: "no-store" });
    if (!res.ok) throw new Error("API chưa sẵn sàng.");
    setDocs(await res.json());
    window.dispatchEvent(new Event("documents-changed"));
    setHasLoaded(true);
    setError("");
  }

  async function showDetail(id: number) {
    const res = await fetch(`/api/documents/${id}`, { cache: "no-store" });
    if (!res.ok) { setError("Không đọc được chi tiết tài liệu."); return; }
    setDetail(await res.json());
  }

  async function handleUpload(e: React.ChangeEvent<HTMLInputElement>) {
    const file = e.target.files?.[0];
    if (!file) return;
    if (file.size > 10 * 1024 * 1024) {
      setError("File vượt quá 10 MB.");
      e.target.value = "";
      return;
    }
    setBusy(true);
    setError("");
    const operationKey = crypto.randomUUID();
    try {
      const fd = new FormData();
      fd.append("file", file);
      const res = await fetch("/api/proxy?target=upload", {
        method: "POST",
        body: fd,
        headers: { "Idempotency-Key": operationKey },
        signal: AbortSignal.timeout(125000),
      });
      if (!res.ok) {
        if ([502, 504].includes(res.status)) {
          const operation = await reconcileOperation("upload", operationKey);
          if (operation?.status === "succeeded") {
            await refresh();
            return;
          }
        }
        const d = await res.json().catch(() => ({}));
        throw new Error(errorMessage(d, `Upload lỗi: ${res.status}`));
      }
      await refresh();
    } catch (err) {
      // Processing can persist a failed document before returning an HTTP error.
      const operation = await reconcileOperation("upload", operationKey).catch(() => null);
      await refresh().catch(() => {});
      if (operation?.status !== "succeeded") setError(err instanceof Error ? err.message : "Lỗi không xác định");
    } finally {
      setBusy(false);
      e.target.value = "";
    }
  }

  async function removeDocument(id: number) {
    if (!window.confirm("Xóa tài liệu và toàn bộ nguồn/chỉ mục liên quan?")) return;
    setBusy(true); setError("");
    const operationKey = crypto.randomUUID();
    try {
      const res = await fetch(`/api/documents/${id}`, {
        method: "DELETE",
        headers: { "Idempotency-Key": operationKey },
        signal: AbortSignal.timeout(65000),
      });
      if (!res.ok) {
        if ([502, 504].includes(res.status)) {
          const operation = await reconcileOperation("delete", operationKey);
          if (operation?.status === "succeeded") { await refresh(); return; }
        }
        throw new Error("Không xóa được tài liệu.");
      }
      await refresh();
    } catch (err) {
      const operation = await reconcileOperation("delete", operationKey).catch(() => null);
      await refresh().catch(() => {});
      if (operation?.status !== "succeeded") setError(err instanceof Error ? err.message : "Không xóa được tài liệu.");
    } finally { setBusy(false); }
  }

  async function retryDocument(id: number, file: File) {
    setBusy(true); setError("");
    const operationKey = crypto.randomUUID();
    try {
      const fd = new FormData(); fd.append("file", file);
      const res = await fetch(`/api/documents/${id}/retry`, {
        method: "POST", body: fd,
        headers: { "Idempotency-Key": operationKey },
        signal: AbortSignal.timeout(125000),
      });
      if (!res.ok) {
        if ([502, 504].includes(res.status)) {
          const operation = await reconcileOperation("retry", operationKey);
          if (operation?.status === "succeeded") { await refresh(); return; }
        }
        const data = await res.json().catch(() => ({})); throw new Error(errorMessage(data, "Retry thất bại."));
      }
      await refresh();
    } catch (err) {
      const operation = await reconcileOperation("retry", operationKey).catch(() => null);
      await refresh().catch(() => {});
      if (operation?.status !== "succeeded") setError(err instanceof Error ? err.message : "Retry thất bại.");
    }
    finally { setBusy(false); }
  }

  return (
    <div className="panel">
      <h2>Tài liệu</h2>
      <input
        type="file"
        aria-label="Chọn tài liệu .txt, .md hoặc .pdf"
        accept=".txt,.md,.pdf"
        onChange={handleUpload}
        disabled={busy}
      />
      {busy && <p className="meta">Đang gửi tài liệu...</p>}
      {pending && <p className="meta" role="status">Đang chờ xử lý. Trạng thái sẽ tự cập nhật.</p>}
      <button onClick={() => { setError(""); refresh().catch(() => setError("Không đọc được trạng thái.")); }} disabled={busy}>Làm mới trạng thái</button>
      {error && <p className="error" role="alert">{error}</p>}
      <ul className="doc-list" style={{ marginTop: "1rem" }}>
        {hasLoaded && docs.length === 0 && (
          <li className="meta">Chưa có tài liệu. Upload .txt / .md / .pdf.</li>
        )}
        {docs.map((d) => (
          <li key={d.id} className="doc-item">
            <span>
              {d.filename}{" "}
              <span className="meta">({d.chunk_count} chunks)</span>
            </span>
            <span className={`badge ${d.status}`}>{d.status === "ready" ? "Sẵn sàng" : d.status === "failed" ? "Thất bại" : "Đang xử lý"}</span>
            <span>
              <button className="action-link" onClick={() => showDetail(d.id)}>Chi tiết</button>
              {d.status === "failed" && <label className="action-link">Thử lại<input hidden type="file" accept=".txt,.md,.pdf" onChange={(e) => { const file = e.target.files?.[0]; if (file) retryDocument(d.id, file); }} /></label>}
              <button className="action-link" onClick={() => removeDocument(d.id)} disabled={busy}>Xóa</button>
            </span>
            {d.error_code && <span className="error">Mã lỗi: {d.error_code}</span>}
            {detail?.id === d.id && <div className="document-detail"><strong>Lịch sử xử lý</strong>{detail.attempts.length === 0 ? <p className="meta">Chưa có attempt.</p> : <ul>{detail.attempts.map((attempt) => <li key={attempt.id}>#{attempt.id}: {attempt.status}{attempt.error_code ? ` (${attempt.error_code})` : ""}</li>)}</ul>}<button className="action-link" onClick={() => setDetail(null)}>Đóng</button></div>}
          </li>
        ))}
      </ul>
    </div>
  );
}
