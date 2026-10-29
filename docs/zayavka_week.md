<style>
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
</style>
## Направленные заявки за неделю

### Период: 15.10 по 22.10 {#week-1-15-10-по-22-10 .toc-hidden}
### Период: 08.10 по 15.10 {#week-2-08-10-по-15-10 .toc-hidden}

<div class="weeks-grid">
<div class="week-column">
  <div class="week-period">Период: 15.10 по 22.10</div>
  <table class="ticket-table" id="table-1">
    <thead>
      <tr>
        <th>Отправитель</th>
        <th>Заявок</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Сапогов М.Д.</td>
        <td class="ticket-count">16</td>
      </tr>
      <tr>
        <td>Роганова А.А.</td>
        <td class="ticket-count">4</td>
      </tr>
      <tr>
        <td>Гасанов С.Н.</td>
        <td class="ticket-count">2</td>
      </tr>
      <tr>
        <td>Шевелева К.В.</td>
        <td class="ticket-count">2</td>
      </tr>
      <tr>
        <td>Мулявин Я.В.</td>
        <td class="ticket-count">2</td>
      </tr>
      <tr>
        <td>Останин И.Г.</td>
        <td class="ticket-count">2</td>
      </tr>
      <tr>
        <td>Худышкин С.Н.</td>
        <td class="ticket-count">2</td>
      </tr>
      <tr>
        <td>Кошик В.И.</td>
        <td class="ticket-count">1</td>
      </tr>
      <tr>
        <td>Конева Е.И.</td>
        <td class="ticket-count">1</td>
      </tr>
      <tr>
        <td>Родина Н.В.</td>
        <td class="ticket-count">1</td>
      </tr>
      <tr class="ticket-hidden-row" style="display: none;">
        <td>Павлова Н.Г.</td>
        <td class="ticket-count">1</td>
      </tr>
      <tr class="total-row">
        <td>Итого:</td>
        <td class="ticket-count">34</td>
      </tr>
    </tbody>
  </table>
  <button class="toggle-btn" onclick="toggleWeek(1)" data-col="1">
    <span class="toggle-icon">›</span>
    Показать ещё 1 записей
  </button>
</div>
<div class="week-column">
  <div class="week-period">Период: 08.10 по 15.10</div>
  <table class="ticket-table" id="table-2">
    <thead>
      <tr>
        <th>Отправитель</th>
        <th>Заявок</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Сапогов М.Д.</td>
        <td class="ticket-count">8</td>
      </tr>
      <tr>
        <td>Ильдеркина И.Н.</td>
        <td class="ticket-count">5</td>
      </tr>
      <tr>
        <td>Петрова Н.А.</td>
        <td class="ticket-count">5</td>
      </tr>
      <tr>
        <td>Роганова А.А.</td>
        <td class="ticket-count">5</td>
      </tr>
      <tr>
        <td>Суханова И.К.</td>
        <td class="ticket-count">4</td>
      </tr>
      <tr>
        <td>Кузнецова Н.А.</td>
        <td class="ticket-count">3</td>
      </tr>
      <tr>
        <td>Родина Н.В.</td>
        <td class="ticket-count">3</td>
      </tr>
      <tr>
        <td>Худышкин С.Н.</td>
        <td class="ticket-count">3</td>
      </tr>
      <tr>
        <td>Дмитриенко Т.В.</td>
        <td class="ticket-count">2</td>
      </tr>
      <tr>
        <td>Мулявин Я.В.</td>
        <td class="ticket-count">2</td>
      </tr>
      <tr class="ticket-hidden-row" style="display: none;">
        <td>Алыкова Т.В.</td>
        <td class="ticket-count">1</td>
      </tr>
      <tr class="ticket-hidden-row" style="display: none;">
        <td>Букреева Е.Н.</td>
        <td class="ticket-count">1</td>
      </tr>
      <tr class="ticket-hidden-row" style="display: none;">
        <td>Бусыгина И.С.</td>
        <td class="ticket-count">1</td>
      </tr>
      <tr class="ticket-hidden-row" style="display: none;">
        <td>Вернер Е.В.</td>
        <td class="ticket-count">1</td>
      </tr>
      <tr class="ticket-hidden-row" style="display: none;">
        <td>Гасанов С.Н.</td>
        <td class="ticket-count">1</td>
      </tr>
      <tr class="ticket-hidden-row" style="display: none;">
        <td>Ершова А.Н.</td>
        <td class="ticket-count">1</td>
      </tr>
      <tr class="ticket-hidden-row" style="display: none;">
        <td>Зуева Г.П.</td>
        <td class="ticket-count">1</td>
      </tr>
      <tr class="ticket-hidden-row" style="display: none;">
        <td>Каргаполова А.А.</td>
        <td class="ticket-count">1</td>
      </tr>
      <tr class="ticket-hidden-row" style="display: none;">
        <td>Кошик В.И.</td>
        <td class="ticket-count">1</td>
      </tr>
      <tr class="ticket-hidden-row" style="display: none;">
        <td>Лазарева Е.Н.</td>
        <td class="ticket-count">1</td>
      </tr>
      <tr class="ticket-hidden-row" style="display: none;">
        <td>Минакова О.Ф.</td>
        <td class="ticket-count">1</td>
      </tr>
      <tr class="ticket-hidden-row" style="display: none;">
        <td>Семенова Н.В.</td>
        <td class="ticket-count">1</td>
      </tr>
      <tr class="ticket-hidden-row" style="display: none;">
        <td>Тимофеева А.Н.</td>
        <td class="ticket-count">1</td>
      </tr>
      <tr class="ticket-hidden-row" style="display: none;">
        <td>Шибанаева Т.В.</td>
        <td class="ticket-count">1</td>
      </tr>
      <tr class="ticket-hidden-row" style="display: none;">
        <td>Юшкевич Т.В.</td>
        <td class="ticket-count">1</td>
      </tr>
      <tr class="total-row">
        <td>Итого:</td>
        <td class="ticket-count">55</td>
      </tr>
    </tbody>
  </table>
  <button class="toggle-btn" onclick="toggleWeek(2)" data-col="2">
    <span class="toggle-icon">›</span>
    Показать ещё 15 записей
  </button>
</div>
</div>

<script>
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
</script>