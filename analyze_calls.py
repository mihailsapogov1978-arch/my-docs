#!/usr/bin/env python3
"""
Анализ CDR-звонков по ФИО для MkDocs с Material Theme.
Генерирует docs/calls_by_person.md с Mermaid-диаграммами.
"""

import pandas as pd
import numpy as np
from pathlib import Path

# === Настройки ===
INPUT_FILE = Path("docs/calls/calls.xlsx")
OUTPUT_FILE = Path("docs/calls_by_person.md")

def load_and_clean_data():
    """Загружает и очищает CDR-данные."""
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Файл не найден: {INPUT_FILE}")

    # Чтение Excel
    df = pd.read_excel(INPUT_FILE, engine="openpyxl", dtype=str)

    # Очистка колонок ФИО
    for col in ["Имя инициатора", "Имя адресата вызова"]:
        if col in df.columns:
            df[col] = df[col].fillna("").astype(str).str.strip()

    # Преобразование числовых полей
    numeric_cols = [
        "Продолжительность вызова",
        "Число потерянных медиапакетов во вх.вызове",
        "Число потерянных медиапакетов на исх. участке вызова"
    ]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").astype('float64')

    # Вычисление общих потерь
    df["Потери всего"] = (
        df["Число потерянных медиапакетов во вх.вызове"].fillna(0) +
        df["Число потерянных медиапакетов на исх. участке вызова"].fillna(0)
    )

    # === Гибкое преобразование дат ===
    date_cols = ["Дата создания CDR", "Время старта"]
    for col in date_cols:
        if col in df.columns:
            # Пробуем несколько подходов
            df[col] = pd.to_datetime(
                df[col],
                format=None,      # Автоматическое определение формата
                errors="coerce",  # Некорректные → NaT
                dayfirst=True     # Приоритет DD.MM.YYYY
            )

    # Фильтрация записей
    df = df[
        (df["Имя инициатора"] != "") &
        (df["Имя адресата вызова"] != "")
    ].copy()

    print(f"✅ Загружено {len(df)} записей CDR")
    return df

def generate_markdown(df):
    """Генерирует Markdown-контент с Mermaid-диаграммами."""
    total = len(df)
    successful = df["Результат вызова конечного получателя"].str.contains("Соединение установлено").sum()
    failed = total - successful

    # Безопасное извлечение периода
    min_date = df['Дата создания CDR'].min()
    max_date = df['Дата создания CDR'].max()
    
    if pd.isna(min_date) or pd.isna(max_date):
        date_range = "—"
    else:
        date_range = f"{min_date.strftime('%d.%m.%Y')} – {max_date.strftime('%d.%m.%Y')}"

    # Статистика по инициаторам
    initiator_stats = df.groupby("Имя инициатора").agg(
        calls=("Имя инициатора", "count"),
        failed=("Результат вызова конечного получателя", lambda x: (x == "Попытка вызова прекращена").sum())
    ).sort_values("calls", ascending=False).reset_index()

    top_initiators = initiator_stats.head(10)
    top_recipients = df.groupby("Имя адресата вызова").size().sort_values(ascending=False).head(15).reset_index()
    top_recipients.columns = ["ФИО", "Количество"]

    # === Подготовка данных для Mermaid ===
    init_labels = []
    init_values = []
    for _, row in top_initiators.iterrows():
        name = str(row["Имя инициатора"]).replace('"', '').replace('\n', ' ').strip()[:15]
        init_labels.append(f'"{name}"')
        init_values.append(str(int(row["calls"])))
    init_labels_str = ", ".join(init_labels)
    init_values_str = ", ".join(init_values)

    # === Сборка Markdown по частям ===
    lines = []

    # Заголовок
    lines.append("# Анализ CDR-звонков по ФИО\n")
    lines.append(f"Период: {date_range}\n")

    # Общая статистика
    lines.append("## 📊 Общая статистика\n")
    lines.append(f"- **Всего звонков**: {total:,}")
    lines.append(f"- **Успешные**: {successful:,} ({successful/total*100:.1f}%)")
    lines.append(f"- **Неудачные**: {failed:,} ({failed/total*100:.1f}%)\n")

    # Диаграммы
    lines.append("## 📈 Диаграммы\n")

    # xychart: Топ-10 инициаторов
    lines.append("### Топ-10 инициаторов звонков\n")
    lines.append("```mermaid")
    lines.append("xychart-beta")
    lines.append("    title Кол-во звонков (Топ-10)")
    lines.append("    x-axis \"Инициатор\"")
    lines.append("    y-axis \"Количество\"")
    lines.append(f"    line [{init_values_str}]")
    lines.append(f"    labels [{init_labels_str}]")
    lines.append("```\n")

    # pie: Распределение по статусам
    lines.append("### Распределение по статусам\n")
    lines.append("```mermaid")
    lines.append("pie")
    lines.append("    title Успешные vs Неудачные")
    lines.append(f'    "Успешные": {successful}')
    lines.append(f'    "Неудачные": {failed}')
    lines.append("```\n")

    # Топ-10 инициаторов (таблица)
    lines.append("## 👥 Топ-10 инициаторов\n")
    lines.append("| # | ФИО | Звонки | Неудачные |")
    lines.append("|---|-----|--------|-----------|")
    for i, (_, row) in enumerate(top_initiators.iterrows()):
        lines.append(f"| {i+1} | {row['Имя инициатора']} | {int(row['calls'])} | {int(row['failed'])} |")

    # Топ-15 адресатов (таблица)
    lines.append("\n## 📞 Топ-15 адресатов\n")
    lines.append("| # | ФИО | Количество |")
    lines.append("|---|-----|------------|")
    for i, (_, row) in enumerate(top_recipients.iterrows()):
        lines.append(f"| {i+1} | {row['ФИО']} | {row['Количество']} |")

    return "\n".join(lines)

def main():
    try:
        df = load_and_clean_data()
        markdown_content = generate_markdown(df)
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(markdown_content)
        print(f"✅ Отчёт сохранён: {OUTPUT_FILE}")
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()