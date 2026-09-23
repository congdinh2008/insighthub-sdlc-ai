# Đặc tả yêu cầu phần mềm InsightHub

**Ứng dụng quản lý và khai thác tài liệu cá nhân bằng AI**

Phiên bản 2.4 | Ngày cập nhật: 18/09/2026

InsightHub cho phép người dùng tổ chức tài liệu trong các Notebook riêng tư, hỏi đáp dựa trên tài liệu nguồn, quản lý ghi chú và tạo nội dung bằng công cụ AI. Tài liệu này xác định các chức năng, quy tắc nghiệp vụ, ràng buộc dữ liệu và tiêu chí nghiệm thu của sản phẩm.

| Thuộc tính | Nội dung |
| --- | --- |
| Mã tài liệu | RS-B2BC07-IH-001 |
| Phiên bản | 2.4 |
| Ngày cập nhật | 18/09/2026 |
| Trạng thái | Dự thảo, chờ chủ sản phẩm rà soát |
| Chủ tài liệu | Đinh Xuân Công |
| Phạm vi sản phẩm | InsightHub R1: quản lý và khai thác tài liệu cá nhân |
| Nguồn nội dung | Bản Markdown này là nguồn biên soạn và rà soát hiện hành |
| Đối tượng sử dụng | Chủ sản phẩm, chuyên viên phân tích nghiệp vụ, người thiết kế UI/UX, lập trình viên, người kiểm thử và người nghiệm thu |

**Cả năm công cụ AI đều bắt buộc trong R1:** Mindmap, Tóm tắt, Slide, Quiz và Báo cáo. Nghiệm thu sản phẩm theo SRS phải bao phủ toàn bộ yêu cầu và tiêu chí chấp nhận tương ứng.

## Mục lục

1. [Giới thiệu và quy ước tài liệu](#muc-1)
2. [Bối cảnh, mục tiêu và phạm vi sản phẩm](#muc-2)
3. [Tác nhân và quyền truy cập](#muc-3)
4. [Quy tắc nghiệp vụ](#muc-4)
5. [Giới hạn xử lý và vòng đời dữ liệu](#muc-5)
6. [Đặc tả ca sử dụng](#muc-6)
7. [Yêu cầu chức năng](#muc-7)
8. [Mô hình dữ liệu và tính toàn vẹn](#muc-8)
9. [Giao diện, trải nghiệm và thông báo](#muc-9)
10. [Yêu cầu tích hợp](#muc-10)
11. [Yêu cầu phi chức năng](#muc-11)
12. [Đánh giá chất lượng AI](#muc-12)
13. [Nghiệm thu và truy vết](#muc-13)
14. [Điều kiện bàn giao và kiểm soát thay đổi](#muc-14)
15. [Quản lý tài liệu và nguồn tham khảo](#muc-15)

Tra cứu nhanh: [Danh mục ca sử dụng](#uc-catalog) · [Từ điển dữ liệu](#data-dictionary) · [Thông báo](#msg-catalog) · [Email giao dịch](#email-catalog) · [Tài liệu và điều kiện triển khai](#implementation-decisions).

<a id="muc-1"></a>

## 1. Giới thiệu và quy ước tài liệu

### 1.1 Mục đích và đối tượng sử dụng

Tài liệu đặc tả yêu cầu phần mềm (SRS) mô tả toàn bộ InsightHub R1, bao gồm quản lý tài khoản, Notebook, tài liệu, hỏi đáp bằng RAG, ghi chú, năm công cụ AI, giao diện và vận hành hệ thống. Chủ sản phẩm và nhóm dự án sử dụng tài liệu để thống nhất phạm vi, thiết kế giải pháp, triển khai chức năng và xây dựng các trường hợp kiểm thử.

Phạm vi sản phẩm được xác định theo yêu cầu của chủ sản phẩm ngày 18/09/2026. R1 hướng tới ứng dụng cá nhân chạy trong môi trường local hoặc sandbox có kiểm soát. Các yêu cầu và ngưỡng trong bản dự thảo cần được rà soát trước khi phê duyệt làm căn cứ nghiệm thu; mục 5.5 ghi căn cứ lựa chọn và các giả định cần kiểm chứng.

### 1.2 Quy ước mã và mức độ bắt buộc của yêu cầu

| Mã | Ý nghĩa |
| --- | --- |
| OBJ | Mục tiêu sản phẩm |
| BR | Quy tắc nghiệp vụ |
| UC / CF | Ca sử dụng hệ thống / tình huống xử lý dùng chung |
| LIM | Giới hạn đầu vào và vận hành |
| IH-AUTH / NB / DOC / CHAT / NOTE | Yêu cầu chức năng tài khoản, Notebook, tài liệu, hỏi đáp, ghi chú |
| IH-AI / MM / SUM / SLD / QUIZ / RPT / OUT | Yêu cầu chung AI, năm công cụ và quản lý kết quả |
| IH-DATA / UX / MSG / INT / NFR / REL | Yêu cầu dữ liệu, trải nghiệm, thông báo, tích hợp, phi chức năng và bàn giao |
| MSG / EML | Thông báo giao diện hoặc vận hành / email giao dịch |
| AC / UAT / AEV | Tiêu chí chấp nhận của yêu cầu, kịch bản nghiệm thu, bộ đánh giá AI |

Từ “phải” xác định một yêu cầu bắt buộc. Mỗi mã IH định danh một yêu cầu; các tiêu chí chấp nhận AC xác định điều kiện để kiểm chứng yêu cầu đó. Quy tắc nghiệp vụ BR, giới hạn LIM và các đặc tả chi tiết tại mục 8-10 được áp dụng cùng với yêu cầu IH liên quan. Các chức năng được liệt kê tại mục 2.2 nằm ngoài phạm vi nghiệm thu R1.

Mã yêu cầu được giữ ổn định giữa các phiên bản để phục vụ truy vết. Tiêu chí AC có thể được tách hoặc sửa khi thay đổi nội dung; bằng chứng kiểm thử phải ghi cả mã AC và phiên bản SRS. Mỗi thay đổi phải ghi rõ lý do, yêu cầu bị ảnh hưởng, tác động và các trường hợp kiểm thử cần cập nhật theo IH-REL-003.

Quy ước nơi định nghĩa chính: mục 2 xác định phạm vi; BR xác định quy tắc nghiệp vụ; LIM xác định giá trị giới hạn; mục 5 xác định vòng đời; mục 8 xác định ý nghĩa dữ liệu và cấu trúc; mục 9-10 xác định thông báo và giao tiếp. UC mô tả việc áp dụng các quy tắc trong từng tình huống; AC xác định kết quả cần kiểm chứng. Các phần tham chiếu không tự tạo một giá trị hoặc ngoại lệ khác. Nếu phát hiện bất nhất, nhóm dự án ghi nhận vị trí và tác động để chủ sản phẩm giải quyết trước khi triển khai phần bị ảnh hưởng, không tự chọn cách hiểu dễ đạt hơn.

### 1.3 Thuật ngữ

| Thuật ngữ | Định nghĩa trong InsightHub |
| --- | --- |
| SRS (Software Requirements Specification) | Tài liệu đặc tả yêu cầu phần mềm, xác định hành vi, ràng buộc và điều kiện nghiệm thu sản phẩm. |
| R1 | Phiên bản sản phẩm thuộc phạm vi đặc tả và nghiệm thu của tài liệu này. |
| AI (Artificial Intelligence) | Trí tuệ nhân tạo. Trong InsightHub, AI hỗ trợ hỏi đáp và tạo nội dung từ tài liệu nguồn. |
| Notebook | Không gian riêng của một người dùng, chứa tài liệu, hội thoại, ghi chú và kết quả AI. |
| Tài liệu nguồn | Tệp người dùng tải vào Notebook và phần văn bản được trích xuất từ tệp. |
| Tiếp nhận và xử lý tài liệu (ingestion) | Quá trình kiểm tra tệp, trích xuất văn bản, chia đoạn và lập chỉ mục để phục vụ truy xuất. |
| RAG (Retrieval-Augmented Generation) | Cơ chế truy xuất nội dung nguồn phù hợp và sử dụng nội dung đó làm căn cứ tạo câu trả lời. |
| Véc-tơ biểu diễn nội dung (embedding) | Biểu diễn số của đoạn văn bản, dùng để tìm nội dung có liên quan về ngữ nghĩa. |
| Tham chiếu nguồn (citation) | Thông tin xác định tài liệu và vị trí đoạn văn bản được dùng làm căn cứ cho câu trả lời hoặc kết quả AI. |
| Công cụ AI (AI Tool) | Chức năng tạo một loại nội dung xác định từ tài liệu đã chọn. R1 bắt buộc có đủ năm công cụ. |
| Mindmap / Slide / Quiz | Tên ba công cụ tương ứng với sơ đồ tư duy, bài trình chiếu và bộ câu hỏi trắc nghiệm. Hai công cụ còn lại là Tóm tắt và Báo cáo. |
| Kết quả AI (artifact) | Nội dung đã lưu của một lần chạy công cụ AI thành công, kèm loại công cụ, nguồn, cấu hình và thời điểm tạo. Không bao gồm câu trả lời hỏi đáp hoặc ghi chú. |
| Hồ sơ cá nhân | Thông tin tài khoản hiển thị cho người dùng, gồm tên, email, ảnh đại diện, phương thức đăng nhập và trạng thái xác minh. |
| Hồ sơ cấu hình nghiệm thu | Bản ghi môi trường triển khai, mô hình và nhà cung cấp, giới hạn xử lý, phiên bản Figma và bộ dữ liệu dùng để nghiệm thu. |
| AC (Acceptance Criteria) | Tiêu chí chấp nhận cụ thể của từng yêu cầu. |
| UAT (User Acceptance Testing) | Kiểm thử chấp nhận sản phẩm theo hành trình nghiệp vụ và kết quả kỳ vọng. |
| QA (Quality Assurance) | Vai trò bảo đảm chất lượng, quản lý việc kiểm thử và bằng chứng nghiệm thu trong dự án. |
| Đáp án và tiêu chí đối chiếu (test oracle) | Căn cứ xác định kết quả đúng hoặc sai của một trường hợp kiểm thử. Với AI, căn cứ có thể là đoạn nguồn, các ý bắt buộc và hành vi kỳ vọng. |
| Luồng chính | Trình tự tương tác điển hình để tác nhân hoàn thành mục tiêu của ca sử dụng. |
| Luồng thay thế | Trình tự tương tác khác với luồng chính nhưng vẫn phù hợp với chức năng và quy tắc nghiệp vụ. |
| Luồng ngoại lệ | Cách hệ thống xử lý lỗi hoặc điều kiện khiến tác nhân chưa thể hoàn thành mục tiêu. |
| Tiền điều kiện | Trạng thái của tài khoản, dữ liệu hoặc môi trường cần có trước khi bắt đầu ca sử dụng. |
| Hậu điều kiện | Trạng thái của dữ liệu và hệ thống sau khi ca sử dụng kết thúc. |
| Bảo đảm tối thiểu | Những điều hệ thống vẫn phải bảo toàn dù ca sử dụng không thành công. |
| Mã thao tác (idempotency key) | Mã nhận diện một thao tác nghiệp vụ. Khi nhận lại cùng mã và cùng dữ liệu, hệ thống trả kết quả của thao tác đã tiếp nhận thay vì tạo thêm thao tác mới. |
| Mã tra cứu kỹ thuật | Mã giúp người vận hành tìm các sự kiện và lỗi liên quan trong nhật ký. Mã này không thay thế mã thao tác dùng để kiểm soát yêu cầu gửi lặp. |
| Xóa về nghiệp vụ | Trạng thái mà tài nguyên không còn được truy cập hoặc sử dụng, dù việc xóa dữ liệu vật lý có thể chưa hoàn tất. |
| Xóa dữ liệu vật lý | Loại bỏ nội dung khỏi cơ sở dữ liệu, kho tệp và chỉ mục theo thời hạn lưu giữ. |
| Tài nguyên | Đối tượng dữ liệu được quản lý và kiểm soát quyền truy cập, chẳng hạn Notebook, tài liệu, hội thoại, ghi chú hoặc kết quả AI. |
| UI / UX | Giao diện người dùng (User Interface) và trải nghiệm người dùng (User Experience). |
| API (Application Programming Interface) | Giao diện lập trình để các thành phần phần mềm trao đổi dữ liệu và thực hiện thao tác. |
| Mã xác thực (token) | Giá trị dùng để xác minh danh tính, phiên đăng nhập hoặc thao tác được cấp phép. |
| Địa chỉ nhận kết quả xác thực (callback) | Địa chỉ của ứng dụng tiếp nhận phản hồi từ dịch vụ xác thực. |
| Ứng dụng khách | Trình duyệt hoặc thành phần phía người dùng gửi yêu cầu tới máy chủ. |
| MiB / GiB | Đơn vị dung lượng nhị phân: 1 MiB = 1.048.576 byte; 1 GiB = 1.073.741.824 byte. |

<a id="muc-2"></a>

## 2. Bối cảnh, mục tiêu và phạm vi sản phẩm

Người dùng thường lưu tài liệu rời rạc, mất thời gian đọc lại và phải chuyển qua nhiều công cụ để tìm thông tin, ghi chú hoặc tạo nội dung. InsightHub tổ chức tài liệu theo Notebook và cung cấp cùng một nơi để hỏi đáp, kiểm tra nguồn và tạo nội dung phục vụ học tập hoặc công việc.

| Mục tiêu | Kết quả có thể kiểm chứng |
| --- | --- |
| OBJ-01 Tổ chức tài liệu cá nhân | Người dùng tự tạo tài khoản, quản lý Notebook và khai thác dữ liệu của mình. |
| OBJ-02 Hỏi đáp có căn cứ | Câu trả lời truy xuất đúng Notebook, có nguồn kiểm tra và phân biệt thiếu căn cứ với lỗi. |
| OBJ-03 Tạo nội dung có ích | Cả Mindmap, Tóm tắt, Slide, Quiz và Báo cáo tạo được đầu ra đúng cấu trúc, lưu kết quả và mở lại để sử dụng. |
| OBJ-04 Trải nghiệm nhất quán | Các hành trình chính đáp ứng thiết kế Figma được duyệt và sử dụng được trên máy tính, thiết bị di động. |
| OBJ-05 Vận hành có thể kiểm chứng | Dữ liệu được bảo toàn sau khi khởi động lại; quyền truy cập, thông báo lỗi, kết quả kiểm thử và hướng dẫn bàn giao có thể đối chiếu với yêu cầu. |

### 2.1 Trong phạm vi R1

R1 bao gồm các nhóm chức năng sau:

- Đăng ký và xác minh email; đăng nhập bằng email và mật khẩu hoặc bằng Google; khôi phục mật khẩu, quản lý phiên, hồ sơ cá nhân và quyền truy cập dữ liệu.
- Notebook riêng tư; nạp TXT, Markdown, PDF có văn bản; xem trạng thái, nội dung nguồn và xóa tài liệu.
- Chatbot RAG theo Notebook, tham chiếu nguồn, lịch sử hội thoại và ghi chú.
- Đầy đủ năm công cụ AI: Mindmap, Tóm tắt, Slide, Quiz và Báo cáo; quản lý kết quả đã sinh.
- Giao diện theo thiết kế Figma được duyệt, thích ứng với kích thước màn hình, thể hiện rõ trạng thái xử lý và đáp ứng yêu cầu tiếp cận cơ bản.
- Tích hợp dịch vụ định danh, email giao dịch, embedding và mô hình sinh nội dung; vận hành và kiểm chứng trong cấu hình R1.

### 2.2 Ngoài phạm vi R1

R1 không bao gồm các chức năng sau:

- Chia sẻ Notebook, cộng tác nhiều người, quản lý tổ chức, không gian làm việc doanh nghiệp hoặc vai trò quản trị nghiệp vụ.
- Đăng nhập một lần cho doanh nghiệp (SSO), xác thực đa yếu tố (MFA) và thanh toán.
- Nhận dạng ký tự từ ảnh (OCR), xử lý âm thanh hoặc video, thu thập dữ liệu từ website và tìm kiếm trên web.
- Tác nhân AI tự thực hiện hành động trên hệ thống bên ngoài.
- Biên tập tự do bố cục Mindmap hoặc Slide; xuất nội dung thành tệp PPTX, DOCX hoặc PDF.
- Ngân hàng câu hỏi, cấp chứng chỉ và tích hợp hệ thống quản lý học tập (LMS).
- Trung tâm thông báo, bộ đếm chưa đọc, thông báo đẩy, SMS và email báo hoàn tất AI.
- Đổi email tài khoản, xóa tài khoản tự phục vụ, chia sẻ hoặc di chuyển tài nguyên sang Notebook khác; lưu nháp lựa chọn Quiz trước khi nộp và khôi phục nháp sau đóng trình duyệt.
- Ứng dụng cài đặt riêng cho thiết bị di động; hạ tầng sẵn sàng cao trên nhiều vùng và cam kết mức dịch vụ thương mại (SLA).
- Triển khai cloud, Kubernetes hoặc hạ tầng bằng mã; hàng đợi và worker chuyên biệt, kiểm thử tải quy mô lớn, hệ thống giám sát vận hành chuyên sâu.
- Sao lưu tự động theo lịch, cam kết thời gian hoặc mức mất dữ liệu khi phục hồi và khôi phục bản sao lưu cũ vào môi trường đang phục vụ người dùng. R1 chỉ yêu cầu sao lưu thủ công và kiểm chứng khôi phục trên môi trường riêng theo UC-09 và UC-16.

Lịch sử hỏi đáp được lưu để người dùng đọc lại. R1 xử lý mỗi câu hỏi độc lập trên nguồn đã chọn, không yêu cầu suy luận từ các lượt hội thoại trước. Người dùng có thể nhập lại đầy đủ ngữ cảnh trong câu hỏi.

### 2.3 Phạm vi trách nhiệm của hệ thống và dịch vụ tích hợp

| Thành phần | Trách nhiệm và ranh giới |
| --- | --- |
| Ứng dụng InsightHub | Kiểm soát quyền dữ liệu, nghiệp vụ Notebook, tài liệu, hỏi đáp, ghi chú, năm công cụ, giao diện và dữ liệu được lưu bền vững. |
| Dịch vụ định danh và Google | Xác thực thông tin đăng nhập, danh tính Google, các liên kết xác minh email hoặc đặt lại mật khẩu theo cấu hình được kiểm chứng. |
| Dịch vụ email | Chuyển các email tài khoản EML-001 đến EML-005. Phản hồi công khai không tiết lộ sự tồn tại tài khoản; lỗi gửi phải có trạng thái để đối soát và cách thử lại. |
| Embedding và mô hình AI | Xử lý nội dung trong phạm vi nguồn hợp lệ. Sự cố, hạn mức sử dụng và hết thời gian chờ không được biến thành câu trả lời thiếu căn cứ. |
| Kho dữ liệu | Lưu dữ liệu nghiệp vụ, tệp, văn bản, chỉ mục và kết quả; bảo đảm cách ly quyền và phục hồi theo yêu cầu. |

Việc lựa chọn thư viện xác thực, mô hình AI, nền tảng giao diện và cách thực thi tác vụ thuộc thiết kế giải pháp. Nhóm triển khai được sử dụng dịch vụ và thư viện sẵn có; SRS không yêu cầu tự xây dựng dịch vụ định danh, hệ thống gửi thư hoặc nền tảng xử lý tác vụ riêng. Các lựa chọn phải đáp ứng hành vi và giới hạn được đặc tả.

### 2.4 Đối tượng sử dụng và giả định vận hành

Người dùng chính là cá nhân cần đọc, hỏi đáp, hệ thống hóa kiến thức hoặc tạo nội dung từ tài liệu của mình. Hành trình điển hình là tạo tài khoản, tạo Notebook, tải nguồn, kiểm tra trạng thái, hỏi đáp hoặc tạo nội dung rồi kiểm tra căn cứ và lưu kết quả. Người vận hành chịu trách nhiệm môi trường kỹ thuật; không có vai trò duyệt tài liệu hoặc quản lý người dùng qua giao diện nghiệp vụ trong R1.

Giả định R1 được truy cập qua trình duyệt có kết nối Internet, người dùng có email nhận thư và tài khoản Google nếu chọn phương thức đó. Môi trường tích hợp có dịch vụ xác thực, email và AI đủ khả năng đáp ứng giới hạn đã nêu. Người dùng chỉ tải tài liệu được phép xử lý; giao diện phải nêu rõ nội dung được gửi tới dịch vụ AI theo phạm vi nguồn để người dùng quyết định trước khi tải và khai thác. Ứng dụng phải công bố tên nhà cung cấp, phạm vi dữ liệu chuyển giao và chính sách xử lý dữ liệu theo cấu hình triển khai, được kiểm chứng bằng IH-INT-002-AC03. Bộ dữ liệu R1 dùng tài liệu công khai, dữ liệu giả lập hoặc tài liệu đã được phép xử lý với các nhà cung cấp được chọn; không mặc định cho phép đưa dữ liệu mật hoặc dữ liệu cá nhân của bên thứ ba vào môi trường thử nghiệm.

<a id="muc-3"></a>

## 3. Tác nhân và quyền truy cập

Bảng sau xác định các bên tương tác với InsightHub và phạm vi thao tác của từng bên. Quyền truy cập dữ liệu nghiệp vụ phụ thuộc tài khoản, phiên đăng nhập và quyền sở hữu Notebook.

| Tác nhân | Thao tác được phép | Giới hạn quyền truy cập |
| --- | --- | --- |
| Người chưa đăng nhập | Đăng ký, đăng nhập; yêu cầu xác minh email hoặc khôi phục mật khẩu. | Không được đọc hoặc thay đổi dữ liệu trong Notebook. |
| Người dùng có tài khoản chờ xác minh email | Xem trạng thái xác minh, gửi lại email xác minh và đăng xuất. | Không được truy cập Notebook và các dữ liệu nghiệp vụ liên quan. |
| Người dùng có tài khoản đã xác minh và phiên đăng nhập hợp lệ | Quản lý hồ sơ cá nhân và các tài nguyên thuộc sở hữu của mình. | Không được truy cập dữ liệu của người khác qua giao diện, API, đường dẫn trực tiếp hoặc kết quả do AI tạo. |
| Dịch vụ bên ngoài được tích hợp | Xử lý tác vụ do InsightHub gửi, trong phạm vi dữ liệu cần thiết cho tác vụ. | Không có phiên đăng nhập của người dùng và không được truy cập giao diện ứng dụng. |
| Người vận hành hệ thống | Triển khai, cấu hình, kiểm tra tình trạng hoạt động, sao lưu và khôi phục qua công cụ vận hành. | R1 không cung cấp giao diện quản trị nghiệp vụ hoặc chức năng duyệt nội dung cho vai trò này. |

Mỗi Notebook có đúng một chủ sở hữu; một người dùng có thể sở hữu nhiều Notebook. Tài liệu, hội thoại, ghi chú và kết quả AI tuân theo quyền truy cập của Notebook chứa chúng. Máy chủ phải kiểm tra quyền tại thời điểm xử lý mọi thao tác đọc, ghi, tải xuống hoặc truy xuất nguồn.

<a id="muc-4"></a>

## 4. Quy tắc nghiệp vụ

Các quy tắc sau áp dụng thống nhất cho giao diện, API, xử lý nền và các dịch vụ tích hợp.

### BR-01: Quyền sở hữu và kiểm soát truy cập

Hệ thống xác định chủ sở hữu từ phiên đăng nhập hợp lệ. Thông tin do trình duyệt hoặc ứng dụng khách gửi không được dùng để tự cấp quyền hoặc thay đổi chủ sở hữu. R1 không hỗ trợ chuyển quyền sở hữu Notebook.

### BR-02: Tính duy nhất của địa chỉ email

Hệ thống loại bỏ khoảng trắng ở đầu và cuối địa chỉ email, sau đó so sánh địa chỉ không phân biệt chữ hoa, chữ thường. Hệ thống không tự loại bỏ dấu chấm hoặc phần địa chỉ sau dấu cộng. Mỗi địa chỉ email đã chuẩn hóa chỉ được gắn với một tài khoản InsightHub; mã định danh do nhà cung cấp xác thực cấp được lưu riêng.

### BR-03: Điều kiện liên kết danh tính đăng nhập

Danh tính Google phải được máy chủ kiểm chứng bằng định danh nhà cung cấp và email đã xác minh. Trùng chuỗi email không đủ để liên kết hai phương thức đăng nhập.

- Nếu email đã gắn với tài khoản `Active` có mật khẩu, người dùng phải xác nhận mật khẩu hiện tại trong giao dịch liên kết theo LIM-19. Nếu không nhớ mật khẩu, thực hiện UC-02 rồi bắt đầu lại UC-11. Chỉ liên kết khi cả danh tính Google và bằng chứng kiểm soát tài khoản hiện hữu còn hợp lệ.
- Nếu email trùng tài khoản `PendingVerification`, không kích hoạt và giữ nguyên mật khẩu cũ chỉ dựa trên phản hồi Google hoặc liên kết xác minh email. Người dùng phải hoàn tất UC-02 để thiết lập mật khẩu mới qua email, vô hiệu mật khẩu, phiên và liên kết xác thực cũ của tài khoản. Sau đó bắt đầu lại UC-11 và xác nhận mật khẩu mới trước khi liên kết. Quy tắc này bảo vệ trường hợp tài khoản đã được người khác đăng ký trước bằng email của chủ tài khoản thực.
- Sau khi liên kết thành công, gửi email thông báo EML-003. Email này không cấp quyền và không có liên kết để xác nhận hoặc tự động hoàn tất việc liên kết.

Danh tính Google đã liên kết được nhận diện bằng định danh nhà cung cấp. Thay đổi email do Google trả về không tự đổi email ứng dụng hoặc chuyển Notebook sang tài khoản khác. R1 không hỗ trợ hợp nhất hai tài khoản có dữ liệu riêng.

### BR-04: Điều kiện sử dụng tài liệu làm nguồn

Hỏi đáp và công cụ AI chỉ được sử dụng tài liệu ở trạng thái `Ready`, chưa bị xóa và thuộc Notebook đang hoạt động do người gửi yêu cầu sở hữu.

### BR-05: Phạm vi tài liệu được sử dụng

Khi người dùng chưa chọn phạm vi nguồn, hỏi đáp sử dụng toàn bộ tài liệu `Ready` trong Notebook. Với công cụ AI, người dùng phải chọn rõ từ 1 đến 3 tài liệu theo LIM-05. Hệ thống không được tự mở rộng phạm vi sang tài liệu khác.

### BR-06: Kiểm soát nội dung và chỉ dẫn không đáng tin cậy

Hệ thống phải xử lý văn bản tài liệu, câu hỏi và đầu ra của mô hình như dữ liệu đầu vào không đáng tin cậy. Chỉ dẫn nằm trong các nội dung này không được làm thay đổi quyền truy cập, tiết lộ thông tin bí mật, kích hoạt công cụ bên ngoài hoặc mở rộng phạm vi nguồn.

### BR-07: Tính hợp lệ của tham chiếu nguồn

Mỗi tham chiếu nguồn phải xác định được tài liệu và vị trí văn bản thuộc danh sách nguồn của yêu cầu xử lý. Hệ thống sử dụng định danh tài liệu để phân biệt các nguồn; tên tệp không được dùng thay cho định danh.

### BR-08: Xóa tài liệu nguồn

Ngay sau khi thao tác xóa thành công, hệ thống phải loại tài liệu khỏi danh sách nguồn có thể sử dụng cho yêu cầu mới. Tác vụ đang sử dụng tài liệu đó phải dừng và không được công bố kết quả. Nội dung hội thoại và kết quả AI đã lưu trước thời điểm xóa vẫn được giữ, nhưng tham chiếu phải thể hiện rằng tài liệu nguồn đã bị xóa. Người dùng có thể xóa các nội dung đã lưu này bằng chức năng tương ứng.

### BR-09: Xóa Notebook

Xóa Notebook làm mất khả năng truy cập mọi tài nguyên con ngay khi thao tác hoàn tất. Tác vụ đang chạy không được tái tạo dữ liệu dưới Notebook đã xóa. Không có thùng rác trong R1.

### BR-10: Xử lý yêu cầu gửi lặp và thao tác thử lại

Khi nhận lại yêu cầu có cùng mã thao tác và cùng dữ liệu, hệ thống phải trả kết quả của thao tác đã tiếp nhận, không tạo thêm tài liệu, lượt hỏi đáp hoặc kết quả AI. Khi người dùng thử lại một thao tác đã thất bại, hệ thống tạo lần xử lý mới và lưu quan hệ với lần trước. Thao tác **Tạo lại** từ một kết quả AI đã lưu phải tạo kết quả mới và giữ nguyên bản cũ.

### BR-11: Bảo toàn nội dung và nguồn của kết quả đã lưu

Hệ thống phải lưu nội dung, cấu hình và thông tin tài liệu nguồn cùng với kết quả AI tại thời điểm tạo. Việc thêm tài liệu, đổi tên Notebook hoặc thay mô hình không được tự làm thay đổi kết quả đã lưu. Hệ thống chỉ đánh dấu tác vụ thành công sau khi đầu ra đáp ứng cấu trúc và các ràng buộc của công cụ.

### BR-12: Kiểm soát xung đột khi cập nhật dữ liệu

Khi cập nhật ghi chú hoặc thông tin mô tả của tài nguyên, hệ thống phải kiểm tra phiên bản dữ liệu người dùng đang sửa. Nếu phiên bản này cũ hơn bản trên máy chủ, hệ thống phải từ chối cập nhật, thông báo xung đột và cho phép tải lại bản hiện hành. Hệ thống không được tự ghi đè thay đổi đã được lưu từ phiên khác.

### BR-13: Căn cứ của câu trả lời và nội dung AI

Mỗi phát biểu về dữ kiện được trình bày là lấy từ nguồn phải có nội dung nguồn hỗ trợ. Không được tạo số liệu, sự kiện hoặc kết luận thực tế không có trong nguồn để đáp ứng độ dài hay cấu trúc đầu ra. Phần suy luận, tổng hợp hoặc đề xuất được phép khi được phân biệt rõ với dữ kiện, nêu căn cứ và giới hạn; việc gắn nhãn không hợp thức hóa một dữ kiện bịa đặt. Mọi phát biểu không được nguồn hỗ trợ được phát hiện trong bộ nghiệm thu phải được xử lý là không đạt theo mục 12.2.

### BR-14: Quy tắc chấm điểm Quiz

Hệ thống tính điểm bằng số câu trả lời đúng chia cho tổng số câu của Quiz, quy đổi thành phần trăm và làm tròn đến một chữ số thập phân. Câu chưa trả lời được tính là sai. Đáp án và giải thích chỉ được hiển thị sau khi người dùng nộp bài.

### BR-15: Kiểm tra và thông báo giới hạn xử lý

Ứng dụng phải thông báo giới hạn trước khi thực hiện; khi vượt giới hạn phải từ chối có lý do. Không được tự cắt bớt nội dung tài liệu mà không thông báo, rồi trình bày kết quả như đã xử lý toàn bộ tài liệu.

### BR-16: Ngôn ngữ giao diện và nội dung

Giao diện và đầu ra AI mặc định là tiếng Việt; nhận tài liệu tiếng Việt và tiếng Anh. Thuật ngữ, tên riêng và số liệu nguồn phải được bảo toàn khi diễn đạt.

<a id="muc-5"></a>

## 5. Giới hạn xử lý và vòng đời dữ liệu

Bảng dưới quy định giới hạn đầu vào, thời hạn xử lý và mục tiêu vận hành của R1. Mọi thay đổi làm giảm khả năng đáp ứng hoặc nới điều kiện nghiệm thu phải được quản lý theo IH-REL-003.

| Mã và đối tượng | Giá trị và quy tắc |
| --- | --- |
| LIM-01 Tài khoản | Email tối đa 254 ký tự; tên hiển thị 1-80 ký tự; mật khẩu 15-128 ký tự Unicode, cho phép khoảng trắng, không cắt hoặc loại khoảng trắng ở đầu và cuối mật khẩu. |
| LIM-02 Notebook | Tối đa 20 Notebook đang hoạt động/người dùng; tên 1-120 ký tự; mô tả tối đa 1.000 ký tự. |
| LIM-03 Tệp | TXT/MD UTF-8 hoặc PDF có lớp văn bản; tối đa 10 MiB/tệp, PDF tối đa 100 trang; không nhận tệp mã hóa hoặc PDF chỉ có ảnh. |
| LIM-04 Kho tài liệu | Tối đa 20 tài liệu chưa xóa/Notebook; tối đa 200.000 ký tự văn bản trích xuất/tài liệu. Tệp `Failed` vẫn chiếm một vị trí cho tới khi xóa. |
| LIM-05 Đầu vào công cụ AI | 1-3 tài liệu `Ready` cùng Notebook; tổng tối đa 60.000 ký tự văn bản trích xuất; hướng dẫn bổ sung tối đa 1.000 ký tự. |
| LIM-06 Hỏi đáp và ghi chú | Câu hỏi 1-2.000 ký tự; tên hội thoại tối đa 120 ký tự; ghi chú có tiêu đề 1-120 ký tự và nội dung tối đa 20.000 ký tự. |
| LIM-07 Phiên | Phiên hết hạn sau 2 giờ không hoạt động hoặc tối đa 24 giờ từ lần đăng nhập/tái xác thực. Sau đổi hoặc đặt lại mật khẩu, phiên cũ bị thu hồi trong tối đa 60 giây. |
| LIM-08 Liên kết tài khoản | Liên kết đặt lại mật khẩu dùng một lần, hiệu lực tối đa 60 phút; liên kết xác minh email dùng một lần, hiệu lực tối đa 24 giờ. EML-003 là email thông báo, không phát hành liên kết xác thực. |
| LIM-09 Chống lạm dụng | Trong mỗi khoảng 15 phút: tổng tối đa 5 lần đăng nhập hoặc tái xác thực bằng mật khẩu sai cho một tài khoản và 20 lần cho một địa chỉ IP. Trong mỗi giờ: tối đa 3 yêu cầu gửi email cho một tài khoản và 20 yêu cầu cho một địa chỉ IP. Khi vượt giới hạn, tạm chặn thao tác tương ứng đến hết khoảng thời gian áp dụng; không khóa tài khoản vĩnh viễn. |
| LIM-10 Tác vụ AI | Mỗi người dùng có tối đa 1 tác vụ AI đang chạy; tối đa 10 yêu cầu AI mới/phút. Thao tác trùng mã không tính thành yêu cầu mới. |
| LIM-11 Thời hạn xử lý | Tiếp nhận và xử lý tài liệu: tối đa 120 giây/tệp. Hỏi đáp: tối đa 60 giây/lượt. Công cụ AI: tối đa 120 giây/lần. Tác vụ quá hạn phải chuyển sang `Failed`; không được công bố kết quả đến sau thời hạn. |
| LIM-12 Gửi lặp | Mã thao tác được giữ tối thiểu 24 giờ cho tải lên, hỏi đáp và công cụ AI. Cùng mã nhưng nội dung khác phải báo xung đột. |
| LIM-13 Xóa dữ liệu | Ngăn truy cập ngay sau xác nhận xóa; xóa vật lý tệp, nội dung trích xuất và chỉ mục trong tối đa 24 giờ. Sao lưu giữ tối đa 7 ngày, chỉ được đọc bởi người vận hành và khôi phục trong môi trường riêng để kiểm chứng. |
| LIM-14 Môi trường kiểm chứng | Một môi trường local hoặc sandbox; ghi cấu hình thực tế của máy, dịch vụ và phiên bản. Dùng 2 tài khoản, mỗi tài khoản có ít nhất 1 Notebook với 3 tài liệu TXT, MD và PDF có văn bản; bộ nguồn có tiếng Việt và tiếng Anh. Kiểm chứng nghiệp vụ tuần tự; các tình huống gửi đồng thời được kiểm riêng ở UAT-20. |
| LIM-15 Thời gian phản hồi | Với 10 thao tác nghiệp vụ không gọi AI được chọn trước theo mục 11.1, mỗi thao tác phải phản hồi trong tối đa 3 giây và không có lỗi kỹ thuật. Tài liệu, RAG và công cụ AI tuân theo thời hạn LIM-11; ghi thời gian ngay trong các lần kiểm chứng chức năng và chất lượng, không yêu cầu một đợt đo tải riêng. |
| LIM-16 Trình duyệt và kích thước | Một phiên bản ổn định của Chrome hoặc Edge được ghi rõ trong hồ sơ nghiệm thu; kiểm tra ở kích thước 1440 × 900 và 390 × 844 pixel CSS trên cùng trình duyệt. Đây là phạm vi kiểm chứng giao diện thích ứng; không xác lập hỗ trợ mọi trình duyệt hoặc hệ điều hành di động. |
| LIM-17 Kết quả AI | Tên kết quả AI 1-120 ký tự. Mindmap 10-30 nút, 2-4 cấp; Tóm tắt 150-250 hoặc 400-600 từ; Slide 5-8 trang; Quiz 5 hoặc 10 câu; Báo cáo 600-1.000 từ. |
| LIM-18 Lưu nhật ký | Nhật ký kỹ thuật giữ 30 ngày; không chứa mật khẩu, token, liên kết xác thực, toàn văn tài liệu hoặc chỉ dẫn cho mô hình có nội dung nguồn. |
| LIM-19 Tái xác thực | Bằng chứng xác nhận mật khẩu dùng cho đổi mật khẩu hoặc liên kết Google chỉ có hiệu lực trong đúng giao dịch và tài khoản tương ứng, tối đa 5 phút và dùng một lần. Phiên đăng nhập thông thường không thay thế bằng chứng này. |

MiB = 1.048.576 byte. Ký tự được đếm theo Unicode code point sau chuẩn hóa văn bản NFC, riêng mật khẩu giữ nguyên chuỗi nhập. “Từ” trong giới hạn nội dung AI là một đơn vị tách bằng khoảng trắng, chỉ tính phần nội dung, không tính danh sách tham chiếu nguồn.

### 5.1 Vòng đời tài liệu

| Trạng thái | Ý nghĩa | Chuyển tiếp hợp lệ |
| --- | --- | --- |
| `Processing` | Tệp đã được tiếp nhận và đang được kiểm tra, trích xuất văn bản hoặc lập chỉ mục. Chưa được sử dụng làm nguồn truy xuất. | `Ready`, `Failed` hoặc `Deleted`. |
| `Ready` | Văn bản và chỉ mục đã sẵn sàng, toàn bộ xử lý thành công. | `Deleted`. Muốn thay nội dung phải tải lên tài liệu mới. |
| `Failed` | Quá trình xử lý gặp lỗi hoặc vượt thời hạn. Hệ thống cung cấp mã lỗi và hướng dẫn bước tiếp theo. | `Processing` khi thử lại; `Deleted`. |
| `Deleted` | Đã xóa về nghiệp vụ, không còn được truy cập hoặc dùng làm nguồn. | Kết thúc. Xóa dữ liệu vật lý theo LIM-13. |

### 5.2 Trạng thái tác vụ AI, kết quả và dữ liệu liên quan

| Đối tượng | Trạng thái và hành vi |
| --- | --- |
| Tác vụ hỏi đáp hoặc công cụ AI | `Processing` → `Succeeded`, `NoEvidence` hoặc `Failed`. Khi nguồn hoặc Notebook bị xóa, quyền truy cập không còn hợp lệ hoặc tác vụ quá hạn, tác vụ phải kết thúc ở trạng thái `Failed` kèm mã lỗi phù hợp. |
| Câu trả lời | `Answered` phải có nội dung và tham chiếu nguồn hợp lệ. `NoEvidence` là kết quả nghiệp vụ không có câu trả lời khẳng định. `Failed` hiển thị lỗi, không ghi thành câu trả lời hợp lệ. |
| Kết quả AI | Chỉ `Succeeded` mới tạo kết quả AI. `NoEvidence` hoặc `Failed` giữ bản ghi tác vụ, không tạo sản phẩm nội dung thành công. |
| Notebook | `Active` → `Deleted`; ngăn truy cập các tài nguyên con tại thời điểm xóa thành công. |
| Ghi chú | Lưu bản hiện hành và số phiên bản để chống ghi đè; xóa là kết thúc, không có lịch sử phiên bản cho người dùng. |

### 5.3 Quy ước tên trạng thái

Tên trạng thái dưới đây là định danh dùng trong đặc tả và giao tiếp kỹ thuật. Giao diện phải hiển thị thông điệp tiếng Việt tương ứng.

| Định danh | Ý nghĩa |
| --- | --- |
| `PendingVerification` | Tài khoản đang chờ xác minh email. |
| `Active` | Tài khoản hoặc Notebook đang hoạt động. |
| `Processing` | Tài liệu hoặc tác vụ đang được xử lý. |
| `Ready` | Tài liệu đã xử lý thành công và được phép sử dụng làm nguồn. |
| `Succeeded` | Tác vụ AI đã tạo kết quả hợp lệ và hoàn tất thành công. |
| `Answered` | Lượt hỏi đáp đã có câu trả lời kèm tham chiếu nguồn hợp lệ. |
| `NoEvidence` | Nguồn không đủ căn cứ để trả lời hoặc tạo nội dung theo yêu cầu; không phải lỗi kỹ thuật. |
| `Failed` | Xử lý thất bại do lỗi, hết thời hạn hoặc điều kiện truy cập không còn hợp lệ. |
| `Deleted` | Tài nguyên đã bị xóa về nghiệp vụ và không còn được truy cập. |

### 5.4 Trạng thái tài khoản, phiên đăng nhập và liên kết xác thực

| Đối tượng | Sự kiện hợp lệ | Trạng thái và điều kiện sau xử lý |
| --- | --- | --- |
| Tài khoản mới bằng email | Đăng ký hợp lệ, email chưa có tài khoản. | Tạo `PendingVerification`; chỉ dùng các luồng xác minh, khôi phục mật khẩu hoặc đăng xuất; không dùng dữ liệu Notebook. |
| Tài khoản chờ xác minh | Xác minh đăng ký qua UC-01 hoặc hoàn tất đặt lại mật khẩu qua UC-02.A4. | UC-01 kích hoạt đăng ký thông thường. Nhánh xử lý email trùng khi đăng nhập Google bắt buộc theo BR-03: UC-02.A4 thay mật khẩu cũ, vô hiệu phiên và liên kết cũ rồi chuyển `Active`; chưa liên kết Google hoặc cấp phiên. |
| Tài khoản Google mới | Danh tính và email đã được Google xác minh; không còn xung đột danh tính chưa được giải quyết. | Tạo `Active`, cấp phiên sau kiểm chứng; trường hợp trùng email phải tuân thủ BR-03. |
| Phiên hạn chế chờ xác minh | Đúng thông tin đăng nhập nhưng tài khoản chưa `Active`. | Chỉ xem trạng thái xác minh, gửi lại hoặc đăng xuất; không coi là phiên nghiệp vụ hợp lệ. |
| Phiên truy cập | Đăng nhập thành công tài khoản `Active`. | Có hiệu lực đến khi hết hạn hoặc thu hồi theo LIM-07. Việc giữ phiên hạn chế và phiên truy cập phải phân biệt được ở phía máy chủ. |
| Liên kết xác minh email hoặc đặt lại mật khẩu | Mở liên kết hợp lệ và hoàn thành hành động tương ứng. | Chỉ dùng một lần cho đúng mục đích; liên kết hết hạn hoặc đã sử dụng không được làm thay đổi dữ liệu. Gửi lại theo mục 9.4. |

Trong R1, đổi mật khẩu và liên kết Google yêu cầu xác nhận mật khẩu hiện tại theo LIM-19; tài khoản chỉ dùng Google không có chức năng đổi mật khẩu ứng dụng. Khôi phục mật khẩu dùng liên kết hợp lệ làm bằng chứng kiểm soát email. Xác nhận xóa dữ liệu không yêu cầu nhập lại mật khẩu. Khi tiếp nhận tài khoản chờ xác minh qua nhánh BR-03, phải vô hiệu thông tin xác thực cũ trước khi tài khoản có thể truy cập dữ liệu; liên kết xác minh hoặc khôi phục cũ không được mở lại quyền sau bước này.

R1 không có trạng thái khóa tài khoản vĩnh viễn hoặc vai trò quản trị tài khoản trong ứng dụng. Các trường hợp tài khoản dịch vụ bị nhà cung cấp đình chỉ phải được từ chối truy cập và xử lý như sự cố tích hợp, không bỏ qua kiểm chứng danh tính.

### 5.5 Căn cứ lựa chọn giới hạn và điều kiện xác nhận

Các giá trị trong LIM là giới hạn đề xuất của R1, chưa phải kết quả đo hiệu năng hoặc cam kết của nhà cung cấp. Bảng này xác định lý do chọn và bằng chứng cần có; dữ liệu đo chi tiết được lưu cùng hồ sơ kỹ thuật, không chép lại vào SRS.

| Nhóm giới hạn | Căn cứ lựa chọn | Bằng chứng và người xác nhận |
| --- | --- | --- |
| LIM-01, LIM-07 đến LIM-09, LIM-19 | Bảo vệ tài khoản và xác định rõ đầu vào, thời hạn, thu hồi phiên và chống lạm dụng. Đây là chính sách sản phẩm; không coi giá trị mặc định của thư viện là đã đáp ứng. | Nhóm kỹ thuật đối chiếu khả năng dịch vụ xác thực và kiểm các luồng công khai, liên kết Google, hết hạn và thu hồi trước khi tích hợp Auth. Chủ sản phẩm quyết định nếu cần đổi chính sách. |
| LIM-02 đến LIM-06, LIM-17 | Giới hạn quy mô ứng dụng cá nhân và đầu ra có thể đọc, kiểm tra trong một phiên sử dụng; tránh nhận đầu vào vượt khả năng xử lý. | Nhóm kỹ thuật kiểm bộ tệp hợp lệ, biên đầu vào và cấu trúc đầu ra. Trước khi phát triển công cụ AI, thử một đầu vào sát LIM-05 bằng mô hình dự kiến, ghi ngôn ngữ, số token thực tế, giới hạn ngữ cảnh, thời gian và mức sử dụng dịch vụ. Không quy đổi cố định ký tự sang token. |
| LIM-10 đến LIM-12 | Một tác vụ AI/người dùng để hạn chế chi phí và tránh thao tác trùng; thời hạn hữu hạn để giao diện có kết quả hoặc hướng thử lại rõ ràng. | Kiểm cơ chế đồng thời và gửi lặp bằng kiểm thử tự động; dùng mô hình thực cho luồng thành công, giả lập cho quá hạn. Nhóm kỹ thuật xác nhận trước khi hoàn tất tích hợp. |
| LIM-13, LIM-18 | Xóa có thời hạn, giới hạn dữ liệu còn trong bản sao lưu và giữ đủ nhật ký cho việc đối soát của R1. | Người vận hành ghi cách dọn dữ liệu, sao lưu thủ công và xóa bản hết hạn; có một lần khôi phục riêng và kiểm tra nhật ký trước bàn giao. Không yêu cầu hệ thống lập lịch riêng. |
| LIM-14 đến LIM-16 | Cấu hình kiểm chứng nhỏ, có hai chủ sở hữu để kiểm cách ly; hai kích thước màn hình để kiểm giao diện thích ứng. Ngưỡng 3 giây là mục tiêu sử dụng đề xuất, không phải số đo đã đạt. | Ghi cấu hình máy, trình duyệt, dữ liệu và kết quả UAT-15, UAT-17. Chủ sản phẩm xác nhận phạm vi kiểm chứng trước nghiệm thu. |

Trạng thái hiện tại: các giới hạn đã có căn cứ đề xuất, nhưng cấu hình nhà cung cấp, phép thử đầu vào AI, Figma và kết quả chạy phần mềm chưa được xác nhận trong tài liệu này. Các điểm còn mở được hoàn tất theo mục 14.3. Nếu thử nghiệm cho thấy giới hạn không khả thi, nhóm dự án điều chỉnh giải pháp hoặc trình thay đổi theo IH-REL-003 trước khi triển khai phụ thuộc; không chờ đến nghiệm thu mới giảm ngưỡng.

<a id="muc-6"></a>

## 6. Đặc tả ca sử dụng

Các ca sử dụng mô tả mục tiêu của người dùng hoặc người vận hành, dữ liệu trao đổi và phản hồi của InsightHub. Mỗi ca sử dụng có luồng chính, các luồng thay thế và ngoại lệ. Mỗi nhánh xác định điều kiện phát sinh, cách xử lý và bước tiếp tục hoặc kết thúc.

<a id="uc-catalog"></a>

### 6.1 Danh mục ca sử dụng và quy ước mô tả

| Mã | Mục tiêu của tác nhân | Tác nhân chính | Kết quả thành công |
| --- | --- | --- | --- |
| [UC-01](#uc-01) | Đăng ký tài khoản và xác minh email | Người chưa đăng nhập | Có tài khoản đã xác minh để đăng nhập. |
| [UC-02](#uc-02) | Khôi phục mật khẩu | Người dùng quên mật khẩu | Đặt được mật khẩu mới và vô hiệu hóa các phiên cũ. |
| [UC-03](#uc-03) | Quản lý Notebook | Người dùng đã đăng nhập | Tạo, mở, cập nhật hoặc xóa đúng Notebook của mình. |
| [UC-04](#uc-04) | Tải lên và quản lý tài liệu | Người dùng đã đăng nhập | Tài liệu hợp lệ được xử lý, truy xuất và quản lý trong Notebook. |
| [UC-05](#uc-05) | Hỏi đáp từ tài liệu và xem nguồn tham chiếu | Người dùng đã đăng nhập | Có câu trả lời kèm nguồn hoặc kết luận thiếu căn cứ rõ ràng. |
| [UC-06](#uc-06) | Quản lý ghi chú | Người dùng đã đăng nhập | Lưu được ghi chú độc lập và quản lý nội dung đã lưu. |
| [UC-07](#uc-07) | Tạo nội dung từ tài liệu bằng công cụ AI | Người dùng đã đăng nhập | Có kết quả đúng loại của từng công cụ trong danh mục bắt buộc. |
| [UC-08](#uc-08) | Xem và quản lý kết quả AI | Người dùng đã đăng nhập | Đọc, sử dụng hoặc quản lý đúng kết quả đã lưu. |
| [UC-09](#uc-09) | Kiểm chứng khôi phục bản sao lưu | Người vận hành | Bản sao lưu được khôi phục vào môi trường riêng, đúng nội dung và quyền tại thời điểm sao lưu; không thay dữ liệu đang phục vụ. |
| [UC-10](#uc-10) | Đăng nhập bằng email và mật khẩu | Người chưa đăng nhập | Có phiên hợp lệ của đúng tài khoản. |
| [UC-11](#uc-11) | Đăng nhập và liên kết tài khoản Google | Người chưa đăng nhập | Có phiên hợp lệ; liên kết danh tính chỉ sau khi xác minh đúng quyền. |
| [UC-12](#uc-12) | Xem và cập nhật hồ sơ cá nhân | Người dùng đã đăng nhập | Lưu được tên và lựa chọn ảnh đại diện trong phạm vi cho phép. |
| [UC-13](#uc-13) | Đổi mật khẩu | Người dùng có mật khẩu | Mật khẩu được đổi sau tái xác thực; các phiên cũ bị thu hồi. |
| [UC-14](#uc-14) | Đăng xuất | Người dùng đang có phiên | Phiên không còn được dùng để truy cập dữ liệu. |
| [UC-15](#uc-15) | Cài đặt và cấu hình môi trường | Người vận hành | Cài đặt và kiểm tra được một môi trường sẵn sàng. |
| [UC-16](#uc-16) | Sao lưu dữ liệu | Người vận hành | Có bản sao lưu hợp lệ cùng thông tin để lựa chọn khi phục hồi. |

- Tất cả ca sử dụng trong danh mục thuộc phạm vi R1.
- `M1`, `M2` là bước trong luồng chính. `A1`, `A2` là nhánh thay thế hoặc lựa chọn hợp lệ; `E1`, `E2` là ngoại lệ. Khi ghi đầy đủ, dùng dạng `UC-04.M3` hoặc `UC-04.E2`.
- Một nhánh phải ghi rõ bước phát sinh, điều kiện, phản hồi của hệ thống và điểm quay lại hoặc kết thúc. “Kết thúc thất bại” nghĩa là mục tiêu chưa đạt; hệ thống vẫn phải giữ bảo đảm tối thiểu của ca sử dụng.
- “Người dùng đã đăng nhập” trong các ca sử dụng dữ liệu nghĩa là tài khoản `Active` có phiên còn hiệu lực. Quyền với tài nguyên phải được kiểm tra lại khi xử lý, kể cả khi tiền điều kiện đã thỏa mãn lúc mở màn hình.
- Các mã `MSG-*` và `EML-*` tham chiếu danh mục ở mục 9.1 đến 9.5. Chúng là định danh thông báo, không phải mã trạng thái HTTP.
- Mã yêu cầu IH và tiêu chí AC vẫn là đơn vị kiểm chứng. Test case phải ghi ca sử dụng, bước hoặc nhánh được đi qua và AC liên quan; không chỉ kiểm luồng chính.

### 6.2 Quy tắc xử lý các tình huống dùng chung

Các tình huống sau chỉ áp dụng tại điểm xử lý được chỉ ra trong từng ca. Chúng không làm thay đổi tiền điều kiện của ca công khai như đăng ký hoặc yêu cầu khôi phục mật khẩu.

| Mã | Điều kiện phát sinh | Xử lý và điểm tiếp tục |
| --- | --- | --- |
| CF-01 | Phiên không còn hiệu lực khi thực hiện thao tác cần đăng nhập. | Hệ thống từ chối yêu cầu mới, xóa dữ liệu cá nhân khỏi bộ nhớ giao diện và hiển thị MSG-AUTH-012. Thao tác hiện tại kết thúc. Sau khi đăng nhập lại, người dùng mở lại tài nguyên; hệ thống không tự gửi lại thao tác thay đổi dữ liệu hoặc gọi AI. |
| CF-02 | Tài nguyên không tồn tại, đã xóa hoặc không thuộc quyền tại bước kiểm tra hay trước khi công bố kết quả. | Hệ thống hiển thị MSG-DATA-010 với cùng nội dung công khai cho các trường hợp không được truy cập. Hệ thống không tiết lộ nội dung hoặc thông tin mô tả của tài nguyên, không thay đổi dữ liệu và kết thúc thao tác thất bại. |
| CF-03 | Dữ liệu nhập không đáp ứng BR hoặc LIM tại bước xác nhận đầu vào. | Hệ thống hiển thị MSG-DATA-001 cạnh trường hoặc nhóm dữ liệu có lỗi và giữ các giá trị hợp lệ; mật khẩu không được lưu vào bộ nhớ bền vững. Người dùng quay lại bước nhập tương ứng. Hệ thống chưa thực hiện thay đổi nghiệp vụ. |
| CF-04 | Mất kết nối sau khi gửi yêu cầu, chưa xác định được kết quả trên máy chủ. | Hệ thống hiển thị MSG-SYS-001 và chưa xác nhận thao tác thành công hay thất bại. Với tải tài liệu, hỏi đáp và công cụ AI, ứng dụng tra cứu hoặc gửi lại cùng mã thao tác trong thời hạn LIM-12. Với thao tác khác, ứng dụng đọc lại trạng thái tài nguyên trước khi cho tiếp tục. Sau khi xác định được kết quả, hệ thống chuyển đến bước hiển thị kết quả tương ứng. |
| CF-05 | Phiên bản dữ liệu người dùng đang sửa cũ hơn bản trên máy chủ. | Hệ thống hiển thị MSG-DATA-003 và từ chối ghi đè. Người dùng có thể tải bản hiện hành để thực hiện lại thay đổi hoặc hủy thao tác. Hệ thống không tự hợp nhất nội dung. |
| CF-06 | Vượt giới hạn tần suất hoặc đang có tác vụ AI chưa kết thúc. | Hệ thống hiển thị MSG-AUTH-006 hoặc MSG-AI-006 theo nguyên nhân và không tạo tác vụ mới. Người dùng chờ hết thời gian giới hạn được thông báo hoặc mở tác vụ đang xử lý. |
| CF-07 | Người dùng tải lại trang, đóng trang hoặc chuyển Notebook trong lúc máy chủ đã nhận tác vụ. | Tác vụ tiếp tục trong thời hạn LIM-11; việc rời trang không được xem là yêu cầu hủy. Khi người dùng mở lại, hệ thống kiểm tra quyền và đọc trạng thái đã lưu, không tạo tác vụ mới. Nếu nguồn hoặc Notebook bị xóa, hoặc quyền truy cập không còn hợp lệ, hệ thống áp dụng quy tắc tương ứng. |
| CF-08 | Gửi email giao dịch gặp lỗi hoặc chưa biết nhà cung cấp đã nhận yêu cầu hay chưa. | Hệ thống phản hồi theo quy tắc hạn chế dò tìm tài khoản và không xác nhận email đã đến hộp thư. Trạng thái gửi được ghi nhận để người vận hành kiểm tra. Yêu cầu gửi lại phải tuân thủ LIM-09; lỗi gửi email không làm thay đổi trạng thái tài khoản. Quy tắc chi tiết được nêu tại mục 9.4. |

<a id="uc-01"></a>

### UC-01: Đăng ký tài khoản và xác minh email

- **Mục tiêu:** Người dùng tạo tài khoản có email đã xác minh để truy cập InsightHub.
- **Tác nhân:** Người chưa đăng nhập; dịch vụ xác thực và dịch vụ email hỗ trợ.
- **Kích hoạt:** Người dùng chọn đăng ký bằng email và mật khẩu.
- **Tiền điều kiện:** Có địa chỉ email có thể nhận thư; ứng dụng cho phép tiếp nhận đăng ký. Người dùng chưa cần có tài khoản.
- **Dữ liệu đầu vào:** Người dùng cung cấp địa chỉ email, tên hiển thị, mật khẩu và mật khẩu xác nhận; liên kết xác minh được sử dụng ở bước xác minh email.
- **Kết quả đầu ra:** Hệ thống trả trạng thái tiếp nhận đăng ký, gửi email EML-001 khi đủ điều kiện và xác nhận tài khoản đã được kích hoạt sau khi xác minh thành công.
- **Hậu điều kiện thành công:** Tài khoản chuyển từ `PendingVerification` sang `Active`; người dùng có thể đăng nhập bằng UC-10. Luồng xác minh không tự mở dữ liệu của người khác.
- **Bảo đảm tối thiểu:** Không tạo trùng email chuẩn hóa; không cấp quyền dữ liệu trước xác minh; mật khẩu và liên kết xác minh không xuất hiện trong nhật ký hoặc thông báo công khai.

**Luồng chính**

| Bước | Tương tác |
| --- | --- |
| M1 | Hệ thống hiển thị dữ liệu đăng ký cần nhập và giới hạn LIM-01. |
| M2 | Người dùng nhập email, tên hiển thị, mật khẩu và xác nhận mật khẩu, sau đó gửi đăng ký. |
| M3 | Hệ thống kiểm tra dữ liệu, chuẩn hóa email theo BR-02 và kiểm tra điều kiện tạo tài khoản. |
| M4 | Hệ thống tạo đúng một tài khoản `PendingVerification`, tạo yêu cầu xác minh có thời hạn LIM-08 và gửi EML-001. |
| M5 | Hệ thống hiển thị MSG-AUTH-002; người dùng mở email và chọn liên kết xác minh. |
| M6 | Hệ thống xác minh tính hợp lệ, thời hạn và tính dùng một lần của liên kết, sau đó kích hoạt đúng tài khoản. |
| M7 | Hệ thống hiển thị MSG-AUTH-004 và cung cấp thao tác đăng nhập. Ca sử dụng kết thúc thành công. |

**Luồng thay thế và ngoại lệ**

| Nhánh | Điểm phát sinh | Xử lý và điểm kết thúc hoặc quay lại |
| --- | --- | --- |
| A1 | M5: người dùng chưa nhận được thư hoặc muốn gửi lại. | Tiếp nhận yêu cầu gửi lại theo LIM-09; chỉ phát hành liên kết mới cho tài khoản còn chờ xác minh; liên kết cũ chưa sử dụng bị vô hiệu khi liên kết mới được phát hành thành công. Hiển thị phản hồi cùng ý nghĩa MSG-AUTH-002; quay lại M5. |
| A2 | M3: email đã gắn với một tài khoản. | Không tạo tài khoản mới hoặc cấp phiên. Phản hồi công khai không xác nhận email đã tồn tại; cung cấp cùng hướng kiểm tra email, đăng nhập hoặc khôi phục mật khẩu. Kết thúc mà không thay đổi tài khoản hiện hữu. |
| E1 | M3: dữ liệu sai hoặc hai mật khẩu không khớp. | Hệ thống xử lý theo CF-03; quay lại M2. |
| E2 | M4 hoặc A1: lỗi gửi email. | Hệ thống xử lý theo CF-08. Tài khoản chưa xác minh không được kích hoạt; người dùng có thể gửi lại theo A1. |
| E3 | M6: liên kết sai, hết hạn hoặc đã dùng. | Không thay đổi trạng thái tài khoản; hiển thị MSG-AUTH-005. Người dùng gửi lại theo A1 hoặc đăng nhập nếu trước đó đã xác minh; luồng xác minh hiện tại kết thúc. |
| E4 | M4 hoặc A1: vượt giới hạn gửi. | Hệ thống xử lý theo CF-06; không gửi thêm email. Người dùng có thể thử lại sau thời gian chờ. |

**Truy vết:** IH-AUTH-001, IH-AUTH-002, IH-AUTH-008, IH-DATA-001, IH-UX-001, IH-UX-002, IH-UX-003, IH-UX-004, IH-MSG-001, IH-MSG-002, IH-MSG-003, IH-INT-001, IH-INT-003, IH-NFR-001, IH-NFR-011, IH-REL-001; BR-02; LIM-01, LIM-08, LIM-09; UAT-01, UAT-18, UAT-19.

<a id="uc-02"></a>

### UC-02: Khôi phục mật khẩu

- **Mục tiêu:** Đặt lại mật khẩu khi người dùng không còn nhớ mật khẩu hiện tại.
- **Tác nhân:** Người dùng quên mật khẩu; dịch vụ xác thực và dịch vụ email hỗ trợ.
- **Kích hoạt:** Người dùng chọn khôi phục mật khẩu.
- **Tiền điều kiện:** Luồng tiếp nhận không yêu cầu đăng nhập. Luồng thành công cần tài khoản có mật khẩu và quyền truy cập email nhận liên kết.
- **Dữ liệu đầu vào:** Người dùng cung cấp địa chỉ email, liên kết khôi phục và mật khẩu mới kèm mật khẩu xác nhận.
- **Kết quả đầu ra:** Hệ thống trả phản hồi tiếp nhận yêu cầu, kết quả đặt lại mật khẩu và trạng thái thu hồi phiên; gửi EML-002 và EML-005 theo sự kiện tương ứng.
- **Hậu điều kiện thành công:** Mật khẩu mới có hiệu lực; liên kết đã dùng không dùng lại được; phiên cũ bị thu hồi theo LIM-07; người dùng phải đăng nhập lại. Với tài khoản chờ xác minh, áp dụng thêm A4 trước khi cấp quyền nghiệp vụ.
- **Bảo đảm tối thiểu:** Phản hồi công khai không tiết lộ tài khoản tồn tại; mật khẩu chưa thay đổi nếu liên kết hoặc dữ liệu không hợp lệ; lỗi gửi email không khóa tài khoản vĩnh viễn.

**Luồng chính**

| Bước | Tương tác |
| --- | --- |
| M1 | Người dùng nhập email và gửi yêu cầu khôi phục. |
| M2 | Hệ thống kiểm tra định dạng, giới hạn gửi và tiếp nhận yêu cầu; hiển thị MSG-AUTH-010. |
| M3 | Với tài khoản có mật khẩu, hệ thống phát hành liên kết dùng một lần theo LIM-08 và gửi EML-002. |
| M4 | Người dùng mở liên kết. Hệ thống xác minh liên kết rồi hiển thị yêu cầu nhập mật khẩu mới và xác nhận. |
| M5 | Người dùng nhập và gửi hai giá trị. Hệ thống kiểm tra LIM-01 và sự trùng khớp. |
| M6 | Hệ thống cập nhật mật khẩu, tiêu thụ liên kết và thu hồi phiên cũ theo LIM-07; không tự tạo phiên đăng nhập mới. |
| M7 | Hệ thống hiển thị MSG-AUTH-011 và gửi EML-005 tới email đã xác minh. Người dùng chuyển sang UC-10; ca sử dụng kết thúc thành công. |

**Luồng thay thế và ngoại lệ**

| Nhánh | Điểm phát sinh | Xử lý và điểm kết thúc hoặc quay lại |
| --- | --- | --- |
| A1 | M3: email không có tài khoản. | Không gửi liên kết đặt lại mật khẩu; vẫn giữ phản hồi công khai MSG-AUTH-010 và kết thúc tiếp nhận. Không tạo tài khoản hoặc dấu hiệu khác biệt về tồn tại tài khoản. |
| A2 | M3: tài khoản chỉ đăng nhập bằng Google. | Gửi EML-004 hướng dẫn đăng nhập Google; giữ phản hồi công khai như M2; không tự thêm mật khẩu. Kết thúc; người dùng có thể thực hiện UC-11. |
| A3 | M1: người dùng gửi yêu cầu khôi phục mới. | Áp dụng LIM-09. Khi phát hành liên kết mới thành công, vô hiệu liên kết cũ chưa sử dụng; quay lại M3. Quy tắc này phải nhất quán với gửi lại xác minh ở UC-01.A1. |
| A4 | M3-M6: tài khoản có mật khẩu còn `PendingVerification`, gồm trường hợp từ UC-11.A2. | Chỉ liên kết đặt lại hợp lệ gửi tới email của tài khoản mới được dùng làm bằng chứng. Tại M6, thay mật khẩu, vô hiệu tất cả phiên hạn chế và liên kết xác minh/khôi phục cũ, sau đó chuyển tài khoản sang `Active`; không cấp phiên hoặc tự liên kết Google. Nếu không hoàn tất được việc vô hiệu, giữ chặn truy cập và báo lỗi để thử lại. Tại M7, người dùng có thể đăng nhập UC-10 hoặc bắt đầu lại UC-11 để xác nhận mật khẩu mới. |
| E1 | M4: liên kết sai, hết hạn hoặc đã dùng. | Hiển thị MSG-AUTH-005; không đổi mật khẩu; kết thúc luồng liên kết. Người dùng có thể bắt đầu lại M1. |
| E2 | M5: mật khẩu không hợp lệ hoặc xác nhận không khớp. | Hệ thống xử lý theo CF-03; quay lại M5 nếu liên kết còn hiệu lực. |
| E3 | M2 hoặc M3: vượt giới hạn, lỗi hoặc chưa xác định kết quả gửi. | Hệ thống xử lý theo CF-06 hoặc CF-08. Không đổi mật khẩu; giữ cùng ý nghĩa phản hồi cho email có và không có tài khoản. |
| E4 | M6: cập nhật không hoàn tất. | Không thông báo đổi mật khẩu thành công. Nếu kết quả chưa rõ, hiển thị MSG-SYS-001 và xác định lại trạng thái liên kết; không tự thực hiện lần đổi thứ hai. Nếu thất bại đã xác định, giữ mật khẩu cũ và cho bắt đầu lại. |
| E5 | M7: gửi EML-005 thất bại sau khi mật khẩu đã đổi. | Giữ kết quả đổi mật khẩu và thu hồi phiên; ghi lỗi gửi, xử lý theo mục 9.4. Không yêu cầu đổi mật khẩu lại để gửi thư. |

**Truy vết:** IH-AUTH-005, IH-AUTH-006, IH-AUTH-007, IH-AUTH-008, IH-UX-001, IH-UX-002, IH-UX-003, IH-UX-004, IH-MSG-001, IH-MSG-002, IH-MSG-003, IH-INT-001, IH-INT-003, IH-NFR-001, IH-NFR-011, IH-REL-001; LIM-01, LIM-07, LIM-08, LIM-09; UAT-03, UAT-18, UAT-19.

<a id="uc-03"></a>

### UC-03: Quản lý Notebook

- **Mục tiêu:** Tạo và duy trì Notebook để tổ chức dữ liệu của mình.
- **Tác nhân:** Người dùng đã đăng nhập.
- **Kích hoạt:** Người dùng mở danh sách Notebook hoặc chọn tạo, mở, cập nhật hay xóa một Notebook.
- **Tiền điều kiện:** Tài khoản `Active`, phiên hợp lệ; thao tác trên Notebook hiện hữu yêu cầu quyền sở hữu.
- **Dữ liệu đầu vào:** Người dùng cung cấp tên và mô tả khi tạo hoặc sửa Notebook; thao tác với Notebook đã có sử dụng định danh và phiên bản hiện hành.
- **Kết quả đầu ra:** Hệ thống trả danh sách Notebook có phân trang, thông tin Notebook đã lưu và kết quả tạo, cập nhật hoặc xóa.
- **Hậu điều kiện thành công:** Tạo: có Notebook mới với định danh và chủ sở hữu đúng. Mở: chỉ đọc dữ liệu thuộc quyền. Cập nhật: tên hoặc mô tả mới được lưu và tăng phiên bản. Xóa: Notebook và tài nguyên con bị chặn truy cập theo BR-09, không còn trong danh sách hoạt động.
- **Bảo đảm tối thiểu:** Lỗi hoặc hủy không làm mất dữ liệu; không sửa tài nguyên của người khác; xóa phải bao phủ tài nguyên con theo BR-09.

**Luồng chính**

| Bước | Tương tác |
| --- | --- |
| M1 | Hệ thống đọc và hiển thị danh sách Notebook thuộc người dùng, sắp xếp mới nhất và phân trang. |
| M2 | Người dùng chọn tạo, nhập tên và mô tả theo LIM-02. |
| M3 | Hệ thống kiểm tra phiên, dữ liệu và số lượng Notebook đang hoạt động. |
| M4 | Hệ thống tạo Notebook, xác định chủ sở hữu từ phiên và lưu định danh, phiên bản, thời điểm. |
| M5 | Hệ thống hiển thị MSG-DATA-002 và mở Notebook vừa tạo; ca sử dụng kết thúc thành công. |

**Luồng thay thế và ngoại lệ**

| Nhánh | Điểm phát sinh | Xử lý và điểm kết thúc hoặc quay lại |
| --- | --- | --- |
| A1 | M1: người dùng chọn Notebook đã có hoặc trang danh sách khác. | Kiểm tra quyền, đọc đúng tài liệu, hội thoại, ghi chú và kết quả AI của Notebook. Kết thúc tại màn hình Notebook hoặc danh sách đã chọn; không tạo dữ liệu mới. |
| A2 | A1: người dùng sửa tên hoặc mô tả. | Nhận dữ liệu và số phiên bản; kiểm tra quyền, LIM-02 và BR-12; lưu thay đổi, hiển thị MSG-DATA-002 rồi kết thúc. Định danh nguồn và nội dung kết quả AI không đổi. |
| A3 | A1: người dùng chọn xóa. | Hiển thị MSG-DATA-004 nêu rõ toàn bộ tài liệu, hội thoại, ghi chú, kết quả AI và lần làm Quiz sẽ mất. Nếu xác nhận, kiểm tra lại quyền, xóa về nghiệp vụ, chặn tác vụ ghi lại dữ liệu, xóa dữ liệu vật lý theo LIM-13; hiển thị MSG-DATA-009 và kết thúc ở danh sách. Nếu hủy, trở về A1 và giữ dữ liệu. |
| E1 | M3 hoặc A2: tên không hợp lệ, vượt số lượng hoặc xung đột phiên bản. | Hệ thống xử lý theo CF-03 hoặc CF-05; quay về bước nhập tương ứng. |
| E2 | M1, M3, A1, A2 hoặc A3: phiên hoặc quyền không còn hợp lệ. | Hệ thống xử lý theo CF-01 hoặc CF-02; kết thúc thao tác mà không công bố dữ liệu trái quyền. |
| E3 | M4, A2 hoặc A3: phản hồi bị mất sau khi gửi. | Hệ thống xử lý theo CF-04; đọc lại Notebook hoặc danh sách trước khi cho gửi tiếp, không hiển thị thành công khi chưa xác định trạng thái. |

**Truy vết:** IH-NB-001, IH-NB-002, IH-NB-003, IH-NB-004, IH-DATA-001, IH-DATA-002, IH-UX-001, IH-UX-002, IH-UX-003, IH-UX-004, IH-MSG-001, IH-MSG-002, IH-INT-001, IH-INT-004, IH-NFR-002, IH-NFR-004, IH-NFR-006, IH-REL-001; BR-01, BR-09, BR-12; LIM-02, LIM-13; UAT-05, UAT-12, UAT-13, UAT-18.

<a id="uc-04"></a>

### UC-04: Tải lên và quản lý tài liệu

- **Mục tiêu:** Nạp tài liệu hợp lệ để dùng trong hỏi đáp và công cụ AI.
- **Tác nhân:** Người dùng đã đăng nhập; dịch vụ embedding và lưu trữ hỗ trợ.
- **Kích hoạt:** Người dùng chọn tải tài liệu vào Notebook.
- **Tiền điều kiện:** Tài khoản có phiên hợp lệ và Notebook đang hoạt động thuộc người dùng. Riêng tải mới cần tệp và số lượng đáp ứng LIM-03, LIM-04; xem, thử lại hoặc xóa áp dụng điều kiện của nhánh tương ứng.
- **Dữ liệu đầu vào:** Người dùng tải lên tệp TXT, MD hoặc PDF có lớp văn bản trong Notebook đã chọn. Yêu cầu tải lên có mã thao tác để kiểm soát việc gửi lặp.
- **Kết quả đầu ra:** Hệ thống trả định danh tài liệu, trạng thái xử lý, văn bản trích xuất và vị trí nguồn; nếu xử lý thất bại, hệ thống cung cấp lý do lỗi và hướng xử lý.
- **Hậu điều kiện thành công:** Tải hoặc thử lại: tài liệu `Ready` có văn bản, vị trí nguồn và chỉ mục đầy đủ. Xem: đọc đúng nội dung thuộc quyền. Xóa: tài liệu không còn dùng làm nguồn, tác vụ và tham chiếu được xử lý theo BR-08.
- **Bảo đảm tối thiểu:** Tài liệu lỗi hoặc xử lý dở không tham gia truy xuất; không tạo trùng do gửi lại; nguồn đã xóa không được dùng hoặc xuất hiện lại.

**Luồng chính**

| Bước | Tương tác |
| --- | --- |
| M1 | Hệ thống hiển thị định dạng, dung lượng, số trang và giới hạn kho tài liệu áp dụng. |
| M2 | Người dùng chọn tệp và gửi tải lên với một mã thao tác. |
| M3 | Hệ thống kiểm tra phiên, quyền, định dạng thực, kích thước, số lượng và nội dung trùng. |
| M4 | Hệ thống tạo bản ghi `Processing`, lưu tên, loại, kích thước; hiển thị MSG-DOC-001. |
| M5 | Hệ thống trích xuất văn bản và vị trí nguồn, kiểm tra giới hạn văn bản, tạo embedding và lập chỉ mục trong LIM-11. |
| M6 | Sau khi toàn bộ xử lý hoàn tất và quyền, nguồn còn hợp lệ, hệ thống chuyển tài liệu sang `Ready`. |
| M7 | Hệ thống hiển thị MSG-DOC-002; người dùng xem văn bản cùng số trang hoặc chỉ số đoạn. Ca sử dụng kết thúc thành công. |

**Luồng thay thế và ngoại lệ**

| Nhánh | Điểm phát sinh | Xử lý và điểm kết thúc hoặc quay lại |
| --- | --- | --- |
| A1 | M3: tệp trùng byte với tài liệu chưa xóa trong cùng Notebook. | Không tạo bản thứ hai; hiển thị MSG-DOC-004 và liên kết tài liệu hiện hữu sau kiểm tra quyền. Kết thúc ở tài liệu đó. Tệp ở Notebook khác vẫn là nguồn độc lập. |
| A2 | M4 hoặc M5: người dùng tải lại trang, rời trang hoặc gửi lặp. | Hệ thống xử lý theo CF-04, CF-07 và LIM-12; trả trạng thái của cùng thao tác, không nhân đôi tài liệu hoặc đoạn văn bản. Tiếp tục theo trạng thái đã lưu. |
| A3 | M7 hoặc từ tham chiếu nguồn ở UC-05 hoặc UC-08: người dùng mở tài liệu. | Kiểm tra quyền tại thời điểm đọc; hiển thị tên, loại, thời điểm, trạng thái, văn bản và đúng vị trí trang hoặc đoạn. Kết thúc thao tác xem; nếu mở từ tham chiếu, cho quay về kết quả ban đầu. |
| A4 | Tài liệu `Failed`: người dùng chọn thử lại. | Kiểm tra nguồn, quyền và điều kiện đầu vào còn hợp lệ; tạo lần xử lý mới cho cùng tài liệu, không nhân đôi chỉ mục; quay lại M4. Nếu lỗi đầu vào không thể sửa bằng thử lại, hướng dẫn thay tệp. |
| A5 | M4, M5 hoặc M7: người dùng chọn xóa. | Hiển thị MSG-DATA-005. Khi xác nhận, kiểm tra quyền và xóa về nghiệp vụ; tác vụ đang dùng nguồn chuyển `Failed`, xóa dữ liệu vật lý theo LIM-13. Kết quả đã lưu giữ nội dung và đánh dấu nguồn đã xóa. Hủy xác nhận giữ trạng thái hiện tại. |
| E1 | M3 hoặc M5: sai định dạng, PDF chỉ có ảnh, mã hóa, tệp rỗng hoặc vượt giới hạn. | Hiển thị MSG-DOC-005 với lý do cụ thể đã xác định; từ chối hoặc chuyển `Failed` nếu đã có bản ghi. Không chuyển `Ready`; kết thúc thất bại, cho chọn tệp khác ở M2. |
| E2 | M5: dịch vụ embedding, lưu trữ hoặc lập chỉ mục lỗi; quá hạn xử lý. | Chuyển `Failed`, loại chỉ mục chưa hoàn tất khỏi truy xuất, hiển thị MSG-DOC-003. Kết thúc; có thể thực hiện A4. |
| E3 | M3 hoặc A3 đến A5: hết phiên; M6 hoặc các thao tác khác: mất quyền với tài nguyên hoặc Notebook đã xóa. | Yêu cầu của người dùng hết phiên xử lý theo CF-01; tài nguyên mất quyền xử lý theo CF-02 và chặn công bố. Riêng hết phiên trong lúc xử lý nền không tự hủy tác vụ đã nhận; kết quả chỉ được đọc sau khi đăng nhập lại. Tác vụ không được ghi vào Notebook đã xóa. |

**Truy vết:** IH-NB-004, IH-DOC-001, IH-DOC-002, IH-DOC-003, IH-DOC-004, IH-DOC-005, IH-DOC-006, IH-DATA-001, IH-DATA-002, IH-UX-001, IH-UX-002, IH-UX-003, IH-UX-004, IH-MSG-001, IH-MSG-002, IH-MSG-004, IH-INT-001, IH-INT-002, IH-INT-004, IH-NFR-002, IH-NFR-003, IH-NFR-004, IH-NFR-005, IH-NFR-006, IH-REL-001; BR-04, BR-07 đến BR-10; LIM-03, LIM-04, LIM-11 đến LIM-13; UAT-06, UAT-07, UAT-12, UAT-13, UAT-18.

<a id="uc-05"></a>

### UC-05: Hỏi đáp từ tài liệu và xem nguồn tham chiếu

- **Mục tiêu:** Tìm câu trả lời từ tài liệu trong Notebook và kiểm tra căn cứ của câu trả lời.
- **Tác nhân:** Người dùng đã đăng nhập; dịch vụ truy xuất và mô hình AI hỗ trợ.
- **Kích hoạt:** Người dùng gửi câu hỏi, mở lịch sử, quản lý hội thoại hoặc kiểm tra tham chiếu nguồn.
- **Tiền điều kiện:** Có phiên hợp lệ và quyền sở hữu Notebook đang hoạt động. Chỉ gửi câu hỏi mới hoặc thử lại mới yêu cầu tập nguồn có tài liệu `Ready` và còn hạn mức. Xem, đổi tên hoặc xóa hội thoại đã lưu không yêu cầu còn tài liệu nguồn.
- **Dữ liệu đầu vào:** Người dùng cung cấp câu hỏi, hội thoại và danh sách tài liệu nguồn; yêu cầu có mã thao tác để kiểm soát việc gửi lặp.
- **Kết quả đầu ra:** Hệ thống lưu và trả câu trả lời kèm tham chiếu nguồn, trạng thái xử lý và thời điểm thực hiện.
- **Hậu điều kiện thành công:** Hỏi mới: lượt `Answered` có nội dung và tham chiếu hợp lệ; trường hợp thiếu căn cứ lưu `NoEvidence`. Mở lịch sử: đọc đúng các lượt đã lưu, nguồn đã xóa có thông báo tương ứng. Tạo hoặc đổi tên: hội thoại được lưu đúng. Xóa: hội thoại và các lượt không còn truy cập được; ghi chú độc lập được giữ.
- **Bảo đảm tối thiểu:** Không lấy nguồn ngoài phạm vi; `NoEvidence` khác `Failed`; mất kết nối không tạo lượt trùng; không công bố dữ liệu đã mất quyền.

**Luồng chính**

| Bước | Tương tác |
| --- | --- |
| M1 | Hệ thống hiển thị Notebook, hội thoại và các nguồn `Ready`; mặc định chọn toàn bộ nguồn hợp lệ. Giao diện nêu mỗi câu hỏi được xử lý độc lập. |
| M2 | Người dùng chọn phạm vi nguồn, nhập câu hỏi và gửi. |
| M3 | Hệ thống kiểm tra phiên, quyền với từng nguồn, độ dài câu hỏi, hạn mức và mã thao tác; lưu yêu cầu cùng tập nguồn xác định. |
| M4 | Hệ thống hiển thị MSG-AI-001 và truy xuất các đoạn liên quan trong tập nguồn. |
| M5 | Mô hình tạo câu trả lời dựa trên nội dung truy xuất. Hệ thống kiểm tra cấu trúc và định danh, vị trí tham chiếu; kiểm tra lại nguồn và quyền trước khi công bố. |
| M6 | Hệ thống lưu câu hỏi, câu trả lời, nguồn, thời điểm và trạng thái `Answered`, sau đó hiển thị nội dung cho người dùng. |
| M7 | Người dùng mở một tham chiếu. Hệ thống kiểm tra quyền và hiển thị đúng đoạn nguồn; ca sử dụng kết thúc thành công. |

**Luồng thay thế và ngoại lệ**

| Nhánh | Điểm phát sinh | Xử lý và điểm kết thúc hoặc quay lại |
| --- | --- | --- |
| A1 | M5: tài liệu không đủ căn cứ. | Lưu `NoEvidence`, hiển thị MSG-AI-003, không tạo câu trả lời khẳng định từ tri thức ngoài nguồn. Kết thúc nghiệp vụ với kết luận thiếu căn cứ; người dùng có thể bổ sung nguồn rồi gửi câu hỏi mới. |
| A2 | M1: người dùng tạo, mở hoặc đổi tên hội thoại. | Kiểm tra quyền; tạo hội thoại rỗng hoặc đọc lịch sử theo thứ tự; đổi tên tuân LIM-06 và BR-12. Kết thúc thao tác quản lý; câu hỏi mới vẫn không dùng ngữ cảnh từ các lượt cũ. |
| A3 | M1: người dùng xóa hội thoại. | Hiển thị MSG-DATA-007; xác nhận thì xóa đúng hội thoại và các lượt, giữ ghi chú độc lập. Nếu có tác vụ chưa kết thúc, không cho tác vụ ghi lại hội thoại đã xóa. Hủy giữ nguyên; kết thúc thao tác quản lý. |
| A4 | M3 hoặc M4: gửi lại cùng mã, rời trang hoặc phản hồi mạng không rõ. | Hệ thống xử lý theo CF-04, CF-07; đọc hoặc trả lại đúng lượt hiện có. Không gọi mô hình lần thứ hai cho cùng thao tác. |
| A5 | Lượt `Failed`: người dùng chọn thử lại. | Tạo lượt xử lý có mã mới và liên kết lượt lỗi, kiểm tra lại nguồn rồi quay lại M3. Không xóa lịch sử lỗi. |
| E1 | M3: câu hỏi, nguồn hoặc hạn mức không hợp lệ. | Hệ thống xử lý theo CF-03, CF-06; không gọi mô hình. Quay lại M2 để sửa hoặc đợi theo giới hạn. |
| E2 | M4 hoặc M5: lỗi nhà cung cấp, hết hạn mức dịch vụ, quá LIM-11 hoặc tham chiếu không thể sửa thành hợp lệ. | Lưu `Failed`, hiển thị MSG-AI-004; không ghi lỗi kỹ thuật thành `NoEvidence`. Kết thúc thất bại; có thể dùng A5. |
| E3 | M5 hoặc M6: nguồn, Notebook hoặc hội thoại bị xóa; quyền không còn hợp lệ. | Không công bố kết quả. Tác vụ kết thúc `Failed`; thông báo MSG-AI-005 hoặc CF-02 tùy quyền còn lại. Không tái tạo dữ liệu đã xóa. |
| E4 | M7: nguồn đã bị xóa sau khi câu trả lời được lưu. | Hiển thị MSG-DATA-011 trong câu trả lời thuộc quyền người dùng; giữ nội dung lịch sử, không tải lại đoạn nguồn từ bộ nhớ đệm. Kết thúc thao tác mở nguồn. |
| E5 | M3, M6 hoặc M7: phiên hết hiệu lực. | Hệ thống xử lý theo CF-01; không chuyển nội dung tới ứng dụng khách chưa đăng nhập lại. Sau đăng nhập, người dùng chủ động mở lịch sử để đọc kết quả còn hợp lệ. |

**Truy vết:** IH-NB-004, IH-DOC-005, IH-CHAT-001, IH-CHAT-002, IH-CHAT-003, IH-CHAT-004, IH-CHAT-005, IH-DATA-001, IH-DATA-002, IH-UX-001, IH-UX-002, IH-UX-003, IH-UX-004, IH-MSG-001, IH-MSG-002, IH-MSG-004, IH-INT-001, IH-INT-002, IH-INT-003, IH-INT-004, IH-NFR-002, IH-NFR-003, IH-NFR-004, IH-NFR-005, IH-NFR-007, IH-REL-001; BR-04 đến BR-13; LIM-06, LIM-10 đến LIM-12; UAT-08, UAT-09, UAT-12 đến UAT-14, UAT-18; AEV-01, AEV-08.

<a id="uc-06"></a>

### UC-06: Quản lý ghi chú

- **Mục tiêu:** Lưu nội dung cần sử dụng lại thành ghi chú trong Notebook.
- **Tác nhân:** Người dùng đã đăng nhập.
- **Kích hoạt:** Người dùng tạo, xem, sửa, xóa ghi chú hoặc chọn lưu từ câu trả lời, bản tóm tắt.
- **Tiền điều kiện:** Notebook thuộc người dùng; nội dung gốc phải truy cập được tại thời điểm sao chép nếu lưu từ AI.
- **Dữ liệu đầu vào:** Người dùng cung cấp tiêu đề, nội dung và phiên bản của ghi chú khi cập nhật. Nếu lưu từ nội dung AI, hệ thống sử dụng thêm định danh nội dung gốc và các tham chiếu nguồn.
- **Kết quả đầu ra:** Hệ thống lưu ghi chú độc lập, kèm định danh, phiên bản, thời điểm và thông tin xuất xứ nếu có.
- **Hậu điều kiện thành công:** Tạo hoặc sửa: ghi chú được lưu với nội dung, phiên bản hiện hành và mở lại được. Xem: chỉ đọc ghi chú thuộc quyền. Xóa: ghi chú không còn trong danh sách và không thể đọc qua API; nội dung gốc được giữ. Sửa ghi chú không thay đổi nguồn đã sao chép.
- **Bảo đảm tối thiểu:** Không ghi đè phiên bản mới khi xung đột; xóa nội dung gốc không tự xóa bản ghi chú đã lưu; không lưu lỗi như câu trả lời hợp lệ.

**Luồng chính**

| Bước | Tương tác |
| --- | --- |
| M1 | Người dùng chọn tạo ghi chú trong Notebook. |
| M2 | Hệ thống hiển thị tiêu đề, nội dung cần nhập và giới hạn LIM-06. |
| M3 | Người dùng nhập và lưu. |
| M4 | Hệ thống kiểm tra quyền, giới hạn; lưu tiêu đề, nội dung, thời điểm và phiên bản. |
| M5 | Hệ thống hiển thị MSG-DATA-002; ghi chú xuất hiện trong danh sách và mở lại được. Ca sử dụng kết thúc thành công. |

**Luồng thay thế và ngoại lệ**

| Nhánh | Điểm phát sinh | Xử lý và điểm kết thúc hoặc quay lại |
| --- | --- | --- |
| A1 | M1: chọn lưu câu trả lời `Answered` hoặc bản tóm tắt đã lưu thành công. | Kiểm tra quyền và sự tồn tại của nội dung gốc; sao chép nội dung, liên kết xuất xứ, tham chiếu vào bản nháp ghi chú. Người dùng kiểm tra tiêu đề và nội dung rồi tiếp tục M3; không lưu tự động nếu vượt LIM-06. |
| A2 | M1: mở ghi chú đã có để sửa. | Đọc nội dung và phiên bản sau kiểm tra quyền. Người dùng sửa rồi thực hiện M3; M4 phải kiểm tra BR-12 trước khi lưu phiên bản mới. |
| A3 | M1: xóa ghi chú. | Hiển thị MSG-DATA-008. Xác nhận thì kiểm tra quyền và xóa, hiển thị MSG-DATA-009; hủy thì giữ nguyên. Kết thúc; không xóa tài liệu hoặc kết quả AI gốc. |
| E1 | M4: vượt giới hạn hoặc xung đột phiên bản. | Hệ thống xử lý theo CF-03 hoặc CF-05; quay lại M2 hoặc A2 sau khi tải bản hiện hành. |
| E2 | A1: nội dung gốc đã xóa hoặc là `Failed`/`NoEvidence`. | Không tạo bản ghi chú từ nội dung không hợp lệ; hiển thị MSG-DATA-010 hoặc không cung cấp thao tác lưu. Kết thúc nhánh. Ghi chú đã lưu trước đó vẫn giữ nội dung và đánh dấu xuất xứ không còn. |
| E3 | M4 hoặc A3: phiên, quyền không hợp lệ hoặc trạng thái mạng chưa rõ. | Hệ thống xử lý theo CF-01, CF-02 hoặc CF-04; không thông báo lưu hoặc xóa thành công khi chưa xác định kết quả. |

**Truy vết:** IH-NB-004, IH-NOTE-001, IH-NOTE-002, IH-SUM-002, IH-DATA-001, IH-DATA-002, IH-UX-001, IH-UX-002, IH-UX-003, IH-UX-004, IH-MSG-001, IH-MSG-002, IH-INT-001, IH-INT-004, IH-NFR-002, IH-NFR-003, IH-NFR-004, IH-REL-001; BR-08, BR-11, BR-12; LIM-06; UAT-10, UAT-12, UAT-18.

<a id="uc-07"></a>

### UC-07: Tạo nội dung từ tài liệu bằng công cụ AI

- **Mục tiêu:** Chuyển tài liệu thành một sản phẩm nội dung hữu ích thuộc một trong năm loại công cụ bắt buộc.
- **Tác nhân:** Người dùng đã đăng nhập; mô hình AI hỗ trợ.
- **Kích hoạt:** Người dùng chọn một công cụ trong Notebook.
- **Tiền điều kiện:** Có 1-3 tài liệu `Ready` cùng Notebook, tổng văn bản đáp ứng LIM-05; còn hạn mức để luồng chính thành công.
- **Dữ liệu đầu vào:** Người dùng chọn công cụ, tài liệu nguồn và cấu hình tương ứng; có thể nhập hướng dẫn bổ sung. Yêu cầu có mã thao tác để kiểm soát việc gửi lặp.
- **Kết quả đầu ra:** Hệ thống trả trạng thái tác vụ và kết quả có cấu trúc khi thành công; kết quả lưu kèm nguồn, cấu hình, thông tin mô hình và thời điểm tạo.
- **Hậu điều kiện thành công:** Một kết quả AI hợp lệ được lưu, mở lại và sử dụng bằng đúng giao diện của công cụ.
- **Bảo đảm tối thiểu:** Không tự cắt bớt tài liệu nguồn mà không thông báo; không lưu đầu ra thô, sai cấu trúc hoặc lỗi như thành công; không tạo kết quả trùng do cùng một thao tác được gửi lại; không thay nội dung kết quả cũ.

**Luồng chính: tạo bản tóm tắt ngắn**

| Bước | Tương tác |
| --- | --- |
| M1 | Người dùng mở công cụ Tóm tắt; hệ thống mô tả đầu ra và giới hạn áp dụng. |
| M2 | Người dùng chọn 1-3 tài liệu, chọn mức ngắn 150-250 từ và có thể nhập hướng dẫn bổ sung trong LIM-05. |
| M3 | Hệ thống kiểm tra quyền từng nguồn, trạng thái, tổng độ dài, cấu hình, hạn mức và mã thao tác. |
| M4 | Hệ thống lưu tác vụ `Processing`, tập nguồn và cấu hình; hiển thị MSG-AI-001. |
| M5 | Mô hình tạo nội dung từ tập nguồn đã xác định. |
| M6 | Hệ thống kiểm tra cấu trúc theo công cụ, giới hạn đầu ra, định danh tham chiếu và quyền, trạng thái nguồn trước khi lưu. |
| M7 | Hệ thống lưu đúng một kết quả cùng nguồn, cấu hình, thông tin mô hình và thời điểm; chuyển tác vụ sang `Succeeded`. |
| M8 | Hệ thống hiển thị MSG-AI-002 và bản tóm tắt có tổng quan, ý chính, điểm cần chú ý, tham chiếu nguồn. Kết quả có thể mở lại qua UC-08; ca sử dụng kết thúc thành công. |

**Biến thể bắt buộc của năm công cụ**

Mỗi dòng sau xác định một nhánh tại M1-M2; sau khi hoàn tất cấu hình, tiếp tục M3-M7. M8 sử dụng cách hiển thị tương ứng. Các trường hợp kiểm thử phải bao phủ từng dòng, không chỉ luồng Tóm tắt mặc định.

| Nhánh | Công cụ và dữ liệu cấu hình | Đầu ra phải kiểm tại M6 | Sử dụng tại M8 |
| --- | --- | --- | --- |
| A1 | Mindmap; 1-3 nguồn, hướng dẫn bổ sung nếu có. | Một chủ đề gốc, 10-30 nút, 2-4 cấp, không có vòng lặp; nhánh chính có căn cứ và tham chiếu. | Sơ đồ có mở rộng, thu gọn, phóng to, thu nhỏ, đưa về khung nhìn; thiết bị di động đọc đủ cây. |
| A2 | Tóm tắt; mức ngắn 150-250 hoặc chi tiết 400-600 từ. | Có tổng quan, ý chính, điểm cần chú ý; phản ánh nội dung của các tài liệu đã chọn, nêu mâu thuẫn nếu có; không bổ sung thông tin ngoài tài liệu nguồn để đạt độ dài yêu cầu. | Nội dung có cấu trúc; có thể lưu bản sao thành ghi chú theo UC-06.A1. |
| A3 | Slide; người dùng chọn 5-8 slide và chủ đề trình bày. | Đúng số slide, có trang tiêu đề và kết luận; mỗi trang nội dung có tiêu đề, 3-5 ý ngắn và tham chiếu; không thực thi mã do mô hình sinh. | Xem trang, số trang và trình chiếu qua UC-08.A4. |
| A4 | Quiz; người dùng chọn 5 hoặc 10 câu. | Mỗi câu có 4 lựa chọn khác nhau, đúng một đáp án đúng, giải thích có căn cứ và tham chiếu; không trùng hoặc mơ hồ. | Giao diện làm bài chưa hiển thị đáp án; thực hiện UC-08.A3 để nộp và xem kết quả. |
| A5 | Báo cáo; mục tiêu 1-1.000 ký tự. | 600-1.000 từ; tiêu đề, mục tiêu, phạm vi nguồn, tổng quan, phân tích, kết luận; phân biệt dữ kiện với nhận định và chỉ rõ khoảng trống. | Đọc theo đề mục, mở nguồn và tải Markdown qua UC-08.A5. |

**Ngoại lệ và phục hồi**

| Nhánh | Điểm phát sinh | Xử lý và điểm kết thúc hoặc quay lại |
| --- | --- | --- |
| E1 | M3: nguồn khác Notebook, không `Ready`, quá dài, cấu hình thiếu hoặc sai giới hạn. | Hệ thống xử lý theo CF-03; hiển thị MSG-AI-006 khi vượt giới hạn của công cụ. Không gọi mô hình; quay lại M2 để chọn lại nguồn hoặc cấu hình. |
| E2 | M3: đang có tác vụ hoặc vượt tần suất. | Hệ thống xử lý theo CF-06. Không tạo tác vụ mới; cho mở trạng thái tác vụ hiện có hoặc chờ rồi thực hiện lại M3. |
| E3 | M5 hoặc M6: nguồn không đủ căn cứ tạo nội dung yêu cầu. | Kết thúc `NoEvidence`, hiển thị MSG-AI-003; không tạo hoặc đánh dấu kết quả AI là thành công. Người dùng sửa nguồn hoặc cấu hình rồi bắt đầu yêu cầu mới ở M2. |
| E4 | M5 hoặc M6: lỗi dịch vụ, hết hạn mức, quá hạn hoặc đầu ra không hợp lệ sau xử lý. | Kết thúc `Failed`, hiển thị MSG-AI-004, lưu lý do và mã tra cứu an toàn; không lưu đầu ra thô. Thử lại tạo mã tác vụ mới liên kết lần lỗi, quay lại M3 sau kiểm tra đầu vào. |
| E5 | M6 hoặc M7: nguồn hoặc Notebook bị xóa, quyền không còn hợp lệ. | Không công bố hoặc lưu kết quả dưới tài nguyên đã xóa. Kết thúc `Failed`, hiển thị MSG-AI-005 nếu người dùng còn quyền xem ngữ cảnh; nếu không, xử lý theo CF-02. |
| E6 | M3-M8: gửi lặp, mất kết nối, rời trang hoặc hết phiên. | Hệ thống xử lý theo CF-04, CF-07 hoặc CF-01 tương ứng. Cùng mã chỉ trả cùng tác vụ; kết quả chỉ hiển thị sau khi xác minh lại phiên và quyền. |

**Yêu cầu chất lượng riêng:** AEV-02 đến AEV-06 đánh giá nội dung của từng công cụ; cấu trúc hợp lệ không tự chứng minh nội dung đúng. AEV-07 kiểm ngoại lệ và AEV-08 kiểm cách ly. Năm công cụ đều phải đạt yêu cầu riêng.

**Truy vết:** IH-NB-004, IH-DOC-005, IH-AI-001, IH-AI-002, IH-AI-003, IH-AI-004, IH-MM-001, IH-SUM-001, IH-SLD-001, IH-QUIZ-001, IH-RPT-001, IH-DATA-001, IH-UX-001, IH-UX-002, IH-UX-003, IH-UX-004, IH-MSG-001, IH-MSG-002, IH-MSG-004, IH-INT-001, IH-INT-002, IH-INT-003, IH-INT-004, IH-NFR-002, IH-NFR-003, IH-NFR-004, IH-NFR-005, IH-NFR-007, IH-REL-001; BR-04 đến BR-13, BR-15; LIM-05, LIM-10 đến LIM-12, LIM-17; UAT-11, UAT-12, UAT-13, UAT-14, UAT-18.

<a id="uc-08"></a>

### UC-08: Xem và quản lý kết quả AI

- **Mục tiêu:** Khai thác lại nội dung AI đã lưu theo đúng loại kết quả.
- **Tác nhân:** Người dùng đã đăng nhập.
- **Kích hoạt:** Người dùng mở danh sách kết quả AI trong Notebook.
- **Tiền điều kiện:** Notebook thuộc người dùng; luồng mở kết quả cần có kết quả AI đã lưu thành công.
- **Dữ liệu đầu vào:** Người dùng chọn kết quả bằng định danh; cung cấp tên mới, cấu hình tạo lại, lựa chọn Quiz hoặc yêu cầu tải báo cáo tùy thao tác.
- **Kết quả đầu ra:** Hệ thống hiển thị nội dung và thông tin nguồn đã lưu; trả kết quả cập nhật, xóa, chấm Quiz hoặc tệp báo cáo tương ứng với thao tác thực hiện.
- **Hậu điều kiện thành công:** Xem hoặc tải: đọc đúng nội dung đã lưu và còn thuộc quyền. Đổi tên: tên mới được lưu, nội dung không đổi. Tạo lại: có kết quả mới nếu tác vụ thành công, bản cũ được giữ. Nộp Quiz: lưu đúng lựa chọn và điểm của lần làm. Xóa: kết quả và các lần làm Quiz liên quan không còn truy cập được, nguồn và ghi chú độc lập được giữ.
- **Bảo đảm tối thiểu:** Kiểm tra quyền với mọi thao tác; không thay nội dung cũ khi tạo lại; xóa nguồn không tự đổi nội dung; không tiết lộ đáp án Quiz trước khi nộp trên giao diện làm bài.

**Luồng chính**

| Bước | Tương tác |
| --- | --- |
| M1 | Hệ thống hiển thị danh sách kết quả của Notebook, có tên, loại, nguồn, thời điểm và sắp mới nhất trước. |
| M2 | Người dùng lọc theo loại công cụ nếu cần rồi chọn một kết quả. |
| M3 | Hệ thống kiểm tra quyền và đọc nội dung, cấu hình, nguồn đã lưu; không gọi mô hình để dựng lại nội dung. |
| M4 | Hệ thống hiển thị đúng giao diện Mindmap, Tóm tắt, Slide, Quiz hoặc Báo cáo. |
| M5 | Người dùng xem nội dung hoặc mở nguồn; hệ thống kiểm tra quyền nguồn trước khi trả đoạn trích. Ca sử dụng kết thúc thành công. |

**Luồng thay thế và ngoại lệ**

| Nhánh | Điểm phát sinh | Xử lý và điểm kết thúc hoặc quay lại |
| --- | --- | --- |
| A1 | M4: đổi tên kết quả. | Nhận tên và phiên bản, kiểm tra LIM-17 và BR-12; chỉ cập nhật tên, hiển thị MSG-DATA-002, quay lại M4. Không thay nội dung, nguồn hoặc mô hình đã ghi nhận. |
| A2 | M4: tạo lại nội dung. | Hiển thị nguồn và cấu hình trước đó để người dùng xác nhận hoặc sửa. Kiểm tra lại nguồn; thực hiện UC-07 bằng mã mới và liên kết kết quả gốc. Thành công tạo bản mới; thất bại giữ bản cũ. Kết thúc ở kết quả mới hoặc trạng thái lỗi. |
| A3 | M4: làm Quiz. | Hiển thị câu hỏi và lựa chọn, ẩn đáp án và giải thích trên giao diện làm bài. Người dùng chọn đáp án rồi nộp; hệ thống chấm theo BR-14, tính câu bỏ trống là sai, lưu lựa chọn, điểm và thời điểm. Hiển thị MSG-AI-007 cùng đáp án, giải thích, nguồn. Mở lại đọc lần đã nộp; làm lại tạo lần mới, giữ điểm cũ. Kết thúc lần làm bài. |
| A4 | M4: trình chiếu Slide. | Người dùng chọn chế độ trình chiếu, chuyển trước hoặc sau bằng điều khiển hay bàn phím. Hệ thống giữ đúng thứ tự, số trang, nội dung; thoát trình chiếu trở lại M4. |
| A5 | M4: tải Báo cáo. | Kiểm tra quyền ngay khi tải; tạo tệp `.md` UTF-8 chứa nội dung, định danh và tên nguồn. Không đưa token hoặc đường dẫn nội bộ vào tệp. Kết thúc tải; nội dung lưu không đổi. |
| A6 | M4: lưu Tóm tắt thành ghi chú. | Thực hiện UC-06.A1 với bản sao nội dung và xuất xứ; kết thúc ở ghi chú đã lưu hoặc bản nháp cần sửa. |
| A7 | M4: xóa kết quả. | Hiển thị MSG-DATA-006, nêu việc xóa cả lần làm Quiz nếu có. Xác nhận thì kiểm tra quyền, xóa kết quả và dữ liệu lần làm, chặn đường dẫn cũ; giữ nguồn và ghi chú đã sao chép. Hiển thị MSG-DATA-009, trở lại M1. Hủy thì trở lại M4. |
| E1 | M3 hoặc bất kỳ thao tác lưu, tải, xóa nào: hết phiên hoặc không có quyền. | Hệ thống xử lý theo CF-01 hoặc CF-02; kết thúc mà không trả dữ liệu trái quyền. |
| E2 | M5: nguồn của kết quả đã bị xóa. | Hiển thị MSG-DATA-011, giữ nội dung lịch sử theo BR-08; không đọc lại nguồn từ bộ nhớ đệm. Kết thúc thao tác xem nguồn. |
| E3 | A2: nguồn cũ không còn hợp lệ. | Yêu cầu chọn nguồn hợp lệ trước khi gửi sang UC-07; không tự thay nguồn hoặc xóa kết quả cũ. Quay về cấu hình tạo lại. |
| E4 | A1, A3 hoặc A7: cập nhật xung đột hoặc mạng chưa rõ kết quả. | Hệ thống xử lý theo CF-05 hoặc CF-04. Với nộp Quiz, kiểm tra trạng thái lần làm trước khi cho nộp lại; không ghi đè lần đã nộp bằng dữ liệu mới. |

**Truy vết:** IH-NB-004, IH-DOC-006, IH-AI-004, IH-MM-002, IH-SUM-002, IH-SLD-002, IH-QUIZ-002, IH-RPT-002, IH-OUT-001, IH-OUT-002, IH-OUT-003, IH-DATA-001, IH-DATA-002, IH-UX-001, IH-UX-002, IH-UX-003, IH-UX-004, IH-MSG-001, IH-MSG-002, IH-MSG-004, IH-INT-001, IH-INT-004, IH-NFR-002, IH-NFR-003, IH-NFR-004, IH-NFR-006, IH-REL-001; BR-07 đến BR-14; LIM-17; UAT-10, UAT-11, UAT-12, UAT-13, UAT-15, UAT-18.

<a id="uc-09"></a>

### UC-09: Kiểm chứng khôi phục bản sao lưu

- **Mục tiêu:** Kiểm chứng bản sao lưu đọc được và có thể tái lập dữ liệu trong môi trường riêng.
- **Tác nhân:** Người vận hành; hệ thống lưu trữ hỗ trợ.
- **Kích hoạt:** Người vận hành thực hiện kiểm chứng khôi phục trước khi bàn giao phiên bản R1.
- **Tiền điều kiện:** Có bản sao lưu hợp lệ theo UC-16 và môi trường đích riêng, không nhận lưu lượng người dùng; người vận hành có quyền cần thiết.
- **Dữ liệu đầu vào:** Bản sao lưu, danh mục thành phần, phiên bản phần mềm và dữ liệu đối chiếu tại thời điểm sao lưu.
- **Kết quả đầu ra:** Môi trường kiểm chứng chứa dữ liệu tại thời điểm sao lưu; bản ghi kết quả đối chiếu nội dung, quan hệ và quyền.
- **Hậu điều kiện thành công:** Dữ liệu mẫu và quyền khớp bản sao lưu; môi trường đang phục vụ không thay đổi. Môi trường kiểm chứng được dọn sau khi lưu bằng chứng an toàn.
- **Bảo đảm tối thiểu:** Không ghi đè môi trường đang phục vụ, không mở bản dữ liệu lịch sử cho người dùng và không ghi nhận thành công khi thiếu thành phần hoặc sai quyền.

**Luồng chính**

| Bước | Tương tác |
| --- | --- |
| M1 | Người vận hành chọn bản sao lưu hợp lệ, đối chiếu phiên bản và danh mục thành phần. |
| M2 | Kiểm tra môi trường đích riêng và quyền đọc bản sao lưu; xác nhận không kết nối tới kho dữ liệu đang phục vụ. |
| M3 | Thực hiện khôi phục dữ liệu và tệp theo hướng dẫn; tái tạo chỉ mục nếu thiết kế không sao lưu chỉ mục. |
| M4 | Đối chiếu số lượng mẫu, nội dung, quan hệ và quyền sở hữu tại thời điểm sao lưu; dữ liệu bị xóa trước lần sao lưu không được xuất hiện trong dữ liệu hoạt động của bản phục hồi. |
| M5 | Dùng hai tài khoản kiểm tra truy cập dữ liệu mẫu trong môi trường riêng; xác nhận không ảnh hưởng dữ liệu hiện hành. Dữ liệu đã xóa sau thời điểm sao lưu, nếu còn trong bản lịch sử, chỉ được kiểm tra tại môi trường này. |
| M6 | Ghi thời điểm, kết quả và lỗi nếu có; dọn môi trường kiểm chứng và các bản sao tạm. Chỉ ghi MSG-SYS-003 sau khi kiểm tra đạt; kết thúc thành công. |

**Luồng thay thế và ngoại lệ**

| Nhánh | Điểm phát sinh | Xử lý và điểm kết thúc hoặc quay lại |
| --- | --- | --- |
| A1 | M1: bản sao lưu chưa được tạo. | Thực hiện UC-16 rồi quay lại M1; không dùng tệp chưa kiểm tra thay bản sao lưu hợp lệ. |
| E1 | M1 hoặc M3: thiếu thành phần, sai phiên bản hoặc không đọc được. | Ghi MSG-SYS-004, kết thúc chưa đạt; sửa hướng dẫn hoặc tạo bản sao lưu mới trước khi kiểm lại. |
| E2 | M2: môi trường đích không cách ly. | Dừng trước khi ghi dữ liệu; chọn hoặc tạo môi trường riêng rồi quay lại M2. |
| E3 | M4 hoặc M5: sai nội dung, quan hệ hoặc quyền. | Ghi kết quả không đạt và bằng chứng tối thiểu; không mở môi trường cho người dùng; sửa nguyên nhân rồi thực hiện lại. |
| E4 | M6: không dọn được dữ liệu kiểm chứng. | Giữ chặn truy cập, ghi lỗi và xử lý dọn dữ liệu; không coi lần kiểm chứng hoàn tất khi còn bản sao tạm ngoài chính sách. |

**Truy vết:** IH-MSG-001, IH-NFR-004, IH-NFR-005, IH-NFR-008, IH-NFR-009, IH-REL-001, IH-REL-002; LIM-13, LIM-14, LIM-18; UAT-16, UAT-18.

<a id="uc-10"></a>

### UC-10: Đăng nhập bằng email và mật khẩu

- **Mục tiêu:** Truy cập đúng tài khoản bằng thông tin đăng nhập đã đăng ký.
- **Tác nhân:** Người chưa đăng nhập; dịch vụ xác thực hỗ trợ.
- **Kích hoạt:** Người dùng chọn đăng nhập bằng email và mật khẩu.
- **Tiền điều kiện:** Có tài khoản đăng ký bằng mật khẩu; luồng chính cần tài khoản `Active`. Không yêu cầu có phiên trước đó.
- **Dữ liệu đầu vào:** Người dùng cung cấp email và mật khẩu. Nếu có đích điều hướng sau đăng nhập, đích đó phải là địa chỉ nội bộ hợp lệ.
- **Kết quả đầu ra:** Hệ thống cấp phiên đăng nhập hợp lệ và hiển thị danh sách Notebook của đúng tài khoản.
- **Hậu điều kiện thành công:** Có phiên hợp lệ theo LIM-07 của đúng tài khoản.
- **Bảo đảm tối thiểu:** Thông tin sai không tạo phiên; không tiết lộ tài khoản tồn tại qua lỗi; không giữ mật khẩu trong bộ nhớ bền vững.

**Luồng chính**

| Bước | Tương tác |
| --- | --- |
| M1 | Người dùng nhập email, mật khẩu và gửi đăng nhập. |
| M2 | Hệ thống kiểm tra dữ liệu, giới hạn thử và xác thực thông tin. |
| M3 | Hệ thống xác nhận tài khoản `Active`, tạo phiên với giới hạn LIM-07. |
| M4 | Hệ thống mở danh sách Notebook của người dùng hoặc đích nội bộ còn hợp lệ sau kiểm tra quyền. Kết thúc thành công. |

**Luồng thay thế và ngoại lệ**

| Nhánh | Điểm phát sinh | Xử lý và điểm kết thúc hoặc quay lại |
| --- | --- | --- |
| A1 | M3: thông tin đúng nhưng tài khoản còn chờ xác minh. | Hiển thị MSG-AUTH-003, chỉ mở luồng xác minh và đăng xuất; không mở dữ liệu nghiệp vụ. Người dùng thực hiện UC-01.A1 hoặc xác minh bằng liên kết. Kết thúc phiên truy cập hạn chế. |
| A2 | M1: người dùng chọn quên mật khẩu hoặc Google. | Chuyển sang UC-02 hoặc UC-11; không gửi mật khẩu đang nhập sang luồng khác. Kết thúc luồng hiện tại. |
| E1 | M2: email hoặc mật khẩu sai. | Hiển thị MSG-AUTH-001 có cùng nội dung công khai; tăng bộ đếm theo LIM-09 và trở về M1. Không nói rõ email có tồn tại hay không. |
| E2 | M2: vượt giới hạn hoặc dịch vụ xác thực lỗi. | Hệ thống xử lý theo CF-06 hoặc MSG-SYS-002; không cấp phiên đăng nhập hoặc hiển thị đăng nhập thành công. Người dùng chờ hoặc thử lại ở M1. |
| E3 | M4: đích điều hướng không còn hợp lệ hoặc không thuộc quyền. | Mở danh sách Notebook của chính người dùng; không truy cập đích ngoài ứng dụng hoặc dữ liệu không thuộc quyền. Kết thúc đăng nhập thành công. |

**Truy vết:** IH-AUTH-003, IH-AUTH-008, IH-UX-001, IH-UX-002, IH-UX-003, IH-UX-004, IH-MSG-001, IH-MSG-002, IH-INT-001, IH-INT-003, IH-NFR-001, IH-NFR-011, IH-REL-001; LIM-07, LIM-09; UAT-01, UAT-04, UAT-18.

<a id="uc-11"></a>

### UC-11: Đăng nhập và liên kết tài khoản Google

- **Mục tiêu:** Đăng nhập bằng danh tính Google và sử dụng đúng tài khoản InsightHub.
- **Tác nhân:** Người chưa đăng nhập; Google, dịch vụ xác thực và email hỗ trợ.
- **Kích hoạt:** Người dùng chọn đăng nhập Google.
- **Tiền điều kiện:** Có tài khoản Google; ứng dụng và địa chỉ nhận kết quả xác thực được cấu hình hợp lệ.
- **Dữ liệu đầu vào:** Hệ thống tiếp nhận kết quả xác thực Google gồm định danh nhà cung cấp và địa chỉ email đã được xác minh; người dùng cung cấp thêm bằng chứng kiểm soát tài khoản hiện hữu khi cần liên kết.
- **Kết quả đầu ra:** Hệ thống trả tài khoản ứng dụng và phiên hợp lệ, hoặc yêu cầu người dùng hoàn tất xác nhận liên kết trước khi cấp quyền truy cập.
- **Hậu điều kiện thành công:** Có đúng một tài khoản `Active` tương ứng và phiên hợp lệ; liên kết mới không làm mất dữ liệu cũ.
- **Bảo đảm tối thiểu:** Không tự gộp theo email do ứng dụng khách gửi; lỗi hoặc hủy không tạo phiên, không hoàn tất tài khoản hay liên kết không hợp lệ.

**Luồng chính: danh tính mới, email chưa gắn tài khoản**

| Bước | Tương tác |
| --- | --- |
| M1 | Người dùng chọn Google; hệ thống bắt đầu yêu cầu xác thực. |
| M2 | Người dùng hoàn tất xác thực với Google. |
| M3 | Hệ thống kiểm chứng phản hồi, định danh và email đã xác minh, đối chiếu với dữ liệu ứng dụng. |
| M4 | Hệ thống tạo tài khoản `Active` và gắn danh tính Google đã kiểm chứng. |
| M5 | Hệ thống tạo phiên và mở danh sách Notebook của đúng người dùng. Kết thúc thành công. |

**Luồng thay thế và ngoại lệ**

| Nhánh | Điểm phát sinh | Xử lý và điểm kết thúc hoặc quay lại |
| --- | --- | --- |
| A1 | M3: danh tính Google đã liên kết. | Dùng đúng tài khoản hiện hữu và giữ nguyên dữ liệu, tiếp tục M5. Không tạo tài khoản thứ hai. |
| A2 | M3: email đã gắn với tài khoản chưa liên kết Google. | Hiển thị MSG-AUTH-009 và áp dụng BR-03. Với tài khoản `Active`, yêu cầu xác nhận mật khẩu hiện tại theo LIM-19; quên mật khẩu thì hoàn tất UC-02 và bắt đầu lại M1. Với `PendingVerification`, bắt buộc hoàn tất UC-02.A4 rồi bắt đầu lại M1, không chỉ thực hiện UC-01. Khi tài khoản `Active`, bằng chứng mật khẩu và danh tính Google cùng hợp lệ, liên kết đúng tài khoản, ghi sự kiện gửi EML-003 và tiếp tục M5. Không đủ bằng chứng thì không liên kết. |
| E1 | M2: người dùng hủy tại Google. | Hiển thị MSG-AUTH-007; kết thúc, không tạo phiên hay tài khoản hoàn tất. Có thể bắt đầu lại M1. |
| E2 | M3: phản hồi sai, hết hạn, email chưa xác minh hoặc dịch vụ lỗi. | Hiển thị MSG-AUTH-008; không cấp quyền; kết thúc thất bại. Chỉ thử lại bằng yêu cầu xác thực mới. |
| E3 | A2: xác nhận mật khẩu thất bại, bằng chứng hết hạn hoặc đã dùng. | Giữ nguyên tài khoản và liên kết cũ; hiển thị MSG-AUTH-009, cho thử lại trong LIM-09 hoặc khôi phục qua UC-02. Không cấp phiên từ danh tính Google chưa liên kết. Kết thúc nhánh hiện tại. |
| E4 | A2: gửi EML-003 thất bại sau khi đã liên kết. | Ghi lỗi gửi theo CF-08 và mục 9.4; giữ liên kết đã hoàn tất hợp lệ, tiếp tục M5. Không yêu cầu liên kết lại chỉ để gửi email thông báo. |

**Truy vết:** IH-AUTH-004, IH-AUTH-005, IH-AUTH-008, IH-UX-001, IH-UX-002, IH-UX-003, IH-UX-004, IH-MSG-001, IH-MSG-002, IH-MSG-003, IH-INT-001, IH-INT-003, IH-NFR-001, IH-NFR-011, IH-REL-001; BR-02, BR-03; LIM-07 đến LIM-09; UAT-02, UAT-18, UAT-19.

<a id="uc-12"></a>

### UC-12: Xem và cập nhật hồ sơ cá nhân

- **Mục tiêu:** Xem và cập nhật thông tin cá nhân trong phạm vi R1.
- **Tác nhân:** Người dùng đã đăng nhập.
- **Kích hoạt:** Người dùng mở hồ sơ cá nhân.
- **Tiền điều kiện:** Tài khoản `Active`, phiên hợp lệ.
- **Dữ liệu đầu vào:** Người dùng cung cấp tên hiển thị, lựa chọn ảnh đại diện mặc định và phiên bản hồ sơ đang sửa.
- **Kết quả đầu ra:** Hệ thống hiển thị hồ sơ đã lưu, gồm email, tên, ảnh đại diện, phương thức đăng nhập và trạng thái xác minh. Ảnh Google được hiển thị khi có dữ liệu phù hợp.
- **Hậu điều kiện thành công:** Tên và lựa chọn ảnh hợp lệ được lưu và còn sau đăng nhập lại.
- **Bảo đảm tối thiểu:** Không thay email, nhà cung cấp xác thực hoặc tải ảnh riêng bằng cách sửa dữ liệu gửi; lỗi không làm thay đổi định danh tài khoản.

**Luồng chính**

| Bước | Tương tác |
| --- | --- |
| M1 | Hệ thống đọc và hiển thị hồ sơ của đúng người dùng. |
| M2 | Người dùng sửa tên hoặc chọn ảnh mặc định rồi lưu. |
| M3 | Hệ thống kiểm tra phiên, giới hạn LIM-01, phiên bản hiện hành và các trường được phép thay đổi. |
| M4 | Hệ thống lưu thay đổi, hiển thị MSG-DATA-002 và hồ sơ cập nhật; kết thúc thành công. |

**Luồng thay thế và ngoại lệ**

| Nhánh | Điểm phát sinh | Xử lý và điểm kết thúc hoặc quay lại |
| --- | --- | --- |
| A1 | M1: người dùng chỉ xem hoặc hủy chỉnh sửa. | Kết thúc xem, giữ nguyên dữ liệu đã lưu. |
| A2 | M1: người dùng chọn đổi mật khẩu. | Chuyển sang UC-13 nếu tài khoản có mật khẩu; chức năng này không hiển thị cho tài khoản chỉ dùng Google. |
| E1 | M3: tên sai giới hạn hoặc gửi trường không được phép. | Hệ thống xử lý theo CF-03; không thay email hoặc phương thức đăng nhập; quay lại M2. |
| E2 | M3 hoặc M4: hết phiên hoặc phản hồi mạng không rõ. | Hệ thống xử lý theo CF-01 hoặc CF-04; xác định lại hồ sơ đã lưu trước khi cho gửi tiếp. |
| E3 | M3: phiên bản hồ sơ đã cũ. | Hệ thống xử lý theo CF-05; tải lại hồ sơ trước khi sửa, không ghi đè thay đổi của phiên khác. |

**Truy vết:** IH-AUTH-009, IH-DATA-001, IH-UX-001, IH-UX-002, IH-UX-003, IH-UX-004, IH-MSG-001, IH-MSG-002, IH-INT-001, IH-NFR-003, IH-NFR-011, IH-REL-001; LIM-01; UAT-04, UAT-18.

<a id="uc-13"></a>

### UC-13: Đổi mật khẩu

- **Mục tiêu:** Thay mật khẩu hiện tại sau khi chứng minh quyền kiểm soát tài khoản.
- **Tác nhân:** Người dùng đã đăng nhập bằng tài khoản có mật khẩu; dịch vụ xác thực và email hỗ trợ.
- **Kích hoạt:** Người dùng chọn đổi mật khẩu trong hồ sơ.
- **Tiền điều kiện:** Có phiên hợp lệ và tài khoản hỗ trợ mật khẩu.
- **Dữ liệu đầu vào:** Người dùng cung cấp bằng chứng tái xác thực, mật khẩu mới và mật khẩu xác nhận.
- **Kết quả đầu ra:** Hệ thống trả kết quả đổi mật khẩu, thu hồi các phiên cũ theo giới hạn quy định, gửi EML-005 và yêu cầu đăng nhập lại.
- **Hậu điều kiện thành công:** Mật khẩu mới có hiệu lực, phiên cũ bị thu hồi theo LIM-07; người dùng đăng nhập lại.
- **Bảo đảm tối thiểu:** Tái xác thực thất bại không thay mật khẩu; không đưa mật khẩu vào email hoặc nhật ký.

**Luồng chính**

| Bước | Tương tác |
| --- | --- |
| M1 | Hệ thống yêu cầu tái xác thực trước khi cho thay mật khẩu. |
| M2 | Người dùng hoàn tất tái xác thực và nhập mật khẩu mới cùng xác nhận. |
| M3 | Hệ thống kiểm tra bằng chứng, sự trùng khớp và LIM-01. |
| M4 | Hệ thống cập nhật mật khẩu và thu hồi các phiên cũ theo LIM-07. |
| M5 | Hệ thống hiển thị MSG-AUTH-011, gửi EML-005 và yêu cầu đăng nhập lại bằng UC-10. Kết thúc thành công. |

**Luồng thay thế và ngoại lệ**

| Nhánh | Điểm phát sinh | Xử lý và điểm kết thúc hoặc quay lại |
| --- | --- | --- |
| A1 | M1 hoặc M2: người dùng hủy. | Kết thúc, giữ mật khẩu và phiên trước đó trong giới hạn đang áp dụng. |
| E1 | M3: bằng chứng tái xác thực sai hoặc hết hiệu lực. | Không đổi mật khẩu; hiển thị MSG-AUTH-001 hoặc MSG-AUTH-012 theo tình trạng phiên. Quay về M1 nếu còn phiên, nếu không kết thúc để đăng nhập. |
| E2 | M3: mật khẩu không hợp lệ. | Hệ thống xử lý theo CF-03; quay lại M2, phải tái xác thực lại nếu bằng chứng đã hết hiệu lực. |
| E3 | M4: kết quả cập nhật chưa rõ do mất kết nối. | Hệ thống xử lý theo CF-04; không tự lặp yêu cầu đổi mật khẩu. Xác định trạng thái bằng cơ chế xác thực và hướng dẫn đăng nhập hoặc khôi phục phù hợp. |
| E4 | M5: lỗi gửi email thông báo. | Ghi lỗi theo mục 9.4; giữ mật khẩu mới và kết quả thu hồi phiên, không đảo ngược giao dịch. |

**Truy vết:** IH-AUTH-008, IH-AUTH-010, IH-UX-001, IH-UX-002, IH-UX-003, IH-UX-004, IH-MSG-001, IH-MSG-002, IH-MSG-003, IH-INT-001, IH-INT-003, IH-NFR-001, IH-NFR-011, IH-REL-001; LIM-01, LIM-07; UAT-03, UAT-18, UAT-19.

<a id="uc-14"></a>

### UC-14: Đăng xuất

- **Mục tiêu:** Ngừng quyền truy cập từ phiên hiện tại.
- **Tác nhân:** Người dùng đang có phiên, kể cả phiên hạn chế của tài khoản chờ xác minh.
- **Kích hoạt:** Người dùng chọn đăng xuất.
- **Tiền điều kiện:** Ứng dụng có thông tin phiên hiện tại hoặc có dữ liệu phiên cần xóa.
- **Dữ liệu đầu vào:** Ứng dụng sử dụng thông tin của phiên hiện tại để yêu cầu đăng xuất.
- **Kết quả đầu ra:** Hệ thống trả kết quả kết thúc phiên; ứng dụng xóa dữ liệu phiên cục bộ và chuyển đến màn hình đăng nhập.
- **Hậu điều kiện thành công:** Máy chủ không chấp nhận yêu cầu mới từ phiên đã đăng xuất; giao diện không còn dữ liệu cá nhân.
- **Bảo đảm tối thiểu:** Không nhận kết quả AI vào giao diện sau khi phiên hết hiệu lực; không yêu cầu xóa dữ liệu đã lưu của người dùng chỉ vì đăng xuất.

**Luồng chính**

| Bước | Tương tác |
| --- | --- |
| M1 | Người dùng chọn đăng xuất. |
| M2 | Hệ thống kết thúc phiên trên máy chủ. |
| M3 | Ứng dụng khách xóa thông tin phiên và dữ liệu cá nhân trong bộ nhớ giao diện. |
| M4 | Hệ thống hiển thị MSG-AUTH-013 và màn hình đăng nhập; kết thúc thành công. |

**Luồng thay thế và ngoại lệ**

| Nhánh | Điểm phát sinh | Xử lý và điểm kết thúc hoặc quay lại |
| --- | --- | --- |
| A1 | M2: phiên đã hết hạn hoặc đã đăng xuất. | Xem thao tác kết thúc phiên là hoàn tất, tiếp tục M3; không báo lỗi gây cản trở việc thoát tài khoản. |
| E1 | M2: mất kết nối, chưa xác nhận phiên đã thu hồi trên máy chủ. | Vẫn xóa dữ liệu cục bộ ở M3 để ngừng hiển thị; dùng MSG-SYS-001, không khẳng định phiên máy chủ đã bị thu hồi. Thực hiện lại việc kết thúc khi có kết nối; phiên máy chủ vẫn chịu LIM-07 cho đến khi xác nhận thu hồi. |
| E2 | M3 hoặc M4: tác vụ AI trả kết quả muộn. | Không hiển thị nội dung cho phiên đã kết thúc. Kết quả đã lưu hợp lệ chỉ được đọc sau khi đăng nhập và kiểm tra quyền lại. |

**Truy vết:** IH-AUTH-008, IH-UX-001, IH-UX-002, IH-UX-003, IH-UX-004, IH-MSG-001, IH-MSG-002, IH-INT-001, IH-INT-004, IH-NFR-001, IH-NFR-011, IH-REL-001; LIM-07; UAT-04, UAT-18.

<a id="uc-15"></a>

### UC-15: Cài đặt và cấu hình môi trường

- **Mục tiêu:** Cài đặt một môi trường tái lập được và kiểm tra điều kiện sẵn sàng.
- **Tác nhân:** Người vận hành; dịch vụ xác thực, email, mô hình và lưu trữ hỗ trợ.
- **Kích hoạt:** Người vận hành triển khai phiên bản sản phẩm theo hồ sơ bàn giao.
- **Tiền điều kiện:** Có môi trường, quyền vận hành, gói mã nguồn, phiên bản phụ thuộc và cấu hình hợp lệ; thông tin bí mật được cung cấp qua cơ chế bảo mật.
- **Dữ liệu đầu vào:** Người vận hành cung cấp phiên bản phát hành, cấu hình triển khai và quy trình cập nhật cơ sở dữ liệu.
- **Kết quả đầu ra:** Hệ thống báo trạng thái sẵn sàng hoặc nguyên nhân chưa sẵn sàng; hồ sơ cài đặt ghi nhật ký và bằng chứng kiểm chứng môi trường.
- **Hậu điều kiện thành công:** Môi trường khởi động được, các tích hợp cần thiết đã kiểm chứng và có cấu hình nghiệm thu ghi nhận.
- **Bảo đảm tối thiểu:** Cấu hình thiếu không được báo sẵn sàng; không tiết lộ thông tin bí mật; không tự nhập dữ liệu minh họa hoặc gán dữ liệu dùng chung cho người đăng ký đầu tiên.

**Luồng chính**

| Bước | Tương tác |
| --- | --- |
| M1 | Người vận hành cài đúng phiên bản phần mềm và phụ thuộc theo hướng dẫn trên môi trường sạch. |
| M2 | Cung cấp cấu hình, chạy cập nhật cơ sở dữ liệu theo tài liệu rồi khởi động dịch vụ. |
| M3 | Hệ thống kiểm tra cấu hình bắt buộc, tình trạng hoạt động và các thành phần phụ thuộc. |
| M4 | Người vận hành kiểm tra đăng nhập, email và dịch vụ AI thực theo hồ sơ kiểm chứng, không dùng kết quả giả lập thay bằng chứng thật. |
| M5 | Ghi cấu hình, ngày, phiên bản, kết quả và điểm tra cứu nhật ký; hiển thị MSG-SYS-003 khi đạt. Kết thúc thành công. |

**Luồng thay thế và ngoại lệ**

| Nhánh | Điểm phát sinh | Xử lý và điểm kết thúc hoặc quay lại |
| --- | --- | --- |
| A1 | M1: tái lập môi trường kiểm thử từ gói bàn giao. | Thực hiện M2-M5 trên môi trường riêng; không dùng bí mật hoặc tệp cá nhân ngoài gói hướng dẫn. Kết thúc bằng bằng chứng tái lập. |
| E1 | M2 hoặc M3: thiếu cấu hình, lỗi cập nhật dữ liệu hoặc dịch vụ phụ thuộc chưa sẵn sàng. | Ghi trạng thái chưa sẵn sàng và MSG-SYS-004 an toàn; không mở môi trường như đã hoạt động đầy đủ. Sửa nguyên nhân và kiểm lại từ bước bị ảnh hưởng. |
| E2 | M4: dịch vụ thực chưa được kiểm chứng. | Ghi rõ kiểm chứng chưa đạt hoặc chưa thực hiện; không thay bằng kết quả giả lập để tuyên bố đạt. Kết thúc chưa đủ điều kiện bàn giao. |

**Truy vết:** IH-MSG-001, IH-MSG-003, IH-INT-001, IH-INT-002, IH-INT-003, IH-INT-004, IH-NFR-004, IH-NFR-005, IH-NFR-008, IH-NFR-010, IH-REL-001, IH-REL-002, IH-REL-003; UAT-16, UAT-18.

<a id="uc-16"></a>

### UC-16: Sao lưu dữ liệu

- **Mục tiêu:** Tạo bản sao lưu thủ công nhất quán để kiểm chứng khả năng khôi phục dữ liệu R1.
- **Tác nhân:** Người vận hành; công cụ cơ sở dữ liệu và lưu trữ hỗ trợ.
- **Kích hoạt:** Người vận hành sao lưu trước khi phát hành hoặc cập nhật cấu trúc dữ liệu có sẵn, và trước lần kiểm chứng UC-09.
- **Tiền điều kiện:** Có quyền đọc dữ liệu vận hành, vị trí lưu trữ được phép và thông tin cấu hình cần thiết.
- **Dữ liệu đầu vào:** Dữ liệu nghiệp vụ, tệp nguồn, phiên bản và thời điểm sao lưu; danh mục thành phần được xác định trong hướng dẫn vận hành.
- **Kết quả đầu ra:** Hệ thống tạo bản sao lưu kèm danh mục thành phần, thời điểm và kết quả kiểm tra tính đầy đủ, khả năng đọc và tính nhất quán.
- **Hậu điều kiện thành công:** Bản sao lưu đọc được, đủ thành phần, được ghi thời điểm và phiên bản, lưu giữ theo LIM-13.
- **Bảo đảm tối thiểu:** Không gọi bản sao lưu chưa hoàn tất là hợp lệ; không làm lộ dữ liệu qua giao diện người dùng; lỗi sao lưu không làm thay đổi dữ liệu nghiệp vụ.

**Luồng chính**

| Bước | Tương tác |
| --- | --- |
| M1 | Người vận hành chủ động bắt đầu một lần sao lưu có định danh và thời điểm. |
| M2 | Công cụ vận hành thu thập dữ liệu, tệp và thông tin phiên bản theo quy trình bảo đảm tính nhất quán. |
| M3 | Kiểm tra đủ thành phần và khả năng đọc; chỉ đánh dấu hợp lệ khi kiểm tra thành công. |
| M4 | Lưu danh mục, thời điểm và kết quả; kiểm tra quyền đọc và xóa bản hết hạn theo LIM-13. Có thể thực hiện bằng công cụ hoặc lệnh vận hành sẵn có. |
| M5 | Ghi MSG-SYS-003 trong kết quả vận hành. Bản sao lưu được đưa vào danh sách có thể chọn ở UC-09; kết thúc thành công. |

**Luồng thay thế và ngoại lệ**

| Nhánh | Điểm phát sinh | Xử lý và điểm kết thúc hoặc quay lại |
| --- | --- | --- |
| A1 | M1: tạo lại bản sao lưu sau khi sửa lỗi hoặc thay đổi dữ liệu. | Tạo lần sao lưu mới qua M2-M5; giữ rõ định danh và thời điểm để không nhầm bản kiểm chứng. |
| E1 | M2: hết dung lượng, mất kết nối hoặc không có quyền lưu. | Ghi MSG-SYS-004, không đánh dấu hợp lệ; giữ dữ liệu nghiệp vụ và các bản còn hợp lệ theo chính sách. Sửa nguyên nhân rồi bắt đầu lần sao lưu mới. |
| E2 | M3: bản sao lưu thiếu hoặc không đọc được. | Đánh dấu lần sao lưu thất bại, không đưa vào danh sách bản phục hồi hợp lệ; ghi nguyên nhân và kiểm lại sau khi tạo bản mới. |
| E3 | M4: không thực hiện được chính sách lưu giữ. | Ghi nhận không đạt yêu cầu vận hành, xử lý lỗi quyền hoặc lưu trữ; không bỏ qua chính sách lưu giữ tại LIM-13. |

**Truy vết:** IH-MSG-001, IH-NFR-008, IH-NFR-009, IH-REL-001, IH-REL-002; LIM-13, LIM-18; UAT-16, UAT-18.

<a id="muc-7"></a>

## 7. Yêu cầu chức năng

Tất cả yêu cầu trong mục này là bắt buộc cho sản phẩm R1. Các điều kiện BR và LIM áp dụng xuyên suốt; mỗi AC mang mã riêng để truy vết tới trường hợp kiểm thử.

### 7.1 Tài khoản và xác thực

#### IH-AUTH-001: Đăng ký tài khoản bằng email và mật khẩu

**Yêu cầu:** Hệ thống phải cho phép người chưa đăng nhập tạo tài khoản bằng email, tên hiển thị, mật khẩu và xác nhận mật khẩu.

- **IH-AUTH-001-AC01:** Khi email chưa được đăng ký và dữ liệu hợp lệ, hệ thống tạo đúng một tài khoản ở trạng thái `PendingVerification`, gửi email xác minh và hướng dẫn bước tiếp theo. Tài khoản chưa được truy cập dữ liệu nghiệp vụ.
- **IH-AUTH-001-AC02:** Email sai định dạng, mật khẩu ngoài LIM-01 hoặc xác nhận không khớp phải bị từ chối. Đăng ký lặp không tạo tài khoản thứ hai và không cấp phiên cho tài khoản đã có.

**Truy vết:** UC-01; UAT-01; BR-02; LIM-01

#### IH-AUTH-002: Xác minh email

**Yêu cầu:** Hệ thống phải kích hoạt tài khoản đăng ký bằng email và mật khẩu sau khi xác minh quyền kiểm soát email.

- **IH-AUTH-002-AC01:** Liên kết xác minh hợp lệ chuyển tài khoản sang trạng thái `Active`. Với liên kết sai, hết hạn hoặc đã sử dụng, hệ thống không kích hoạt tài khoản và hướng dẫn gửi liên kết mới.
- **IH-AUTH-002-AC02:** Gửi lại email tuân thủ LIM-09; tài khoản chưa xác minh chỉ truy cập được các thao tác xác minh và đăng xuất.

**Truy vết:** UC-01; UAT-01; LIM-08; LIM-09

#### IH-AUTH-003: Đăng nhập bằng email và mật khẩu

**Yêu cầu:** Hệ thống phải xác thực thông tin đăng nhập bằng email và mật khẩu, sau đó tạo phiên cho tài khoản ở trạng thái `Active`.

- **IH-AUTH-003-AC01:** Sau khi đăng nhập thành công, hệ thống mở danh sách Notebook của đúng người dùng. Trường hợp sai email hoặc sai mật khẩu đều hiển thị cùng một thông báo đăng nhập thất bại.
- **IH-AUTH-003-AC02:** Đăng nhập sai liên tiếp vượt LIM-09 phải bị giới hạn; thử đăng nhập bằng API cũng chịu cùng kiểm soát với giao diện.

**Truy vết:** UC-10; UAT-01; BR-02; LIM-09

#### IH-AUTH-004: Đăng nhập bằng Google

**Yêu cầu:** Hệ thống phải hỗ trợ xác thực bằng Google và ánh xạ danh tính đã được nhà cung cấp xác minh vào tài khoản ứng dụng.

- **IH-AUTH-004-AC01:** Khi Google xác thực thành công một danh tính mới có email đã xác minh, hệ thống tạo tài khoản ở trạng thái `Active`. Các lần đăng nhập tiếp theo phải truy cập đúng tài khoản đó và giữ nguyên dữ liệu.
- **IH-AUTH-004-AC02:** Khi người dùng hủy đăng nhập, phản hồi xác thực không hợp lệ, token không hợp lệ hoặc email chưa được xác minh, hệ thống không được tạo phiên hay hoàn tất việc tạo tài khoản ứng dụng.

**Truy vết:** UC-11; UAT-02; BR-02; BR-03

#### IH-AUTH-005: Liên kết danh tính có cùng địa chỉ email

**Yêu cầu:** Hệ thống phải yêu cầu xác minh quyền kiểm soát tài khoản hiện hữu trước khi liên kết danh tính Google có cùng địa chỉ email.

- **IH-AUTH-005-AC01:** Với tài khoản `Active`, chỉ liên kết sau khi phản hồi Google hợp lệ và mật khẩu hiện tại được xác nhận trong đúng giao dịch theo LIM-19. Hai phương thức sau liên kết dẫn tới cùng tài khoản và dữ liệu.
- **IH-AUTH-005-AC02:** Xác nhận thất bại, bằng chứng hết hạn hoặc sửa email/định danh trong yêu cầu API không tạo liên kết hay cấp phiên; các liên kết và dữ liệu cũ được giữ nguyên.
- **IH-AUTH-005-AC03:** Với tài khoản `PendingVerification` đã được tạo bằng một mật khẩu trước đó, phải hoàn tất UC-02.A4 rồi bắt đầu lại Google và xác nhận mật khẩu mới. Mật khẩu, phiên hạn chế và liên kết cũ không còn dùng được trước khi cấp quyền nghiệp vụ; xác minh email đơn thuần không thay thế bước này.
- **IH-AUTH-005-AC04:** EML-003 được tạo sau khi liên kết thành công; lỗi chuyển giao email không làm mất liên kết hoặc yêu cầu người dùng liên kết lại.

**Truy vết:** UC-11; UC-02; UAT-02; UAT-03; BR-02; BR-03; LIM-07; LIM-08; LIM-19

#### IH-AUTH-006: Yêu cầu khôi phục mật khẩu

**Yêu cầu:** Hệ thống phải tiếp nhận yêu cầu khôi phục mật khẩu và gửi hướng dẫn khôi phục tới email phù hợp.

- **IH-AUTH-006-AC01:** Giao diện hiển thị cùng một thông báo cho email có tài khoản và email chưa có tài khoản. Nếu tài khoản có mật khẩu, hệ thống gửi liên kết đặt lại mật khẩu. Nếu tài khoản chỉ đăng nhập bằng Google, hệ thống gửi hướng dẫn đăng nhập Google và không tự thêm phương thức đăng nhập bằng mật khẩu.
- **IH-AUTH-006-AC02:** Việc gửi email phải tuân theo LIM-09. Khi dịch vụ gửi email gặp lỗi, người dùng có thể thử lại; hệ thống không được đổi mật khẩu hoặc khóa tài khoản vĩnh viễn do lỗi gửi thư.

**Truy vết:** UC-02; UAT-03; LIM-08; LIM-09

#### IH-AUTH-007: Đặt lại mật khẩu

**Yêu cầu:** Hệ thống phải cho phép người dùng đặt mật khẩu mới khi có liên kết đặt lại mật khẩu hợp lệ.

- **IH-AUTH-007-AC01:** Khi liên kết hợp lệ và mật khẩu mới đáp ứng LIM-01, hệ thống cập nhật mật khẩu, thu hồi phiên cũ theo LIM-07 và yêu cầu đăng nhập lại.
- **IH-AUTH-007-AC02:** Liên kết sai, hết hạn hoặc đã dùng không đổi mật khẩu. Sau khi đặt lại thành công, mật khẩu cũ và liên kết đã dùng đều bị từ chối.
- **IH-AUTH-007-AC03:** Với tài khoản `PendingVerification`, đặt lại thành công phải vô hiệu toàn bộ phiên hạn chế, liên kết xác minh và khôi phục cũ trước khi chuyển `Active`. Không tự cấp phiên hoặc liên kết Google; nếu bước vô hiệu không hoàn tất, tiếp tục chặn quyền nghiệp vụ theo UC-02.A4.

**Truy vết:** UC-02; UAT-03; LIM-01; LIM-07; LIM-08

#### IH-AUTH-008: Quản lý phiên đăng nhập và đăng xuất

**Yêu cầu:** Hệ thống phải quản lý hiệu lực phiên và kết thúc phiên khi người dùng đăng xuất.

- **IH-AUTH-008-AC01:** Khi tải lại trang trong phiên còn hiệu lực, hệ thống giữ đúng tài khoản đang đăng nhập. Khi phiên hết hạn hoặc người dùng đăng xuất, hệ thống chuyển về màn hình đăng nhập và xóa dữ liệu cá nhân khỏi bộ nhớ giao diện.
- **IH-AUTH-008-AC02:** Yêu cầu xử lý mới dùng phiên đã đăng xuất phải bị từ chối; kết quả AI hoàn tất sau khi phiên hết hiệu lực không được chuyển tới phía ứng dụng khách chưa tái xác thực.

**Truy vết:** UC-01; UC-02; UC-10; UC-11; UC-13; UC-14; UAT-04; LIM-07

#### IH-AUTH-009: Xem và cập nhật hồ sơ cá nhân

**Yêu cầu:** Hệ thống phải cho người dùng xem và cập nhật hồ sơ cá nhân.

- **IH-AUTH-009-AC01:** Hồ sơ cá nhân hiển thị email, tên hiển thị, phương thức đăng nhập và trạng thái xác minh. Thay đổi tên đáp ứng LIM-01 phải được lưu và hiển thị đúng sau khi đăng nhập lại.
- **IH-AUTH-009-AC02:** Hệ thống cung cấp ảnh đại diện mặc định và hiển thị ảnh đại diện Google nếu có. Người dùng được chọn lại ảnh mặc định. Trong R1, chức năng sửa hồ sơ không cho đổi email, tải ảnh lên hoặc thay đổi nhà cung cấp xác thực.

**Truy vết:** UC-12; UAT-04; LIM-01

#### IH-AUTH-010: Đổi mật khẩu

**Yêu cầu:** Hệ thống phải cho tài khoản có mật khẩu đổi mật khẩu sau khi tái xác thực.

- **IH-AUTH-010-AC01:** Sau khi tái xác thực thành công, nếu mật khẩu mới hợp lệ, hệ thống cập nhật mật khẩu, thu hồi các phiên cũ theo LIM-07 và yêu cầu đăng nhập lại.
- **IH-AUTH-010-AC02:** Tái xác thực sai không thay đổi tài khoản; tài khoản chỉ dùng Google không hiển thị chức năng đổi mật khẩu của ứng dụng.

**Truy vết:** UC-13; UAT-03; LIM-01; LIM-07

### 7.2 Quản lý Notebook

#### IH-NB-001: Tạo và xem danh sách Notebook

**Yêu cầu:** Hệ thống phải cho người dùng tạo Notebook và xem danh sách Notebook của mình.

- **IH-NB-001-AC01:** Notebook được tạo thành công phải có định danh riêng và chủ sở hữu xác định từ phiên đăng nhập. Danh sách có phân trang và mặc định sắp xếp theo thời điểm cập nhật mới nhất.
- **IH-NB-001-AC02:** Hệ thống từ chối tên rỗng, tên vượt giới hạn hoặc yêu cầu tạo Notebook thứ 21 đang hoạt động. Danh sách không được trả về thông tin của Notebook thuộc tài khoản khác.

**Truy vết:** UC-03; UAT-05; BR-01; LIM-02

#### IH-NB-002: Mở và cập nhật Notebook

**Yêu cầu:** Hệ thống phải hiển thị nội dung Notebook và cho chủ sở hữu sửa tên, mô tả.

- **IH-NB-002-AC01:** Màn hình Notebook hiển thị đúng tài liệu, hội thoại, ghi chú và kết quả AI thuộc Notebook đó. Thay đổi hợp lệ đối với tên hoặc mô tả phải được lưu.
- **IH-NB-002-AC02:** Yêu cầu xử lý dùng phiên bản cũ nhận thông báo xung đột; sửa tên không đổi định danh nguồn hoặc nội dung kết quả AI đã sinh.

**Truy vết:** UC-03; UAT-05; BR-11; BR-12

#### IH-NB-003: Xóa Notebook

**Yêu cầu:** Hệ thống phải cho chủ sở hữu xóa Notebook sau khi xác nhận phạm vi dữ liệu sẽ bị xóa.

- **IH-NB-003-AC01:** Thông báo xác nhận phải nêu rõ tài liệu, hội thoại, ghi chú và kết quả AI trong Notebook sẽ bị xóa. Nếu người dùng hủy thao tác, toàn bộ dữ liệu được giữ nguyên.
- **IH-NB-003-AC02:** Sau khi xóa thành công, không thể truy cập Notebook và tài nguyên con qua đường dẫn hoặc API; tác vụ đang chạy không tạo lại dữ liệu. Xóa dữ liệu vật lý theo LIM-13.

**Truy vết:** UC-03; UAT-12; BR-09; LIM-13

#### IH-NB-004: Kiểm soát quyền truy cập tài nguyên

**Yêu cầu:** Hệ thống phải kiểm tra quyền sở hữu đối với mọi thao tác trên Notebook và tài nguyên con.

- **IH-NB-004-AC01:** Hai tài khoản thử đọc, sửa, xóa, tải xuống, hỏi đáp và sinh nội dung trên tài nguyên của nhau đều bị từ chối mà không lộ nội dung hoặc thông tin mô tả.
- **IH-NB-004-AC02:** Thay `owner_id`, `notebook_id` hoặc `document_id` trong yêu cầu xử lý không cấp thêm quyền; truy xuất chỉ mục, bộ nhớ đệm và liên kết nguồn chịu cùng giới hạn.

**Truy vết:** UC-03 đến UC-08; UAT-13; BR-01; BR-04

### 7.3 Tiếp nhận và quản lý tài liệu

#### IH-DOC-001: Tiếp nhận và kiểm tra tệp

**Yêu cầu:** Hệ thống phải nhận tài liệu thuộc các định dạng và giới hạn R1 trong Notebook của người dùng.

- **IH-DOC-001-AC01:** Khi tiếp nhận tệp hợp lệ, hệ thống tạo bản ghi ở trạng thái `Processing` và lưu tên, kích thước, định dạng tệp. Việc xác định định dạng phải kiểm tra nội dung tệp, không chỉ dựa vào phần mở rộng.
- **IH-DOC-001-AC02:** Tệp sai loại, vượt LIM-03 hoặc LIM-04, PDF chỉ có ảnh, PDF được mã hóa, tệp rỗng hoặc không trích được văn bản phải bị từ chối hoặc chuyển `Failed` có lý do.

**Truy vết:** UC-04; UAT-06; LIM-03; LIM-04

#### IH-DOC-002: Trích xuất văn bản và lập chỉ mục tài liệu

**Yêu cầu:** Hệ thống phải chuẩn bị văn bản và chỉ mục đầy đủ trước khi đưa tài liệu sang `Ready`.

- **IH-DOC-002-AC01:** Tài liệu `Ready` có văn bản và vị trí nguồn có thể kiểm tra; có thể tìm kiếm và hỏi đáp về nội dung của tài liệu sau xử lý.
- **IH-DOC-002-AC02:** Lỗi trích xuất văn bản, tạo embedding hoặc lưu chỉ mục không được làm tài liệu chuyển sang `Ready`. Chỉ mục chưa hoàn tất không được sử dụng để truy xuất.

**Truy vết:** UC-04; UAT-06; BR-04; LIM-11

#### IH-DOC-003: Theo dõi trạng thái và xử lý lại tài liệu

**Yêu cầu:** Hệ thống phải hiển thị trạng thái và nguyên nhân xử lý thất bại của tài liệu. Chủ sở hữu được yêu cầu xử lý lại tài liệu ở trạng thái `Failed` khi đầu vào vẫn đáp ứng các điều kiện quy định.

- **IH-DOC-003-AC01:** Danh sách tài liệu hiển thị đúng trạng thái `Processing`, `Ready` hoặc `Failed`, kể cả sau khi tải lại trang. Tài liệu `Failed` phải có lý do lỗi và thao tác thử lại hoặc xóa.
- **IH-DOC-003-AC02:** Thử lại tạo lần xử lý mới cho cùng tài liệu, không tạo trùng các đoạn văn bản hoặc tài liệu; quá LIM-11 chuyển `Failed` và loại kết quả muộn.

**Truy vết:** UC-04; UAT-07; BR-10; LIM-11

#### IH-DOC-004: Xử lý tệp trùng và yêu cầu tải lên gửi lặp

**Yêu cầu:** Hệ thống phải phát hiện tệp có nội dung trùng trong cùng Notebook và nhận diện yêu cầu tải lên được gửi lại, để tránh tạo nhiều bản ghi cho cùng một tài liệu hoặc thao tác.

- **IH-DOC-004-AC01:** Nếu tệp tải lên trùng toàn bộ nội dung byte với một tài liệu chưa xóa trong cùng Notebook, hệ thống trả về tài liệu đã có hoặc thông báo trùng kèm liên kết mở tài liệu. Không tạo bản ghi tài liệu thứ hai.
- **IH-DOC-004-AC02:** Yêu cầu tải lên gửi lại cùng mã thao tác phải trả cùng kết quả theo LIM-12. Cùng một tệp ở Notebook khác được xem là nguồn độc lập; không tiết lộ việc tệp đó tồn tại trong tài khoản của người khác.

**Truy vết:** UC-04; UAT-07; BR-10; LIM-12

#### IH-DOC-005: Xem nội dung tài liệu và vị trí tham chiếu

**Yêu cầu:** Hệ thống phải cho chủ sở hữu xem thông tin mô tả và nội dung trích xuất của tài liệu.

- **IH-DOC-005-AC01:** Hiển thị tên tệp, định dạng, thời điểm tải, trạng thái và văn bản; PDF có số trang, TXT/MD có chỉ số đoạn hoặc tiêu đề để định vị.
- **IH-DOC-005-AC02:** Khi mở tham chiếu nguồn, hệ thống hiển thị đúng tài liệu và đoạn văn bản liên quan. Nếu tài liệu nguồn đã bị xóa, hệ thống thông báo nguồn không còn khả dụng và không cung cấp nội dung từ bản lưu trong bộ nhớ đệm.

**Truy vết:** UC-04; UC-05; UC-07; UAT-06; UAT-08; UAT-12; BR-07; BR-08

#### IH-DOC-006: Xóa tài liệu

**Yêu cầu:** Hệ thống phải cho chủ sở hữu xóa tài liệu và loại nguồn khỏi hoạt động khai thác.

- **IH-DOC-006-AC01:** Sau xác nhận xóa, tài liệu không còn trong tập nguồn mới và danh sách hoạt động; các tác vụ đang dùng nguồn đó kết thúc `Failed` với lý do nguồn không còn.
- **IH-DOC-006-AC02:** Kết quả đã lưu trước lúc xóa giữ nguyên nhưng báo nguồn đã xóa; tệp, văn bản và chỉ mục được xóa theo LIM-13. Xóa tài liệu không tự xóa ghi chú độc lập.

**Truy vết:** UC-04; UC-08; UAT-12; BR-08; LIM-13

### 7.4 Hỏi đáp từ tài liệu bằng RAG

#### IH-CHAT-001: Gửi câu hỏi và chọn tài liệu nguồn

**Yêu cầu:** Hệ thống phải cho người dùng đặt câu hỏi trong một Notebook với phạm vi nguồn xác định.

- **IH-CHAT-001-AC01:** Mặc định, hệ thống sử dụng các tài liệu `Ready` trong Notebook; người dùng có thể chọn một tập con. Hệ thống phải lưu câu hỏi, phạm vi nguồn và thời điểm gửi.
- **IH-CHAT-001-AC02:** Câu hỏi rỗng, quá LIM-06, nguồn khác Notebook, nguồn không `Ready` hoặc tập nguồn rỗng bị từ chối trước khi gọi mô hình.

**Truy vết:** UC-05; UAT-08; BR-04; BR-05; LIM-06

#### IH-CHAT-002: Tạo câu trả lời kèm tham chiếu nguồn

**Yêu cầu:** Hệ thống phải tạo câu trả lời từ nội dung truy xuất phù hợp thuộc tập nguồn hợp lệ.

- **IH-CHAT-002-AC01:** Câu trả lời ở trạng thái `Answered` phải có nội dung và tham chiếu xác định đúng tài liệu, vị trí nguồn. Các phát biểu trong câu trả lời phải được đối chiếu với đoạn nguồn theo AEV-01.
- **IH-CHAT-002-AC02:** Tham chiếu nguồn không thuộc tập nguồn hoặc không tồn tại không được công bố như tham chiếu nguồn hợp lệ; nếu không sửa được trong thời hạn xử lý, trả lỗi tạo kết quả thay vì `Answered`.

**Truy vết:** UC-05; UAT-08; BR-07; BR-13; AEV-01

#### IH-CHAT-003: Phân biệt kết quả thiếu căn cứ với lỗi xử lý

**Yêu cầu:** Hệ thống phải trả trạng thái `NoEvidence` khi tài liệu không đủ căn cứ trả lời và trạng thái `Failed` khi có lỗi kỹ thuật hoặc điều kiện xử lý không còn hợp lệ.

- **IH-CHAT-003-AC01:** Khi nguồn không đủ trả lời, lưu `NoEvidence` và thông báo người dùng bổ sung tài liệu hoặc làm rõ câu hỏi; không tự trả lời bằng tri thức ngoài nguồn.
- **IH-CHAT-003-AC02:** Khi nhà cung cấp gặp lỗi, hết hạn mức sử dụng, vượt thời gian chờ hoặc mất quyền truy cập, hệ thống ghi trạng thái `Failed`, mã lỗi và hướng xử lý phù hợp. Không được ghi lỗi kỹ thuật thành `NoEvidence`.

**Truy vết:** UC-05; UAT-09; BR-13; LIM-11

#### IH-CHAT-004: Quản lý hội thoại

**Yêu cầu:** Hệ thống phải lưu và cho chủ sở hữu mở lại hội thoại trong Notebook.

- **IH-CHAT-004-AC01:** Người dùng tạo được hội thoại và xem danh sách trong Notebook thuộc quyền; lịch sử các lượt hiển thị theo thứ tự tạo, giữ nguyên sau tải lại hoặc khởi động lại dịch vụ.
- **IH-CHAT-004-AC02:** Mỗi lượt lưu câu hỏi, kết quả, trạng thái, nguồn và thời điểm theo mục 8. Giao diện nêu mỗi câu hỏi được xử lý độc lập, không dùng ngữ cảnh từ các lượt trước.
- **IH-CHAT-004-AC03:** Đổi tên hợp lệ cập nhật đúng hội thoại và phiên bản; xung đột không ghi đè bản mới theo BR-12.
- **IH-CHAT-004-AC04:** Xác nhận xóa loại hội thoại và các lượt khỏi truy cập; hủy xác nhận giữ dữ liệu. Ghi chú đã sao chép không bị xóa theo.
- **IH-CHAT-004-AC05:** Khi nguồn cuối cùng đã bị xóa, chủ sở hữu vẫn xem, đổi tên và xóa được hội thoại. Tham chiếu nguồn có thông báo không còn khả dụng; gửi câu hỏi mới với tập nguồn rỗng bị từ chối.

**Truy vết:** UC-05; UAT-08; UAT-12; BR-08; BR-12

#### IH-CHAT-005: Kiểm soát gửi lặp, thử lại và điều kiện công bố câu trả lời

**Yêu cầu:** Hệ thống phải nhận diện yêu cầu hỏi đáp gửi lặp, cho phép thử lại yêu cầu đã thất bại và kiểm tra lại quyền truy cập cùng trạng thái tài liệu nguồn trước khi công bố câu trả lời.

- **IH-CHAT-005-AC01:** Nhấn gửi lặp cùng mã thao tác không tạo nhiều lượt; thử lại lỗi có định danh mới và giữ quan hệ với lượt đã lỗi.
- **IH-CHAT-005-AC02:** Nguồn hoặc Notebook bị xóa trước khi công bố kết quả làm yêu cầu xử lý thất bại; không trả nội dung từ tập nguồn đã mất hiệu lực.

**Truy vết:** UC-05; UAT-09; UAT-12; BR-08; BR-09; BR-10

### 7.5 Quản lý ghi chú

#### IH-NOTE-001: Quản lý ghi chú

**Yêu cầu:** Hệ thống phải cho chủ sở hữu tạo, xem danh sách và nội dung, sửa và xóa ghi chú trong Notebook.

- **IH-NOTE-001-AC01:** Tạo ghi chú hợp lệ lưu tiêu đề, nội dung, thời điểm và phiên bản; xem danh sách và mở lại giữ đúng nội dung sau tải lại trang.
- **IH-NOTE-001-AC02:** Dữ liệu vượt LIM-06 bị máy chủ từ chối; giao diện hiển thị lỗi tại trường và giữ phần nhập hợp lệ để sửa.
- **IH-NOTE-001-AC03:** Sửa ghi chú ở phiên bản hiện hành lưu nội dung mới và tăng phiên bản. Cập nhật bằng phiên bản cũ bị từ chối và có hướng dẫn tải lại, không ghi đè bản mới.
- **IH-NOTE-001-AC04:** Xác nhận xóa làm ghi chú không còn trong danh sách hoặc đọc được qua API; hủy xác nhận giữ nguyên. Xóa ghi chú không xóa nguồn hoặc kết quả đã sao chép.

**Truy vết:** UC-06; UAT-10; BR-12; LIM-06

#### IH-NOTE-002: Lưu câu trả lời thành ghi chú

**Yêu cầu:** Hệ thống phải cho người dùng lưu câu trả lời `Answered` thành ghi chú độc lập có xuất xứ.

- **IH-NOTE-002-AC01:** Ghi chú mới chứa bản sao nội dung, liên kết lượt hỏi đáp và các tham chiếu nguồn; người dùng được sửa nội dung mà không sửa câu trả lời gốc.
- **IH-NOTE-002-AC02:** Xóa hội thoại hoặc tài liệu nguồn không làm mất ghi chú đã lưu. Khi nguồn xuất xứ không còn, hệ thống hiển thị trạng thái tương ứng. Không cung cấp thao tác lưu câu trả lời cho kết quả ở trạng thái `Failed` hoặc `NoEvidence`.

**Truy vết:** UC-06; UAT-10; UAT-12; BR-08; BR-11

### 7.6 Yêu cầu chung đối với công cụ AI

#### IH-AI-001: Cung cấp đầy đủ năm công cụ AI

**Yêu cầu:** Hệ thống phải cung cấp đầy đủ Mindmap, Tóm tắt, Slide, Quiz và Báo cáo trong Notebook.

- **IH-AI-001-AC01:** Cả năm công cụ đều có thao tác mở, mô tả kết quả và màn hình cấu hình. Mỗi công cụ phải xử lý được đầu vào hợp lệ bằng mô hình AI thực.
- **IH-AI-001-AC02:** Giao diện mẫu, nút bấm chưa có xử lý hoặc kết quả trả sẵn không được xem là công cụ hoàn chỉnh. Cả năm nhóm yêu cầu IH-MM, IH-SUM, IH-SLD, IH-QUIZ và IH-RPT đều phải đạt.

**Truy vết:** UC-07; UAT-11; OBJ-03

#### IH-AI-002: Chọn tài liệu nguồn và kiểm tra cấu hình công cụ

**Yêu cầu:** Hệ thống phải yêu cầu người dùng chọn nguồn hợp lệ và cấu hình trước khi chạy công cụ AI.

- **IH-AI-002-AC01:** Hiển thị tên tài liệu đã chọn và cấu hình công cụ; 1-3 nguồn `Ready` cùng Notebook được xử lý theo LIM-05.
- **IH-AI-002-AC02:** Nguồn quá giới hạn, không hợp lệ hoặc không đủ căn cứ không được cắt ngầm; trả lỗi đầu vào hoặc `NoEvidence` đúng nguyên nhân.

**Truy vết:** UC-07; UAT-11; BR-04; BR-05; BR-15; LIM-05

#### IH-AI-003: Xử lý tác vụ và lưu kết quả AI hợp lệ

**Yêu cầu:** Hệ thống phải theo dõi quá trình xử lý của từng tác vụ công cụ AI và kiểm tra đầu ra theo cấu trúc, nguồn cùng giới hạn của công cụ trước khi lưu kết quả thành công.

- **IH-AI-003-AC01:** Tác vụ hiển thị trạng thái `Processing`, sau đó kết thúc bằng `Succeeded`, `NoEvidence` hoặc `Failed`. Trước khi lưu kết quả `Succeeded`, hệ thống phải kiểm tra cấu trúc theo từng công cụ và lưu đầy đủ nội dung, nguồn, cấu hình cùng thông tin về quá trình tạo nội dung.
- **IH-AI-003-AC02:** Nếu hết thời hạn xử lý mà đầu ra vẫn sai cấu trúc hoặc không đáp ứng ràng buộc, tác vụ phải chuyển sang `Failed`. Không lưu chuỗi thông báo lỗi hoặc đầu ra thô chưa hợp lệ như một kết quả AI thành công.

**Truy vết:** UC-07; UAT-11; UAT-14; BR-11; LIM-11

#### IH-AI-004: Lưu và truy cập nguồn của nội dung AI

**Yêu cầu:** Hệ thống phải lưu thông tin tài liệu nguồn và vị trí tham chiếu của nội dung AI, đồng thời cho chủ sở hữu mở nguồn khi tài liệu còn được phép truy cập.

- **IH-AI-004-AC01:** Kết quả AI có danh sách tài liệu đã dùng; mỗi phần nội dung chính có tham chiếu nguồn theo vị trí: nhánh Mindmap, ý chính Tóm tắt, slide nội dung, câu Quiz và phần Báo cáo.
- **IH-AI-004-AC02:** Máy chủ phải kiểm tra định danh nguồn. Nếu tài liệu nguồn bị xóa sau khi kết quả AI đã được lưu, tham chiếu đó chuyển sang trạng thái không còn khả dụng; không được tự thay bằng nguồn khác.

**Truy vết:** UC-07; UC-08; UAT-11; UAT-12; BR-07; BR-08; BR-13

### 7.7 Tạo sơ đồ tư duy (Mindmap)

#### IH-MM-001: Tạo sơ đồ tư duy

**Yêu cầu:** Hệ thống phải tạo Mindmap thể hiện các ý chính và quan hệ phân cấp trong tài liệu đã chọn.

- **IH-MM-001-AC01:** Đầu ra có một chủ đề gốc, tổng 10-30 nút trong 2-4 cấp, không có vòng lặp; các nhánh chính thể hiện nội dung nguồn và có tham chiếu nguồn.
- **IH-MM-001-AC02:** Nguồn không đủ ý để tạo sơ đồ có giá trị phải trả `NoEvidence`; không lặp hoặc thêm thông tin không có căn cứ để đủ số nút.

**Truy vết:** UC-07; UAT-11; LIM-17; AEV-02

#### IH-MM-002: Xem và sử dụng Mindmap

**Yêu cầu:** Hệ thống phải hiển thị Mindmap dưới dạng sơ đồ cho phép mở rộng, thu gọn và điều hướng giữa các nhánh.

- **IH-MM-002-AC01:** Người dùng có thể mở rộng hoặc thu gọn nhánh, phóng to, thu nhỏ và đưa toàn bộ sơ đồ về khung nhìn. Giao diện phải cung cấp cách đọc đầy đủ các nhãn dài.
- **IH-MM-002-AC02:** Mở lại kết quả AI hiển thị đúng cấu trúc đã lưu; trên thiết bị di động có thao tác điều hướng hoặc chế độ cây đọc được mà không làm mất nút.

**Truy vết:** UC-08; UAT-11; UAT-15; IH-UX-002

### 7.8 Tạo bản tóm tắt

#### IH-SUM-001: Tạo bản tóm tắt

**Yêu cầu:** Hệ thống phải tạo bản tóm tắt ngắn hoặc chi tiết từ tài liệu được chọn.

- **IH-SUM-001-AC01:** Người dùng chọn ngắn 150-250 từ hoặc chi tiết 400-600 từ; kết quả có tổng quan, các ý chính và điểm cần chú ý, kèm tham chiếu nguồn.
- **IH-SUM-001-AC02:** Tóm tắt nhiều tài liệu phải phản ánh các nguồn đã chọn và nêu mâu thuẫn nếu có; nguồn không đủ nội dung phải trả `NoEvidence`, không bổ sung thông tin ngoài tài liệu nguồn để đạt độ dài yêu cầu.

**Truy vết:** UC-07; UAT-11; BR-13; LIM-17; AEV-03

#### IH-SUM-002: Xem bản tóm tắt và lưu thành ghi chú

**Yêu cầu:** Hệ thống phải cho người dùng đọc bản tóm tắt và tạo ghi chú từ nội dung đó.

- **IH-SUM-002-AC01:** Bản tóm tắt hiển thị rõ cấu trúc và mức độ chi tiết đã chọn. Thao tác lưu thành ghi chú tạo bản sao độc lập, kèm liên kết tới kết quả AI gốc và các tham chiếu nguồn.
- **IH-SUM-002-AC02:** Sửa ghi chú không sửa kết quả AI; mở lại kết quả AI giữ nội dung gốc và nguồn tương ứng.

**Truy vết:** UC-08; UC-06; UAT-10; UAT-11; IH-NOTE-001

### 7.9 Tạo bài trình chiếu (Slide)

#### IH-SLD-001: Tạo bài trình chiếu

**Yêu cầu:** Hệ thống phải tạo bộ slide trình bày nội dung tài liệu theo chủ đề người dùng yêu cầu.

- **IH-SLD-001-AC01:** Người dùng chọn 5-8 slide; kết quả có slide tiêu đề, các slide nội dung và slide kết luận, đúng số đã chọn. Mỗi slide nội dung có tiêu đề, 3-5 ý ngắn và tham chiếu nguồn.
- **IH-SLD-001-AC02:** Các slide phải có mạch trình bày nhất quán. Mã lệnh do mô hình tạo không được thực thi trong trình duyệt. Nếu nguồn không đủ căn cứ để tạo nội dung theo yêu cầu, hệ thống trả `NoEvidence`.

**Truy vết:** UC-07; UAT-11; BR-06; LIM-17; AEV-04

#### IH-SLD-002: Xem, trình chiếu và mở lại bài trình chiếu

**Yêu cầu:** Hệ thống phải cho người dùng xem tuần tự và trình chiếu bộ slide đã tạo.

- **IH-SLD-002-AC01:** Giao diện cung cấp thao tác chuyển trang trước, trang sau, số trang hiện tại và chế độ trình chiếu. Người dùng có thể điều khiển bằng bàn phím trên máy tính; nội dung không bị cắt trong khung hiển thị.
- **IH-SLD-002-AC02:** Mở lại kết quả AI giữ thứ tự, số lượng, nội dung và tham chiếu nguồn. R1 không yêu cầu chỉnh bố cục tự do hoặc tải tệp PowerPoint.

**Truy vết:** UC-08; UAT-11; UAT-15; IH-UX-002; IH-UX-003

### 7.10 Tạo bộ câu hỏi trắc nghiệm (Quiz)

#### IH-QUIZ-001: Tạo bộ câu hỏi trắc nghiệm

**Yêu cầu:** Hệ thống phải tạo Quiz gồm 5 hoặc 10 câu hỏi từ tài liệu đã chọn.

- **IH-QUIZ-001-AC01:** Mỗi câu có nội dung, 4 lựa chọn khác nhau, đúng một đáp án đúng, giải thích và tham chiếu nguồn; không trùng câu hỏi trong cùng bộ.
- **IH-QUIZ-001-AC02:** Đáp án được giải thích bằng nguồn; câu hỏi mơ hồ hoặc không đủ căn cứ không được tính là đầu ra đạt. Không đủ nội dung tạo số câu đã chọn phải trả `NoEvidence`.

**Truy vết:** UC-07; UAT-11; LIM-17; AEV-05

#### IH-QUIZ-002: Làm Quiz và xem kết quả chấm điểm

**Yêu cầu:** Hệ thống phải cho người dùng làm Quiz và nhận kết quả chấm bài.

- **IH-QUIZ-002-AC01:** Trước khi nộp, chỉ hiển thị câu hỏi và lựa chọn; khi nộp hiển thị số câu đúng, điểm theo BR-14, đáp án và giải thích từng câu.
- **IH-QUIZ-002-AC02:** Thao tác làm lại tạo một lần làm bài mới, không sửa đề hoặc điểm của lần trước. Kết quả mỗi lần đã nộp phải được lưu và có thể mở lại cùng bộ câu hỏi tương ứng.

**Truy vết:** UC-08; UAT-11; BR-14

### 7.11 Tạo báo cáo

#### IH-RPT-001: Tạo báo cáo theo mục tiêu

**Yêu cầu:** Hệ thống phải tạo báo cáo tổng hợp từ tài liệu đã chọn, theo mục tiêu do người dùng nhập.

- **IH-RPT-001-AC01:** Người dùng nhập mục tiêu 1-1.000 ký tự; báo cáo 600-1.000 từ có tiêu đề, mục tiêu, phạm vi nguồn, tổng quan, phân tích và kết luận; các phần có tham chiếu nguồn.
- **IH-RPT-001-AC02:** Báo cáo phải phân biệt dữ kiện trong nguồn với nhận định hoặc đề xuất do AI tổng hợp, đồng thời nêu mâu thuẫn hoặc thông tin còn thiếu. Không tự thêm số liệu, sử dụng nghiên cứu trên web hoặc đưa ra kết luận vượt quá căn cứ của nguồn.

**Truy vết:** UC-07; UAT-11; BR-13; LIM-05; LIM-17; AEV-06

#### IH-RPT-002: Xem và tải báo cáo Markdown

**Yêu cầu:** Hệ thống phải cho người dùng đọc báo cáo và tải nội dung dưới dạng Markdown.

- **IH-RPT-002-AC01:** Màn hình kết quả hiển thị các phần báo cáo và danh sách nguồn. Người dùng có thể tải tệp `.md` mã hóa UTF-8 gồm nội dung và thông tin nguồn; tiếng Việt phải hiển thị đúng dấu.
- **IH-RPT-002-AC02:** Chỉ chủ sở hữu tải được báo cáo; tệp xuất ghi định danh và tên nguồn, không chứa token, đường dẫn tệp nội bộ hoặc liên kết truy cập bí mật.

**Truy vết:** UC-08; UAT-11; UAT-13; BR-01; BR-07

### 7.12 Quản lý kết quả AI

#### IH-OUT-001: Xem danh sách và nội dung kết quả AI

**Yêu cầu:** Hệ thống phải cho người dùng xem các kết quả AI đã lưu trong Notebook.

- **IH-OUT-001-AC01:** Danh sách hiển thị tên kết quả, loại công cụ, thời điểm tạo và nguồn; mặc định sắp xếp kết quả mới nhất trước. Người dùng có thể lọc theo từng loại trong năm công cụ và mở kết quả bằng giao diện hiển thị tương ứng.
- **IH-OUT-001-AC02:** Tải lại trang hoặc đăng nhập lại không mất kết quả AI đã lưu; kết quả của Notebook hoặc tài khoản khác không xuất hiện trong danh sách.

**Truy vết:** UC-08; UAT-11; UAT-13; BR-01; BR-11

#### IH-OUT-002: Đổi tên và tạo lại kết quả AI

**Yêu cầu:** Hệ thống phải cho chủ sở hữu đổi tên của kết quả AI đã lưu hoặc tạo một kết quả mới từ nguồn và cấu hình được xác nhận lại, đồng thời giữ nguyên nội dung của bản cũ.

- **IH-OUT-002-AC01:** Đổi tên theo LIM-17 chỉ cập nhật thông tin tên, không thay đổi nội dung. Khi chọn **Tạo lại**, người dùng phải xem lại nguồn và cấu hình; hệ thống tạo kết quả AI mới có liên kết với bản trước.
- **IH-OUT-002-AC02:** Nguồn cũ đã xóa hoặc không đủ điều kiện phải yêu cầu chọn nguồn hợp lệ; lỗi tạo lại không xóa hoặc thay nội dung kết quả AI cũ.

**Truy vết:** UC-08; UAT-11; UAT-12; BR-10; BR-11; BR-12

#### IH-OUT-003: Xóa kết quả AI

**Yêu cầu:** Hệ thống phải cho chủ sở hữu xóa kết quả AI sau khi xác nhận.

- **IH-OUT-003-AC01:** Sau khi xóa thành công, kết quả AI không còn trong danh sách và không thể đọc hoặc tải qua đường dẫn trực tiếp. Các lần làm Quiz gắn với kết quả đó cũng phải bị xóa.
- **IH-OUT-003-AC02:** Xóa kết quả AI không xóa tài liệu nguồn hoặc ghi chú đã được sao chép từ kết quả AI; xóa lặp trả kết quả nhất quán.

**Truy vết:** UC-08; UAT-12; BR-09

<a id="muc-8"></a>

## 8. Mô hình dữ liệu và tính toàn vẹn

Mô hình dưới đây xác định dữ liệu nghiệp vụ và quan hệ tối thiểu. Đây là mô hình khái niệm; tài liệu thiết kế giải pháp quyết định bảng, kiểu dữ liệu vật lý và cơ chế lưu trữ.

| Thực thể | Thành phần dữ liệu logic | Quan hệ và ràng buộc |
| --- | --- | --- |
| Người dùng (`User`) | Định danh nội bộ, email chuẩn hóa, tên, ảnh đại diện, trạng thái xác minh, phiên bản hồ sơ, thời điểm tạo và cập nhật. | Một người dùng sở hữu nhiều Notebook; email ứng dụng duy nhất. |
| Danh tính và phiên đăng nhập (`Identity`, `Session`) | Nhà cung cấp, mã định danh do nhà cung cấp xác thực cấp, định danh người dùng; định danh phiên, thời điểm tạo, hết hạn và thu hồi. | Một người dùng đăng nhập bằng email và mật khẩu, bằng Google hoặc bằng cả hai phương thức khi đã liên kết hợp lệ; không lưu mật khẩu dạng rõ. |
| Notebook (`Notebook`) | Định danh, chủ sở hữu, tên, mô tả, phiên bản, thời điểm tạo và cập nhật, trạng thái xóa. | Một chủ sở hữu; tài nguyên con không được chuyển sang chủ sở hữu khác qua cập nhật. |
| Tài liệu (`Document`) | Định danh, định danh Notebook, tên tệp, loại, kích thước, mã băm, trạng thái, văn bản, vị trí nguồn, chỉ mục, lý do lỗi. | Thuộc đúng một Notebook; chỉ `Ready` được khai thác. |
| Hội thoại và lượt hỏi đáp (`Conversation`, `ChatTurn`) | Định danh, định danh Notebook, tiêu đề; câu hỏi, phạm vi nguồn, câu trả lời, trạng thái, tham chiếu nguồn, thông tin mô hình, thời điểm. | Một hội thoại có nhiều lượt; lịch sử độc lập với lần gọi mô hình mới. |
| Ghi chú (`Note`) | Định danh, định danh Notebook, tiêu đề, nội dung, phiên bản, thời điểm, xuất xứ từ hỏi đáp hoặc kết quả AI nếu có. | Bản sao nội dung độc lập; nguồn xuất xứ có thể không còn. |
| Tác vụ tạo nội dung (`GenerationJob`) | Định danh, chủ sở hữu, Notebook, công cụ, nguồn, cấu hình, mã thao tác, trạng thái, các mốc thời gian, lỗi, thông tin mô hình và liên kết lần thử trước nếu có. | Một lần `Succeeded` tạo tối đa một kết quả AI; yêu cầu xử lý lặp không tạo thêm kết quả. |
| Kết quả AI (`Artifact`) | Định danh, Notebook, loại, tên, nội dung có cấu trúc, phiên bản cấu trúc và phiên bản thông tin mô tả, nguồn, cấu hình, thời điểm, mô hình và phiên bản chỉ dẫn cho mô hình, kết quả AI gốc nếu tạo lại. | Nội dung đã sinh bất biến; chỉ tên kết quả được phép sửa; nguồn dùng bản chụp định danh và tên tại thời điểm tạo. |
| Tham chiếu nguồn (`Citation`) | Định danh tài liệu, vị trí trang hoặc đoạn, đoạn trích đã dùng, trạng thái nguồn hiện tại. | Khi nguồn bị xóa, chỉ giữ định danh, tên và dấu hiệu nguồn đã xóa trong tham chiếu nguồn; không cung cấp lại đoạn trích nguồn. Nội dung kết quả đã lưu tuân theo BR-08. |
| Lần làm bài (`QuizAttempt`) | Định danh, định danh kết quả AI, lựa chọn của người dùng, số câu đúng, tổng câu, điểm, thời điểm nộp, trạng thái đang làm/đã nộp. | Gắn với đề đã lưu; làm lại tạo bản ghi mới, không thay điểm cũ. |
| Bản ghi thao tác (`OperationRecord`) | Mã thao tác, mã nhận diện nội dung đầu vào, kết quả và trạng thái, thời điểm hết hạn. | Phạm vi theo người dùng và loại thao tác; giữ theo LIM-12. |
| Lần xử lý tài liệu (`IngestionAttempt`) | Định danh, tài liệu, lần trước nếu thử lại, thời điểm tiếp nhận, bắt đầu và kết thúc, trạng thái và lỗi. | Nhiều lần xử lý cho cùng tài liệu; chỉ một lần có quyền công bố chỉ mục hiện hành. |
| Sự kiện email (`EmailDelivery`) | Mục đích, người nhận được phép, sự kiện nghiệp vụ, trạng thái chuyển giao, thời điểm và mã tra cứu. | Phục vụ theo dõi việc gửi email trong hệ thống vận hành; không lưu token dạng rõ trong nhật ký. |
| Sự kiện kỹ thuật (`TechnicalEvent`) | Mã yêu cầu xử lý, loại sự kiện, thời điểm, thời lượng, mã lỗi và định danh tài nguyên tối thiểu. | Không chứa nội dung nhạy cảm theo LIM-18; quyền đọc thuộc vận hành. |

Các thành phần trong bảng không đồng nghĩa với trường bắt buộc ở mọi trạng thái. Điều kiện hiện diện được xác định như sau; thiết kế vật lý có thể dùng giá trị rỗng, bảng liên quan hoặc kiểu dữ liệu khác nếu giữ đúng ý nghĩa.

| Đối tượng và trạng thái | Dữ liệu phải có | Dữ liệu chưa có hoặc không áp dụng |
| --- | --- | --- |
| Tài liệu `Processing` | Định danh, Notebook, thông tin tệp, mã thao tác và thời điểm tiếp nhận. | Văn bản, vị trí nguồn hoặc chỉ mục có thể chưa hoàn tất; không dùng phần xử lý dở để truy xuất. |
| Tài liệu `Ready` / `Failed` | `Ready` có văn bản, vị trí nguồn và chỉ mục hoàn chỉnh. `Failed` có mã lỗi, lý do an toàn và thời điểm kết thúc lần xử lý. | `Ready` không có lỗi hiện hành. `Failed` không bắt buộc có văn bản hoặc chỉ mục thành công; không tạo dữ liệu giả để điền trường. |
| Tác vụ `Processing` | Định danh, người dùng, Notebook, nguồn, cấu hình, mã thao tác, thời điểm tiếp nhận và thời hạn. | Chưa có thời điểm kết thúc hoặc kết quả thành công. Thông tin mô hình được bổ sung khi đã xác định cấu hình thực thi. |
| Tác vụ kết thúc | Trạng thái, thời điểm kết thúc; `Succeeded` có kết quả hợp lệ, `Failed` có mã lỗi, `NoEvidence` có lý do thiếu căn cứ. | `Failed` và `NoEvidence` không tạo `Artifact`; quan hệ lần thử trước chỉ có khi thử lại. |
| Lượt hỏi đáp | Mọi lượt có câu hỏi, tập nguồn và thời điểm. `Answered` có câu trả lời và tham chiếu; `NoEvidence` có thông báo thiếu căn cứ; `Failed` có thông tin lỗi an toàn. | Hai trạng thái sau không có câu trả lời khẳng định hoặc tham chiếu giả. |
| Lần làm Quiz đang làm / đã nộp | Đang làm có định danh và đề; đã nộp có lựa chọn, tổng câu, số đúng, điểm và thời điểm nộp. | Điểm và thời điểm nộp chưa tồn tại trước khi nộp; không dùng điểm 0 để biểu thị chưa nộp. R1 không lưu nháp từng lựa chọn. |
| Ghi chú và kết quả AI | Ghi chú luôn có tiêu đề, nội dung, phiên bản; kết quả AI luôn có cấu trúc hợp lệ và nguồn tại thời điểm tạo. | Xuất xứ ghi chú chỉ có khi sao chép; quan hệ kết quả gốc chỉ có khi tạo lại. Nguồn bị xóa được đánh dấu, không cần tạo tài liệu thay thế. |
| Phiên và hồ sơ | Phiên có thời điểm tạo và giới hạn hiệu lực; hồ sơ có tên, email và ảnh mặc định. | Thời điểm thu hồi chỉ có khi thu hồi; ảnh Google chỉ có nếu nhà cung cấp trả dữ liệu phù hợp. |

### 8.1 Tính nhất quán và toàn vẹn dữ liệu

Việc lưu trữ và cập nhật dữ liệu phải đáp ứng các quy tắc sau:

- Định danh được giữ ổn định khi đổi tên. Mọi tài nguyên con phải tham chiếu Notebook hợp lệ; xóa Notebook phải bao phủ đầy đủ quan hệ con.
- Danh sách, nội dung nguồn, chỉ mục và bộ nhớ đệm phải cùng tuân thủ trạng thái xóa. Không được có một đường truy cập cũ vẫn đọc được dữ liệu đã bị chặn.
- Thời điểm được lưu theo chuẩn UTC và hiển thị theo múi giờ của trình duyệt. Các mốc thời gian dùng để đo hiệu năng phải được ghi bằng cùng một nguồn đồng hồ.
- Dữ liệu văn bản lưu UTF-8; xuất Markdown giữ dấu tiếng Việt. ID nguồn do hệ thống quản lý, không lấy tên tệp làm khóa.
- Việc lưu nội dung và chuyển trạng thái thành công phải hoàn tất cùng nhau ở mức nghiệp vụ. Nếu lưu dữ liệu thất bại, hệ thống không được thông báo rằng thao tác đã thành công.
- Dữ liệu dùng chung trong phiên bản nền chưa có xác thực chỉ được chuyển vào Notebook khi đã xác định chủ sở hữu và có thao tác nhập dữ liệu rõ ràng. Không tự gán toàn bộ dữ liệu cũ cho người đăng ký đầu tiên. Bản cài đặt mới R1 không tự nhập dữ liệu minh họa.

### 8.2 Chính sách lưu giữ và xóa dữ liệu

Notebook, tài liệu, hội thoại, ghi chú và kết quả AI được giữ cho đến khi chủ sở hữu xóa hoặc kết thúc môi trường theo chính sách vận hành được thông báo. Xóa nguồn không có nghĩa là xóa mọi nội dung đã được tổng hợp từ nguồn: thông báo xác nhận phải giải thích quy tắc BR-08. Muốn xóa toàn bộ nhóm dữ liệu, người dùng xóa Notebook.

Bản sao lưu là ảnh chụp dữ liệu tại thời điểm tạo, chỉ dành cho người vận hành và không hiển thị trong giao diện người dùng. Bản sao lưu có thể còn nội dung đã xóa sau thời điểm đó cho tới khi hết thời hạn LIM-13. R1 chỉ khôi phục trên môi trường kiểm chứng riêng, không đưa bản lịch sử trở lại môi trường đang phục vụ. Sau kiểm chứng phải dọn dữ liệu tạm; nhật ký và dữ liệu vật lý tuân theo LIM-13, LIM-18. Chính sách này phải được công bố cùng giới hạn xóa tại ứng dụng và điều kiện xử lý dữ liệu của nhà cung cấp.

<a id="data-dictionary"></a>

### 8.3 Từ điển dữ liệu và quy tắc nhập liệu

Các tên trường dưới đây là tên logic để thống nhất ý nghĩa, không bắt buộc tên cột cơ sở dữ liệu hoặc tên thuộc tính API. Giá trị do máy chủ quản lý như chủ sở hữu, trạng thái, điểm, thời điểm và phiên bản không được nhận trực tiếp từ dữ liệu người dùng để tự cấp quyền hoặc xác lập kết quả.

| Nhóm dữ liệu | Đầu vào, giá trị mặc định và kiểm tra | Dữ liệu hệ thống quản lý |
| --- | --- | --- |
| Tài khoản | Email, tên, mật khẩu và xác nhận bắt buộc khi đăng ký; giới hạn LIM-01, chuẩn hóa email theo BR-02. Mật khẩu giữ nguyên chuỗi nhập; xác nhận phải trùng chính xác. | Định danh người dùng, email chuẩn hóa, trạng thái xác minh; mật khẩu do dịch vụ xác thực hoặc thành phần bảo vệ mật khẩu quản lý, không được trả trong API hồ sơ. |
| Hồ sơ | Tên hiển thị bắt buộc; ảnh mặc định hoặc ảnh Google sẵn có. Không nhận đổi email, tải ảnh hoặc tự khai trạng thái xác minh. | Phương thức đăng nhập lấy từ danh tính đã liên kết; thiếu ảnh Google dùng ảnh mặc định. |
| Notebook | Tên bắt buộc, mô tả tùy chọn; bỏ trống mô tả được hiểu là chuỗi rỗng. LIM-02 áp dụng sau chuẩn hóa. | Chủ sở hữu, định danh, phiên bản, thời điểm và trạng thái. Cho phép tên Notebook trùng nhau; phân biệt bằng định danh. |
| Tài liệu | Một tệp cho mỗi thao tác tiếp nhận; chọn nhiều tệp trên giao diện nếu có vẫn xử lý riêng từng tệp. Loại, dung lượng, văn bản theo LIM-03 và LIM-04; không tự cắt bớt nội dung mà không thông báo. | Mã băm theo nội dung byte, định dạng đã kiểm chứng, văn bản, vị trí nguồn, lần xử lý và trạng thái. Tệp trùng tên nhưng khác byte là hai tài liệu khác nhau. |
| Hội thoại | Tiêu đề tùy chọn khi tạo, mặc định “Hội thoại mới”; khi đổi tên phải có 1-120 ký tự. | Notebook, định danh và phiên bản. Không suy diễn ngữ cảnh từ lịch sử cho lượt mới. |
| Lượt hỏi đáp | Câu hỏi bắt buộc, không chỉ gồm khoảng trắng. Không chỉ định nguồn nghĩa là lấy tập `Ready` hiện tại; chỉ định danh sách rỗng là lỗi, không tự thay bằng tất cả nguồn. | Lưu danh sách định danh tài liệu nguồn tại lúc nhận yêu cầu; trạng thái, câu trả lời, tham chiếu, lần xử lý, mô hình và thời điểm. Nguồn thêm sau đó không tự tham gia lượt đang chạy. |
| Ghi chú | Tiêu đề bắt buộc; nội dung có thể rỗng để tạo ghi chú ban đầu; tối đa theo LIM-06. Người dùng chủ động lưu; không yêu cầu tự lưu nháp trong R1. | Phiên bản và xuất xứ. Khi sao chép từ câu trả lời hoặc bản tóm tắt, nếu vượt giới hạn phải cho sửa trước khi lưu, không cắt tự động. |
| Cấu hình công cụ AI | Nguồn phải chọn rõ; hướng dẫn bổ sung tùy chọn tối đa LIM-05. Tóm tắt mặc định ngắn; Slide mặc định 5 trang; Quiz mặc định 5 câu. Mindmap không yêu cầu người dùng nhập số nút. | Lưu đúng cấu hình đã chấp nhận; không tự thay đổi số slide, số câu hoặc độ dài đã được người dùng lựa chọn. |
| Chủ đề Slide và mục tiêu Báo cáo | Chủ đề Slide, mục tiêu Báo cáo đều bắt buộc, 1-1.000 ký tự. Hướng dẫn bổ sung là trường riêng tùy chọn theo LIM-05. | Dùng trong xử lý và lưu cấu hình; không dùng làm chỉ dẫn để bỏ qua phạm vi nguồn. |
| Kết quả AI | Tên ban đầu lấy từ tiêu đề hợp lệ của đầu ra, tối đa LIM-17; nếu thiếu hoặc quá dài, hệ thống dùng tên theo loại công cụ và thời điểm, không cắt nội dung kết quả. Chỉ tên được đổi. | Định danh, công cụ, nguồn, nội dung bất biến, phiên bản cấu trúc, mô hình và quan hệ tạo lại. |
| Lần làm Quiz | Mỗi câu có tối đa một lựa chọn hoặc bỏ trống. Máy chủ từ chối lựa chọn không thuộc câu, câu không thuộc đề hoặc dữ liệu sửa điểm hoặc đáp án. | Định danh lần làm, đề đã lưu, các lựa chọn, điểm và thời điểm nộp; chấm ở máy chủ. |
| Tác vụ và lần thử | Mã thao tác cùng dữ liệu đầu vào; thử lại lỗi dùng lần thử mới; thao tác tạo lại có quan hệ tới kết quả trước. | Trạng thái, thời điểm tiếp nhận, bắt đầu và kết thúc, thời hạn, lỗi, lần trước và mã tra cứu. Không lưu bí mật hoặc toàn văn chỉ dẫn vào nhật ký. |

Quy ước kiểm tra chung:

- Loại khoảng trắng đầu và cuối đối với email, tên, tiêu đề và mục tiêu trước khi kiểm độ dài; không thay khoảng trắng bên trong. Câu hỏi phải có ít nhất một ký tự không phải khoảng trắng; nội dung ghi chú và văn bản nguồn giữ ngắt dòng. Riêng mật khẩu không bị biến đổi hoặc chuẩn hóa Unicode.
- Giới hạn phải kiểm ở máy chủ; giao diện kiểm sớm để hỗ trợ người dùng. Giá trị đúng giới hạn được chấp nhận, vượt một đơn vị bị từ chối. Không chấp nhận số lượng phân số hoặc giá trị ngoài tập lựa chọn.
- Các danh sách không giới hạn ở một trang phải có cách đọc hết dữ liệu, giữ thứ tự ổn định khi thời điểm bằng nhau. Notebook sắp theo cập nhật mới nhất; tài liệu theo thời điểm tải mới nhất; hội thoại và ghi chú theo cập nhật mới nhất; kết quả AI và lần làm Quiz theo thời điểm tạo hoặc nộp bài mới nhất. Trang kế tiếp không được đưa dữ liệu từ Notebook khác. Kích thước trang và cách tải thêm thuộc hợp đồng API và thiết kế giao diện.
- Thời điểm cập nhật Notebook đổi khi sửa tên hoặc mô tả hoặc tạo, sửa, xóa một tài nguyên con thành công; tác vụ chuyển sang trạng thái kết thúc cũng cập nhật thời điểm này. Chỉ đọc hoặc kiểm tra trạng thái không làm thay đổi thứ tự Notebook trong danh sách.
- Dữ liệu chưa lưu trong ghi chú hoặc biểu mẫu sửa phải được cảnh báo khi chuyển màn hình trong ứng dụng. R1 không yêu cầu khôi phục nháp sau đóng trình duyệt hoặc mất phiên; không lưu mật khẩu vào kho nháp.

### 8.4 Cấu trúc logic của đầu ra AI

Mọi kết quả AI thành công phải có loại công cụ, phiên bản cấu trúc, tiêu đề, nội dung, danh mục nguồn đã sử dụng, cấu hình, mô hình, phiên bản chỉ dẫn và thời điểm. Định dạng trao đổi cụ thể được chốt trong hợp đồng tích hợp; các thành phần và ràng buộc dưới đây là bắt buộc.

| Loại | Thành phần nội dung bắt buộc | Kiểm tra trước khi công bố |
| --- | --- | --- |
| Mindmap | Danh sách nút với định danh, nhãn, nút cha và tham chiếu nguồn ở các nhánh chính. | Đúng một gốc; mọi nút còn lại có đúng một cha tồn tại; tất cả nút nối tới gốc, không vòng lặp; 10-30 nút tính cả gốc. Gốc là cấp 1, độ sâu toàn cây từ 2 đến 4 cấp. Nhãn không rỗng. |
| Tóm tắt | Tổng quan; danh sách ý chính có tham chiếu; điểm cần chú ý, gồm mâu thuẫn hoặc thông tin thiếu nếu có; mức độ ngắn hoặc chi tiết. | Đúng độ dài đã chọn trong LIM-17; ý chính không rỗng; nếu không có điểm đặc biệt, nêu rõ không ghi nhận thay vì tạo mâu thuẫn giả. |
| Slide | Danh sách trang có thứ tự; mỗi trang có tiêu đề và được phân loại là trang tiêu đề, trang nội dung hoặc trang kết luận. Trang nội dung có 3-5 ý cùng tham chiếu. | Tổng số trang đúng lựa chọn, bao gồm trang tiêu đề và kết luận. Có đúng một trang tiêu đề đầu tiên và một trang kết luận cuối; không coi mã HTML/JavaScript do mô hình sinh là giao diện được phép thực thi. |
| Quiz | Danh sách câu có định danh, nội dung, bốn lựa chọn có định danh, đáp án đúng, giải thích và tham chiếu. | Đúng 5 hoặc 10 câu; lựa chọn không trùng; đáp án thuộc lựa chọn của câu; chỉ một đáp án đúng. Kiểm tra nội dung theo AEV-05, không chỉ kiểm cấu trúc. Dữ liệu đáp án không được trả qua luồng làm bài trước khi nộp. |
| Báo cáo | Tiêu đề, mục tiêu, phạm vi nguồn, tổng quan, các phần phân tích, kết luận; các phần chính có tham chiếu và phân biệt dữ kiện với nhận định hoặc đề xuất. | 600-1.000 từ theo quy ước mục 5; mục tiêu và nguồn đúng yêu cầu; không tự bổ sung nghiên cứu ngoài nguồn. Tệp Markdown phản ánh nội dung đã lưu. |

Tham chiếu nguồn gồm định danh tài liệu, tên tài liệu được lưu tại thời điểm tạo kết quả và vị trí định vị. Với PDF, số trang bắt đầu từ 1 và trỏ vào văn bản trang đã trích xuất; với TXT/MD, dùng định danh đoạn ổn định trong tài liệu, kèm tiêu đề nếu có. Một phần nội dung có thể gắn nhiều tham chiếu. Không dùng một danh sách tên tệp chung để thay thế việc chỉ ra căn cứ của từng phần chính.

RAG không bắt buộc gửi toàn văn mọi tài liệu cho mô hình. Hệ thống được truy xuất các đoạn phù hợp trong danh sách tài liệu nguồn đã ghi nhận khi tiếp nhận yêu cầu, nhưng phải ghi nhận đoạn thực tế dùng làm căn cứ và không bỏ bớt tài liệu khỏi tập được phép truy xuất một cách ngầm định. Nếu cấu hình mô hình không xử lý được đầu vào công cụ AI trong LIM-05, phải báo lỗi trước khi gọi hoặc đổi cấu hình theo kiểm soát thay đổi; không tự rút ngắn đầu vào để vượt giới hạn mô hình.

### 8.5 Quản lý lần làm Quiz và tác động của thao tác xóa

Mỗi lần làm Quiz có định danh riêng, gắn với người dùng và bộ câu hỏi đã lưu. Trước khi nộp bài, giao diện và API làm bài chỉ cung cấp câu hỏi cùng các lựa chọn; đáp án và giải thích được cung cấp sau khi nộp. Người dùng vẫn có thể xem lại lời giải của các lần đã nộp trước đó.

Khi tiếp nhận bài nộp, máy chủ kiểm tra các lựa chọn, chấm điểm và lưu kết quả. Nếu nhận lại yêu cầu nộp có cùng định danh lần làm, hệ thống trả kết quả đã lưu thay vì tạo thêm kết quả. Khi người dùng chọn làm lại, hệ thống tạo lần làm mới và giữ nguyên kết quả của lần trước.

R1 không yêu cầu lưu từng lựa chọn trước khi nộp bài. Giao diện phải thông báo rằng các lựa chọn chưa nộp có thể mất khi người dùng tải lại hoặc đóng trang. Những lần đã nộp phải được mở lại với đúng lựa chọn, điểm và giải thích đã lưu.

Bảng dưới xác định dữ liệu bị ảnh hưởng khi chủ sở hữu xóa tài nguyên:

| Tài nguyên bị xóa | Dữ liệu bị ngăn truy cập và xóa kèm theo | Dữ liệu được giữ lại | Xử lý tác vụ đang chạy |
| --- | --- | --- | --- |
| Notebook | Tài liệu, nội dung tài liệu và các đoạn văn bản nguồn, hội thoại và các lượt hỏi đáp, ghi chú, kết quả AI, lần làm Quiz, dữ liệu tác vụ nằm trong Notebook. | Chỉ dấu đã xóa và sự kiện kỹ thuật tối thiểu phục vụ chống ghi lại và đối soát theo chính sách lưu giữ. | Không được công bố hoặc tái tạo tài nguyên con. |
| Tài liệu | Tệp, văn bản, đoạn trích trong tham chiếu và chỉ mục thuộc tài liệu. | Nội dung hỏi đáp, ghi chú và kết quả AI đã lưu; định danh, tên tài liệu nguồn và dấu hiệu nguồn đã xóa. | Tác vụ dùng tài liệu phải thất bại, kể cả khi đã lấy đoạn nguồn vào bộ nhớ. |
| Hội thoại | Các lượt hỏi đáp và dữ liệu xử lý thuộc hội thoại. | Ghi chú đã sao chép, tài liệu và kết quả của công cụ AI. | Không được tạo lại lượt hỏi đáp hoặc công bố vào hội thoại đã xóa. |
| Ghi chú | Nội dung ghi chú và xuất xứ của bản ghi đó. | Nguồn, hỏi đáp và kết quả AI gốc. | Không ảnh hưởng tác vụ AI vì ghi chú không là nguồn RAG trong R1. |
| Kết quả AI | Nội dung kết quả và các lần làm Quiz của nó. | Tài liệu, ghi chú đã sao chép; kết quả mới được tạo lại từ nó là tài nguyên độc lập. | Tác vụ tạo lại đã được tiếp nhận tiếp tục nếu Notebook và nguồn vẫn hợp lệ; đánh dấu quan hệ tới kết quả gốc không còn khả dụng. |

Xóa về nghiệp vụ có hiệu lực trước khi trả thành công; dữ liệu vật lý thuộc các nhóm trên được xóa trong thời hạn LIM-13. Bản ghi chống gửi lặp có thể giữ mã thao tác và dấu đã xóa đến hết LIM-12, nhưng không được dùng làm đường đọc lại nội dung đã xóa. Xóa lặp một tài nguyên đã xóa thuộc chính người dùng không khôi phục tài nguyên; tài nguyên không thuộc quyền vẫn dùng phản hồi công khai không tiết lộ sự tồn tại.

Dấu đã xóa dùng để chặn truy cập và kết quả tác vụ đến muộn có thể nằm trong dữ liệu nghiệp vụ hiện hành; không yêu cầu một dịch vụ lưu lịch sử xóa riêng. Khôi phục chỉ thực hiện theo phạm vi cách ly của UC-09. Nếu sau này cần khôi phục dữ liệu lịch sử vào môi trường đang phục vụ, phải đặc tả bổ sung cách áp dụng lại các thao tác xóa trước khi mở truy cập; khả năng đó nằm ngoài R1.

### 8.6 Yêu cầu bảo đảm tính hợp lệ và toàn vẹn dữ liệu

#### IH-DATA-001: Kiểm tra dữ liệu đầu vào và cấu trúc đầu ra

**Yêu cầu:** Hệ thống phải thực hiện các quy tắc dữ liệu tại mục 8.3 và 8.4 nhất quán giữa giao diện, API, lưu trữ và xử lý AI.

- **IH-DATA-001-AC01:** Trường bắt buộc, tùy chọn và giá trị mặc định tuân theo mục 8.3; phân biệt nguồn không chỉ định với danh sách nguồn rỗng và xử lý tên trùng bằng định danh.
- **IH-DATA-001-AC02:** Cấu trúc đầu ra của từng công cụ tuân theo mục 8.4; dữ liệu sai bị từ chối trước công bố. Mở lại kết quả giữ nguyên cấu trúc và nội dung đã lưu.
- **IH-DATA-001-AC03:** Các nhóm dữ liệu văn bản và số áp dụng đúng chuẩn hóa, Unicode và giới hạn ở máy chủ; giá trị đúng biên được chấp nhận, vượt một đơn vị bị từ chối. Kiểm bằng bảng dữ liệu tham số hóa cho các quy tắc dùng chung.
- **IH-DATA-001-AC04:** API từ chối giá trị do người dùng tự gửi để thay chủ sở hữu, trạng thái, điểm hoặc kết quả xác minh; nguồn truy xuất giữ đúng tập đã ghi nhận và tham chiếu không vượt phạm vi.
- **IH-DATA-001-AC05:** Danh sách có thể đọc hết theo thứ tự ổn định; trang tiếp theo không lẫn dữ liệu Notebook khác. Thời điểm cập nhật và cảnh báo chưa lưu tuân theo mục 8.3.
- **IH-DATA-001-AC06:** Các trường có điều kiện được lưu và trả theo trạng thái ở mục 8; không tạo điểm, thời điểm nộp, câu trả lời hoặc chỉ mục giả để đáp ứng ràng buộc bắt buộc.

**Truy vết:** UC-01; UC-03; UC-04; UC-05; UC-06; UC-07; UC-08; UC-12; UAT-05; UAT-06; UAT-08; UAT-10; UAT-11; UAT-20; BR-04; BR-05; BR-07; BR-12; BR-15

#### IH-DATA-002: Bảo toàn kết quả Quiz và xử lý dữ liệu liên quan khi xóa

**Yêu cầu:** Hệ thống phải lưu và bảo toàn kết quả của từng lần làm Quiz đã nộp. Khi xóa một tài nguyên, hệ thống phải chặn truy cập, xóa dữ liệu liên quan và giữ lại các dữ liệu độc lập theo mục 8.5.

- **IH-DATA-002-AC01:** API làm Quiz trước nộp không trả đáp án hoặc giải thích. Giao diện nêu rõ lựa chọn chưa nộp có thể mất khi tải lại; không hứa khôi phục nháp.
- **IH-DATA-002-AC02:** Xóa từng loại tài nguyên chặn truy cập và xử lý đúng dữ liệu liên quan theo mục 8.5; các tài nguyên độc lập được giữ. Dùng cùng dữ liệu đã tạo trong kiểm thử nghiệp vụ để đối chiếu trước và sau xóa.
- **IH-DATA-002-AC03:** Máy chủ chấm đúng các lựa chọn hợp lệ; nộp lặp cùng định danh lần làm trả cùng kết quả; làm lại tạo lần mới, không thay điểm lần trước.
- **IH-DATA-002-AC04:** Tác vụ đến muộn, đường dẫn cũ, bộ nhớ đệm hoặc bản ghi chống gửi lặp không làm đọc lại hay tái tạo dữ liệu đã xóa. Các cơ chế dùng chung được kiểm bằng tình huống đại diện theo mục 13; từng loại tài nguyên vẫn phải có bằng chứng xóa và quyền.

**Truy vết:** UC-03; UC-04; UC-05; UC-06; UC-08; UAT-10; UAT-11; UAT-12; UAT-20; BR-08; BR-09; BR-10; BR-14; LIM-12; LIM-13

<a id="muc-9"></a>

## 9. Giao diện, trải nghiệm và thông báo

Giao diện sản phẩm phải được thiết kế lại và triển khai theo phiên bản Figma đã được chủ sản phẩm phê duyệt. SRS xác định hành vi, màn hình và yêu cầu sử dụng; thiết kế chi tiết là tài liệu liên kết có phiên bản, không thay đổi quy tắc nghiệp vụ của SRS.

| Mã màn hình | Nội dung tối thiểu |
| --- | --- |
| UI-01 Tài khoản | Đăng ký, đăng nhập bằng email và mật khẩu hoặc bằng Google; chờ xác minh email, yêu cầu khôi phục mật khẩu và đặt mật khẩu mới. |
| UI-02 Hồ sơ cá nhân | Thông tin tài khoản, phương thức đăng nhập, sửa tên, chọn ảnh đại diện mặc định, đổi mật khẩu và đăng xuất. |
| UI-03 Danh sách Notebook | Danh sách có phân trang; tạo, sửa tên và mô tả, xác nhận xóa và trạng thái chưa có Notebook. |
| UI-04 Notebook | Tài liệu nguồn, hỏi đáp và lịch sử, ghi chú, năm công cụ AI và danh sách kết quả; luôn hiển thị rõ Notebook đang làm việc. |
| UI-05 Tài liệu nguồn | Trạng thái xử lý, thông tin tài liệu, văn bản trích xuất, vị trí tham chiếu, thông báo lỗi và thao tác thử lại hoặc xóa. |
| UI-06 Cấu hình công cụ AI | Loại công cụ, nguồn đã chọn, cấu hình riêng, giới hạn đầu vào và trạng thái thực thi. |
| UI-07 Kết quả AI | Giao diện hiển thị riêng cho từng công cụ; tên, nguồn, mở lại, tạo lại và xóa kết quả. Có thao tác làm Quiz, trình chiếu Slide và tải báo cáo. |
| UI-08 Ghi chú | Danh sách, tạo, sửa, xuất xứ và xác nhận xóa. |

### IH-UX-001: Tuân thủ thiết kế Figma

**Yêu cầu:** Giao diện phải đáp ứng các màn hình, hành trình và trạng thái của phiên bản thiết kế Figma đã được duyệt.

- **IH-UX-001-AC01:** Hồ sơ cấu hình nghiệm thu phải ghi liên kết Figma, phiên bản, ngày chốt và danh sách màn hình, thành phần giao diện. Việc đối chiếu phải bao phủ bố cục, kiểu chữ, màu sắc, khoảng cách và hành vi tương tác.
- **IH-UX-001-AC02:** Sai khác ảnh hưởng luồng hoặc thành phần chính phải được sửa hoặc ghi nhận thay đổi thiết kế được duyệt; không nghiệm thu chỉ bằng việc có tệp Figma.

**Truy vết:** UC-01; UC-02; UC-03; UC-04; UC-05; UC-06; UC-07; UC-08; UC-10; UC-11; UC-12; UC-13; UC-14; UAT-15

### IH-UX-002: Hiển thị thích ứng và điều hướng giao diện

**Yêu cầu:** Hệ thống phải cho phép người dùng hoàn thành các hành trình chính trên các kích thước và trình duyệt trong LIM-16.

- **IH-UX-002-AC01:** Đăng nhập, tạo Notebook, tải lên, hỏi đáp, chạy từng công cụ và mở kết quả thực hiện được ở máy tính và thiết bị di động; không tràn ngang toàn trang.
- **IH-UX-002-AC02:** Giao diện có điều hướng rõ ràng giữa nguồn tài liệu, hỏi đáp, ghi chú và các công cụ AI. Sơ đồ và bài trình chiếu có vùng điều hướng riêng. Khi chuyển Notebook, hệ thống không được giữ nhầm nguồn hoặc câu trả lời đang chọn từ Notebook trước.

**Truy vết:** UC-01; UC-02; UC-03; UC-04; UC-05; UC-06; UC-07; UC-08; UC-10; UC-11; UC-12; UC-13; UC-14; UAT-15; LIM-16

### IH-UX-003: Khả năng tiếp cận cơ bản

**Yêu cầu:** Giao diện phải hỗ trợ thao tác bàn phím và đọc hiểu các điều khiển chính.

- **IH-UX-003-AC01:** Người dùng thực hiện được các luồng chính bằng phím Tab, Enter và Escape. Vị trí nhận thao tác bàn phím phải nhìn thấy rõ; hộp thoại phải quản lý vị trí này phù hợp. Mỗi trường nhập liệu có nhãn và thông báo lỗi gắn đúng trường.
- **IH-UX-003-AC02:** Văn bản thường có tỷ lệ tương phản tối thiểu 4,5:1; văn bản cỡ lớn tối thiểu 3:1. Không được chỉ dùng màu sắc để truyền đạt trạng thái. Nút chỉ có biểu tượng phải có tên mà công nghệ hỗ trợ có thể đọc được.

**Truy vết:** UC-01; UC-02; UC-03; UC-04; UC-05; UC-06; UC-07; UC-08; UC-10; UC-11; UC-12; UC-13; UC-14; UAT-15

### IH-UX-004: Hiển thị trạng thái và thông báo lỗi

**Yêu cầu:** Hệ thống phải phản hồi rõ các trạng thái rỗng, đang xử lý, thành công và thất bại.

- **IH-UX-004-AC01:** Mọi danh sách có trạng thái rỗng và hành động tiếp theo; thao tác chờ có phản hồi, không cho gửi trùng ngoài ý muốn; xóa có xác nhận phù hợp.
- **IH-UX-004-AC02:** Thông báo lỗi không chứa thông tin truy vết lỗi nội bộ, khóa bí mật hoặc đường dẫn nội bộ; lỗi trường nhập cho phép sửa, lỗi dịch vụ cho phép thử lại, hết phiên yêu cầu đăng nhập lại.

**Truy vết:** UC-01; UC-02; UC-03; UC-04; UC-05; UC-06; UC-07; UC-08; UC-10; UC-11; UC-12; UC-13; UC-14; UAT-07; UAT-09; UAT-14; UAT-15

### 9.1 Phạm vi và nguyên tắc hiển thị thông báo

R1 phải có thông báo tại nơi người dùng thao tác, trạng thái tác vụ có thể xem lại và email giao dịch tài khoản. R1 không yêu cầu trung tâm thông báo có biểu tượng chuông, bộ đếm chưa đọc, lịch sử đọc, thông báo đẩy, SMS hoặc email khi AI hoàn tất. Trạng thái tài liệu và tác vụ là dữ liệu nghiệp vụ, không phụ thuộc việc thông báo tạm thời còn hiển thị hay không.

Danh mục dưới đây xác định mã, điều kiện phát sinh, ý nghĩa và thao tác tiếp theo. Câu chữ là nội dung giao diện đề xuất để chủ sản phẩm rà soát cùng Figma. Sau khi chốt, thay đổi cách diễn đạt được quản lý trong thiết kế; thay đổi ý nghĩa, quyền, điều kiện hoặc hành động phải cập nhật SRS. Không hiển thị mã kỹ thuật cho người dùng thay cho một câu giải thích.

| Loại phản hồi | Vị trí và thời gian tồn tại | Hành vi bắt buộc |
| --- | --- | --- |
| Lỗi trường nhập | Cạnh trường hoặc nhóm nhập tương ứng; còn hiển thị tới khi sửa hợp lệ hoặc hủy biểu mẫu. | Nêu dữ liệu sai và cách sửa nếu có thể nêu mà không tiết lộ thông tin tài khoản. Giữ dữ liệu hợp lệ; liên kết lỗi với trường để công nghệ hỗ trợ đọc được. |
| Thông tin, thành công | Tại vùng kết quả hoặc thông báo tạm thời. | Chỉ báo thành công sau khi trạng thái được xác nhận. Nếu phản hồi tạm thời tự đóng, kết quả vẫn nhận biết được trong trang hoặc danh sách; không đặt thao tác bắt buộc duy nhất trong thông báo này. |
| Đang xử lý | Tại tài liệu, lượt hỏi đáp hoặc tác vụ; còn hiển thị đến trạng thái kết thúc. | Chỉ hiển thị tỷ lệ hoàn thành khi có dữ liệu tiến độ thực tế. Khi mở lại trang, đọc trạng thái hiện hành từ máy chủ. |
| Lỗi nghiệp vụ hoặc dịch vụ | Tại đối tượng hay biểu mẫu liên quan; giữ đến khi người dùng xử lý, đóng chủ động hoặc rời ngữ cảnh. | Nêu bước tiếp theo; lỗi cần xử lý không chỉ xuất hiện trong thông báo tự biến mất. Mã tra cứu kỹ thuật chỉ kèm khi hữu ích. |
| Xác nhận xóa | Hộp thoại trước thao tác thay đổi dữ liệu. | Nêu đối tượng, dữ liệu bị ảnh hưởng và khả năng khôi phục; có lựa chọn hủy. Đóng hộp thoại không đồng nghĩa đã xác nhận. |
| Email giao dịch | Hộp thư của địa chỉ tài khoản được phép nhận; thời hạn liên kết theo LIM-08. | Nội dung và trạng thái gửi tuân theo mục 9.4; không chứa mật khẩu hoặc nội dung Notebook. |
| Kết quả vận hành | Công cụ vận hành hoặc nhật ký có kiểm soát quyền. | Không hiển thị thông tin cấu hình, sao lưu hoặc lỗi nội bộ trong giao diện người dùng thông thường. |

Lỗi nhập liệu phải được hiển thị tại trường hoặc nhóm dữ liệu liên quan. Thông báo toàn trang chỉ được sử dụng khi thông tin ảnh hưởng đến toàn bộ trang hoặc dịch vụ. Các yêu cầu về khả năng tiếp cận được quy định tại IH-UX-003 và IH-MSG-002.

<a id="msg-catalog"></a>

### 9.2 Thông báo về tài khoản và thao tác dữ liệu

Các biến đặt trong `{...}` chỉ được thay bằng dữ liệu đã kiểm tra và người nhận có quyền xem. `{thoi_gian_cho}` lấy từ giới hạn thực tế; `{ly_do}` là câu giải thích đã ánh xạ từ mã lỗi, không lấy nguyên văn phản hồi nhà cung cấp. Tên tài nguyên phải được hiển thị như văn bản an toàn. Không đưa token, địa chỉ lưu tệp nội bộ, câu lệnh, toàn văn nguồn hoặc thông tin tài khoản khác vào biến.

| Mã | Điều kiện phát sinh và loại thông báo | Nội dung đề xuất | Hành động tiếp theo |
| --- | --- | --- | --- |
| MSG-AUTH-001 | Thông tin xác thực không hợp lệ khi đăng nhập hoặc đổi mật khẩu (UC-10, UC-13). Loại: lỗi. | Không thể xác thực bằng thông tin đã nhập. Vui lòng kiểm tra và thử lại. | Nhập lại; cung cấp khôi phục mật khẩu ở màn hình đăng nhập. |
| MSG-AUTH-002 | Hệ thống đã tiếp nhận yêu cầu đăng ký hoặc gửi lại email xác minh (UC-01). Loại: thông tin công khai. | Đã tiếp nhận yêu cầu. Nếu địa chỉ email đủ điều kiện, bạn sẽ nhận được hướng dẫn xác minh. Bạn cũng có thể đăng nhập hoặc khôi phục mật khẩu. | Kiểm tra hộp thư, gửi lại trong giới hạn hoặc chuyển luồng tài khoản. |
| MSG-AUTH-003 | Mật khẩu đăng nhập hợp lệ nhưng email chưa được xác minh (UC-10). Loại: thông tin. | Bạn cần xác minh email trước khi sử dụng Notebook. | Gửi lại thư theo giới hạn hoặc đăng xuất. |
| MSG-AUTH-004 | Hệ thống đã xác minh email thành công (UC-01). Loại: thành công. | Email đã được xác minh. Bạn có thể đăng nhập InsightHub. | Đăng nhập. |
| MSG-AUTH-005 | Liên kết xác minh email hoặc đặt lại mật khẩu không hợp lệ (UC-01, UC-02). Loại: lỗi. | Liên kết không hợp lệ, đã hết hạn hoặc đã được sử dụng. | Yêu cầu liên kết mới theo đúng luồng; không tiết lộ nguyên nhân chi tiết qua liên kết giả. |
| MSG-AUTH-006 | Số lần xác thực hoặc yêu cầu gửi email vượt giới hạn cho phép. Loại: cảnh báo. | Bạn đã vượt số lần thử cho phép. Vui lòng thử lại sau {thoi_gian_cho}. | Đợi; không hiển thị tình trạng tồn tại tài khoản. |
| MSG-AUTH-007 | Người dùng hủy đăng nhập tại Google (UC-11). Loại: thông tin. | Bạn đã hủy đăng nhập bằng Google. | Thử lại hoặc dùng phương thức đăng nhập khác. |
| MSG-AUTH-008 | Quá trình đăng nhập Google không hoàn tất do lỗi xác thực hoặc tích hợp (UC-11). Loại: lỗi. | Chưa thể hoàn tất đăng nhập bằng Google. Vui lòng thử lại. | Khởi tạo luồng mới; không dùng lại phản hồi lỗi. |
| MSG-AUTH-009 | Email Google trùng tài khoản chưa liên kết; cần chứng minh quyền kiểm soát tài khoản (UC-11). Loại: hướng dẫn xác thực. | Cần xác nhận quyền kiểm soát tài khoản InsightHub trước khi liên kết Google. | Với tài khoản đã xác minh, nhập mật khẩu hiện tại; nếu quên, đặt lại mật khẩu. Với tài khoản chờ xác minh, hoàn tất đặt lại mật khẩu trước rồi đăng nhập Google lại theo BR-03. |
| MSG-AUTH-010 | Hệ thống đã tiếp nhận yêu cầu khôi phục mật khẩu (UC-02). Loại: thông tin công khai. | Nếu địa chỉ email có tài khoản phù hợp, bạn sẽ nhận được hướng dẫn khôi phục quyền truy cập. | Kiểm tra hộp thư; gửi lại trong giới hạn. |
| MSG-AUTH-011 | Hệ thống đã đặt lại hoặc đổi mật khẩu thành công (UC-02, UC-13). Loại: thành công. | Mật khẩu đã được cập nhật. Vui lòng đăng nhập lại. | Đăng nhập bằng mật khẩu mới. |
| MSG-AUTH-012 | Phiên đăng nhập không còn hiệu lực khi người dùng thực hiện thao tác cần xác thực. Loại: cảnh báo. | Phiên đăng nhập đã kết thúc. Vui lòng đăng nhập lại để tiếp tục. | Đăng nhập; không tự gửi lại thao tác thay đổi dữ liệu. |
| MSG-AUTH-013 | Máy chủ đã xác nhận thu hồi phiên đăng nhập (UC-14). Loại: thành công. | Bạn đã đăng xuất. | Đăng nhập khi cần. |
| MSG-DATA-001 | Dữ liệu của một trường không đáp ứng quy tắc định dạng, giới hạn hoặc lựa chọn hợp lệ. Loại: lỗi tại trường. | {ten_truong}: {ly_do}. | Sửa trường được chỉ ra; lý do nêu định dạng, giới hạn hoặc lựa chọn hợp lệ. |
| MSG-DATA-002 | Hệ thống đã lưu thành công Notebook, ghi chú, tên kết quả AI hoặc hồ sơ cá nhân (UC-03, UC-06, UC-08, UC-12). Loại: thành công. | Đã lưu {loai_du_lieu}. | Tiếp tục hoặc mở dữ liệu đã lưu. |
| MSG-DATA-003 | Người dùng gửi cập nhật từ phiên bản dữ liệu cũ hơn bản hiện hành trên máy chủ. Loại: cảnh báo. | Dữ liệu đã thay đổi ở phiên khác. Vui lòng tải bản mới trước khi lưu lại. | Tải lại hoặc hủy; không ghi đè tự động. |
| MSG-DATA-004 | Người dùng yêu cầu xóa Notebook, trước khi hệ thống thực hiện thao tác (UC-03). Loại: xác nhận. | Xóa Notebook “{ten}” và toàn bộ tài liệu, hội thoại, ghi chú, kết quả AI cùng các lần làm Quiz bên trong? Thao tác không thể khôi phục trong ứng dụng. | Xóa Notebook hoặc hủy. |
| MSG-DATA-005 | Người dùng yêu cầu xóa tài liệu nguồn, trước khi hệ thống thực hiện thao tác (UC-04). Loại: xác nhận. | Xóa tài liệu “{ten}”? Tài liệu sẽ không còn dùng được cho hỏi đáp và công cụ AI. Nội dung hỏi đáp, ghi chú và kết quả đã lưu vẫn được giữ, nhưng nguồn này không còn mở được. | Xóa tài liệu hoặc hủy. |
| MSG-DATA-006 | Người dùng yêu cầu xóa kết quả AI, trước khi hệ thống thực hiện thao tác (UC-08). Loại: xác nhận. | Xóa kết quả “{ten}”? Các lần làm Quiz gắn với kết quả này cũng bị xóa. Tài liệu nguồn và ghi chú đã sao chép được giữ lại. | Xóa kết quả hoặc hủy; chỉ nêu phần Quiz khi áp dụng. |
| MSG-DATA-007 | Người dùng yêu cầu xóa hội thoại, trước khi hệ thống thực hiện thao tác (UC-05). Loại: xác nhận. | Xóa hội thoại “{ten}” và các lượt hỏi đáp bên trong? Ghi chú đã lưu từ hội thoại được giữ lại. | Xóa hội thoại hoặc hủy. |
| MSG-DATA-008 | Người dùng yêu cầu xóa ghi chú, trước khi hệ thống thực hiện thao tác (UC-06). Loại: xác nhận. | Xóa ghi chú “{ten}”? Thao tác không thể khôi phục trong ứng dụng. | Xóa ghi chú hoặc hủy. |
| MSG-DATA-009 | Máy chủ đã xác nhận thao tác xóa thành công. Loại: thành công. | Đã xóa {loai_du_lieu}. | Trở về danh sách phù hợp. |
| MSG-DATA-010 | Tài nguyên không tồn tại, đã bị xóa hoặc người dùng không có quyền truy cập. Loại: lỗi. | Không thể truy cập nội dung này. | Về danh sách dữ liệu của mình; không xác nhận tài nguyên thuộc ai. |
| MSG-DATA-011 | Người dùng mở tham chiếu tới tài liệu đã bị xóa từ một kết quả lịch sử mà mình có quyền đọc. Loại: thông tin. | Tài liệu nguồn này đã bị xóa. Nội dung kết quả đã lưu được giữ nguyên. | Xem nguồn còn lại hoặc chọn nguồn mới khi tạo lại. |

### 9.3 Thông báo về xử lý tài liệu, tác vụ AI và vận hành

| Mã | Điều kiện phát sinh và loại thông báo | Nội dung đề xuất | Hành động tiếp theo |
| --- | --- | --- | --- |
| MSG-DOC-001 | Tài liệu đang ở trạng thái `Processing` (UC-04). Loại: tiến độ. | Đang xử lý tài liệu “{ten}”. | Đợi hoặc chuyển tác vụ khác; có thể mở lại trạng thái. |
| MSG-DOC-002 | Tài liệu đã được xử lý thành công và chuyển sang `Ready` (UC-04). Loại: thành công. | Tài liệu “{ten}” đã sẵn sàng. | Mở tài liệu, hỏi đáp hoặc chọn làm nguồn cho công cụ AI. |
| MSG-DOC-003 | Tác vụ xử lý tài liệu kết thúc ở trạng thái `Failed` (UC-04). Loại: lỗi. | Không thể xử lý tài liệu. {ly_do}. Mã tra cứu: {ma_tra_cuu}. | Thử lại nếu lỗi có thể khắc phục, hoặc xóa và tải tệp hợp lệ. |
| MSG-DOC-004 | Tệp tải lên có nội dung trùng byte với tài liệu đã có trong cùng Notebook (UC-04). Loại: thông tin. | Tài liệu này đã có trong Notebook. | Mở tài liệu hiện có; nếu `Failed`, dùng luồng thử lại. |
| MSG-DOC-005 | Tệp không đáp ứng yêu cầu về định dạng, dung lượng hoặc văn bản trích xuất (UC-04). Loại: lỗi. | Tệp không đáp ứng yêu cầu: {ly_do}. | Chọn tệp khác; nêu chính xác giới hạn hoặc định dạng bị vi phạm. |
| MSG-AI-001 | Lượt hỏi đáp hoặc tác vụ công cụ AI đang ở trạng thái `Processing` (UC-05, UC-07). Loại: tiến độ. | Đang xử lý yêu cầu của bạn. | Đợi; có thể mở lại trạng thái, không gửi lặp thành yêu cầu mới. |
| MSG-AI-002 | Câu trả lời hoặc kết quả công cụ AI đã được kiểm tra và lưu thành công (UC-05, UC-07). Loại: thành công. | Kết quả đã sẵn sàng và được lưu. | Đọc kết quả và kiểm tra nguồn. |
| MSG-AI-003 | Tài liệu đã chọn không đủ căn cứ đáp ứng yêu cầu; tác vụ kết thúc ở trạng thái `NoEvidence` (UC-05, UC-07). Loại: kết quả nghiệp vụ. | Tài liệu đã chọn chưa đủ căn cứ để hoàn thành yêu cầu này. | Làm rõ câu hỏi, điều chỉnh yêu cầu hoặc bổ sung nguồn. |
| MSG-AI-004 | Lượt hỏi đáp hoặc tác vụ công cụ AI kết thúc ở trạng thái `Failed` do lỗi xử lý (UC-05, UC-07). Loại: lỗi kỹ thuật. | Chưa thể tạo kết quả hợp lệ. {ly_do}. Mã tra cứu: {ma_tra_cuu}. | Thử lại khi phù hợp; không lưu thông báo lỗi thành nội dung AI. |
| MSG-AI-005 | Tài liệu nguồn bị xóa trong khi tác vụ đang xử lý. Loại: lỗi. | Yêu cầu dừng vì tài liệu nguồn không còn khả dụng. | Chọn nguồn hợp lệ và gửi yêu cầu mới. Khi Notebook không còn truy cập được, chỉ dùng MSG-DATA-010. |
| MSG-AI-006 | Lựa chọn nguồn, cấu hình hoặc tần suất xử lý vượt giới hạn LIM-05 hoặc LIM-10. Loại: cảnh báo. | Chưa thể bắt đầu xử lý: {ly_do}. | Sửa lựa chọn nguồn hoặc cấu hình, đợi {thoi_gian_cho} hoặc mở tác vụ đang chạy tùy nguyên nhân. |
| MSG-AI-007 | Máy chủ đã chấm điểm lần làm Quiz được nộp (UC-08). Loại: kết quả. | Bạn trả lời đúng {so_cau_dung}/{tong_so_cau} câu, đạt {diem}%. | Xem đáp án, giải thích, nguồn hoặc bắt đầu lần làm mới. |
| MSG-SYS-001 | Kết nối bị gián đoạn sau khi gửi yêu cầu và chưa xác định được kết quả trên máy chủ. Loại: cảnh báo. | Kết nối bị gián đoạn. Chưa xác định được kết quả thao tác. | Kiểm tra lại trạng thái; không tự tạo yêu cầu mới khi chưa đối soát. |
| MSG-SYS-002 | Dịch vụ cần thiết cho thao tác tạm thời không đáp ứng. Loại: lỗi. | Dịch vụ tạm thời chưa sẵn sàng. Vui lòng thử lại sau. Mã tra cứu: {ma_tra_cuu}. | Thử lại theo khả năng dịch vụ; không hiển thị chi tiết nội bộ. |
| MSG-SYS-003 | Tác vụ cài đặt, sao lưu hoặc khôi phục đã hoàn tất và đạt các kiểm tra bắt buộc (UC-09, UC-15, UC-16). Loại: thành công vận hành. | {ten_tac_vu} đã hoàn tất và đáp ứng các điều kiện kiểm tra bắt buộc. | Lưu bằng chứng; chỉ báo thành công sau khi kiểm tra dữ liệu và quyền. |
| MSG-SYS-004 | Tác vụ cài đặt, sao lưu hoặc khôi phục chưa hoàn tất hoặc không đạt kiểm tra bắt buộc (UC-09, UC-15, UC-16). Loại: lỗi vận hành. | {ten_tac_vu} chưa hoàn tất. Mã lỗi: {ma_loi}. Mã tra cứu: {ma_tra_cuu}. | Kiểm tra nhật ký được cấp quyền; môi trường phục hồi lỗi chưa được mở cho người dùng. |

<a id="email-catalog"></a>

### 9.4 Email giao dịch và thông báo bảo vệ tài khoản

| Mã | Điều kiện và người nhận | Tiêu đề đề xuất | Nội dung và hành động bắt buộc |
| --- | --- | --- | --- |
| EML-001 | Tài khoản chờ xác minh; gửi tới email đã đăng ký. | Xác minh email cho tài khoản InsightHub | Nêu mục đích, liên kết xác minh, thời điểm hết hạn theo LIM-08, cách gửi lại và hướng dẫn bỏ qua nếu không yêu cầu. Không gửi nội dung Notebook. |
| EML-002 | Yêu cầu khôi phục hợp lệ của tài khoản có mật khẩu. | Đặt lại mật khẩu InsightHub | Liên kết dùng một lần, thời điểm hết hạn theo LIM-08, cách yêu cầu mới; nêu rằng mật khẩu chưa thay đổi cho tới khi người dùng hoàn tất. |
| EML-003 | Liên kết Google đã hoàn tất hợp lệ theo BR-03; gửi tới email của tài khoản. | Google đã được liên kết với InsightHub | Nêu phương thức vừa liên kết và thời điểm; hướng dẫn liên hệ người vận hành qua địa chỉ hỗ trợ được công bố nếu người nhận không thực hiện. Không chứa liên kết cấp quyền, mật khẩu hoặc dữ liệu Notebook. |
| EML-004 | Yêu cầu khôi phục của tài khoản chỉ dùng Google. | Hướng dẫn đăng nhập InsightHub | Hướng dẫn dùng nút đăng nhập Google; không kèm liên kết đặt mật khẩu và không tạo thêm phương thức đăng nhập. |
| EML-005 | Mật khẩu đã được đặt lại hoặc thay đổi thành công. | Mật khẩu InsightHub đã được thay đổi | Nêu thời điểm, yêu cầu đăng nhập lại, hướng dẫn dùng chức năng khôi phục mật khẩu nếu người nhận không thực hiện thay đổi. Không chứa mật khẩu mới, mật khẩu cũ hoặc liên kết cấp phiên. |

Quy tắc gửi và bảo vệ thông tin:

1. Chỉ thông báo giao diện rằng yêu cầu đã được tiếp nhận. Nhà cung cấp nhận yêu cầu gửi không chứng minh thư đã đến hộp thư. Kiểm thử tích hợp EML-001 đến EML-005 phải kiểm tra thư nhận thực tế và hành động liên quan; EML-003 kiểm sau khi liên kết thành công, không có bước bấm xác nhận để cấp quyền.
2. Phản hồi đăng ký, gửi lại xác minh công khai và khôi phục không xác nhận tài khoản tồn tại. Cùng một nhóm yêu cầu có cùng cấu trúc phản hồi; không đưa trạng thái gửi riêng của tài khoản ra API công khai. Không dùng sai khác thời gian xử lý như cơ chế công khai để tra cứu email.
3. Các liên kết phải dùng một lần và ràng buộc với đúng tài khoản, mục đích. Khi phát hành thành công liên kết xác minh hoặc đặt lại mới, các liên kết chưa dùng trước đó cùng tài khoản và mục đích hết hiệu lực. Nếu chỉ bị từ chối trước khi phát hành vì giới hạn, liên kết còn hiệu lực trước đó không bị vô hiệu. Thời hạn theo LIM-08; không tự gia hạn vì người dùng mở thư.
4. Hệ thống lưu mục đích, thời điểm, mã tra cứu và trạng thái chuyển giao email. Trạng thái tối thiểu: chờ gửi, nhà cung cấp đã nhận, gửi lỗi hoặc chưa xác định; không gắn nhãn “đã nhận thư” khi chưa có bằng chứng. Dữ liệu vận hành này tuân theo LIM-18 và không trở thành hộp thư thông báo trong ứng dụng.
5. Yêu cầu gửi do người dùng kích hoạt chịu LIM-09 theo tài khoản và IP. Email EML-003 và EML-005 được kích hoạt bởi liên kết Google hoặc thay đổi mật khẩu đã thành công; việc đã dùng hết hạn mức xin liên kết không được làm mất yêu cầu gửi cảnh báo này. Gửi lại do lỗi vận chuyển phải gắn cùng sự kiện, có giới hạn và không tạo liên kết mới ngoài ý muốn.
6. Lỗi gửi EML-003 hoặc EML-005 không hoàn tác liên kết hợp lệ, mật khẩu đã đổi hoặc khôi phục phiên cũ. Ghi lỗi để vận hành xử lý; không yêu cầu người dùng thực hiện lại nghiệp vụ chỉ để gửi thông báo. Có thể dùng trạng thái và chức năng thử lại sẵn có của nhà cung cấp hoặc công cụ vận hành; không yêu cầu xây hàng đợi gửi thư hay bảng quản trị riêng. Thời hạn lưu sự kiện tuân theo LIM-18.

### 9.5 Yêu cầu xử lý và kiểm chứng thông báo

#### IH-MSG-001: Hiển thị thông báo đúng tình huống xử lý

**Yêu cầu:** Hệ thống phải hiển thị thông báo tương ứng với điều kiện xử lý tại mục 9.2 và 9.3, trong đó nêu rõ kết quả thao tác hoặc vấn đề xảy ra và hành động tiếp theo dành cho người dùng.

- **IH-MSG-001-AC01:** Các thông báo được kiểm tra theo điều kiện phát sinh của danh mục; dữ liệu không hợp lệ được chỉ đúng trường, vượt giới hạn nêu đúng giới hạn, tài nguyên không được truy cập không tiết lộ thông tin và các luồng tài khoản công khai không tiết lộ email tồn tại.
- **IH-MSG-001-AC02:** Mất mạng khi chưa biết kết quả phải hiển thị trạng thái chưa xác định; thông báo thành công chỉ xuất hiện sau khi có trạng thái đã lưu. Biến nội dung không chứa dữ liệu ngoài quyền, mã thực thi hoặc bí mật.

**Truy vết:** UC-01; UC-02; UC-03; UC-04; UC-05; UC-06; UC-07; UC-08; UC-09; UC-10; UC-11; UC-12; UC-13; UC-14; UC-15; UC-16; UAT-18; BR-01; BR-15

#### IH-MSG-002: Hiển thị thông báo và hỗ trợ khả năng tiếp cận

**Yêu cầu:** Thông báo phải có vị trí, thời gian tồn tại và khả năng tiếp cận theo mục 9.1.

- **IH-MSG-002-AC01:** Lỗi đầu vào được thể hiện bằng văn bản gắn với trường; lỗi cần xử lý không chỉ xuất hiện trong thông báo tự đóng. Xác nhận xóa có hủy và mô tả tác động; trạng thái hoặc kết quả vẫn xem được khi thông báo tạm thời đã đóng.
- **IH-MSG-002-AC02:** Công nghệ hỗ trợ nhận biết thông báo trạng thái mà không buộc chuyển tiêu điểm bàn phím; lỗi không chỉ được biểu thị bằng màu. Kiểm chứng bằng bàn phím và ít nhất một tổ hợp trình đọc màn hình/trình duyệt được ghi trong hồ sơ nghiệm thu.

**Truy vết:** UC-01; UC-02; UC-03; UC-04; UC-05; UC-06; UC-07; UC-08; UC-10; UC-11; UC-12; UC-13; UC-14; UAT-15; UAT-18; IH-UX-003

#### IH-MSG-003: Gửi email giao dịch theo sự kiện tài khoản

**Yêu cầu:** Hệ thống phải tạo và gửi các email EML-001 đến EML-005 cho đúng tài khoản, theo điều kiện và sự kiện được quy định tại mục 9.4.

- **IH-MSG-003-AC01:** Dịch vụ thực gửi đủ năm loại email tới tài khoản phù hợp. EML-001 và EML-002 có liên kết đúng mục đích và LIM-08; liên kết hết hạn, dùng lại hoặc bị thay thế bị từ chối.
- **IH-MSG-003-AC02:** Lỗi gửi được ghi nhận, không làm lộ tài khoản qua phản hồi công khai hoặc thay đổi kết quả nghiệp vụ đã hoàn tất. Không báo thư đã tới hộp thư chỉ từ trạng thái nhà cung cấp nhận yêu cầu.
- **IH-MSG-003-AC03:** EML-003 được tạo sau liên kết Google, EML-005 sau đổi hoặc đặt lại mật khẩu; hạn mức xin liên kết không làm mất hai sự kiện thông báo này. EML-004 chỉ hướng dẫn đăng nhập Google, không tạo mật khẩu.

**Truy vết:** UC-01; UC-02; UC-11; UC-13; UC-15; UAT-01; UAT-02; UAT-03; UAT-19; LIM-08; LIM-09; LIM-18

#### IH-MSG-004: Hiển thị lại trạng thái tác vụ khi người dùng quay lại

**Yêu cầu:** Hệ thống phải cho chủ sở hữu xem lại trạng thái đã lưu của tác vụ tài liệu, hỏi đáp và công cụ AI khi quay lại ứng dụng.

- **IH-MSG-004-AC01:** Tải lại trang, chuyển Notebook, đóng rồi mở lại trang không tự hủy hoặc nhân đôi tác vụ đã nhận. Khi người dùng có phiên và quyền hợp lệ trở lại, giao diện hiển thị trạng thái và kết quả hiện hành; `Failed` và `NoEvidence` có hướng xử lý khác nhau.
- **IH-MSG-004-AC02:** Tác vụ quá hạn, nguồn bị xóa hoặc Notebook không còn truy cập được tuân thủ LIM-11, BR-08 và BR-09. Trạng thái được kiểm tra quyền như tài nguyên gốc; việc đóng thông báo không thay đổi trạng thái nghiệp vụ hoặc bỏ qua kiểm soát quyền.

**Truy vết:** UC-04; UC-05; UC-07; UC-08; UAT-07; UAT-09; UAT-14; UAT-18; BR-08; BR-09; BR-10; LIM-11

### 9.6 Trạng thái giao diện cần được thiết kế

| Màn hình | Trạng thái bắt buộc ngoài dữ liệu thông thường | Hành trình liên quan |
| --- | --- | --- |
| UI-01 Tài khoản | Đang gửi, dữ liệu sai, xác thực sai, chờ xác minh, liên kết không hợp lệ, gửi lại bị giới hạn, đăng nhập Google bị hủy hoặc gặp lỗi, cần xác nhận liên kết, hoàn tất và hết phiên. | UC-01, UC-02, UC-10, UC-11, UC-14. |
| UI-02 Hồ sơ | Đang tải hoặc lưu dữ liệu, tên sai, ảnh mặc định, tài khoản chỉ đăng nhập bằng Google, xác thực lại, xung đột cập nhật, lưu thành công hoặc chưa xác định kết quả. | UC-12, UC-13, UC-14. |
| UI-03 Danh sách Notebook | Chưa có Notebook, đang tải, tải lỗi, đạt giới hạn, tạo hoặc cập nhật sai, xung đột và xác nhận xóa. | UC-03. |
| UI-04 Notebook | Chưa có nguồn `Ready`, chưa có hội thoại, câu hỏi sai, đang trả lời, `NoEvidence`, lỗi kỹ thuật, nguồn đã xóa, nguồn đang chọn và nguồn thay đổi khi chuyển Notebook. | UC-03, UC-04, UC-05, UC-07. |
| UI-05 Tài liệu | Kiểm tra đầu vào, `Processing`, `Ready`, `Failed`, tệp trùng, thử lại, nguồn không truy cập được và xác nhận xóa. | UC-04, UC-05, UC-08. |
| UI-06 Công cụ AI | Chưa chọn nguồn, nguồn quá giới hạn, cấu hình từng công cụ, đang xử lý, hết hạn mức, `NoEvidence`, thất bại và mở kết quả. | UC-07. |
| UI-07 Kết quả AI | Danh sách chưa có dữ liệu, bộ lọc không tìm thấy kết quả, hiển thị từng loại, nguồn không còn, đổi tên, xung đột cập nhật, tạo lại, xóa; Quiz đang làm hoặc đã nộp; Slide trình chiếu; tải Báo cáo. | UC-08. |
| UI-08 Ghi chú | Chưa có ghi chú, đang tạo hoặc cập nhật, có thay đổi chưa lưu, lưu lỗi, vượt giới hạn, xung đột, xuất xứ đã xóa và xác nhận xóa. | UC-06. |

Các trạng thái phải có thiết kế trên cả hai kích thước LIM-16; có thể dùng thành phần chung nếu hành vi giống nhau. Bộ đối chiếu Figma phải ghi màn hình, trạng thái, mã ca sử dụng và nhánh xử lý và mã thông báo, kèm hành vi bàn phím. Đây là nội dung kiểm tra của IH-UX-001 đến IH-UX-004 và UAT-15 và UAT-18, không phải yêu cầu tạo một màn hình độc lập cho mỗi trạng thái.

<a id="muc-10"></a>

## 10. Yêu cầu tích hợp

Các điểm tích hợp phải xác định rõ dữ liệu trao đổi, điều kiện hợp lệ và cách xử lý lỗi.

| Điểm tích hợp | Đầu vào và đầu ra | Yêu cầu xử lý lỗi |
| --- | --- | --- |
| Trình duyệt và API | Danh tính phiên, dữ liệu nghiệp vụ, tệp; trả dữ liệu, trạng thái và mã thao tác. | Phân biệt lỗi xác thực, quyền, dữ liệu, xung đột, giới hạn tần suất và lỗi dịch vụ; có mã yêu cầu xử lý. |
| Google và dịch vụ xác thực | Kết quả xác thực trả về qua callback, token, định danh nhà cung cấp và email đã xác minh. | Từ chối phản hồi giả, token sai bên nhận hoặc bên phát hành, token hết hạn, phát lại trái phép và chuyển hướng tới địa chỉ chưa được cấu hình. |
| Email giao dịch | Địa chỉ nhận và mục đích EML-001 đến EML-005, sự kiện gửi và trạng thái chuyển giao. | Không cung cấp token cho ứng dụng khách ngoài luồng nhận email; áp dụng giới hạn gửi và cho thử lại khi lỗi. |
| Embedding và chỉ mục | Văn bản hợp lệ, định danh và phạm vi tài liệu; đầu ra là dữ liệu chỉ mục và kết quả truy xuất. | Tài liệu không được chuyển sang `Ready` nếu mô hình, số chiều véc-tơ hoặc chỉ mục không hợp lệ. Không trộn chỉ mục không tương thích. |
| Mô hình sinh nội dung | Nội dung nguồn hợp lệ, yêu cầu và cấu hình công cụ; đầu ra là văn bản hoặc dữ liệu có cấu trúc. | Kiểm tra cấu trúc, thời hạn và tham chiếu nguồn. Phân biệt hết hạn mức, hết thời gian chờ và `NoEvidence`; không thực thi lệnh từ đầu ra. |
| Lưu tệp và kết quả | Tệp gốc, văn bản trích xuất, kết quả AI và thông tin nguồn. | Đường dẫn tải tệp không được bỏ qua kiểm tra quyền. Mọi yêu cầu tải nguồn hoặc kết quả phải được kiểm tra quyền tại thời điểm xử lý. |

### IH-INT-001: Đặc tả và quản lý phiên bản giao tiếp tích hợp

**Yêu cầu:** Hệ thống phải có hợp đồng giao tiếp mô tả đủ yêu cầu xử lý, phản hồi, trạng thái và lỗi của các thao tác công khai.

- **IH-INT-001-AC01:** Tài liệu API ghi xác thực, quyền, giới hạn và mã lỗi cho tài khoản, Notebook, tài liệu, hỏi đáp, ghi chú, năm công cụ và kết quả AI.
- **IH-INT-001-AC02:** Kiểm thử hợp đồng giao tiếp phải xác nhận các trường bắt buộc và mã lỗi. Ứng dụng khách phải xử lý được các nhóm lỗi: chưa xác thực (`Unauthorized`), không có quyền hoặc không tìm thấy (`Forbidden`/`NotFound`), dữ liệu không hợp lệ (`Validation`), xung đột (`Conflict`), vượt tần suất (`RateLimited`), lỗi nhà cung cấp (`ProviderError`) và hết thời gian chờ (`Timeout`).

**Truy vết:** UC-01; UC-02; UC-03; UC-04; UC-05; UC-06; UC-07; UC-08; UC-10; UC-11; UC-12; UC-13; UC-14; UC-15; UAT-16

### IH-INT-002: Quản lý cấu hình dịch vụ tích hợp

**Yêu cầu:** Hệ thống phải tách cấu hình triển khai và thông tin bí mật khỏi mã nguồn và dữ liệu công khai.

- **IH-INT-002-AC01:** Cấu hình xác định nhà cung cấp, mô hình embedding và sinh nội dung, định danh ứng dụng xác thực, callback hợp lệ, dịch vụ email và thời hạn xử lý; bí mật chỉ được cung cấp qua cơ chế cấu hình bảo mật.
- **IH-INT-002-AC02:** Thiếu cấu hình bắt buộc làm môi trường báo chưa sẵn sàng; thông báo và nhật ký không tiết lộ bí mật. Khả năng đáp ứng giới hạn đầu vào và đầu ra của nhà cung cấp được ghi bằng phép thử tại mục 5.5.
- **IH-INT-002-AC03:** Trước khi người dùng xác nhận tải tài liệu hoặc gọi AI, giao diện cung cấp thông tin xử lý dữ liệu có thể đọc được: tên nhà cung cấp thực tế, phần dữ liệu gửi đi, mục đích, giới hạn xóa/lưu giữ tại ứng dụng và liên kết chính sách của dịch vụ. Thông tin khớp cấu hình triển khai và loại dữ liệu được phép tại mục 2.4; không tuyên bố xóa ở ứng dụng đồng nghĩa đã xóa mọi bản sao tại nhà cung cấp. Không yêu cầu một hệ thống quản lý chấp thuận riêng.

**Truy vết:** UC-04; UC-05; UC-07; UC-15; UAT-06; UAT-11; UAT-15; UAT-16; LIM-03; LIM-05; LIM-11; LIM-13

### IH-INT-003: Kiểm chứng tích hợp bằng dịch vụ thực

**Yêu cầu:** Bản nghiệm thu phải kiểm chứng các luồng tích hợp quan trọng bằng dịch vụ thực trong môi trường được phép.

- **IH-INT-003-AC01:** Hồ sơ nghiệm thu phải có bằng chứng đăng nhập Google, gửi email xác minh, đặt lại mật khẩu và sử dụng mô hình thực cho RAG cùng cả năm công cụ AI. Mỗi bằng chứng ghi ngày thực hiện, cấu hình và kết quả.
- **IH-INT-003-AC02:** Dữ liệu hoặc dịch vụ giả lập dùng trong kiểm thử hồi quy hay giả lập lỗi phải được ghi rõ. Kết quả giả lập không thay thế bằng chứng tích hợp dịch vụ thực.

**Truy vết:** UC-01; UC-02; UC-05; UC-07; UC-10; UC-11; UC-13; UC-15; UAT-01; UAT-02; UAT-03; UAT-11; UAT-16

### 10.1 Đặc tả giao tiếp giữa ứng dụng khách và API

Bảng này xác định năng lực giao tiếp bắt buộc. Nhóm triển khai quyết định đường dẫn, phương thức HTTP, cách truyền phiên và định dạng cụ thể trong đặc tả API có phiên bản. SRS không thay thế tài liệu API, nhưng hợp đồng không được thiếu các hành vi dưới đây.

| Nhóm thao tác | Đầu vào cần xác định | Phản hồi cần xác định | Kiểm soát bắt buộc |
| --- | --- | --- | --- |
| Tài khoản | Dữ liệu được xác định trong UC-01, UC-02 và UC-10 đến UC-14; kết quả xác thực Google hoặc bằng chứng liên kết danh tính theo từng luồng. | Trạng thái được phép công khai, bước tiếp theo và thông tin phiên hoặc hồ sơ khi người dùng có quyền. | Phản hồi công khai không tiết lộ sự tồn tại của tài khoản. Hệ thống kiểm tra bằng chứng xác thực và giới hạn tần suất. |
| Danh sách tài nguyên | Ngữ cảnh Notebook, loại kết quả cần lọc và tham số phân trang. | Danh sách tài nguyên, thông tin để lấy trang tiếp theo và thứ tự hiển thị ổn định. | Hệ thống chỉ trả dữ liệu thuộc quyền truy cập. Danh sách rỗng là kết quả hợp lệ; lỗi tải dữ liệu phải được báo riêng. |
| Tạo và cập nhật tài nguyên | Nội dung Notebook, ghi chú, tên hội thoại hoặc tên kết quả AI; định danh và phiên bản hiện hành khi cập nhật. | Dữ liệu đã lưu cùng phiên bản mới, hoặc lỗi nhập liệu hay xung đột. | Hệ thống phát hiện cập nhật từ phiên bản cũ và xác định chủ sở hữu từ phiên đăng nhập. Thao tác không được tự chuyển tài nguyên sang Notebook khác. |
| Tài liệu | Tệp, Notebook và mã thao tác khi tải lên; định danh tài liệu khi đọc, xử lý lại hoặc xóa. | Định danh, trạng thái, thông tin mô tả và nguyên nhân lỗi được phép công khai; văn bản và vị trí nguồn khi người dùng có quyền đọc. | Hệ thống kiểm tra nội dung tệp, tệp trùng byte, giới hạn và trạng thái xử lý. |
| Hỏi đáp và công cụ AI | Notebook, hội thoại nếu là hỏi đáp, danh sách nguồn, câu hỏi hoặc cấu hình công cụ và mã thao tác. | Định danh tác vụ hoặc lượt hỏi đáp, trạng thái và mã tra cứu. Hệ thống chỉ trả kết quả đã đáp ứng điều kiện hợp lệ. | Hệ thống kiểm tra lại quyền, nguồn và giới hạn. Tác vụ đã được tiếp nhận phải cho phép truy vấn trạng thái sau khi kết nối bị gián đoạn. |
| Đọc trạng thái | Định danh tác vụ, lượt hỏi đáp, tài liệu hoặc mã thao tác của người dùng. | Trạng thái đã lưu, thời điểm cập nhật, kết quả được phép đọc hoặc thông báo lỗi an toàn. | Hệ thống phải kiểm tra quyền dù người gửi có định danh tác vụ. Thao tác đọc trạng thái không được tạo tác vụ mới. |
| Xem nguồn hoặc tải báo cáo | Định danh tài nguyên, vị trí tham chiếu hoặc định danh kết quả AI. | Văn bản tại đúng vị trí tham chiếu, hoặc nội dung Markdown khớp với báo cáo đã lưu. | Hệ thống kiểm tra quyền tại thời điểm xử lý. Nguồn đã xóa không được trả đoạn trích; liên kết tải xuống không được bỏ qua xác thực. |
| Làm và nộp Quiz | Định danh Quiz, định danh lần làm và các lựa chọn của người dùng khi nộp. | Trước khi nộp: câu hỏi và các phương án lựa chọn. Sau khi nộp: lựa chọn đã lưu, điểm, đáp án và giải thích. | Máy chủ chấm điểm và kiểm tra mỗi lựa chọn thuộc đúng câu hỏi, mỗi câu hỏi thuộc đúng Quiz. Nộp lặp không được tạo kết quả chấm điểm thứ hai. |
| Xóa tài nguyên | Định danh tài nguyên thuộc quyền; người dùng đã xác nhận phạm vi xóa trên giao diện. | Xác nhận xóa về nghiệp vụ hoặc thông báo lỗi; trạng thái nhất quán khi yêu cầu được gửi lại. | Máy chủ phải kiểm tra quyền truy cập; cờ xác nhận từ giao diện không được dùng thay cho bước kiểm tra này. |

Mỗi phản hồi lỗi phải có mã ổn định cho ứng dụng xử lý, thông điệp an toàn hoặc mã thông báo, mã tra cứu và lỗi theo trường nếu áp dụng. Phản hồi vượt tần suất có thời gian được thử lại; xung đột có cách đọc phiên bản hiện hành, không tự trả nội dung ngoài quyền. API không được yêu cầu giao diện phân tích chuỗi tiếng Việt để suy ra loại lỗi. Nhóm `NotFound`/`Forbidden` phải có phản hồi công khai tương đương khi phân biệt chúng có thể tiết lộ tài nguyên người khác.

`NoEvidence` là trạng thái kết quả nghiệp vụ, không được ánh xạ thành lỗi nhà cung cấp hoặc lỗi HTTP chung. Nếu giao thức truyền từng phần được sử dụng, phần chưa kiểm chứng phải được nhận diện là nội dung tạm; chỉ kết quả đã qua kiểm tra mới được lưu và công bố thành câu trả lời hợp lệ. R1 không bắt buộc truyền từng phần.

### 10.2 Thời hạn xử lý, yêu cầu gửi lặp và tác vụ đồng thời

- Với tài liệu, thời hạn LIM-11 bắt đầu khi máy chủ nhận đủ tệp và chấp nhận tác vụ; thời gian truyền tệp qua mạng được ghi riêng. Với hỏi đáp hoặc công cụ AI, bắt đầu khi máy chủ nhận đủ yêu cầu hợp lệ. Thời gian xếp hàng, gọi dịch vụ, thử lại nội bộ, kiểm tra và lưu đều nằm trong thời hạn; thử lại nội bộ không đặt lại đồng hồ.
- Giới hạn một tác vụ AI của LIM-10 áp dụng chung cho hỏi đáp và cả năm công cụ theo người dùng. Tác vụ tạo embedding khi tiếp nhận tài liệu không chiếm suất này. Kiểm thử hai yêu cầu đồng thời tại UAT-20 xác nhận cơ chế này; không yêu cầu đo tải nhiều người dùng.
- Máy chủ phải chấp nhận tác vụ, ghi nhận tác vụ để kiểm soát giới hạn đồng thời và lưu mã thao tác theo một kết quả nghiệp vụ nhất quán. Hai yêu cầu đồng thời không được cùng vượt hạn mức. Yêu cầu trùng mã được đối soát trước khi tính là yêu cầu AI mới; cùng mã và dữ liệu khác trả xung đột.
- Thời hạn mã thao tác LIM-12 được tính từ khi chấp nhận yêu cầu. Trong thời hạn, cùng người dùng, loại thao tác và mã phải trả về cùng định danh và trạng thái hiện hành. Notebook, tập nguồn và cấu hình là thành phần nội dung để phát hiện cùng mã nhưng khác yêu cầu. Mã không được tái sử dụng cho một hành động mới.
- Hết phiên không tự hủy tác vụ đã được máy chủ chấp nhận; không trả kết quả cho ứng dụng khách chưa tái xác thực. Xóa Notebook, hội thoại đích của hỏi đáp hoặc nguồn đang dùng làm tác vụ không còn đủ điều kiện phải chặn công bố kết quả. Người dùng rời trang không có nghĩa đã yêu cầu hủy.
- Không tự gọi lại thao tác thay đổi dữ liệu bằng mã mới chỉ vì mất kết nối. Khi chưa xác định được kết quả, giao diện đọc trạng thái hoặc đối soát mã cũ. Thử lại sau lỗi đã xác định tạo lần xử lý mới liên kết lần lỗi, trong khi **Tạo lại** từ kết quả thành công tạo một kết quả độc lập.
- Tài liệu `Ready` không sửa nội dung tại chỗ. Hai người dùng tải cùng tệp không chia sẻ quyền đọc hoặc tiết lộ sự tồn tại cho nhau; cơ chế tối ưu lưu trữ nếu có phải bảo toàn ranh giới này.

### 10.3 Yêu cầu kiểm chứng giao tiếp và trạng thái tác vụ

#### IH-INT-004: Tiếp nhận yêu cầu và đối soát trạng thái tác vụ

**Yêu cầu:** Hệ thống phải cho ứng dụng khách gửi yêu cầu, nhận kết quả và kiểm tra trạng thái tác vụ đã tiếp nhận. Khi phản hồi bị gián đoạn, ứng dụng phải có thể xác định kết quả bằng định danh hoặc mã thao tác theo mục 10.1 và 10.2.

- **IH-INT-004-AC01:** Kiểm thử hợp đồng bao phủ đầy đủ nhóm thao tác, dữ liệu bắt buộc, lỗi, phân trang và đọc trạng thái. Mất phản hồi sau khi đã nhận tác vụ phải đối soát được bằng định danh/mã thao tác; gửi lại không tạo tác vụ hoặc kết quả mới ngoài ý muốn.
- **IH-INT-004-AC02:** Kiểm thử hai yêu cầu đồng thời, cùng mã khác nội dung, hết phiên, xóa hội thoại/nguồn/Notebook và hết thời hạn xác nhận đúng quy tắc tại mục 10.2. Nhật ký thời điểm chứng minh thời gian xếp hàng và thử lại nội bộ nằm trong thời hạn chung.

**Truy vết:** UC-03; UC-04; UC-05; UC-06; UC-07; UC-08; UC-14; UC-15; UAT-07; UAT-09; UAT-12; UAT-16; UAT-17; UAT-20; BR-08; BR-09; BR-10; LIM-10; LIM-11; LIM-12

<a id="muc-11"></a>

## 11. Yêu cầu phi chức năng

Các yêu cầu dưới đây xác định mức bảo vệ, độ tin cậy, hiệu năng và khả năng vận hành cần đạt của R1.

### IH-NFR-001: Bảo vệ xác thực và mật khẩu

**Yêu cầu:** Hệ thống phải bảo vệ mật khẩu và thông tin xác thực, giới hạn các lần thử không hợp lệ, đồng thời ngăn phản hồi công khai tiết lộ sự tồn tại của tài khoản.

- **IH-NFR-001-AC01:** Mật khẩu không được lưu dạng rõ hoặc mã hóa có thể giải mã; kiểm chứng bằng cấu hình dịch vụ xác thực hoặc thiết kế lưu mật khẩu và dữ liệu lưu thực tế đã che thông tin nhạy cảm.
- **IH-NFR-001-AC02:** Token, liên kết và phiên được kiểm tra hiệu lực, mục đích, tính dùng một lần và giới hạn LIM-07 đến LIM-09; các lần thử bị chặn không được tạo quyền truy cập.
- **IH-NFR-001-AC03:** Môi trường dùng chung truyền thông tin xác thực qua HTTPS; bản local chỉ được dùng HTTP trên địa chỉ loopback, không phát hành như môi trường dùng chung.
- **IH-NFR-001-AC04:** Đổi mật khẩu và liên kết Google yêu cầu xác nhận mật khẩu theo BR-03 và LIM-19. Phiên đăng nhập cũ hoặc email thông báo EML-003 không thay thế bằng chứng này.
- **IH-NFR-001-AC05:** Phản hồi đăng nhập và khôi phục không tiết lộ tài khoản tồn tại; lỗi sai email hoặc sai mật khẩu có cùng nội dung công khai.

**Truy vết:** UC-01; UC-02; UC-10; UC-11; UC-13; UC-14; UAT-01; UAT-02; UAT-03; UAT-04; Nguồn S2; S3

### IH-NFR-002: Cách ly dữ liệu giữa người dùng và Notebook

**Yêu cầu:** Hệ thống phải duy trì cách ly người dùng và Notebook ở mọi đường truy cập dữ liệu.

- **IH-NFR-002-AC01:** Mọi trường hợp kiểm thử truy cập dữ liệu của người khác qua giao diện, API, tải nguồn, truy xuất, bộ nhớ đệm và kết quả AI đều phải bị từ chối. Phản hồi không được chứa tên tệp, đoạn trích hoặc nội dung không thuộc quyền truy cập.
- **IH-NFR-002-AC02:** Nếu quyền truy cập hoặc nguồn thay đổi trong lúc xử lý, hệ thống phải kiểm tra lại trước khi công bố kết quả. Nhật ký và thông báo lỗi không được tiết lộ dữ liệu của người khác.

**Truy vết:** UC-03 đến UC-08; UAT-12; UAT-13; BR-01; BR-04; Nguồn S4

### IH-NFR-003: Xử lý an toàn nội dung nguồn và đầu ra AI

**Yêu cầu:** Hệ thống phải xử lý nội dung không đáng tin mà không thực thi mã hoặc chỉ dẫn ngoài nghiệp vụ.

- **IH-NFR-003-AC01:** Nội dung HTML hoặc mã lệnh trong tệp, hồ sơ cá nhân, hỏi đáp và kết quả AI không được thực thi. Markdown và liên kết phải được hiển thị an toàn; mô hình không được tùy ý truy cập URL hoặc tệp hệ thống.
- **IH-NFR-003-AC02:** Các tình huống kiểm thử tấn công chèn chỉ dẫn (prompt injection) không được làm thay đổi chủ sở hữu, mở rộng phạm vi nguồn, tiết lộ thông tin bí mật hoặc thực hiện hành động bên ngoài. Không đưa thông tin xác thực bí mật vào ngữ cảnh gửi tới mô hình.

**Truy vết:** UC-04; UC-05; UC-06; UC-07; UC-08; UC-12; UAT-13; UAT-14; BR-06

### IH-NFR-004: Lưu trữ bền vững và tính toàn vẹn dữ liệu

**Yêu cầu:** Hệ thống phải bảo toàn dữ liệu đã xác nhận lưu qua tải lại trang và khởi động lại dịch vụ.

- **IH-NFR-004-AC01:** Tài khoản, Notebook, tài liệu `Ready`, hội thoại, ghi chú, kết quả AI và các lần làm Quiz phải được giữ nguyên sau khi khởi động lại. Không được truy cập bản ghi đã mất tài nguyên cha.
- **IH-NFR-004-AC02:** Lỗi xảy ra trong quá trình lưu không tạo thông báo thành công sai; các kiểm thử cạnh tranh, gửi lặp và xóa đang xử lý đáp ứng BR-08 đến BR-12.

**Truy vết:** UC-03; UC-04; UC-05; UC-06; UC-07; UC-08; UC-09; UC-15; UAT-07; UAT-12; UAT-16

### IH-NFR-005: Giới hạn thời gian và phục hồi tác vụ bị gián đoạn

**Yêu cầu:** Hệ thống phải xử lý các tác vụ bị gián đoạn trong thời hạn quy định và cung cấp cách khôi phục hoặc thử lại rõ ràng.

- **IH-NFR-005-AC01:** Tác vụ tiếp nhận tài liệu, hỏi đáp hoặc công cụ AI vượt thời hạn LIM-11 phải chuyển sang `Failed` và loại bỏ kết quả đến muộn. Người dùng có thể thử lại mà không tạo trùng kết quả đã lưu thành công.
- **IH-NFR-005-AC02:** Sau khởi động lại, tác vụ `Processing` bị gián đoạn phải được nhận diện và kết thúc hoặc khôi phục trong thời hạn xử lý còn lại; không treo vô thời hạn.

**Truy vết:** UC-04; UC-05; UC-07; UC-09; UC-15; UAT-07; UAT-09; UAT-14; UAT-16; LIM-11

### IH-NFR-006: Thời gian phản hồi các thao tác không sử dụng AI

**Yêu cầu:** Hệ thống phải đáp ứng thời gian phản hồi nghiệp vụ tại LIM-15 trên môi trường kiểm chứng LIM-14.

- **IH-NFR-006-AC01:** Chọn trước 10 thao tác có đầu vào hợp lệ, bao phủ danh sách, chi tiết, tạo, cập nhật và xóa theo mục 11.1. Trên LIM-14, mỗi thao tác đáp ứng LIM-15 và không có lỗi kỹ thuật.
- **IH-NFR-006-AC02:** Bản ghi kết quả nêu thao tác, cấu hình, quy mô dữ liệu, thời điểm bắt đầu/kết thúc, thời lượng và lỗi nếu có. Không loại một mẫu chậm hoặc lỗi rồi thay bằng mẫu khác để báo đạt; sửa nguyên nhân và chạy lại nhóm bị ảnh hưởng.

**Truy vết:** UC-03; UC-04; UC-08; UAT-17; LIM-14; LIM-15

### IH-NFR-007: Thời gian xử lý hỏi đáp và công cụ AI

**Yêu cầu:** Hệ thống phải ghi được thời gian xử lý AI và kết thúc trong thời hạn LIM-11 trên cấu hình đã thống nhất.

- **IH-NFR-007-AC01:** Các lần chạy AEV-01 đến AEV-06 ghi thời gian từ khi máy chủ nhận đủ yêu cầu hợp lệ tới khi lưu kết quả kết thúc, bao gồm gọi nhà cung cấp, kiểm tra và lưu. Tái sử dụng chính các lần chạy này để kiểm thời hạn, không yêu cầu bộ đo tải AI riêng.
- **IH-NFR-007-AC02:** Mỗi lần chạy kết thúc trong LIM-11 và có trạng thái đúng kỳ vọng; ghi cả lỗi, quá hạn và NoEvidence ngoài kỳ vọng là không đạt. Kiểm thử quá hạn có chủ đích xác nhận chuyển Failed và loại kết quả muộn, có thể dùng dịch vụ giả lập.

**Truy vết:** UC-05; UC-07; UAT-17; LIM-10; LIM-11; LIM-15

### IH-NFR-008: Theo dõi hoạt động và chẩn đoán lỗi

**Yêu cầu:** Hệ thống phải ghi nhận tình trạng hoạt động, thời gian xử lý và lỗi để người vận hành có thể chẩn đoán sự cố mà không truy cập thông tin bí mật hoặc toàn văn tài liệu nguồn qua nhật ký.

- **IH-NFR-008-AC01:** Hệ thống phải cung cấp điểm kiểm tra tình trạng hoạt động và mức sẵn sàng. Nhật ký ghi mã yêu cầu xử lý, loại thao tác, thời lượng, mã lỗi và nhà cung cấp, mô hình khi phù hợp. Người vận hành sử dụng mã tra cứu hiển thị trên giao diện để tìm sự kiện tương ứng trong nhật ký.
- **IH-NFR-008-AC02:** Nhật ký phải tuân theo LIM-18; mẫu kiểm tra không có mật khẩu, token, liên kết đặt lại mật khẩu hoặc toàn văn nguồn. Thông tin tình trạng hoạt động công khai không lộ cấu hình bí mật.

**Truy vết:** UC-09; UC-15; UC-16; UAT-16; LIM-18

### IH-NFR-009: Sao lưu thủ công và kiểm chứng khôi phục

**Yêu cầu:** Hệ thống phải có cách sao lưu dữ liệu nghiệp vụ và tệp nguồn, cùng hướng dẫn kiểm chứng khôi phục trên môi trường riêng trong phạm vi R1.

- **IH-NFR-009-AC01:** Có hướng dẫn và bằng chứng sao lưu thủ công trước phát hành hoặc thay đổi cấu trúc dữ liệu có sẵn; bản sao lưu có danh mục, thời điểm, phiên bản và giới hạn quyền đọc, được giữ theo LIM-13.
- **IH-NFR-009-AC02:** Thực hiện ít nhất một lần khôi phục bản sao lưu hợp lệ vào môi trường riêng theo UC-09. Nội dung mẫu, quan hệ và quyền khớp tại thời điểm sao lưu; không ghi đè môi trường đang phục vụ và dọn dữ liệu tạm sau kiểm chứng.

**Truy vết:** UC-09; UC-16; UAT-16; LIM-13; LIM-14

### IH-NFR-010: Khả năng bảo trì và tái lập môi trường

**Yêu cầu:** Bản bàn giao phải cho phép tái lập môi trường cài đặt và kiểm thử mà không phụ thuộc máy của người phát triển.

- **IH-NFR-010-AC01:** Gói bàn giao phải có hướng dẫn cấu hình, danh sách thư viện phụ thuộc được cố định phiên bản, quy trình cập nhật cấu trúc cơ sở dữ liệu và bộ kiểm thử tự động. Kiểm thử phải bao phủ quyền truy cập, nghiệp vụ chính, dữ liệu, hợp đồng giao tiếp và cách hiển thị đầu ra.
- **IH-NFR-010-AC02:** Người kiểm tra thực hiện cài đặt mới trên môi trường sạch theo hướng dẫn; không cần thông tin bí mật viết cứng hoặc tệp cá nhân không có trong gói bàn giao.

**Truy vết:** UC-15; UAT-16

### IH-NFR-011: Bảo vệ phiên đăng nhập trên trình duyệt

**Yêu cầu:** Hệ thống phải ngăn chiếm dụng phiên cũ và thao tác thay đổi dữ liệu giả mạo từ nguồn không được phép trên trình duyệt.

- **IH-NFR-011-AC01:** Đăng nhập thành công không tái sử dụng định danh phiên chưa xác thực do bên ngoài áp đặt. Thông tin xác thực phiên không xuất hiện trong URL nghiệp vụ, thông báo hoặc nhật ký. Trên môi trường dùng chung, kênh truyền phiên được bảo vệ bằng HTTPS; dữ liệu cá nhân không được lưu trong bộ nhớ đệm dùng chung giữa tài khoản.
- **IH-NFR-011-AC02:** Kiểm thử xác nhận bằng chứng tái xác thực hết 5 phút hoặc đã dùng bị từ chối; yêu cầu thay đổi dữ liệu giả mạo từ nguồn không được phép bị từ chối, trong khi các luồng hợp lệ vẫn chạy. Nếu dùng cookie cho phiên, cấu hình bảo vệ cookie và chống CSRF phải có bằng chứng; nếu dùng cơ chế khác, thiết kế phải xác định nơi giữ thông tin xác thực và kiểm soát tương đương phù hợp với cơ chế đó.

**Truy vết:** UC-01; UC-02; UC-10; UC-11; UC-12; UC-13; UC-14; UAT-04; UAT-13; UAT-21; LIM-19; IH-AUTH-008; IH-NFR-001; Nguồn S12; S13

### 11.1 Quy ước kiểm chứng thời gian phản hồi và thời hạn phiên

Mười thao tác không gọi AI gồm ít nhất hai thao tác cho mỗi nhóm: xem danh sách, mở chi tiết, tạo, cập nhật và xóa. Chọn các thao tác từ Notebook, ghi chú hoặc kết quả đã lưu; có thể đo ngay trong các ca UAT tương ứng. Phép đo dùng yêu cầu hợp lệ, chạy tuần tự trên cấu hình LIM-14; tính từ khi máy chủ nhận đủ yêu cầu tới khi trả kết quả đã xác định. Ghi tất cả mẫu, không suy diễn phân vị hoặc năng lực chịu tải từ bộ mẫu nhỏ này.

Các lần chạy tài liệu, RAG và AI ghi thời lượng cùng kết quả chức năng. Tái sử dụng ít nhất một tệp hợp lệ cho mỗi định dạng TXT, MD, PDF từ UAT-06; kiểm biên dung lượng và độ dài ở tầng kiểm tra đầu vào, không cần gọi mô hình lặp cho mỗi trường hợp sai giới hạn. Thời gian truyền tệp qua mạng được ghi riêng; thời hạn xử lý tính theo mục 10.2. Kiểm trước cấu hình bằng đầu vào AI sát giới hạn theo mục 5.5.

Kết quả AI được kỳ vọng có nội dung mà trả `NoEvidence`, `Failed` hoặc quá hạn vẫn là không đạt, dù phản hồi nhanh. Bộ kết quả ghi định danh trường hợp, mô hình, thời lượng, trạng thái và bằng chứng nội dung; không cần tách một báo cáo hiệu năng khác nếu đã đủ các trường này.

Tác vụ kiểm tra trạng thái tự động không được kéo dài phiên không hoạt động. Với LIM-07, hoạt động là yêu cầu nghiệp vụ được xác thực do người dùng chủ động thực hiện; thời hạn tuyệt đối vẫn được kiểm ở máy chủ. Đăng xuất kết thúc phiên hiện tại; đổi hoặc đặt lại mật khẩu thu hồi mọi phiên cũ trong LIM-07. R1 không yêu cầu màn hình liệt kê và thu hồi từng thiết bị.

<a id="muc-12"></a>

## 12. Đánh giá chất lượng AI

Kiểm tra phần mềm xác nhận quyền, trạng thái và cấu trúc. Chất lượng nội dung AI được đánh giá riêng bằng bộ dữ liệu có đáp án hoặc tiêu chí đối chiếu. Kết quả trả sẵn từ dữ liệu kiểm thử, ảnh chụp giao diện hoặc điểm do mô hình tự chấm không đủ để nghiệm thu chất lượng nội dung.

### 12.1 Bộ dữ liệu nghiệm thu

Trước khi chạy, nhóm kiểm thử chốt một danh mục dữ liệu gồm mã trường hợp, phiên bản bộ dữ liệu, tệp và mã băm, ngôn ngữ, chủ sở hữu/Notebook, đoạn nguồn, cấu hình và kết quả kỳ vọng. Tài liệu có thể dùng lại giữa các bộ; một trường hợp có thể đồng thời bao phủ tiếng Anh, nhiều nguồn và dữ kiện mâu thuẫn. Không nhân tất cả tổ hợp cấu hình thành các bộ riêng.

| Bộ | Số lượng tối thiểu | Thành phần và căn cứ đối chiếu |
| --- | --- | --- |
| AEV-01 RAG | 6 trường hợp | 3 câu có căn cứ, 2 câu thiếu căn cứ, 1 câu có nguồn chứa chỉ dẫn gây nhiễu. Trong nhóm có căn cứ phải có nguồn tiếng Anh và một câu tổng hợp nhiều tài liệu; ghi rõ ý cần trả lời và đoạn nguồn. Trường hợp gây nhiễu có câu hỏi trả lời được, kỳ vọng trả lời đúng nguồn và bỏ qua chỉ dẫn trái quyền. |
| AEV-02 Mindmap | 2 trường hợp | Một nguồn đơn và một bộ nhiều nguồn có nội dung giao nhau; danh sách đối chiếu chủ đề và nhánh quan trọng. |
| AEV-03 Tóm tắt | 2 trường hợp | Một nguồn đơn ở mức ngắn, một bộ nhiều nguồn ở mức chi tiết; bộ nhiều nguồn có thông tin mâu thuẫn cần nêu. |
| AEV-04 Slide | 2 trường hợp | Một nguồn đơn tạo 5 trang, một bộ nhiều nguồn tạo 8 trang; có danh sách ý và mạch trình bày kỳ vọng. |
| AEV-05 Quiz | 2 trường hợp | Một nguồn đơn tạo 5 câu, một bộ nhiều nguồn tạo 10 câu; kiểm từng câu, lựa chọn, đáp án và giải thích với nguồn. |
| AEV-06 Báo cáo | 2 trường hợp | Một nguồn đơn và một bộ nhiều nguồn có khoảng trống hoặc mâu thuẫn; mục tiêu khác nhau, có danh sách ý phân tích và kết luận được phép. |
| AEV-07 Ngoại lệ chung | 3 nhóm kiểm tra | Thiếu căn cứ, đầu vào vượt giới hạn và đầu ra sai cấu trúc. Kiểm cơ chế trạng thái dùng chung bằng một công cụ đại diện. Riêng cấu trúc sai phải có dữ liệu giả lập cho cả năm loại đầu ra, có thể chạy bằng một bài kiểm thử tham số hóa. Lỗi nhà cung cấp và quá hạn dùng chung bằng chứng UAT-14. |
| AEV-08 Bảo vệ dữ liệu | 4 tình huống đại diện | Truy cập tài nguyên của tài khoản khác; đưa nguồn từ Notebook khác vào yêu cầu; xóa nguồn trong lúc xử lý; đọc qua API, liên kết hoặc bộ nhớ đệm sau khi mất quyền. Các tình huống dùng chung bằng chứng UAT-12, UAT-13 và UAT-20; không thay thế kiểm tra quyền trên từng loại tài nguyên. |

AEV-01 đến AEV-06 phải chạy trên cấu hình dùng mô hình thực. Chọn trước một trường hợp RAG có căn cứ và một trường hợp công cụ AI để chạy thêm lần thứ hai nhằm quan sát biến động; chấm cả hai lần, không chọn riêng kết quả tốt. Bộ ban đầu có 18 lượt chạy: 6 RAG, 10 công cụ và 2 lượt lặp. Số lần gọi nhà cung cấp thực tế còn phụ thuộc việc phát hiện thiếu căn cứ trước khi gọi mô hình và thử lại nội bộ; phải ghi mức sử dụng thực tế. Con số 18 không gồm embedding, phép thử cấu hình tại mục 5.5 hoặc lần chạy lại sau khi sửa lỗi.

AEV-07 được dùng giả lập có chủ đích để kiểm trạng thái và cấu trúc; không thay bằng chứng nội dung thực của từng công cụ. AEV-08 có thể kiểm ở tầng API hoặc dịch vụ với dữ liệu kiểm soát. Thời lượng các lần chạy thực được dùng lại cho IH-NFR-007.

### 12.2 Tiêu chí đánh giá và điều kiện chấp nhận

| Tiêu chí | Cách đánh giá | Điều kiện đạt R1 |
| --- | --- | --- |
| Cấu trúc và hình thức | Đối chiếu thành phần và giới hạn theo mục 8.4, LIM-17. | Tất cả đầu ra thành công trong mẫu hợp lệ; không lưu đầu ra thô hoặc sai cấu trúc thành sản phẩm hoàn chỉnh. |
| Tham chiếu nguồn | Mở tham chiếu và đối chiếu đúng tài liệu, vị trí, quyền và phạm vi nguồn. | Tất cả tham chiếu trong mẫu hợp lệ; tham chiếu sai hoặc trái quyền phải sửa trước nghiệm thu. |
| Căn cứ của dữ kiện | Người đánh giá đối chiếu các phát biểu thực tế, số liệu và kết luận với nguồn; kiểm phần suy luận theo BR-13. | Không có phát biểu thực tế thiếu căn cứ được phát hiện trong đầu ra nghiệm thu. Một lỗi như vậy làm trường hợp không đạt; không dùng tỷ lệ trung bình để bỏ qua. |
| Ý chính cần đạt | Trước khi chạy, liệt kê 3-5 ý bắt buộc cho mỗi trường hợp có nội dung; có thể ghi thêm ý mở rộng không bắt buộc. | Đầu ra phản ánh đúng toàn bộ ý bắt buộc; không cần giống từng câu chữ trong đáp án mẫu. |
| Thiếu căn cứ của RAG | Đối chiếu hai câu không có đủ căn cứ trong AEV-01. | Cả hai trả `NoEvidence`; lỗi kỹ thuật vẫn là `Failed`. |
| Tính đúng của Quiz | Kiểm từng câu hỏi, tính đơn nghĩa, đáp án, giải thích và nguồn. | Mỗi câu có đúng một đáp án đúng và giải thích có căn cứ; không chấp nhận câu mơ hồ hoặc sai đáp án. |
| Khả năng sử dụng | Đối chiếu hành động sử dụng của từng công cụ: đọc cây, đọc nội dung, trình chiếu, làm bài hoặc tải báo cáo. | Hoàn thành được hành động theo yêu cầu; không có lỗi cấu trúc, nội dung mâu thuẫn với nguồn hoặc câu chữ làm sai nghĩa/cản trở sử dụng. Lỗi trình bày nhỏ xử lý theo mục 14.1. |
| Cách ly và chỉ dẫn độc hại | Kiểm AEV-08 và trường hợp gây nhiễu của AEV-01. | Không mở rộng quyền hoặc nguồn, tiết lộ bí mật hay thực hiện hành động bên ngoài. |

Ví dụ áp dụng BR-13: nguồn nêu “chi phí tháng 6 là 120 triệu đồng, tháng 7 là 100 triệu đồng”. Câu “chi phí giảm 20 triệu đồng” là phép tổng hợp có căn cứ. Câu “chi phí giảm nhờ dùng AI” không đạt nếu nguồn không nêu nguyên nhân. Câu “Đề xuất kiểm tra khả năng tự động hóa; tài liệu chưa đủ dữ kiện để kết luận nguyên nhân giảm chi phí” được phép khi đặt trong phần đề xuất. Gắn nhãn “AI suy luận” cho một nguyên nhân bịa đặt không làm dữ kiện đó hợp lệ.

Người đánh giá phải hiểu bộ nguồn và được chủ sản phẩm chỉ định; một người có thể kiêm nhiệm kiểm thử và đánh giá nội dung. Mỗi kết luận ghi căn cứ hoặc ý chưa đạt. Khi đáp án kỳ vọng chưa rõ, thống nhất lại với chủ sản phẩm và cập nhật phiên bản bộ dữ liệu trước khi chạy lại.

Trường hợp kỳ vọng có câu trả lời phải trả `Answered` hoặc `Succeeded`; `NoEvidence`, `Failed` hoặc nội dung không có dữ kiện cần thiết đều là không đạt. Ghi toàn bộ lần chạy, sửa nguyên nhân và kiểm lại nhóm bị ảnh hưởng; nếu thay đổi cơ chế dùng chung, kiểm lại toàn bộ luồng thành công và ngoại lệ liên quan. Bộ mẫu này xác nhận phạm vi R1 đã kiểm, không chứng minh mô hình luôn đúng trên mọi dữ liệu.

<a id="muc-13"></a>

## 13. Nghiệm thu và truy vết

Các bảng UAT là kịch bản chấp nhận tổng hợp, không phải yêu cầu tạo một bộ kiểm thử riêng cho từng bảng. Nhóm dự án lập một bảng kiểm chứng chung: mã trường hợp, phiên bản SRS, AC, UC/nhánh, dữ liệu và tiền điều kiện, thao tác, kết quả kỳ vọng, kết quả thực tế, bằng chứng và lỗi nếu có. Một trường hợp có thể chứng minh nhiều AC khi từng kết quả được ghi rõ.

Áp dụng kiểm thử theo rủi ro:

- Kiểm bắt buộc các luồng thành công của toàn bộ chức năng, đủ năm công cụ và các điểm có thể sai quyền, mất dữ liệu, sai liên kết tài khoản, sai điểm Quiz hoặc công bố nguồn đã xóa. Mỗi loại tài nguyên phải có bằng chứng kiểm soát quyền và xóa; có thể dùng bảng tham số thay nhiều kịch bản thủ công.
- Với xác thực đầu vào, hiển thị lỗi, mất kết nối, quá hạn và chống gửi lặp dùng chung, kiểm cơ chế một lần ở tầng phù hợp, rồi kiểm các điểm tích hợp có khác biệt. Bảng truy vết ghi rõ phạm vi bao phủ tương đương; nếu các chức năng có cơ chế riêng thì phải kiểm riêng.
- Kiểm cấu trúc hợp lệ và sai cấu trúc của cả năm công cụ; chỉ đánh giá nội dung bằng mô hình thực theo bộ mẫu mục 12. Không lặp toàn bộ ma trận lỗi cho từng công cụ khi dùng chung cơ chế.
- Chọn cách kiểm phù hợp: tự động cho quy tắc, dữ liệu, API và quyền; kiểm thủ công có ghi kết quả cho UI/UX, Figma, nội dung AI và lần khôi phục. Không yêu cầu tự động hóa mọi màn hình hoặc có tỷ lệ bao phủ mã nguồn tùy ý.

Mỗi AC phải có kết luận dựa trên bằng chứng trực tiếp hoặc bao phủ tương đương có giải thích. Không được dùng lựa chọn mẫu để bỏ một hành vi bắt buộc hay ghi toàn bộ nhóm đạt khi còn AC chưa kiểm. Các phép đo thời gian, thông báo và tích hợp được ghi ngay trong cùng ca nghiệp vụ; không yêu cầu nhiều báo cáo trùng nội dung.

### 13.1 Kịch bản nghiệm thu sản phẩm

Các kịch bản sau phải được thực hiện với vai trò, dữ liệu và điều kiện trước và sau thao tác được ghi lại. Trường hợp kiểm thử chi tiết phải bao phủ cả AC thành công và AC ngoại lệ; các kịch bản tổng hợp không thay thế việc kiểm tra từng yêu cầu liên quan.

| Mã | Nhóm | Tình huống chính | Kết quả kỳ vọng |
| --- | --- | --- | --- |
| UAT-01 | Đăng ký và đăng nhập | Đăng ký mới, gửi và xác minh email; liên kết hết hạn hoặc dùng lại; đăng nhập đúng, sai, chưa xác minh; giới hạn tần suất. | Tài khoản và phiên có trạng thái đúng; không tạo trùng tài khoản hoặc cho truy cập dữ liệu trước khi xác minh. |
| UAT-02 | Đăng nhập Google và liên kết danh tính | Danh tính mới/đã liên kết, hủy hoặc phản hồi sai; email trùng tài khoản Active và PendingVerification; mật khẩu, phiên và liên kết cũ trước/sau UC-02.A4. | Chỉ liên kết sau BR-03; tài khoản đăng ký trước không giữ đường truy cập bằng mật khẩu hoặc phiên cũ sau khi chủ email nhận quyền. EML-003 chỉ là thông báo sau liên kết. |
| UAT-03 | Khôi phục và đổi mật khẩu | Email có hoặc chưa có tài khoản; tài khoản chỉ đăng nhập bằng Google; liên kết sai, hết hạn, đã dùng; đổi mật khẩu thành công và thất bại. | Mật khẩu và phiên đăng nhập được xử lý đúng quy tắc; thông báo công khai không tiết lộ tài khoản có tồn tại. |
| UAT-04 | Phiên và hồ sơ cá nhân | Tải lại trang, hết phiên, đăng xuất rồi gọi lại API bằng phiên cũ; sửa hồ sơ và kiểm tra sau khi đăng nhập lại. | Phiên hết hiệu lực bị từ chối; hồ sơ được lưu đúng; dữ liệu cá nhân trong bộ nhớ ứng dụng khách được xóa khi kết thúc phiên. |
| UAT-05 | Quản lý Notebook | Tạo, sửa, xem danh sách và phân trang; tên không hợp lệ, vượt giới hạn số lượng và cập nhật đồng thời. | Chỉ hiển thị Notebook của người dùng; lỗi giới hạn hoặc xung đột không làm mất dữ liệu. |
| UAT-06 | Tiếp nhận và xem tài liệu nguồn | Mỗi định dạng được hỗ trợ; tệp gần giới hạn; PDF chỉ có ảnh hoặc được mã hóa; xem trang và đoạn trích. | Tài liệu chỉ chuyển sang `Ready` khi xử lý hoàn tất; nội dung và vị trí nguồn hiển thị chính xác. |
| UAT-07 | Lỗi xử lý tài liệu và yêu cầu gửi lặp | Lỗi tạo embedding, hết thời gian chờ, khởi động lại giữa tác vụ, thử lại, tệp trùng và mã thao tác tải lên trùng. | Không tạo trùng tài liệu hoặc chỉ mục; không giữ trạng thái `Processing` vô thời hạn; có cách khôi phục hoặc thử lại. |
| UAT-08 | RAG và hội thoại | Sử dụng nguồn mặc định hoặc tự chọn; hỏi đáp, mở tham chiếu nguồn, tạo, đổi tên, xóa và mở lại hội thoại. | Câu trả lời có căn cứ đúng phạm vi; lịch sử được lưu bền vững; giao diện nêu rõ mỗi câu hỏi được xử lý độc lập. |
| UAT-09 | Ngoại lệ RAG | Thiếu căn cứ, nguồn không hợp lệ, hết hạn mức, hết thời gian chờ, tham chiếu sai và gửi lặp. | Phân biệt `NoEvidence` với `Failed`; không công bố câu trả lời hoặc tham chiếu nguồn không hợp lệ. |
| UAT-10 | Quản lý ghi chú | Tạo, đọc, sửa, xóa ghi chú; lưu từ hỏi đáp và bản tóm tắt; xung đột cập nhật; xóa nguồn xuất xứ. | Ghi chú là bản sao độc lập, giữ thông tin xuất xứ và không tự ghi đè phiên bản mới. |
| UAT-11 | Đầy đủ năm công cụ AI | Chạy từng công cụ với cấu hình riêng; kiểm tra hiển thị, tham chiếu nguồn, lưu, mở, lọc, đổi tên và tạo lại; làm Quiz, trình chiếu Slide, tải báo cáo Markdown. | Cả năm công cụ đáp ứng yêu cầu riêng và đạt bộ đánh giá AEV tương ứng. |
| UAT-12 | Xóa dữ liệu trong các giai đoạn xử lý | Xóa tài liệu, Notebook, kết quả AI hoặc hội thoại trước, trong và sau tác vụ; truy cập đường dẫn cũ; kiểm tra tài nguyên con. | Dữ liệu đã xóa không xuất hiện lại; kết quả lịch sử tuân theo chính sách giữ nội dung và đánh dấu nguồn đã xóa. |
| UAT-13 | Truy cập trái phép và nội dung độc hại | Hai tài khoản, hai Notebook; thay định danh, đường dẫn tải xuống, phạm vi truy xuất, bộ nhớ đệm; chèn mã lệnh vào nội dung. | Không tiết lộ nội dung hoặc thông tin mô tả ngoài quyền truy cập; không thực thi mã lệnh từ dữ liệu. |
| UAT-14 | Ngoại lệ công cụ AI | Bộ AEV-07; hết hạn mức, quá thời hạn xử lý, sai cấu trúc đầu ra, thiếu căn cứ và thử lại. | Trạng thái phản ánh đúng nguyên nhân; không lưu kết quả không hợp lệ như kết quả thành công hoặc tạo trùng kết quả. |
| UAT-15 | UI/UX và Figma | Đối chiếu UI-01 đến UI-08 trên máy tính và thiết bị di động; thao tác bàn phím, tương phản, trạng thái rỗng và lỗi. | Các hành trình đáp ứng thiết kế đã phê duyệt; không có lỗi cản trở thao tác chính. |
| UAT-16 | Tái lập môi trường và vận hành | Cài đặt sạch, cấu hình, API, dịch vụ thực, khởi động lại, nhật ký; sao lưu thủ công và một lần khôi phục trên môi trường riêng. | Tái lập được môi trường; nội dung và quyền khớp bản sao lưu, dữ liệu hiện hành không bị thay thế; dọn dữ liệu kiểm chứng sau hoàn tất. |
| UAT-17 | Thời gian phản hồi | 10 thao tác không gọi AI theo LIM-15; tái sử dụng thời lượng xử lý tệp và bộ AEV; ghi mọi lỗi hoặc quá hạn. | Thao tác nghiệp vụ đạt LIM-15, xử lý tài liệu và AI đạt LIM-11 trên cấu hình đã ghi nhận; không yêu cầu kiểm thử tải riêng. |
| UAT-18 | Thông báo và trạng thái có thể xem lại | Danh mục MSG; phản hồi khi mất mạng chưa biết kết quả; lỗi trường; xác nhận xóa; tải lại/chuyển trang; bàn phím và trình đọc màn hình. | Đúng ý nghĩa/vị trí/thời gian tồn tại, không báo thành công trước khi lưu; trạng thái nghiệp vụ không mất khi đóng thông báo, không tiết lộ dữ liệu. |
| UAT-19 | Email giao dịch và bảo vệ tài khoản | EML-001 đến EML-005 qua dịch vụ thực; tài khoản không tồn tại/chỉ đăng nhập bằng Google; liên kết hết hạn, dùng lại, gửi lại; lỗi vận chuyển có chủ đích. | Đúng người nhận và mục đích; liên kết cũ vô hiệu theo quy tắc; lỗi gửi không hoàn tác mật khẩu; phản hồi công khai không xác nhận tồn tại tài khoản. |
| UAT-20 | Hợp đồng dữ liệu và xử lý đồng thời | Quy tắc mục 8.3-8.5 và 10.1-10.2: mặc định, Unicode, biên giới hạn, cấu trúc AI, phân trang, cùng mã khác nội dung, nộp Quiz lặp và xóa trong khi xử lý. | Máy chủ kiểm dữ liệu, chống ghi đè/trùng, đầu ra đúng cấu trúc, API trước nộp không lộ lời giải, thời hạn không đặt lại khi thử nội bộ. |
| UAT-21 | Bảo vệ phiên trình duyệt | Phiên trước/sau đăng nhập, yêu cầu giả mạo từ nguồn không được phép, bộ nhớ đệm giữa hai tài khoản, hết hạn khi chỉ đọc trạng thái tự động. | Phiên và dữ liệu cá nhân được bảo vệ theo IH-NFR-011; cơ chế đã chọn có bằng chứng, các luồng hợp lệ vẫn hoàn thành. |

### 13.2 Truy vết mục tiêu tới nhóm yêu cầu

| Mục tiêu | Yêu cầu chi phối | Nghiệm thu chính |
| --- | --- | --- |
| OBJ-01 | IH-AUTH, IH-NB, IH-DOC, IH-NOTE, IH-NFR-002 | UAT-01 đến UAT-07, UAT-10, UAT-12, UAT-13 |
| OBJ-02 | IH-CHAT, IH-DOC-005, IH-DOC-006, IH-NFR-002, IH-NFR-003 | UAT-08, UAT-09, UAT-12, UAT-13; AEV-01 |
| OBJ-03 | IH-AI, IH-MM, IH-SUM, IH-SLD, IH-QUIZ, IH-RPT, IH-OUT | UAT-11, UAT-14; AEV-02 đến AEV-07 |
| OBJ-04 | IH-UX; hành vi giao diện trong các nhóm chức năng | UAT-15 và luồng giao diện của UAT-01 đến UAT-14 |
| OBJ-05 | IH-INT, IH-NFR, IH-REL, IH-DATA | UAT-12 đến UAT-17; UAT-20; UAT-21 |

### 13.3 Ma trận truy vết yêu cầu, ca sử dụng và nghiệm thu

Mỗi yêu cầu có mã AC ngay tại nơi đặc tả. Bản ghi kiểm thử phải ghi phiên bản SRS, ID yêu cầu và AC, dữ liệu đầu vào, kết quả kỳ vọng và kết quả thực tế, trạng thái, bằng chứng và mã lỗi nếu có. Bảng dưới hỗ trợ tra cứu phạm vi; nhóm REL được định nghĩa ở mục 14.

| Yêu cầu | Ca sử dụng | Kịch bản UAT | Số AC |
| --- | --- | --- | --- |
| IH-AUTH-001 | UC-01 | UAT-01 | 2 |
| IH-AUTH-002 | UC-01 | UAT-01 | 2 |
| IH-AUTH-003 | UC-10 | UAT-01 | 2 |
| IH-AUTH-004 | UC-11 | UAT-02 | 2 |
| IH-AUTH-005 | UC-02; UC-11 | UAT-02; UAT-03 | 4 |
| IH-AUTH-006 | UC-02 | UAT-03 | 2 |
| IH-AUTH-007 | UC-02 | UAT-03 | 3 |
| IH-AUTH-008 | UC-01; UC-02; UC-10; UC-11; UC-13; UC-14 | UAT-04 | 2 |
| IH-AUTH-009 | UC-12 | UAT-04 | 2 |
| IH-AUTH-010 | UC-13 | UAT-03 | 2 |
| IH-NB-001 | UC-03 | UAT-05 | 2 |
| IH-NB-002 | UC-03 | UAT-05 | 2 |
| IH-NB-003 | UC-03 | UAT-12 | 2 |
| IH-NB-004 | UC-03; UC-04; UC-05; UC-06; UC-07; UC-08 | UAT-13 | 2 |
| IH-DOC-001 | UC-04 | UAT-06 | 2 |
| IH-DOC-002 | UC-04 | UAT-06 | 2 |
| IH-DOC-003 | UC-04 | UAT-07 | 2 |
| IH-DOC-004 | UC-04 | UAT-07 | 2 |
| IH-DOC-005 | UC-04; UC-05; UC-07 | UAT-06; UAT-08; UAT-12 | 2 |
| IH-DOC-006 | UC-04; UC-08 | UAT-12 | 2 |
| IH-CHAT-001 | UC-05 | UAT-08 | 2 |
| IH-CHAT-002 | UC-05 | UAT-08 | 2 |
| IH-CHAT-003 | UC-05 | UAT-09 | 2 |
| IH-CHAT-004 | UC-05 | UAT-08; UAT-12 | 5 |
| IH-CHAT-005 | UC-05 | UAT-09; UAT-12 | 2 |
| IH-NOTE-001 | UC-06 | UAT-10 | 4 |
| IH-NOTE-002 | UC-06 | UAT-10; UAT-12 | 2 |
| IH-AI-001 | UC-07 | UAT-11 | 2 |
| IH-AI-002 | UC-07 | UAT-11 | 2 |
| IH-AI-003 | UC-07 | UAT-11; UAT-14 | 2 |
| IH-AI-004 | UC-07; UC-08 | UAT-11; UAT-12 | 2 |
| IH-MM-001 | UC-07 | UAT-11 | 2 |
| IH-MM-002 | UC-08 | UAT-11; UAT-15 | 2 |
| IH-SUM-001 | UC-07 | UAT-11 | 2 |
| IH-SUM-002 | UC-06; UC-08 | UAT-10; UAT-11 | 2 |
| IH-SLD-001 | UC-07 | UAT-11 | 2 |
| IH-SLD-002 | UC-08 | UAT-11; UAT-15 | 2 |
| IH-QUIZ-001 | UC-07 | UAT-11 | 2 |
| IH-QUIZ-002 | UC-08 | UAT-11 | 2 |
| IH-RPT-001 | UC-07 | UAT-11 | 2 |
| IH-RPT-002 | UC-08 | UAT-11; UAT-13 | 2 |
| IH-OUT-001 | UC-08 | UAT-11; UAT-13 | 2 |
| IH-OUT-002 | UC-08 | UAT-11; UAT-12 | 2 |
| IH-OUT-003 | UC-08 | UAT-12 | 2 |
| IH-DATA-001 | UC-01; UC-03; UC-04; UC-05; UC-06; UC-07; UC-08; UC-12 | UAT-05; UAT-06; UAT-08; UAT-10; UAT-11; UAT-20 | 6 |
| IH-DATA-002 | UC-03; UC-04; UC-05; UC-06; UC-08 | UAT-10; UAT-11; UAT-12; UAT-20 | 4 |
| IH-UX-001 | UC-01; UC-02; UC-03; UC-04; UC-05; UC-06; UC-07; UC-08; UC-10; UC-11; UC-12; UC-13; UC-14 | UAT-15 | 2 |
| IH-UX-002 | UC-01; UC-02; UC-03; UC-04; UC-05; UC-06; UC-07; UC-08; UC-10; UC-11; UC-12; UC-13; UC-14 | UAT-15 | 2 |
| IH-UX-003 | UC-01; UC-02; UC-03; UC-04; UC-05; UC-06; UC-07; UC-08; UC-10; UC-11; UC-12; UC-13; UC-14 | UAT-15 | 2 |
| IH-UX-004 | UC-01; UC-02; UC-03; UC-04; UC-05; UC-06; UC-07; UC-08; UC-10; UC-11; UC-12; UC-13; UC-14 | UAT-07; UAT-09; UAT-14; UAT-15 | 2 |
| IH-MSG-001 | UC-01; UC-02; UC-03; UC-04; UC-05; UC-06; UC-07; UC-08; UC-09; UC-10; UC-11; UC-12; UC-13; UC-14; UC-15; UC-16 | UAT-18 | 2 |
| IH-MSG-002 | UC-01; UC-02; UC-03; UC-04; UC-05; UC-06; UC-07; UC-08; UC-10; UC-11; UC-12; UC-13; UC-14 | UAT-15; UAT-18 | 2 |
| IH-MSG-003 | UC-01; UC-02; UC-11; UC-13; UC-15 | UAT-01; UAT-02; UAT-03; UAT-19 | 3 |
| IH-MSG-004 | UC-04; UC-05; UC-07; UC-08 | UAT-07; UAT-09; UAT-14; UAT-18 | 2 |
| IH-INT-001 | UC-01; UC-02; UC-03; UC-04; UC-05; UC-06; UC-07; UC-08; UC-10; UC-11; UC-12; UC-13; UC-14; UC-15 | UAT-16 | 2 |
| IH-INT-002 | UC-04; UC-05; UC-07; UC-15 | UAT-06; UAT-11; UAT-15; UAT-16 | 3 |
| IH-INT-003 | UC-01; UC-02; UC-05; UC-07; UC-10; UC-11; UC-13; UC-15 | UAT-01; UAT-02; UAT-03; UAT-11; UAT-16 | 2 |
| IH-INT-004 | UC-03; UC-04; UC-05; UC-06; UC-07; UC-08; UC-14; UC-15 | UAT-07; UAT-09; UAT-12; UAT-16; UAT-17; UAT-20 | 2 |
| IH-NFR-001 | UC-01; UC-02; UC-10; UC-11; UC-13; UC-14 | UAT-01; UAT-02; UAT-03; UAT-04 | 5 |
| IH-NFR-002 | UC-03; UC-04; UC-05; UC-06; UC-07; UC-08 | UAT-12; UAT-13 | 2 |
| IH-NFR-003 | UC-04; UC-05; UC-06; UC-07; UC-08; UC-12 | UAT-13; UAT-14 | 2 |
| IH-NFR-004 | UC-03; UC-04; UC-05; UC-06; UC-07; UC-08; UC-09; UC-15 | UAT-07; UAT-12; UAT-16 | 2 |
| IH-NFR-005 | UC-04; UC-05; UC-07; UC-09; UC-15 | UAT-07; UAT-09; UAT-14; UAT-16 | 2 |
| IH-NFR-006 | UC-03; UC-04; UC-08 | UAT-17 | 2 |
| IH-NFR-007 | UC-05; UC-07 | UAT-17 | 2 |
| IH-NFR-008 | UC-09; UC-15; UC-16 | UAT-16 | 2 |
| IH-NFR-009 | UC-09; UC-16 | UAT-16 | 2 |
| IH-NFR-010 | UC-15 | UAT-16 | 2 |
| IH-NFR-011 | UC-01; UC-02; UC-10; UC-11; UC-12; UC-13; UC-14 | UAT-04; UAT-13; UAT-21 | 2 |
| IH-REL-001 | UC-01; UC-02; UC-03; UC-04; UC-05; UC-06; UC-07; UC-08; UC-09; UC-10; UC-11; UC-12; UC-13; UC-14; UC-15; UC-16 | UAT-01; UAT-02; UAT-03; UAT-04; UAT-05; UAT-06; UAT-07; UAT-08; UAT-09; UAT-10; UAT-11; UAT-12; UAT-13; UAT-14; UAT-15; UAT-16; UAT-17; UAT-18; UAT-19; UAT-20; UAT-21 | 2 |
| IH-REL-002 | UC-09; UC-15; UC-16 | UAT-16 | 2 |
| IH-REL-003 | UC-15 | UAT-16 | 2 |

<a id="muc-14"></a>

## 14. Điều kiện bàn giao và kiểm soát thay đổi

### IH-REL-001: Điều kiện nghiệm thu R1

**Yêu cầu:** Sản phẩm chỉ được đề nghị nghiệm thu R1 khi đáp ứng toàn bộ yêu cầu bắt buộc trong SRS.

- **IH-REL-001-AC01:** Tất cả AC có bằng chứng trực tiếp hoặc bao phủ tương đương cùng kết quả riêng theo mục 13; UAT-01 đến UAT-21 cùng các bộ AEV đạt; cả năm công cụ AI được triển khai đầy đủ, không ghi “không áp dụng” vì chỉ triển khai một phần.
- **IH-REL-001-AC02:** Không còn lỗi chặn luồng chính, mất dữ liệu, sai quyền hoặc sai đáp án Quiz đã biết. Lỗi trình bày nhỏ còn lại có danh sách và chấp thuận của chủ sản phẩm.

**Truy vết:** UC-01 đến UC-16; UAT-01 đến UAT-21

### IH-REL-002: Hồ sơ bàn giao

**Yêu cầu:** Bản bàn giao phải chứa đủ thông tin để sử dụng, vận hành và kiểm chứng phiên bản sản phẩm.

- **IH-REL-002-AC01:** Hồ sơ bàn giao phải có phiên bản phát hành, mã nguồn, danh sách thư viện phụ thuộc, hướng dẫn cài đặt và cấu hình, quy trình cập nhật cơ sở dữ liệu, đặc tả API, hướng dẫn sử dụng, hướng dẫn sao lưu và khôi phục, phiên bản Figma, kết quả kiểm thử chức năng, chất lượng AI và thời gian xử lý. Có thể lưu trong một bảng kiểm chứng chung, không yêu cầu ba báo cáo riêng.
- **IH-REL-002-AC02:** Hồ sơ bàn giao phải ghi các hạn chế đã biết, hồ sơ cấu hình nghiệm thu và hướng dẫn quản lý thông tin bí mật. Không đưa tài khoản cá nhân, khóa bí mật thật hoặc dữ liệu chưa được phép sử dụng vào gói bàn giao.

**Truy vết:** UC-09; UC-15; UC-16; UAT-16

### IH-REL-003: Quản lý thay đổi yêu cầu

**Yêu cầu:** Mọi thay đổi phạm vi đã được phê duyệt phải được ghi nhận và đối chiếu tác động trước khi phát hành phiên bản mới.

- **IH-REL-003-AC01:** Hồ sơ thay đổi phải nêu yêu cầu bị ảnh hưởng, lý do, tác động đến dữ liệu, quyền truy cập, tích hợp, giao diện, kiểm thử và quyết định của chủ sản phẩm. SRS và ma trận truy vết phải được cập nhật đồng bộ.
- **IH-REL-003-AC02:** Kiểm thử hồi quy bao phủ phần bị ảnh hưởng; một yêu cầu bị hoãn phải thể hiện qua phiên bản và phạm vi được duyệt, không được giữ nhãn đáp ứng R1 khi còn thiếu chức năng bắt buộc.

**Truy vết:** UC-15; UAT-16

### 14.1 Phân loại lỗi để quyết định bàn giao

| Mức độ lỗi | Định nghĩa | Xử lý trước nghiệm thu |
| --- | --- | --- |
| Chặn nghiệm thu | Sai quyền, tiết lộ thông tin bí mật, mất hoặc hỏng dữ liệu, không chạy được luồng chính hoặc thiếu bất kỳ công cụ bắt buộc. | Phải sửa và kiểm lại. |
| Nghiêm trọng | Sai nghiệp vụ, sai cấu trúc hoặc đáp án, sai nguồn, không đạt ngưỡng AI hoặc hiệu năng; không có cách sử dụng đáp ứng yêu cầu. | Phải sửa và kiểm lại nhóm bị ảnh hưởng. |
| Nhỏ | Lỗi trình bày hoặc câu chữ không làm sai dữ liệu, quyền, hành vi bắt buộc hoặc cản trở hành trình. | Ghi danh sách, hướng khắc phục và quyết định chấp thuận cụ thể. |

### 14.2 Cấu hình phải ghi nhận khi nghiệm thu

Hồ sơ cấu hình nghiệm thu phải ghi nhận:

- Tên và phiên bản dịch vụ xác thực; định danh ứng dụng Google và địa chỉ nhận kết quả xác thực (callback).
- Cấu hình liên kết danh tính theo email và dịch vụ gửi email.
- Mô hình embedding và số chiều véc-tơ; mô hình sinh nội dung và các tham số; phiên bản chỉ dẫn gửi tới mô hình.
- Môi trường triển khai, phiên bản trình duyệt, phiên bản Figma và mã băm của bộ dữ liệu nghiệm thu.

Các giá trị này thuộc quyết định thiết kế và triển khai. Phải chốt trước khi kiểm thử và kiểm tra lại khi có thay đổi.

Việc sử dụng dịch vụ bên ngoài không miễn trừ các ngưỡng nghiệm thu trong SRS. Nếu cấu hình được chọn không đáp ứng yêu cầu khi kiểm chứng, nhóm dự án phải điều chỉnh giải pháp hoặc đề xuất thay đổi có căn cứ để chủ sản phẩm xem xét. Không được tự hạ ngưỡng yêu cầu trong biên bản kiểm thử.

<a id="implementation-decisions"></a>

### 14.3 Tài liệu thiết kế và điều kiện triển khai

Nhóm dự án xác định các quyết định dưới đây trước hoạt động phụ thuộc. Có thể ghi chung trong README, một hồ sơ thiết kế ngắn và bảng kiểm chứng của repository, kèm liên kết tới SRS; không yêu cầu mỗi dòng là một tài liệu độc lập. Các vai trò có thể do cùng một người đảm nhiệm. Các quyết định cấu hình trong bảng hiện đang chờ nhóm triển khai xác nhận; tài liệu này không xác lập kết quả thử nghiệm chưa thực hiện.

| Tài liệu hoặc quyết định | Nội dung cần xác định | Trách nhiệm và thời điểm hoàn thành |
| --- | --- | --- |
| Phạm vi và cấu hình R1 | Phiên bản SRS được sử dụng, các giới hạn LIM và quyết định đối với thay đổi yêu cầu. Mọi thay đổi ngưỡng phải có lý do và đánh giá tác động. | Chủ sản phẩm xác nhận trước khi sử dụng làm căn cứ nghiệm thu. |
| Thiết kế Figma | Liên kết và phiên bản thiết kế; các màn hình UI-01 đến UI-08; luồng tài khoản; trạng thái chưa có dữ liệu, đang xử lý, lỗi và xung đột; giao diện năm công cụ AI; thông báo và hai kích thước trong LIM-16. | Người thiết kế và chủ sản phẩm hoàn tất trước khi đối chiếu giao diện triển khai với thiết kế. |
| Thiết kế dữ liệu và API | Sơ đồ quan hệ, cấu trúc đầu ra AI có phiên bản, phân trang, mã lỗi và thông báo, quyền truy cập, kiểm soát gửi lặp, chính sách xóa và phục hồi theo mục 8 và 10. | Nhóm kỹ thuật hoàn tất trước khi tích hợp các thành phần. |
| Cấu hình xác thực, Google và email | Nhà cung cấp, bằng chứng mật khẩu và liên kết Google theo BR-03, xử lý tài khoản chờ xác minh, thu hồi phiên, tên miền/callback, địa chỉ gửi và hỗ trợ, mẫu email và trạng thái gửi. Ưu tiên kiểm chứng khả năng sẵn có của dịch vụ được chọn. | Nhóm kỹ thuật xác định và thử luồng rủi ro trước triển khai Auth; ghi phần đã kiểm và giới hạn còn lại, không chờ đến nghiệm thu. |
| Cấu hình RAG và AI | Mô hình embedding, chia đoạn/truy xuất, giới hạn ngữ cảnh, mô hình sinh nội dung, phiên bản chỉ dẫn và kiểm cấu trúc. Ghi phép thử đầu vào sát LIM-05, định dạng LIM-03 và thời hạn LIM-11; công bố phạm vi dữ liệu gửi dịch vụ theo IH-INT-002-AC03. | Nhóm kỹ thuật thử cấu hình trước khi phát triển tính năng phụ thuộc; sau đó dùng lại cấu hình đã chốt cho AEV, ghi thay đổi nếu có. |
| Bộ dữ liệu và hồ sơ kiểm thử | Một bộ nguồn được phép sử dụng, mã băm, các ý bắt buộc của AEV, bảng kiểm chứng AC và nhánh UC theo rủi ro; ghi luôn thông báo, thời lượng và lỗi trong cùng kết quả. | Nhóm dự án chốt dữ liệu trước kiểm thử; người đánh giá nội dung đối chiếu trước nghiệm thu. |
| Hướng dẫn triển khai và vận hành | Cài đặt mới, biến cấu hình, quản lý bí mật, sao lưu thủ công, khôi phục trong môi trường riêng, dọn dữ liệu theo thời hạn và đối soát lỗi email/tác vụ. Dùng công cụ sẵn có, không yêu cầu xây giao diện vận hành. | Nhóm kỹ thuật kiểm chứng một lần theo UC-09, UC-15 và UC-16 trước bàn giao; lưu lệnh thực hiện và kết quả trong README hoặc hướng dẫn cùng repository. |

<a id="muc-15"></a>

## 15. Quản lý tài liệu và nguồn tham khảo

### 15.1 Lịch sử phiên bản

| Phiên bản | Ngày | Nội dung thay đổi |
| --- | --- | --- |
| 1.0 / 1.1 | 10-12/09/2026 | Đặc tả theo phạm vi Enterprise Knowledge Management trước khi thay đổi định hướng sản phẩm. |
| 2.0 | 18/09/2026 | Xác định phạm vi sản phẩm cá nhân: tài khoản, Notebook, tài liệu, hỏi đáp RAG, ghi chú, năm công cụ AI và UI/UX theo Figma. |
| 2.1 | 18/09/2026 | Chuẩn hóa văn phong, thuật ngữ và cấu trúc; sử dụng Markdown làm nguồn biên soạn. |
| 2.2 | 18/09/2026 | Chi tiết hóa 16 ca sử dụng; bổ sung yêu cầu dữ liệu, thông báo, email, giao tiếp tác vụ và bảo vệ phiên. Tài liệu có 72 yêu cầu, 144 tiêu chí chấp nhận và 21 kịch bản UAT. |
| 2.3 | 18/09/2026 | Chuẩn hóa tiêu đề và mô tả, làm rõ câu chữ, tách dữ liệu đầu vào và kết quả đầu ra trong ca sử dụng; lược bỏ nội dung trùng lặp và giải thích về quá trình biên soạn. Giữ nguyên phạm vi và ràng buộc nghiệp vụ của bản 2.2. |
| 2.4 | 18/09/2026 | Làm rõ liên kết Google và tài khoản chờ xác minh, điều kiện từng thao tác trong ca sử dụng, dữ liệu theo trạng thái và thông tin xử lý dữ liệu; tách các AC cần kết quả riêng. Thu gọn bộ nghiệm thu AI, kiểm tra thời gian phản hồi và sao lưu/khôi phục theo cấu hình local/sandbox; giữ đủ năm công cụ và các yêu cầu bảo vệ dữ liệu. |

### 15.2 Trách nhiệm rà soát

| Vai trò | Phạm vi rà soát | Trạng thái |
| --- | --- | --- |
| Chủ sản phẩm và chủ tài liệu | Đinh Xuân Công: mục tiêu, phạm vi, quy tắc nghiệp vụ và ngưỡng nghiệm thu. | Chờ rà soát |
| Đại diện kỹ thuật | Tính khả thi, dữ liệu, xác thực, tích hợp, thời hạn xử lý và cấu hình đo hiệu năng; nhân sự do chủ sản phẩm phân công. | Thực hiện khi rà soát kỹ thuật |
| Đại diện UI/UX | Luồng thao tác của người dùng, các màn hình và trạng thái, khả năng thích ứng với kích thước màn hình, khả năng tiếp cận và Figma. | Thực hiện khi rà soát thiết kế |
| Đại diện QA và người dùng | Khả năng kiểm chứng, đáp án và tiêu chí đối chiếu AI, trường hợp kiểm thử, UAT và điều kiện bàn giao. | Thực hiện khi rà soát nghiệm thu |

Kết quả rà soát phải ghi nhận người thực hiện, ngày rà soát, phiên bản tài liệu và các vấn đề cần xử lý. Khi phê duyệt, chủ sản phẩm xác nhận phiên bản SRS được sử dụng làm căn cứ nghiệm thu.

### 15.3 Tài liệu tham khảo

Các tài liệu dưới đây được sử dụng để tham khảo cách đặc tả yêu cầu, ca sử dụng, bảo mật và khả năng tiếp cận. Phạm vi bắt buộc của InsightHub được xác định bởi các yêu cầu trong SRS. Các nguồn đã được đối chiếu ngày 18/09/2026.

| Mã | Tài liệu | Nội dung tham khảo |
| --- | --- | --- |
| S1 | [NASA - How to Write a Good Requirement](https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/) | Cách viết yêu cầu rõ nghĩa, nhất quán và kiểm chứng được. |
| S2 | [OWASP - Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) | Bảo vệ mật khẩu, tái xác thực và phản hồi lỗi xác thực. |
| S3 | [OWASP - Forgot Password Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html) | Khôi phục mật khẩu, liên kết dùng một lần và hạn chế tiết lộ thông tin tài khoản. |
| S4 | [OWASP - Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) | Kiểm tra quyền truy cập cho từng yêu cầu xử lý. |
| S5 | [W3C - WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Các tiêu chí tương phản, bàn phím, tiêu điểm, nhãn và thông báo lỗi được nêu trong IH-UX và IH-MSG. |
| S6 | [IBM Rational - Tips for writing good use cases](https://public.dhe.ibm.com/software/rational/web/whitepapers/RAW14023-USEN-00.pdf), James Heumann, tháng 5/2008 | Mô tả luồng chính, điều kiện phát sinh nhánh và cách tiếp tục hoặc kết thúc. |
| S7 | [Use-Case Foundation](https://www.ivarjacobson.com/publications/use-case-foundation), Ivar Jacobson và Alistair Cockburn | Mục tiêu tác nhân, phạm vi hệ thống và các luồng tương tác. |
| S8 | [W3C - Understanding SC 4.1.3: Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) | Thông báo trạng thái có thể được công nghệ hỗ trợ nhận biết. |
| S9 | [W3C - Understanding SC 3.3.1: Error Identification](https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html) | Xác định lỗi nhập liệu bằng văn bản. |
| S10 | [W3C - Understanding SC 3.3.3: Error Suggestion](https://www.w3.org/WAI/WCAG22/Understanding/error-suggestion.html) | Hướng dẫn sửa lỗi phù hợp với yêu cầu bảo vệ thông tin. |
| S11 | [GOV.UK Design System - Notification banner](https://design-system.service.gov.uk/components/notification-banner/) | Phân biệt thông báo toàn trang với phản hồi tại trường nhập liệu. |
| S12 | [OWASP - Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) | Bảo vệ và quản lý vòng đời phiên đăng nhập. |
| S13 | [OWASP - Cross-Site Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html) | Ngăn yêu cầu giả mạo theo cơ chế xác thực được sử dụng. |
