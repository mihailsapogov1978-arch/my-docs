import pandas as pd
from datetime import datetime, timedelta
import warnings
import os
import glob
import numpy as np
import re
warnings.filterwarnings('ignore')

def format_duration(minutes):
    """Форматирование длительности в читаемый вид"""
    if pd.isna(minutes) or minutes == 0:
        return "0 мин"
    
    hours = int(minutes // 60)
    mins = int(minutes % 60)
    
    if hours > 0:
        if mins > 0:
            return f"{hours} час {mins} мин"
        else:
            return f"{hours} час"
    else:
        return f"{mins} мин"

def convert_duration(value):
    """Конвертирует значение продолжительности в секунды (число)"""
    if pd.isna(value):
        return 0
    
    # Если это строка, удаляем лишние символы и пробелы
    if isinstance(value, str):
        value = str(value).strip()
        if value == '' or value.lower() in ['nan', 'null', 'none']:
            return 0
        
        # Пробуем преобразовать в число
        try:
            # Убираем запятые и другие нечисловые символы (кроме точки)
            value = ''.join(ch for ch in value if ch.isdigit() or ch == '.')
            if value:
                return float(value)
            else:
                return 0
        except:
            return 0
    
    # Если уже число
    try:
        return float(value)
    except:
        return 0

def normalize_name(name):
    """Нормализует имя: удаляет лишние пробелы, приводит к стандартному виду"""
    if pd.isna(name):
        return ''
    
    name_str = str(name).strip()
    # Удаляем двойные и более пробелы
    name_str = re.sub(r'\s+', ' ', name_str)
    # Удаляем пробелы в конце имен (часто встречается в данных)
    name_str = name_str.rstrip()
    
    return name_str

def get_last_30_days_data(df):
    """Получаем данные за последние 30 дней"""
    # Определяем последнюю дату в данных
    last_date = df['Время старта'].max()
    
    # Начало периода - 30 дней назад
    start_date = last_date - timedelta(days=30)
    
    print(f"📅 Последняя дата в данных: {last_date.strftime('%d.%m.%Y %H:%M:%S')}")
    print(f"📅 Начало периода (30 дней назад): {start_date.strftime('%d.%m.%Y %H:%M:%S')}")
    print(f"📅 Дней в периоде: 30 дней")
    
    # Фильтруем данные за последние 30 дней
    period_data = df[(df['Время старта'] >= start_date) & (df['Время старта'] <= last_date)]
    
    return period_data, start_date, last_date

def analyze_calls_csv(file_path, output_path="docs/calls.md"):
    # Список сотрудников отдела СР и ТП
    sr_tp_employees = [
        "Ставер Андрей Петрович",
        "Сапогов Михаил Дмитриевич",
        "Чечеткин Михаил Игоревич",
        "Обмолова Валентина Витальевна",
        "Роганова Анна Анатольевна",
        "Кошик Владимир Иванович",
        "Худышкин Сергей Николаевич",
        "Гасанов Сархан Нураддин"
    ]
    
    # Проверяем, существует ли файл
    if not os.path.exists(file_path):
        print(f"❌ Файл {file_path} не найден!")
        
        # Пробуем найти CSV файлы
        csv_files = glob.glob("*.csv") + glob.glob("**/*.csv", recursive=True)
        if csv_files:
            print(f"📁 Найдены CSV файлы: {csv_files}")
            file_path = csv_files[0]
            print(f"📁 Используем файл: {file_path}")
        else:
            print("❌ CSV файлы не найдены!")
            return
    
    # Читаем CSV файл
    try:
        # Пробуем определить кодировку и разделитель
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            first_line = f.readline()
            
        # Проверяем разделитель
        if ';' in first_line and ',' not in first_line.replace('",', ''):
            separator = ';'
        else:
            separator = ','
        
        print(f"📖 Чтение файла {file_path} с разделителем '{separator}'")
        df = pd.read_csv(file_path, sep=separator, low_memory=False)
        
    except Exception as e:
        print(f"❌ Ошибка при чтении CSV файла {file_path}: {e}")
        print("⚠️  Пробуем альтернативные кодировки...")
        try:
            # Пробуем разные кодировки
            for encoding in ['cp1251', 'windows-1251', 'utf-8']:
                try:
                    df = pd.read_csv(file_path, encoding=encoding, sep=None, engine='python')
                    print(f"✅ Успешно прочитано с кодировкой {encoding}")
                    break
                except:
                    continue
        except Exception as e2:
            print(f"❌ Не удалось прочитать файл: {e2}")
            return
    
    # Выводим информацию о колонках
    print(f"📊 Загружено {len(df)} записей")
    print(f"📋 Колонки в файле: {list(df.columns)}")
    
    # Стандартизируем названия колонок (убираем пробелы в начале/конце)
    df.columns = df.columns.str.strip()
    
    # Удаляем пустые колонки
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    
    # Проверяем наличие необходимых колонок
    required_columns = ['Время старта', 'Имя инициатора', 'Имя адресата вызова', 
                       'Продолжительность вызова', 'Результат вызова конечного получателя']
    
    for col in required_columns:
        if col not in df.columns:
            print(f"⚠️  Внимание: колонка '{col}' не найдена в файле")
            print(f"   Доступные колонки: {list(df.columns)}")
            # Пробуем найти похожие названия
            similar = [c for c in df.columns if col.lower() in c.lower()]
            if similar:
                print(f"   Возможно имелось в виду: {similar}")
    
    # Преобразуем время в datetime
    try:
        print("🔄 Преобразование дат...")
        df['Время старта'] = pd.to_datetime(df['Время старта'], errors='coerce')
        df['Время разъединения'] = pd.to_datetime(df['Время разъединения'], errors='coerce')
        
        # Удаляем строки с некорректными датами
        initial_count = len(df)
        df = df.dropna(subset=['Время старта'])
        removed_count = initial_count - len(df)
        if removed_count > 0:
            print(f"🗑️  Удалено {removed_count} записей с некорректными датами")
        
        print(f"📅 Диапазон дат в данных: {df['Время старта'].min()} - {df['Время старта'].max()}")
    except Exception as e:
        print(f"❌ Ошибка при преобразовании дат: {e}")
        return
    
    # Преобразуем Продолжительность вызова в числа
    if 'Продолжительность вызова' in df.columns:
        print("🔄 Преобразование продолжительности вызовов в числа...")
        initial_non_numeric = df['Продолжительность вызова'].apply(lambda x: not isinstance(x, (int, float)) and not pd.isna(x)).sum()
        print(f"📊 Найдено {initial_non_numeric} нечисловых значений в столбце 'Продолжительность вызова'")
        
        df['Продолжительность вызова'] = df['Продолжительность вызова'].apply(convert_duration)
        
        # Проверяем результат
        numeric_count = df['Продолжительность вызова'].apply(lambda x: isinstance(x, (int, float))).sum()
        print(f"✅ Преобразовано {numeric_count} значений в числовой формат")
        print(f"📊 Минимальная продолжительность: {df['Продолжительность вызова'].min():.1f} сек")
        print(f"📊 Максимальная продолжительность: {df['Продолжительность вызова'].max():.1f} сек")
        print(f"📊 Средняя продолжительность: {df['Продолжительность вызова'].mean():.1f} сек")
    
    # Нормализуем имена в колонках
    if 'Имя инициатора' in df.columns:
        print("🔄 Нормализация имен инициаторов...")
        df['Имя инициатора'] = df['Имя инициатора'].apply(normalize_name)
    
    if 'Имя адресата вызова' in df.columns:
        print("🔄 Нормализация имен адресатов...")
        df['Имя адресата вызова'] = df['Имя адресата вызова'].apply(normalize_name)
    
    # 1. Получаем данные за последние 30 дней
    df_period, start_date, end_date = get_last_30_days_data(df)
    
    if len(df_period) == 0:
        print(f"⚠️ Нет данных за последние 30 дней ({start_date.strftime('%d.%m.%Y')} - {end_date.strftime('%d.%m.%Y')})!")
        print("📊 Используем все доступные данные...")
        df_period = df
        start_date = df['Время старта'].min()
        end_date = df['Время старта'].max()
    
    print(f"📊 Данных за период: {len(df_period)} записей")
    print(f"📅 Период: {start_date.strftime('%d.%m.%Y')} - {end_date.strftime('%d.%m.%Y')}")
    
    # Проверяем имена сотрудников в данных
    print("\n🔍 Проверка сотрудников отдела СР и ТП в данных:")
    found_employees = []
    for employee in sr_tp_employees:
        # Проверяем как инициатора
        as_initiator = len(df_period[df_period['Имя инициатора'] == employee])
        # Проверяем как адресата
        as_target = len(df_period[df_period['Имя адресата вызова'] == employee])
        
        if as_initiator > 0 or as_target > 0:
            print(f"  ✅ {employee}: инициатор {as_initiator} раз, адресат {as_target} раз")
            found_employees.append(employee)
        else:
            print(f"  ❌ {employee}: не найден")
    
    # Uplink теперь включаем в статистику (не фильтруем)
    print("\nℹ️  Uplink включен в статистику (но не отображается в таблицах отдельно)")
    
    # Рассчитываем количество рабочих дней (исключаем выходные)
    business_days = pd.bdate_range(start=start_date.date(), end=end_date.date()).shape[0]
    print(f"📅 Рабочих дней в периоде: {business_days}")
    print(f"📅 Всего дней в периоде: {(end_date - start_date).days + 1}")
    
    # Создаем markdown файл
    with open(output_path, 'w', encoding='utf-8') as md_file:
        # Заголовок и метаданные для Material Theme
        md_file.write("""---
title: Анализ телефонных звонков
description: Статистика и аналитика по звонкам за последние 30 дней
date: """ + datetime.now().strftime("%Y-%m-%d") + """
tags:
  - аналитика
  - звонки
  - статистика
  - CDR
---

# 📊 Анализ телефонных звонков 
## Период: """ + start_date.strftime("%d.%m.%Y") + " - " + end_date.strftime("%d.%m.%Y") + """
### (Последние 30 дней)

""")
        
        # Общая информация
        md_file.write(f"## 📋 Общая статистика за период\n\n")
        md_file.write(f"| Показатель | Значение |\n")
        md_file.write(f"|------------|----------|\n")
        md_file.write(f"| Всего записей о вызовах | {len(df_period)} |\n")
        md_file.write(f"| Период данных | с {df_period['Время старта'].min().strftime('%d.%m.%Y')} по {df_period['Время старта'].max().strftime('%d.%m.%Y')} |\n")
        md_file.write(f"| Всего дней в периоде | {(end_date - start_date).days + 1} дней |\n")
        md_file.write(f"| Рабочих дней в периоде | {business_days} дней |\n")
        
        if 'Имя инициатора' in df_period.columns:
            md_file.write(f"| Уникальных инициаторов | {df_period['Имя инициатора'].nunique()} |\n")
        
        if 'Имя адресата вызова' in df_period.columns:
            md_file.write(f"| Уникальных адресатов | {df_period['Имя адресата вызова'].nunique()} |\n")
        
        # 1. Топ 5 инициаторов по количеству звонков (Uplink не показываем)
        if 'Имя инициатора' in df_period.columns:
            md_file.write("\n## 🎯 Топ-5 инициаторов по количеству звонков\n\n")
            
            # Фильтруем, чтобы не показывать Uplink в таблице, но учитываем его звонки для сотрудников
            initiator_stats = df_period['Имя инициатора'].value_counts()
            # Исключаем Uplink из отображения в топе
            initiator_stats_no_uplink = initiator_stats[initiator_stats.index != 'Uplink']
            
            if len(initiator_stats_no_uplink) > 0:
                top_initiators = initiator_stats_no_uplink.head(5)
                md_file.write("| № | Инициатор | Количество звонков | Среднее в день |\n")
                md_file.write("|:-:|-----------|-------------------|----------------|\n")
                for i, (name, count) in enumerate(top_initiators.items(), 1):
                    daily_avg = count / business_days if business_days > 0 else 0
                    md_file.write(f"| {i} | {name} | {count} | {daily_avg:.1f} |\n")
            else:
                md_file.write("Нет данных для отображения\n")
        
        # 2. Топ 5 адресатов по количеству звонков (Uplink не показываем)
        if 'Имя адресата вызова' in df_period.columns:
            md_file.write("\n## 📞 Топ-5 адресатов по количеству звонков\n\n")
            
            # Считаем статистику для каждого адресата (исключая Uplink из отображения)
            all_targets = df_period['Имя адресата вызова'].value_counts()
            # Исключаем Uplink из отображения в топе
            all_targets_no_uplink = all_targets[all_targets.index != 'Uplink'].head(10)
            
            # Подготовим данные для таблицы
            target_stats = []
            for target in all_targets_no_uplink.index:
                target_calls = df_period[df_period['Имя адресата вызова'] == target]
                total_calls = len(target_calls)
                
                # Пропущенные звонки
                if 'Результат вызова конечного получателя' in target_calls.columns:
                    missed_calls = len(target_calls[~target_calls['Результат вызова конечного получателя'].astype(str).str.contains('Соединение установлено', na=False)])
                else:
                    missed_calls = 0
                
                # Принятые звонки
                accepted_calls = total_calls - missed_calls
                
                target_stats.append({
                    'Адресат': target,
                    'Всего': total_calls,
                    'Пропущено': missed_calls,
                    'Принято': accepted_calls,
                    'Процент принятых': (accepted_calls / total_calls * 100) if total_calls > 0 else 0
                })
            
            # Берем топ-5
            if target_stats:
                target_stats = sorted(target_stats, key=lambda x: x['Всего'], reverse=True)[:5]
                
                md_file.write("| № | Адресат | Всего звонков | Из них пропущено | Принято | % принятых |\n")
                md_file.write("|:-:|---------|---------------|------------------|---------|------------|\n")
                for i, stat in enumerate(target_stats, 1):
                    md_file.write(f"| {i} | {stat['Адресат']} | {stat['Всего']} | {stat['Пропущено']} | {stat['Принято']} | {stat['Процент принятых']:.1f}% |\n")
            else:
                md_file.write("Нет данных для отображения\n")
        
        # 3. Топ-5 по общей длительности разговоров (в минутах) - Uplink не показываем
        if 'Продолжительность вызова' in df_period.columns and 'Имя инициатора' in df_period.columns:
            md_file.write("\n## ⏱️ Топ-5 по общей длительности разговоров\n\n")
            
            try:
                # Считаем общую длительность в минутах для каждого инициатора (исключая Uplink)
                initiator_duration = df_period.groupby('Имя инициатора')['Продолжительность вызова'].sum() / 60
                # Исключаем Uplink из отображения
                initiator_duration_no_uplink = initiator_duration[initiator_duration.index != 'Uplink']
                initiator_duration_minutes = initiator_duration_no_uplink.sort_values(ascending=False).head(5)
                
                if len(initiator_duration_minutes) > 0:
                    md_file.write("| № | Инициатор | Общая длительность | Среднее в день |\n")
                    md_file.write("|:-:|-----------|-------------------|----------------|\n")
                    for i, (name, duration_minutes) in enumerate(initiator_duration_minutes.items(), 1):
                        formatted_duration = format_duration(duration_minutes)
                        daily_avg = format_duration(duration_minutes / business_days) if business_days > 0 else "0 мин"
                        md_file.write(f"| {i} | {name} | {formatted_duration} | {daily_avg} |\n")
                else:
                    md_file.write("Нет данных для отображения\n")
            except Exception as e:
                print(f"⚠️  Ошибка при расчете длительности: {e}")
                md_file.write("Не удалось рассчитать длительность разговоров\n")
        
        # 4. Самые активные пары (кто кому чаще всего звонит) - Uplink не показываем
        if 'Имя инициатора' in df_period.columns and 'Имя адресата вызова' in df_period.columns:
            md_file.write("\n## 🤝 Самые активные пары собеседников\n\n")
            try:
                # Исключаем пары, где инициатор или адресат - Uplink
                df_filtered = df_period[(df_period['Имя инициатора'] != 'Uplink') & (df_period['Имя адресата вызова'] != 'Uplink')]
                df_filtered['Пара'] = df_filtered['Имя инициатора'].astype(str) + " → " + df_filtered['Имя адресата вызова'].astype(str)
                top_pairs = df_filtered['Пара'].value_counts().head(5)
                
                if len(top_pairs) > 0:
                    md_file.write("| № | Пара собеседников | Количество звонков | Среднее в день |\n")
                    md_file.write("|:-:|------------------|-------------------|----------------|\n")
                    for i, (pair, count) in enumerate(top_pairs.items(), 1):
                        daily_avg = count / business_days if business_days > 0 else 0
                        md_file.write(f"| {i} | {pair} | {count} | {daily_avg:.1f} |\n")
                else:
                    md_file.write("Нет данных для отображения\n")
            except Exception as e:
                md_file.write(f"Не удалось рассчитать пары собеседников: {e}\n")
        
        # 5. Статистика по отделу СР и ТП
        if 'Имя инициатора' in df_period.columns and 'Имя адресата вызова' in df_period.columns:
            md_file.write("\n## 👨‍💼 Отдел СР и ТП\n\n")
            
            # Статистика по инициаторам отдела СР и ТП
            md_file.write("### Инициаторы отдела СР и ТП\n\n")
            
            sr_tp_initiators_stats = []
            
            for employee in found_employees:  # Используем только найденных сотрудников
                # Находим все звонки, где сотрудник был инициатором (включая звонки на Uplink)
                employee_calls_as_initiator = df_period[df_period['Имя инициатора'] == employee]
                total_calls = len(employee_calls_as_initiator)
                
                if total_calls > 0:
                    sr_tp_initiators_stats.append({
                        'Инициатор': employee,
                        'Количество звонков': total_calls,
                        'Среднее в день': total_calls / business_days if business_days > 0 else 0
                    })
            
            if sr_tp_initiators_stats:
                # Сортируем по количеству звонков
                sr_tp_initiators_stats = sorted(sr_tp_initiators_stats, key=lambda x: x['Количество звонков'], reverse=True)
                
                md_file.write("| № | Инициатор | Количество звонков | Среднее в день |\n")
                md_file.write("|:-:|-----------|-------------------|----------------|\n")
                for i, stat in enumerate(sr_tp_initiators_stats, 1):
                    md_file.write(f"| {i} | {stat['Инициатор']} | {stat['Количество звонков']} | {stat['Среднее в день']:.1f} |\n")
            else:
                md_file.write("Нет данных по инициаторам отдела СР и ТП\n")
            
            # Статистика по адресатам отдела СР и ТП
            md_file.write("\n### Адресаты отдела СР и ТП\n\n")
            
            sr_tp_targets_stats = []
            
            for employee in found_employees:  # Используем только найденных сотрудников
                # Находим все звонки, где сотрудник был адресатом (включая звонки от Uplink)
                employee_calls_as_target = df_period[df_period['Имя адресата вызова'] == employee]
                total_calls = len(employee_calls_as_target)
                
                if total_calls > 0:
                    # Пропущенные звонки
                    if 'Результат вызова конечного получателя' in employee_calls_as_target.columns:
                        missed_calls = len(employee_calls_as_target[~employee_calls_as_target['Результат вызова конечного получателя'].astype(str).str.contains('Соединение установлено', na=False)])
                    else:
                        missed_calls = 0
                    
                    # Принятые звонки
                    accepted_calls = total_calls - missed_calls
                    
                    sr_tp_targets_stats.append({
                        'Адресат': employee,
                        'Всего звонков': total_calls,
                        'Пропущено': missed_calls,
                        'Принято': accepted_calls,
                        'Процент принятых': (accepted_calls / total_calls * 100) if total_calls > 0 else 0
                    })
            
            if sr_tp_targets_stats:
                # Сортируем по общему количество звонков
                sr_tp_targets_stats = sorted(sr_tp_targets_stats, key=lambda x: x['Всего звонков'], reverse=True)
                
                md_file.write("| № | Адресат | Всего звонков | Из них пропущено | Принято | % принятых |\n")
                md_file.write("|:-:|---------|---------------|------------------|---------|------------|\n")
                for i, stat in enumerate(sr_tp_targets_stats, 1):
                    md_file.write(f"| {i} | {stat['Адресат']} | {stat['Всего звонков']} | {stat['Пропущено']} | {stat['Принято']} | {stat['Процент принятых']:.1f}% |\n")
            else:
                md_file.write("Нет данных по адресатам отдела СР и ТП\n")
            
            # Общая статистика по отделу СР и ТП
            md_file.write("\n### Общая статистика по отделу СР и ТП\n\n")
            
            # Считаем общее количество звонков с участием сотрудников отдела
            all_sr_tp_calls = df_period[
                (df_period['Имя инициатора'].isin(found_employees)) | 
                (df_period['Имя адресата вызова'].isin(found_employees))
            ]
            
            # Звонки, где сотрудники отдела были инициаторами
            sr_tp_as_initiators = df_period[df_period['Имя инициатора'].isin(found_employees)]
            
            # Звонки, где сотрудники отдела были адресатами
            sr_tp_as_targets = df_period[df_period['Имя адресата вызова'].isin(found_employees)]
            
            md_file.write(f"| Показатель | Значение |\n")
            md_file.write(f"|------------|----------|\n")
            md_file.write(f"| Всего звонков с участием отдела | {len(all_sr_tp_calls)} |\n")
            md_file.write(f"| Из них: сотрудники как инициаторы | {len(sr_tp_as_initiators)} |\n")
            md_file.write(f"| Из них: сотрудники как адресаты | {len(sr_tp_as_targets)} |\n")
            if len(df_period) > 0:
                md_file.write(f"| Доля от общего числа звонков | {len(all_sr_tp_calls)/len(df_period)*100:.1f}% |\n")
            else:
                md_file.write(f"| Доля от общего числа звонков | 0% |\n")
        
        # Разделы, которые были на скрине (диаграмма, статистика по дням, выводы) - УДАЛЕНЫ
        
        md_file.write("\n---\n\n")
        md_file.write(f"*Отчет сгенерирован: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}*\n")
        md_file.write(f"*Источник данных: {os.path.basename(file_path)}*\n")
        md_file.write(f"*Период анализа: {start_date.strftime('%d.%m.%Y')} - {end_date.strftime('%d.%m.%Y')} ({business_days} рабочих дней)*\n")
        md_file.write(f"*Uplink включен в статистику (но не отображается в таблицах)*\n")
        md_file.write(f"*В статистике по отделу СР и ТП учтены звонки с Uplink*\n")
    
    print(f"\n✅ Отчет успешно сохранен в файл: {output_path}")
    print(f"📊 Всего записей в отчете: {len(df_period)}")
    print(f"📅 Период: {start_date.strftime('%d.%m.%Y')} - {end_date.strftime('%d.%m.%Y')}")
    if 'Имя инициатора' in df_period.columns:
        print(f"👥 Уникальных инициаторов: {df_period['Имя инициатора'].nunique()}")

if __name__ == "__main__":
    # Укажите путь к вашему CSV файлу
    file_path = "calls.csv"  # Основное имя файла
    
    # Проверяем, существует ли основной файл, если нет - ищем альтернативы
    if not os.path.exists(file_path):
        # Пробуем найти файлы с разными расширениями и префиксами
        possible_files = ["calls.csv", "calls1.csv", "calls_data.csv", 
                         "docs/calls/calls.csv", "data/calls.csv", "*.csv"]
        
        found = False
        for pattern in possible_files:
            if "*" in pattern:
                files = glob.glob(pattern)
                if files:
                    file_path = files[0]
                    found = True
                    break
            elif os.path.exists(pattern):
                file_path = pattern
                found = True
                break
        
        if not found:
            print("❌ Не найден файл с данными звонков")
            print("⚠️  Разместите файл calls.csv в той же директории, что и скрипт")
            exit(1)
    
    # Путь для сохранения отчета
    output_path = "docs/calls.md"
    
    # Создаем директорию docs, если её нет
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Запускаем анализ
    try:
        analyze_calls_csv(file_path, output_path)
    except Exception as e:
        print(f"❌ Ошибка при выполнении анализа: {e}")
        import traceback
        traceback.print_exc()