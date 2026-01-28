# generate_nav_entries.py
import os

def main():
    nav_lines = []
    
    base_dir = "docs/Meropriyatia"
    for year in sorted(os.listdir(base_dir)):
        year_path = os.path.join(base_dir, year)
        if not os.path.isdir(year_path) or not year.isdigit():
            continue
        
        # Добавляем год
        nav_lines.append(f"    - {year}:")
        nav_lines.append(f"      - {year}: Meropriyatia/{year}/index.md")
        
        # Добавляем все contract-*.md как отдельные пункты (скрытые, но индексируемые)
        for file in sorted(os.listdir(year_path)):
            if file.startswith("contract-") and file.endswith(".md"):
                # Используем короткое имя без расширения как заголовок
                title = file.replace("contract-", "").replace(".md", "")
                nav_lines.append(f"      - {title}: Meropriyatia/{year}/{file}")

    # Выводим в файл
    with open("mkdocs.nav.entries.yml", "w", encoding="utf-8") as f:
        f.write("\n".join(nav_lines))
    
    print("✅ Секция nav для контрактов сохранена в mkdocs.nav.entries.yml")

if __name__ == "__main__":
    main()