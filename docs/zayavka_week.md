<style>
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
</style>
## Направленные заявки (по неделям)

<div class="chart-container">
  <canvas id="ticketsChart" width="400" height="200"></canvas>
  <div class="chart-hint">💡 Нажмите на точку для просмотра детализации по сотрудникам</div>
  <div id="chartError" style="display: none; padding: 20px; text-align: center; color: #e74c3c;">
    Не удалось загрузить диаграмму. Пожалуйста, обновите страницу.
  </div>
</div>

<div id="detailModal" class="modal">
  <div class="modal-content">
    <span class="close">&times;</span>
    <h3 id="modalTitle"></h3>
    <div id="modalBody"></div>
  </div>
</div>

<script>
window.chartData = [{"period": "08.10 по 15.10", "total": 55, "dev": 20, "accounting": 35, "dev_top10": [{"name": "Сапогов М.Д.", "count": 8}, {"name": "Роганова А.А.", "count": 5}, {"name": "Худышкин С.Н.", "count": 3}, {"name": "Мулявин Я.В.", "count": 2}, {"name": "Гасанов С.Н.", "count": 1}, {"name": "Кошик В.И.", "count": 1}], "accounting_top10": [{"name": "Ильдеркина И.Н.", "count": 5}, {"name": "Петрова Н.А.", "count": 5}, {"name": "Суханова И.К.", "count": 4}, {"name": "Кузнецова Н.А.", "count": 3}, {"name": "Родина Н.В.", "count": 3}, {"name": "Дмитриенко Т.В.", "count": 2}, {"name": "Алыкова Т.В.", "count": 1}, {"name": "Букреева Е.Н.", "count": 1}, {"name": "Бусыгина И.С.", "count": 1}, {"name": "Вернер Е.В.", "count": 1}]}, {"period": "15.10 по 22.10", "total": 34, "dev": 27, "accounting": 7, "dev_top10": [{"name": "Сапогов М.Д.", "count": 16}, {"name": "Роганова А.А.", "count": 4}, {"name": "Гасанов С.Н.", "count": 2}, {"name": "Мулявин Я.В.", "count": 2}, {"name": "Худышкин С.Н.", "count": 2}, {"name": "Кошик В.И.", "count": 1}], "accounting_top10": [{"name": "Шевелева К.В.", "count": 2}, {"name": "Останин И.Г.", "count": 2}, {"name": "Конева Е.И.", "count": 1}, {"name": "Родина Н.В.", "count": 1}, {"name": "Павлова Н.Г.", "count": 1}]}, {"period": "22.10 по 29.10", "total": 38, "dev": 21, "accounting": 17, "dev_top10": [{"name": "Сапогов М.Д.", "count": 7}, {"name": "Гасанов С.Н.", "count": 4}, {"name": "Кошик В.И.", "count": 4}, {"name": "Мулявин Я.В.", "count": 4}, {"name": "Роганова А.А.", "count": 2}], "accounting_top10": [{"name": "Останин И.Г.", "count": 6}, {"name": "Зуева Г.П.", "count": 2}, {"name": "Лазарева Е.Н.", "count": 1}, {"name": "Манджиева  А.А.", "count": 1}, {"name": "Минакова О.Ф.", "count": 1}, {"name": "Нурлубаева А.З.", "count": 1}, {"name": "Россолова Е.С.", "count": 1}, {"name": "Русмиленко И.Ю.", "count": 1}, {"name": "Семенова Н.В.", "count": 1}, {"name": "Стрельникова О.С.", "count": 1}]}, {"period": "29.10 по 05.11", "total": 31, "dev": 16, "accounting": 15, "dev_top10": [{"name": "Роганова А.А.", "count": 9}, {"name": "Сапогов М.Д.", "count": 4}, {"name": "Кошик В.И.", "count": 2}, {"name": "Гасанов С.Н.", "count": 1}], "accounting_top10": [{"name": "Останин И.Г.", "count": 3}, {"name": "Зуева Г.П.", "count": 2}, {"name": "Манджиева  А.А.", "count": 2}, {"name": "Ершова А.Н.", "count": 1}, {"name": "Кропотов И.А.", "count": 1}, {"name": "Кузнецова Н.А.", "count": 1}, {"name": "Лычев А.В.", "count": 1}, {"name": "Павлова Н.Г.", "count": 1}, {"name": "Петрова Н.А.", "count": 1}, {"name": "Россолова Е.С.", "count": 1}]}];
</script>

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
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
</script>