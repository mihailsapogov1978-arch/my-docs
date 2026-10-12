#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Генератор:
  - docs/index.md      — дашборд на главной
  - docs/calendar.md   — календарь ключевых дат

Источники данных:
  - statuses.json                       (roadmap: сроки, статусы, детализация)
  - docs/reports/YYYY-MM.md             (готовые отчёты — для плитки «Последний отчёт»)
  - docs/calls/calls.md                 (статистика звонков — для плитки «Звонки»)
  - docs/_calendar/events.json          (жёсткие даты: отчётность, ВКС, окончание контрактов)
  - docs/projects_2026/roadmap.md       (мероприятия — сроки, статусы)
  - docs/Contracts/svod_gk.md           (контракты за текущий год)

Запуск:
    python3 make_dashboard.py
"""
import json
import os
import re
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATUS_FILE = os.path.join(BASE_DIR, 'statuses.json')
CALENDAR_FILE = os.path.join(BASE_DIR, 'docs', '_calendar', 'events.json')
ROADMAP_MD = os.path.join(BASE_DIR, 'docs', 'projects_2026', 'roadmap.md')
CALLS_MD = os.path.join(BASE_DIR, 'docs', 'calls', 'calls.md')
REPORTS_DIR = os.path.join(BASE_DIR, 'docs', 'reports')
SVOD_GK_MD = os.path.join(BASE_DIR, 'docs', 'Contracts', 'svod_gk.md')
INDEX_OUT = os.path.join(BASE_DIR, 'docs', 'index.md')
CALENDAR_OUT = os.path.join(BASE_DIR, 'docs', 'calendar.md')

MONTHS_RU = {
    1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая', 6: 'июня',
    7: 'июля', 8: 'августа', 9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря',
}


# =====================  ЗАГРУЗКА ДАННЫХ  =====================
def load_statuses():
    if not os.path.exists(STATUS_FILE):
        return {}
    try:
        with open(STATUS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {}


def load_calendar_events():
    if not os.path.exists(CALENDAR_FILE):
        return []
    try:
        with open(CALENDAR_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return data.get('events', [])
    except Exception:
        return []


def parse_roadmap_events():
    """
    Из roadmap.md вытаскиваем мероприятия: key, name, status, deadline.
    """
    if not os.path.exists(ROADMAP_MD):
        return []

    with open(ROADMAP_MD, 'r', encoding='utf-8') as f:
        content = f.read()

    events = []
    pattern = re.compile(
        r'<tr\s+class="main-row"\s+data-key="(\d+)"\s+data-status="([^"]*)"\s+data-deadline="([^"]*)"[^>]*>(.*?)</tr>',
        re.DOTALL
    )
    for m in pattern.finditer(content):
        key, status, deadline, body = m.group(1), m.group(2), m.group(3), m.group(4)
        name_m = re.search(r'<td[^>]*class="meropriyatie-cell"[^>]*>(.*?)<span', body, re.DOTALL)
        name = ''
        if name_m:
            name = re.sub(r'<[^>]+>', '', name_m.group(1)).strip()
        events.append({
            'key': int(key),
            'name': name,
            'status': status,
            'deadline': deadline or '',
            'source': 'roadmap',
        })
    return events


def parse_reports_months():
    """
    Список месяцев вида ['2026-09', ...], для которых есть готовый отчёт
    в docs/reports/YYYY-MM.md.
    """
    if not os.path.isdir(REPORTS_DIR):
        return []
    months = []
    for name in os.listdir(REPORTS_DIR):
        m = re.match(r'^(\d{4})-(\d{2})\.md$', name)
        if m:
            months.append(f'{m.group(1)}-{m.group(2)}')
    return sorted(months)


def parse_calls_totals():
    """
    Читает docs/calls/calls.md, извлекает:
      - месяц и год из заголовка «Статистика звонков за <месяц> <год>»;
      - суммарные значения из блока .calls-total.
    """
    if not os.path.exists(CALLS_MD):
        return None

    with open(CALLS_MD, 'r', encoding='utf-8') as f:
        content = f.read()

    month_ru = None
    year = None
    m = re.search(r'#\s+Статистика звонков за\s+([А-Яа-яЁё]+)\s+(\d{4})', content)
    if m:
        month_ru = m.group(1).strip().lower()
        year = int(m.group(2))

    incoming = missed = outgoing = None

    m_in = re.search(r'class="ct-cell ct-in"[^>]*>.*?class="ct-value"[^>]*>(\d+)', content, re.DOTALL)
    if m_in:
        incoming = int(m_in.group(1))

    m_miss = re.search(r'class="ct-cell ct-miss"[^>]*>.*?class="ct-value"[^>]*>(\d+)', content, re.DOTALL)
    if m_miss:
        missed = int(m_miss.group(1))

    m_out = re.search(r'class="ct-cell ct-out"[^>]*>.*?class="ct-value"[^>]*>(\d+)', content, re.DOTALL)
    if m_out:
        outgoing = int(m_out.group(1))

    if incoming is None and missed is None and outgoing is None:
        return None

    return {
        'month_ru': month_ru,
        'year': year,
        'incoming': incoming or 0,
        'missed': missed or 0,
        'outgoing': outgoing or 0,
    }


def parse_contracts_2026():
    """
    Берёт число контрактов и сумму за текущий год из блока «Общая статистика»
    в docs/Contracts/svod_gk.md.

    Формат строки:
      <tr>
        <td ...>2026</td>
        <td ...>8</td>
        <td ...>75 936 750,00</td>
      </tr>

    Возвращает (count, sum_str) или (None, None), если не нашёл.
    """
    year = datetime.now().year

    if not os.path.exists(SVOD_GK_MD):
        return None, None

    try:
        with open(SVOD_GK_MD, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return None, None

    # Ищем все <tr>...</tr>, внутри — три <td> с годом, количеством и суммой
    for tr in re.findall(r'<tr\b.*?</tr>', content, re.DOTALL | re.IGNORECASE):
        m = re.search(
            r'<td[^>]*>\s*(\d{4})\s*</td>\s*'
            r'<td[^>]*>\s*(\d+)\s*</td>\s*'
            r'<td[^>]*>\s*([\d\s\u00a0]+,\d{2})\s*</td>',
            tr, re.DOTALL
        )
        if m and int(m.group(1)) == year:
            return int(m.group(2)), m.group(3).strip()

    return None, None


# =====================  ЛОГИКА  =====================
STATUS_LABEL = {
    'postanovka':   'Постановка задачи',
    'soglasovanie': 'Согласование ТЗ',
    'torgi':        'Торги',
    'raboty':       'Работы по ГК',
    'done':         'Выполнено',
}


def classify_deadline(deadline_str, today):
    """'overdue' / 'soon' (≤7) / 'near' (≤30) / 'far' / ''."""
    if not deadline_str:
        return ''
    try:
        d = datetime.strptime(deadline_str, '%Y-%m-%d').date()
    except ValueError:
        return ''
    delta = (d - today).days
    if delta < 0:
        return 'overdue'
    if delta <= 7:
        return 'soon'
    if delta <= 30:
        return 'near'
    return 'far'


def human_date(dt):
    return f'{dt.day:02d} {MONTHS_RU[dt.month]} {dt.year}'


# =====================  DASHBOARD  =====================
DASHBOARD_STYLE = '''<style>
.dash-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 14px;
    margin: 20px 0 30px 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}
.dash-card {
    display: block;
    background: #fff;
    border: 1px solid #e2e8f0;
    border-left: 4px solid #2b6cb0;
    border-radius: 10px;
    padding: 16px 18px;
    text-decoration: none !important;
    color: inherit !important;
    transition: box-shadow 0.15s, transform 0.15s;
}
.dash-card:hover {
    box-shadow: 0 4px 14px rgba(43, 108, 176, 0.10);
    transform: translateY(-1px);
}
.dash-card .dc-label {
    font-size: 11.5px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #718096;
    font-weight: 700;
    margin-bottom: 8px;
}
.dash-card .dc-value {
    font-size: 28px;
    font-weight: 700;
    color: #2c3e50;
    line-height: 1.1;
    margin-bottom: 6px;
}
.dash-card .dc-value.dc-good { color: #2f855a; }
.dash-card .dc-value.dc-warn { color: #b7791f; }
.dash-card .dc-value.dc-bad  { color: #c53030; }
.dash-card .dc-sub {
    font-size: 12.5px;
    color: #4a5568;
    font-weight: 500;
    line-height: 1.4;
}
.dash-card.dc-done    { border-left-color: #38a169; }
.dash-card.dc-work    { border-left-color: #e6b800; }
.dash-card.dc-late    { border-left-color: #e53e3e; }
.dash-card.dc-neutral { border-left-color: #805ad5; }
.dash-card.dc-info    { border-left-color: #3182ce; }

.attn-table {
    width: 100%;
    border-collapse: collapse;
    background: #fff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    overflow: hidden;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 13.5px;
    margin: 12px 0 24px 0;
}
.attn-table th {
    background: #f5f7fa;
    color: #2c3e50;
    font-weight: 600;
    text-align: left;
    padding: 10px 14px;
    border-bottom: 1px solid #e2e8f0;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 0.03em;
}
.attn-table td {
    padding: 10px 14px;
    border-bottom: 1px solid #eef2f6;
    vertical-align: middle;
}
.attn-table tr:last-child td { border-bottom: none; }
.attn-table .at-deadline { white-space: nowrap; font-weight: 700; }
.attn-table .at-deadline.overdue { color: #c53030; }
.attn-table .at-deadline.soon    { color: #b7791f; }
.attn-table .at-deadline.near    { color: #2b6cb0; }

.attn-empty {
    padding: 14px 18px;
    background: #f0fff4;
    border: 1px solid #c6f6d5;
    border-radius: 8px;
    color: #276749;
    font-size: 13.5px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}
</style>'''


def render_dashboard(statuses, roadmap_events, contracts_count, contracts_sum,
                     reports_months, calls_totals):
    today = datetime.now().date()

    saved_statuses = statuses.get('statuses', {})
    saved_deadlines = statuses.get('deadlines', {})

    total = 0
    done = 0
    work = 0
    late = 0
    upcoming = []

    for ev in roadmap_events:
        key = str(ev['key'])
        if key in saved_statuses:
            ev['status'] = saved_statuses[key]
        if key in saved_deadlines:
            ev['deadline'] = saved_deadlines[key]

        total += 1
        if ev['status'] == 'done':
            done += 1

        kind = classify_deadline(ev['deadline'], today)
        if ev['status'] != 'done':
            work += 1
            if kind == 'overdue':
                late += 1
            if kind in ('overdue', 'soon', 'near'):
                upcoming.append({
                    'name': ev['name'],
                    'deadline': ev['deadline'],
                    'kind': kind,
                    'status': ev['status'],
                })

    def sort_key(item):
        try:
            d = datetime.strptime(item['deadline'], '%Y-%m-%d').date()
        except ValueError:
            d = datetime.max.date()
        return (0 if item['kind'] == 'overdue' else 1, d)

    upcoming.sort(key=sort_key)

    last_report_month = None
    if reports_months:
        last_report_month = sorted(reports_months, reverse=True)[0]

    year = today.year

    parts = []
    parts.append(DASHBOARD_STYLE)
    parts.append('')
    parts.append('# Дашборд')
    parts.append('')
    parts.append(f'*Обновлено: {human_date(today)}*')
    parts.append('')

    # ==== Плитки ====
    parts.append('<div class="dash-grid">')

    # Мероприятия
    parts.append(f'''<a class="dash-card dc-info" href="projects_2026/roadmap/">
    <div class="dc-label">Мероприятия 2026</div>
    <div class="dc-value">{total}</div>
    <div class="dc-sub">в работе {work} · выполнено {done}</div>
</a>''')

    # Просрочено
    dc_cls = 'dc-bad' if late > 0 else 'dc-good'
    parts.append(f'''<a class="dash-card {'dc-late' if late else 'dc-done'}" href="calendar/">
    <div class="dc-label">Просрочено</div>
    <div class="dc-value {dc_cls}">{late}</div>
    <div class="dc-sub">{'требует внимания' if late else 'нет просроченных'}</div>
</a>''')

    # Готово
    parts.append(f'''<a class="dash-card dc-done" href="projects_2026/roadmap/">
    <div class="dc-label">Готово</div>
    <div class="dc-value dc-good">{done}</div>
    <div class="dc-sub">из {total} мероприятий</div>
</a>''')

    # Контракты за текущий год
    if contracts_count is not None:
        count_display = str(contracts_count)
        if contracts_sum:
            sub_text = f'на сумму {contracts_sum} ₽'
        else:
            sub_text = 'по данным реестра контрактов'
    else:
        count_display = '—'
        sub_text = 'по данным реестра контрактов'

    parts.append(f'''<a class="dash-card dc-neutral" href="Contracts/svod_gk/">
    <div class="dc-label">Заключено контрактов за {year} год</div>
    <div class="dc-value">{count_display}</div>
    <div class="dc-sub">{sub_text}</div>
</a>''')

    # Последний отчёт
    if last_report_month:
        y, m = last_report_month.split('-')
        month_label = f'{MONTHS_RU[int(m)].capitalize()} {y}'
        parts.append(f'''<a class="dash-card dc-done" href="reports/">
    <div class="dc-label">Последний отчёт</div>
    <div class="dc-value" style="font-size:18px;">{month_label}</div>
    <div class="dc-sub">отчёты отдела СРиТП</div>
</a>''')
    else:
        parts.append('''<a class="dash-card" href="reports/">
    <div class="dc-label">Последний отчёт</div>
    <div class="dc-value" style="font-size:18px;">—</div>
    <div class="dc-sub">отчёты отдела СРиТП</div>
</a>''')

    # Звонки — с цифрами из calls.md
    if calls_totals:
        month_label = ''
        if calls_totals.get('month_ru') and calls_totals.get('year'):
            month_label = f'{calls_totals["month_ru"].capitalize()} {calls_totals["year"]}'
        elif calls_totals.get('year'):
            month_label = str(calls_totals['year'])

        total_calls = calls_totals["incoming"] + calls_totals["missed"] + calls_totals["outgoing"]
        label = 'Звонки' + (f' за {month_label}' if month_label else '')

        parts.append(f'''<a class="dash-card dc-info" href="calls/calls/">
    <div class="dc-label">{label}</div>
    <div class="dc-value" style="font-size:22px;">{total_calls}</div>
    <div class="dc-sub">принятые {calls_totals["incoming"]} · пропущенные {calls_totals["missed"]} · исходящие {calls_totals["outgoing"]}</div>
</a>''')
    else:
        parts.append('''<a class="dash-card dc-info" href="calls/calls/">
    <div class="dc-label">Звонки</div>
    <div class="dc-value" style="font-size:18px;">Статистика</div>
    <div class="dc-sub">принятые · пропущенные · исходящие</div>
</a>''')

    parts.append('</div>')
    parts.append('')

    # ==== Требует внимания ====
    parts.append('## Требует внимания')
    parts.append('')

    if upcoming:
        parts.append('<table class="attn-table">')
        parts.append('<thead><tr>'
                     '<th>Мероприятие</th>'
                     '<th style="width:140px;">Срок</th>'
                     '<th style="width:170px;">Этап</th>'
                     '</tr></thead>')
        parts.append('<tbody>')
        for item in upcoming[:10]:
            try:
                d = datetime.strptime(item['deadline'], '%Y-%m-%d').date()
                d_disp = f'{d.day:02d}.{d.month:02d}.{d.year}'
            except ValueError:
                d_disp = item['deadline']

            stage = STATUS_LABEL.get(item['status'], item['status'])
            parts.append(
                f'<tr>'
                f'<td>{item["name"]}</td>'
                f'<td class="at-deadline {item["kind"]}">{d_disp}</td>'
                f'<td>{stage}</td>'
                f'</tr>'
            )
        parts.append('</tbody></table>')
    else:
        parts.append('<div class="attn-empty">Просроченных и близких к сроку мероприятий нет.</div>')

    parts.append('')

    return '\n'.join(parts)


# =====================  CALENDAR  =====================
CALENDAR_STYLE = '''<style>
.cal-table {
    width: 100%;
    border-collapse: collapse;
    background: #fff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    overflow: hidden;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 13.5px;
    margin: 16px 0 24px 0;
}
.cal-table th {
    background: #f5f7fa;
    color: #2c3e50;
    font-weight: 600;
    text-align: left;
    padding: 10px 14px;
    border-bottom: 1px solid #e2e8f0;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 0.03em;
}
.cal-table td {
    padding: 10px 14px;
    border-bottom: 1px solid #eef2f6;
    vertical-align: middle;
}
.cal-table tr:last-child td { border-bottom: none; }

.cal-date {
    white-space: nowrap;
    font-weight: 700;
    color: #2c3e50;
}
.cal-days {
    text-align: right;
    white-space: nowrap;
    color: #718096;
    font-size: 12.5px;
}

.cal-row.overdue td { background: #fff5f5; }
.cal-row.overdue .cal-date { color: #c53030; }
.cal-row.soon td    { background: #fffaf0; }
.cal-row.soon .cal-date { color: #b7791f; }
.cal-row.near td    { background: #f0f8ff; }
.cal-row.near .cal-date { color: #2b6cb0; }

.cal-kind {
    display: inline-block;
    padding: 2px 10px;
    border-radius: 10px;
    font-size: 11.5px;
    font-weight: 600;
    white-space: nowrap;
}
.cal-kind.k-roadmap  { background: #ebf8ff; color: #2b6cb0; }
.cal-kind.k-report   { background: #f0fff4; color: #2f855a; }
.cal-kind.k-meeting  { background: #faf5ff; color: #6b46c1; }
.cal-kind.k-contract { background: #fffaf0; color: #b7791f; }
.cal-kind.k-other    { background: #edf2f7; color: #4a5568; }

.cal-summary {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin: 12px 0 22px 0;
}
.cal-summary .cs-card {
    background: #fff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 14px 16px;
    border-left: 4px solid #3182ce;
}
.cal-summary .cs-card.cs-overdue { border-left-color: #c53030; }
.cal-summary .cs-card.cs-soon    { border-left-color: #b7791f; }
.cal-summary .cs-card.cs-near    { border-left-color: #2b6cb0; }
.cal-summary .cs-card.cs-total   { border-left-color: #4a5568; }
.cal-summary .cs-value {
    font-size: 24px;
    font-weight: 700;
    color: #2c3e50;
    line-height: 1.1;
}
.cal-summary .cs-label {
    font-size: 11.5px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #718096;
    font-weight: 700;
    margin-top: 6px;
}
@media (max-width: 720px) {
    .cal-summary { grid-template-columns: repeat(2, 1fr); }
}
</style>'''


KIND_LABEL = {
    'roadmap':  'Мероприятие',
    'report':   'Отчётность',
    'meeting':  'Совещание',
    'contract': 'Контракт',
    'other':    'Прочее',
}


def render_calendar(statuses, roadmap_events, calendar_events):
    today = datetime.now().date()

    saved_statuses = statuses.get('statuses', {})
    saved_deadlines = statuses.get('deadlines', {})

    items = []

    # Из roadmap
    for ev in roadmap_events:
        key = str(ev['key'])
        status = saved_statuses.get(key, ev['status'])
        deadline = saved_deadlines.get(key, ev['deadline'])
        if status == 'done' or not deadline:
            continue
        items.append({
            'date': deadline,
            'kind': 'roadmap',
            'title': ev['name'],
            'meta': STATUS_LABEL.get(status, status),
        })

    # Из отдельного файла событий
    for ev in calendar_events:
        d = ev.get('date', '')
        if not d:
            continue
        items.append({
            'date': d,
            'kind': ev.get('kind', 'other'),
            'title': ev.get('title', '—'),
            'meta': ev.get('meta', ''),
        })

    def days_until(d):
        try:
            return (datetime.strptime(d, '%Y-%m-%d').date() - today).days
        except ValueError:
            return None

    items = [it for it in items if days_until(it['date']) is not None]
    items.sort(key=lambda it: days_until(it['date']))

    overdue = sum(1 for it in items if days_until(it['date']) < 0)
    soon    = sum(1 for it in items if 0 <= days_until(it['date']) <= 7)
    near    = sum(1 for it in items if 8 <= days_until(it['date']) <= 30)

    parts = []
    parts.append(CALENDAR_STYLE)
    parts.append('')
    parts.append('# Календарь ключевых дат')
    parts.append('')
    parts.append(f'*Обновлено: {human_date(today)}*')
    parts.append('')

    parts.append('<div class="cal-summary">')
    parts.append(f'''<div class="cs-card cs-overdue">
    <div class="cs-value">{overdue}</div>
    <div class="cs-label">Просрочено</div>
</div>''')
    parts.append(f'''<div class="cs-card cs-soon">
    <div class="cs-value">{soon}</div>
    <div class="cs-label">В течение 7 дней</div>
</div>''')
    parts.append(f'''<div class="cs-card cs-near">
    <div class="cs-value">{near}</div>
    <div class="cs-label">В течение 30 дней</div>
</div>''')
    parts.append(f'''<div class="cs-card cs-total">
    <div class="cs-value">{len(items)}</div>
    <div class="cs-label">Всего в календаре</div>
</div>''')
    parts.append('</div>')
    parts.append('')

    if not items:
        parts.append('*Событий пока нет.*')
        return '\n'.join(parts)

    parts.append('<table class="cal-table">')
    parts.append('<thead><tr>'
                 '<th style="width:130px;">Дата</th>'
                 '<th style="width:130px;">Тип</th>'
                 '<th>Событие</th>'
                 '<th style="width:110px; text-align:right;">Осталось</th>'
                 '</tr></thead>')
    parts.append('<tbody>')

    for it in items:
        dlt = days_until(it['date'])
        kind_label = KIND_LABEL.get(it['kind'], it['kind'])
        kind_class = f"k-{it['kind']}"

        try:
            d = datetime.strptime(it['date'], '%Y-%m-%d').date()
            d_disp = f'{d.day:02d}.{d.month:02d}.{d.year}'
        except ValueError:
            d_disp = it['date']

        if dlt < 0:
            row_cls = 'cal-row overdue'
            days_disp = f'просрочено на {-dlt} дн.'
        elif dlt <= 7:
            row_cls = 'cal-row soon'
            days_disp = f'{dlt} дн.' if dlt > 0 else 'сегодня'
        elif dlt <= 30:
            row_cls = 'cal-row near'
            days_disp = f'{dlt} дн.'
        else:
            row_cls = 'cal-row'
            days_disp = f'{dlt} дн.'

        meta = it['meta']
        title_html = it['title']
        if meta:
            title_html = f'{it["title"]} <span style="color:#718096;font-size:12px;">— {meta}</span>'

        parts.append(
            f'<tr class="{row_cls}">'
            f'<td class="cal-date">{d_disp}</td>'
            f'<td><span class="cal-kind {kind_class}">{kind_label}</span></td>'
            f'<td>{title_html}</td>'
            f'<td class="cal-days">{days_disp}</td>'
            f'</tr>'
        )

    parts.append('</tbody></table>')
    parts.append('')

    return '\n'.join(parts)


# =====================  MAIN  =====================
def main():
    statuses = load_statuses()
    roadmap_events = parse_roadmap_events()
    calendar_events = load_calendar_events()
    contracts_count, contracts_sum = parse_contracts_2026()
    reports_months = parse_reports_months()
    calls_totals = parse_calls_totals()

    print(f'  roadmap-событий: {len(roadmap_events)}')
    print(f'  событий из calendar: {len(calendar_events)}')
    print(f'  контрактов за {datetime.now().year}: {contracts_count} (сумма: {contracts_sum})')
    print(f'  месяцев с отчётами: {len(reports_months)}')
    if calls_totals:
        print(f'  звонков: принято {calls_totals["incoming"]}, '
              f'пропущено {calls_totals["missed"]}, '
              f'исходящих {calls_totals["outgoing"]}')
    else:
        print('  звонков: данные не найдены')

    index_md = render_dashboard(
        statuses, roadmap_events,
        contracts_count, contracts_sum,
        reports_months, calls_totals,
    )
    calendar_md = render_calendar(statuses, roadmap_events, calendar_events)

    with open(INDEX_OUT, 'w', encoding='utf-8') as f:
        f.write(index_md)
    print(f'✅ Дашборд: {INDEX_OUT}')

    with open(CALENDAR_OUT, 'w', encoding='utf-8') as f:
        f.write(calendar_md)
    print(f'✅ Календарь: {CALENDAR_OUT}')


if __name__ == '__main__':
    main()