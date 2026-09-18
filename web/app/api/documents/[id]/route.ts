import { API_URL } from "@/lib/api";
import { allowsMutation } from "@/lib/errors";

export async function GET(_req: Request, context: { params: Promise<{ id: string }> }) {
  const { id } = await context.params;
  const res = await fetch(`${API_URL}/documents/${encodeURIComponent(id)}`, { cache: "no-store" });
  return Response.json(await res.json(), { status: res.status });
}

export async function DELETE(req: Request, context: { params: Promise<{ id: string }> }) {
  if (!allowsMutation(req)) return Response.json({ detail: "Origin không được phép." }, { status: 403 });
  const { id } = await context.params;
  const res = await fetch(`${API_URL}/documents/${encodeURIComponent(id)}`, { method: "DELETE" });
  return new Response(null, { status: res.status });
}
