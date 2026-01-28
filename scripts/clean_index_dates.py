# clean_index_dates.py
import os
import re

def clean_index_file(filepath):
    """Удаляет строки с 'Дата начала исполнения' и 'Дата окончания исполнения' из index.md"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Удаляем обе строки (регистронезависимо, с любыми пробелами)
    patterns = [
        r'<li>\s*<strong>\s*Дата\s+начала\s+исполнени(?:я|я)\s*:\s*</strong>\s*Не\s+указана\s*</li>\s*',
        r'<li>\s*<strong>\s*Дата\s+окончани(?:я|я)\s+исполнени(?:я|я)\s*:\s*</strong>\s*Не\s+указана\s*</li>\s*',
    ]
    
    for pat in patterns:
        content = re.sub(pat, '', content, flags=re.IGNORECASE | re.DOTALL)
    
    # Также убираем пустые строки после удаления
    content = re.sub(r'\n\s*\n', '\n', content)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"✅ Очищено: {filepath}")

def main():
    base_dir = "docs/Meropriyatia"
    
    for year_folder in os.listdir(base_dir):
        year_path = os.path.join(base_dir, year_folder)
        if not os.path.isdir(year_path) or not year_folder.isdigit():
            continue
        
        index_path = os.path.join(year_path, "index.md")
        if os.path.exists(index_path):
            clean_index_file(index_path)

if __name__ == "__main__":
    main()