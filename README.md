# PDF to Markdown with MinerU

Công cụ chuyển đổi hàng loạt tài liệu PDF sang Markdown bằng MinerU API.

Dự án được sử dụng để xử lý các tài liệu đề cương học phần. Mỗi PDF đầu vào được chuyển thành một file Markdown có cùng tên.

## Chức năng

- Đọc toàn bộ file PDF trong thư mục đầu vào.
- Gửi từng PDF tới MinerU API.
- Hỗ trợ OCR cho PDF dạng ảnh hoặc bản quét.
- Hỗ trợ nhận dạng bảng.
- Chuyển mỗi PDF thành một file Markdown.
- Tự động tiếp tục với file tiếp theo nếu một file gặp lỗi.
- Thống kê số file thành công và thất bại.

## Luồng xử lý

```text
PDF
 ↓
MinerU API
 ↓
OCR và nhận dạng bảng
 ↓
Markdown
```

Dự án này chỉ thực hiện chuyển đổi PDF sang Markdown, chưa thực hiện trích xuất JSON.

## Cấu trúc dự án

```text
pdf-to-markdown-mineru/
├── config/
│   ├── __init__.py
│   └── settings.py
├── scripts/
│   └── 01_pdf_to_markdown.py
├── data/
│   ├── 00_input/
│   │   └── pdf/
│   └── 01_markdown/
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

Các thư mục `data/`, file `.env` và môi trường `.venv` không được đưa lên GitHub.

## Yêu cầu

- Python 3.10 trở lên.
- Tài khoản MinerU.
- MinerU API token.
- Kết nối Internet.

## Cài đặt

Clone repository:

```bash
git clone https://github.com/trandinhbac11/pdf-to-markdown-mineru.git
cd pdf-to-markdown-mineru
```

Tạo môi trường Python:

```bash
python -m venv .venv
```

Kích hoạt môi trường trong Git Bash trên Windows:

```bash
source .venv/Scripts/activate
```

Cài đặt thư viện:

```bash
pip install -r requirements.txt
```

## Cấu hình API

Tạo file `.env` tại thư mục gốc:

```env
MINERU_TOKEN=your_mineru_token
```

Không đưa khóa API thật vào source code hoặc GitHub.

## Chuẩn bị dữ liệu

Vì thư mục `data/` không được lưu trên GitHub, hãy tạo lại:

```bash
mkdir -p data/00_input/pdf
mkdir -p data/01_markdown
```

Đưa các file PDF vào:

```text
data/00_input/pdf/
```

Ví dụ:

```text
data/00_input/pdf/
├── IT6086_EN_DCCT_Web Programming in ASP.NET.pdf
├── IT6126_DCCT_He thong co so du lieu.pdf
└── IT6168_DCCT_Lap trinh an toan.pdf
```

## Cách chạy

Tại thư mục gốc của dự án, chạy:

```bash
python scripts/01_pdf_to_markdown.py
```

Chương trình sẽ xử lý lần lượt tất cả file PDF trong thư mục đầu vào.

## Kết quả

Các file Markdown được lưu tại:

```text
data/01_markdown/
```

Tên Markdown tương ứng với tên PDF:

```text
data/01_markdown/
├── IT6086_EN_DCCT_Web Programming in ASP.NET.md
├── IT6126_DCCT_He thong co so du lieu.md
└── IT6168_DCCT_Lap trinh an toan.md
```

## Kiểm tra kết quả

Sau khi chuyển đổi, cần đối chiếu Markdown với PDF gốc, đặc biệt tại:

- Mã và tên học phần.
- Số tín chỉ.
- Mục tiêu học phần.
- Chuẩn đầu ra.
- Bảng nội dung giảng dạy.
- Các quan hệ học phần.
- Nội dung ở đầu và cuối tài liệu.

Việc chương trình báo thành công chỉ xác nhận MinerU đã tạo được Markdown, không bảo đảm toàn bộ nội dung đã được nhận dạng hoàn toàn chính xác.

## Bảo mật dữ liệu

Repository không lưu trữ:

- MinerU API token.
- PDF đầu vào.
- Markdown đầu ra.
- Môi trường Python `.venv`.

Các nội dung này được loại trừ bằng `.gitignore`.

Không sử dụng `git add -f` với những file dữ liệu bị bỏ qua.
