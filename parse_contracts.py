import os
import csv
import re
from collections import defaultdict

# ========== НАСТРОЙКИ ==========
CSV_FILE = "downloads_csv/contracts_8901038364.csv"  # исходный CSV
OUTPUT_DIR = "docs/Contracts"  # директория для выходных файлов
OUTPUT_MD = os.path.join(OUTPUT_DIR, "svod_gk.md")  # результат

# Создаём директорию если не существует
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Сопоставление типа работ по ключевым словам в названии
TYPE_MAPPING = {
    'миграция': 'Миграция данных',
    'миграции': 'Миграция данных',
    'технической поддержке': 'Техническая поддержка',
    'техническая поддержка': 'Техническая поддержка',
    'настройке': 'Настройка/Развитие системы',
    'настройка': 'Настройка/Развитие системы',
    'развитию': 'Настройка/Развитие системы',
    'развитие': 'Настройка/Развитие системы',
    'консалтинговых': 'Консалтинг',
    'консалтинг': 'Консалтинг',
    'предпроектного': 'Предпроектные работы',
    'обследования': 'Предпроектные работы',
}

def detect_encoding(filepath):
    """Определение кодировки файла"""
    encodings = ['utf-8-sig', 'utf-8', 'windows-1251', 'cp1251']
    for enc in encodings:
        try:
            with open(filepath, 'r', encoding=enc) as f:
                f.read()
            return enc
        except:
            continue
    return 'utf-8'

def extract_year(date_str):
    """Извлечение года из даты в формате DD.MM.YYYY или YYYY-MM-DD"""
    if not date_str:
        return 'Неизвестно'
    
    # Пробуем формат DD.MM.YYYY
    match = re.search(r'(\d{2})\.(\d{2})\.(\d{4})', date_str)
    if match:
        return match.group(3)  # год
    
    # Пробуем формат YYYY-MM-DD
    match = re.search(r'(\d{4})-\d{2}-\d{2}', date_str)
    if match:
        return match.group(1)
    
    # Пробуем найти 4 цифры подряд (год)
    match = re.search(r'\b(\d{4})\b', date_str)
    if match:
        year = match.group(1)
        if 2019 <= int(year) <= 2030:
            return year
    
    return 'Неизвестно'

def parse_contracts(csv_path):
    """Парсинг CSV и извлечение данных"""
    print(f"📂 Чтение: {csv_path}")
    
    encoding = detect_encoding(csv_path)
    print(f"  Кодировка: {encoding}")
    
    contracts = []
    
    try:
        with open(csv_path, 'r', encoding=encoding) as f:
            reader = csv.DictReader(f, delimiter=';')
            
            for row in reader:
                # Полный номер контракта
                reg_number = row.get('Реестровый номер закупки', '').strip()
                reg_number = reg_number.replace('№', '').strip()
                
                # Короткий номер (последние 5 цифр)
                short_number = reg_number[-5:] if reg_number else ''
                
                # Идентификационный код закупки (ИКЗ) - уникальный идентификатор
                ikz = row.get('Идентификационный код закупки', '').strip()
                
                # Название
                name = row.get('Наименование закупки', '').strip()
                
                # Формируем уникальное название: исходное название + короткий номер
                # Это позволит различать контракты с одинаковыми названиями
                unique_name = f"{name} (№ {short_number})"
                
                # Цена
                price_raw = row.get('Начальная (максимальная) цена контракта', '0')
                price_clean = price_raw.replace(',', '').replace(' ', '')
                try:
                    price_float = float(price_clean) if price_clean else 0
                except:
                    price_float = 0
                price_formatted = f"{price_float:,.2f}".replace(',', ' ').replace('.', ',')
                
                # Дата размещения
                publish_date = row.get('Дата размещения', '').strip()
                
                # Извлекаем год из даты
                year = extract_year(publish_date)
                
                # Статус
                stage = row.get('Этап закупки', '').strip()
                
                # Ссылка на карточку
                link = f"https://zakupki.gov.ru/epz/order/notice/ea44/view/common-info.html?regNumber={reg_number}"
                
                # Определяем тип работ
                work_type = 'Прочее'
                name_lower = name.lower()
                for keyword, wtype in TYPE_MAPPING.items():
                    if keyword in name_lower:
                        work_type = wtype
                        break
                
                contracts.append({
                    'reg_number': reg_number,
                    'short_number': short_number,
                    'ikz': ikz,
                    'name': name,
                    'unique_name': unique_name,
                    'price': price_formatted,
                    'price_float': price_float,
                    'publish_date': publish_date,
                    'year': year,
                    'stage': stage,
                    'link': link,
                    'work_type': work_type,
                })
        
        print(f"  ✅ Обработано контрактов: {len(contracts)}")
        return contracts
        
    except Exception as e:
        print(f"  ❌ Ошибка: {e}")
        return []

def generate_md(contracts):
    """Генерация MD-файла с корректными годами (2019-2026)"""
    print(f"\n📝 Генерация: {OUTPUT_MD}")
    
    # Группировка по годам (только 2019-2026)
    years = defaultdict(list)
    for c in contracts:
        year = c['year']
        # Фильтруем только реальные года (2019-2026)
        if year.isdigit() and 2019 <= int(year) <= 2026:
            years[year].append(c)
        else:
            # Если год не определился, пытаемся извлечь из даты ещё раз
            year2 = extract_year(c['publish_date'])
            if year2.isdigit() and 2019 <= int(year2) <= 2026:
                years[year2].append(c)
            else:
                print(f"  ⚠️ Пропущен контракт с неверной датой: {c['publish_date']}")
    
    # Сортируем года от 2019 до 2026 (по возрастанию)
    sorted_years = sorted(years.keys())
    
    # Но для отображения используем убывание (2026 вверху)
    display_years = sorted_years[::-1]
    
    # Начинаем сбор MD
    md = "# Сводная информация по государственным контрактам\n\n"
    
    # ===== КОНТРАКТЫ ПО ГОДАМ =====
    for year in display_years:
        year_contracts = years[year]
        md += f"## {year} год\n\n"
        md += """<div style="overflow-x:auto;">\n"""
        md += """<table class="table-contracts" style="width:100%; border-collapse:collapse; font-size:0.85em;">\n"""
        md += """<thead>\n"""
        md += """<tr style="background-color:#f5f7fa; font-weight:bold;">\n"""
        md += """  <th style="width:3%; padding:6px; text-align:center;">№</th>\n"""
        md += """  <th style="width:55%; padding:6px; text-align:left;">Наименование</th>\n"""
        md += """  <th style="width:21%; padding:6px; text-align:center;">Дата размещения<br>и номер контракта</th>\n"""
        md += """  <th style="width:21%; padding:6px; text-align:right;">Цена</th>\n"""
        md += """</tr>\n"""
        md += """</thead>\n"""
        md += """<tbody>\n"""
        
        for i, c in enumerate(year_contracts, 1):
            # Добавляем ИКЗ в title для возможности полной идентификации
            ikz_short = c.get('ikz', '')[:20] + '...' if len(c.get('ikz', '')) > 20 else c.get('ikz', '')
            title_attr = f' title="ИКЗ: {c.get("ikz", "")}"' if c.get('ikz') else ''
            
            md += f"""<tr style="border-bottom:1px solid #eee;">\n"""
            md += f"""  <td style="padding:6px; text-align:center;">{i}</td>\n"""
            md += f"""  <td style="padding:6px;"{title_attr}>{c['unique_name']}</td>\n"""
            md += f"""  <td style="padding:6px; text-align:center;">{c['publish_date']}<br>№ {c['short_number']}<br><a href="{c['link']}" target="_blank">ГК на zakupki.gov.ru</a></td>\n"""
            md += f"""  <td style="padding:6px; text-align:right; white-space:nowrap;">{c['price']}</td>\n"""
            md += f"""</tr>\n"""
        
        md += """</tbody>\n"""
        md += """</table>\n"""
        md += """</div>\n\n"""
    
    # ===== СТАТИСТИКА ПО ГОДАМ =====
    md += "## Общая статистика\n\n"
    md += """<div style="overflow-x:auto;">\n"""
    md += """<table class="table-stats" style="width:100%; border-collapse:collapse; font-size:0.85em;">\n"""
    md += """<thead>\n"""
    md += """<tr style="background-color:#f5f7fa; font-weight:bold;">\n"""
    md += """<th style="padding:6px; text-align:left;">Год</th>\n"""
    md += """<th style="padding:6px; text-align:center;">Контрактов</th>\n"""
    md += """<th style="padding:6px; text-align:right;">Сумма</th>\n"""
    md += """</tr>\n"""
    md += """</thead>\n"""
    md += """<tbody>\n"""
    
    total_count = 0
    total_sum = 0
    
    for year in display_years:
        year_contracts = years[year]
        count = len(year_contracts)
        total = sum(c['price_float'] for c in year_contracts)
        total_count += count
        total_sum += total
        
        total_str = f"{total:,.2f}".replace(',', ' ').replace('.', ',')
        
        md += f"""<tr style="border-bottom:1px solid #eee;">\n"""
        md += f"""  <td style="padding:6px; font-weight:bold;">{year}</td>\n"""
        md += f"""  <td style="padding:6px; text-align:center;">{count}</td>\n"""
        md += f"""  <td style="padding:6px; text-align:right;">{total_str}</td>\n"""
        md += f"""</tr>\n"""
    
    total_str = f"{total_sum:,.2f}".replace(',', ' ').replace('.', ',')
    md += f"""<tr style="border-bottom:1px solid #eee; background-color:#f8f9fa; font-weight:bold;">\n"""
    md += f"""  <td style="padding:6px;">Итого</td>\n"""
    md += f"""  <td style="padding:6px; text-align:center;">{total_count}</td>\n"""
    md += f"""  <td style="padding:6px; text-align:right;">{total_str}</td>\n"""
    md += f"""</tr>\n"""
    
    md += """</tbody>\n"""
    md += """</table>\n"""
    md += """</div>\n\n"""
    
    # ===== РАСПРЕДЕЛЕНИЕ ПО ТИПАМ РАБОТ =====
    md += "## Распределение по типам работ\n\n"
    md += """<div style="overflow-x:auto;">\n"""
    md += """<table class="table-types" style="width:100%; border-collapse:collapse; font-size:0.85em;">\n"""
    md += """<thead>\n"""
    md += """<tr style="background-color:#f5f7fa; font-weight:bold;">\n"""
    md += """<th style="padding:6px; text-align:left;">Тип работ</th>\n"""
    md += """<th style="padding:6px; text-align:center;">Контрактов</th>\n"""
    md += """<th style="padding:6px; text-align:right;">Сумма</th>\n"""
    md += """<th style="padding:6px; text-align:right;">% от общей суммы</th>\n"""
    md += """</tr>\n"""
    md += """</thead>\n"""
    md += """<tbody>\n"""
    
    # Группировка по типам
    types = defaultdict(list)
    for c in contracts:
        # Проверяем, что год корректен
        if c['year'].isdigit() and 2019 <= int(c['year']) <= 2026:
            types[c['work_type']].append(c)
    
    # Сортируем по убыванию суммы
    sorted_types = sorted(types.items(), key=lambda x: sum(c['price_float'] for c in x[1]), reverse=True)
    
    for wtype, items in sorted_types:
        count = len(items)
        total = sum(c['price_float'] for c in items)
        percent = (total / total_sum * 100) if total_sum > 0 else 0
        
        total_str = f"{total:,.2f}".replace(',', ' ').replace('.', ',')
        percent_str = f"{percent:.1f}%"
        
        md += f"""<tr style="border-bottom:1px solid #eee;">\n"""
        md += f"""  <td style="padding:6px; font-weight:bold;">{wtype}</td>\n"""
        md += f"""  <td style="padding:6px; text-align:center;">{count}</td>\n"""
        md += f"""  <td style="padding:6px; text-align:right;">{total_str}</td>\n"""
        md += f"""  <td style="padding:6px; text-align:right; color:#27ae60;">{percent_str}</td>\n"""
        md += f"""</tr>\n"""
    
    md += """</tbody>\n"""
    md += """</table>\n"""
    md += """</div>\n"""
    
    # Сохраняем
    with open(OUTPUT_MD, 'w', encoding='utf-8') as f:
        f.write(md)
    
    print(f"  ✅ Сохранено: {OUTPUT_MD}")
    print(f"  📊 Всего контрактов: {total_count}")
    print(f"  💰 Общая сумма: {total_str}")

def main():
    print("=" * 60)
    print("ГЕНЕРАЦИЯ СВОДНОЙ ТАБЛИЦЫ КОНТРАКТОВ")
    print("=" * 60)
    
    if not os.path.exists(CSV_FILE):
        print(f"❌ Файл {CSV_FILE} не найден!")
        print(f"   Убедитесь, что CSV-файл лежит в папке: {os.getcwd()}")
        return
    
    contracts = parse_contracts(CSV_FILE)
    if not contracts:
        print("❌ Контракты не найдены!")
        return
    
    generate_md(contracts)
    
    print("\n" + "=" * 60)
    print("✅ ГОТОВО! Файл svod_gk.md обновлён.")
    print("   Скопируйте его в папку docs/ вашего MkDocs-проекта.")
    print("=" * 60)

if __name__ == "__main__":
    main()