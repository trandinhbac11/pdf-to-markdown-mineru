import sys
import time
from pathlib import Path

from mineru import MinerU


PROJECT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_DIR))

from config.settings import INPUT_PDF_DIR, MARKDOWN_DIR, MINERU_TOKEN


def main() -> None:
    if not MINERU_TOKEN:
        raise RuntimeError(
            "Không tìm thấy MINERU_TOKEN trong file .env"
        )

    pdf_files = sorted(INPUT_PDF_DIR.glob("*.pdf"))

    if not pdf_files:
        raise FileNotFoundError(
            f"Không có PDF trong: {INPUT_PDF_DIR}"
        )

    MARKDOWN_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Tìm thấy {len(pdf_files)} file PDF.")

    client = MinerU()
    success_count = 0
    failed_files = []

    try:
        for pdf_file in pdf_files:
            print("\n" + "=" * 60)
            print(f"Đang xử lý: {pdf_file.name}")

            try:
                batch_id = client.submit(
                    str(pdf_file),
                    model="vlm",
                    ocr=True,
                    table=True,
                )

                print(f"Batch ID: {batch_id}")

                while True:
                    result = client.get_batch(batch_id)[0]

                    print(
                        f"Trạng thái: {result.state}, "
                        f"tiến độ: "
                        f"{getattr(result, 'progress', None)}"
                    )

                    if result.state in ("done", "failed"):
                        break

                    time.sleep(5)

                if result.state != "done":
                    print(f"Xử lý thất bại: {pdf_file.name}")
                    failed_files.append(pdf_file.name)
                    continue

                # Markdown có tên giống PDF gốc
                output_file = (
                    MARKDOWN_DIR
                    / f"{pdf_file.stem}.md"
                )

                # Chỉ lưu Markdown, không lưu JSON
                result.save_markdown(
                    str(output_file),
                    with_images=False,
                )

                print(f"Đã tạo: {output_file}")
                success_count += 1

            except Exception as error:
                print(
                    f"Lỗi {pdf_file.name}: "
                    f"{type(error).__name__}: {error}"
                )
                failed_files.append(pdf_file.name)

    finally:
        client.close()

    print("\n" + "=" * 60)
    print("KẾT QUẢ")
    print(f"Thành công: {success_count}/{len(pdf_files)}")
    print(f"Thất bại: {len(failed_files)}")

    for file_name in failed_files:
        print(f"- {file_name}")


if __name__ == "__main__":
    main()