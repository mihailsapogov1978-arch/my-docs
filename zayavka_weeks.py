#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Генератор еженедельного отчета по заявкам ТП Криста.
Интерактивная диаграмма с группировкой по отделам и детализацией при клике.
"""
import os
import re
import glob
import json
from openpyxl import load_workbook
from collections import Counter

DOCS_DIR = 'docs'
OUTPUT_FILE = os.path.join(DOCS_DIR, 'zayavka_week.md')

# ===== НАСТРОЙКА: Сколько последних недель выводить =====
COUNT_WEEKS = 30

# ===== СПИСОК СОТРУДНИКОВ ОТДЕЛА РАЗВИТИЯ =====
DEV_TEAM = {
    'Сапогов М.Д.', 'Чечеткин М.И.', 'Роганова А.А.', 'Кошик В.И.',
    'Худышкин С.Н.', 'Гасанов С.Н.', 'Мулявин Я.В.', 'Обмолова В.В.'
}

def extract_dates_from_filename(filename):
    """Извлекает даты начала и конца периода из имени файла"""
    basename = os.path.basename(filename)
    match = re.search(r'с\s+(\d{2})\.(\d{2})\s+по\s+(\d{2})\.(\d{2})', basename)
    if match:
        return tuple(int(x) for x in match.groups())
    return (0, 0, 0, 0)

def find_latest_reports(count=COUNT_WEEKS):
    """Находит последние N файлов отчетов по заявкам"""
    pattern = os.path.join(DOCS_DIR, 'Заявки ТП Криста с *.xlsx')
    files = glob.glob(pattern)
    if not files:
        return []
    files.sort(key=extract_dates_from_filename, reverse=True)
    return files[:count]

def extract_period_from_filename(filename):
    """Извлекает период из имени файла"""
    basename = os.path.basename(filename)
    match = re.search(r'с\s+(\d{2}\.\d{2})\s+по\s+(\d{2}\.\d{2})', basename)
    if match:
        return f"{match.group(1)} по {match.group(2)}"
    return "неизвестный период"

def process_tickets(filepath):
    """Обрабатывает файл заявок и возвращает статистику по отправителям"""
    try:
        wb = load_workbook(filepath, data_only=True, read_only=True)
        
        if 'Статистика по Отправителю' in wb.sheetnames:
            ws = wb['Статистика по Отправителю']
            sender_stats = {}
            
            header_row_idx = 1
            for idx, row in enumerate(ws.iter_rows(min_row=1, max_row=10, values_only=True), start=1):
                if row and row[0] and 'названия строк' in str(row[0]).lower():
                    header_row_idx = idx
                    break
            
            for row in ws.iter_rows(min_row=header_row_idx + 1, values_only=True):
                if not row or len(row) < 2:
                    continue
                sender = row[0]
                count = row[1]
                if not sender or not count:
                    continue
                sender_str = str(sender).strip()
                if 'общий итог' in sender_str.lower() or sender_str == '':
                    continue
                try:
                    if isinstance(count, (int, float, str)):
                        count_int = int(float(count))
                    else:
                        continue
                    sender_stats[sender_str] = count_int
                except (ValueError, TypeError):
                    continue
            wb.close()
            return sender_stats
        
        if 'Заявки' not in wb.sheetnames:
            print(f"⚠️  Лист 'Заявки' не найден в {filepath}")
            wb.close()
            return None
        
        ws = wb['Заявки']
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

def categorize_senders(sender_stats):
    """Разделяет отправителей на отдел развития и бухгалтерию"""
    dev_count = 0
    accounting_count = 0
    dev_senders = []
    accounting_senders = []
    
    for sender, count in sender_stats.items():
        if sender in DEV_TEAM:
            dev_count += count
            dev_senders.append({'name': sender, 'count': count})
        else:
            accounting_count += count
            accounting_senders.append({'name': sender, 'count': count})
    
    dev_senders.sort(key=lambda x: x['count'], reverse=True)
    accounting_senders.sort(key=lambda x: x['count'], reverse=True)
    
    return {
        'total': dev_count + accounting_count,
        'dev': dev_count,
        'accounting': accounting_count,
        'dev_top10': dev_senders[:10],
        'accounting_top10': accounting_senders[:10]
    }

def generate_markdown(weeks_data):
    """Генерирует Markdown с интерактивной диаграммой"""
    lines = []
    lines.append('## Направленные заявки (по неделям)')  # <-- ИЗМЕНЕНО
    lines.append('')
    
    chart_data = []
    for filepath, period, stats in weeks_data:
        categorized = categorize_senders(stats)
        chart_data.append({
            'period': period,
            'total': categorized['total'],
            'dev': categorized['dev'],
            'accounting': categorized['accounting'],
            'dev_top10': categorized['dev_top10'],
            'accounting_top10': categorized['accounting_top10']
        })
    
    chart_data.reverse()
    
    lines.append('<div class="chart-container">')
    lines.append('  <canvas id="ticketsChart" width="400" height="200"></canvas>')
    lines.append('  <div class="chart-hint">💡 Нажмите на точку для просмотра детализации по сотрудникам</div>')
    lines.append('  <div id="chartError" style="display: none; padding: 20px; text-align: center; color: #e74c3c;">')
    lines.append('    Не удалось загрузить диаграмму. Пожалуйста, обновите страницу.')
    lines.append('  </div>')
    lines.append('</div>')
    lines.append('')
    
    lines.append('<div id="detailModal" class="modal">')
    lines.append('  <div class="modal-content">')
    lines.append('    <span class="close">&times;</span>')
    lines.append('    <h3 id="modalTitle"></h3>')
    lines.append('    <div id="modalBody"></div>')
    lines.append('  </div>')
    lines.append('</div>')
    lines.append('')
    
    lines.append(f'<script>')
    lines.append(f'window.chartData = {json.dumps(chart_data, ensure_ascii=False)};')
    lines.append(f'</script>')
    lines.append('')
    
    return '\n'.join(lines)

STYLES = '''<style>
.chart-container {
  position: relative;
  height: 300px;
  margin: 30px 0;
  padding: 20px;
  background: #fff;
  border: 1px solid #e0e4e8;
  border-radius: 8px;
}

.chart-container canvas {
  cursor: pointer;
}

.chart-hint {
  text-align: center;
  color: #718096;
  font-size: 13px;
  margin-top: 10px;
  font-style: italic;
}

.modal {
  display: none;
  position: fixed;
  z-index: 1000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0,0,0,0.5);
}

.modal-content {
  background-color: #fff;
  margin: 5% auto;
  padding: 30px;
  border: 1px solid #e0e4e8;
  border-radius: 8px;
  width: 80%;
  max-width: 600px;
  max-height: 80vh;
  overflow-y: auto;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
  cursor: pointer;
}

.close:hover {
  color: #000;
}

#modalTitle {
  margin-top: 0;
  color: #2c3e50;
  border-bottom: 2px solid #e0e4e8;
  padding-bottom: 10px;
}

.detail-section {
  margin: 20px 0;
}

.detail-section h4 {
  color: #2c3e50;
  margin-bottom: 10px;
}

.detail-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 14px;
}

.detail-table th {
  background: #f5f7fa;
  padding: 8px 12px;
  text-align: left;
  border-bottom: 2px solid #e0e4e8;
  font-weight: 600;
}

.detail-table td {
  padding: 8px 12px;
  border-bottom: 1px solid #eef2f6;
}

.detail-table tr:hover {
  background: #f9fafb;
}

.total-badge {
  display: inline-block;
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 13px;
  font-weight: 600;
  margin-left: 10px;
}

.total-badge.dev {
  background: #e3f2fd;
  color: #1976d2;
}

.total-badge.accounting {
  background: #f3e5f5;
  color: #7b1fa2;
}
</style>'''

SCRIPT = '''<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<script>
(function() {
  function initChart() {
    const chartData = window.chartData || [];
    
    if (chartData.length === 0) {
      console.error('chartData не найден');
      return;
    }
    
    const canvas = document.getElementById('ticketsChart');
    if (!canvas) {
      console.error('Canvas не найден');
      return;
    }
    
    if (typeof Chart === 'undefined') {
      console.error('Chart.js не загружен');
      document.getElementById('chartError').style.display = 'block';
      canvas.style.display = 'none';
      return;
    }
    
    const ctx = canvas.getContext('2d');
    
    new Chart(ctx, {
      type: 'line',
      data: {
        labels: chartData.map(d => d.period),
        datasets: [
          {
            label: 'Всего заявок',
            data: chartData.map(d => d.total),
            borderColor: '#2c3e50',
            backgroundColor: 'rgba(44, 62, 80, 0.05)',
            borderWidth: 1.5,
            pointRadius: 6,
            pointHoverRadius: 10,
            pointBackgroundColor: '#fff',
            pointBorderColor: '#2c3e50',
            pointBorderWidth: 2,
            pointStyle: 'circle',
            fill: true,
            tension: 0.3
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        interaction: {
          mode: 'index',
          intersect: false,
        },
        plugins: {
          legend: {
            display: false
          },
          tooltip: {
            backgroundColor: 'rgba(255, 255, 255, 0.98)',
            titleColor: '#2c3e50',
            bodyColor: '#2d3748',
            borderColor: '#e0e4e8',
            borderWidth: 1,
            padding: 12,
            titleFont: { size: 13, weight: 'bold' },
            bodyFont: { size: 12 },
            displayColors: false,
            callbacks: {
              title: function(context) {
                return context[0].label;
              },
              label: function(context) {
                const index = context.dataIndex;
                const data = chartData[index];
                return [
                  `Всего: ${data.total} заявок`,
                  `Отдел развития: ${data.dev}`,
                  `Бухгалтерия: ${data.accounting}`,
                  '',
                  '👆 Нажмите для детализации'
                ];
              }
            }
          }
        },
        scales: {
          x: {
            grid: { display: false },
            ticks: {
              font: { size: 11 },
              maxRotation: 45,
              minRotation: 45
            }
          },
          y: {
            beginAtZero: true,
            grid: { 
              color: '#f0f0f0',
              drawBorder: false
            },
            ticks: { 
              font: { size: 11 },
              stepSize: 10
            }
          }
        },
        onHover: function(e, elements) {
          const canvas = e.chart.canvas;
          if (elements.length > 0) {
            canvas.style.cursor = 'pointer';
          } else {
            canvas.style.cursor = 'default';
          }
        },
        onClick: function(e, elements) {
          if (elements.length > 0) {
            const index = elements[0].index;
            showDetails(index);
          }
        }
      }
    });
  }
  
  function showDetails(index) {
    const data = window.chartData[index];
    const modal = document.getElementById('detailModal');
    const modalTitle = document.getElementById('modalTitle');
    const modalBody = document.getElementById('modalBody');
    
    modalTitle.innerHTML = `Период: ${data.period} <span class="total-badge dev">Отдел развития: ${data.dev}</span> <span class="total-badge accounting">Бухгалтерия: ${data.accounting}</span> <span class="total-badge" style="background: #e0e4e8; color: #2c3e50;">Всего: ${data.total}</span>`;
    
    let html = '';
    
    if (data.dev_top10.length > 0) {
      html += '<div class="detail-section">';
      html += '<h4>🔧 Отдел развития (Топ 10)</h4>';
      html += '<table class="detail-table">';
      html += '<thead><tr><th>Сотрудник</th><th>Заявок</th></tr></thead>';
      html += '<tbody>';
      data.dev_top10.forEach(item => {
        html += `<tr><td>${item.name}</td><td>${item.count}</td></tr>`;
      });
      html += '</tbody></table>';
      html += '</div>';
    }
    
    if (data.accounting_top10.length > 0) {
      html += '<div class="detail-section">';
      html += '<h4>📊 Бухгалтерия (Топ 10)</h4>';
      html += '<table class="detail-table">';
      html += '<thead><tr><th>Сотрудник</th><th>Заявок</th></tr></thead>';
      html += '<tbody>';
      data.accounting_top10.forEach(item => {
        html += `<tr><td>${item.name}</td><td>${item.count}</td></tr>`;
      });
      html += '</tbody></table>';
      html += '</div>';
    }
    
    modalBody.innerHTML = html;
    modal.style.display = 'block';
  }
  
  document.querySelector('.close').onclick = function() {
    document.getElementById('detailModal').style.display = 'none';
  }
  
  window.onclick = function(event) {
    const modal = document.getElementById('detailModal');
    if (event.target == modal) {
      modal.style.display = 'none';
    }
  }
  
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initChart);
  } else {
    initChart();
  }
})();
</script>'''

def main():
    print(f'🔍 Поиск файлов отчетов (ожидаем последние {COUNT_WEEKS})...')
    files = find_latest_reports(COUNT_WEEKS)
    if not files:
        print('❌ Файлы отчетов не найдены в папке docs/')
        print('   Ожидаемый формат: "Заявки ТП Криста с ДД.ММ по ДД.ММ.xlsx"')
        return
    
    print(f'✅ Найдено файлов для обработки: {len(files)}')
    for f in files:
        print(f'   - {os.path.basename(f)}')
    
    weeks_data = []
    for filepath in files:
        period = extract_period_from_filename(filepath)
        print(f'📅 Период: {period}')
        print('   📊 Обработка данных...')
        stats = process_tickets(filepath)
        if stats is None:
            print(f'⚠️  Не удалось обработать файл: {os.path.basename(filepath)}')
            continue
        print(f'   📋 Найдено отправителей: {len(stats)}')
        print(f'   📝 Всего заявок: {sum(stats.values())}')
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