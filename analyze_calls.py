import pandas as pd
from datetime import datetime
import warnings
import os
warnings.filterwarnings('ignore')

def format_duration(minutes):
    """Форматирование длительности в читаемый вид"""
    hours = int(minutes // 60)
    mins = int(minutes % 60)
    
    if hours > 0:
        if mins > 0:
            return f"{hours} час {mins} мин"
        else:
            return f"{hours} час"
    else:
        return f"{mins} мин"

def analyze_calls(file_path, output_path="docs/calls.md"):
    # Проверяем, существует ли файл
    if not os.path.exists(file_path):
        print(f"❌ Файл {file_path} не найден!")
        return
    
    # Игнорируем временные файлы Excel
    if "~$" in file_path:
        print(f"⚠️  Пропускаем временный файл Excel: {file_path}")
        return
    
    # Читаем Excel файл
    try:
        df = pd.read_excel(file_path, sheet_name=0)
    except Exception as e:
        print(f"❌ Ошибка при чтении файла {file_path}: {e}")
        return
    
    # Преобразуем время в datetime
    df['Время старта'] = pd.to_datetime(df['Время старта'])
    df['Время разъединения'] = pd.to_datetime(df['Время разъединения'])
    
    # 1. Фильтруем данные за период с 21.01.2025 по 20.02.2025
    start_date = pd.Timestamp('2025-01-21')
    end_date = pd.Timestamp('2025-02-20')
    
    df_period = df[(df['Время старта'] >= start_date) & (df['Время старта'] <= end_date)]
    
    if len(df_period) == 0:
        print("⚠️ Нет данных за указанный период!")
        return
    
    # 2. Убираем Uplink из отчетов
    df_period = df_period[df_period['Имя инициатора'] != 'Uplink']
    df_period = df_period[df_period['Имя адресата вызова'] != 'Uplink']
    
    # Создаем markdown файл
    with open(output_path, 'w', encoding='utf-8') as md_file:
        # Заголовок и метаданные для Material Theme
        md_file.write("""---
title: Анализ телефонных звонков
description: Статистика и аналитика по звонкам за период с 21 января по 20 февраля 2025 года
date: """ + datetime.now().strftime("%Y-%m-%d") + """
tags:
  - аналитика
  - звонки
  - статистика
  - CDR
---

# 📊 Анализ телефонных звонков 
## Период: 21 января - 20 февраля 2025 года

""")
        
        # Общая информация
        md_file.write(f"## 📋 Общая статистика за период\n\n")
        md_file.write(f"| Показатель | Значение |\n")
        md_file.write(f"|------------|----------|\n")
        md_file.write(f"| Всего записей о вызовах | {len(df_period)} |\n")
        md_file.write(f"| Период данных | с {df_period['Время старта'].min().strftime('%d.%m.%Y')} по {df_period['Время старта'].max().strftime('%d.%m.%Y')} |\n")
        md_file.write(f"| Рабочих дней в периоде | 23 дня |\n")
        
        # 1. Топ 5 инициаторов по количеству звонков
        md_file.write("\n## 🎯 Топ-5 инициаторов по количеству звонков\n\n")
        top_initiators = df_period['Имя инициатора'].value_counts().head(5)
        md_file.write("| № | Инициатор | Количество звонков | Среднее в день |\n")
        md_file.write("|---|-----------|-------------------|----------------|\n")
        for i, (name, count) in enumerate(top_initiators.items(), 1):
            daily_avg = count / 23
            md_file.write(f"| {i} | {name} | {count} | {daily_avg:.1f} |\n")
        
        # 2. Топ 5 адресатов по количеству звонков с детальной статистикой
        md_file.write("\n## 📞 Топ-5 адресатов по количеству звонков\n\n")
        
        # Считаем статистику для каждого адресата
        all_targets = df_period['Имя адресата вызова'].value_counts().head(10)
        
        # Подготовим данные для таблицы
        target_stats = []
        for target in all_targets.index:
            target_calls = df_period[df_period['Имя адресата вызова'] == target]
            total_calls = len(target_calls)
            
            # Пропущенные звонки
            missed_calls = len(target_calls[target_calls['Результат вызова конечного получателя'] != 'Соединение установлено'])
            
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
        target_stats = sorted(target_stats, key=lambda x: x['Всего'], reverse=True)[:5]
        
        md_file.write("| № | Адресат | Всего звонков | Из них пропущено | Принято | % принятых |\n")
        md_file.write("|---|---------|---------------|------------------|---------|------------|\n")
        for i, stat in enumerate(target_stats, 1):
            md_file.write(f"| {i} | {stat['Адресат']} | {stat['Всего']} | {stat['Пропущено']} | {stat['Принято']} | {stat['Процент принятых']:.1f}% |\n")
        
        # 3. Топ-5 по общей длительности разговоров (в минутах)
        md_file.write("\n## ⏱️ Топ-5 по общей длительности разговоров\n\n")
        
        # Считаем общую длительность в минутах для каждого инициатора
        initiator_duration_minutes = df_period.groupby('Имя инициатора')['Продолжительность вызова'].sum() / 60
        initiator_duration_minutes = initiator_duration_minutes.sort_values(ascending=False).head(5)
        
        md_file.write("| № | Инициатор | Общая длительность | Среднее в день |\n")
        md_file.write("|---|-----------|-------------------|----------------|\n")
        for i, (name, duration_minutes) in enumerate(initiator_duration_minutes.items(), 1):
            formatted_duration = format_duration(duration_minutes)
            daily_avg = format_duration(duration_minutes / 23)
            md_file.write(f"| {i} | {name} | {formatted_duration} | {daily_avg} |\n")
        
        # 4. Средняя продолжительность звонка
        md_file.write("\n## 📈 Средняя продолжительность звонков\n\n")
        avg_duration = df_period['Продолжительность вызова'].mean()
        avg_minutes = avg_duration / 60
        avg_formatted = format_duration(avg_minutes)
        md_file.write(f"Средняя продолжительность звонка: **{avg_formatted}** ({avg_duration:.1f} секунд)\n")
        
        # 5. Распределение звонков по времени суток
        md_file.write("\n## 🕐 Распределение звонков по времени суток\n\n")
        df_period['Час'] = df_period['Время старта'].dt.hour
        hour_distribution = df_period['Час'].value_counts().sort_index()
        
        time_periods = {
            'Ночь (00:00-06:00)': 0,
            'Утро (06:00-12:00)': 0,
            'День (12:00-18:00)': 0,
            'Вечер (18:00-00:00)': 0
        }
        
        for hour, count in hour_distribution.items():
            if 0 <= hour < 6:
                time_periods['Ночь (00:00-06:00)'] += count
            elif 6 <= hour < 12:
                time_periods['Утро (06:00-12:00)'] += count
            elif 12 <= hour < 18:
                time_periods['День (12:00-18:00)'] += count
            else:
                time_periods['Вечер (18:00-00:00)'] += count
        
        md_file.write("| Время суток | Количество звонков | Доля |\n")
        md_file.write("|-------------|-------------------|------|\n")
        for period, count in time_periods.items():
            percentage = (count / len(df_period)) * 100 if len(df_period) > 0 else 0
            md_file.write(f"| {period} | {count} | {percentage:.1f}% |\n")
        
        # 6. Статистика по типам вызовов (внутренние/внешние)
        md_file.write("\n## 🌐 Типы вызовов\n\n")
        
        # Определяем тип вызова по имени маршрута
        internal_calls = df_period[df_period['Имя маршрута'] == 'DialLocalNumbers']
        external_calls = df_period[df_period['Имя маршрута'] != 'DialLocalNumbers']
        
        md_file.write("| Тип вызова | Количество | Доля | Средняя длительность |\n")
        md_file.write("|------------|------------|------|----------------------|\n")
        
        internal_avg = internal_calls['Продолжительность вызова'].mean() / 60 if len(internal_calls) > 0 else 0
        external_avg = external_calls['Продолжительность вызова'].mean() / 60 if len(external_calls) > 0 else 0
        
        md_file.write(f"| Внутренние звонки | {len(internal_calls)} | {len(internal_calls)/len(df_period)*100:.1f}% | {format_duration(internal_avg)} |\n")
        md_file.write(f"| Внешние звонки | {len(external_calls)} | {len(external_calls)/len(df_period)*100:.1f}% | {format_duration(external_avg)} |\n")
        
        # 7. Активность по дням - таблица вместо mermaid
        md_file.write("\n## 📅 Активность по дням\n\n")
        
        # Готовим данные
        df_period['Дата'] = df_period['Время старта'].dt.date
        
        # Создаем список всех дней в периоде
        day_stats = []
        current_date = start_date
        while current_date <= end_date:
            day_calls = len(df_period[df_period['Дата'] == current_date.date()])
            day_name = current_date.strftime('%A')
            date_str = current_date.strftime('%d.%m.%Y')
            day_stats.append({
                'Дата': date_str,
                'Звонков': day_calls,
                'День недели': day_name
            })
            current_date += pd.Timedelta(days=1)
        
        md_file.write("### Статистика по дням\n\n")
        md_file.write("| Дата | Количество звонков | День недели |\n")
        md_file.write("|------|-------------------|-------------|\n")
        
        for day in day_stats:
            md_file.write(f"| {day['Дата']} | {day['Звонков']} | {day['День недели']} |\n")
        
        # Добавляем простую текстовую гистограмму
        md_file.write("\n### График активности (текстовый)\n\n")
        md_file.write("```\n")
        for day in day_stats:
            # Создаем простую текстовую гистограмму
            bars = "█" * min(day['Звонков'] // 10, 50)  # 1 символ = 10 звонков, максимум 50 символов
            if bars:
                md_file.write(f"{day['Дата']}: {bars} {day['Звонков']}\n")
            else:
                md_file.write(f"{day['Дата']}: {day['Звонков']}\n")
        md_file.write("```\n")
        md_file.write("*Примечание: 1 символ █ = примерно 10 звонков*\n")
        
        # 8. Самые активные пары (кто кому чаще всего звонит)
        md_file.write("\n## 🤝 Самые активные пары собеседников\n\n")
        df_period['Пара'] = df_period['Имя инициатора'] + " → " + df_period['Имя адресата вызова']
        top_pairs = df_period['Пара'].value_counts().head(5)
        md_file.write("| № | Пара собеседников | Количество звонков | Среднее в день |\n")
        md_file.write("|---|------------------|-------------------|----------------|\n")
        for i, (pair, count) in enumerate(top_pairs.items(), 1):
            daily_avg = count / 23
            md_file.write(f"| {i} | {pair} | {count} | {daily_avg:.1f} |\n")
        
        # 9. Статистика по инициаторам разъединения
        md_file.write("\n## 📞 Кто чаще всего завершает звонки\n\n")
        disconnect_stats = df_period['Инициатор разъединения'].value_counts()
        md_file.write("| Инициатор завершения | Количество | Доля |\n")
        md_file.write("|----------------------|------------|------|\n")
        for initiator, count in disconnect_stats.items():
            percentage = (count / len(df_period)) * 100 if len(df_period) > 0 else 0
            md_file.write(f"| {initiator} | {count} | {percentage:.1f}% |\n")
        
        # 10. Короткие звонки (менее 10 секунд)
        md_file.write("\n## ⏰ Короткие звонки (< 10 секунд)\n\n")
        short_calls = df_period[df_period['Продолжительность вызова'] < 10]
        short_percentage = len(short_calls)/len(df_period)*100 if len(df_period) > 0 else 0
        
        md_file.write(f"**Всего коротких звонков:** {len(short_calls)} ({short_percentage:.1f}%)\n\n")
        
        if len(short_calls) > 0:
            short_calls_initiators = short_calls['Имя инициатора'].value_counts().head(3)
            md_file.write("### Топ инициаторов коротких звонков\n\n")
            md_file.write("| № | Инициатор | Коротких звонков |\n")
            md_file.write("|---|-----------|------------------|\n")
            for i, (name, count) in enumerate(short_calls_initiators.items(), 1):
                md_file.write(f"| {i} | {name} | {count} |\n")
        
        # 11. Детальное распределение по часам
        md_file.write("\n## 👔 Детальное распределение звонков по часам\n\n")
        hourly_stats = df_period['Час'].value_counts().sort_index()
        
        if len(hourly_stats) > 0:
            md_file.write("| Час | Количество звонков | Доля |\n")
            md_file.write("|-----|-------------------|------|\n")
            for hour, count in hourly_stats.items():
                percentage = (count / len(df_period)) * 100 if len(df_period) > 0 else 0
                md_file.write(f"| {hour:02d}:00 - {hour:02d}:59 | {count} | {percentage:.1f}% |\n")
        
        # 12. Общие выводы и рекомендации
        md_file.write("\n## 📝 Выводы и рекомендации\n\n")
        
        # Определяем самого активного сотрудника
        most_active = top_initiators.index[0] if len(top_initiators) > 0 else "не определен"
        avg_call_duration_minutes = avg_duration / 60
        
        md_file.write("### Основные выводы:\n\n")
        md_file.write(f"1. **Самый активный сотрудник:** {most_active}\n")
        md_file.write(f"2. **Средняя длительность звонка:** {format_duration(avg_call_duration_minutes)}\n")
        
        # Считаем общий процент неудачных звонков
        total_failed_calls = len(df_period[df_period['Результат вызова конечного получателя'] != 'Соединение установлено'])
        failed_percentage = total_failed_calls/len(df_period)*100 if len(df_period) > 0 else 0
        md_file.write(f"3. **Доля неудачных звонков:** {failed_percentage:.1f}%\n")
        
        if len(hourly_stats) > 0:
            peak_hour = hourly_stats.idxmax()
            md_file.write(f"4. **Пик активности:** {peak_hour}:00 - {peak_hour}:59 ({hourly_stats.max()} звонков)\n")
        
        # Считаем среднее количество звонков в день
        avg_calls_per_day = len(df_period) / 23
        md_file.write(f"5. **Среднее количество звонков в день:** {avg_calls_per_day:.1f}\n")
        
        md_file.write("\n### Рекомендации:\n\n")
        if short_percentage > 20:
            md_file.write("⚠️ **Высокий процент коротких звонков** - рекомендуется проверить качество связи или провести обучение сотрудников\n")
        if failed_percentage > 30:
            md_file.write("⚠️ **Высокий процент неудачных звонков** - рекомендуется проанализировать причины сбоев\n")
        if avg_call_duration_minutes < 0.5:  # Менее 30 секунд
            md_file.write("⚠️ **Короткая средняя длительность звонков** - возможно, требуется улучшить процесс общения\n")
        if avg_calls_per_day < 10:
            md_file.write("⚠️ **Низкая активность звонков** - рекомендуется стимулировать коммуникацию между сотрудниками\n")
        
        md_file.write("\n---\n\n")
        md_file.write(f"*Отчет сгенерирован: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}*\n")
        md_file.write(f"*Источник данных: {os.path.basename(file_path)}*\n")
        md_file.write(f"*Период анализа: 21.01.2025 - 20.02.2025 (23 рабочих дня)*\n")
        md_file.write(f"*Uplink исключен из статистики*\n")
        
    print(f"✅ Отчет за период 21.01.2025-20.02.2025 успешно сохранен в файл: {output_path}")
    print(f"📊 Всего записей в отчете: {len(df_period)}")
    print(f"📅 Период: {start_date.strftime('%d.%m.%Y')} - {end_date.strftime('%d.%m.%Y')}")

if __name__ == "__main__":
    # Укажите путь к вашему файлу
    file_path = "docs/calls/calls.xlsx"
    
    # Проверяем, существует ли основной файл, если нет - ищем альтернативы
    if not os.path.exists(file_path):
        # Пробуем найти файл в текущей директории
        possible_files = ["calls.xlsx", "calls1.xlsx", "docs/calls/calls.xlsx"]
        for f in possible_files:
            if os.path.exists(f):
                file_path = f
                print(f"📁 Найден файл: {f}")
                break
    
    # Путь для сохранения отчета
    output_path = "docs/calls.md"
    
    # Проверяем, закрыт ли файл Excel
    try:
        analyze_calls(file_path, output_path)
    except PermissionError as e:
        print(f"❌ Ошибка доступа к файлу: {e}")
        print("⚠️  Закройте файл Excel и попробуйте снова")
    except Exception as e:
        print(f"❌ Ошибка: {e}")