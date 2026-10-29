#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Генератор еженедельного отчета по заявкам ТП Криста.
Показывает данные за 2 последние недели в 2 колонках.
Добавляет периоды в TOC MkDocs Material через настоящие Markdown-заголовки H3.
"""
import os
import re
import glob
from openpyxl import load_workbook

DOCS_DIR = 'docs'
OUTPUT_FILE = os.path.join(DOCS_DIR, 'zayavka_week.md')


def find_latest_reports(count=2):
    """Находит последние N файлов отчетов по заявкам"""
    pattern = os.path.join(DOCS_DIR, 'Заявки ТП Криста с *.xlsx')
    files = glob.glob(pattern)
    if not files:
        return []
    # Сортируем по дате модификации (новые первые)
    files.sort(key=os.path.getmtime, reverse=True)
    return files[:count]


def extract_period_from_filename(filename):
    """Извлекает период из имени файла"""
    basename = os.path.basename(filename)
    match = re.search(r'с\s+(\d{2}\.\d{2})\s+по\s+(\d{2}\.\d{2})', basename)
    if match:
        return f"{match.group(1)} по {match.group(2)}"
    return "неизвестный период"


def make_anchor_id(period, col_index):
    """Создает безопасный уникальный ID для якоря TOC"""
    safe = re.sub(r'[^0-9a-zA-Zа-яА-Я]+', '-', period).strip('-').lower()
    return f"week-{col_index}-{safe}"


def process_tickets(filepath):
    """Обрабатывает файл заявок и возвращает статистику по отправителям"""
    try:
        wb = load_workbook(filepath, data_only=True, read_only=True)

        # Используем лист "Статистика по Отправителю"
        if 'Статистика по Отправителю' in wb.sheetnames:
            ws = wb['Статистика по Отправителю']
            sender_stats = {}

            for row in ws.iter_rows(min_row=2, values_only=True):
                if not row or len(row) < 2:
                    continue

                sender = row[0]
                count = row[1]

                if not sender or not count:
                    continue

                sender_str = str(sender).strip()
                # Пропускаем итоговую строку
                if 'общий итог' in sender_str.lower() or sender_str == '':
                    continue

                try:
                    # Защита от ArrayFormula и прочих нестандартных типов openpyxl
                    if isinstance(count, (int, float, str)):
                        count_int = int(float(count))
                    else:
                        # Если это формула массива или другой объект — пропускаем
                        continue
                    sender_stats[sender_str] = count_int
                except (ValueError, TypeError):
                    continue

            wb.close()
            return sender_stats

        # Fallback: если листа нет, парсим лист "Заявки"
        if 'Заявки' not in wb.sheetnames:
            print(f"⚠️  Лист 'Заявки' не найден в {filepath}")
            wb.close()
            return None

        ws = wb['Заявки']

        # Ищем колонку "Отправитель"
        sender_col_idx = None
        for row_idx, row in enumerate(ws.iter_rows(min_row=1, max_row=10, values_only=True), start=1):
            if row:
                for idx, cell in enumerate(row):
                    if cell and 'отправитель' in str(cell).lower():
                        sender_col_idx = idx
                        break
            if sender_col_idx is not None:
                break

        if sender_col_idx is None:
            print("⚠️  Колонка 'Отправитель' не найдена")
            wb.close()
            return None

        from collections import Counter
        sender_counter = Counter()

        for row in ws.iter_rows(min_row=2, values_only=True):
            if row and len(row) > sender_col_idx:
                sender = row[sender_col_idx]
                if sender:
                    sender_counter[str(sender).strip()] += 1

        wb.close()
        return dict(sender_counter)

    except Exception as e:
        print(f"⚠️  Ошибка обработки файла: {e}")
        import traceback
        traceback.print_exc()
        return None


def generate_week_toc_heading(period, col_index):
    """
    Генерирует настоящий Markdown-заголовок H3, который Python-Markdown
    включит в TOC. Визуально скрывается CSS-классом .toc-hidden.
    Синтаксис {#id .class} работает благодаря расширению attr_list
    (в MkDocs Material включено по умолчанию).
    """
    anchor_id = make_anchor_id(period, col_index)
    return f'### Период: {period} {{#{anchor_id} .toc-hidden}}'


def generate_week_column(sender_stats, period, col_index):
    """Генерирует HTML для одной колонки (одной недели)."""
    sorted_stats = sorted(sender_stats.items(), key=lambda x: x[1], reverse=True)
    total = sum(count for _, count in sorted_stats)

    visible_count = 10
    visible_rows = sorted_stats[:visible_count]
    hidden_rows = sorted_stats[visible_count:]

    lines = []
    lines.append(f'<div class="week-column">')
    lines.append(f'  <div class="week-period">Период: {period}</div>')
    # Уникальный ID для таблицы, чтобы JS мог найти именно её
    lines.append(f'  <table class="ticket-table" id="table-{col_index}">')
    lines.append('    <thead>')
    lines.append('      <tr>')
    lines.append('        <th>Отправитель</th>')
    lines.append('        <th>Заявок</th>')
    lines.append('      </tr>')
    lines.append('    </thead>')
    lines.append('    <tbody>')

    # Видимые строки
    for sender, count in visible_rows:
        lines.append('      <tr>')
        lines.append(f'        <td>{sender}</td>')
        lines.append(f'        <td class="ticket-count">{count}</td>')
        lines.append('      </tr>')

    # Скрытые строки (добавляются в ту же таблицу для сохранения стилей)
    for sender, count in hidden_rows:
        lines.append(f'      <tr class="ticket-hidden-row" style="display: none;">')
        lines.append(f'        <td>{sender}</td>')
        lines.append(f'        <td class="ticket-count">{count}</td>')
        lines.append('      </tr>')

    # Итоговая строка
    lines.append(f'      <tr class="total-row">')
    lines.append(f'        <td>Итого:</td>')
    lines.append(f'        <td class="ticket-count">{total}</td>')
    lines.append(f'      </tr>')

    lines.append('    </tbody>')
    lines.append('  </table>')

    if hidden_rows:
        # Передаем индекс колонки в функцию toggleWeek
        lines.append(f'  <button class="toggle-btn" onclick="toggleWeek({col_index})" data-col="{col_index}">')
        lines.append(f'    <span class="toggle-icon">›</span>')
        lines.append(f'    Показать ещё {len(hidden_rows)} записей')
        lines.append(f'  </button>')

    lines.append(f'</div>')

    return '\n'.join(lines)


def generate_markdown(weeks_data):
    """Генерирует Markdown: настоящие H3 для TOC + HTML-грид для таблиц."""
    lines = []
    lines.append('## Направленные заявки за неделю')
    lines.append('')

    # 1) Сначала — настоящие Markdown-заголовки H3 для TOC
    for idx, (filepath, period, stats) in enumerate(weeks_data, start=1):
        if stats:
            lines.append(generate_week_toc_heading(period, idx))
    lines.append('')

    # 2) Затем — HTML-грид с колонками
    lines.append('<div class="weeks-grid">')
    for idx, (filepath, period, stats) in enumerate(weeks_data, start=1):
        if stats:
            lines.append(generate_week_column(stats, period, idx))
    lines.append('</div>')
    lines.append('')

    return '\n'.join(lines)


STYLES = '''<style>
.weeks-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr); /* Ровно 2 колонки одинаковой ширины */
  gap: 40px; /* Большой отступ между колонками */
  margin: 20px 0;
  align-items: start;
}
.week-column {
  width: 100%;
  min-width: 0; /* Позволяет сжиматься при необходимости */
}
.week-period {
  font-weight: 600;
  margin-bottom: 8px;
  color: #2c3e50;
  font-size: 14px;
}
.ticket-table {
  width: 100%;
  border-collapse: collapse;
  background: #fff;
  border: 1px solid #e0e4e8;
  border-radius: 6px;
  overflow: hidden;
  font-size: 14px; /* Шрифт 14px */
  margin-bottom: 4px;
}
.ticket-table thead th {
  background: #f5f7fa;
  color: #2c3e50;
  text-align: left;
  font-weight: 600;
  padding: 6px 10px;
  border-bottom: 1px solid #e0e4e8;
  font-size: 14px;
}
.ticket-table thead th:last-child {
  text-align: center;
  width: 70px;
}
.ticket-table tbody td {
  padding: 5px 10px;
  border-bottom: 1px solid #eef2f6;
  color: #2d3748;
  font-size: 14px;
}
.ticket-table tbody td.ticket-count {
  text-align: center;
}
.ticket-table tbody tr:last-child td {
  border-bottom: none;
}
.total-row td {
  background: #fafbfc;
  font-weight: 600;
  border-top: 2px solid #e0e4e8;
  padding: 8px 10px;
}
.toggle-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  background: #f5f7fa;
  border: 1px solid #e0e4e8;
  border-radius: 4px;
  color: #2b6cb0;
  font-size: 13px;
  cursor: pointer;
  margin-top: 8px;
  transition: all 0.15s;
}
.toggle-btn:hover {
  background: #eaf4ff;
  border-color: #bee3f8;
}
.toggle-icon {
  display: inline-block;
  font-size: 16px;
  font-weight: 700;
  transition: transform 0.15s;
}
.toggle-btn.open .toggle-icon {
  transform: rotate(90deg);
}
/* Скрываем H3 из TOC визуально, но оставляем в структуре для MkDocs */
h3.toc-hidden {
  display: none !important;
}
/* Адаптивность: на узких экранах переходим в 1 колонку */
@media (max-width: 900px) {
  .weeks-grid {
    grid-template-columns: 1fr;
    gap: 30px;
  }
}
</style>'''

SCRIPT = '''<script>
function toggleWeek(colIndex) {
  // Ищем таблицу по уникальному ID
  var table = document.getElementById('table-' + colIndex);
  if (!table) return;

  var hiddenRows = table.querySelectorAll('.ticket-hidden-row');
  if (!hiddenRows || hiddenRows.length === 0) return;

  // Проверяем состояние первой скрытой строки
  var isHidden = hiddenRows[0].style.display === 'none';

  // Переключаем все скрытые строки в этой таблице
  for (var i = 0; i < hiddenRows.length; i++) {
    hiddenRows[i].style.display = isHidden ? '' : 'none';
  }

  // Находим кнопку по атрибуту data-col
  var btn = document.querySelector('button[data-col="' + colIndex + '"]');
  if (!btn) return;

  if (isHidden) {
    btn.classList.add('open');
    btn.innerHTML = '<span class="toggle-icon" style="transform: rotate(90deg);">›</span> Скрыть записи';
  } else {
    btn.classList.remove('open');
    btn.innerHTML = '<span class="toggle-icon">›</span> Показать ещё ' + hiddenRows.length + ' записей';
  }
}
</script>'''


def main():
    print('🔍 Поиск файлов отчетов...')
    files = find_latest_reports(2)

    if not files:
        print('❌ Файлы отчетов не найдены в папке docs/')
        print('   Ожидаемый формат: "Заявки ТП Криста с ДД.ММ по ДД.ММ.xlsx"')
        return

    print(f'✅ Найдено файлов: {len(files)}')
    for f in files:
        print(f'   - {os.path.basename(f)}')

    weeks_data = []
    for filepath in files:
        period = extract_period_from_filename(filepath)
        print(f'📅 Период: {period}')

        print(' Обработка данных...')
        stats = process_tickets(filepath)

        if stats is None:
            print(f'⚠️  Не удалось обработать файл: {os.path.basename(filepath)}')
            continue

        print(f'📋 Найдено отправителей: {len(stats)}')
        print(f'📝 Всего заявок: {sum(stats.values())}')

        weeks_data.append((filepath, period, stats))

    if not weeks_data:
        print('❌ Не удалось обработать ни один файл')
        return

    markdown = generate_markdown(weeks_data)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(STYLES)
        f.write('\n')
        f.write(markdown)
        f.write('\n')
        f.write(SCRIPT)

    print(f'✅ Отчет сохранен: {OUTPUT_FILE}')


if __name__ == '__main__':
    main()