export async function reconcileOperation(
  operationType: "upload" | "retry" | "chat" | "delete",
  key: string,
) {
  for (let attempt = 0; attempt < 5; attempt += 1) {
    const res = await fetch(`/api/operations/${operationType}/${encodeURIComponent(key)}`, { cache: "no-store" });
    if (res.ok) {
      const operation = await res.json();
      if (operation.status !== "processing") return operation;
    }
    await new Promise((resolve) => setTimeout(resolve, 1000));
  }
  return null;
}
