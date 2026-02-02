#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import pandas as pd
from pathlib import Path
from decimal import Decimal

def load_csv_contracts(csv_path: Path) -> list:
    """Загружает контракты из CSV с cp1251, разделитель ;"""
    try:
        df = pd.read_csv(csv_path, sep=';', encoding='cp1251', on_bad_lines='skip')
    except Exception:
        # Попробуем без кодировки (для совместимости)
        df = pd.read_csv(csv_path, sep=';', on_bad_lines='skip')

    contracts = []
    for _, row in df.iterrows():
        # Реестровый номер
        reg_raw = str(row.get('Реестровый номер закупки', '')).strip()
        if not reg_raw or reg_raw == 'nan':
            continue
        reg_clean = re.sub(r'[^\d]', '', reg_raw)
        if len(reg_clean) < 15:
            continue

        # Дата размещения → DD.MM.YYYY
        date_raw = str(row.get('Дата размещения', '')).strip()
        date_display = "не указана"
        if date_raw and date_raw != 'nan':
            date_match = re.search(r'(\d{2})\.(\d{2})\.(\d{4})', date_raw)
            if date_match:
                day, month, year = date_match.groups()
                date_display = f"{day}.{month}.{year}"
            else:
                date_match2 = re.search(r'(\d{4})-(\d{2})-(\d{2})', date_raw)
                if date_match2:
                    year, month, day = date_match2.groups()
                    date_display = f"{day}.{month}.{year}"

        # Цена
        price_val = None
        try:
            price_raw = str(row.get('Начальная (максимальная) цена контракта', '')).strip()
            if price_raw and price_raw != 'nan':
                price_val = Decimal(price_raw)
        except:
            pass
        if price_val is None:
            continue

        # Наименование
        name = str(row.get('Наименование закупки', '')).strip()
        if name == 'nan':
            name = "Не указано"

        contracts.append({
            "reg_number": reg_clean,
            "name": name,
            "date": date_display,
            "price": price_val,
            "year": date_display.split('.')[-1] if '.' in date_display else "2025"
        })
    return contracts

def format_currency_no_symbol(value: Decimal) -> str:
    """Форматирует цену БЕЗ символа ₽ и БЕЗ жирности: 3 229 200,00"""
    s = f"{value:.2f}"
    integer_part, frac_part = s.split('.')
    integer_part = re.sub(r'(\d)(?=(\d{3})+(?!\d))', r'\1 ', integer_part)
    return f"{integer_part},{frac_part}"

def generate_svod_markdown(contracts: list, output_path: str):
    if not contracts:
        md = ["# Сводная информация по государственным контрактам", "", "⚠ Нет данных."]
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(md))
        return

    # Группировка по годам
    by_year = {}
    for c in contracts:
        y = c["year"]
        if y not in by_year:
            by_year[y] = {"count": 0, "sum": Decimal('0'), "contracts": []}
        by_year[y]["count"] += 1
        by_year[y]["sum"] += c["price"]
        by_year[y]["contracts"].append(c)

    total_sum = sum(v["sum"] for v in by_year.values())
    total_count = sum(v["count"] for v in by_year.values())

    md = []
    md.append("# Сводная информация по государственным контрактам")
    md.append("")
    md.append("## Общая статистика")
    md.append("")
    md.append(f"- **Всего контрактов:** {total_count}")
    md.append(f"- **Общая сумма:** {format_currency_no_symbol(total_sum)}")
    md.append("")

    # Таблица по годам (компактная)
    md.append("## Сводка по годам")
    md.append("")
    md.append('<table style="width:100%; border-collapse:collapse; font-size:0.85em;">')
    md.append("<thead>")
    md.append('<tr style="background-color:#f5f7fa; font-weight:bold;">')
    md.append('<th style="width:3%; padding:6px; text-align:center;">№</th>')
    md.append('<th style="width:62%; padding:6px; text-align:left;">Наименование</th>')
    md.append('<th style="width:14%; padding:6px; text-align:center;">Дата размещения и номер контракта</th>')
    md.append('<th style="width:18%; padding:6px; text-align:right;">Цена</th>')
    md.append("</tr>")
    md.append("</thead>")
    md.append("<tbody>")
    for year in sorted(by_year.keys()):
        stats = by_year[year]
        share = (stats["sum"] / total_sum * 100) if total_sum > 0 else 0
        bg = "#e6f7ff" if year == "2025" else "#ffffff"
        md.append(
            f'<tr style="background-color:{bg}; border-bottom:1px solid #eee;">'
            f'<td style="padding:6px; font-weight:bold;">{year}</td>'
            f'<td style="padding:6px; text-align:center;">{stats["count"]}</td>'
            f'<td style="padding:6px; text-align:right;">{format_currency_no_symbol(stats["sum"])}</td>'
            f'<td style="padding:6px; text-align:right;">{share:.1f}%</td>'
            f'</tr>'
        )
    md.append("</tbody></table>")
    md.append("")

    # 🔥 ДЕТАЛИЗАЦИЯ — ТОЧНО КАК НА СКРИНЕ
    md.append("## Детализация по контрактам")
    md.append("")
    for year in sorted(by_year.keys()):
        md.append(f"### {year} год")
        md.append("")
        md.append('<div style="overflow-x:auto;">')
        md.append('<table class="table-contracts" style="width:100%; border-collapse:collapse; font-size:0.85em;">')
        md.append("<thead>")
        md.append('<tr style="background-color:#f5f7fa; font-weight:bold;">')
        md.append('<th style="width:3%; padding:6px; text-align:center;">№</th>')
        md.append('<th style="width:55%; padding:6px; text-align:left;">Наименование</th>')
        md.append('<th style="width:22%; padding:6px; text-align:center;">Дата размещения и номер контракта</th>')
        md.append('<th style="width:20%; padding:6px; text-align:right;">Цена</th>')
        md.append("</tr>")
        md.append("</thead>")
        md.append("<tbody>")
        for idx, c in enumerate(by_year[year]["contracts"], 1):
            # Последние 5 цифр реестрового номера
            last_5 = c["reg_number"][-5:] if len(c["reg_number"]) >= 5 else c["reg_number"]
            date_and_num = f'<div style="text-align:center; line-height:1.3;">{c["date"]}<br><span style="font-size:0.85em;">№ {last_5}</span></div>'
            price_str = format_currency_no_symbol(c["price"])
            md.append(
                f'<tr style="border-bottom:1px solid #eee;">'
                f'<td style="padding:6px; text-align:center; font-weight:normal;">{idx}</td>'
                f'<td style="padding:6px; word-break:break-word;">{c["name"]}</td>'
                f'<td style="padding:6px;">{date_and_num}</td>'
                f'<td style="padding:6px; text-align:right; font-weight:normal; color:#000;">{price_str}</td>'
                f'</tr>'
            )
        md.append("</tbody>")
        md.append("</table>")
        md.append("</div>")
        md.append("")

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))

    print(f"✅ Отчёт сохранён: {output_path}")
    print(f"   — Контрактов: {total_count}")
    print(f"   — Сумма: {format_currency_no_symbol(total_sum)}")

def main():
    csv_path = Path("OrderSearch(1-59)_26.01.2026(1).csv")
    if not csv_path.exists():
        print("❌ CSV-файл не найден!")
        return

    contracts = load_csv_contracts(csv_path)
    print(f"📥 Загружено контрактов: {len(contracts)}")

    generate_svod_markdown(contracts, "docs/Meropriyatia/svod_gk.md")

if __name__ == "__main__":
    main()