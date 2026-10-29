import os
import csv
import re
from collections import defaultdict

# ========== НАСТРОЙКИ ==========
CSV_FILE = "downloads_csv/contracts_8901038364.csv"
OUTPUT_DIR = "docs/Contracts"
OUTPUT_MD = os.path.join(OUTPUT_DIR, "svod_gk.md")

os.makedirs(OUTPUT_DIR, exist_ok=True)

TYPE_MAPPING = {
    'миграци': 'Миграция данных',
    'техническ': 'Техническая поддержка',
    'настройк': 'Настройка/Развитие системы',
    'развити': 'Настройка/Развитие системы',
    'консалтинг': 'Консалтинг',
    'предпроектн': 'Предпроектные работы',
    'обследован': 'Предпроектные работы',
}


def detect_encoding(filepath):
    for enc in ('utf-8-sig', 'utf-8', 'windows-1251', 'cp1251'):
        try:
            with open(filepath, 'r', encoding=enc) as f:
                f.read()
            return enc
        except Exception:
            continue
    return 'utf-8'


def detect_delimiter(filepath, encoding):
    with open(filepath, 'r', encoding=encoding) as f:
        first_line = f.readline()
    counts = {',': 0, ';': 0, '\t': 0}
    in_quotes = False
    for ch in first_line:
        if ch == '"':
            in_quotes = not in_quotes
        elif not in_quotes and ch in counts:
            counts[ch] += 1
    return max(counts, key=counts.get)


def extract_year(date_str):
    if not date_str:
        return None
    m = re.search(r'(\d{2})\.(\d{2})\.(\d{4})', date_str)
    if m:
        return m.group(3)
    m = re.search(r'(\d{4})-\d{2}-\d{2}', date_str)
    if m:
        return m.group(1)
    m = re.search(r'\b(20\d{2})\b', date_str)
    if m:
        return m.group(1)
    return None


def normalize_headers(fieldnames):
    result = []
    for name in fieldnames or []:
        if name is None:
            result.append('')
            continue
        clean = name.replace('\ufeff', '').strip()
        result.append(clean)
    return result


def parse_price(raw):
    if not raw:
        return 0.0
    s = raw.replace('\xa0', '').replace(' ', '').replace(',', '.')
    s = re.sub(r'[^\d.]', '', s)
    try:
        return float(s) if s else 0.0
    except ValueError:
        return 0.0


def format_money(value):
    return f"{value:,.2f}".replace(',', ' ').replace('.', ',')


def parse_contracts(csv_path):
    print(f"📂 Чтение: {csv_path}")
    encoding = detect_encoding(csv_path)
    delimiter = detect_delimiter(csv_path, encoding)
    print(f"  Кодировка: {encoding}, разделитель: {repr(delimiter)}")

    contracts = []
    with open(csv_path, 'r', encoding=encoding, newline='') as f:
        sample = f.read(4096)
        f.seek(0)
        dialect = csv.Sniffer().sniff(sample, delimiters=';,\t') if sample else None
        if dialect is not None:
            delimiter = dialect.delimiter
            
        reader = csv.reader(f, delimiter=delimiter)
        try:
            raw_headers = next(reader)
        except StopIteration:
            return []
        headers = normalize_headers(raw_headers)

        for row in reader:
            if not row or all(not c.strip() for c in row):
                continue
            data = dict(zip(headers, row))

            reg_number = (data.get('Реестровый номер закупки') or '').strip()
            reg_number = reg_number.replace('№', '').strip()
            if not reg_number:
                continue

            name = (data.get('Наименование закупки') or '').strip()
            price_float = parse_price(data.get('Начальная (максимальная) цена контракта'))
            publish_date = (data.get('Дата размещения') or '').strip()
            stage = (data.get('Этап закупки') or '').strip()

            year = extract_year(publish_date)
            if not year:
                year = extract_year(reg_number)

            link = ("https://zakupki.gov.ru/epz/order/notice/ea44/view/"
                    f"common-info.html?regNumber={reg_number}")

            work_type = 'Прочее'
            name_lower = name.lower()
            for keyword, wtype in TYPE_MAPPING.items():
                if keyword in name_lower:
                    work_type = wtype
                    break

            contracts.append({
                'reg_number': reg_number,
                'short_number': reg_number[-4:],  # Берем ровно 4 последние цифры
                'name': name,
                'price': format_money(price_float),
                'price_float': price_float,
                'publish_date': publish_date,
                'year': year,
                'stage': stage,
                'link': link,
                'work_type': work_type,
            })

    print(f"  ✅ Обработано контрактов: {len(contracts)}")
    return contracts


def load_existing_reg_numbers(md_path):
    """
    Читаем существующий md и собираем уже имеющиеся реестровые номера.
    Ищем либо полные 19-значные номера (из старых версий), 
    либо 4-значные (из новых).
    """
    if not os.path.exists(md_path):
        return set()
    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()
    # Ищем любые числа после знака № (от 4 до 19 цифр)
    return set(re.findall(r'№\s*(\d{4,19})', text))


def merge_with_existing(new_contracts, existing_numbers):
    """
    Оставляем только те, которых нет в md. 
    Проверяем по полному и по короткому номеру.
    """
    added = []
    for c in new_contracts:
        if c['reg_number'] in existing_numbers or c['short_number'] in existing_numbers:
            continue
        added.append(c)
    return new_contracts, added


def render_md(contracts):
    years = defaultdict(list)
    for c in contracts:
        if c['year'] and c['year'].isdigit() and 2019 <= int(c['year']) <= 2030:
            years[c['year']].append(c)
        else:
            print(f"  ⚠️ Пропущен контракт с неопределённым годом: {c['reg_number']}")

    display_years = sorted(years.keys(), reverse=True)

    md = "# Сводная информация по государственным контрактам\n\n"

    for year in display_years:
        md += f"## {year} год\n\n"
        md += '<div style="overflow-x:auto;">\n'
        md += '<table class="table-contracts" style="width:100%; border-collapse:collapse; font-size:0.85em;">\n'
        md += '<thead>\n<tr style="background-color:#f5f7fa; font-weight:bold;">\n'
        md += '  <th style="width:3%; padding:6px; text-align:center;">№</th>\n'
        md += '  <th style="width:55%; padding:6px; text-align:left;">Наименование</th>\n'
        md += '  <th style="width:21%; padding:6px; text-align:center;">Дата размещения<br>и номер контракта</th>\n'
        md += '  <th style="width:21%; padding:6px; text-align:right;">Цена</th>\n'
        md += '</tr>\n</thead>\n<tbody>\n'

        year_contracts = sorted(
            years[year],
            key=lambda c: (c['publish_date'][-4:], c['publish_date'][3:5], c['publish_date'][:2]),
            reverse=True,
        )

        for i, c in enumerate(year_contracts, 1):
            md += '<tr style="border-bottom:1px solid #eee;">\n'
            md += f'  <td style="padding:6px; text-align:center;">{i}</td>\n'
            md += f'  <td style="padding:6px;">{c["name"]}</td>\n'
            # Выводим только 4 последние цифры в коротком формате
            md += (f'  <td style="padding:6px; text-align:center;">{c["publish_date"]}'
                   f'<br>№ {c["short_number"]}<br>'
                   f'<a href="{c["link"]}" target="_blank">ГК на zakupki.gov.ru</a></td>\n')
            md += f'  <td style="padding:6px; text-align:right; white-space:nowrap;">{c["price"]}</td>\n'
            md += '</tr>\n'

        md += '</tbody>\n</table>\n</div>\n\n'

    # --- Статистика по годам ---
    md += "## Общая статистика\n\n"
    md += '<div style="overflow-x:auto;">\n'
    md += '<table class="table-stats" style="width:100%; border-collapse:collapse; font-size:0.85em;">\n'
    md += '<thead>\n<tr style="background-color:#f5f7fa; font-weight:bold;">\n'
    md += '<th style="padding:6px; text-align:left;">Год</th>\n'
    md += '<th style="padding:6px; text-align:center;">Контрактов</th>\n'
    md += '<th style="padding:6px; text-align:right;">Сумма</th>\n'
    md += '</tr>\n</thead>\n<tbody>\n'

    total_count, total_sum = 0, 0.0
    for year in display_years:
        items = years[year]
        cnt = len(items)
        s = sum(c['price_float'] for c in items)
        total_count += cnt
        total_sum += s
        md += '<tr style="border-bottom:1px solid #eee;">\n'
        md += f'  <td style="padding:6px; font-weight:bold;">{year}</td>\n'
        md += f'  <td style="padding:6px; text-align:center;">{cnt}</td>\n'
        md += f'  <td style="padding:6px; text-align:right;">{format_money(s)}</td>\n'
        md += '</tr>\n'

    md += ('<tr style="border-bottom:1px solid #eee; background-color:#f8f9fa; font-weight:bold;">\n'
           f'  <td style="padding:6px;">Итого</td>\n'
           f'  <td style="padding:6px; text-align:center;">{total_count}</td>\n'
           f'  <td style="padding:6px; text-align:right;">{format_money(total_sum)}</td>\n'
           '</tr>\n</tbody>\n</table>\n</div>\n\n')

    # --- По типам работ ---
    md += "## Распределение по типам работ\n\n"
    md += '<div style="overflow-x:auto;">\n'
    md += '<table class="table-types" style="width:100%; border-collapse:collapse; font-size:0.85em;">\n'
    md += '<thead>\n<tr style="background-color:#f5f7fa; font-weight:bold;">\n'
    md += '<th style="padding:6px; text-align:left;">Тип работ</th>\n'
    md += '<th style="padding:6px; text-align:center;">Контрактов</th>\n'
    md += '<th style="padding:6px; text-align:right;">Сумма</th>\n'
    md += '<th style="padding:6px; text-align:right;">% от общей суммы</th>\n'
    md += '</tr>\n</thead>\n<tbody>\n'

    types = defaultdict(list)
    for c in contracts:
        if c['year'] and c['year'].isdigit() and 2019 <= int(c['year']) <= 2030:
            types[c['work_type']].append(c)

    for wtype, items in sorted(
        types.items(), key=lambda x: sum(c['price_float'] for c in x[1]), reverse=True
    ):
        s = sum(c['price_float'] for c in items)
        pct = (s / total_sum * 100) if total_sum else 0
        md += '<tr style="border-bottom:1px solid #eee;">\n'
        md += f'  <td style="padding:6px; font-weight:bold;">{wtype}</td>\n'
        md += f'  <td style="padding:6px; text-align:center;">{len(items)}</td>\n'
        md += f'  <td style="padding:6px; text-align:right;">{format_money(s)}</td>\n'
        md += f'  <td style="padding:6px; text-align:right; color:#27ae60;">{pct:.1f}%</td>\n'
        md += '</tr>\n'

    md += '</tbody>\n</table>\n</div>\n'
    return md, total_count, total_sum


def main():
    print("=" * 60)
    print("ГЕНЕРАЦИЯ / ОБНОВЛЕНИЕ СВОДНОЙ ТАБЛИЦЫ КОНТРАКТОВ")
    print("=" * 60)

    if not os.path.exists(CSV_FILE):
        print(f"❌ Файл {CSV_FILE} не найден!")
        return

    contracts = parse_contracts(CSV_FILE)
    if not contracts:
        print("❌ Контракты не найдены!")
        return

    existing = load_existing_reg_numbers(OUTPUT_MD)
    _, added = merge_with_existing(contracts, existing)
    print(f"  🆕 Новых контрактов (которых нет в md): {len(added)}")

    md_text, total_count, total_sum = render_md(contracts)

    with open(OUTPUT_MD, 'w', encoding='utf-8') as f:
        f.write(md_text)

    print(f"\n  ✅ Сохранено: {OUTPUT_MD}")
    print(f"  📊 Всего контрактов: {total_count}")
    print(f"  💰 Общая сумма: {format_money(total_sum)}")
    print("=" * 60)


if __name__ == "__main__":
    main()