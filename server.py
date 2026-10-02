#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Раздаёт собранный сайт MkDocs (папка site/) + API для статусов и сроков.

Запуск:
    mkdocs build            # один раз (или после правок)
    python server.py

Открыть:
    http://<IP>:8000/                 → главная MkDocs
    http://<IP>:8000/roadmap/         → страница карты мероприятий
    http://<IP>:8000/api/statuses     → JSON со статусами и сроками
    http://<IP>:8000/api/config       → права текущего клиента
"""
import json
import os
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

# ---------- Настройки ----------
PORT = 8000
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_DIR = os.path.join(BASE_DIR, 'site')
STATUS_FILE = os.path.join(BASE_DIR, 'statuses.json')

# IP-адрес, с которого разрешено редактирование
EDIT_IP = '10.18.32.139'

DEFAULT_STATE = {
    "statuses":  {},
    "deadlines": {},
    "assignees": {},
    "stages":    {},
}


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
    if ('statuses' not in data
            and 'deadlines' not in data
            and 'assignees' not in data
            and 'stages' not in data):
        data = {"statuses": data, "deadlines": {}, "assignees": {}, "stages": {}}
    else:
        data.setdefault('statuses',  {})
        data.setdefault('deadlines', {})
        data.setdefault('assignees', {})
        data.setdefault('stages',    {})

    return data


def save_statuses(data):
    tmp = STATUS_FILE + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tmp, STATUS_FILE)


def get_client_ip(handler):
    """Возвращает реальный IP клиента с учётом X-Forwarded-For."""
    xff = handler.headers.get('X-Forwarded-For')
    if xff:
        return xff.split(',')[0].strip()
    return handler.client_address[0]


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

    # ---------- GET ----------
    def do_GET(self):
        path = urlparse(self.path).path

        if path == '/api/statuses':
            self._send_json(load_statuses())
            return

        if path == '/api/config':
            client_ip = get_client_ip(self)
            can_edit = (client_ip == EDIT_IP)
            self._send_json({
                'can_edit':  can_edit,
                'client_ip': client_ip,
            })
            return

        super().do_GET()

    # ---------- POST ----------
    def do_POST(self):
        path = urlparse(self.path).path
        if path != '/api/statuses':
            self.send_error(404, 'Not found')
            return

        # ---- Проверка IP: только EDIT_IP может писать ----
        client_ip = get_client_ip(self)
        if client_ip != EDIT_IP:
            self._send_json({
                'error': 'forbidden',
                'client_ip': client_ip,
            }, 403)
            return

        length = int(self.headers.get('Content-Length', 0))
        raw = self.rfile.read(length) if length else b'{}'
        try:
            data = json.loads(raw.decode('utf-8'))
        except Exception:
            self._send_json({'error': 'invalid json'}, 400)
            return
        if not isinstance(data, dict):
            self._send_json({'error': 'expected object'}, 400)
            return

        # Допускаем только известные ключи верхнего уровня
        clean = {
            'statuses':  data.get('statuses',  {}) if isinstance(data.get('statuses'),  dict) else {},
            'deadlines': data.get('deadlines', {}) if isinstance(data.get('deadlines'), dict) else {},
            'assignees': data.get('assignees', {}) if isinstance(data.get('assignees'), dict) else {},
            'stages':    data.get('stages',    {}) if isinstance(data.get('stages'),    dict) else {},
        }

        # Мержим с текущим состоянием, чтобы не терять поля, которых нет в запросе
        current = load_statuses()
        for key in ('statuses', 'deadlines', 'assignees', 'stages'):
            current.setdefault(key, {})
            current[key].update(clean[key])

        try:
            save_statuses(current)
        except Exception as e:
            self._send_json({'error': str(e)}, 500)
            return

        self._send_json({'ok': True})

    # ---------- тишина в консоли ----------
    def log_message(self, fmt, *args):
        msg = fmt % args
        if '/api/statuses' in msg or '/api/config' in msg or ' 200 ' not in msg:
            sys.stderr.write('%s - - [%s] %s\n' % (
                self.address_string(),
                self.log_date_time_string(),
                msg,
            ))


def main():
    if not os.path.isdir(SITE_DIR):
        print(f'Папка "{SITE_DIR}" не найдена.')
        print('Сначала выполните:  mkdocs build')
        sys.exit(1)

    os.chdir(SITE_DIR)
    server = ThreadingHTTPServer(('0.0.0.0', PORT), Handler)
    print('Сервер запущен.')
    print(f'  Сайт:            http://0.0.0.0:{PORT}/')
    print(f'  API статусов:    http://0.0.0.0:{PORT}/api/statuses')
    print(f'  API конфигурации:http://0.0.0.0:{PORT}/api/config')
    print(f'  Файл состояния:  {STATUS_FILE}')
    print(f'  IP для правки:   {EDIT_IP}')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nОстановлено.')


if __name__ == '__main__':
    main()