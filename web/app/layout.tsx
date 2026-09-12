import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "InsightHub SDLC",
  description: "Quản lý tài liệu và hỏi đáp có nguồn",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="vi">
      <body>{children}</body>
    </html>
  );
}
