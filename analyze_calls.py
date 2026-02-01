#!/usr/bin/env python3
"""
Анализ заявок техподдержки из Excel и генерация HTML-отчёта.
Ожидает файл: docs/calls/calls.xlsx
Создаёт: calls.html
"""

import pandas as pd
from pathlib import Path
import datetime

# Настройки
INPUT_FILE = Path("docs/calls/calls.xlsx")
OUTPUT_FILE = Path("calls.html")

# Ожидаемые колонки (адаптируйте под ваш файл)
EXPECTED_COLUMNS = [
    "Дата регистрации",
    "Приоритет",
    "Тема",
    "Модуль",
    "Статус",
    "Дата закрытия",
    "Организация"
]

def load_data():
    """Загружает и проверяет данные."""
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Файл не найден: {INPUT_FILE}")

    df = pd.read_excel(INPUT_FILE, engine="openpyxl")

    # Автоопределение колонок, если заголовки в первой строке
    if not set(EXPECTED_COLUMNS).issubset(df.columns):
        print("⚠️  Колонки не совпадают. Используемые колонки:")
        print(df.columns.tolist())
        # Можно добавить логику маппинга, но пока просто используем то, что есть

    # Преобразование дат
    df["Дата регистрации"] = pd.to_datetime(df["Дата регистрации"], errors="coerce")
    df["Дата закрытия"] = pd.to_datetime(df["Дата закрытия"], errors="coerce")

    # Вычисление времени решения (в часах)
    df["Время решения (часы)"] = (
        (df["Дата закрытия"] - df["Дата регистрации"])
        .dt.total_seconds() / 3600
    ).round(1)

    return df

def generate_html(df):
    """Генерирует HTML-отчёт."""
    total = len(df)
    by_priority = df["Приоритет"].value_counts().to_dict()
    by_module = df["Модуль"].value_counts().head(5).to_dict()
    by_status = df["Статус"].value_counts().to_dict()

    # Среднее время решения по приоритетам
    avg_time = df.groupby("Приоритет")["Время решения (часы)"].mean().round(1).to_dict()

    # Ежедневная динамика
    daily = df.set_index("Дата регистрации").resample("D").size()
    daily_str = "\n".join([f'    "{date.strftime("%Y-%m-%d")}": {count},' for date, count in daily.items()])

    html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Анализ заявок техподдержки</title>
    <script type="module" src="https://unpkg.com/mermaid@10/dist/mermaid.esm.min.mjs"></script>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; margin: 2rem; }}
        h1, h2 {{ color: #2c3e50; }}
        .stats {{ display: flex; gap: 2rem; margin: 2rem 0; }}
        .stat-box {{ background: #f8f9fa; padding: 1rem; border-radius: 8px; min-width: 120px; }}
        .stat-value {{ font-size: 1.5em; font-weight: bold; color: #3498db; }}
        table {{ width: 100%; border-collapse: collapse; margin: 1.5rem 0; }}
        th, td {{ text-align: left; padding: 0.75rem; border-bottom: 1px solid #eee; }}
        th {{ background-color: #f8f9fa; }}
        .priority-1 {{ color: #e74c3c; }}
        .priority-2 {{ color: #f39c12; }}
        .priority-3 {{ color: #27ae60; }}
    </style>
</head>
<body>
    <h1>📊 Анализ заявок технической поддержки</h1>
    <p>Период: {df['Дата регистрации'].min().strftime('%d.%m.%Y')} – {df['Дата регистрации'].max().strftime('%d.%m.%Y')}</p>

    <div class="stats">
        <div class="stat-box">
            <div class="stat-value">{total}</div>
            <div>Всего заявок</div>
        </div>
        <div class="stat-box">
            <div class="stat-value">{by_priority.get('1', 0)}</div>
            <div class="priority-1">Приоритет 1</div>
        </div>
        <div class="stat-box">
            <div class="stat-value">{by_priority.get('2', 0)}</div>
            <div class="priority-2">Приоритет 2</div>
        </div>
        <div class="stat-box">
            <div class="stat-value">{by_priority.get('3', 0)}</div>
            <div class="priority-3">Приоритет 3</div>
        </div>
    </div>

    <h2>📈 Динамика заявок</h2>
    <div class="mermaid">
gantt
    title Заявки по дням
    dateFormat YYYY-MM-DD
    axisFormat %m-%d
{daily_str}
    </div>

    <h2>🧩 Топ-5 проблемных модулей</h2>
    <table>
        <thead>
            <tr><th>Модуль</th><th>Количество заявок</th></tr>
        </thead>
        <tbody>
"""
    for module, count in by_module.items():
        html += f"            <tr><td>{module}</td><td>{count}</td></tr>\n"

    html += """        </tbody>
    </table>

    <h2>⏱ Среднее время решения (часы)</h2>
    <table>
        <thead>
            <tr><th>Приоритет</th><th>Среднее время</th></tr>
        </thead>
        <tbody>
"""

    for prio in ['1', '2', '3']:
        time_val = avg_time.get(prio, 0)
        cls = f"class='priority-{prio}'"
        html += f"            <tr><td {cls}>Приоритет {prio}</td><td>{time_val}</td></tr>\n"

    html += """        </tbody>
    </table>

    <h2>📋 Статусы заявок</h2>
    <table>
        <thead>
            <tr><th>Статус</th><th>Количество</th></tr>
        </thead>
        <tbody>
"""

    for status, count in by_status.items():
        html += f"            <tr><td>{status}</td><td>{count}</td></tr>\n"

    html += """        </tbody>
    </table>

    <h2>🔍 Рекомендации</h2>
    <ul>
        <li>Уделить внимание модулям с наибольшим числом заявок — возможно, требуется дополнительное обучение или доработка</li>
        <li>Проверить соблюдение SLA по приоритету 1 (должно быть ≤ 4 часов)</li>
        <li>Анализировать повторяющиеся темы — выявить системные проблемы</li>
    </ul>

</body>
</html>
"""
    return html

def main():
    try:
        df = load_data()
        if df.empty:
            print("❌ Файл пустой")
            return

        html_content = generate_html(df)
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(html_content)

        print(f"✅ Отчёт сохранён: {OUTPUT_FILE.absolute()}")

    except Exception as e:
        print(f"❌ Ошибка: {e}")

if __name__ == "__main__":
    main()