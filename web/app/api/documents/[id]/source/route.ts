import { API_URL } from "@/lib/api";

export async function GET(req: Request, context: { params: Promise<{ id: string }> }) {
  const { id } = await context.params;
  const segmentId = new URL(req.url).searchParams.get("segment_id");
  const query = segmentId ? `?segment_id=${encodeURIComponent(segmentId)}` : "";
  const res = await fetch(`${API_URL}/documents/${encodeURIComponent(id)}/source${query}`, { cache: "no-store" });
  return Response.json(await res.json(), { status: res.status });
}
