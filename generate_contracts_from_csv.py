# generate_contracts_from_csv.py
import csv
import os
import re
from datetime import datetime

def clean_filename(name):
    """Очищает имя файла от недопустимых символов"""
    return re.sub(r'[<>:"/\\|?*]', '_', name)

def main():
    csv_file = "OrderSearch(1-59)_25.01.2026(1).csv"
    
    if not os.path.exists(csv_file):
        print(f"❌ Файл {csv_file} не найден")
        return
    
    # ИСПРАВЛЕНО: используем cp1251 вместо utf-8-sig
    with open(csv_file, "r", encoding="cp1251") as f:
        reader = csv.DictReader(f, delimiter=";")
        rows = list(reader)
    
    print(f"✅ Найдено {len(rows)} закупок")
    
    for row in rows:
        try:
            # Извлекаем данные
            zakupka_number = row.get("Закупки по", "").strip()
            reestr_number_raw = row.get("Реестровый номер закупки", "").strip()
            name = row.get("Наименование закупки", "").strip()
            price = row.get("Начальная (максимальная) цена контракта", "").strip()
            date_placement = row.get("Дата размещения", "").strip()
            status = row.get("Этап закупки", "").strip()
            ikz = row.get("Идентификационный код закупки", "").strip()
            
            # Очищаем реестровый номер (удаляем № и кавычки)
            reestr_number = reestr_number_raw.replace("№", "").strip()
            if not reestr_number:
                continue
            
            # Извлекаем год из даты размещения
            if date_placement:
                try:
                    placement_date = datetime.strptime(date_placement, "%d.%m.%Y")
                    year = str(placement_date.year)
                except ValueError:
                    year = "архив"
            else:
                year = "архив"
            
            # Создаём папку года
            output_dir = f"docs/Meropriyatia/{year}"
            os.makedirs(output_dir, exist_ok=True)
            
            # Генерируем имя файла
            filename = f"contract-{reestr_number}.md"
            filepath = os.path.join(output_dir, filename)
            
            # Пропускаем, если файл уже существует
            if os.path.exists(filepath):
                print(f"⚠️  Пропускаем {reestr_number} (уже существует)")
                continue
            
            # Генерируем содержимое
            content = f"""---
title: "{name[:60]}..."
reestr_number: "{reestr_number}"
year: {year}
status: "{status}"
tags: [закупка, 44-ФЗ]
---

# {name}

## Основная информация

- **Реестровый номер**: {reestr_number}
- **Статус**: {status}
- **Дата размещения**: {date_placement}
- **Цена контракта**: {price} руб.
- **ИКЗ**: {ikz}

[Полная карточка на zakupki.gov.ru](https://zakupki.gov.ru/epz/order/notice/ea44/view/common-info.html?regNumber={reestr_number})
"""
            
            # Сохраняем файл в UTF-8
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            
            print(f"✅ Сохранён: {filepath}")
            
        except Exception as e:
            print(f"❌ Ошибка при обработке строки: {e}")
            continue
    
    print(f"\n🎉 Обработано {len(rows)} закупок!")

if __name__ == "__main__":
    main()