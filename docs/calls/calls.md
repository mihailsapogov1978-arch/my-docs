<style>
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


# Статистика звонков за месяц

<div class="calls-total">
  <div class="ct-label">Всего звонков</div>
  <div class="ct-cell ct-in">
    <div class="ct-value">8966</div>
    <div class="ct-caption">Принятые</div>
  </div>
  <div class="ct-cell ct-miss">
    <div class="ct-value">2979</div>
    <div class="ct-caption">Пропущенные</div>
  </div>
  <div class="ct-cell ct-out">
    <div class="ct-value">9112</div>
    <div class="ct-caption">Исходящие</div>
  </div>
</div>

## Детализация по подразделениям

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-1" class="dept-checkbox">
    <label for="dept-1" class="dept-row">
      <span class="dept-name">Администрация</span>
      <span class="dept-summary">
        <span class="ds-cell"><span class="ds-label">принято:</span> <b>1193</b></span>
        <span class="ds-cell"><span class="ds-label">пропущено:</span> <b>605</b></span>
        <span class="ds-cell"><span class="ds-label">исходящих:</span> <b>1172</b></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
<table class="calls-table">
  <colgroup>
    <col class="col-num">
    <col class="col-fio">
    <col class="col-stat">
    <col class="col-stat">
    <col class="col-stat">
  </colgroup>
  <thead>
    <tr>
      <th rowspan="2" class="col-num">№</th>
      <th rowspan="2" class="col-fio">ФИО</th>
      <th colspan="2">Входящие</th>
      <th rowspan="2" class="col-out">Исходящие</th>
    </tr>
    <tr>
      <th class="col-in">Принятые</th>
      <th class="col-miss">Пропущенные</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="col-num">1</td>
      <td class="col-fio">Останин Иван Георгиевич</td>
      <td class="col-in">424</td>
      <td class="col-miss">260</td>
      <td class="col-out">355</td>
    </tr>
    <tr>
      <td class="col-num">2</td>
      <td class="col-fio">Родина Наталья Васильевна</td>
      <td class="col-in">435</td>
      <td class="col-miss">183</td>
      <td class="col-out">352</td>
    </tr>
    <tr>
      <td class="col-num">3</td>
      <td class="col-fio">Гареева Регина Рафаэлевна</td>
      <td class="col-in">102</td>
      <td class="col-miss">63</td>
      <td class="col-out">207</td>
    </tr>
    <tr>
      <td class="col-num">4</td>
      <td class="col-fio">Жданова Галина Игоревна</td>
      <td class="col-in">132</td>
      <td class="col-miss">52</td>
      <td class="col-out">169</td>
    </tr>
    <tr>
      <td class="col-num">5</td>
      <td class="col-fio">Галямов Азат Ахтамович</td>
      <td class="col-in">100</td>
      <td class="col-miss">47</td>
      <td class="col-out">89</td>
    </tr>
  </tbody>
</table>
    </div>
  </div>
  <div class="dept-item">
    <input type="checkbox" id="dept-2" class="dept-checkbox">
    <label for="dept-2" class="dept-row">
      <span class="dept-name">Отдел информационной безопасности</span>
      <span class="dept-summary">
        <span class="ds-cell"><span class="ds-label">принято:</span> <b>385</b></span>
        <span class="ds-cell"><span class="ds-label">пропущено:</span> <b>113</b></span>
        <span class="ds-cell"><span class="ds-label">исходящих:</span> <b>253</b></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
<table class="calls-table">
  <colgroup>
    <col class="col-num">
    <col class="col-fio">
    <col class="col-stat">
    <col class="col-stat">
    <col class="col-stat">
  </colgroup>
  <thead>
    <tr>
      <th rowspan="2" class="col-num">№</th>
      <th rowspan="2" class="col-fio">ФИО</th>
      <th colspan="2">Входящие</th>
      <th rowspan="2" class="col-out">Исходящие</th>
    </tr>
    <tr>
      <th class="col-in">Принятые</th>
      <th class="col-miss">Пропущенные</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="col-num">1</td>
      <td class="col-fio">Иванников Вадим Вячеславович</td>
      <td class="col-in">148</td>
      <td class="col-miss">31</td>
      <td class="col-out">71</td>
    </tr>
    <tr>
      <td class="col-num">2</td>
      <td class="col-fio">Ананьев Евгений Сергеевич</td>
      <td class="col-in">69</td>
      <td class="col-miss">32</td>
      <td class="col-out">109</td>
    </tr>
    <tr>
      <td class="col-num">3</td>
      <td class="col-fio">Лычев Антон Владимирович</td>
      <td class="col-in">120</td>
      <td class="col-miss">37</td>
      <td class="col-out">39</td>
    </tr>
    <tr>
      <td class="col-num">4</td>
      <td class="col-fio">Шляпин Денис Олегович</td>
      <td class="col-in">48</td>
      <td class="col-miss">13</td>
      <td class="col-out">34</td>
    </tr>
  </tbody>
</table>
    </div>
  </div>
  <div class="dept-item">
    <input type="checkbox" id="dept-3" class="dept-checkbox">
    <label for="dept-3" class="dept-row">
      <span class="dept-name">Отдел СР и ТП</span>
      <span class="dept-summary">
        <span class="ds-cell"><span class="ds-label">принято:</span> <b>1091</b></span>
        <span class="ds-cell"><span class="ds-label">пропущено:</span> <b>727</b></span>
        <span class="ds-cell"><span class="ds-label">исходящих:</span> <b>872</b></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
<table class="calls-table">
  <colgroup>
    <col class="col-num">
    <col class="col-fio">
    <col class="col-stat">
    <col class="col-stat">
    <col class="col-stat">
  </colgroup>
  <thead>
    <tr>
      <th rowspan="2" class="col-num">№</th>
      <th rowspan="2" class="col-fio">ФИО</th>
      <th colspan="2">Входящие</th>
      <th rowspan="2" class="col-out">Исходящие</th>
    </tr>
    <tr>
      <th class="col-in">Принятые</th>
      <th class="col-miss">Пропущенные</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="col-num">1</td>
      <td class="col-fio">Чечеткин Михаил Игоревич</td>
      <td class="col-in">260</td>
      <td class="col-miss">332</td>
      <td class="col-out">271</td>
    </tr>
    <tr>
      <td class="col-num">2</td>
      <td class="col-fio">Роганова Анна Анатольевна</td>
      <td class="col-in">318</td>
      <td class="col-miss">224</td>
      <td class="col-out">82</td>
    </tr>
    <tr>
      <td class="col-num">3</td>
      <td class="col-fio">Сапогов Михаил Дмитриевич</td>
      <td class="col-in">171</td>
      <td class="col-miss">69</td>
      <td class="col-out">179</td>
    </tr>
    <tr>
      <td class="col-num">4</td>
      <td class="col-fio">Кошик Владимир Иванович</td>
      <td class="col-in">126</td>
      <td class="col-miss">16</td>
      <td class="col-out">135</td>
    </tr>
    <tr>
      <td class="col-num">5</td>
      <td class="col-fio">Худышкин Сергей Николаевич</td>
      <td class="col-in">90</td>
      <td class="col-miss">19</td>
      <td class="col-out">97</td>
    </tr>
    <tr>
      <td class="col-num">6</td>
      <td class="col-fio">Мулявин Яков Владиславович</td>
      <td class="col-in">69</td>
      <td class="col-miss">8</td>
      <td class="col-out">55</td>
    </tr>
    <tr>
      <td class="col-num">7</td>
      <td class="col-fio">Гасанов Сархан Нураддин</td>
      <td class="col-in">53</td>
      <td class="col-miss">13</td>
      <td class="col-out">45</td>
    </tr>
    <tr>
      <td class="col-num">8</td>
      <td class="col-fio">Ставер Андрей Петрович</td>
      <td class="col-in">4</td>
      <td class="col-miss">22</td>
      <td class="col-out">8</td>
    </tr>
    <tr>
      <td class="col-num">9</td>
      <td class="col-fio">Обмолова Валентина Витальевна</td>
      <td class="col-in">0</td>
      <td class="col-miss">24</td>
      <td class="col-out">0</td>
    </tr>
  </tbody>
</table>
    </div>
  </div>
  <div class="dept-item">
    <input type="checkbox" id="dept-4" class="dept-checkbox">
    <label for="dept-4" class="dept-row">
      <span class="dept-name">Отдел кадрового и правового обеспечения</span>
      <span class="dept-summary">
        <span class="ds-cell"><span class="ds-label">принято:</span> <b>625</b></span>
        <span class="ds-cell"><span class="ds-label">пропущено:</span> <b>246</b></span>
        <span class="ds-cell"><span class="ds-label">исходящих:</span> <b>746</b></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
<table class="calls-table">
  <colgroup>
    <col class="col-num">
    <col class="col-fio">
    <col class="col-stat">
    <col class="col-stat">
    <col class="col-stat">
  </colgroup>
  <thead>
    <tr>
      <th rowspan="2" class="col-num">№</th>
      <th rowspan="2" class="col-fio">ФИО</th>
      <th colspan="2">Входящие</th>
      <th rowspan="2" class="col-out">Исходящие</th>
    </tr>
    <tr>
      <th class="col-in">Принятые</th>
      <th class="col-miss">Пропущенные</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="col-num">1</td>
      <td class="col-fio">Ядрова Анна Викторовна</td>
      <td class="col-in">196</td>
      <td class="col-miss">110</td>
      <td class="col-out">379</td>
    </tr>
    <tr>
      <td class="col-num">2</td>
      <td class="col-fio">Чернов Андрей Анатольевич</td>
      <td class="col-in">319</td>
      <td class="col-miss">98</td>
      <td class="col-out">205</td>
    </tr>
    <tr>
      <td class="col-num">3</td>
      <td class="col-fio">Полякова Анна Викторовна</td>
      <td class="col-in">99</td>
      <td class="col-miss">22</td>
      <td class="col-out">110</td>
    </tr>
    <tr>
      <td class="col-num">4</td>
      <td class="col-fio">Суханова Ирина Константиновна</td>
      <td class="col-in">9</td>
      <td class="col-miss">12</td>
      <td class="col-out">50</td>
    </tr>
    <tr>
      <td class="col-num">5</td>
      <td class="col-fio">Цветнова Наталья Геннадьевна</td>
      <td class="col-in">2</td>
      <td class="col-miss">4</td>
      <td class="col-out">2</td>
    </tr>
  </tbody>
</table>
    </div>
  </div>
  <div class="dept-item">
    <input type="checkbox" id="dept-5" class="dept-checkbox">
    <label for="dept-5" class="dept-row">
      <span class="dept-name">Отдел учета основных средств и запасов</span>
      <span class="dept-summary">
        <span class="ds-cell"><span class="ds-label">принято:</span> <b>1087</b></span>
        <span class="ds-cell"><span class="ds-label">пропущено:</span> <b>146</b></span>
        <span class="ds-cell"><span class="ds-label">исходящих:</span> <b>1325</b></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
<table class="calls-table">
  <colgroup>
    <col class="col-num">
    <col class="col-fio">
    <col class="col-stat">
    <col class="col-stat">
    <col class="col-stat">
  </colgroup>
  <thead>
    <tr>
      <th rowspan="2" class="col-num">№</th>
      <th rowspan="2" class="col-fio">ФИО</th>
      <th colspan="2">Входящие</th>
      <th rowspan="2" class="col-out">Исходящие</th>
    </tr>
    <tr>
      <th class="col-in">Принятые</th>
      <th class="col-miss">Пропущенные</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="col-num">1</td>
      <td class="col-fio">Гатаулина Марина Васильевна</td>
      <td class="col-in">215</td>
      <td class="col-miss">32</td>
      <td class="col-out">251</td>
    </tr>
    <tr>
      <td class="col-num">2</td>
      <td class="col-fio">Стрельникова Ольга Сергеевна</td>
      <td class="col-in">184</td>
      <td class="col-miss">37</td>
      <td class="col-out">142</td>
    </tr>
    <tr>
      <td class="col-num">3</td>
      <td class="col-fio">Щирская Ксения Васильевна</td>
      <td class="col-in">93</td>
      <td class="col-miss">18</td>
      <td class="col-out">207</td>
    </tr>
    <tr>
      <td class="col-num">4</td>
      <td class="col-fio">Зуева Галия Парвасьевна</td>
      <td class="col-in">109</td>
      <td class="col-miss">7</td>
      <td class="col-out">160</td>
    </tr>
    <tr>
      <td class="col-num">5</td>
      <td class="col-fio">Петрова Наталья Александровна</td>
      <td class="col-in">100</td>
      <td class="col-miss">7</td>
      <td class="col-out">122</td>
    </tr>
    <tr>
      <td class="col-num">6</td>
      <td class="col-fio">Минакова Ольга Фахрутдиновна</td>
      <td class="col-in">82</td>
      <td class="col-miss">12</td>
      <td class="col-out">129</td>
    </tr>
    <tr>
      <td class="col-num">7</td>
      <td class="col-fio">Филиппова Олеся Валерьевна</td>
      <td class="col-in">99</td>
      <td class="col-miss">11</td>
      <td class="col-out">110</td>
    </tr>
    <tr>
      <td class="col-num">8</td>
      <td class="col-fio">Шибанаева Татьяна Викторовна</td>
      <td class="col-in">99</td>
      <td class="col-miss">7</td>
      <td class="col-out">91</td>
    </tr>
    <tr>
      <td class="col-num">9</td>
      <td class="col-fio">Вернер Елена Викторовна</td>
      <td class="col-in">57</td>
      <td class="col-miss">1</td>
      <td class="col-out">55</td>
    </tr>
    <tr>
      <td class="col-num">10</td>
      <td class="col-fio">Ильницкая Светлана Викторовна</td>
      <td class="col-in">29</td>
      <td class="col-miss">6</td>
      <td class="col-out">26</td>
    </tr>
    <tr>
      <td class="col-num">11</td>
      <td class="col-fio">Бусыгина Ирина Сергеевна</td>
      <td class="col-in">20</td>
      <td class="col-miss">8</td>
      <td class="col-out">32</td>
    </tr>
  </tbody>
</table>
    </div>
  </div>
  <div class="dept-item">
    <input type="checkbox" id="dept-6" class="dept-checkbox">
    <label for="dept-6" class="dept-row">
      <span class="dept-name">Отдел подготовки отчетности</span>
      <span class="dept-summary">
        <span class="ds-cell"><span class="ds-label">принято:</span> <b>355</b></span>
        <span class="ds-cell"><span class="ds-label">пропущено:</span> <b>86</b></span>
        <span class="ds-cell"><span class="ds-label">исходящих:</span> <b>411</b></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
<table class="calls-table">
  <colgroup>
    <col class="col-num">
    <col class="col-fio">
    <col class="col-stat">
    <col class="col-stat">
    <col class="col-stat">
  </colgroup>
  <thead>
    <tr>
      <th rowspan="2" class="col-num">№</th>
      <th rowspan="2" class="col-fio">ФИО</th>
      <th colspan="2">Входящие</th>
      <th rowspan="2" class="col-out">Исходящие</th>
    </tr>
    <tr>
      <th class="col-in">Принятые</th>
      <th class="col-miss">Пропущенные</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="col-num">1</td>
      <td class="col-fio">Тимофеева Алиса Николаевна</td>
      <td class="col-in">113</td>
      <td class="col-miss">35</td>
      <td class="col-out">158</td>
    </tr>
    <tr>
      <td class="col-num">2</td>
      <td class="col-fio">Шевелева Ксения Викторовна</td>
      <td class="col-in">111</td>
      <td class="col-miss">21</td>
      <td class="col-out">107</td>
    </tr>
    <tr>
      <td class="col-num">3</td>
      <td class="col-fio">Янова Екатерина Анатольевна</td>
      <td class="col-in">55</td>
      <td class="col-miss">7</td>
      <td class="col-out">65</td>
    </tr>
    <tr>
      <td class="col-num">4</td>
      <td class="col-fio">Лейпожих Алёна Алексеевна</td>
      <td class="col-in">24</td>
      <td class="col-miss">12</td>
      <td class="col-out">21</td>
    </tr>
    <tr>
      <td class="col-num">5</td>
      <td class="col-fio">Чистякова Елена Дмитриевна</td>
      <td class="col-in">16</td>
      <td class="col-miss">6</td>
      <td class="col-out">20</td>
    </tr>
    <tr>
      <td class="col-num">6</td>
      <td class="col-fio">Яковлева Вилена Фаильевна</td>
      <td class="col-in">18</td>
      <td class="col-miss">3</td>
      <td class="col-out">14</td>
    </tr>
    <tr>
      <td class="col-num">7</td>
      <td class="col-fio">Павлова Надежда Григорьевна</td>
      <td class="col-in">14</td>
      <td class="col-miss">2</td>
      <td class="col-out">17</td>
    </tr>
    <tr>
      <td class="col-num">8</td>
      <td class="col-fio">Ребась Кристина Владимировна</td>
      <td class="col-in">4</td>
      <td class="col-miss">0</td>
      <td class="col-out">9</td>
    </tr>
  </tbody>
</table>
    </div>
  </div>
  <div class="dept-item">
    <input type="checkbox" id="dept-7" class="dept-checkbox">
    <label for="dept-7" class="dept-row">
      <span class="dept-name">Отдел учета доходов</span>
      <span class="dept-summary">
        <span class="ds-cell"><span class="ds-label">принято:</span> <b>984</b></span>
        <span class="ds-cell"><span class="ds-label">пропущено:</span> <b>174</b></span>
        <span class="ds-cell"><span class="ds-label">исходящих:</span> <b>875</b></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
<table class="calls-table">
  <colgroup>
    <col class="col-num">
    <col class="col-fio">
    <col class="col-stat">
    <col class="col-stat">
    <col class="col-stat">
  </colgroup>
  <thead>
    <tr>
      <th rowspan="2" class="col-num">№</th>
      <th rowspan="2" class="col-fio">ФИО</th>
      <th colspan="2">Входящие</th>
      <th rowspan="2" class="col-out">Исходящие</th>
    </tr>
    <tr>
      <th class="col-in">Принятые</th>
      <th class="col-miss">Пропущенные</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="col-num">1</td>
      <td class="col-fio">Семенова Наталья Александровна</td>
      <td class="col-in">149</td>
      <td class="col-miss">68</td>
      <td class="col-out">174</td>
    </tr>
    <tr>
      <td class="col-num">2</td>
      <td class="col-fio">Жукова Анастасия Сергеевна</td>
      <td class="col-in">152</td>
      <td class="col-miss">24</td>
      <td class="col-out">138</td>
    </tr>
    <tr>
      <td class="col-num">3</td>
      <td class="col-fio">Лаба Вера Алексеевна</td>
      <td class="col-in">112</td>
      <td class="col-miss">26</td>
      <td class="col-out">117</td>
    </tr>
    <tr>
      <td class="col-num">4</td>
      <td class="col-fio">Каргаполова Алёна Андреевна</td>
      <td class="col-in">100</td>
      <td class="col-miss">20</td>
      <td class="col-out">97</td>
    </tr>
    <tr>
      <td class="col-num">5</td>
      <td class="col-fio">Юшкевич Татьяна Владимировна</td>
      <td class="col-in">89</td>
      <td class="col-miss">5</td>
      <td class="col-out">87</td>
    </tr>
    <tr>
      <td class="col-num">6</td>
      <td class="col-fio">Занина Ирина Александровна</td>
      <td class="col-in">81</td>
      <td class="col-miss">13</td>
      <td class="col-out">71</td>
    </tr>
    <tr>
      <td class="col-num">7</td>
      <td class="col-fio">Леванских Людмила Владимировна</td>
      <td class="col-in">77</td>
      <td class="col-miss">6</td>
      <td class="col-out">65</td>
    </tr>
    <tr>
      <td class="col-num">8</td>
      <td class="col-fio">Кропотов Иван Александрович</td>
      <td class="col-in">68</td>
      <td class="col-miss">3</td>
      <td class="col-out">47</td>
    </tr>
    <tr>
      <td class="col-num">9</td>
      <td class="col-fio">Фаузер Татьяна Леовна</td>
      <td class="col-in">76</td>
      <td class="col-miss">4</td>
      <td class="col-out">13</td>
    </tr>
    <tr>
      <td class="col-num">10</td>
      <td class="col-fio">Семенова Наталья Викторовна</td>
      <td class="col-in">50</td>
      <td class="col-miss">1</td>
      <td class="col-out">35</td>
    </tr>
    <tr>
      <td class="col-num">11</td>
      <td class="col-fio">Мицура Ираида Илдаровна</td>
      <td class="col-in">30</td>
      <td class="col-miss">4</td>
      <td class="col-out">31</td>
    </tr>
  </tbody>
</table>
    </div>
  </div>
  <div class="dept-item">
    <input type="checkbox" id="dept-8" class="dept-checkbox">
    <label for="dept-8" class="dept-row">
      <span class="dept-name">Отдел расчётов с персоналом</span>
      <span class="dept-summary">
        <span class="ds-cell"><span class="ds-label">принято:</span> <b>2343</b></span>
        <span class="ds-cell"><span class="ds-label">пропущено:</span> <b>630</b></span>
        <span class="ds-cell"><span class="ds-label">исходящих:</span> <b>2712</b></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
<table class="calls-table">
  <colgroup>
    <col class="col-num">
    <col class="col-fio">
    <col class="col-stat">
    <col class="col-stat">
    <col class="col-stat">
  </colgroup>
  <thead>
    <tr>
      <th rowspan="2" class="col-num">№</th>
      <th rowspan="2" class="col-fio">ФИО</th>
      <th colspan="2">Входящие</th>
      <th rowspan="2" class="col-out">Исходящие</th>
    </tr>
    <tr>
      <th class="col-in">Принятые</th>
      <th class="col-miss">Пропущенные</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="col-num">1</td>
      <td class="col-fio">Константинова Людмила Алексеевна</td>
      <td class="col-in">240</td>
      <td class="col-miss">81</td>
      <td class="col-out">423</td>
    </tr>
    <tr>
      <td class="col-num">2</td>
      <td class="col-fio">Ильдеркина Ирина Николаевна</td>
      <td class="col-in">272</td>
      <td class="col-miss">77</td>
      <td class="col-out">269</td>
    </tr>
    <tr>
      <td class="col-num">3</td>
      <td class="col-fio">Павлова Ирина Игоревна</td>
      <td class="col-in">274</td>
      <td class="col-miss">80</td>
      <td class="col-out">187</td>
    </tr>
    <tr>
      <td class="col-num">4</td>
      <td class="col-fio">Конева Елена Ивановна</td>
      <td class="col-in">196</td>
      <td class="col-miss">45</td>
      <td class="col-out">281</td>
    </tr>
    <tr>
      <td class="col-num">5</td>
      <td class="col-fio">Мунарева Виктория Игоревна</td>
      <td class="col-in">131</td>
      <td class="col-miss">20</td>
      <td class="col-out">353</td>
    </tr>
    <tr>
      <td class="col-num">6</td>
      <td class="col-fio">Алыкова Татьяна Валерьевна</td>
      <td class="col-in">173</td>
      <td class="col-miss">35</td>
      <td class="col-out">212</td>
    </tr>
    <tr>
      <td class="col-num">7</td>
      <td class="col-fio">Казанцева Лариса Анатольевна</td>
      <td class="col-in">151</td>
      <td class="col-miss">53</td>
      <td class="col-out">208</td>
    </tr>
    <tr>
      <td class="col-num">8</td>
      <td class="col-fio">Букреева Елена Николаевна</td>
      <td class="col-in">197</td>
      <td class="col-miss">67</td>
      <td class="col-out">124</td>
    </tr>
    <tr>
      <td class="col-num">9</td>
      <td class="col-fio">Сафаралеева Елена Хайрулловна</td>
      <td class="col-in">140</td>
      <td class="col-miss">45</td>
      <td class="col-out">129</td>
    </tr>
    <tr>
      <td class="col-num">10</td>
      <td class="col-fio">Россолова Екатерина Сергеевна</td>
      <td class="col-in">152</td>
      <td class="col-miss">24</td>
      <td class="col-out">89</td>
    </tr>
    <tr>
      <td class="col-num">11</td>
      <td class="col-fio">Злобина Мария Александровна</td>
      <td class="col-in">100</td>
      <td class="col-miss">20</td>
      <td class="col-out">144</td>
    </tr>
    <tr>
      <td class="col-num">12</td>
      <td class="col-fio">Шахова Галина Максимовна</td>
      <td class="col-in">75</td>
      <td class="col-miss">35</td>
      <td class="col-out">91</td>
    </tr>
    <tr>
      <td class="col-num">13</td>
      <td class="col-fio">Манджиева Алевтина Алексеевна</td>
      <td class="col-in">66</td>
      <td class="col-miss">17</td>
      <td class="col-out">102</td>
    </tr>
    <tr>
      <td class="col-num">14</td>
      <td class="col-fio">Ершова Алла Николаевна</td>
      <td class="col-in">103</td>
      <td class="col-miss">15</td>
      <td class="col-out">64</td>
    </tr>
    <tr>
      <td class="col-num">15</td>
      <td class="col-fio">Лазарева Екатерина Николаевна</td>
      <td class="col-in">32</td>
      <td class="col-miss">8</td>
      <td class="col-out">24</td>
    </tr>
    <tr>
      <td class="col-num">16</td>
      <td class="col-fio">Русмиленко Инга Юрьевна</td>
      <td class="col-in">41</td>
      <td class="col-miss">8</td>
      <td class="col-out">12</td>
    </tr>
  </tbody>
</table>
    </div>
  </div>
  <div class="dept-item">
    <input type="checkbox" id="dept-9" class="dept-checkbox">
    <label for="dept-9" class="dept-row">
      <span class="dept-name">Отдел расчётов с поставщиками, подрядчиками</span>
      <span class="dept-summary">
        <span class="ds-cell"><span class="ds-label">принято:</span> <b>903</b></span>
        <span class="ds-cell"><span class="ds-label">пропущено:</span> <b>252</b></span>
        <span class="ds-cell"><span class="ds-label">исходящих:</span> <b>746</b></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
<table class="calls-table">
  <colgroup>
    <col class="col-num">
    <col class="col-fio">
    <col class="col-stat">
    <col class="col-stat">
    <col class="col-stat">
  </colgroup>
  <thead>
    <tr>
      <th rowspan="2" class="col-num">№</th>
      <th rowspan="2" class="col-fio">ФИО</th>
      <th colspan="2">Входящие</th>
      <th rowspan="2" class="col-out">Исходящие</th>
    </tr>
    <tr>
      <th class="col-in">Принятые</th>
      <th class="col-miss">Пропущенные</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="col-num">1</td>
      <td class="col-fio">Нурулина Наталья Владимировна</td>
      <td class="col-in">171</td>
      <td class="col-miss">113</td>
      <td class="col-out">194</td>
    </tr>
    <tr>
      <td class="col-num">2</td>
      <td class="col-fio">Кузнецова Надежда Александровна</td>
      <td class="col-in">103</td>
      <td class="col-miss">17</td>
      <td class="col-out">67</td>
    </tr>
    <tr>
      <td class="col-num">3</td>
      <td class="col-fio">Обломкина Лариса Ивановна</td>
      <td class="col-in">80</td>
      <td class="col-miss">14</td>
      <td class="col-out">87</td>
    </tr>
    <tr>
      <td class="col-num">4</td>
      <td class="col-fio">Нурлубаева Алина Залимхановна</td>
      <td class="col-in">119</td>
      <td class="col-miss">21</td>
      <td class="col-out">39</td>
    </tr>
    <tr>
      <td class="col-num">5</td>
      <td class="col-fio">Дмитриенко Татьяна Валерьевна</td>
      <td class="col-in">105</td>
      <td class="col-miss">10</td>
      <td class="col-out">64</td>
    </tr>
    <tr>
      <td class="col-num">6</td>
      <td class="col-fio">Мухамадеева Танзиля Рафкатовна</td>
      <td class="col-in">88</td>
      <td class="col-miss">13</td>
      <td class="col-out">74</td>
    </tr>
    <tr>
      <td class="col-num">7</td>
      <td class="col-fio">Карташова Мария Александровна</td>
      <td class="col-in">63</td>
      <td class="col-miss">15</td>
      <td class="col-out">81</td>
    </tr>
    <tr>
      <td class="col-num">8</td>
      <td class="col-fio">Горохова Алёна Павловна</td>
      <td class="col-in">69</td>
      <td class="col-miss">18</td>
      <td class="col-out">51</td>
    </tr>
    <tr>
      <td class="col-num">9</td>
      <td class="col-fio">Кундаль Нина Валерьевна</td>
      <td class="col-in">70</td>
      <td class="col-miss">11</td>
      <td class="col-out">48</td>
    </tr>
    <tr>
      <td class="col-num">10</td>
      <td class="col-fio">Якута Светлана Михайловна</td>
      <td class="col-in">35</td>
      <td class="col-miss">18</td>
      <td class="col-out">41</td>
    </tr>
    <tr>
      <td class="col-num">11</td>
      <td class="col-fio">Иванова Любовь Васильевна</td>
      <td class="col-in">0</td>
      <td class="col-miss">2</td>
      <td class="col-out">0</td>
    </tr>
  </tbody>
</table>
    </div>
  </div>
</div>

## Статистика

<div class="facts-grid">
<div class="fact-card fact-time">
  <div class="fact-label">Максимальная длительность звонка</div>
  <div class="fact-value">Родина Наталья Васильевна → Ядрова Анна Викторовна</div>
  <div class="fact-sub">Длительность: 28 мин 07 с · 2026-09-10 11:43:01</div>
</div>
<div class="fact-card fact-pair">
  <div class="fact-label">Наиболее частая пара абонентов</div>
  <div class="fact-value">Родина Наталья Васильевна ⇄ Ядрова Анна Викторовна</div>
  <div class="fact-sub">Всего звонков: 174</div>
</div>
<div class="fact-card fact-out">
  <div class="fact-label">Лидер по исходящим звонкам</div>
  <div class="fact-value">Константинова Людмила Алексеевна</div>
  <div class="fact-sub">Исходящих: 423</div>
</div>
<div class="fact-card fact-in">
  <div class="fact-label">Лидер по принятым звонкам</div>
  <div class="fact-value">Родина Наталья Васильевна</div>
  <div class="fact-sub">Принятых: 435</div>
</div>
<div class="fact-card fact-miss">
  <div class="fact-label">Наибольшая доля пропущенных звонков</div>
  <div class="fact-value">Чечеткин Михаил Игоревич</div>
  <div class="fact-sub">332 из 592 входящих · 56%</div>
</div>
<div class="fact-card fact-in">
  <div class="fact-label">Наилучший приём звонков</div>
  <div class="fact-value">Вернер Елена Викторовна</div>
  <div class="fact-sub">57 из 58 входящих · 98%</div>
</div>
<div class="fact-card fact-hour">
  <div class="fact-label">Час пиковой нагрузки</div>
  <div class="fact-value">15:00 – 15:59</div>
  <div class="fact-sub">Звонков: 2410</div>
</div>
</div>
