# generate_index.py
import os

def main():
    years = list(range(2019, 2027))
    
    for year in years:
        folder_path = f"docs/Meropriyatia/{year}"
        if not os.path.exists(folder_path):
            continue
            
        # Собираем список файлов contract-*.md
        contracts = []
        for file in os.listdir(folder_path):
            if file.startswith("contract-") and file.endswith(".md"):
                contracts.append(file)
        
        if not contracts:
            continue
            
        # Генерируем содержимое index.md
        content = f"""---
title: Мероприятия {year} года
---

# Мероприятия {year} года

Список контрактов за {year} год:

"""
        for contract in sorted(contracts):
            name = contract.replace(".md", "").replace("contract-", "")
            content += f"- [{name}]({contract})\n"
        
        # Сохраняем файл
        index_path = os.path.join(folder_path, "index.md")
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(content)
        
        print(f"✅ Обновлён: {index_path}")

if __name__ == "__main__":
    main()