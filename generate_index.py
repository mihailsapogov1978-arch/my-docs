# generate_index.py
import os
import csv
from datetime import datetime

def format_price(price_str):
    """Форматирует цену в вид: 1 000 000.00"""
    try:
        price = float(price_str)
        return f"{price:,.2f}".replace(",", " ")
    except (ValueError, TypeError):
        return price_str

def main():
    csv_file = "OrderSearch(1-59)_25.01.2026(1).csv"
    if not os.path.exists(csv_file):
        print("❌ CSV-файл не найден")
        return

    # Чтение всех строк
    contracts_by_year = {}
    with open(csv_file, "r", encoding="cp1251") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            date_placement = row.get("Дата размещения", "").strip()
            if not date_placement:
                continue
            try:
                dt = datetime.strptime(date_placement, "%d.%m.%Y")
                year = str(dt.year)
                if year == "2019":
                    continue  # Пропускаем 2019
                if year not in contracts_by_year:
                    contracts_by_year[year] = []
                contracts_by_year[year].append(row)
            except ValueError:
                continue

    # Обработка каждого года
    for year in sorted(contracts_by_year.keys(), reverse=True):
        folder = f"docs/Meropriyatia/{year}"
        os.makedirs(folder, exist_ok=True)

        content = f"""---
title: Мероприятия {year} года
---

# Мероприятия {year} года

Список контрактов за {year} год:

<table class="table-contracts">
<thead>
<tr>
<th>№</th>
<th>Наименование</th>
<th>Дата размещения</th>
<th>Цена</th>
</tr>
</thead>
<tbody>
"""

        for i, row in enumerate(contracts_by_year[year], 1):
            name = row.get("Наименование закупки", "").strip()
            date_placement = row.get("Дата размещения", "").strip()
            price_raw = row.get("Начальная (максимальная) цена контракта", "").strip()
            price = format_price(price_raw)

            content += f"""<tr>
<td>{i}</td>
<td>{name}</td>
<td>{date_placement}</td>
<td style="text-align: right;">{price}</td>
</tr>
"""

        content += """</tbody>
</table>
"""

        with open(os.path.join(folder, "index.md"), "w", encoding="utf-8") as f:
            f.write(content)

        print(f"✅ Обновлён index.md для {year}")

if __name__ == "__main__":
    main()