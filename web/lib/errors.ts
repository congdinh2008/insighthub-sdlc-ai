export function errorMessage(payload: unknown, fallback: string): string {
  if (payload && typeof payload === "object" && "detail" in payload) {
    const detail = (payload as { detail?: unknown }).detail;
    if (typeof detail === "string" && detail.trim()) return detail;
  }
  return fallback;
}

export function allowsMutation(
  request: Request,
  allowedOrigins = (process.env.MUTATION_ALLOWED_ORIGINS || "http://localhost:3107,http://127.0.0.1:3107").split(",").map(value => value.trim()),
): boolean {
  const origin = request.headers.get("origin");
  return origin === null || allowedOrigins.includes(origin);
}
