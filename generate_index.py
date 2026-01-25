# generate_index.py
import os
import csv
import re
from datetime import datetime

def clean_filename(name):
    """Очищает имя файла от недопустимых символов"""
    return re.sub(r'[<>:"/\\|?*]', '_', name)

def format_price(price_str):
    """Форматирует цену в финансовый вид: 1 000 000.00"""
    try:
        price = float(price_str)
        # Форматируем с пробелами для тысяч и двумя знаками после запятой
        return f"{price:,.2f}".replace(",", " ")
    except (ValueError, TypeError):
        return price_str

def main():
    years = list(range(2020, 2027))  # 2020–2026 (без 2019)
    
    for year in years:
        folder_path = f"docs/Meropriyatia/{year}"
        if not os.path.exists(folder_path):
            continue
            
        # Собираем список контрактов из CSV
        contracts = []
        with open("OrderSearch(1-59)_25.01.2026(1).csv", "r", encoding="cp1251") as f:
            reader = csv.DictReader(f, delimiter=";")
            for row in reader:
                date_placement = row.get("Дата размещения", "").strip()
                if date_placement:
                    try:
                        placement_date = datetime.strptime(date_placement, "%d.%m.%Y")
                        contract_year = str(placement_date.year)
                        if contract_year == str(year):
                            contracts.append(row)
                    except ValueError:
                        continue
        
        if not contracts:
            continue
            
        # Генерируем содержимое index.md
        content = f"""---
title: Мероприятия {year} года
---

# Мероприятия {year} года

Список контрактов за {year} год:

<table style="width:100%; border-collapse:collapse; border:1px solid #ddd;">
  <thead>
    <tr>
      <th style="padding:8px; text-align:left; background:#f9f9f9; width:5%;">№</th>
      <th style="padding:8px; text-align:left; background:#f9f9f9; width:60%;">Наименование</th>
      <th style="padding:8px; text-align:left; background:#f9f9f9; width:15%;">Дата размещения</th>
      <th style="padding:8px; text-align:right; background:#f9f9f9; width:20%;">Цена</th>
    </tr>
  </thead>
  <tbody>
"""

        for i, row in enumerate(contracts, 1):
            # Извлекаем данные
            name = row.get("Наименование закупки", "").strip()
            price = row.get("Начальная (максимальная) цена контракта", "").strip()
            date_placement = row.get("Дата размещения", "").strip()
            
            # Форматируем наименование — убираем лишние переносы
            # Оставляем естественные разрывы (по пробелам), но не ломаем слова
            if len(name) > 80:
                words = name.split()
                lines = []
                current_line = ""
                for word in words:
                    if len(current_line) + len(word) + 1 <= 80:
                        current_line += (" " + word) if current_line else word
                    else:
                        lines.append(current_line)
                        current_line = word
                if current_line:
                    lines.append(current_line)
                formatted_name = "<br>".join(lines)
            else:
                formatted_name = name
            
            # Форматируем цену
            formatted_price = format_price(price)
            
            # Добавляем строку в таблицу
            content += f"""    <tr>
      <td style="padding:8px; border:1px solid #ddd; min-width: 40px; max-width: 60px; text-align: center;">{i}</td>
      <td style="padding:8px; border:1px solid #ddd; width:60%; word-wrap: break-word; white-space: pre-line;">{formatted_name}</td>
      <td style="padding:8px; border:1px solid #ddd; width:15%;">{date_placement}</td>
      <td style="padding:8px; border:1px solid #ddd; text-align:right; width:20%;">{formatted_price}</td>
    </tr>
"""

        content += """  </tbody>
</table>
"""

        # Сохраняем файл
        index_path = os.path.join(folder_path, "index.md")
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(content)
        
        print(f"✅ Обновлён: {index_path}")

if __name__ == "__main__":
    main()