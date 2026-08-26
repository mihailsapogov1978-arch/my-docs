import pandas as pd
import numpy as np
from datetime import datetime
import os
import re
from openpyxl import load_workbook

def categorize_issue(topic, description):
    """
    Категоризирует заявку по проблемным направлениям на основе темы и описания
    """
    text = str(topic).lower() + " " + str(description).lower()
    
    # 1. Технические проблемы
    tech_keywords = [
        'запуск', 'обновл', 'права доступа', 'доступ', 'парол', 'вход', 'авторизац',
        'завис', 'тормоз', 'ошибка', 'не открывает', 'не заходит', 'эп', 'эцп',
        'подпис', 'сертификат', 'технич', 'сбой', 'работает', 'не работает',
        'версия', 'установк', 'инсталл', 'клиент', 'веб', 'браузер', 'интернет'
    ]
    
    # 2. Бухгалтерский учет и налогообложение
    accounting_keywords = [
        'бухгалтер', 'учет', 'операц', 'проводк', 'счет', 'дебет', 'кредит',
        'зарплат', 'заработн', 'оплат', 'выплат', 'начисл', 'удержан', 'преми',
        'налог', 'ндфл', 'страхов', 'взнос', 'фсс', 'пфр', 'период', 'закрыт',
        'отчетн', 'баланс', 'прибыл', 'убыток', 'амортиз', 'основн', 'касс',
        'банк', 'платеж', 'поручен', 'аванс'
    ]
    
    # 3. Взаимодействие с внешними системами
    external_keywords = [
        'ркс', 'еис', 'гис имущество', 'банк', 'платеж', 'поручен', 'выписк',
        'казначей', 'фин', 'бюджет', 'госзакуп', 'закупк', 'тендер', 'конкурс',
        'электрон', 'эд', 'документооборот', 'архив', 'хранен', 'офд', 'оператор'
    ]
    
    # 4. Формирование регламентированной отчетности
    reporting_keywords = [
        'отчетност', 'фнс', 'сфр', 'росстат', 'астрал', 'контур', 'такском',
        'сзв', 'рсв', '4-фсс', '2-ндфл', '6-ндфл', 'бухгалтерск', 'финансов',
        'статистич', 'декларац', 'налогов'
    ]
    
    # 5. Кадровый учет
    hr_keywords = [
        'кадр', 'сотрудник', 'работник', 'персонал', 'гис тк', 'сзв-тд',
        'труд', 'больничн', 'отпуск', 'отгул', 'командиров', 'стаж', 'тк',
        'трудовой', 'договор', 'контракт', 'прием', 'увольнен', 'перевод',
        'гис ку', 'гис еску', 'единый', 'реестр'
    ]
    
    # 6. Личный кабинет подотчетного лица
    personal_keywords = [
        'личный кабинет', 'лк', 'подотчетн', 'авансов', 'отчет', 'командировоч',
        'подотчетное лицо', 'физ лицо', 'сотруднический'
    ]
    
    # 7. Дополнительный функционал и сервисы
    additional_keywords = [
        'аналитик', 'планирован', 'бюджетирован', 'консолидац', 'мониторинг',
        'контрол', 'апи', 'интеграц', 'api', 'веб-сервис', 'сервис', 'модуль',
        'дополнительн', 'расширен', 'новый функционал'
    ]
    
    # 8. Справочники и классификаторы
    directory_keywords = [
        'справочник', 'классификатор', 'инн', 'кпп', 'огрн', 'задвоен',
        'дубликат', 'повтор', 'аналитик', 'иерархи', 'структур', 'подразделен',
        'организац', 'контрагент', 'поставщик', 'покупатель', 'сотрудничеств',
        'номенклатур', 'материал', 'ос', 'основные средства', 'мног'
    ]
    
    # Проверяем категории
    categories = {
        'Технические проблемы': any(keyword in text for keyword in tech_keywords),
        'Бухгалтерский учет': any(keyword in text for keyword in accounting_keywords),
        'Внешние системы': any(keyword in text for keyword in external_keywords),
        'Регламентированная отчетность': any(keyword in text for keyword in reporting_keywords),
        'Кадровый учет': any(keyword in text for keyword in hr_keywords),
        'Личный кабинет': any(keyword in text for keyword in personal_keywords),
        'Дополнительный функционал': any(keyword in text for keyword in additional_keywords),
        'Справочники': any(keyword in text for keyword in directory_keywords)
    }
    
    # Возвращаем первую подходящую категорию
    for category, matches in categories.items():
        if matches:
            return category
    
    return 'Другое'

def parse_excel_to_md(excel_path, md_path):
    """
    Парсит Excel файл с заявками и ПЕРЕЗАПИСЫВАЕТ отчет в markdown файл
    """
    
    try:
        # Загружаем Excel файл
        wb = load_workbook(excel_path, data_only=True)
        ws = wb.active
        
        print(f"📊 Загружаем файл: {excel_path}")
        print(f"   Всего строк в файле: {ws.max_row}")
        
        # Ищем строку с заголовками таблицы
        header_row = None
        for i in range(1, min(10, ws.max_row + 1)):
            cell_value = ws.cell(row=i, column=1).value
            if cell_value in ['Номер', 1, '1']:
                header_row = i
                print(f"✅ Найдены заголовки на строке {i}")
                break
        
        if header_row:
            # Загружаем данные начиная с найденной строки заголовков
            df = pd.read_excel(excel_path, header=header_row-1)
        else:
            # По умолчанию с 4-й строки (как в примере)
            df = pd.read_excel(excel_path, header=3)
            print("⚠️ Заголовки не найдены, используем строку 4")
        
        print(f"✅ Данные загружены. Строк: {len(df)}, Колонок: {len(df.columns)}")
        
    except Exception as e:
        print(f"❌ Ошибка при чтении файла: {e}")
        return None
    
    # Очищаем названия колонок
    df.columns = [str(col).strip() for col in df.columns]
    
    # Определяем колонки (поиск по известным названиям из вашего файла)
    column_mapping = {}
    
    # Список возможных названий для каждой колонки
    column_patterns = {
        'Номер': ['номер', '№', '1'],
        'Дата': ['дата', 'время', 'регистрац', '2'],
        'Инициатор': ['инициатор', 'заявки', '3'],
        'Статус': ['статус', 'обращен', '4'],
        'Тема': ['тема', '5'],
        'Описание': ['описание', '6'],
        'Исполнитель': ['исполнитель', '7'],
        'Решение': ['решение', '8'],
        'Услуга': ['услуга', '9']
    }
    
    print(f"\n🔍 Определяем колонки:")
    for col_name, patterns in column_patterns.items():
        for pattern in patterns:
            for df_col in df.columns:
                if pattern in str(df_col).lower():
                    column_mapping[col_name] = df_col
                    print(f"   • {col_name}: '{df_col}'")
                    break
            if col_name in column_mapping:
                break
    
    # Создаем метку времени для отчета
    report_time = datetime.now().strftime("%d.%m.%Y %H:%M")
    
    # 1. Подсчитываем общее количество заявок
    total_requests = len(df)
    print(f"\n📊 Всего заявок: {total_requests}")
    
    # 2. Распределение по статусам (только для внутренних расчетов)
    status_counts = pd.Series(dtype='object')
    if 'Статус' in column_mapping:
        status_col = column_mapping['Статус']
        status_series = df[status_col].dropna()
        if len(status_series) > 0:
            status_series = status_series.astype(str).str.strip()
            status_counts = status_series.value_counts()
    
    # 3. Собираем организации и их статистику
    org_stats = {}  # Словарь для хранения статистики по организациям
    
    # Ключевые слова для классификации
    gov_keywords = ['ГОСУДАРСТВЕНН', 'ГКУ', 'ГУ', 'ГБУ', 'ГАУ', 'ГОСУДАРСТВЕННОЕ', 'ГОСУДАРСТВЕННЫЙ']
    mun_keywords = ['МУНИЦИПАЛЬН', 'МКУ', 'МУ', 'МАУ', 'МБУ', 'МУНИЦИПАЛЬНОЕ', 'МУНИЦИПАЛЬНЫЙ']
    
    # Проходим по всем строкам и собираем статистику
    current_org = None
    current_org_name = None
    
    for idx, row in df.iterrows():
        org_value = row.iloc[0] if len(df.columns) > 0 else None
        
        # Определяем организацию
        if pd.notna(org_value) and isinstance(org_value, str):
            org_str = str(org_value).strip()
            if org_str and len(org_str) > 5:
                current_org_name = org_str
                current_org = org_str
        
        # Если есть текущая организация, считаем заявку
        if current_org:
            # Инициализируем статистику для организации, если еще нет
            if current_org not in org_stats:
                org_stats[current_org] = {
                    'total': 0,
                    'resolved': 0,
                    'in_work': 0
                }
            
            # Определяем статус заявки
            status = str(row[status_col]).strip().lower() if 'Статус' in column_mapping and pd.notna(row.get(status_col)) else ''
            
            # Обновляем статистику
            org_stats[current_org]['total'] += 1
            
            # Проверяем статус для полей "Решено" и "В работе"
            if 'закрыт' in status or 'решен' in status:
                org_stats[current_org]['resolved'] += 1
            elif any(word in status for word in ['назначен', 'в работе', 'зарегистрирован']):
                org_stats[current_org]['in_work'] += 1
    
    print(f"✅ Найдено организаций: {len(org_stats)}")
    
    # 4. Группируем организации по новым правилам
    gov_orgs = []  # Государственные учреждения (без ЦБ)
    mun_orgs = []  # Муниципальные учреждения + все остальные из "прочих"
    iogv_orgs = []  # ИОГВ ЯНАО (19 департаментов + ЦБ)
    
    gov_total = 0
    gov_resolved = 0
    gov_in_work = 0
    
    mun_total = 0
    mun_resolved = 0
    mun_in_work = 0
    
    iogv_total = 0
    iogv_resolved = 0
    iogv_in_work = 0
    
    # Список департаментов для ИОГВ ЯНАО (19 организаций)
    iogv_keywords = [
        'ДЕПАРТАМЕНТ ОБРАЗОВАНИЯ ЯМАЛО-НЕНЕЦКОГО',
        'ДЕПАРТАМЕНТ КУЛЬТУРЫ ЯМАЛО-НЕНЕЦКОГО',
        'ДЕПАРТАМЕНТ ПО ДЕЛАМ КОРЕННЫХ',
        'ДЕПАРТАМЕНТ ИНФОРМАЦИОННЫХ ТЕХНОЛОГИЙ',
        'ДЕПАРТАМЕНТ МОЛОДЁЖНОЙ ПОЛИТИКИ',
        'ДЕПАРТАМЕНТ ЭКОНОМИКИ ЯМАЛО-НЕНЕЦКОГО',
        'ДЕПАРТАМЕНТ ПО ФИЗИЧЕСКОЙ КУЛЬТУРЕ',
        'ДЕПАРТАМЕНТ ГРАЖДАНСКОЙ ЗАЩИТЫ',
        'СЛУЖБА ЗАПИСИ АКТОВ ГРАЖДАНСКОГО СОСТОЯНИЯ',
        'ДЕПАРТАМЕНТ ВНУТРЕННЕЙ ПОЛИТИКИ',
        'ДЕПАРТАМЕНТ ПРИРОДНЫХ РЕСУРСОВ',
        'ДЕПАРТАМЕНТ ВНЕШНИХ СВЯЗЕЙ',
        'ДЕПАРТАМЕНТ ТРАНСПОРТА И ДОРОЖНОГО ХОЗЯЙСТВА',
        'ДЕПАРТАМЕНТ ЗДРАВООХРАНЕНИЯ ЯМАЛО-НЕНЕЦКОГО',
        'СЛУЖБА ВЕТЕРИНАРИИ ЯМАЛО-НЕНЕЦКОГО',
        'ДЕПАРТАМЕНТ СТРОИТЕЛЬСТВА И ЖИЛИЩНОЙ ПОЛИТИКИ',
        'ДЕПАРТАМЕНТ АГРОПРОМЫШЛЕННОГО КОМПЛЕКСА',
        'ДЕПАРТАМЕНТ РЕГИОНАЛЬНОЙ БЕЗОПАСНОСТИ',
        'УПРАВЛЕНИЕ ДЕЛАМИ ПРАВИТЕЛЬСТВА ЯМАЛО-НЕНЕЦКОГО'
    ]
    
    # ЦБ - Централизованная бухгалтерия
    cb_keyword = 'ЦЕНТРАЛИЗОВАННАЯ БУХГАЛТЕРИЯ ОРГАНОВ ГОСУДАРСТВЕННОЙ ВЛАСТИ'
    
    for org_name, stats in org_stats.items():
        org_upper = org_name.upper()
        
        # Проверяем, является ли организация ЦБ
        is_cb = cb_keyword in org_upper
        
        # Проверяем, является ли организация одним из департаментов ИОГВ
        is_iogv_dept = any(keyword in org_upper for keyword in iogv_keywords)
        
        # Определяем тип учреждения по новым правилам:
        # 1. Если это ЦБ или департамент ИОГВ -> ИОГВ ЯНАО
        # 2. Иначе если государственное -> Государственные учреждения
        # 3. Иначе -> Муниципальные учреждения
        
        if is_cb or is_iogv_dept:
            iogv_orgs.append((org_name, stats['total']))
            iogv_total += stats['total']
            iogv_resolved += stats['resolved']
            iogv_in_work += stats['in_work']
        elif any(keyword in org_upper for keyword in gov_keywords):
            # Это государственное учреждение (но не ЦБ и не департамент ИОГВ)
            gov_orgs.append((org_name, stats['total']))
            gov_total += stats['total']
            gov_resolved += stats['resolved']
            gov_in_work += stats['in_work']
        else:
            # Все остальное -> Муниципальные учреждения
            mun_orgs.append((org_name, stats['total']))
            mun_total += stats['total']
            mun_resolved += stats['resolved']
            mun_in_work += stats['in_work']
    
    # Сортируем списки организаций по количеству заявок (по убыванию)
    gov_orgs.sort(key=lambda x: x[1], reverse=True)
    mun_orgs.sort(key=lambda x: x[1], reverse=True)
    iogv_orgs.sort(key=lambda x: x[1], reverse=True)
    
    print(f"📊 Типы учреждений (новая классификация):")
    print(f"   • Государственные учреждения: {gov_total} заявок ({len(gov_orgs)} организаций)")
    print(f"   • Муниципальные учреждения: {mun_total} заявок ({len(mun_orgs)} организаций)")
    print(f"   • ИОГВ ЯНАО: {iogv_total} заявок ({len(iogv_orgs)} организаций)")
    
    # 5. Анализ проблемных направлений
    issue_categories = {}
    
    if 'Тема' in column_mapping and 'Описание' in column_mapping:
        theme_col = column_mapping['Тема']
        desc_col = column_mapping['Описание']
        
        print(f"\n🔍 Анализируем проблемные направления...")
        
        # Берем выборку для анализа (первые 200 заявок или все, если меньше)
        sample_size = min(200, len(df))
        
        for idx in range(sample_size):
            row = df.iloc[idx]
            topic = row[theme_col] if pd.notna(row.get(theme_col)) else ''
            description = row[desc_col] if pd.notna(row.get(desc_col)) else ''
            category = categorize_issue(topic, description)
            issue_categories[category] = issue_categories.get(category, 0) + 1
        
        print(f"✅ Проанализировано {sample_size} заявок")
    
    # Сортируем категории проблем по количеству заявок
    sorted_issues = sorted(issue_categories.items(), key=lambda x: x[1], reverse=True)
    
    # Создаем ПОЛНОСТЬЮ НОВЫЙ markdown отчет (ПЕРЕЗАПИСЫВАЕМ файл)
    md_content = f"""# 📊 Отчет по заявкам

**Обновлено:** {report_time}  
**Всего заявок:** {total_requests}

---

## 📈 Заявки ГМУ и ИОГВ за период с 5.01.2026 по 5.02.2026

### Общая статистика

| Тип учреждения | Всего заявок | Решено | В работе |
|----------------|--------------|--------|----------|
| Государственные учреждения | {gov_total} | {gov_resolved} | {gov_in_work} |
| Муниципальные учреждения | {mun_total} | {mun_resolved} | {mun_in_work} |
| ИОГВ ЯНАО | {iogv_total} | {iogv_resolved} | {iogv_in_work} |

---

### Анализ проблемных направлений

| № | Категория проблемы | Количество заявок | Доля |
|---|-------------------|-------------------|------|
"""
    
    if sorted_issues:
        sample_total = sum(issue_categories.values())
        for i, (category, count) in enumerate(sorted_issues, 1):
            percentage = round((count / sample_total) * 100, 1) if sample_total > 0 else 0
            md_content += f"| {i} | {category} | {count} | {percentage}% |\n"
    else:
        md_content += "| 1 | *Нет данных для анализа* | 0 | 0% |\n"
    
    # Добавляем разделитель перед дополнительными данными
    md_content += "\n---\n\n"
    
    # Проверяем и создаем директорию
    os.makedirs(os.path.dirname(md_path), exist_ok=True)
    
    # ПОЛНОСТЬЮ ПЕРЕЗАПИСЫВАЕМ ФАЙЛ (mode='w' - write, перезапись)
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    print(f"\n✅ Основной отчет успешно ПЕРЕЗАПИСАН: {md_path}")
    print(f"📊 Проанализировано заявок: {total_requests}")
    print(f"🏢 Государственные учреждения: {gov_total} заявок ({len(gov_orgs)} организаций)")
    print(f"🏢 Муниципальные учреждения: {mun_total} заявок ({len(mun_orgs)} организаций)")
    print(f"🏛️ ИОГВ ЯНАО: {iogv_total} заявок ({len(iogv_orgs)} организаций)")
    
    # Выводим список организаций ИОГВ ЯНАО в консоль для отладки
    if iogv_orgs:
        print(f"\n🔍 Организации ИОГВ ЯНАО ({len(iogv_orgs)} наименований):")
        for i, (org_name, count) in enumerate(iogv_orgs, 1):
            print(f"   {i:3}. {org_name[:80]}: {count} заявок")
    
    return {
        'total_requests': total_requests,
        'gov_total': gov_total,
        'gov_resolved': gov_resolved,
        'gov_in_work': gov_in_work,
        'gov_orgs': gov_orgs,
        'mun_total': mun_total,
        'mun_resolved': mun_resolved,
        'mun_in_work': mun_in_work,
        'mun_orgs': mun_orgs,
        'iogv_total': iogv_total,
        'iogv_resolved': iogv_resolved,
        'iogv_in_work': iogv_in_work,
        'iogv_orgs': iogv_orgs,
        'status_counts': dict(status_counts),
        'issue_categories': dict(sorted_issues)
    }

def generate_zayavky_report():
    """
    Читает данные из файла zayavky.xlsx (лист "Заявки") 
    и добавляет их в конец файла zayavky.md
    """
    print(f"\n📖 Читаем дополнительный файл: zayavky.xlsx")
    
    try:
        # Чтение файла Excel (лист "Заявки")
        file_path = "zayavky.xlsx"
        
        if not os.path.exists(file_path):
            print(f"❌ Файл {file_path} не найден!")
            return False
        
        # Пробуем прочитать лист "Заявки"
        try:
            df = pd.read_excel(file_path, sheet_name="Заявки", dtype=str)
            print(f"✅ Лист 'Заявки' прочитан успешно")
        except:
            # Если лист не найден, пробуем первый лист
            print("⚠️ Лист 'Заявки' не найден, читаем первый лист")
            df = pd.read_excel(file_path, dtype=str)
        
        # Проверяем, есть ли нужные колонки
        required_columns = ['Статус', 'Инициатор']
        missing_columns = [col for col in required_columns if col not in df.columns]
        
        if missing_columns:
            print(f"⚠️ В файле отсутствуют колонки: {missing_columns}")
            # Пробуем найти колонки с похожими названиями
            for col in required_columns:
                for df_col in df.columns:
                    if col.lower() in df_col.lower():
                        df.rename(columns={df_col: col}, inplace=True)
                        print(f"   • Переименовали '{df_col}' в '{col}'")
                        break
        
        # 1. Общая статистика
        total = len(df)
        print(f"📊 Всего заявок в zayavky.xlsx: {total}")
        
        # Статистика по статусам
        if 'Статус' in df.columns:
            # Приводим к строковому типу и очищаем
            df['Статус'] = df['Статус'].astype(str).str.strip()
            
            resolved = df[df['Статус'].str.contains('Решен', case=False, na=False)].shape[0]
            in_work = df[df['Статус'].str.contains('В работе', case=False, na=False)].shape[0]
            closed = df[df['Статус'].str.contains('Закрыт', case=False, na=False)].shape[0]
            
            print(f"   • Решено: {resolved}")
            print(f"   • В работе: {in_work}")
            print(f"   • Закрыто: {closed}")
        else:
            resolved = 0
            in_work = 0
            closed = 0
            print("⚠️ Колонка 'Статус' не найдена для статистики")
        
        # 2. Топ-3 активных инициаторов
        top_3_table = ""
        if 'Инициатор' in df.columns:
            # Очищаем данные инициаторов
            df['Инициатор'] = df['Инициатор'].astype(str).str.strip()
            initiator_counts = df['Инициатор'].value_counts().head(3)
            
            if not initiator_counts.empty:
                # Создаем таблицу для топ-3
                top_3_table = "| Инициатор | Количество заявок |\n|:---|---:|\n"
                for name, count in initiator_counts.items():
                    # Обрезаем длинные имена
                    name_display = str(name)[:30] + ('...' if len(str(name)) > 30 else '')
                    top_3_table += f"| {name_display} | {count} |\n"
                
                print(f"✅ Найдено {len(initiator_counts)} активных инициаторов")
            else:
                top_3_table = "*Нет данных об инициаторах*\n"
                print("⚠️ Нет данных об инициаторах")
        else:
            top_3_table = "*Колонка 'Инициатор' не найдена*\n"
            print("⚠️ Колонка 'Инициатор' не найдена")
        
        # Формируем содержимое Markdown
        md_content = f"""
## 📊 Заявки ЦБ ОГВ ЯНАО за прошлую неделю

### 1. Общая статистика

**Всего заявок:** {total}  
**Из них:**
- Решено: {resolved}
- В работе: {in_work} 
- Закрыто: {closed}
- Ожидают обработки: {total - resolved - in_work - closed}

### 2. Топ-3 активных инициаторов

{top_3_table}
"""
        
        return md_content
        
    except Exception as e:
        print(f"❌ Ошибка при чтении файла zayavky.xlsx: {e}")
        return False

if __name__ == "__main__":
    # Пути к файлам
    excel_file = "zayavky_all.xlsx"
    md_file = os.path.join("docs", "calls", "zayavky.md")
    os.makedirs(os.path.dirname(md_file), exist_ok=True)
    
    print("="*60)
    print("🚀 ЗАПУСК ГЕНЕРАЦИИ ОТЧЕТА")
    print("="*60)
    
    # Удаляем старый файл, чтобы убедиться, что создается новый
    if os.path.exists(md_file):
        print(f"🗑️ Удаляем старый файл: {md_file}")
        os.remove(md_file)
    
    if os.path.exists(excel_file):
        # 1. Генерируем основной отчет из zayavky_all.xlsx
        stats = parse_excel_to_md(excel_file, md_file)
        
        if stats:
            # 2. Добавляем данные из zayavky.xlsx в конец файла
            additional_content = generate_zayavky_report()
            
            if additional_content:
                # Добавляем дополнительный отчет к основному
                with open(md_file, 'a', encoding='utf-8') as f:
                    f.write(additional_content)
                
                print(f"\n✅ Дополнительные данные из zayavky.xlsx добавлены в конец файла")
            else:
                print(f"\n⚠️ Не удалось добавить данные из zayavky.xlsx")
            
            print("\n" + "="*60)
            print("✅ ФИНАЛЬНЫЙ ОТЧЕТ УСПЕШНО СОЗДАН")
            print("="*60)
            print(f"📋 Основные показатели:")
            print(f"   • Всего заявок: {stats['total_requests']}")
            print(f"   • Государственные учреждения: {stats['gov_total']} заявок ({len(stats['gov_orgs'])} организаций)")
            print(f"     (Решено: {stats['gov_resolved']}, В работе: {stats['gov_in_work']})")
            print(f"   • Муниципальные учреждения: {stats['mun_total']} заявок ({len(stats['mun_orgs'])} организаций)")
            print(f"     (Решено: {stats['mun_resolved']}, В работе: {stats['mun_in_work']})")
            print(f"   • ИОГВ ЯНАО: {stats['iogv_total']} заявок ({len(stats['iogv_orgs'])} организаций)")
            print(f"     (Решено: {stats['iogv_resolved']}, В работе: {stats['iogv_in_work']})")
            
            print(f"\n📄 Файл создан: {md_file}")
            print("📁 Содержит:")
            print("   1. Основной отчет из zayavky_all.xlsx")
            print("   2. Дополнительные данные из zayavky.xlsx")
    else:
        print(f"❌ Основной файл {excel_file} не найден!")
        
        # Проверяем существование zayavky.xlsx
        if os.path.exists("zayavky.xlsx"):
            print(f"⚠️ Но найден файл zayavky.xlsx - пробуем создать отчет только из него")
            
            # Создаем базовый отчет
            report_time = datetime.now().strftime("%d.%m.%Y %H:%M")
            md_content = f"""# 📊 Отчет по заявкам

**Обновлено:** {report_time}

"""
            
            # Добавляем данные из zayavky.xlsx
            additional_content = generate_zayavky_report()
            
            if additional_content:
                md_content += additional_content
                
                # Сохраняем файл
                os.makedirs("docs", exist_ok=True)
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(md_content)
                
                print(f"\n✅ Отчет создан только из zayavky.xlsx: {md_file}")
            else:
                print("❌ Не удалось создать отчет")