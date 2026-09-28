import { API_URL } from "@/lib/api";

export async function GET(_req: Request, context: { params: Promise<{ type: string; key: string }> }) {
  const { type, key } = await context.params;
  const res = await fetch(`${API_URL}/operations/${encodeURIComponent(type)}/${encodeURIComponent(key)}`, { cache: "no-store" });
  return Response.json(await res.json(), { status: res.status, headers: { "X-Request-ID": res.headers.get("X-Request-ID") || "" } });
}
