# AEV-01 - RAG evaluation corpus

Bộ nhỏ dùng để kiểm `Answered`, `NoEvidence`, citation và prompt injection trước release. Fixture không được tính là kết quả AEV.

1. Upload ba file trong `corpus/` vào database/index riêng cho provider thật.
2. Chạy từng case trong `AEV-01.json` với đúng `document_ids`.
3. Ghi provider, model, embedding identity, thời gian, response status, citation và nhận xét.
4. Không ghi API key hoặc provider response chứa dữ liệu không cần thiết.

Các file do Mochi AI biên soạn cho chương trình B2B C07, phạm vi sử dụng nội bộ lớp học.

| File | SHA-256 |
| --- | --- |
| `01_quy_trinh_vi.md` | `164567376f9ca27d9f2d05d8e9001e628c87ab3aa2fa1810da302f9619e642d1` |
| `02_operations_en.txt` | `d4a586ce013f138804580532b4030fcf219d985aaa3558e9f33eedc103fa2b37` |
| `03_reference.pdf` | `50fab3673cd8e7ce894afb428c67dfb38129807f9a2c7d4964afbbefad73712a` |
