import pandas as pd
import os
from collections import Counter
import re

# --- КОНФИГУРАЦИЯ ---
# Пути к файлам. Можно указать несколько.
FILE_PATHS = [
    'docs/calls/part1.xlsx',
    'docs/calls/part2.xlsx'
]
OUTPUT_MD_FILE = 'report.md'

# Индексы строк и столбцов в исходном файле (на основе part2.xlsx)
# Внимание: эти индексы могут потребовать корректировки для part1.xlsx,
# если его структура отличается. Скрипт попытается определить их автоматически.
HEADER_ROW_INDEX = 2  # Строка с заголовками (0-based)
DATA_START_ROW_INDEX = 4 # Первая строка с данными (0-based)

# Индексы столбцов (0-based) на основе анализа part2.xlsx
# A:0, B:1, C:2, D:3, E:4, F:5, G:6, H:7, I:8, J:9
COL_ORG = 0       # Столбец A (для строк-разделителей)
COL_ID = 1        # Столбец B (Номер)
COL_DATE = 2      # Столбец C (Дата и время регистрации)
COL_STATUS = 4    # Столбец E (Статус обращения)
COL_THEME = 5     # Столбец F (Тема)
COL_DESC = 6      # Столбец G (Описание)
COL_EXECUTOR = 7  # Столбец H (Исполнитель)
COL_SOLUTION = 8  # Столбец I (Решение)
COL_SERVICE = 9   # Столбец J (Услуга)


def clean_text(text):
    """Очистка текста от лишних пробелов и переносов строк."""
    if not isinstance(text, str):
        return ""
    # Убираем html-теги, которые могут встречаться
    text = re.sub(r'<[^>]+>', '', text)
    # Убираем множественные пробелы и переносы
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def parse_excel_files(file_paths):
    """Читает и объединяет данные из нескольких Excel-файлов."""
    all_data = []
    
    for file_path in file_paths:
        if not os.path.exists(file_path):
            print(f"Предупреждение: Файл не найден - {file_path}")
            continue
            
        print(f"Обработка файла: {file_path}")
        
        try:
            # Читаем файл без заголовков, чтобы получить все строки
            df_raw = pd.read_excel(file_path, header=None)
            
            # Попытка найти строку с заголовками (ищем "Номер", "Дата")
            header_row = None
            for i, row in df_raw.iterrows():
                if 'Номер' in row.values and 'Дата и время регистрации' in row.values:
                    header_row = i
                    break
            
            if header_row is None:
                print(f"  Не удалось найти строку с заголовками в {file_path}. Пропускаем.")
                continue

            # Определяем строку начала данных
            data_start_row = header_row + 2 # Обычно после заголовка и строки с нумерацией

            # Устанавливаем заголовки
            headers = df_raw.iloc[header_row].tolist()
            # Заменяем NaN в заголовках на пустые строки
            headers = [str(h).strip() if pd.notna(h) else f'Unnamed_{i}' for i, h in enumerate(headers)]
            
            # Создаем новый DataFrame с правильными заголовками
            df = df_raw.iloc[data_start_row:].copy()
            df.columns = headers
            
            # Удаляем полностью пустые строки
            df.dropna(how='all', inplace=True)
            
            # Добавляем столбец для названия файла (для отслеживания)
            df['source_file'] = os.path.basename(file_path)
            
            all_data.append(df)
            
        except Exception as e:
            print(f"  Ошибка при чтении файла {file_path}: {e}")
            continue

    if not all_data:
        return pd.DataFrame()

    # Объединяем все данные
    combined_df = pd.concat(all_data, ignore_index=True)
    
    # Добавляем столбец "Учреждение", заполняя его на основе строк-разделителей
    combined_df['Учреждение'] = None
    current_org = None
    
    # Проходим по строкам, чтобы заполнить "Учреждение"
    # Это делается до фильтрации, так как строки-разделители не имеют "Номер"
    for index, row in combined_df.iterrows():
        # Проверяем, является ли строка разделителем (нет номера, но есть текст в первом столбце)
        # Предполагаем, что в разделителе есть текст в COL_ORG, но пусто в COL_ID
        org_cell = row.iloc[COL_ORG]
        id_cell = row.iloc[COL_ID]
        
        # Если ID пустой, а Org не пустой и это не "Номер" (заголовок) - это разделитель
        if pd.isna(id_cell) and pd.notna(org_cell) and str(org_cell).strip() not in ['', 'Номер']:
            current_org = clean_text(org_cell)
            # Присваиваем название учреждения этой строке, чтобы потом отфильтровать
            combined_df.loc[index, 'Учреждение'] = current_org
        elif current_org is not None:
            combined_df.loc[index, 'Учреждение'] = current_org

    # Фильтруем, оставляя только строки, где есть номер заявки
    # Номер заявки должен быть числом или строкой, содержащей цифры
    combined_df = combined_df[pd.notna(combined_df.iloc[:, COL_ID])].copy()
    
    # Убираем строку с нумерацией столбцов (1,2,3...)
    combined_df = combined_df[pd.to_numeric(combined_df.iloc[:, COL_ID], errors='coerce').notna()].copy()

    return combined_df

def generate_report(df):
    """Генерирует Markdown-отчет на основе DataFrame."""
    if df.empty:
        return "# Отчет по заявкам\n\nНет данных для отображения."

    # --- Очистка данных ---
    # Приводим столбцы к единому виду
    df['Номер'] = df.iloc[:, COL_ID].astype(str)
    df['Дата'] = pd.to_datetime(df.iloc[:, COL_DATE], errors='coerce', dayfirst=True)
    df['Статус'] = df.iloc[:, COL_STATUS].apply(clean_text)
    df['Тема'] = df.iloc[:, COL_THEME].apply(clean_text)
    df['Описание'] = df.iloc[:, COL_DESC].apply(clean_text)
    df['Исполнитель'] = df.iloc[:, COL_EXECUTOR].apply(clean_text)
    df['Услуга'] = df.iloc[:, COL_SERVICE].apply(clean_text)
    df['Учреждение'] = df['Учреждение'].apply(clean_text)

    # Убираем строки, где "Услуга" пустая или 'nan'
    df = df[df['Услуга'] != 'nan']

    # Добавляем год и месяц
    df['Год'] = df['Дата'].dt.year
    df['Месяц'] = df['Дата'].dt.strftime('%Y-%m')

    # Фильтрация по текущему году (2026)
    current_year_df = df[df['Год'] == 2026].copy()

    if current_year_df.empty:
        return "# Отчет по заявкам\n\nНет данных за 2026 год."

    # --- Генерация отчета ---
    report_lines = []
    report_lines.append("# Агрегированный отчет по заявкам за 2026 год")
    report_lines.append(f"\n**Всего заявок за 2026 год:** {len(current_year_df)}")
    report_lines.append(f"**Всего уникальных учреждений:** {current_year_df['Учреждение'].nunique()}")
    report_lines.append(f"**Всего уникальных исполнителей:** {current_year_df['Исполнитель'].nunique()}")
    report_lines.append("\n---\n")

    # 1. Топ-5 проблемных направлений (по услуге)
    report_lines.append("## Топ-5 проблемных направлений (Услуга)")
    top_services = current_year_df['Услуга'].value_counts().head(5)
    report_lines.append("| Услуга | Количество заявок |")
    report_lines.append("|---|---|")
    for service, count in top_services.items():
        report_lines.append(f"| {service} | {count} |")
    report_lines.append("\n")

    # 2. Топ-5 учреждений
    report_lines.append("## Топ-5 учреждений по количеству заявок")
    top_orgs = current_year_df['Учреждение'].value_counts().head(5)
    report_lines.append("| Учреждение | Количество заявок |")
    report_lines.append("|---|---|")
    for org, count in top_orgs.items():
        report_lines.append(f"| {org} | {count} |")
    report_lines.append("\n")

    # 3. Топ-5 исполнителей
    report_lines.append("## Топ-5 исполнителей по количеству обработанных заявок")
    top_executors = current_year_df['Исполнитель'].value_counts().head(5)
    report_lines.append("| Исполнитель | Количество заявок |")
    report_lines.append("|---|---|")
    for executor, count in top_executors.items():
        report_lines.append(f"| {executor} | {count} |")
    report_lines.append("\n")

    # 4. Распределение по статусам
    report_lines.append("## Распределение заявок по статусам")
    status_counts = current_year_df['Статус'].value_counts()
    report_lines.append("| Статус | Количество заявок | Доля |")
    report_lines.append("|---|---|---|")
    total = status_counts.sum()
    for status, count in status_counts.items():
        percentage = (count / total) * 100
        report_lines.append(f"| {status} | {count} | {percentage:.2f}% |")
    report_lines.append("\n")

    # 5. Топ-5 по ключевым словам в теме
    report_lines.append("## Топ-5 по ключевым словам в теме заявки")
    # Собираем все слова из тем, исключая стоп-слова
    stop_words = set(['и', 'в', 'на', 'с', 'по', 'не', 'к', 'у', 'о', 'для', 'из', 'а', 'или', 'но', 'что', 'это', 'как', 'то', 'все', 'так', 'же', 'бы', 'за', 'от', 'до', 'при', 'об', 'под', 'над', 'про', 'без', 'через', 'между', 'перед', 'около', 'после', 'во', 'со', 'ко', 'изо'])
    all_words = []
    for theme in current_year_df['Тема']:
        words = re.findall(r'\b[а-яА-ЯёЁa-zA-Z]{3,}\b', theme.lower())
        all_words.extend([w for w in words if w not in stop_words])
    
    word_counts = Counter(all_words)
    top_words = word_counts.most_common(5)
    report_lines.append("| Ключевое слово | Количество упоминаний |")
    report_lines.append("|---|---|")
    for word, count in top_words:
        report_lines.append(f"| {word} | {count} |")
    report_lines.append("\n")

    # 6. Динамика по месяцам (2026)
    report_lines.append("## Динамика заявок по месяцам (2026)")
    monthly_counts = current_year_df.groupby('Месяц').size().sort_index()
    report_lines.append("| Месяц | Количество заявок |")
    report_lines.append("|---|---|")
    for month, count in monthly_counts.items():
        report_lines.append(f"| {month} | {count} |")
    report_lines.append("\n")

    # 7. Среднее время решения (если есть данные)
    report_lines.append("## Среднее время решения заявки")
    # Попытка извлечь дату из поля 'Решение'. Это сложно, так как формат неоднородный.
    # Будем искать паттерн даты в начале строки решения.
    def extract_solution_date(solution_text):
        if not isinstance(solution_text, str):
            return pd.NaT
        # Ищем дату в формате ДД.ММ.ГГГГ ЧЧ:ММ:СС
        match = re.search(r'(\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2})', solution_text)
        if match:
            try:
                return pd.to_datetime(match.group(1), format='%d.%m.%Y %H:%M:%S')
            except:
                return pd.NaT
        return pd.NaT

    current_year_df['Дата_решения'] = current_year_df['Решение'].apply(extract_solution_date)
    
    # Рассчитываем разницу только для строк, где обе даты есть
    valid_dates = current_year_df.dropna(subset=['Дата', 'Дата_решения']).copy()
    if not valid_dates.empty:
        valid_dates['Время_решения'] = (valid_dates['Дата_решения'] - valid_dates['Дата']).dt.total_seconds() / 3600 # в часах
        # Фильтруем отрицательные значения (ошибки в данных)
        valid_dates = valid_dates[valid_dates['Время_решения'] >= 0]
        
        if not valid_dates.empty:
            avg_hours = valid_dates['Время_решения'].mean()
            median_hours = valid_dates['Время_решения'].median()
            report_lines.append(f"- **Среднее время решения:** {avg_hours:.2f} часов")
            report_lines.append(f"- **Медианное время решения:** {median_hours:.2f} часов")
            report_lines.append(f"- **Заявок с рассчитанным временем:** {len(valid_dates)}")
        else:
            report_lines.append("Недостаточно данных для расчета среднего времени (все значения отрицательные или отсутствуют).")
    else:
        report_lines.append("Недостаточно данных для расчета среднего времени решения.")
    
    report_lines.append("\n---\n")
    report_lines.append("*Отчет сгенерирован автоматически.*")

    return "\n".join(report_lines)

def main():
    """Основная функция."""
    print("Начало генерации отчета...")
    
    # 1. Парсинг данных
    df = parse_excel_files(FILE_PATHS)
    
    if df.empty:
        print("Не удалось загрузить данные. Проверьте пути к файлам и их структуру.")
        return

    print(f"Загружено {len(df)} строк с данными.")
    
    # 2. Генерация отчета
    report_content = generate_report(df)
    
    # 3. Сохранение отчета
    with open(OUTPUT_MD_FILE, 'w', encoding='utf-8') as f:
        f.write(report_content)
        
    print(f"Отчет успешно сохранен в файл: {OUTPUT_MD_FILE}")

if __name__ == "__main__":
    main()