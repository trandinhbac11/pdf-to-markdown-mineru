import os
from pathlib import Path

from dotenv import load_dotenv


# Thư mục gốc prj_1
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Đọc biến môi trường trong file .env
ENV_FILE = PROJECT_DIR / ".env"
load_dotenv(ENV_FILE)

# Khóa API
MINERU_TOKEN = os.getenv("MINERU_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Các thư mục dữ liệu
INPUT_PDF_DIR = PROJECT_DIR / "data" / "00_input" / "pdf"
MARKDOWN_DIR = PROJECT_DIR / "data" / "01_markdown"
EXTRACTED_JSON_DIR = PROJECT_DIR / "data" / "02_extracted_json"
PROVENANCE_DIR = PROJECT_DIR / "data" / "03_provenance"
CANONICAL_DIR = PROJECT_DIR / "data" / "04_canonical"

# JSON Schema dùng cho đề cương học phần
COURSE_SCHEMA_FILE = (
    PROJECT_DIR
    / "schemas"
    / "course_extraction.schema.json"
)