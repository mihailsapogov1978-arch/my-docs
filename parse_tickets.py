import pandas as pd
import re
from datetime import datetime, time
import os
from pathlib import Path
from typing import Optional

# --- Конфигурация ---
INPUT_FOLDER = 'otchet'
KEYWORDS_MUNICIPAL = [
    'муниципальное', 'муниципальные', 'муниципального',
    'мку', 'му', 'администрация', 'городского', 'мбу', 'мбоу',
    'город', 'поселение', 'сельского', 'район', 'сельское',
    'поселка', 'города', 'района', 'городской', 'сельский',
    'село', 'села', 'поселок'
]
TIME_START = time(8, 30)
TIME_END = time(11, 0)

# Результаты по месяцам: total_all - все заявки, total_morning - заявки утром
results_by_month = {i: {
    'total_all': 0,           # Все заявки от муниципальных учреждений
    'total_morning': 0,        # Заявки утром 8:30-11:00
    'resolved_counts': {1: 0, 2: 0, 3: 0}  # Решено за 1-3, 4-6, 7-10 дней (только утренние)
} for i in range(1, 13)}

def is_municipal_org(org_name: str) -> bool:
    if not isinstance(org_name, str):
        return False
    org_name_lower = org_name.lower()
    for keyword in KEYWORDS_MUNICIPAL:
        if keyword in org_name_lower:
            return True
    return False

def extract_resolution_date(solution_text: str) -> Optional[datetime]:
    """Извлекает дату решения из поля 'Решение' (колонка 8)."""
    if not isinstance(solution_text, str) or solution_text == 'nan' or solution_text == 'None':
        return None
    
    pattern = r'(\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2})'
    match = re.search(pattern, solution_text)
    
    if match:
        date_str = match.group(1)
        try:
            return datetime.strptime(date_str, "%d.%m.%Y %H:%M:%S")
        except ValueError:
            pass
    
    return None

def parse_russian_date(date_str: str) -> Optional[datetime]:
    if not isinstance(date_str, str) or date_str == 'nan' or date_str == 'None':
        return None
    
    date_str = date_str.strip()
    
    for fmt in ("%d.%m.%Y %H:%M", "%d.%m.%Y %H:%M:%S"):
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return None

def find_data_start(df: pd.DataFrame) -> int:
    """Находит строку, где начинаются данные."""
    for i, row in df.iterrows():
        row_str = ' '.join([str(v).lower() for v in row if pd.notna(v)])
        if 'дата' in row_str and 'время' in row_str and 'статус' in row_str:
            return i + 1
    return -1

def is_organization_header(cell_value) -> bool:
    """Проверяет, является ли ячейка заголовком организации."""
    if not isinstance(cell_value, str) or pd.isna(cell_value):
        return False
    cell = cell_value.strip()
    
    if re.match(r'^\d+$', cell):
        return False
    
    if len(cell) < 5:
        return False
    
    org_indicators = ['департамент', 'управление', 'служба', 'комитет',
                      'учреждение', 'администрация', 'центр', 'институт',
                      'дирекция', 'фонд', 'агентство', 'муниципальное',
                      'город', 'район', 'село', 'поселение']
    
    cell_lower = cell.lower()
    for indicator in org_indicators:
        if indicator in cell_lower:
            return True
    
    return False

def process_file(filepath: Path):
    print(f"Обработка файла: {filepath.name}")
    
    try:
        df = pd.read_excel(filepath, header=None, dtype=str)
    except Exception as e:
        print(f"  Ошибка чтения: {e}")
        return

    data_start = find_data_start(df)
    if data_start == -1:
        print(f"  Не найдены заголовки в файле {filepath.name}")
        return

    current_org = None
    org_is_municipal = False
    month_num = int(filepath.stem.split('_')[0])
    
    for idx in range(data_start, len(df)):
        row = df.iloc[idx]
        
        # Проверяем заголовок организации (колонка 0)
        org_cell = str(row.iloc[0]) if len(row) > 0 and pd.notna(row.iloc[0]) else ''
        
        if is_organization_header(org_cell):
            current_org = org_cell.strip()
            org_is_municipal = is_municipal_org(current_org)
            continue

        # Обрабатываем заявку
        if current_org and org_is_municipal:
            reg_date_str = str(row.iloc[2]) if len(row) > 2 and pd.notna(row.iloc[2]) else ''
            status = str(row.iloc[4]) if len(row) > 4 and pd.notna(row.iloc[4]) else ''
            solution = str(row.iloc[8]) if len(row) > 8 and pd.notna(row.iloc[8]) else ''

            if not reg_date_str or reg_date_str in ['nan', 'None']:
                continue

            reg_date = parse_russian_date(reg_date_str)
            if not reg_date:
                continue

            # Учитываем ВСЕ заявки от муниципальных учреждений
            results_by_month[month_num]['total_all'] += 1

            # Проверяем время регистрации для утренних заявок
            if TIME_START <= reg_date.time() <= TIME_END:
                results_by_month[month_num]['total_morning'] += 1

                # Анализируем решение только для утренних заявок
                if status in ['Закрыто', 'Решено'] and solution and solution not in ['nan', 'None']:
                    res_date = extract_resolution_date(solution)
                    
                    if res_date:
                        delta_days = (res_date.date() - reg_date.date()).days
                        if delta_days == 0:
                            delta_days = 1

                        if 1 <= delta_days <= 3:
                            results_by_month[month_num]['resolved_counts'][1] += 1
                        elif 4 <= delta_days <= 6:
                            results_by_month[month_num]['resolved_counts'][2] += 1
                        elif 7 <= delta_days <= 10:
                            results_by_month[month_num]['resolved_counts'][3] += 1

# --- Основной цикл ---
input_path = Path(INPUT_FOLDER)
if not input_path.exists():
    print(f"Ошибка: Папка '{INPUT_FOLDER}' не найдена.")
    print(f"Текущая директория: {os.getcwd()}")
else:
    files = sorted(input_path.glob('[0-9][0-9]_25.xlsx'))
    if not files:
        print(f"В папке '{INPUT_FOLDER}' нет файлов формата '01_25.xlsx'...")
    else:
        for month_file in files:
            process_file(month_file)

# --- Вывод результатов ---
print("\n" + "="*80)
print("СВОДНАЯ ИНФОРМАЦИЯ ПО МУНИЦИПАЛЬНЫМ УЧРЕЖДЕНИЯМ")
print("="*80)

total_all_municipal = 0
total_morning_municipal = 0
total_resolved = {1: 0, 2: 0, 3: 0}

for month_num in sorted(results_by_month.keys()):
    month_data = results_by_month[month_num]
    total_all_municipal += month_data['total_all']
    total_morning_municipal += month_data['total_morning']
    total_resolved[1] += month_data['resolved_counts'][1]
    total_resolved[2] += month_data['resolved_counts'][2]
    total_resolved[3] += month_data['resolved_counts'][3]

    if month_data['total_all'] > 0:
        print(f"\nМесяц {month_num:02d}.2025:")
        print(f"  Всего заявок от муниципальных учреждений: {month_data['total_all']}")
        print(f"  Из них с 8:30 до 11:00: {month_data['total_morning']}")
        if month_data['total_morning'] > 0:
            print(f"  Решено (утренние):")
            print(f"    - 1-3 дня:  {month_data['resolved_counts'][1]}")
            print(f"    - 4-6 дней: {month_data['resolved_counts'][2]}")
            print(f"    - 7-10 дней:{month_data['resolved_counts'][3]}")
    else:
        print(f"\nМесяц {month_num:02d}.2025: заявок не найдено")

print("\n" + "-"*80)
print("ИТОГО ЗА 2025 ГОД:")
print(f"  Всего заявок от муниципальных учреждений: {total_all_municipal}")
print(f"  Из них зарегистрировано с 8:30 до 11:00: {total_morning_municipal}")
print(f"  Решено (утренние):")
print(f"    - 1-3 дня:  {total_resolved[1]}")
print(f"    - 4-6 дней: {total_resolved[2]}")
print(f"    - 7-10 дней:{total_resolved[3]}")
print("="*80)