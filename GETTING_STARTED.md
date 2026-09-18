# Chạy InsightHub bản khởi động lại

18/09/2026. Code/config giữ first commit; dùng namespace riêng để không đụng database của project đã archive. Các lệnh dưới đây là hướng dẫn, chưa được chạy lại trong lượt khôi phục.

## Môi trường local riêng

Cần Docker Compose và cổng 8117/3117 trống. Chạy từ thư mục project, dùng cấu hình mẫu không có khóa thật:

```sh
export API_PORT=8117 WEB_PORT=3117
export RAG_MODE=fixture LLM_PROVIDER=fixture EMBEDDING_PROVIDER=fixture
docker compose --env-file .env.example -p insighthub-c07 up --build -d --wait
```

Web: http://localhost:3117. API docs: http://localhost:8117/docs. Namespace `insighthub-c07` tạo volume riêng; không dùng `insighthub-sdlc` hoặc `insighthub-c07-reference` của hướng cũ. Chưa có Auth, chỉ dùng local với tài liệu giả lập.

## Kiểm tra

Giữ các biến môi trường ở terminal trên. Các target Makefile gốc vẫn giữ nguyên; truyền đúng namespace và cổng:

```sh
make COMPOSE="docker compose --env-file .env.example -p insighthub-c07" test
make API_URL=http://127.0.0.1:8117 WEB_URL=http://127.0.0.1:3117 smoke
```

Nạp tài liệu trong `sample-docs/`, kiểm trạng thái Ready và hỏi một câu. Fixture trả kết quả giả lập có nhãn; không dùng kết quả đó làm bằng chứng AI thật đạt chất lượng. Backend integration test dùng schema riêng; smoke chỉ xóa dữ liệu do chính lần kiểm tạo.

## Dừng môi trường

```sh
docker compose --env-file .env.example -p insighthub-c07 stop
```

Giữ nguyên volume. Provider thật là việc riêng, chỉ cấu hình sau khi có yêu cầu và môi trường được xác nhận; cần index riêng khi đổi embedding identity. Lỗi provider không được âm thầm đổi thành fixture.

[Quay lại project](README.md) | [Quyết định và provenance](../00_INDEX.md).
