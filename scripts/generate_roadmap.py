#!/usr/bin/env python3

# Данные задач (замените на реальные при интеграции)
tasks = [
    # Этап 1
    {"title": "Концепция, цели и задачи проекта", "status": "✅ Завершено", "deadline": "13–20.05.2025", "assignee": "Исполнитель", "stage": 1},
    {"title": "Согласована бизнес-модель", "status": "✅ Завершено", "deadline": "17.11.2025", "assignee": "Исполнитель", "stage": 1},
    {"title": "ТЗ согласовано", "status": "✅ Завершено", "deadline": "15.12.2025", "assignee": "Исполнитель", "stage": 1},

    # Этап 2
    {"title": "Сервис группового администрирования прав", "status": "🔸 В работе", "deadline": "14.04–14.05.2026", "assignee": "Исполнитель", "stage": 2},
    {"title": "Подготовлен MVP (standalone DB)", "status": "✅ Завершено", "deadline": "24.11.2025", "assignee": "Исполнитель", "stage": 2},

    # Этап 3
    {"title": "Тестовые испытания (тестовая среда)", "status": "🔴 Запланировано", "deadline": "30.04.2026", "assignee": "Исполнитель", "stage": 3},
]

from datetime import datetime

# Группировка
s1 = [t for t in tasks if t["stage"] == 1]
s2 = [t for t in tasks if t["stage"] == 2]
s3 = [t for t in tasks if t["stage"] == 3]

# Подсчёт
s1_done = len(s1)
s2_done = len([t for t in s2 if "Завершено" in t["status"]])
s2_in_progress = len(s2) - s2_done
s3_planned = len(s3)

# Генерация Markdown
md = f"""# 🗓 План реализации миграции в ГИС «Смета ЯНАО» (2025–2026)

> ⚡ Обновлено: {datetime.now().strftime('%d.%m.%Y %H:%M')}

---

## 📊 Общий прогресс проекта

<div class="roadmap-progress">
<div class="roadmap-card">
<strong>Этап 1: Подготовка и согласование</strong>
<div class="roadmap-bar"><span style="width:100%"></span></div>
<span>{s1_done} из {len(s1)} задач</span>
</div>
<div class="roadmap-card">
<strong>Этап 2: Разработка и тестирование</strong>
<div class="roadmap-bar"><span style="width:{int((s2_done/len(s2))*100) if s2 else 0}%"></span></div>
<span>{s2_done} завершено, {s2_in_progress} в работе</span>
</div>
<div class="roadmap-card">
<strong>Этап 3: Тестирование и внедрение</strong>
<div class="roadmap-bar"><span style="width:0%"></span></div>
<span>{s3_planned} задач запланировано</span>
</div>
</div>

---

## 📦 Этап 1: Подготовка и согласование

<details open>
<summary><strong>✅ {s1_done} задач завершено</strong></summary>

"""
for t in s1:
    md += f"- **{t['title']}**\n  - Статус: {t['status']}\n  - Срок: {t['deadline']}\n  - Ответственный: {t['assignee']}\n\n"

md += """</details>

---

## ⚙️ Этап 2: Разработка и тестирование

"""
md += f"""<details>
<summary><strong>🔸 {s2_in_progress} в работе, ✅ {s2_done} завершено</strong></summary>

"""
for t in s2:
    md += f"- **{t['title']}**\n  - Статус: {t['status']}\n  - Срок: {t['deadline']}\n  - Ответственный: {t['assignee']}\n\n"

md += """</details>

---

## 🧪 Этап 3: Тестирование и внедрение

"""
md += f"""<details>
<summary><strong>🔴 {s3_planned} задач запланировано</strong></summary>

"""
for t in s3:
    md += f"- **{t['title']}**\n  - Статус: {t['status']}\n  - Срок: {t['deadline']}\n  - Ответственный: {t['assignee']}\n\n"

md += """</details>
"""

# Сохранение
with open("docs/roadmap.md", "w", encoding="utf-8") as f:
    f.write(md)

print("docs/roadmap.md updated.")