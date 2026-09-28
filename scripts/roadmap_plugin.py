"""
Плагин mkdocs «roadmap_save».

Позволяет редактировать карту мероприятий (docs/projects_2026/roadmap.md)
прямо в браузере — изменения сохраняются ОБРАТНО В ИСХОДНЫЙ ФАЙЛ markdown,
поэтому их видят ВСЕ пользователи сайта:

    1. Браузер (docs/javascripts/roadmap-editor.js) при нажатии ✓ отправляет
       POST /_roadmap/save с JSON {row, col, html, status}.
    2. Плагин заменяет содержимое и класс статуса соответствующей <td>
       в файле docs/projects_2026/roadmap.md.
    3. Встроенный live-reload mkdocs замечает изменение файла, пересобирает
       страницу и уведомляет всех подключённых клиентов — у коллег страница
       обновляется сама (или по F5).

Подключение в mkdocs.yml:

    plugins:
      - search
      - roadmap_save:
          source: projects_2026/roadmap.md

Запуск сервера (доступ по локальной сети):

    mkdocs serve -a 0.0.0.0:8000
"""

from __future__ import annotations

import json
import os
import re
import tempfile
import threading
from http.server import BaseHTTPRequestHandler

from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin

_lock = threading.Lock()

CELL_RE = re.compile(r"<td[^>]*>.*?</td>", flags=re.S)
CLASS_ATTR_RE = re.compile(r'\s*class="[^"]*"')


def _atomic_write(path: str, text: str) -> None:
    """Атомарная запись, чтобы watcher не прочитал полупустой файл."""
    directory = os.path.dirname(path) or "."
    fd, tmp = tempfile.mkstemp(dir=directory, suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(text)
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def replace_cell(md_text: str, row: int, col: int,
                 new_html: str, status: str) -> tuple[str, bool]:
    """
    Заменяет содержимое ячейки (row, col, 1-based) в tbody HTML-таблице
    внутри markdown-файла и обновляет её класс статуса.

    Возвращает (новый_текст_файла, было_ли_изменение).
    """
    lines = md_text.split("\n")

    # Собираем блоки <tr>...</tr>, содержащие данные (<td>)
    data_rows: list[tuple[int, int]] = []
    i = 0
    while i < len(lines):
        if "<tr>" in lines[i]:
            j = i
            while j < len(lines) and "</tr>" not in lines[j]:
                j += 1
            block = "\n".join(lines[i:j + 1])
            if "<td" in block:
                data_rows.append((i, j))
            i = j + 1
        else:
            i += 1

    if not (1 <= row <= len(data_rows)):
        return md_text, False

    start, end = data_rows[row - 1]
    block_text = "\n".join(lines[start:end + 1])

    cells = CELL_RE.findall(block_text)
    if not (1 <= col <= len(cells)):
        return md_text, False

    old_cell = cells[col - 1]

    # атрибуты старой ячейки без class
    m = re.match(r"<td([^>]*)>", old_cell)
    attrs = CLASS_ATTR_RE.sub("", m.group(1) if m else "").strip()
    if status and status != "status-wait":
        attrs = (attrs + f' class="{status}"').strip()
    attrs = (" " + attrs) if attrs else ""

    new_cell = f"<td{attrs}>{new_html}</td>"
    new_block = block_text.replace(old_cell, new_cell, 1)

    new_lines = lines[:start] + new_block.split("\n") + lines[end + 1:]
    return "\n".join(new_lines), True


class _SaveMixin(BaseHTTPRequestHandler):
    """HTTP-логика сохранения; исходный файл задаётся через атрибут класса."""

    source_abs: str = ""

    def _respond(self, code: int, payload: dict) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):  # noqa: N802
        if not self.path.split("?")[0].rstrip("/").endswith("_roadmap/save"):
            self._respond(404, {"ok": False, "error": "not found"})
            return
        try:
            length = int(self.headers.get("Content-Length", 0) or 0)
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
            src = type(self).source_abs
            if not src or not os.path.isfile(src):
                raise FileNotFoundError("roadmap.md не найден")

            with _lock:
                with open(src, encoding="utf-8") as f:
                    text = f.read()
                new_text, changed = replace_cell(
                    text,
                    int(payload["row"]),
                    int(payload["col"]),
                    str(payload["html"]),
                    str(payload.get("status", "")),
                )
                if not changed:
                    raise ValueError(f"ячейка {payload['row']}:{payload['col']} не найдена")
                _atomic_write(src, new_text)

            self._respond(200, {"ok": True})
        except Exception as exc:  # noqa: BLE001
            self._respond(500, {"ok": False, "error": str(exc)})

    def log_message(self, *args):  # не засоряем консоль mkdocs serve
        pass


class RoadmapSavePlugin(BasePlugin):
    config_scheme = (
        ("source", config_options.Type(str, default="projects_2026/roadmap.md")),
    )

    def on_config(self, config, **kwargs):
        # абсолютный путь к исходному файлу (не ко временной сборке)
        docs_dir = os.path.abspath(config["docs_dir"])
        path = os.path.join(docs_dir, self.config["source"])
        if not os.path.isfile(path):
            self.source_abs = ""
        else:
            self.source_abs = path
        return config

    def on_serve(self, server, config, **kwargs):
        base_handler = server.RequestHandlerClass

        handler = type(
            "RoadmapCombinedHandler",
            (_SaveMixin, base_handler),
            {"source_abs": getattr(self, "source_abs", "")},
        )
        server.RequestHandlerClass = handler
        return server
