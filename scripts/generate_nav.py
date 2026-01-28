# generate_nav.py
import os
import yaml

def main():
    # Загружаем текущий mkdocs.yml
    with open("mkdocs.yml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    
    # Находим секцию "Мероприятия"
    nav = config["nav"]
    for item in nav:
        if isinstance(item, dict) and "Мероприятия" in item:
            years_list = item["Мероприятия"]
            new_years = []
            
            for year_entry in years_list:
                if isinstance(year_entry, str):
                    # Формат: "2024: Meropriyatia/2024/index.md"
                    parts = year_entry.split(": ", 1)
                    if len(parts) == 2:
                        year_name, index_path = parts
                        folder = os.path.dirname(index_path)
                        if os.path.exists(folder):
                            # Добавляем index.md
                            new_years.append({year_name: index_path})
                            # Добавляем все contract-*.md
                            for file in sorted(os.listdir(folder)):
                                if file.startswith("contract-") and file.endswith(".md"):
                                    full_path = f"{folder}/{file}"
                                    # Используем заголовок из файла или имя
                                    title = get_title_from_file(full_path) or file.replace("contract-", "").replace(".md", "")
                                    new_years.append({title: full_path})
                elif isinstance(year_entry, dict):
                    # Уже обработано
                    new_years.append(year_entry)
            
            item["Мероприятия"] = new_years
            break
    
    # Сохраняем обновлённый mkdocs.yml
    with open("mkdocs.yml", "w", encoding="utf-8") as f:
        yaml.dump(config, f, allow_unicode=True, default_flow_style=False, indent=2, sort_keys=False)
    
    print("✅ Все contract-*.md добавлены в nav")

def get_title_from_file(filepath):
    """Получает заголовок из первого заголовка файла"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("# "):
                    return line[2:].strip()
    except:
        pass
    return None

if __name__ == "__main__":
    main()