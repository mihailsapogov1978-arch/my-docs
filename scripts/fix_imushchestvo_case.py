# fix_gis_imushchestvo.py
import os
import re

def fix_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Ищем шаблон: ГИС («|")?имущество → делаем "Имущество"
    # Поддерживаем:
    # - ГИС «имущество
    # - ГИС "имущество
    # - ГИС имущество
    # - гис имущество (на всякий случай)
    pattern = r'(ГИС\s*[«"]?)\s*имущество'
    replacement = r'\1Имущество'
    
    new_content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
    
    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"✅ Исправлено: {filepath}")

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