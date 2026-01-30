import re
import sys
from pathlib import Path

def clean_google_docs_md_inplace(file_path: str):
    """
    Очищает Markdown-файл от мусора Google Docs:
    - Сохраняет всё, включая строки ![][imageX]
    - Удаляет всё, начиная с <data:image/... или <image/... до конца файла
    - Перезаписывает исходный файл
    """
    input_file = Path(file_path)
    if not input_file.is_file():
        raise FileNotFoundError(f"Файл не найден: {file_path}")

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Удаляем всё, начиная с первого вхождения <data:image или <image (Google Docs иногда генерирует <image...)
    # Используем нежадный поиск до первого вхождения
    cleaned = re.split(r'<(?:data:)?image/[a-z]+;base64,', content, maxsplit=1)[0]

    # Перезаписываем исходный файл
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(cleaned)

    print(f"✅ Файл очищен: {input_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python clean_gdocs_md.py <файл.md>")
        print("Пример: python clean_gdocs_md.py document.md")
        sys.exit(1)

    file_to_clean = sys.argv[1]
    clean_google_docs_md_inplace(file_to_clean)