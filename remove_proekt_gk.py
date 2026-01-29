# generate_index.py
import os
import csv
from datetime import datetime

def format_price(price_str):
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
                    continue
                if year not in contracts_by_year:
                    contracts_by_year[year] = []
                contracts_by_year[year].append(row)
            except ValueError:
                continue

    for year in sorted(contracts_by_year.keys(), reverse=True):
        folder = f"docs/Meropriyatia/{year}"
        os.makedirs(folder, exist_ok=True)

        content = f"""---
title: Мероприятия {year} года
---

# Мероприятия {year} года

Список контрактов за {year} год:

<div class="interactive-contracts">
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
            reestr_number_raw = row.get("Реестровый номер закупки", "").strip()
            reestr_number = reestr_number_raw.replace("№", "").strip()
            name = row.get("Наименование закупки", "").strip()
            date_placement = row.get("Дата размещения", "").strip()
            price_raw = row.get("Начальная (максимальная) цена контракта", "").strip()
            price = format_price(price_raw)
            status = row.get("Этап закупки", "")

            card_id = f"contract-{i}"

            content += f"""<tr class="contract-row" data-target="{card_id}">
<td>{i}</td>
<td>{name}</td>
<td>{date_placement}</td>
<td style="text-align: right;">{price}</td>
</tr>
<tr class="contract-details" id="{card_id}" style="display: none;">
<td colspan="4">
<div class="contract-card">
<div class="contract-info">
<h4>Основная информация</h4>
<ul>
<li><strong>Реестровый номер:</strong> {reestr_number}</li>
<li><strong>Статус:</strong> {status}</li>
<li><strong>Дата заключения контракта:</strong> {date_placement}</li>
<li><strong>Номер контракта:</strong> {reestr_number.split('0')[-1] if reestr_number else 'Не указан'}</li>
</ul>
</div>
<div class="contract-links">
<p><a href="https://zakupki.gov.ru/epz/order/notice/ea44/view/common-info.html?regNumber={reestr_number}" target="_blank">Полный контракт на zakupki.gov.ru</a></p>
<p><a href="contract-{reestr_number}/">Смотреть ТЗ</a></p>
<h4>План мероприятий</h4>
<p>План мероприятий будет добавлен позже.</p>
</div>
</div>
</td>
</tr>
"""

        content += """</tbody>
</table>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const rows = document.querySelectorAll('.contract-row');
    let currentOpen = null;

    rows.forEach(row => {
        row.addEventListener('click', function() {
            const targetId = this.getAttribute('data-target');
            const detailsRow = document.getElementById(targetId);

            if (currentOpen && currentOpen !== detailsRow) {
                currentOpen.style.display = 'none';
            }

            if (detailsRow.style.display === 'none' || detailsRow.style.display === '') {
                detailsRow.style.display = 'table-row';
                currentOpen = detailsRow;
            } else {
                detailsRow.style.display = 'none';
                currentOpen = null;
            }
        });
    });
});
</script>
"""

        with open(os.path.join(folder, "index.md"), "w", encoding="utf-8") as f:
            f.write(content)

        print(f"✅ Обновлён index.md для {year}")

if __name__ == "__main__":
    main()