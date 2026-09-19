"use client";

import { useEffect, useState } from "react";
import type { ChatResult, Document } from "@/lib/api";
import { reconcileOperation } from "@/lib/operations";

export default function ChatPanel() {
  const [question, setQuestion] = useState("");
  const [result, setResult] = useState<ChatResult | null>(null);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");
  const [documents, setDocuments] = useState<Document[]>([]);
  const [selected, setSelected] = useState<number[]>([]);
  const [sourceView, setSourceView] = useState<{ title: string; content: string } | null>(null);

  async function openSource(documentId: number, segmentId?: number) {
    const query = segmentId ? `?segment_id=${segmentId}` : "";
    const res = await fetch(`/api/documents/${documentId}/source${query}`, { cache: "no-store" });
    if (!res.ok) { setError("Nguồn không còn khả dụng."); return; }
    const data = await res.json();
    setSourceView({ title: `${data.filename} - ${data.locator ? `${data.locator.type} ${data.locator.value}` : "toàn văn"}`, content: data.content });
  }

  useEffect(() => {
    const loadDocuments = () => fetch("/api/documents", { cache: "no-store" }).then((res) => res.ok ? res.json() : []).then((items: Document[]) => {
      const ready = items.filter((item) => item.status === "ready"); setDocuments(ready); setSelected(ready.map((item) => item.id));
    }).catch(() => setDocuments([]));
    loadDocuments();
    window.addEventListener("documents-changed", loadDocuments);
    return () => window.removeEventListener("documents-changed", loadDocuments);
  }, []);

  async function handleAsk() {
    if (!question.trim()) return;
    setBusy(true);
    setError("");
    setResult(null);
    const operationKey = crypto.randomUUID();
    try {
      const res = await fetch("/api/proxy?target=chat", {
        method: "POST",
        headers: { "Content-Type": "application/json", "Idempotency-Key": operationKey },
        body: JSON.stringify({ question, document_ids: selected }),
      });
      if (!res.ok) {
        if ([502, 504].includes(res.status)) {
          const operation = await reconcileOperation("chat", operationKey);
          if (operation?.status === "succeeded" && operation.response) {
            setResult(operation.response);
            return;
          }
        }
        const d = await res.json().catch(() => ({}));
        throw new Error(typeof d.detail === "string" ? d.detail : `Câu hỏi không hợp lệ hoặc API trả lỗi (${res.status}).`);
      }
      setResult(await res.json());
    } catch (err) {
      const operation = await reconcileOperation("chat", operationKey).catch(() => null);
      if (operation?.status === "succeeded" && operation.response) setResult(operation.response);
      else setError(err instanceof Error ? err.message : "Lỗi không xác định");
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="panel">
      <h2>Hỏi đáp (RAG)</h2>
      <textarea
        aria-label="Câu hỏi về tài liệu"
        maxLength={2000}
        placeholder="Đặt câu hỏi dựa trên tài liệu đã upload..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />
      <fieldset className="source-picker">
        <legend>Nguồn tra cứu</legend>
        {documents.length === 0 && <span className="meta">Chưa có tài liệu ready.</span>}
        {documents.map((doc) => <label key={doc.id}><input type="checkbox" checked={selected.includes(doc.id)} onChange={(event) => setSelected(event.target.checked ? [...selected, doc.id] : selected.filter((id) => id !== doc.id))} /> {doc.filename}</label>)}
      </fieldset>
      <button onClick={handleAsk} disabled={busy || !question.trim() || selected.length === 0}>
        {busy ? "Đang truy vấn..." : "Hỏi"}
      </button>
      {error && <p className="error" role="alert">{error}</p>}
      {result && (
        <>
          <div className="answer">{result.status === "NoEvidence" ? "Không tìm thấy bằng chứng phù hợp trong tài liệu đã chọn." : result.answer}</div>
          <div className="sources">
            Nguồn: {result.sources.join(", ") || "(không có)"}
          </div>
          <ul className="citation-list">{result.citations.map((citation) => <li key={citation.citation_id}><button className="action-link" onClick={() => openSource(citation.document_id, citation.source_segment_id)}><strong>{citation.source}</strong> - {citation.locator.type} {citation.locator.value}</button><br /><span className="meta">{citation.excerpt}</span></li>)}</ul>
          <div className="meta">Profile: {result.profile} | Provider: {result.provider} | Model: {result.model} | Reranker: {result.retrieval?.reranker_provider || "none"} | Latency: {result.latency_ms} ms</div>
          {sourceView && <div className="source-view" role="dialog" aria-label="Nội dung nguồn"><div><strong>{sourceView.title}</strong><button className="action-link" onClick={() => setSourceView(null)}>Đóng</button></div><pre>{sourceView.content}</pre></div>}
        </>
      )}
    </div>
  );
}
