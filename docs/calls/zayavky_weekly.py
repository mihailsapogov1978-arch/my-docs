import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os
import re
from openpyxl import load_workbook
from collections import defaultdict


def parse_excel_to_md(excel_path, md_path):
    """
    Парсит Excel файл с заявками и генерирует отчёт в Markdown
    с вкладками Неделя / Месяц / Год
    """
    try:
        wb = load_workbook(excel_path, data_only=True)
        ws = wb.active

        print(f"📊 Загружаем файл: {excel_path}")
        print(f"   Всего строк в файле: {ws.max_row}")

        header_row = None
        for i in range(1, min(10, ws.max_row + 1)):
            cell_value = ws.cell(row=i, column=1).value
            if cell_value in ['Номер', '№', 1, '1']:
                header_row = i
                print(f"✅ Найдены заголовки на строке {i}")
                break

        if header_row:
            df = pd.read_excel(excel_path, header=header_row - 1)
        else:
            df = pd.read_excel(excel_path, header=3)
            print("⚠️ Заголовки не найдены, используем строку 4")

        print(f"✅ Данные загружены. Строк: {len(df)}, Колонок: {len(df.columns)}")

    except Exception as e:
        print(f"❌ Ошибка при чтении файла: {e}")
        return False

    df.columns = [str(col).strip() for col in df.columns]

    # Сопоставляем колонки
    column_mapping = {}
    column_patterns = {
        'Номер': ['номер', '№', '1'],
        'Регистрация': ['регистрац', 'дата', '2'],
        'Активность': ['активность', 'обновл', '3'],
        'Заголовок': ['заголовок', 'тема', '4'],
        'Описание': ['описание', '5'],
        'Исполнитель': ['исполнитель', '7'],
        'Инициатор': ['инициатор', 'заявки', '3'],
        'Статус': ['статус', '6'],
        'Услуга': ['услуга', '9'],
        'Организация': ['организац', 'учрежден'],
    }

    print("\n🔍 Определяем колонки:")
    for col_name, patterns in column_patterns.items():
        for pattern in patterns:
            for df_col in df.columns:
                if pattern in str(df_col).lower():
                    column_mapping[col_name] = df_col
                    print(f"   • {col_name}: '{df_col}'")
                    break
            if col_name in column_mapping:
                break

    # ===== ПОДГОТОВКА ДАННЫХ =====
    total_requests = len(df)
    report_time = datetime.now().strftime("%d.%m.%Y %H:%M")

    today = datetime.now()
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(days=6)
    week_label = f"Неделя ({week_start.strftime('%d.%m')}–{week_end.strftime('%d.%m')})"

    months_ru_full = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
                      'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    month_label = f"{months_ru_full[today.month - 1]} {today.year}"
    year_label = f"{today.year} год"

    reg_col = column_mapping.get('Регистрация', df.columns[1])
    df['Регистрация_dt'] = pd.to_datetime(df[reg_col], errors='coerce', dayfirst=True)
    df['Год'] = df['Регистрация_dt'].dt.year
    df['Месяц'] = df['Регистрация_dt'].dt.month
    df['День'] = df['Регистрация_dt'].dt.day

    status_col = column_mapping.get('Статус')
    if status_col:
        df['Статус_clean'] = df[status_col].astype(str).str.strip()
    else:
        df['Статус_clean'] = 'Неизвестно'

    init_col = column_mapping.get('Инициатор')
    if init_col:
        init_series = df[init_col].dropna().astype(str).str.strip()
        initiator_counts_all = init_series.value_counts().to_dict()
    else:
        initiator_counts_all = {}

    # --- Недельная статистика ---
    week_ago = datetime.now() - timedelta(days=7)
    df_week = df[df['Регистрация_dt'] >= week_ago]
    week_total = len(df_week)

    week_status = {}
    if status_col and week_total > 0:
        week_status = df_week['Статус_clean'].value_counts().to_dict()

    week_initiators_all = {}
    if init_col and week_total > 0:
        week_init_series = df_week[init_col].dropna().astype(str).str.strip()
        week_initiators_all = week_init_series.value_counts().to_dict()

    # --- Месячная статистика ---
    month_ago = datetime.now() - timedelta(days=30)
    df_month = df[df['Регистрация_dt'] >= month_ago]
    month_total = len(df_month)

    month_status = {}
    if status_col and month_total > 0:
        month_status = df_month['Статус_clean'].value_counts().to_dict()

    month_initiators_all = {}
    if init_col and month_total > 0:
        month_init_series = df_month[init_col].dropna().astype(str).str.strip()
        month_initiators_all = month_init_series.value_counts().to_dict()

    # --- Годовая статистика ---
    year_total = total_requests

    year_status = {}
    if status_col:
        year_status = df['Статус_clean'].value_counts().to_dict()

    year_initiators_all = {}
    if init_col:
        year_init_series = df[init_col].dropna().astype(str).str.strip()
        year_initiators_all = year_init_series.value_counts().to_dict()

    month_stats = {}
    for month in range(1, 13):
        month_data = df[df['Месяц'] == month]
        if len(month_data) > 0:
            resolved_count = len(month_data[month_data['Статус_clean'].str.contains('Решено|Закрыто', case=False, na=False)])
            month_stats[month] = {
                'total': len(month_data),
                'resolved': resolved_count
            }

    # ===== ФУНКЦИИ ДЛЯ ГЕНЕРАЦИИ HTML =====
    def build_table(headers, rows, nowrap_cols=None):
        html = '<table style="width:100%; border-collapse:collapse; margin:6px 0;">'
        html += '<thead><tr style="background-color:#f0f2f5;">'
        for i, h in enumerate(headers):
            html += f'<th style="padding:6px 12px; border:1px solid #dee2e6; text-align:left; font-size:14px;">{h}</th>'
        html += '</tr></thead><tbody>'
        for row in rows:
            html += '<tr>'
            for i, cell in enumerate(row):
                if nowrap_cols and i in nowrap_cols:
                    html += f'<td style="padding:4px 12px; border:1px solid #dee2e6; font-size:14px; white-space:nowrap;">{cell}</td>'
                else:
                    html += f'<td style="padding:4px 12px; border:1px solid #dee2e6; font-size:14px;">{cell}</td>'
            html += '</tr>'
        html += '</tbody></table>'
        return html

    def get_status_rows(status_dict):
        rows = []
        if status_dict:
            for status, count in sorted(status_dict.items(), key=lambda x: x[1], reverse=True):
                rows.append([status, str(count)])
        else:
            rows.append(["Нет данных", "0"])
        return rows

    def get_initiator_rows(initiator_dict):
        rows = []
        if initiator_dict:
            for initiator, count in sorted(initiator_dict.items(), key=lambda x: x[1], reverse=True):
                display_name = str(initiator)[:35] + ('...' if len(str(initiator)) > 35 else '')
                rows.append([display_name, str(count)])
        else:
            rows.append(["Нет данных", "0"])
        return rows

    def build_two_column_tables(init_html, status_html, summary_html=None):
        html = '<table style="width:100%; border-collapse:collapse; border:none; margin:8px 0;">'
        html += '<tr>'
        html += f'<td style="width:55%; vertical-align:top; padding-right:20px; border:none;"><strong>Инициаторы</strong>{init_html}</td>'
        html += '<td style="width:45%; vertical-align:top; padding-left:20px; border:none;">'
        html += f'<strong>Статусы</strong>{status_html}'
        if summary_html:
            html += f'<div style="margin-top:16px;"><strong>Итоги</strong>{summary_html}</div>'
        html += '</td>'
        html += '</tr>'
        html += '</table>'
        return html

    # ===== ГЕНЕРАЦИЯ HTML-СОДЕРЖИМОГО =====
    # Неделя
    week_status_rows = get_status_rows(week_status)
    week_status_html = build_table(['Статус', 'Кол-во'], week_status_rows)
    week_init_rows = get_initiator_rows(week_initiators_all)
    week_init_html = build_table(['Инициатор', 'Заявок'], week_init_rows, nowrap_cols=[0])
    
    week_summary_rows = [['Неделя', str(week_total)]]
    week_summary_html = build_table(['Период', 'Заявок'], week_summary_rows)
    
    week_two_col = build_two_column_tables(week_init_html, week_status_html, week_summary_html)

    # Месяц
    month_status_rows = get_status_rows(month_status)
    month_status_html = build_table(['Статус', 'Кол-во'], month_status_rows)
    month_init_rows = get_initiator_rows(month_initiators_all)
    month_init_html = build_table(['Инициатор', 'Заявок'], month_init_rows, nowrap_cols=[0])
    
    month_summary_rows = [['Месяц', str(month_total)]]
    month_summary_html = build_table(['Период', 'Заявок'], month_summary_rows)
    
    month_two_col = build_two_column_tables(month_init_html, month_status_html, month_summary_html)

    # Год: месяцы
    month_rows = []
    months_ru_short = ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн',
                       'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек']
    for month in range(1, 13):
        stats = month_stats.get(month, {'total': 0, 'resolved': 0})
        percent = round((stats['resolved'] / stats['total'] * 100), 1) if stats['total'] > 0 else 0
        month_rows.append([months_ru_short[month-1], str(stats['total']), str(stats['resolved']), f"{percent}%"])
    month_table_html = build_table(['Месяц', 'Всего', 'Решено', '%'], month_rows)

    # Год: статусы + инициаторы + итоги
    year_status_rows = get_status_rows(year_status)
    year_status_html = build_table(['Статус', 'Кол-во'], year_status_rows)
    year_init_rows = get_initiator_rows(year_initiators_all)
    year_init_html = build_table(['Инициатор', 'Заявок'], year_init_rows, nowrap_cols=[0])
    
    year_summary_rows = [['Год', str(year_total)]]
    year_summary_html = build_table(['Период', 'Заявок'], year_summary_rows)
    
    year_two_col = build_two_column_tables(year_init_html, year_status_html, year_summary_html)

    # ===== СБОРКА ИТОГОВОГО MD =====
    md_content = f"""# 📊 Отчет по заявкам

**📅 Дата:** {report_time}  
**📦 Всего заявок:** {total_requests}

---

<div style="display:flex; gap:4px; margin-bottom:16px; border-bottom:2px solid #e2e8f0; padding-bottom:0;">

<style>
.tab-btn {{
    padding:10px 24px;
    border:1px solid #e2e8f0;
    border-bottom:3px solid transparent;
    border-radius:8px 8px 0 0;
    cursor:pointer;
    font-weight:400;
    font-size:15px;
    color:#4a5568;
    background:#f7fafc;
    transition:all 0.2s ease;
    margin-bottom:-2px;
    text-decoration:none;
    display:inline-block;
}}
.tab-btn:hover {{
    background:#edf2f7;
    text-decoration:none;
}}
.tab-btn.active {{
    background:#ffffff;
    border-bottom:3px solid #2b6cb0;
    color:#2b6cb0;
}}
.tab-content {{
    display:block;
    padding:16px 0;
}}
</style>

<button class="tab-btn active" onclick="showTab('week')">📅 {week_label}</button>
<button class="tab-btn" onclick="showTab('month')">📆 {month_label}</button>
<button class="tab-btn" onclick="showTab('year')">📊 {year_label}</button>
</div>

<div id="week" class="tab-content">
    **📈 За неделю:** {week_total} заявок
    {week_two_col}
</div>

<div id="month" class="tab-content" style="display:none;">
    **📈 За месяц:** {month_total} заявок
    {month_two_col}
</div>

<div id="year" class="tab-content" style="display:none;">
    **📈 За год:** {year_total} заявок

    <strong>По месяцам</strong>
    {month_table_html}

    {year_two_col}
</div>

<script>
function showTab(tabId) {{
    var contents = document.querySelectorAll('.tab-content');
    contents.forEach(function(el) {{
        el.style.display = 'none';
    }});
    var selected = document.getElementById(tabId);
    if (selected) selected.style.display = 'block';
    
    var btns = document.querySelectorAll('.tab-btn');
    btns.forEach(function(el) {{
        el.classList.remove('active');
    }});
    var activeBtn = document.querySelector('.tab-btn[onclick*="' + tabId + '"]');
    if (activeBtn) activeBtn.classList.add('active');
}}
</script>
"""

    # Сохраняем файл
    output_dir = os.path.dirname(md_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)

    print(f"\n✅ Отчет успешно создан: {md_path}")
    print(f"📊 Всего заявок: {total_requests}")
    print(f"📅 За неделю: {week_total}")
    print(f"📅 За месяц: {month_total}")
    print(f"📅 За год: {year_total}")

    return True


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))

    excel_file = os.path.join(script_dir, "2026829_РеестрЗаявок31103.xlsx")

    if not os.path.exists(excel_file):
        for f in os.listdir(script_dir):
            if f.endswith('.xlsx') and ('заявк' in f.lower() or 'реестр' in f.lower()):
                excel_file = os.path.join(script_dir, f)
                break

    md_file = os.path.join(script_dir, "zayavky.md")

    print("=" * 60)
    print("📋 ГЕНЕРАЦИЯ ОТЧЕТА ПО ЗАЯВКАМ (Неделя / Месяц / Год)")
    print("=" * 60)

    if excel_file and os.path.exists(excel_file):
        print(f"📁 Найден файл: {os.path.basename(excel_file)}")
        parse_excel_to_md(excel_file, md_file)
    else:
        print("❌ Файл с заявками не найден!")
        print("   Поместите файл '2026829_РеестрЗаявок31103.xlsx' в папку со скриптом.")