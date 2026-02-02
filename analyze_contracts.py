#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import pandas as pd
from pathlib import Path
from decimal import Decimal

def format_currency_no_symbol(value: Decimal) -> str:
    """Форматирует как '1 234 567,00' — без ₽, без жирности"""
    s = f"{value:.2f}"
    integer_part, frac_part = s.split('.')
    parts = []
    while integer_part:
        parts.append(integer_part[-3:])
        integer_part = integer_part[:-3]
    integer_part = ' '.join(reversed(parts))
    return f"{integer_part},{frac_part}"

def extract_year_from_date(date_str: str) -> str:
    match = re.search(r'(20\d{2})', date_str)
    return match.group(1) if match else "2025"

def load_contracts_from_csv(csv_path: Path):
    try:
        df = pd.read_csv(csv_path, sep=';', encoding='cp1251', on_bad_lines='skip')
    except Exception:
        df = pd.read_csv(csv_path, sep=';', on_bad_lines='skip')

    contracts_by_year = {}
    for _, row in df.iterrows():
        reg_raw = str(row.get('Реестровый номер закупки', '')).strip()
        if not reg_raw or reg_raw == 'nan':
            continue
        reg_clean = ''.join(filter(str.isdigit, reg_raw))
        if len(reg_clean) < 15:
            continue

        date_raw = str(row.get('Дата размещения', '')).strip()
        if not date_raw:
            continue

        price_val = None
        try:
            price_raw = str(row.get('Начальная (максимальная) цена контракта', '')).strip()
            if price_raw and price_raw != 'nan':
                price_val = Decimal(price_raw)
        except:
            pass
        if price_val is None:
            continue

        name = str(row.get('Наименование закупки', '')).strip()
        if name == 'nan':
            name = "Не указано"

        last5 = reg_clean[-5:] if len(reg_clean) >= 5 else reg_clean
        year = extract_year_from_date(date_raw)

        contract = {
            "name": name,
            "date": date_raw,
            "last5": last5,
            "price": price_val
        }

        if year not in contracts_by_year:
            contracts_by_year[year] = []
        contracts_by_year[year].append(contract)

    # Сортировка по дате внутри года
    for year, lst in contracts_by_year.items():
        def parse_date(d):
            d = re.sub(r'[^\d]', '', d)
            return d if len(d) >= 8 else "99999999"
        lst.sort(key=lambda x: parse_date(x["date"]))

    return contracts_by_year

def generate_md(contracts_by_year, output_path: Path):
    years = sorted(contracts_by_year.keys())
    all_contracts = [c for year in years for c in contracts_by_year[year]]
    total_count = len(all_contracts)
    total_sum = sum(c["price"] for c in all_contracts)

    md = []
    md.append("# Сводная информация по государственным контрактам")
    md.append("")
    md.append("## Общая статистика")
    md.append("")
    md.append(f"- **Всего контрактов:** {total_count}")
    md.append(f"- **Общая сумма:** {format_currency_no_symbol(total_sum)}")
    md.append("")

    # Таблицы по годам — только заголовки ## Год, без списка сверху
    for year in years:
        md.append(f"## {year} год")
        md.append("")
        md.append('<div style="overflow-x:auto;">')
        md.append('<table class="table-contracts" style="width:100%; border-collapse:collapse; font-size:0.85em;">')
        md.append("<thead>")
        md.append('<tr style="background-color:#f5f7fa; font-weight:bold;">')
        md.append('<th style="width:3%; padding:6px; text-align:center;">№</th>')
        md.append('<th style="width:55%; padding:6px; text-align:left;">Наименование</th>')
        md.append('<th style="width:21%; padding:6px; text-align:center;">Дата размещения<br>и номер контракта</th>')
        md.append('<th style="width:21%; padding:6px; text-align:right;">Цена</th>')
        md.append("</tr>")
        md.append("</thead>")
        md.append("<tbody>")

        for idx, c in enumerate(contracts_by_year[year], 1):
            date_and_num = f'{c["date"]}<br><span style="font-size:0.85em;">№ {c["last5"]}</span>'
            price_str = format_currency_no_symbol(c["price"])
            md.append(
                f'<tr style="border-bottom:1px solid #eee;">'
                f'<td style="padding:6px; text-align:center;">{idx}</td>'
                f'<td style="padding:6px; word-break:break-word;">{c["name"]}</td>'
                f'<td style="padding:6px; text-align:center;">{date_and_num}</td>'
                f'<td style="padding:6px; text-align:right; white-space:nowrap;">{price_str}</td>'
                f'</tr>'
            )

        md.append("</tbody>")
        md.append("</table>")
        md.append("</div>")
        md.append("")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))

    print(f"✅ Отчёт сохранён: {output_path}")
    print(f"   — Контрактов: {total_count}")
    print(f"   — Сумма: {format_currency_no_symbol(total_sum)}")

def main():
    csv_path = Path("OrderSearch(1-59)_26.01.2026(1).csv")
    if not csv_path.exists():
        print("❌ CSV не найден")
        return

    contracts_by_year = load_contracts_from_csv(csv_path)
    generate_md(contracts_by_year, Path("docs/Meropriyatia/svod_gk.md"))

if __name__ == "__main__":
    main()