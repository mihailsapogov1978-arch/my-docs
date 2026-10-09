#!/usr/bin/env python3
"""
Парсер CDR-звонков из docs/calls/calls_09.xlsx
Формирует docs/calls/calls.md со статистикой по сотрудникам,
сгруппированной по структурным подразделениям.

Разделы:
    1. Детализация по подразделениям (раскрывающиеся блоки)
    2. Нагрузка отделов (гистограмма + таблица + выводы)
    3. Нагрузка сотрудников (карточки с топами)

Запуск из корня проекта:
    python3 parse_calls.py
"""

import re
import sys
from pathlib import Path
from collections import defaultdict, Counter

try:
    import pandas as pd
except ImportError:
    sys.exit("Установите pandas: pip install pandas openpyxl")


# ---------- Пути ----------
_here = Path(__file__).resolve().parent
ROOT = _here
for _ in range(5):
    if (ROOT / "mkdocs.yml").exists() or (ROOT / "docs").is_dir():
        break
    ROOT = ROOT.parent

CALLS_DIR = ROOT / "docs" / "calls"
MD_PATH = CALLS_DIR / "calls.md"

_candidates = (
    list(CALLS_DIR.glob("calls_*.xlsx"))
    + list(CALLS_DIR.glob("call_*.xlsx"))
)
_candidates = [p for p in _candidates if not p.name.startswith("~$")]

if not _candidates:
    sys.exit(f"В {CALLS_DIR} нет файлов calls_*.xlsx или call_*.xlsx")

XLSX_PATH = max(_candidates, key=lambda p: p.stat().st_mtime)

print(f"[parse_calls] ROOT      = {ROOT}")
print(f"[parse_calls] CALLS_DIR = {CALLS_DIR}")
print(f"[parse_calls] XLSX      = {XLSX_PATH}")


# ---------- Справочник подразделений ----------
DEPARTMENTS = {
    "Администрация": [
        "Подгайный Алексей Алексеевич",
        "Жданова Галина Игоревна",
        "Останин Иван Георгиевич",
        "Родина Наталья Васильевна",
        "Галямов Азат Ахтамович",
        "Гареева Регина Рафаэлевна",
    ],
    "Отдел информационной безопасности": [
        "Лычев Антон Владимирович",
        "Ананьев Евгений Сергеевич",
        "Шляпин Денис Олегович",
        "Иванников Вадим Вячеславович",
    ],
    "Отдел СР и ТП": [
        "Сапогов Михаил Дмитриевич",
        "Мулявин Яков Владиславович",
        "Чечеткин Михаил Игоревич",
        "Обмолова Валентина Витальевна",
        "Роганова Анна Анатольевна",
        "Кошик Владимир Иванович",
        "Худышкин Сергей Николаевич",
        "Гасанов Сархан Нураддин",
        "Ставер Андрей Петрович",
    ],
    "Отдел кадрового и правового обеспечения": [
        "Чернов Андрей Анатольевич",
        "Суханова Ирина Константиновна",
        "Цветнова Наталья Геннадьевна",
        "Ядрова Анна Викторовна",
        "Полякова Анна Викторовна",
    ],
    "Отдел учета основных средств и запасов": [
        "Стрельникова Ольга Сергеевна",
        "Щирская Ксения Васильевна",
        "Бусыгина Ирина Сергеевна",
        "Шибанаева Татьяна Викторовна",
        "Гатаулина Марина Васильевна",
        "Вернер Елена Викторовна",
        "Ильницкая Светлана Викторовна",
        "Петрова Наталья Александровна",
        "Филиппова Олеся Валерьевна",
        "Минакова Ольга Фахрутдиновна",
        "Зуева Галия Парвасьевна",
    ],
    "Отдел подготовки отчетности": [
        "Тимофеева Алиса Николаевна",
        "Шевелева Ксения Викторовна",
        "Лейпожих Алёна Алексеевна",
        "Чистякова Елена Дмитриевна",
        "Янова Екатерина Анатольевна",
        "Павлова Надежда Григорьевна",
        "Ребась Кристина Владимировна",
        "Яковлева Вилена Фаильевна",
    ],
    "Отдел учета доходов": [
        "Лаба Вера Алексеевна",
        "Занина Ирина Александровна",
        "Леванских Людмила Владимировна",
        "Жукова Анастасия Сергеевна",
        "Каргаполова Алёна Андреевна",
        "Семенова Наталья Викторовна",
        "Кропотов Иван Александрович",
        "Юшкевич Татьяна Владимировна",
        "Фаузер Татьяна Леовна",
        "Мицура Ираида Илдаровна",
        "Семенова Наталья Александровна",
    ],
    "Отдел расчётов с персоналом": [
        "Ильдеркина Ирина Николаевна",
        "Россолова Екатерина Сергеевна",
        "Павлова Ирина Игоревна",
        "вакансия",
        "Русмиленко Инга Юрьевна",
        "Казанцева Лариса Анатольевна",
        "Сафаралеева Елена Хайрулловна",
        "Манджиева Алевтина Алексеевна",
        "Лазарева Екатерина Николаевна",
        "Букреева Елена Николаевна",
        "Ершова Алла Николаевна",
        "Шахова Галина Максимовна",
        "Алыкова Татьяна Валерьевна",
        "Константинова Людмила Алексеевна",
        "Мунарева Виктория Игоревна",
        "Злобина Мария Александровна",
        "Конева Елена Ивановна",
    ],
    "Отдел расчётов с поставщиками, подрядчиками": [
        "Якута Светлана Михайловна",
        "Нурулина Наталья Владимировна",
        "Обломкина Лариса Ивановна",
        "Мухамадеева Танзиля Рафкатовна",
        "Горохова Алёна Павловна",
        "временная",
        "Кузнецова Надежда Александровна",
        "Нурлубаева Алина Залимхановна",
        "Дмитриенко Татьяна Валерьевна",
        "Кундаль Нина Валерьевна",
        "Карташова Мария Александровна",
        "Иванова Любовь Васильевна",
    ],
}


# ---------- Алиасы (грязное имя в CDR → чистое ФИО из справочника) ----------
FIO_ALIASES = {
    "константинова людмила алексеев":   "Константинова Людмила Алексеевна",
    "кузнецова надежда александровн":   "Кузнецова Надежда Александровна",
    "любовь васильевна иванова":        "Иванова Любовь Васильевна",
    "ксения викторовна шевелева":       "Шевелева Ксения Викторовна",
    "минакова ольга фрунзеновна":       "Минакова Ольга Фахрутдиновна",
}


# ---------- Полный стоп-лист ФИО ----------
EXCLUDE_FIOS = {
    "Подгайный Алексей Алексеевич",
}


def _norm_fio(s: str) -> str:
    if not s:
        return ""
    s = s.lower().replace("ё", "е")
    s = re.sub(r"\s+", " ", s).strip()
    return s


_EXCLUDE_NORM = {_norm_fio(x) for x in EXCLUDE_FIOS}

_FIO_TO_DEPT = {}
for _dept, _fios in DEPARTMENTS.items():
    for _fio in _fios:
        _FIO_TO_DEPT[_norm_fio(_fio)] = _dept

_ALIAS_TO_CLEAN = {_norm_fio(k): _norm_fio(v) for k, v in FIO_ALIASES.items()}

_CLEAN_KEY_TO_CANON = {}
for _dept, _fios in DEPARTMENTS.items():
    for _f in _fios:
        _CLEAN_KEY_TO_CANON[_norm_fio(_f)] = _f


def is_excluded(fio: str) -> bool:
    if not fio:
        return False
    key = _norm_fio(fio)
    clean_key = _ALIAS_TO_CLEAN.get(key, key)
    return key in _EXCLUDE_NORM or clean_key in _EXCLUDE_NORM


def resolve_fio(fio: str) -> str:
    if not fio:
        return ""
    key = _norm_fio(fio)
    clean_key = _ALIAS_TO_CLEAN.get(key, key)
    return _CLEAN_KEY_TO_CANON.get(clean_key, fio)


def get_department(fio: str) -> str:
    if not fio:
        return "Прочие / не указано"
    key = _ALIAS_TO_CLEAN.get(_norm_fio(fio), _norm_fio(fio))
    return _FIO_TO_DEPT.get(key, "Прочие / не указано")


# ---------- Стоп-лист служебных имён ----------
SERVICE_NAMES = {
    "uplink", "null", "undefined", "gateway", "logicterminal",
    "disa", "service-platform",
    "sp-1", "sp-2", "sp-3", "sp-4", "sp-5",
}
_SERVICE_RE = re.compile(r"(?i)^(disa|sp|gw|trunk)[-_]?\d*$")


# ---------- Утилиты ----------
def is_internal(number) -> bool:
    if number is None or pd.isna(number):
        return False
    s = str(number).strip()
    if not s or s.lower() == "null":
        return False
    return bool(re.fullmatch(r"\d{3,4}", s))


def is_filled(value) -> bool:
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return False
    s = str(value).strip()
    return s not in ("", "NULL", "NaT", "nan", "None")


def normalize_fio(name) -> str:
    if not is_filled(name):
        return ""
    s = re.sub(r"\s+", " ", str(name)).strip()
    if s.lower() in SERVICE_NAMES:
        return ""
    if _SERVICE_RE.match(s):
        return ""
    return s


def fmt_duration(seconds: int) -> str:
    if seconds is None or seconds < 0:
        return "—"
    h, rem = divmod(int(seconds), 3600)
    m, s = divmod(rem, 60)
    if h:
        return f"{h} ч {m:02d} мин {s:02d} с"
    if m:
        return f"{m} мин {s:02d} с"
    return f"{s} с"


# ---------- Парсинг ----------
def parse_calls() -> dict:
    if not XLSX_PATH.exists():
        sys.exit(f"Файл не найден: {XLSX_PATH}")

    df = pd.read_excel(XLSX_PATH, sheet_name=0, header=0, dtype=str)
    df.columns = [str(c).strip() for c in df.columns]

    def find_col(*variants):
        for v in variants:
            for c in df.columns:
                if v.lower() in c.lower():
                    return c
        return None

    c_initiator_name = find_col("Имя инициатора")
    c_result         = find_col("Результат вызова")
    c_connect        = find_col("Время соединения")
    c_disconnect     = find_col("Время разъединения")
    c_duration       = find_col("Продолжительность вызова")
    c_target_name    = find_col("Имя адресата вызова")
    c_target_num     = find_col("Б-номер во внутреннем плане нумерации")
    c_a_num          = find_col("А-номер во внутреннем плане нумерации")
    c_start          = find_col("Время старта")

    if not c_initiator_name or not c_result:
        sys.exit(f"Не найдены ключевые колонки. Доступные: {list(df.columns)}")

    stats = defaultdict(lambda: {"incoming": 0, "missed": 0, "outgoing": 0})

    longest_call = None
    pair_counter = Counter()
    hour_counter = Counter()

    for _, row in df.iterrows():
        initiator   = resolve_fio(normalize_fio(row.get(c_initiator_name)))
        result      = str(row.get(c_result) or "").strip().lower()
        connected   = is_filled(row.get(c_connect))
        target_name = resolve_fio(normalize_fio(row.get(c_target_name)))
        target_num  = row.get(c_target_num)
        a_num       = row.get(c_a_num)

        initiator_ok = bool(initiator) and not is_excluded(initiator)
        target_ok    = bool(target_name) and not is_excluded(target_name)

        missed_call = (
            not connected
            and ("прекращен" in result or "busy" in result or "занят" in result)
        )

        if connected:
            if initiator_ok and is_internal(a_num):
                stats[initiator]["outgoing"] += 1
            if target_ok and is_internal(target_num):
                stats[target_name]["incoming"] += 1
        elif missed_call and target_ok and is_internal(target_num):
            stats[target_name]["missed"] += 1

        if connected and initiator_ok and target_ok:
            dur = 0
            if c_duration:
                try:
                    dur = int(float(row.get(c_duration) or 0))
                except (ValueError, TypeError):
                    dur = 0
            if dur == 0 and c_connect and c_disconnect:
                t1, t2 = row.get(c_connect), row.get(c_disconnect)
                if is_filled(t1) and is_filled(t2):
                    try:
                        dur = int((pd.to_datetime(t2) - pd.to_datetime(t1)).total_seconds())
                    except Exception:
                        dur = 0

            if dur > 0:
                if longest_call is None or dur > longest_call["duration"]:
                    longest_call = {
                        "initiator": initiator,
                        "target": target_name,
                        "duration": dur,
                        "start": str(row.get(c_start) or "")[:19],
                    }

            pair_counter[tuple(sorted((initiator, target_name)))] += 1

        start = row.get(c_start)
        if is_filled(start):
            try:
                hour_counter[pd.to_datetime(start).hour] += 1
            except Exception:
                pass

    top_pair = None
    if pair_counter:
        (a, b), cnt = pair_counter.most_common(1)[0]
        top_pair = {"a": a, "b": b, "count": cnt}

    peak_hour = None
    if hour_counter:
        h, cnt = hour_counter.most_common(1)[0]
        peak_hour = {"hour": h, "count": cnt}

    # ---------- Топы по сотрудникам ----------
    MIN_INCOMING_FOR_RATE = 50

    top_initiator = top_target = None
    top_missed_rate = None
    best_answer = None

    if stats:
        fi, si = max(stats.items(), key=lambda kv: kv[1]["outgoing"])
        if si["outgoing"] > 0:
            top_initiator = {"fio": fi, "count": si["outgoing"]}

        ft, st = max(stats.items(), key=lambda kv: kv[1]["incoming"])
        if st["incoming"] > 0:
            top_target = {"fio": ft, "count": st["incoming"]}

        rate_rows = []
        for fio, s in stats.items():
            total_in = s["incoming"] + s["missed"]
            if total_in >= MIN_INCOMING_FOR_RATE:
                rate_rows.append({
                    "fio": fio,
                    "incoming": s["incoming"],
                    "missed": s["missed"],
                    "total_in": total_in,
                    "rate": s["missed"] / total_in,
                })

        if rate_rows:
            worst = max(rate_rows, key=lambda r: r["rate"])
            best  = min(rate_rows, key=lambda r: r["rate"])

            top_missed_rate = {
                "fio": worst["fio"],
                "missed": worst["missed"],
                "total_in": worst["total_in"],
                "percent": round(worst["rate"] * 100),
            }
            best_answer = {
                "fio": best["fio"],
                "incoming": best["incoming"],
                "total_in": best["total_in"],
                "percent": round((1 - best["rate"]) * 100),
            }

    # ---------- Агрегация по отделам ----------
    dept_meta = {}
    for fio, s in stats.items():
        dept = get_department(fio)
        if dept not in dept_meta:
            dept_meta[dept] = {
                "incoming": 0, "missed": 0, "outgoing": 0, "employees": 0
            }
        dept_meta[dept]["incoming"] += s["incoming"]
        dept_meta[dept]["missed"]   += s["missed"]
        dept_meta[dept]["outgoing"] += s["outgoing"]
        dept_meta[dept]["employees"] += 1

    for dept, d in dept_meta.items():
        total_in = d["incoming"] + d["missed"]
        d["total_in"]  = total_in
        d["total_all"] = d["incoming"] + d["missed"] + d["outgoing"]
        d["miss_rate"] = (d["missed"] / total_in) if total_in else 0.0
        d["out_in_ratio"] = (d["outgoing"] / total_in) if total_in else 0.0
        d["per_employee"] = (d["total_all"] / d["employees"]) if d["employees"] else 0.0

    return {
        "stats": dict(stats),
        "dept_meta": dept_meta,
        "meta": {
            "longest_call": longest_call,
            "top_pair": top_pair,
            "peak_hour": peak_hour,
            "top_initiator": top_initiator,
            "top_target": top_target,
            "top_missed_rate": top_missed_rate,
            "best_answer": best_answer,
        },
    }


# ---------- HTML/CSS ----------
HTML_HEADER = """<style>
:root {
    --emp-border: #e2e8f0;
    --emp-bg-hover: #f7fafc;
    --emp-text: #2d3748;
    --emp-muted: #718096;
    --emp-accent: #2b6cb0;
    --emp-accent-light: #ebf8ff;
    --emp-accent-border: #bee3f8;
    --emp-missed: #c53030;
    --emp-in: #2f855a;
    --emp-out: #2b6cb0;

    --col-num: 56px;
    --col-stat: 130px;
    --col-fio-min: 220px;
}

/* ---------- Плашка «Всего звонков» ---------- */
.calls-total {
    display: grid;
    grid-template-columns:
        minmax(var(--col-fio-min), 1fr)
        var(--col-stat)
        var(--col-stat)
        var(--col-stat);
    align-items: stretch;
    column-gap: 0;
    background: var(--emp-accent-light);
    border: 1px solid var(--emp-accent-border);
    border-radius: 8px;
    padding: 0;
    margin: 10px 0 24px 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    overflow: hidden;
}
.calls-total .ct-label {
    display: flex;
    align-items: center;
    font-size: 14px;
    color: var(--emp-accent);
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.03em;
    padding: 14px 20px;
}
.calls-total .ct-cell {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 12px 14px;
    border-left: 1px solid var(--emp-accent-border);
}
.calls-total .ct-value { font-size: 20px; font-weight: 700; line-height: 1.15; }
.calls-total .ct-caption {
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--emp-muted);
    margin-top: 2px;
}
.calls-total .ct-in   .ct-value { color: var(--emp-in); }
.calls-total .ct-miss .ct-value { color: var(--emp-missed); }
.calls-total .ct-out  .ct-value { color: var(--emp-out); }

/* ---------- Список отделов (раскрывающиеся блоки) ---------- */
.dept-list {
    margin: 16px 0;
    border: 1px solid var(--emp-border);
    border-radius: 10px;
    overflow: hidden;
    background: #fff;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}
.dept-item {
    border-bottom: 1px solid var(--emp-border);
}
.dept-item:last-child { border-bottom: none; }

.dept-row {
    display: grid;
    grid-template-columns: minmax(0, 1fr) 380px 20px;
    align-items: center;
    column-gap: 12px;
    padding: 14px 18px;
    font-size: 14px;
    line-height: 1.4;
    cursor: pointer;
    transition: background 0.15s;
    margin: 0;
}
.dept-row:hover { background: var(--emp-bg-hover); }

.dept-name {
    font-weight: 600;
    color: var(--emp-text);
    min-width: 0;
}

.dept-summary {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    column-gap: 12px;
    font-size: 11.5px;
    color: var(--emp-muted);
    text-align: right;
    white-space: nowrap;
    line-height: 1.3;
}
.dept-summary .ds-cell { display: inline-block; }
.dept-summary .ds-label { color: var(--emp-muted); }
.dept-summary b { color: var(--emp-accent); font-weight: 700; }

.dept-toggle {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    color: var(--emp-accent);
    font-size: 18px;
    font-weight: 700;
    transition: transform 0.18s;
    user-select: none;
}

.dept-checkbox { display: none; }
.dept-checkbox:checked ~ .dept-row .dept-toggle { transform: rotate(90deg); }
.dept-checkbox:checked ~ .dept-details { display: block; }

.dept-details {
    display: none;
    background: #fafbfc;
    padding: 0;
}

/* ---------- Общая таблица ---------- */
.calls-table {
    width: 100%;
    border-collapse: collapse;
    background: #fff;
    font-size: 13.5px;
    table-layout: fixed;
}
.calls-table col.col-num  { width: var(--col-num); }
.calls-table col.col-fio  { width: auto; }
.calls-table col.col-stat { width: var(--col-stat); }

.calls-table thead th {
    background: #f0f7ff;
    color: var(--emp-accent);
    font-weight: 700;
    font-size: 11.5px;
    text-transform: uppercase;
    letter-spacing: 0.03em;
    padding: 8px 14px;
    border-bottom: 1px solid var(--emp-accent-border);
    border-right: 1px solid var(--emp-accent-border);
    text-align: center;
    vertical-align: middle;
}
.calls-table thead th:last-child { border-right: none; }

.calls-table tbody td {
    padding: 8px 14px;
    border-bottom: 1px solid var(--emp-border);
    border-right: 1px solid var(--emp-border);
    text-align: right;
    font-weight: 700;
    white-space: nowrap;
}
.calls-table tbody td:last-child { border-right: none; }
.calls-table tbody tr:last-child td { border-bottom: none; }

.calls-table .col-num {
    color: var(--emp-muted);
    text-align: right;
}
.calls-table .col-fio {
    color: var(--emp-text);
    font-weight: 600;
    text-align: left;
    white-space: normal;
    overflow: hidden;
    text-overflow: ellipsis;
}
.calls-table .col-in   { color: var(--emp-in); }
.calls-table .col-miss { color: var(--emp-missed); }
.calls-table .col-out  { color: var(--emp-out); }

/* ---------- Таблица «Нагрузка отделов» (шире по колонкам) ---------- */
.calls-table.dept-load-table col.col-num  { width: 48px; }
.calls-table.dept-load-table col.col-fio  { width: auto; }
.calls-table.dept-load-table col.col-stat { width: 100px; }

.calls-table.dept-load-table thead th {
    font-size: 11px;
    padding: 8px 8px;
    white-space: normal;
    line-height: 1.2;
}
.calls-table.dept-load-table tbody td {
    padding: 8px 10px;
    font-size: 13px;
}

/* ---------- Гистограмма нагрузки ---------- */
.load-chart {
    margin: 16px 0 24px 0;
    padding: 16px 20px;
    border: 1px solid var(--emp-border);
    border-radius: 10px;
    background: #fff;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}

.load-chart-row {
    display: grid;
    grid-template-columns: 260px 1fr 70px;
    align-items: center;
    column-gap: 14px;
    padding: 8px 0;
    border-bottom: 1px dashed var(--emp-border);
}
.load-chart-row:last-child { border-bottom: none; }

.load-chart-name {
    font-size: 13px;
    color: var(--emp-text);
    font-weight: 600;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}

.load-chart-bar-wrap {
    position: relative;
    width: 100%;
    height: 22px;
    background: #f7fafc;
    border-radius: 4px;
    overflow: hidden;
}

.load-chart-bar {
    display: flex;
    height: 100%;
    border-radius: 4px;
    overflow: hidden;
    transition: width 0.3s ease;
}

.load-chart-seg {
    height: 100%;
    transition: opacity 0.15s;
}
.load-chart-seg.seg-in   { background: #6fa8b8; }   /* светлый teal */
.load-chart-seg.seg-miss { background: #f5a623; }   /* светло-оранжевый / янтарный */
.load-chart-seg.seg-out  { background: #8ba0c4; }   /* светло-slate */

.load-chart-value {
    text-align: right;
    font-size: 13px;
    font-weight: 700;
    color: var(--emp-accent);
    white-space: nowrap;
}

.load-chart-legend {
    display: flex;
    flex-wrap: wrap;
    gap: 18px;
    margin-top: 16px;
    padding-top: 12px;
    border-top: 1px solid var(--emp-border);
    font-size: 12.5px;
    color: var(--emp-muted);
}

.load-chart-legend-item {
    display: inline-flex;
    align-items: center;
    gap: 6px;
}
.load-chart-legend-dot {
    display: inline-block;
    width: 12px;
    height: 12px;
    border-radius: 3px;
}
.load-chart-legend-dot.legend-in   { background: #6fa8b8; }
.load-chart-legend-dot.legend-miss { background: #f5a623; }
.load-chart-legend-dot.legend-out  { background: #8ba0c4; }

/* ---------- Статистика ---------- */
.facts-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 14px;
    margin: 16px 0 24px 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}
.fact-card {
    background: #fff;
    border: 1px solid var(--emp-border);
    border-left: 4px solid var(--emp-accent);
    border-radius: 8px;
    padding: 14px 16px;
    transition: box-shadow 0.15s, transform 0.15s;
}
.fact-card:hover {
    box-shadow: 0 4px 12px rgba(43, 108, 176, 0.08);
    transform: translateY(-1px);
}
.fact-label {
    font-size: 11.5px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--emp-muted);
    font-weight: 700;
    margin-bottom: 8px;
}
.fact-value {
    font-size: 15px;
    color: var(--emp-text);
    font-weight: 700;
    line-height: 1.35;
    margin-bottom: 6px;
}
.fact-sub {
    font-size: 13px;
    color: var(--emp-muted);
    font-weight: 500;
    line-height: 1.4;
}
.fact-card.fact-time  { border-left-color: #805ad5; }
.fact-card.fact-pair  { border-left-color: #d53f8c; }
.fact-card.fact-out   { border-left-color: var(--emp-out); }
.fact-card.fact-in    { border-left-color: var(--emp-in); }
.fact-card.fact-miss  { border-left-color: var(--emp-missed); }
.fact-card.fact-hour  { border-left-color: #dd6b20; }

/* ---------- Мелкий пояснительный текст ---------- */
.calls-source {
    font-size: 13px;
    color: var(--emp-muted);
    margin: 4px 0 16px 0;
    line-height: 1.6;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}

/* ---------- Адаптив ---------- */
@media (max-width: 900px) {
    .dept-row {
        grid-template-columns: minmax(0, 1fr) 20px;
        row-gap: 6px;
    }
    .dept-summary {
        grid-column: 1 / -1;
        grid-template-columns: repeat(3, 1fr);
        text-align: left;
    }
    .dept-toggle { grid-row: 1; grid-column: 2; }

    .load-chart-row {
        grid-template-columns: 1fr 70px;
        row-gap: 4px;
    }
    .load-chart-name {
        grid-column: 1 / -1;
    }
}

@media (max-width: 720px) {
    .calls-total { grid-template-columns: 1fr; }
    .calls-total .ct-label {
        padding: 12px 16px;
        border-bottom: 1px solid var(--emp-accent-border);
    }
    .calls-total .ct-cell {
        border-left: none;
        border-top: 1px solid var(--emp-accent-border);
        padding: 10px 16px;
    }
    .calls-table th, .calls-table td { padding: 8px 8px; }
    .load-chart { padding: 12px 14px; }
}
</style>
"""


# ---------- Рендер ----------
def _render_dept_table(rows: list) -> str:
    L = []
    L.append('<table class="calls-table">')
    L.append('  <colgroup>')
    L.append('    <col class="col-num">')
    L.append('    <col class="col-fio">')
    L.append('    <col class="col-stat">')
    L.append('    <col class="col-stat">')
    L.append('    <col class="col-stat">')
    L.append('  </colgroup>')
    L.append('  <thead>')
    L.append('    <tr>')
    L.append('      <th rowspan="2" class="col-num">№</th>')
    L.append('      <th rowspan="2" class="col-fio">ФИО</th>')
    L.append('      <th colspan="2">Входящие</th>')
    L.append('      <th rowspan="2" class="col-out">Исходящие</th>')
    L.append('    </tr>')
    L.append('    <tr>')
    L.append('      <th class="col-in">Принятые</th>')
    L.append('      <th class="col-miss">Пропущенные</th>')
    L.append('    </tr>')
    L.append('  </thead>')
    L.append('  <tbody>')
    for i, (fio, s, _) in enumerate(rows, start=1):
        L.append('    <tr>')
        L.append(f'      <td class="col-num">{i}</td>')
        L.append(f'      <td class="col-fio">{fio}</td>')
        L.append(f'      <td class="col-in">{s["incoming"]}</td>')
        L.append(f'      <td class="col-miss">{s["missed"]}</td>')
        L.append(f'      <td class="col-out">{s["outgoing"]}</td>')
        L.append('    </tr>')
    L.append('  </tbody>')
    L.append('</table>')
    return "\n".join(L)


def _fact_card(label: str, value: str, sub: str, cls: str) -> str:
    L = [f'<div class="fact-card {cls}">']
    L.append(f'  <div class="fact-label">{label}</div>')
    L.append(f'  <div class="fact-value">{value}</div>')
    if sub:
        L.append(f'  <div class="fact-sub">{sub}</div>')
    L.append('</div>')
    return "\n".join(L)


def _render_load_chart(dept_rows: list) -> str:
    """
    Горизонтальная гистограмма нагрузки по отделам.
    dept_rows — список (dept, d), где d содержит incoming, missed, outgoing, total_all.
    Ширина полосы = total_all / max(total_all) * 100%.
    Внутри полосы — три сегмента (принятые / пропущенные / исходящие).
    """
    if not dept_rows:
        return ""

    max_total = max(d["total_all"] for _, d in dept_rows)
    if max_total == 0:
        return ""

    L = []
    L.append('<div class="load-chart">')

    for dept, d in dept_rows:
        total = d["total_all"]
        width_pct = total / max_total * 100.0

        # доли сегментов внутри полосы (сумма = 100%)
        if total > 0:
            pct_in   = d["incoming"] / total * 100.0
            pct_miss = d["missed"]   / total * 100.0
            pct_out  = d["outgoing"] / total * 100.0
        else:
            pct_in = pct_miss = pct_out = 0.0

        L.append('<div class="load-chart-row">')
        L.append(f'  <div class="load-chart-name" title="{dept}">{dept}</div>')
        L.append('  <div class="load-chart-bar-wrap">')
        L.append(f'    <div class="load-chart-bar" style="width: {width_pct:.2f}%;">')
        L.append(
            f'      <div class="load-chart-seg seg-in" '
            f'style="width: {pct_in:.2f}%;" title="Принятые: {d["incoming"]}"></div>'
        )
        L.append(
            f'      <div class="load-chart-seg seg-miss" '
            f'style="width: {pct_miss:.2f}%;" title="Пропущенные: {d["missed"]}"></div>'
        )
        L.append(
            f'      <div class="load-chart-seg seg-out" '
            f'style="width: {pct_out:.2f}%;" title="Исходящие: {d["outgoing"]}"></div>'
        )
        L.append('    </div>')
        L.append('  </div>')
        L.append(f'  <div class="load-chart-value">{total}</div>')
        L.append('</div>')

    # Легенда
    L.append('  <div class="load-chart-legend">')
    L.append(
        '    <span class="load-chart-legend-item">'
        '<span class="load-chart-legend-dot legend-in"></span>принятые</span>'
    )
    L.append(
        '    <span class="load-chart-legend-item">'
        '<span class="load-chart-legend-dot legend-miss"></span>пропущенные</span>'
    )
    L.append(
        '    <span class="load-chart-legend-item">'
        '<span class="load-chart-legend-dot legend-out"></span>исходящие</span>'
    )
    L.append('  </div>')

    L.append('</div>')
    return "\n".join(L)


def render_md(data: dict) -> str:
    stats = data["stats"]
    meta = data["meta"]
    dept_meta = data.get("dept_meta", {})

    all_rows = []
    for fio, s in stats.items():
        total = s["incoming"] + s["missed"] + s["outgoing"]
        if total == 0:
            continue
        all_rows.append((fio, s, total))

    total_in     = sum(s["incoming"] for _, s, _ in all_rows)
    total_missed = sum(s["missed"]   for _, s, _ in all_rows)
    total_out    = sum(s["outgoing"] for _, s, _ in all_rows)

    dept_buckets = {dept: [] for dept in DEPARTMENTS}
    dept_buckets["Прочие / не указано"] = []

    for fio, s, total in all_rows:
        dept = get_department(fio)
        if dept not in dept_buckets:
            dept = "Прочие / не указано"
        dept_buckets[dept].append((fio, s, total))

    for dept in dept_buckets:
        dept_buckets[dept].sort(key=lambda x: x[2], reverse=True)

    ordered_depts = list(DEPARTMENTS.keys())
    if dept_buckets.get("Прочие / не указано"):
        ordered_depts.append("Прочие / не указано")

    L = []
    L.append(HTML_HEADER)
    L.append("")
    L.append("# Статистика звонков за сентябрь 2026")
    L.append("")

    # ---------- Плашка «Всего звонков» ----------
    L.append('<div class="calls-total">')
    L.append('  <div class="ct-label">Всего звонков</div>')
    L.append('  <div class="ct-cell ct-in">')
    L.append(f'    <div class="ct-value">{total_in}</div>')
    L.append('    <div class="ct-caption">Принятые</div>')
    L.append('  </div>')
    L.append('  <div class="ct-cell ct-miss">')
    L.append(f'    <div class="ct-value">{total_missed}</div>')
    L.append('    <div class="ct-caption">Пропущенные</div>')
    L.append('  </div>')
    L.append('  <div class="ct-cell ct-out">')
    L.append(f'    <div class="ct-value">{total_out}</div>')
    L.append('    <div class="ct-caption">Исходящие</div>')
    L.append('  </div>')
    L.append('</div>')
    L.append("")

    # ---------- 1. Детализация по подразделениям ----------
    L.append("## Детализация по подразделениям")
    L.append("")
    L.append('<div class="dept-list">')

    num = 0
    for dept in ordered_depts:
        rows = dept_buckets.get(dept) or []
        if not rows:
            continue
        num += 1
        dept_in    = sum(r[1]["incoming"] for r in rows)
        dept_miss  = sum(r[1]["missed"]   for r in rows)
        dept_out   = sum(r[1]["outgoing"] for r in rows)

        cb_id = f"dept-{num}"
        L.append('  <div class="dept-item">')
        L.append(f'    <input type="checkbox" id="{cb_id}" class="dept-checkbox">')
        L.append(f'    <label for="{cb_id}" class="dept-row">')
        L.append(f'      <span class="dept-name">{dept}</span>')
        L.append('      <span class="dept-summary">')
        L.append(f'        <span class="ds-cell"><span class="ds-label">принято:</span> <b>{dept_in}</b></span>')
        L.append(f'        <span class="ds-cell"><span class="ds-label">пропущено:</span> <b>{dept_miss}</b></span>')
        L.append(f'        <span class="ds-cell"><span class="ds-label">исходящих:</span> <b>{dept_out}</b></span>')
        L.append('      </span>')
        L.append('      <span class="dept-toggle">›</span>')
        L.append('    </label>')
        L.append('    <div class="dept-details">')
        L.append(_render_dept_table(rows))
        L.append('    </div>')
        L.append('  </div>')

    L.append('</div>')
    L.append("")

    # ---------- 2. Нагрузка отделов ----------
    
    L.append("## Нагрузка отделов")
    L.append("")
    L.append('<div class="calls-source">'
             'Сводные показатели по подразделениям. '
             '«Доля пропущенных» — процент входящих вызовов, '
             'не завершившихся разговором. '
             '«Индекс исх./вх.» — отношение исходящих к сумме входящих '
             '(>1 — отдел больше инициирует, <1 — больше принимает).'
             '</div>')
    L.append("")

    dept_rows = []
    for dept, d in dept_meta.items():
        if d["employees"] == 0 or d["total_all"] == 0:
            continue
        dept_rows.append((dept, d))

    dept_rows.sort(key=lambda x: x[1]["total_all"], reverse=True)

    # Гистограмма
    L.append(_render_load_chart(dept_rows))
    L.append("")

    # Сводные выводы
    L.append('<div class="facts-grid">')

    if dept_rows:
        most_out = max(dept_rows, key=lambda x: x[1]["outgoing"])
        most_in  = max(dept_rows, key=lambda x: x[1]["incoming"])
        worst_miss = max(dept_rows, key=lambda x: x[1]["miss_rate"])
        best_miss  = min(dept_rows, key=lambda x: x[1]["miss_rate"])
        most_active = max(dept_rows, key=lambda x: x[1]["total_all"])

        total_all_sum = sum(d["total_all"] for _, d in dept_rows)
        total_emp_sum = sum(d["employees"] for _, d in dept_rows)
        avg_per_emp = round(total_all_sum / total_emp_sum) if total_emp_sum else 0

        L.append(_fact_card(
            "Наибольшее число исходящих",
            most_out[0],
            f'{most_out[1]["outgoing"]} исходящих звонков',
            "fact-out",
        ))
        L.append(_fact_card(
            "Наибольшее число принятых",
            most_in[0],
            f'{most_in[1]["incoming"]} принятых звонков',
            "fact-in",
        ))
        L.append(_fact_card(
            "Наибольшая доля пропущенных",
            worst_miss[0],
            f'{worst_miss[1]["missed"]} из {worst_miss[1]["total_in"]} '
            f'входящих · {worst_miss[1]["miss_rate"] * 100:.1f}%',
            "fact-miss",
        ))
        L.append(_fact_card(
            "Наилучший приём вызовов",
            best_miss[0],
            f'{best_miss[1]["incoming"]} из {best_miss[1]["total_in"]} '
            f'входящих · принято {(1 - best_miss[1]["miss_rate"]) * 100:.1f}%',
            "fact-in",
        ))

        most_extrovert = max(dept_rows, key=lambda x: x[1]["out_in_ratio"])
        most_introvert = min(dept_rows, key=lambda x: x[1]["out_in_ratio"])

        L.append(_fact_card(
            "Преобладание исходящих связей",
            most_extrovert[0],
            f'Индекс исх./вх. = {most_extrovert[1]["out_in_ratio"]:.2f}'
            ' — отдел больше инициирует, чем принимает',
            "fact-out",
        ))
        L.append(_fact_card(
            "Преобладание входящих связей",
            most_introvert[0],
            f'Индекс исх./вх. = {most_introvert[1]["out_in_ratio"]:.2f}'
            ' — отдел больше принимает, чем инициирует',
            "fact-in",
        ))
        L.append(_fact_card(
            "Средняя нагрузка на сотрудника",
            f'{avg_per_emp} звонков / мес.',
            f'Всего в организации: {total_all_sum} звонков, {total_emp_sum} сотрудников',
            "fact-hour",
        ))
        L.append(_fact_card(
            "Наибольший суммарный объём",
            most_active[0],
            f'{most_active[1]["total_all"]} звонков всех типов',
            "fact-pair",
        ))

    L.append('</div>')
    L.append("")

    # ---------- 3. Статистика ----------
    L.append('<div style="height:32px;"></div>')
    L.append("## Нагрузка сотрудников")
    L.append("")
    L.append('<div class="facts-grid">')

    lc = meta.get("longest_call")
    if lc:
        L.append(_fact_card(
            "Максимальная длительность звонка",
            f'{lc["initiator"]} → {lc["target"]}',
            f'Длительность: {fmt_duration(lc["duration"])}'
            + (f' · {lc["start"]}' if lc["start"] else ''),
            "fact-time",
        ))

    tp = meta.get("top_pair")
    if tp:
        L.append(_fact_card(
            "Наиболее частая пара абонентов",
            f'{tp["a"]} ⇄ {tp["b"]}',
            f'Всего звонков: {tp["count"]}',
            "fact-pair",
        ))

    ti = meta.get("top_initiator")
    if ti:
        L.append(_fact_card(
            "Лидер по исходящим звонкам",
            ti["fio"],
            f'Исходящих: {ti["count"]}',
            "fact-out",
        ))

    tt = meta.get("top_target")
    if tt:
        L.append(_fact_card(
            "Лидер по принятым звонкам",
            tt["fio"],
            f'Принятых: {tt["count"]}',
            "fact-in",
        ))

    tmr = meta.get("top_missed_rate")
    if tmr:
        L.append(_fact_card(
            "Наибольшая доля пропущенных звонков",
            tmr["fio"],
            f'{tmr["missed"]} из {tmr["total_in"]} входящих · {tmr["percent"]}%',
            "fact-miss",
        ))

    ba = meta.get("best_answer")
    if ba:
        L.append(_fact_card(
            "Наилучший приём звонков",
            ba["fio"],
            f'{ba["incoming"]} из {ba["total_in"]} входящих · {ba["percent"]}%',
            "fact-in",
        ))

    ph = meta.get("peak_hour")
    if ph:
        L.append(_fact_card(
            "Час пиковой нагрузки",
            f'{ph["hour"]:02d}:00 – {ph["hour"]:02d}:59',
            f'Звонков: {ph["count"]}',
            "fact-hour",
        ))

    L.append('</div>')
    L.append("")

    return "\n".join(L)


# ---------- Точка входа ----------
def main():
    data = parse_calls()
    print(f"[parse_calls] Обработано абонентов: {len(data['stats'])}")

    unknown = [fio for fio in data["stats"] if get_department(fio) == "Прочие / не указано"]
    if unknown:
        print("[parse_calls] Не сопоставлены со справочником:")
        for fio in sorted(unknown):
            print(f"    {fio!r}")

    MD_PATH.parent.mkdir(parents=True, exist_ok=True)
    MD_PATH.write_text(render_md(data), encoding="utf-8")
    print(f"[parse_calls] Записано: {MD_PATH}")


if __name__ == "__main__":
    main()