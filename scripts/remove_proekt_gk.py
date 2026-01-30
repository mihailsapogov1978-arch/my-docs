# add_tz_html_link.py
import os
import re

def add_tz_link_to_index(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Ищем реестровый номер внутри карточки и добавляем ссылку на .html
    # Шаблон: <li><strong>Реестровый номер:</strong> 0190200000320000774</li>
    pattern = r'(<li><strong>Реестровый номер:</strong>\s*([0-9]+)</li>[\s\S]*?<p><a\s+href="https://zakupki\.gov\.ru/[^"]*">\s*Пол контракт на zakupki\.gov\.ru\s*</a></p>)'
    
    def replacer(match):
        full = match.group(1)
        reestr = match.group(2)
        tz_link = f'  <p><a href="contract-{reestr}.html">смотреть ТЗ</a></p>'
        return full + '\n' + tz_link

    new_content = re.sub(pattern, replacer, content, flags=re.IGNORECASE | re.DOTALL)
    
    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"✅ Добавлена ссылка 'смотреть ТЗ' (на .html) в: {filepath}")

def main():
    base_dir = "docs/Meropriyatia"
    for year in os.listdir(base_dir):
        year_path = os.path.join(base_dir, year)
        if not os.path.isdir(year_path) or not year.isdigit():
            continue
        index_path = os.path.join(year_path, "index.md")
        if os.path.exists(index_path):
            add_tz_link_to_index(index_path)

if __name__ == "__main__":
    main()