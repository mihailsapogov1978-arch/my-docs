#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Раздаёт собранный сайт MkDocs (папка site/) + API:
  - /api/statuses           — статусы карты мероприятий (statuses.json)
  - /api/daily/<slug>       — приём ежедневных заметок (POST) от конкретного сотрудника
  - /api/daily?employee=...&month=... (GET) — чтение заметок сотрудника за месяц
  - /daily/<slug>/          — персональная страница формы ежедневника

Запуск:
    mkdocs build
    python server.py

Открыть:
    http://<IP>:8000/                     → главная MkDocs
    http://<IP>:8000/daily/mulyavin/      → форма для Мулявина
"""
import json
import os
import re
import sys
from datetime import datetime, timedelta
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

# ---------- Настройки ----------
PORT = 8000
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_DIR = os.path.join(BASE_DIR, 'site')                      # статика MkDocs
STATUS_FILE = os.path.join(BASE_DIR, 'statuses.json')          # статусы roadmap
DAILY_DIR = os.path.join(BASE_DIR, 'docs', '_daily')           # ежедневные заметки

DEFAULT_STATE = {
    "statuses":  {},
    "assignees": {},
    "stages":    {},
    "deadlines": {},
    "details":   {},
}

MONTHS_RU = {
    1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь',
    7: 'Июль', 8: 'Август', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь',
}

# Слаг → отображаемое ФИО
EMPLOYEE_SLUGS = {
    'staver':     'Ставер',
    'sapogov':    'Сапогов',
    'mulyavin':   'Мулявин',
    'chechetkin': 'Чечеткин',
    'roganova':   'Роганова',
    'obmolova':   'Обмолова',
    'koshik':     'Кошик',
    'gasanov':    'Гасанов',
    'hudyshkin':  'Худышкин',
}


# =====================  STATUSES  =====================
def load_statuses():
    if not os.path.exists(STATUS_FILE):
        return dict(DEFAULT_STATE)
    try:
        with open(STATUS_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print('Не удалось прочитать statuses.json:', e)
        return dict(DEFAULT_STATE)

    if not isinstance(data, dict):
        return dict(DEFAULT_STATE)

    # Миграция старого формата (плоский словарь) в новый
    if ('statuses' not in data and 'assignees' not in data and
            'stages' not in data and 'deadlines' not in data and 'details' not in data):
        data = {"statuses": data, "assignees": {}, "stages": {}, "deadlines": {}, "details": {}}
    else:
        data.setdefault('statuses', {})
        data.setdefault('assignees', {})
        data.setdefault('stages', {})
        data.setdefault('deadlines', {})
        data.setdefault('details', {})

    return data


def save_statuses(data):
    tmp = STATUS_FILE + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tmp, STATUS_FILE)


# =====================  DAILY  =====================
def _validate_date(date_str):
    """
    Проверяет, что дата в разумных рамках:
      - не раньше 1-го числа предыдущего месяца,
      - не позже сегодняшнего дня + 1.
    Возвращает (ok, message).
    """
    try:
        dt = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return False, 'date must be YYYY-MM-DD'

    today = datetime.now().date()
    first_this_month = today.replace(day=1)
    prev_month_last = first_this_month - timedelta(days=1)
    earliest = prev_month_last.replace(day=1)
    latest = today + timedelta(days=1)

    if dt < earliest:
        return False, f'дата слишком старая (мин. {earliest.isoformat()})'
    if dt > latest:
        return False, f'дата из будущего (макс. {latest.isoformat()})'
    return True, ''


def save_daily_entry(employee, date_str, text):
    """
    Сохраняет запись в docs/_daily/YYYY-MM/<имя>.md.
    Логика:
      - файла нет → создаём с заголовком "# Имя — Месяц Год";
      - блок "## YYYY-MM-DD" уже есть → заменяем;
      - нет → вставляем сверху, сразу под заголовком.
    Возвращает относительный путь к файлу.
    """
    dt = datetime.strptime(date_str, '%Y-%m-%d')

    safe_name = re.sub(r'[^\w\-А-Яа-яЁё]', '', employee)
    if not safe_name:
        raise ValueError('invalid employee name')

    month_dir = os.path.join(DAILY_DIR, dt.strftime('%Y-%m'))
    os.makedirs(month_dir, exist_ok=True)
    path = os.path.join(month_dir, safe_name + '.md')

    items = [ln.strip(' -*\t') for ln in text.split('\n') if ln.strip()]
    items = [it for it in items if it]
    new_block = f"## {date_str}\n\n" + '\n'.join(f'- {it}' for it in items) + '\n'

    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
    else:
        month_label = MONTHS_RU[dt.month]
        content = f"# {employee} — {month_label} {dt.year}\n"

    pattern = re.compile(
        r'(##\s+' + re.escape(date_str) + r'\s*\n)(.*?)(?=\n##\s+\d{4}-\d{2}-\d{2}\s*\n|\Z)',
        re.DOTALL
    )

    if pattern.search(content):
        content = pattern.sub(new_block.rstrip() + '\n', content, count=1)
    else:
        if content.startswith('# '):
            nl = content.index('\n')
            content = content[:nl + 1] + '\n' + new_block + content[nl + 1:]
        else:
            content = new_block + '\n' + content

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    return os.path.relpath(path, BASE_DIR)


def list_daily_entries(employee, month):
    """
    Читает файл заметок сотрудника за месяц.
    Возвращает (content, error).
    """
    safe_name = re.sub(r'[^\w\-А-Яа-яЁё]', '', employee or '')
    if not safe_name or not re.match(r'^\d{4}-\d{2}$', month or ''):
        return None, 'invalid params'

    path = os.path.join(DAILY_DIR, month, safe_name + '.md')
    if not os.path.exists(path):
        return '', None
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read(), None
    except Exception as e:
        return None, str(e)


# =====================  HANDLER  =====================
class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=SITE_DIR, **kwargs)

    # ---------- helpers ----------
    def _send_json(self, obj, code=200):
        body = json.dumps(obj, ensure_ascii=False).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(body)

    def _send_html(self, html, code=200):
        body = html.encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(body)

    def _read_json(self):
        length = int(self.headers.get('Content-Length', 0))
        raw = self.rfile.read(length) if length else b'{}'
        try:
            return json.loads(raw.decode('utf-8')), None
        except Exception as e:
            return None, str(e)

    # ---------- GET ----------
    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        # /api/statuses
        if path == '/api/statuses':
            self._send_json(load_statuses())
            return

        # /api/daily?employee=Мулявин&month=2026-10
        if path == '/api/daily':
            qs = parse_qs(parsed.query or '')
            employee = (qs.get('employee') or [''])[0].strip()
            month = (qs.get('month') or [''])[0].strip()
            content, err = list_daily_entries(employee, month)
            if err:
                self._send_json({'ok': False, 'error': err}, 400)
                return
            self._send_json({'ok': True, 'employee': employee, 'month': month, 'content': content or ''})
            return

        # /daily/<slug>/ — персональная форма.
        # Отдаём site/daily/index.html, добавив <base href="/">,
        # чтобы ресурсы (assets/, stylesheets/, javascripts/)
        # грузились от корня сайта, а не от /daily/<slug>/.
        m = re.match(r'^/daily/([a-z\-]+)/?$', path)
        if m and m.group(1).lower() in EMPLOYEE_SLUGS:
            index_path = os.path.join(SITE_DIR, 'daily', 'index.html')
            if os.path.exists(index_path):
                with open(index_path, 'r', encoding='utf-8') as f:
                    html = f.read()

                if '<base ' not in html:
                    html = re.sub(
                        r'(<head[^>]*>)',
                        r'\1\n<base href="/">',
                        html,
                        count=1,
                        flags=re.IGNORECASE,
                    )

                self._send_html(html)
                return

        # всё остальное — статика MkDocs
        super().do_GET()

    # ---------- POST ----------
    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path == '/api/statuses':
            self._handle_statuses_post()
            return

        # /api/daily/<slug>
        m = re.match(r'^/api/daily/([a-z\-]+)/?$', path)
        if m:
            slug = m.group(1).lower()
            employee = EMPLOYEE_SLUGS.get(slug)
            if not employee:
                self._send_json({'ok': False, 'error': 'unknown employee'}, 404)
                return
            self._handle_daily_post(forced_employee=employee)
            return

        # /api/daily без слага — отключено
        if path == '/api/daily':
            self._send_json({'ok': False, 'error': 'use /api/daily/<slug>'}, 400)
            return

        self.send_error(404, 'Not found')

    # ---------- /api/statuses ----------
    def _handle_statuses_post(self):
        data, err = self._read_json()
        if err:
            self._send_json({'error': 'invalid json'}, 400)
            return
        if not isinstance(data, dict):
            self._send_json({'error': 'expected object'}, 400)
            return

        data = {
            'statuses':  data.get('statuses',  {}) if isinstance(data.get('statuses'),  dict) else {},
            'assignees': data.get('assignees', {}) if isinstance(data.get('assignees'), dict) else {},
            'stages':    data.get('stages',    {}) if isinstance(data.get('stages'),    dict) else {},
            'deadlines': data.get('deadlines', {}) if isinstance(data.get('deadlines'), dict) else {},
            'details':   data.get('details',   {}) if isinstance(data.get('details'),   dict) else {},
        }

        try:
            save_statuses(data)
        except Exception as e:
            self._send_json({'error': str(e)}, 500)
            return

        self._send_json({'ok': True})

    # ---------- /api/daily ----------
    def _handle_daily_post(self, forced_employee):
        data, err = self._read_json()
        if err:
            self._send_json({'ok': False, 'error': 'invalid json'}, 400)
            return
        if not isinstance(data, dict):
            self._send_json({'ok': False, 'error': 'expected object'}, 400)
            return

        employee = forced_employee
        date_str = (data.get('date') or '').strip()
        text = (data.get('text') or '').strip()

        if not date_str or not text:
            self._send_json({'ok': False, 'error': 'date and text required'}, 400)
            return

        ok, msg = _validate_date(date_str)
        if not ok:
            self._send_json({'ok': False, 'error': msg}, 400)
            return

        try:
            rel_path = save_daily_entry(employee, date_str, text)
        except Exception as e:
            self._send_json({'ok': False, 'error': str(e)}, 500)
            return

        self._send_json({'ok': True, 'employee': employee, 'path': rel_path})

    # ---------- тишина в консоли ----------
    def log_message(self, fmt, *args):
        msg = fmt % args
        if '/api/' in msg or ' 200 ' not in msg:
            sys.stderr.write('%s - - [%s] %s\n' % (
                self.address_string(),
                self.log_date_time_string(),
                msg,
            ))


# =====================  MAIN  =====================
def main():
    if not os.path.isdir(SITE_DIR):
        print(f'Папка "{SITE_DIR}" не найдена.')
        print('Сначала выполните:  mkdocs build')
        sys.exit(1)

    os.makedirs(DAILY_DIR, exist_ok=True)

    os.chdir(SITE_DIR)
    server = ThreadingHTTPServer(('0.0.0.0', PORT), Handler)
    print(f'Сервер запущен.')
    print(f'  Сайт:           http://0.0.0.0:{PORT}/')
    print(f'  Статусы:        http://0.0.0.0:{PORT}/api/statuses')
    print(f'  Форма (пример): http://0.0.0.0:{PORT}/daily/mulyavin/')
    print(f'  Файл статусов:  {STATUS_FILE}')
    print(f'  Папка daily:    {DAILY_DIR}')
    print(f'  Сотрудники:     {", ".join(sorted(EMPLOYEE_SLUGS.keys()))}')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nОстановлено.')


if __name__ == '__main__':
    main()