import re
from pathlib import Path
import os

# Настройки
INPUT_DIRS = [f"docs/Meropriyatia/{year}" for year in range(2019, 2026)]
OUTPUT_FILE = "onchet.html"

def extract_metadata(file_path: Path):
    """Извлекает метаданные из Markdown-файла контракта."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return None

    data = {
        'file': str(file_path),
        'title': '',
        'reestr_number': '',
        'year': '',
        'status': '',
        'price': '',
        'date_placement': ''
    }

    # Год из пути
    for year in range(2019, 2026):
        if f"/{year}/" in str(file_path):
            data['year'] = str(year)
            break

    # Реестровый номер — из frontmatter или имени файла
    reestr_match = re.search(r'reestr_number:\s*["\']?(\d+)', content)
    if not reestr_match:
        reestr_match = re.search(r'contract-(\d+)\.md', str(file_path))
    if reestr_match:
        data['reestr_number'] = reestr_match.group(1)

    # Статус — из frontmatter или текста
    status_match = re.search(r'status:\s*["\']?([^"\']*)', content)
    if not status_match:
        status_match = re.search(r'(Определение поставщика завершено|Заключение контракта)', content)
    if status_match:
        data['status'] = status_match.group(1).strip()

    # Цена — из таблицы или текста
    price_match = re.search(r'Цена контракта[^\d]*(\d[\d\s\.,]*\d)', content)
    if price_match:
        data['price'] = price_match.group(1).replace(' ', '').replace(',', '.') + " ₽"
    else:
        # Альтернатива: из frontmatter или спецификации
        price_alt = re.search(r'(\d[\d\s]*\d)\s*(?:рублей|₽)', content, re.IGNORECASE)
        if price_alt:
            data['price'] = price_alt.group(1).replace(' ', '') + " ₽"

    # Дата размещения
    date_match = re.search(r'Дата размещения[^\d]*(\d{2}\.\d{2}\.\d{4})', content)
    if not date_match:
        date_match = re.search(r'(\d{2}\.\d{2}\.\d{4})', content)
    if date_match:
        data['date_placement'] = date_match.group(1)

    # Название — из заголовка или frontmatter
    title_match = re.search(r'title:\s*["\']?([^"\']*)', content)
    if not title_match:
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if title_match:
        data['title'] = title_match.group(1).strip()

    return data

def generate_html(contracts):
    total = len(contracts)
    html = f'''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Сводный отчёт по техническим заданиям</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; margin: 2rem; }}
        h1 {{ color: #2c3e50; }}
        table {{ border-collapse: collapse; width: 100%; margin-top: 1rem; }}
        th, td {{ text-align: left; padding: 0.75rem; border-bottom: 1px solid #eee; }}
        th {{ background-color: #f8f9fa; font-weight: 600; }}
        tr:hover {{ background-color: #f5f5f5; }}
        .price {{ color: #27ae60; font-weight: bold; }}
        .status-ok {{ color: #27ae60; }}
        .status-pending {{ color: #f39c12; }}
    </style>
</head>
<body>
    <h1>Сводный отчёт по техническим заданиям (2019–2025)</h1>
    <p>Найдено контрактов: <strong>{total}</strong></p>
    
    <table>
        <thead>
            <tr>
                <th>Год</th>
                <th>Реестровый номер</th>
                <th>Название</th>
                <th>Статус</th>
                <th>Цена</th>
                <th>Дата</th>
                <th>Файл</th>
            </tr>
        </thead>
        <tbody>
'''

    for c in contracts:
        status_class = "status-ok" if "завершено" in c['status'].lower() else "status-pending"
        file_link = c['file'].replace('\\', '/')
        html += f'''
            <tr>
                <td>{c['year']}</td>
                <td><code>{c['reestr_number']}</code></td>
                <td>{c['title'] or '—'}</td>
                <td class="{status_class}">{c['status'] or '—'}</td>
                <td class="price">{c['price'] or '—'}</td>
                <td>{c['date_placement'] or '—'}</td>
                <td><a href="{file_link}">Открыть</a></td>
            </tr>
        '''

    html += '''
        </tbody>
    </table>
</body>
</html>
'''
    return html

def main():
    contracts = []
    
    for dir_path in INPUT_DIRS:
        dir_p = Path(dir_path)
        if not dir_p.exists():
            continue
            
        for md_file in dir_p.rglob("*.md"):
            if md_file.name == "index.md":
                continue
                
            metadata = extract_metadata(md_file)
            if metadata:
                contracts.append(metadata)
    
    # Сортировка по году и дате
    def sort_key(c):
        try:
            from datetime import datetime
            date_obj = datetime.strptime(c['date_placement'], '%d.%m.%Y')
        except:
            date_obj = None
        return (c['year'], date_obj or 0)
    
    contracts.sort(key=sort_key)
    
    # Генерация HTML
    html_content = generate_html(contracts)
    
    # Сохранение
    output_path = Path(OUTPUT_FILE)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Отчёт сохранён: {output_path.absolute()}")

if __name__ == "__main__":
    main()