# fix_quotes_for_search.py
import os
import re

def fix_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Заменяем « и » на пробелы (или удаляем)
    # Вариант 1: удаляем кавычки полностью — безопасно для поиска
    new_content = re.sub(r'[«»]', '', content)
    
    # Вариант 2 (альтернатива): заменяем на пробелы
    # new_content = re.sub(r'[«»]', ' ', content)
    
    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"✅ Кавычки исправлены: {filepath}")

def main():
    base_dir = "docs/Meropriyatia"
    for year in os.listdir(base_dir):
        year_path = os.path.join(base_dir, year)
        if not os.path.isdir(year_path) or not year.isdigit():
            continue
        for file in os.listdir(year_path):
            if file.endswith(".md"):
                fix_file(os.path.join(year_path, file))

if __name__ == "__main__":
    main()