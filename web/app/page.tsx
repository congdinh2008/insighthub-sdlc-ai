import UploadPanel from "@/components/UploadPanel";
import ChatPanel from "@/components/ChatPanel";
import { listDocuments } from "@/lib/api";
import type { Document } from "@/lib/api";

export const dynamic = "force-dynamic";

export default async function Home() {
  let docs: Document[] = [];
  let initialError = "";
  try {
    docs = await listDocuments();
  } catch {
    initialError = "Không tải được danh sách tài liệu. Kiểm tra API rồi làm mới trạng thái.";
  }

  return (
    <div className="container">
      <header>
        <h1>InsightHub SDLC</h1>
        <p>Tra cứu và hỏi đáp từ tài liệu của bạn</p>
      </header>

      <div className="grid">
        <UploadPanel initial={docs} initialError={initialError} />
        <ChatPanel />
      </div>

      <footer>
        InsightHub SDLC - Không gian thực hành phát triển phần mềm.
      </footer>
    </div>
  );
}
