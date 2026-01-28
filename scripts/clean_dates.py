# clean_dates.py
import os
import re

def clean_contract_file(filepath):
    """Удаляет строки 'Дата начала исполнения: Не указана' и аналогичные"""
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    new_lines = []
    for line in lines:
        # Удаляем строки, содержащие:
        # "Дата начала исполнения: Не указана"
        # "Дата окончания исполнения: Не указана"
        # с любым количеством пробелов и регистром
        if re.search(r'^\s*Дата\s+начала\s+исполнени(?:я|я)\s*:\s*Не\s+указана\s*$', line, re.IGNORECASE):
            continue
        if re.search(r'^\s*Дата\s+окончани(?:я|я)\s+исполнени(?:я|я)\s*:\s*Не\s+указана\s*$', line, re.IGNORECASE):
            continue
        new_lines.append(line)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    print(f"✅ Очищено: {filepath}")

def main():
    base_dir = "docs/Meropriyatia"
    
    for year_folder in os.listdir(base_dir):
        year_path = os.path.join(base_dir, year_folder)
        if not os.path.isdir(year_path) or not year_folder.isdigit():
            continue
        
        for file in os.listdir(year_path):
            if file.startswith("contract-") and file.endswith(".md"):
                full_path = os.path.join(year_path, file)
                clean_contract_file(full_path)

if __name__ == "__main__":
    main()