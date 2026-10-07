#!/usr/bin/env python3
"""
Парсер CDR-звонков из docs/calls/calls_09.xlsx
Формирует docs/calls/calls.md со статистикой по сотрудникам,
сгруппированной по структурным подразделениям.

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
}


# ---------- Полный стоп-лист ФИО (полностью исключаем из статистики) ----------
EXCLUDE_FIOS = {
    "Подгайный Алексей Алексеевич",
}


def _norm_fio(s: str) -> str:
    """Нормализация ФИО для сравнения: нижний регистр, ё→е, одиночные пробелы."""
    if not s:
        return ""
    s = s.lower().replace("ё", "е")
    s = re.sub(r"\s+", " ", s).strip()
    return s


# Нормализованный стоп-лист исключений
_EXCLUDE_NORM = {_norm_fio(x) for x in EXCLUDE_FIOS}

# Индекс: чистое ФИО (в нижнем регистре) → отдел
_FIO_TO_DEPT = {}
for _dept, _fios in DEPARTMENTS.items():
    for _fio in _fios:
        _FIO_TO_DEPT[_norm_fio(_fio)] = _dept

# Индекс алиасов: грязное ФИО (в нижнем регистре) → чистое ФИО (в нижнем регистре)
_ALIAS_TO_CLEAN = {_norm_fio(k): _norm_fio(v) for k, v in FIO_ALIASES.items()}

# Индекс: нормализованное чистое ФИО → каноничное написание из DEPARTMENTS
_CLEAN_KEY_TO_CANON = {}
for _dept, _fios in DEPARTMENTS.items():
    for _f in _fios:
        _CLEAN_KEY_TO_CANON[_norm_fio(_f)] = _f


def is_excluded(fio: str) -> bool:
    """Проверка: ФИО в стоп-листе (по нормализованному ключу)."""
    if not fio:
        return False
    key = _norm_fio(fio)
    # проверяем и «как есть», и через алиасы
    clean_key = _ALIAS_TO_CLEAN.get(key, key)
    return key in _EXCLUDE_NORM or clean_key in _EXCLUDE_NORM


def resolve_fio(fio: str) -> str:
    """Приводит ФИО к каноничному виду из справочника (через алиасы, если заданы)."""
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
        # normalize → resolve через алиасы
        initiator   = resolve_fio(normalize_fio(row.get(c_initiator_name)))
        result      = str(row.get(c_result) or "").strip().lower()
        connected   = is_filled(row.get(c_connect))
        target_name = resolve_fio(normalize_fio(row.get(c_target_name)))
        target_num  = row.get(c_target_num)
        a_num       = row.get(c_a_num)

        # исключаем из подсчёта тех, кто в EXCLUDE_FIOS
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

        # мета-статистика — тоже без исключённых
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

    # ---------- Топы ----------
    MIN_INCOMING_FOR_RATE = 50  # порог для рейтинга по доле

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

        # рейтинг по доле пропущенных — только те, у кого входящих >= порога
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

    return {
        "stats": dict(stats),
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

/* ---------- Список отделов ---------- */
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

/* ---------- Таблица внутри отдела ---------- */
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


def render_md(data: dict) -> str:
    stats = data["stats"]
    meta = data["meta"]

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
    L.append("# Статистика звонков за месяц")
    L.append("")

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

    L.append("## Статистика")
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

    # Отладка: показать тех, кто не попал в справочник
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