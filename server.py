#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Раздаёт собранный сайт MkDocs (папка site/) + API для статусов.

Запуск:
    mkdocs build            # один раз (или после правок)
    python server.py

Открыть:
    http://<IP>:8000/                 → главная MkDocs
    http://<IP>:8000/roadmap/         → страница карты мероприятий
    http://<IP>:8000/api/statuses     → JSON со статусами
"""
import json
import os
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

# ---------- Настройки ----------
PORT = 8000
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_DIR = os.path.join(BASE_DIR, 'site')          # что раздаём как статику
STATUS_FILE = os.path.join(BASE_DIR, 'statuses.json')  # где храним статусы


def load_statuses():
    if not os.path.exists(STATUS_FILE):
        return {}
    try:
        with open(STATUS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print('Не удалось прочитать statuses.json:', e)
        return {}


def save_statuses(data):
    tmp = STATUS_FILE + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tmp, STATUS_FILE)


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
        # отдаём статику из SITE_DIR
        super().do_GET()

    # ---------- POST ----------
    def do_POST(self):
        path = urlparse(self.path).path
        if path != '/api/statuses':
            self.send_error(404, 'Not found')
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

        try:
            save_statuses(data)
        except Exception as e:
            self._send_json({'error': str(e)}, 500)
            return

        self._send_json({'ok': True})

    # ---------- немного тишины в консоли ----------
    def log_message(self, fmt, *args):
        msg = fmt % args
        # не засоряем вывод частыми GET-ами
        if '/api/statuses' in msg or ' 200 ' not in msg:
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
    print(f'Сервер запущен.')
    print(f'  Сайт:    http://0.0.0.0:{PORT}/')
    print(f'  API:     http://0.0.0.0:{PORT}/api/statuses')
    print(f'  Статусы: {STATUS_FILE}')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nОстановлено.')


if __name__ == '__main__':
    main()