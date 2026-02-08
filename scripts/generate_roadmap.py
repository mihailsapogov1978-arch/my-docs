#!/usr/bin/env python3
"""
Генерирует файл roadmap.md из данных GitHub Issues
"""

import os
import re
from datetime import datetime
from github import Github
from jinja2 import Template

# Получаем токен из переменной окружения
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
REPO_NAME = os.environ.get('GITHUB_REPOSITORY', 'mihailsapogov1978-arch/my-docs')

# Подключаемся к GitHub
g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)

# Получаем все открытые и закрытые задачи
issues = repo.get_issues(state='all', sort='created')

# Фильтруем только задачи (не пулл-реквесты)
tasks = [issue for issue in issues if not issue.pull_request]

# Группируем по этапам
roadmap = {
    'stage_1': {'completed': [], 'in_progress': [], 'planned': []},
    'stage_2': {'completed': [], 'in_progress': [], 'planned': []},
    'stage_3': {'completed': [], 'in_progress': [], 'planned': []},
}

for task in tasks:
    # Определяем этап по метке
    stage = 'stage_3'  # по умолчанию
    status = 'planned'
    
    for label in task.labels:
        if 'этап-1' in label.name or 'stage-1' in label.name:
            stage = 'stage_1'
        elif 'этап-2' in label.name or 'stage-2' in label.name:
            stage = 'stage_2'
        elif 'этап-3' in label.name or 'stage-3' in label.name:
            stage = 'stage_3'
        
        if 'завершено' in label.name or 'completed' in label.name:
            status = 'completed'
        elif 'в-работе' in label.name or 'in-progress' in label.name:
            status = 'in_progress'
    
    # Извлекаем срок из описания
    deadline = '—'
    if task.body:
        match = re.search(r'Срок:\s*(.+)', task.body)
        if match:
            deadline = match.group(1).strip()
    
    # Добавляем задачу
    task_data = {
        'number': task.number,
        'title': task.title,
        'status': status,
        'deadline': deadline,
        'assignee': task.assignee.login if task.assignee else '—',
        'url': task.html_url,
        'closed': task.closed_at,
    }
    
    roadmap[stage][status].append(task_data)

# Шаблон для генерации Markdown
TEMPLATE = '''# 🗓 План реализации миграции в ГИС «Смета ЯНАО» (2025–2026)

> ⚡ Обновлено автоматически: {{ updated }}

---

## 📊 Общий прогресс проекта

{% set total_1 = stage_1.completed | length + stage_1.in_progress | length + stage_1.planned | length %}
{% set total_2 = stage_2.completed | length + stage_2.in_progress | length + stage_2.planned | length %}
{% set total_3 = stage_3.completed | length + stage_3.in_progress | length + stage_3.planned | length %}

<div style="display: flex; gap: 20px; margin: 20px 0;">

<div style="flex: 1; background: #f5f5f5; padding: 15px; border-radius: 8px; border-left: 4px solid #4caf50;">
<strong style="display: block; margin-bottom: 8px;">Этап 1: Подготовка и согласование</strong>
<div style="background: #e0e0e0; height: 8px; border-radius: 4px; overflow: hidden;">
  <div style="width: {{ (total_1 > 0) and ((stage_1.completed | length * 100 / total_1) | round(0)) or 0 }}%; background: #4caf50; height: 100%;"></div>
</div>
<span style="font-size: 0.9em; color: #666;">{{ stage_1.completed | length }} из {{ total_1 }} задач</span>
</div>

<div style="flex: 1; background: #f5f5f5; padding: 15px; border-radius: 8px; border-left: 4px solid #ff9800;">
<strong style="display: block; margin-bottom: 8px;">Этап 2: Разработка и тестирование</strong>
<div style="background: #e0e0e0; height: 8px; border-radius: 4px; overflow: hidden;">
  <div style="width: {{ (total_2 > 0) and ((stage_2.completed | length * 100 / total_2) | round(0)) or 0 }}%; background: #ff9800; height: 100%;"></div>
</div>
<span style="font-size: 0.9em; color: #666;">{{ stage_2.completed | length }} из {{ total_2 }} задач</span>
</div>

<div style="flex: 1; background: #f5f5f5; padding: 15px; border-radius: 8px; border-left: 4px solid #f44336;">
<strong style="display: block; margin-bottom: 8px;">Этап 3: Тестирование и внедрение</strong>
<div style="background: #e0e0e0; height: 8px; border-radius: 4px; overflow: hidden;">
  <div style="width: {{ (total_3 > 0) and ((stage_3.completed | length * 100 / total_3) | round(0)) or 0 }}%; background: #f44336; height: 100%;"></div>
</div>
<span style="font-size: 0.9em; color: #666;">{{ stage_3.completed | length }} из {{ total_3 }} задач</span>
</div>

</div>

---

## 🚀 Критические вехи

| Дата | Событие | Статус |
|------|---------|--------|
{% for stage in ['stage_1', 'stage_2', 'stage_3'] %}
{% for task in roadmap[stage]['completed'] %}
| ✅ {{ task.deadline }} | {{ task.title }} | Завершено |
{% endfor %}
{% endfor %}
{% for task in roadmap['stage_2']['in_progress'] %}
| 🔸 {{ task.deadline }} | {{ task.title }} | В работе |
{% endfor %}
{% for task in roadmap['stage_2']['planned'] %}
| 🔴 {{ task.deadline }} | {{ task.title }} | Запланировано |
{% endfor %}
{% for task in roadmap['stage_3']['planned'] %}
| 🔴 {{ task.deadline }} | {{ task.title }} | Запланировано |
{% endfor %}

---

## 📦 Этап 1: Подготовка и согласование

<details>
<summary><strong>✅ {{ stage_1.completed | length }} задач завершено (100%)</strong></summary>

| № | Задача | Статус | Срок | Ответственный |
|---|--------|--------|------|---------------|
{% for task in stage_1.completed %}
| {{ task.number }} | [{{ task.title }}]({{ task.url }}) | ✅ Завершено | {{ task.deadline }} | {{ task.assignee }} |
{% endfor %}
</details>

---

## ⚙️ Этап 2: Разработка и тестирование

<details>
<summary><strong>🔸 {{ stage_2.completed | length }} завершено, {{ stage_2.in_progress | length }} в работе, {{ stage_2.planned | length }} запланировано</strong></summary>

| № | Задача | Статус | Срок | Ответственный |
|---|--------|--------|------|---------------|
{% for task in stage_2.completed %}
| {{ task.number }} | [{{ task.title }}]({{ task.url }}) | ✅ Завершено | {{ task.deadline }} | {{ task.assignee }} |
{% endfor %}
{% for task in stage_2.in_progress %}
| {{ task.number }} | [{{ task.title }}]({{ task.url }}) | 🔸 В работе | {{ task.deadline }} | {{ task.assignee }} |
{% endfor %}
{% for task in stage_2.planned %}
| {{ task.number }} | [{{ task.title }}]({{ task.url }}) | 🔴 Запланировано | {{ task.deadline }} | {{ task.assignee }} |
{% endfor %}
</details>

---

## 🧪 Этап 3: Тестирование и внедрение

<details>
<summary><strong>🔴 {{ stage_3.planned | length }} задач запланировано (0%)</strong></summary>

| № | Задача | Статус | Срок | Ответственный |
|---|--------|--------|------|---------------|
{% for task in stage_3.planned %}
| {{ task.number }} | [{{ task.title }}]({{ task.url }}) | 🔴 Запланировано | {{ task.deadline }} | {{ task.assignee }} |
{% endfor %}
</details>

---

## 📌 Сводка по статусам

| Статус | Количество |
|--------|------------|
| ✅ Завершено | {{ stage_1.completed | length + stage_2.completed | length + stage_3.completed | length }} |
| 🔸 В работе | {{ stage_1.in_progress | length + stage_2.in_progress | length + stage_3.in_progress | length }} |
| 🔴 Запланировано | {{ stage_1.planned | length + stage_2.planned | length + stage_3.planned | length }} |

---

> ℹ️ Данные обновляются автоматически при изменении задач в проекте. Последнее обновление: {{ updated }}
'''

# Генерируем файл
template = Template(TEMPLATE)
output = template.render(
    updated=datetime.now().strftime('%d.%m.%Y %H:%M'),
    roadmap=roadmap,
    **roadmap
)

# Сохраняем в файл
with open('docs/roadmap.md', 'w', encoding='utf-8') as f:
    f.write(output)

print(f'✅ Файл docs/roadmap.md успешно обновлён!')
print(f'📊 Статистика: {sum(len(s) for s in roadmap["stage_1"].values()) + sum(len(s) for s in roadmap["stage_2"].values()) + sum(len(s) for s in roadmap["stage_3"].values())} задач')