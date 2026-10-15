#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Генератор страницы MkDocs "Отчёты отдела СРТП".

Два источника задач:
  1) docs/_daily/YYYY-MM/*.md — ежедневные заметки (приоритет);
  2) reports_src/*.xlsx, лист «Количественная аналитика» — fallback,
     оттуда же всегда берутся звонки.

Сборка:
    python3 make_report.py              # по всем xlsx из reports_src/
    python3 make_report.py 2026 10      # только за октябрь 2026, источник — _daily/

Каждый месяц = один H2 (правый TOC).
Сотрудники без задач в отчёт не попадают.
"""
import os
import re
import sys
import glob
import html
from datetime import datetime

from openpyxl import load_workbook

MONTHS_RU = {
    'январь': 1, 'февраль': 2, 'март': 3, 'апрель': 4, 'май': 5, 'июнь': 6,
    'июль': 7, 'август': 8, 'сентябрь': 9, 'октябрь': 10, 'ноябрь': 11, 'декабрь': 12,
}
MONTHS_RU_NOM = {
    1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь',
    7: 'Июль', 8: 'Август', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь',
}

SHEET_NAME = 'Количественная аналитика'
SRC_DIR = 'reports_src'
DAILY_DIR = os.path.join('docs', '_daily')
OUT_PATH = os.path.join('docs', 'reports', 'index.md')
COUNTERS_COL = 10  # столбец J (1-based)

SKIP_TASKS = {
    'текущие задачи', 'исполнитель', 'работа с заявками',
    'текущая задача', 'задачи', 'мероприятие',
}


def esc(v):
    if v is None:
        return ''
    return html.escape(str(v)).replace('\n', '<br>')


def detect_month(xlsx_path):
    base = os.path.basename(xlsx_path).lower()
    m = None
    for name, num in MONTHS_RU.items():
        if name in base:
            m = num
            break
    y = re.search(r'(20\d{2})', base)
    year = int(y.group(1)) if y else datetime.now().year
    month = m or datetime.now().month
    return year, month


# =====================  EXCEL  =====================
def find_month_row(ws, year, month):
    month_name = MONTHS_RU_NOM[month].lower()
    for r in range(1, ws.max_row + 1):
        a = ws.cell(row=r, column=1).value
        if not a:
            continue
        s = str(a).lower()
        if month_name in s and str(year) in s:
            return r
    last = None
    for r in range(1, ws.max_row + 1):
        a = ws.cell(row=r, column=1).value
        if not a:
            continue
        if month_name in str(a).lower():
            last = r
    return last


def extract_calls(ws, year, month):
    employees = []
    col = 3
    while True:
        v = ws.cell(row=2, column=col).value
        if not v:
            break
        name = str(v).strip()
        if name.lower().startswith('работа'):
            break
        employees.append((col, name))
        col += 1

    row_num = find_month_row(ws, year, month)
    if row_num is None:
        return []

    result = []
    for col, name in employees:
        v = ws.cell(row=row_num, column=col).value
        try:
            v = int(v) if v is not None else 0
        except (TypeError, ValueError):
            v = 0
        result.append((name, v))
    return result


def parse_counters(raw):
    if not raw:
        return {}
    s = str(raw)
    counters = {}

    m = re.search(r'резолюц\w*\s*[-–—:]\s*(\d+)', s, re.IGNORECASE)
    if m:
        counters['resolutions'] = int(m.group(1))

    m = re.search(r'в\s+работе\s*[-–—:]\s*(\d+)', s, re.IGNORECASE)
    if m:
        counters['resolutions_inwork'] = int(m.group(1))

    m = re.search(r'заявок[^\d]*?[-–—:]\s*(\d+)', s, re.IGNORECASE)
    if m:
        counters['tickets'] = int(m.group(1))

    return counters


def extract_employees(ws):
    emp_row = None
    for r in range(1, ws.max_row + 1):
        v = ws.cell(row=r, column=1).value
        if v and str(v).strip().lower() == 'исполнитель':
            emp_row = r
            break
    if emp_row is None:
        return []

    employees = []
    r = emp_row + 1
    while r <= ws.max_row:
        name_cell = ws.cell(row=r, column=1).value
        name = str(name_cell).strip() if name_cell else ''

        if not name:
            r += 1
            continue

        if name.startswith('=') or name.lower() in SKIP_TASKS:
            r += 1
            continue

        raw_tasks = ws.cell(row=r, column=2).value
        tasks = []
        if raw_tasks:
            for line in str(raw_tasks).split('\n'):
                s = line.strip()
                if not s:
                    continue
                if s.lower() in SKIP_TASKS:
                    continue
                s = re.sub(r'^\d+[\.\)]\s*', '', s)
                s = re.sub(r'^[-–—]\s*', '', s)
                tasks.append(s)

        counters = {}
        raw_counters = ws.cell(row=r, column=COUNTERS_COL).value
        if raw_counters:
            counters = parse_counters(raw_counters)

        employees.append({
            'name': name,
            'tasks': tasks,
            'tickets': counters.get('tickets'),
            'resolutions': counters.get('resolutions'),
        })
        r += 1

    return employees


# =====================  DAILY  =====================
def parse_daily_file(path):
    if not os.path.exists(path):
        return []

    with open(path, 'r', encoding='utf-8') as f:
        lines = f.read().split('\n')

    entries = []
    cur_date = None

    for line in lines:
        s = line.rstrip()

        m = re.match(r'^##\s+(\d{4}-\d{2}-\d{2})\s*$', s)
        if m:
            cur_date = m.group(1)
            continue

        m = re.match(r'^\s*[-*]\s+(.*)$', s)
        if m and cur_date:
            item = m.group(1).strip()
            if item and item.lower() not in SKIP_TASKS:
                entries.append((cur_date, item))

    return entries


def load_daily_for_month(year, month):
    folder = os.path.join(DAILY_DIR, f'{year}-{month:02d}')
    if not os.path.isdir(folder):
        return {}

    result = {}
    for fname in sorted(os.listdir(folder)):
        if not fname.lower().endswith('.md'):
            continue
        name = os.path.splitext(fname)[0]
        entries = parse_daily_file(os.path.join(folder, fname))
        if entries:
            result[name] = entries
    return result


# =====================  RENDER  =====================
def render_employees(calls, employees):
    """Одна строка на сотрудника, всё в виде обычной HTML-таблицы."""
    calls_map = {name: v for name, v in calls}

    employees = [e for e in employees if e['tasks']]
    if not employees:
        return ''

    total_calls = sum(calls_map.get(e['name'], 0) for e in employees)
    total_tasks = sum(len(e['tasks']) for e in employees)
    total_tickets = sum(e['tickets'] for e in employees if e.get('tickets') is not None)
    total_resolutions = sum(e['resolutions'] for e in employees if e.get('resolutions') is not None)

    L = []
    L.append('<table class="report-table">')
    L.append('  <thead>')
    L.append('    <tr>')
    L.append('      <th style="width:240px;">Сотрудник</th>')
    L.append('      <th style="width:110px;">Звонков</th>')
    L.append('      <th style="width:110px;">Заявок</th>')
    L.append('      <th style="width:110px;">Задач</th>')
    L.append('      <th style="width:120px;">Резолюций</th>')
    L.append('    </tr>')
    L.append('  </thead>')
    L.append('  <tbody>')

    # Первая строка — сводка отдела
    L.append('    <tr class="report-summary-row">')
    L.append(f'      <td><b>Отдел СРТП</b><br><small>Сотрудников: {len(employees)}</small></td>')
    L.append(f'      <td><b>{total_calls}</b></td>')
    L.append(f'      <td><b>{total_tickets}</b></td>')
    L.append(f'      <td><b>{total_tasks}</b></td>')
    L.append(f'      <td><b>{total_resolutions}</b></td>')
    L.append('    </tr>')

    # Строки сотрудников
    for idx, e in enumerate(employees, start=1):
        name = e['name']
        calls_val = calls_map.get(name, 0)
        n_tasks = len(e['tasks'])
        tickets = e.get('tickets')
        resolutions = e.get('resolutions')

        full_list = ''.join(f'<li>{esc(t)}</li>' for t in e['tasks'])

        # Основная строка сотрудника — кликабельная ячейка имени
        L.append(f'    <tr class="report-row" data-emp="{idx}">')
        L.append('      <td class="report-name" onclick="toggleReportRow(this)">')
        L.append(f'        <span class="report-toggle">›</span>')
        L.append(f'        {esc(name)}')
        L.append('      </td>')
        L.append(f'      <td class="report-num">{calls_val}</td>')
        L.append(f'      <td class="report-num">{tickets if tickets is not None else "—"}</td>')
        L.append(f'      <td class="report-num">{n_tasks}</td>')
        L.append(f'      <td class="report-num">{resolutions if resolutions is not None else "—"}</td>')
        L.append('    </tr>')

        # Скрытая строка с задачами
        L.append(f'    <tr class="report-tasks-row" style="display:none;">')
        L.append(f'      <td colspan="5">')
        L.append(f'        <ul class="report-tasks">{full_list}</ul>')
        L.append('      </td>')
        L.append('    </tr>')

    L.append('  </tbody>')
    L.append('</table>')

    return '\n'.join(L)


STYLES = '''<style>
/* ===== Таблица отчёта ===== */
.report-table {
    width: 100%;
    border-collapse: collapse;
    background: #fff;
    border: 1px solid #e0e4e8;
    border-radius: 8px;
    overflow: hidden;
    margin: 16px 0 28px 0;
    table-layout: fixed;
}
.report-table thead th {
    background: #f5f7fa;
    color: #2c3e50;
    text-align: left;
    font-weight: 600;
    font-size: 14px;
    padding: 10px 14px;
    border-bottom: 1px solid #e0e4e8;
    white-space: nowrap;
}
.report-table tbody td {
    padding: 10px 14px;
    border-bottom: 1px solid #eef2f6;
    vertical-align: middle;
    color: #2d3748;
    font-size: 14px;
}
.report-table tbody tr:last-child td { border-bottom: none; }

/* Сводная строка отдела */
.report-summary-row td {
    background: #fafbfc;
    font-weight: 600;
    color: #2c3e50;
    border-bottom: 2px solid #e0e4e8;
}
.report-summary-row small {
    display: block;
    color: #718096;
    font-weight: 400;
    font-size: 12.5px;
    margin-top: 2px;
}

/* Кликабельная ячейка имени */
.report-name {
    cursor: pointer;
    user-select: none;
}
.report-name:hover {
    color: #2b6cb0;
}

/* Маркер раскрытия */
.report-toggle {
    display: inline-block;
    color: #718096;
    font-size: 15px;
    font-weight: 700;
    margin-right: 6px;
    transition: transform 0.15s;
}
.report-toggle.open {
    transform: rotate(90deg);
}

.report-num {
    text-align: left;
    white-space: nowrap;
}

/* Подсветка раскрытой строки сотрудника */
.report-row.open td {
    background: #eaf4ff;
    border-bottom-color: #bee3f8;
}
.report-row.open td:first-child {
    box-shadow: inset 3px 0 0 #3182ce;
}
.report-row.open:hover td {
    background: #e1efff;
}

/* Строка с раскрытыми задачами */
.report-tasks-row > td {
    background: #fafbfc;
    padding: 10px 14px 14px 46px;
    border-bottom: 1px solid #eef2f6;
}
.report-tasks {
    margin: 0;
    padding-left: 18px;
    font-size: 14px;
    line-height: 1.55;
    color: #2d3748;
    font-weight: 400;
}
.report-tasks li { margin-bottom: 4px; }

@media (max-width: 720px) {
    .report-table thead th,
    .report-table tbody td { padding: 8px 8px; }
}
</style>'''


# =====================  BUILD  =====================
def build_month_section(xlsx_path):
    year, month = detect_month(xlsx_path)

    daily = load_daily_for_month(year, month)

    calls = []
    employees_from_excel = []
    try:
        wb = load_workbook(xlsx_path, data_only=True)
        if SHEET_NAME in wb.sheetnames:
            ws = wb[SHEET_NAME]
            calls = extract_calls(ws, year, month)
            employees_from_excel = extract_employees(ws)
    except Exception as e:
        print(f'  ⚠️  Не удалось открыть {xlsx_path}: {e}')

    if daily:
        employees = []
        for name, items in daily.items():
            employees.append({
                'name': name,
                'tasks': [it for _, it in items],
                'tickets': None,
                'resolutions': None,
            })
        print(f'  ℹ️  Источник задач: _daily/{year}-{month:02d}/ ({len(employees)} сотрудников)')
    else:
        employees = employees_from_excel
        if employees:
            print(f'  ℹ️  Источник задач: Excel (fallback)')

    month_label = f'{MONTHS_RU_NOM[month]} {year}'
    parts = [f'## {month_label}', '']

    html_block = render_employees(calls, employees)
    if not html_block:
        parts.append(f'*Данные за {month_label.lower()} не найдены.*')
        parts.append('')
        return year, month, '\n'.join(parts)

    parts.append(html_block)
    parts.append('')
    return year, month, '\n'.join(parts)


def build_month_section_only_daily(year, month):
    daily = load_daily_for_month(year, month)
    if not daily:
        print(f'  ⚠️  Нет заметок за {year}-{month:02d}')
        return None

    employees = []
    for name, items in daily.items():
        employees.append({
            'name': name,
            'tasks': [it for _, it in items],
            'tickets': None,
            'resolutions': None,
        })

    month_label = f'{MONTHS_RU_NOM[month]} {year}'
    parts = [f'## {month_label}', '', render_employees([], employees), '']
    print(f'  ℹ️  Источник задач: _daily/{year}-{month:02d}/ ({len(employees)} сотрудников)')
    return year, month, '\n'.join(parts)


# =====================  MAIN  =====================
def main():
    sections = []

    # Режим: python3 make_report.py 2026 10  → только daily за октябрь
    if len(sys.argv) == 3 and sys.argv[1].isdigit() and sys.argv[2].isdigit():
        year, month = int(sys.argv[1]), int(sys.argv[2])
        print(f'Сборка только daily за {year}-{month:02d}')
        res = build_month_section_only_daily(year, month)
        if res:
            sections.append(res)
    else:
        if len(sys.argv) > 1:
            files = [sys.argv[1]]
        else:
            files = sorted(glob.glob(os.path.join(SRC_DIR, '*.xlsx')))

        if not files:
            print('Нет .xlsx-файлов. Положите их в reports_src/ или укажите файл аргументом.')
            sys.exit(1)

        for f in files:
            print(f'Обрабатываю: {f}')
            res = build_month_section(f)
            if res:
                sections.append(res)

    if not sections:
        print('Не удалось собрать ни одного отчёта.')
        sys.exit(1)

    sections.sort(key=lambda t: (t[0], t[1]), reverse=True)

    out = [STYLES, '', '# Отчёты отдела СРТП', '']
    for _, _, text in sections:
        out.append(text)
        out.append('')

    # Один <script> на всю страницу — работает во всех месячных таблицах
    out.append('''<script>
function toggleReportRow(cell) {
    var tr = cell.closest('tr');
    if (!tr) return;
    var next = tr.nextElementSibling;
    var tog = cell.querySelector('.report-toggle');
    if (!next || !next.classList.contains('report-tasks-row')) return;

    if (next.style.display === 'none') {
        next.style.display = '';
        tr.classList.add('open');
        if (tog) tog.classList.add('open');
    } else {
        next.style.display = 'none';
        tr.classList.remove('open');
        if (tog) tog.classList.remove('open');
    }
}
</script>''')
    out.append('')

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(out))

    print(f'✅ Готово: {OUT_PATH}')
    print(f'   Отчётов: {len(sections)}')


if __name__ == '__main__':
    main()