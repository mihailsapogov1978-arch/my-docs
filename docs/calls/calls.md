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
}

.calls-total {
    display: grid;
    grid-template-columns: minmax(220px, 1fr) 130px 130px 130px;
    align-items: stretch;
    background: var(--emp-accent-light);
    border: 1px solid var(--emp-accent-border);
    border-radius: 8px;
    margin: 10px 0 24px 0;
    overflow: hidden;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
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

.calls-table {
    width: 100%;
    border-collapse: collapse;
    background: #fff;
    font-size: 13.5px;
    table-layout: fixed;
}
.calls-table col.col-num  { width: 40px; }
.calls-table col.col-fio  { width: auto; }
.calls-table col.col-stat { width: 140px; }
.calls-table col.col-pct  { width: 110px; }

.calls-table thead th {
    background: #f0f7ff;
    color: var(--emp-accent);
    font-weight: 700;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.02em;
    padding: 6px 6px;
    border-bottom: 1px solid var(--emp-accent-border);
    border-right: 1px solid var(--emp-accent-border);
    text-align: center;
    vertical-align: middle;
    white-space: nowrap;
    word-break: keep-all;
}
.calls-table thead th:last-child { border-right: none; }

.calls-table tbody td {
    padding: 8px 8px;
    border-bottom: 1px solid var(--emp-border);
    border-right: 1px solid var(--emp-border);
    text-align: right;
    font-weight: 700;
    white-space: nowrap;
}
.calls-table tbody td:last-child { border-right: none; }
.calls-table tbody tr:last-child td { border-bottom: none; }

.calls-table .col-num { color: var(--emp-muted); text-align: right; }
.calls-table .col-fio { color: var(--emp-text); font-weight: 600; text-align: left; white-space: normal; overflow: hidden; text-overflow: ellipsis; }
.calls-table .col-in   { color: var(--emp-in); }
.calls-table .col-miss { color: var(--emp-missed); }
.calls-table .col-out  { color: var(--emp-out); }
.calls-table .col-pct { text-align: center; font-weight: 700; }
.calls-table .col-pct.pct-good { color: var(--emp-in); }
.calls-table .col-pct.pct-warn { color: #b7791f; }
.calls-table .col-pct.pct-bad  { color: var(--emp-missed); }

.load-chart {
    margin: 16px 0 24px 0;
    padding: 16px 20px;
    border: 1px solid var(--emp-border);
    border-radius: 10px;
    background: #fff;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}
.load-chart-row {
    display: grid;
    grid-template-columns: 260px 1fr 70px;
    align-items: center;
    column-gap: 14px;
    padding: 8px 0;
    border-bottom: 1px dashed var(--emp-border);
}
.load-chart-row:last-child { border-bottom: none; }
.load-chart-name { font-size: 13px; color: var(--emp-text); font-weight: 600; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.load-chart-bar-wrap { position: relative; width: 100%; height: 22px; background: #f7fafc; border-radius: 4px; overflow: hidden; }
.load-chart-bar { display: flex; height: 100%; border-radius: 4px; overflow: hidden; transition: width 0.3s ease; }
.load-chart-seg { height: 100%; transition: opacity 0.15s; }
.load-chart-seg.seg-in   { background: #6fa8b8; }
.load-chart-seg.seg-miss { background: #f5a623; }
.load-chart-seg.seg-out  { background: #8ba0c4; }
.load-chart-value { text-align: right; font-size: 13px; font-weight: 700; color: var(--emp-accent); white-space: nowrap; }
.load-chart-legend { display: flex; flex-wrap: wrap; gap: 18px; margin-top: 16px; padding-top: 12px; border-top: 1px solid var(--emp-border); font-size: 12.5px; color: var(--emp-muted); }
.load-chart-legend-item { display: inline-flex; align-items: center; gap: 6px; }
.load-chart-legend-dot { display: inline-block; width: 12px; height: 12px; border-radius: 3px; }
.load-chart-legend-dot.legend-in   { background: #6fa8b8; }
.load-chart-legend-dot.legend-miss { background: #f5a623; }
.load-chart-legend-dot.legend-out  { background: #8ba0c4; }

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
.fact-label { font-size: 11.5px; text-transform: uppercase; letter-spacing: 0.05em; color: var(--emp-muted); font-weight: 700; margin-bottom: 8px; }
.fact-value { font-size: 15px; color: var(--emp-text); font-weight: 700; line-height: 1.35; margin-bottom: 6px; }
.fact-sub { font-size: 13px; color: var(--emp-muted); font-weight: 500; line-height: 1.4; }
.fact-card.fact-time  { border-left-color: #805ad5; }
.fact-card.fact-pair  { border-left-color: #d53f8c; }
.fact-card.fact-out   { border-left-color: var(--emp-out); }
.fact-card.fact-in    { border-left-color: var(--emp-in); }
.fact-card.fact-miss  { border-left-color: var(--emp-missed); }
.fact-card.fact-hour  { border-left-color: #dd6b20; }

.calls-source {
    font-size: 13px;
    color: var(--emp-muted);
    margin: 4px 0 16px 0;
    line-height: 1.6;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}

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
    .load-chart-row { grid-template-columns: 1fr 70px; row-gap: 4px; }
    .load-chart-name { grid-column: 1 / -1; }
}

@media (max-width: 720px) {
    .calls-total { grid-template-columns: 1fr; }
    .calls-total .ct-label { padding: 12px 16px; border-bottom: 1px solid var(--emp-accent-border); }
    .calls-total .ct-cell { border-left: none; border-top: 1px solid var(--emp-accent-border); padding: 10px 16px; }
    .calls-table th, .calls-table td { padding: 8px 8px; }
    .load-chart { padding: 12px 14px; }
}
</style>


# Статистика звонков

## Октябрь

<div class="calls-total">
  <div class="ct-label">Всего звонков</div>
  <div class="ct-cell ct-in"><div class="ct-value">9479</div><div class="ct-caption">Принятые</div></div>
  <div class="ct-cell ct-miss"><div class="ct-value">2942</div><div class="ct-caption">Пропущенные</div></div>
  <div class="ct-cell ct-out"><div class="ct-value">9565</div><div class="ct-caption">Исходящие</div></div>
</div>

### Детализация по подразделениям

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-Октябрь-1" class="dept-checkbox">
    <label for="dept-Октябрь-1" class="dept-row">
      <span class="dept-name">Администрация</span>
      <span class="dept-summary">
        <span class="ds-cell"><span class="ds-label">принято:</span> <b>1139</b></span>
        <span class="ds-cell"><span class="ds-label">пропущено:</span> <b>530</b></span>
        <span class="ds-cell"><span class="ds-label">исходящих:</span> <b>953</b></span>
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
    <col class="col-pct">
    <col class="col-stat">
  </colgroup>
  <thead>
    <tr>
      <th rowspan="2" class="col-num">№</th>
      <th rowspan="2" class="col-fio">ФИО</th>
      <th colspan="2">Входящие</th>
      <th rowspan="2" class="col-pct">Принято, %</th>
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
      <td class="col-fio">Родина Наталья Васильевна</td>
      <td class="col-in">458</td>
      <td class="col-miss">169</td>
      <td class="col-pct pct-warn">73%</td>
      <td class="col-out">309</td>
    </tr>
    <tr>
      <td class="col-num">2</td>
      <td class="col-fio">Останин Иван Георгиевич</td>
      <td class="col-in">398</td>
      <td class="col-miss">246</td>
      <td class="col-pct pct-warn">62%</td>
      <td class="col-out">246</td>
    </tr>
    <tr>
      <td class="col-num">3</td>
      <td class="col-fio">Жданова Галина Игоревна</td>
      <td class="col-in">140</td>
      <td class="col-miss">41</td>
      <td class="col-pct pct-warn">77%</td>
      <td class="col-out">173</td>
    </tr>
    <tr>
      <td class="col-num">4</td>
      <td class="col-fio">Гареева Регина Рафаэлевна</td>
      <td class="col-in">67</td>
      <td class="col-miss">41</td>
      <td class="col-pct pct-warn">62%</td>
      <td class="col-out">155</td>
    </tr>
    <tr>
      <td class="col-num">5</td>
      <td class="col-fio">Галямов Азат Ахтамович</td>
      <td class="col-in">76</td>
      <td class="col-miss">33</td>
      <td class="col-pct pct-warn">70%</td>
      <td class="col-out">70</td>
    </tr>
  </tbody>
</table>
    </div>
  </div>
  <div class="dept-item">
    <input type="checkbox" id="dept-Октябрь-2" class="dept-checkbox">
    <label for="dept-Октябрь-2" class="dept-row">
      <span class="dept-name">Отдел информационной безопасности</span>
      <span class="dept-summary">
        <span class="ds-cell"><span class="ds-label">принято:</span> <b>322</b></span>
        <span class="ds-cell"><span class="ds-label">пропущено:</span> <b>100</b></span>
        <span class="ds-cell"><span class="ds-label">исходящих:</span> <b>191</b></span>
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
    <col class="col-pct">
    <col class="col-stat">
  </colgroup>
  <thead>
    <tr>
      <th rowspan="2" class="col-num">№</th>
      <th rowspan="2" class="col-fio">ФИО</th>
      <th colspan="2">Входящие</th>
      <th rowspan="2" class="col-pct">Принято, %</th>
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
      <td class="col-in">143</td>
      <td class="col-miss">32</td>
      <td class="col-pct pct-good">82%</td>
      <td class="col-out">69</td>
    </tr>
    <tr>
      <td class="col-num">2</td>
      <td class="col-fio">Лычев Антон Владимирович</td>
      <td class="col-in">129</td>
      <td class="col-miss">39</td>
      <td class="col-pct pct-warn">77%</td>
      <td class="col-out">46</td>
    </tr>
    <tr>
      <td class="col-num">3</td>
      <td class="col-fio">Ананьев Евгений Сергеевич</td>
      <td class="col-in">13</td>
      <td class="col-miss">21</td>
      <td class="col-pct pct-bad">38%</td>
      <td class="col-out">47</td>
    </tr>
    <tr>
      <td class="col-num">4</td>
      <td class="col-fio">Шляпин Денис Олегович</td>
      <td class="col-in">37</td>
      <td class="col-miss">8</td>
      <td class="col-pct pct-good">82%</td>
      <td class="col-out">29</td>
    </tr>
  </tbody>
</table>
    </div>
  </div>
  <div class="dept-item">
    <input type="checkbox" id="dept-Октябрь-3" class="dept-checkbox">
    <label for="dept-Октябрь-3" class="dept-row">
      <span class="dept-name">Отдел СР и ТП</span>
      <span class="dept-summary">
        <span class="ds-cell"><span class="ds-label">принято:</span> <b>1056</b></span>
        <span class="ds-cell"><span class="ds-label">пропущено:</span> <b>761</b></span>
        <span class="ds-cell"><span class="ds-label">исходящих:</span> <b>729</b></span>
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
    <col class="col-pct">
    <col class="col-stat">
  </colgroup>
  <thead>
    <tr>
      <th rowspan="2" class="col-num">№</th>
      <th rowspan="2" class="col-fio">ФИО</th>
      <th colspan="2">Входящие</th>
      <th rowspan="2" class="col-pct">Принято, %</th>
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
      <td class="col-fio">Роганова Анна Анатольевна</td>
      <td class="col-in">358</td>
      <td class="col-miss">260</td>
      <td class="col-pct pct-warn">58%</td>
      <td class="col-out">97</td>
    </tr>
    <tr>
      <td class="col-num">2</td>
      <td class="col-fio">Сапогов Михаил Дмитриевич</td>
      <td class="col-in">233</td>
      <td class="col-miss">94</td>
      <td class="col-pct pct-warn">71%</td>
      <td class="col-out">181</td>
    </tr>
    <tr>
      <td class="col-num">3</td>
      <td class="col-fio">Чечеткин Михаил Игоревич</td>
      <td class="col-in">86</td>
      <td class="col-miss">276</td>
      <td class="col-pct pct-bad">24%</td>
      <td class="col-out">106</td>
    </tr>
    <tr>
      <td class="col-num">4</td>
      <td class="col-fio">Кошик Владимир Иванович</td>
      <td class="col-in">161</td>
      <td class="col-miss">42</td>
      <td class="col-pct pct-warn">79%</td>
      <td class="col-out">163</td>
    </tr>
    <tr>
      <td class="col-num">5</td>
      <td class="col-fio">Худышкин Сергей Николаевич</td>
      <td class="col-in">79</td>
      <td class="col-miss">22</td>
      <td class="col-pct pct-warn">78%</td>
      <td class="col-out">84</td>
    </tr>
    <tr>
      <td class="col-num">6</td>
      <td class="col-fio">Мулявин Яков Владиславович</td>
      <td class="col-in">67</td>
      <td class="col-miss">10</td>
      <td class="col-pct pct-good">87%</td>
      <td class="col-out">55</td>
    </tr>
    <tr>
      <td class="col-num">7</td>
      <td class="col-fio">Гасанов Сархан Нураддин</td>
      <td class="col-in">72</td>
      <td class="col-miss">9</td>
      <td class="col-pct pct-good">89%</td>
      <td class="col-out">43</td>
    </tr>
    <tr>
      <td class="col-num">8</td>
      <td class="col-fio">Обмолова Валентина Витальевна</td>
      <td class="col-in">0</td>
      <td class="col-miss">36</td>
      <td class="col-pct pct-bad">0%</td>
      <td class="col-out">0</td>
    </tr>
    <tr>
      <td class="col-num">9</td>
      <td class="col-fio">Ставер Андрей Петрович</td>
      <td class="col-in">0</td>
      <td class="col-miss">12</td>
      <td class="col-pct pct-bad">0%</td>
      <td class="col-out">0</td>
    </tr>
  </tbody>
</table>
    </div>
  </div>
  <div class="dept-item">
    <input type="checkbox" id="dept-Октябрь-4" class="dept-checkbox">
    <label for="dept-Октябрь-4" class="dept-row">
      <span class="dept-name">Отдел кадрового и правового обеспечения</span>
      <span class="dept-summary">
        <span class="ds-cell"><span class="ds-label">принято:</span> <b>597</b></span>
        <span class="ds-cell"><span class="ds-label">пропущено:</span> <b>204</b></span>
        <span class="ds-cell"><span class="ds-label">исходящих:</span> <b>819</b></span>
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
    <col class="col-pct">
    <col class="col-stat">
  </colgroup>
  <thead>
    <tr>
      <th rowspan="2" class="col-num">№</th>
      <th rowspan="2" class="col-fio">ФИО</th>
      <th colspan="2">Входящие</th>
      <th rowspan="2" class="col-pct">Принято, %</th>
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
      <td class="col-in">192</td>
      <td class="col-miss">103</td>
      <td class="col-pct pct-warn">65%</td>
      <td class="col-out">392</td>
    </tr>
    <tr>
      <td class="col-num">2</td>
      <td class="col-fio">Чернов Андрей Анатольевич</td>
      <td class="col-in">239</td>
      <td class="col-miss">59</td>
      <td class="col-pct pct-good">80%</td>
      <td class="col-out">136</td>
    </tr>
    <tr>
      <td class="col-num">3</td>
      <td class="col-fio">Полякова Анна Викторовна</td>
      <td class="col-in">100</td>
      <td class="col-miss">15</td>
      <td class="col-pct pct-good">87%</td>
      <td class="col-out">128</td>
    </tr>
    <tr>
      <td class="col-num">4</td>
      <td class="col-fio">Суханова Ирина Константиновна</td>
      <td class="col-in">41</td>
      <td class="col-miss">20</td>
      <td class="col-pct pct-warn">67%</td>
      <td class="col-out">141</td>
    </tr>
    <tr>
      <td class="col-num">5</td>
      <td class="col-fio">Цветнова Наталья Геннадьевна</td>
      <td class="col-in">25</td>
      <td class="col-miss">7</td>
      <td class="col-pct pct-warn">78%</td>
      <td class="col-out">22</td>
    </tr>
  </tbody>
</table>
    </div>
  </div>
  <div class="dept-item">
    <input type="checkbox" id="dept-Октябрь-5" class="dept-checkbox">
    <label for="dept-Октябрь-5" class="dept-row">
      <span class="dept-name">Отдел учета основных средств и запасов</span>
      <span class="dept-summary">
        <span class="ds-cell"><span class="ds-label">принято:</span> <b>1263</b></span>
        <span class="ds-cell"><span class="ds-label">пропущено:</span> <b>160</b></span>
        <span class="ds-cell"><span class="ds-label">исходящих:</span> <b>1448</b></span>
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
    <col class="col-pct">
    <col class="col-stat">
  </colgroup>
  <thead>
    <tr>
      <th rowspan="2" class="col-num">№</th>
      <th rowspan="2" class="col-fio">ФИО</th>
      <th colspan="2">Входящие</th>
      <th rowspan="2" class="col-pct">Принято, %</th>
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
      <td class="col-in">250</td>
      <td class="col-miss">38</td>
      <td class="col-pct pct-good">87%</td>
      <td class="col-out">301</td>
    </tr>
    <tr>
      <td class="col-num">2</td>
      <td class="col-fio">Петрова Наталья Александровна</td>
      <td class="col-in">192</td>
      <td class="col-miss">16</td>
      <td class="col-pct pct-good">92%</td>
      <td class="col-out">189</td>
    </tr>
    <tr>
      <td class="col-num">3</td>
      <td class="col-fio">Зуева Галия Парвасьевна</td>
      <td class="col-in">138</td>
      <td class="col-miss">7</td>
      <td class="col-pct pct-good">95%</td>
      <td class="col-out">193</td>
    </tr>
    <tr>
      <td class="col-num">4</td>
      <td class="col-fio">Стрельникова Ольга Сергеевна</td>
      <td class="col-in">154</td>
      <td class="col-miss">40</td>
      <td class="col-pct pct-warn">79%</td>
      <td class="col-out">114</td>
    </tr>
    <tr>
      <td class="col-num">5</td>
      <td class="col-fio">Филиппова Олеся Валерьевна</td>
      <td class="col-in">129</td>
      <td class="col-miss">12</td>
      <td class="col-pct pct-good">91%</td>
      <td class="col-out">118</td>
    </tr>
    <tr>
      <td class="col-num">6</td>
      <td class="col-fio">Бусыгина Ирина Сергеевна</td>
      <td class="col-in">68</td>
      <td class="col-miss">9</td>
      <td class="col-pct pct-good">88%</td>
      <td class="col-out">131</td>
    </tr>
    <tr>
      <td class="col-num">7</td>
      <td class="col-fio">Щирская Ксения Васильевна</td>
      <td class="col-in">60</td>
      <td class="col-miss">12</td>
      <td class="col-pct pct-good">83%</td>
      <td class="col-out">105</td>
    </tr>
    <tr>
      <td class="col-num">8</td>
      <td class="col-fio">Ильницкая Светлана Викторовна</td>
      <td class="col-in">68</td>
      <td class="col-miss">12</td>
      <td class="col-pct pct-good">85%</td>
      <td class="col-out">79</td>
    </tr>
    <tr>
      <td class="col-num">9</td>
      <td class="col-fio">Шибанаева Татьяна Викторовна</td>
      <td class="col-in">86</td>
      <td class="col-miss">6</td>
      <td class="col-pct pct-good">93%</td>
      <td class="col-out">60</td>
    </tr>
    <tr>
      <td class="col-num">10</td>
      <td class="col-fio">Минакова Ольга Фахрутдиновна</td>
      <td class="col-in">60</td>
      <td class="col-miss">7</td>
      <td class="col-pct pct-good">90%</td>
      <td class="col-out">85</td>
    </tr>
    <tr>
      <td class="col-num">11</td>
      <td class="col-fio">Вернер Елена Викторовна</td>
      <td class="col-in">58</td>
      <td class="col-miss">1</td>
      <td class="col-pct pct-good">98%</td>
      <td class="col-out">73</td>
    </tr>
  </tbody>
</table>
    </div>
  </div>
  <div class="dept-item">
    <input type="checkbox" id="dept-Октябрь-6" class="dept-checkbox">
    <label for="dept-Октябрь-6" class="dept-row">
      <span class="dept-name">Отдел подготовки отчетности</span>
      <span class="dept-summary">
        <span class="ds-cell"><span class="ds-label">принято:</span> <b>650</b></span>
        <span class="ds-cell"><span class="ds-label">пропущено:</span> <b>117</b></span>
        <span class="ds-cell"><span class="ds-label">исходящих:</span> <b>724</b></span>
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
    <col class="col-pct">
    <col class="col-stat">
  </colgroup>
  <thead>
    <tr>
      <th rowspan="2" class="col-num">№</th>
      <th rowspan="2" class="col-fio">ФИО</th>
      <th colspan="2">Входящие</th>
      <th rowspan="2" class="col-pct">Принято, %</th>
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
      <td class="col-in">189</td>
      <td class="col-miss">60</td>
      <td class="col-pct pct-warn">76%</td>
      <td class="col-out">274</td>
    </tr>
    <tr>
      <td class="col-num">2</td>
      <td class="col-fio">Шевелева Ксения Викторовна</td>
      <td class="col-in">156</td>
      <td class="col-miss">23</td>
      <td class="col-pct pct-good">87%</td>
      <td class="col-out">126</td>
    </tr>
    <tr>
      <td class="col-num">3</td>
      <td class="col-fio">Янова Екатерина Анатольевна</td>
      <td class="col-in">80</td>
      <td class="col-miss">7</td>
      <td class="col-pct pct-good">92%</td>
      <td class="col-out">122</td>
    </tr>
    <tr>
      <td class="col-num">4</td>
      <td class="col-fio">Лейпожих Алёна Алексеевна</td>
      <td class="col-in">64</td>
      <td class="col-miss">16</td>
      <td class="col-pct pct-good">80%</td>
      <td class="col-out">54</td>
    </tr>
    <tr>
      <td class="col-num">5</td>
      <td class="col-fio">Чистякова Елена Дмитриевна</td>
      <td class="col-in">50</td>
      <td class="col-miss">5</td>
      <td class="col-pct pct-good">91%</td>
      <td class="col-out">71</td>
    </tr>
    <tr>
      <td class="col-num">6</td>
      <td class="col-fio">Ребась Кристина Владимировна</td>
      <td class="col-in">42</td>
      <td class="col-miss">4</td>
      <td class="col-pct pct-good">91%</td>
      <td class="col-out">33</td>
    </tr>
    <tr>
      <td class="col-num">7</td>
      <td class="col-fio">Павлова Надежда Григорьевна</td>
      <td class="col-in">45</td>
      <td class="col-miss">2</td>
      <td class="col-pct pct-good">96%</td>
      <td class="col-out">29</td>
    </tr>
    <tr>
      <td class="col-num">8</td>
      <td class="col-fio">Яковлева Вилена Фаильевна</td>
      <td class="col-in">24</td>
      <td class="col-miss">0</td>
      <td class="col-pct pct-good">100%</td>
      <td class="col-out">15</td>
    </tr>
  </tbody>
</table>
    </div>
  </div>
  <div class="dept-item">
    <input type="checkbox" id="dept-Октябрь-7" class="dept-checkbox">
    <label for="dept-Октябрь-7" class="dept-row">
      <span class="dept-name">Отдел учета доходов</span>
      <span class="dept-summary">
        <span class="ds-cell"><span class="ds-label">принято:</span> <b>864</b></span>
        <span class="ds-cell"><span class="ds-label">пропущено:</span> <b>131</b></span>
        <span class="ds-cell"><span class="ds-label">исходящих:</span> <b>732</b></span>
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
    <col class="col-pct">
    <col class="col-stat">
  </colgroup>
  <thead>
    <tr>
      <th rowspan="2" class="col-num">№</th>
      <th rowspan="2" class="col-fio">ФИО</th>
      <th colspan="2">Входящие</th>
      <th rowspan="2" class="col-pct">Принято, %</th>
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
      <td class="col-fio">Жукова Анастасия Сергеевна</td>
      <td class="col-in">94</td>
      <td class="col-miss">7</td>
      <td class="col-pct pct-good">93%</td>
      <td class="col-out">133</td>
    </tr>
    <tr>
      <td class="col-num">2</td>
      <td class="col-fio">Лаба Вера Алексеевна</td>
      <td class="col-in">77</td>
      <td class="col-miss">17</td>
      <td class="col-pct pct-good">82%</td>
      <td class="col-out">122</td>
    </tr>
    <tr>
      <td class="col-num">3</td>
      <td class="col-fio">Занина Ирина Александровна</td>
      <td class="col-in">104</td>
      <td class="col-miss">13</td>
      <td class="col-pct pct-good">89%</td>
      <td class="col-out">74</td>
    </tr>
    <tr>
      <td class="col-num">4</td>
      <td class="col-fio">Кропотов Иван Александрович</td>
      <td class="col-in">108</td>
      <td class="col-miss">5</td>
      <td class="col-pct pct-good">96%</td>
      <td class="col-out">74</td>
    </tr>
    <tr>
      <td class="col-num">5</td>
      <td class="col-fio">Каргаполова Алёна Андреевна</td>
      <td class="col-in">79</td>
      <td class="col-miss">14</td>
      <td class="col-pct pct-good">85%</td>
      <td class="col-out">92</td>
    </tr>
    <tr>
      <td class="col-num">6</td>
      <td class="col-fio">Семенова Наталья Викторовна</td>
      <td class="col-in">104</td>
      <td class="col-miss">9</td>
      <td class="col-pct pct-good">92%</td>
      <td class="col-out">51</td>
    </tr>
    <tr>
      <td class="col-num">7</td>
      <td class="col-fio">Леванских Людмила Владимировна</td>
      <td class="col-in">60</td>
      <td class="col-miss">6</td>
      <td class="col-pct pct-good">91%</td>
      <td class="col-out">66</td>
    </tr>
    <tr>
      <td class="col-num">8</td>
      <td class="col-fio">Семенова Наталья Александровна</td>
      <td class="col-in">44</td>
      <td class="col-miss">48</td>
      <td class="col-pct pct-bad">48%</td>
      <td class="col-out">39</td>
    </tr>
    <tr>
      <td class="col-num">9</td>
      <td class="col-fio">Фаузер Татьяна Леовна</td>
      <td class="col-in">91</td>
      <td class="col-miss">6</td>
      <td class="col-pct pct-good">94%</td>
      <td class="col-out">20</td>
    </tr>
    <tr>
      <td class="col-num">10</td>
      <td class="col-fio">Юшкевич Татьяна Владимировна</td>
      <td class="col-in">67</td>
      <td class="col-miss">5</td>
      <td class="col-pct pct-good">93%</td>
      <td class="col-out">44</td>
    </tr>
    <tr>
      <td class="col-num">11</td>
      <td class="col-fio">Мицура Ираида Илдаровна</td>
      <td class="col-in">36</td>
      <td class="col-miss">1</td>
      <td class="col-pct pct-good">97%</td>
      <td class="col-out">17</td>
    </tr>
  </tbody>
</table>
    </div>
  </div>
  <div class="dept-item">
    <input type="checkbox" id="dept-Октябрь-8" class="dept-checkbox">
    <label for="dept-Октябрь-8" class="dept-row">
      <span class="dept-name">Отдел расчётов с персоналом</span>
      <span class="dept-summary">
        <span class="ds-cell"><span class="ds-label">принято:</span> <b>2506</b></span>
        <span class="ds-cell"><span class="ds-label">пропущено:</span> <b>692</b></span>
        <span class="ds-cell"><span class="ds-label">исходящих:</span> <b>3004</b></span>
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
    <col class="col-pct">
    <col class="col-stat">
  </colgroup>
  <thead>
    <tr>
      <th rowspan="2" class="col-num">№</th>
      <th rowspan="2" class="col-fio">ФИО</th>
      <th colspan="2">Входящие</th>
      <th rowspan="2" class="col-pct">Принято, %</th>
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
      <td class="col-fio">Ильдеркина Ирина Николаевна</td>
      <td class="col-in">326</td>
      <td class="col-miss">116</td>
      <td class="col-pct pct-warn">74%</td>
      <td class="col-out">379</td>
    </tr>
    <tr>
      <td class="col-num">2</td>
      <td class="col-fio">Алыкова Татьяна Валерьевна</td>
      <td class="col-in">278</td>
      <td class="col-miss">61</td>
      <td class="col-pct pct-good">82%</td>
      <td class="col-out">322</td>
    </tr>
    <tr>
      <td class="col-num">3</td>
      <td class="col-fio">Константинова Людмила Алексеевна</td>
      <td class="col-in">168</td>
      <td class="col-miss">52</td>
      <td class="col-pct pct-warn">76%</td>
      <td class="col-out">360</td>
    </tr>
    <tr>
      <td class="col-num">4</td>
      <td class="col-fio">Конева Елена Ивановна</td>
      <td class="col-in">192</td>
      <td class="col-miss">59</td>
      <td class="col-pct pct-warn">76%</td>
      <td class="col-out">306</td>
    </tr>
    <tr>
      <td class="col-num">5</td>
      <td class="col-fio">Павлова Ирина Игоревна</td>
      <td class="col-in">244</td>
      <td class="col-miss">57</td>
      <td class="col-pct pct-good">81%</td>
      <td class="col-out">146</td>
    </tr>
    <tr>
      <td class="col-num">6</td>
      <td class="col-fio">Казанцева Лариса Анатольевна</td>
      <td class="col-in">157</td>
      <td class="col-miss">62</td>
      <td class="col-pct pct-warn">72%</td>
      <td class="col-out">215</td>
    </tr>
    <tr>
      <td class="col-num">7</td>
      <td class="col-fio">Манджиева Алевтина Алексеевна</td>
      <td class="col-in">169</td>
      <td class="col-miss">35</td>
      <td class="col-pct pct-good">83%</td>
      <td class="col-out">229</td>
    </tr>
    <tr>
      <td class="col-num">8</td>
      <td class="col-fio">Сафаралеева Елена Хайрулловна</td>
      <td class="col-in">154</td>
      <td class="col-miss">63</td>
      <td class="col-pct pct-warn">71%</td>
      <td class="col-out">207</td>
    </tr>
    <tr>
      <td class="col-num">9</td>
      <td class="col-fio">Шахова Галина Максимовна</td>
      <td class="col-in">126</td>
      <td class="col-miss">32</td>
      <td class="col-pct pct-warn">80%</td>
      <td class="col-out">208</td>
    </tr>
    <tr>
      <td class="col-num">10</td>
      <td class="col-fio">Россолова Екатерина Сергеевна</td>
      <td class="col-in">172</td>
      <td class="col-miss">27</td>
      <td class="col-pct pct-good">86%</td>
      <td class="col-out">111</td>
    </tr>
    <tr>
      <td class="col-num">11</td>
      <td class="col-fio">Букреева Елена Николаевна</td>
      <td class="col-in">150</td>
      <td class="col-miss">51</td>
      <td class="col-pct pct-warn">75%</td>
      <td class="col-out">88</td>
    </tr>
    <tr>
      <td class="col-num">12</td>
      <td class="col-fio">Злобина Мария Александровна</td>
      <td class="col-in">87</td>
      <td class="col-miss">15</td>
      <td class="col-pct pct-good">85%</td>
      <td class="col-out">123</td>
    </tr>
    <tr>
      <td class="col-num">13</td>
      <td class="col-fio">Русмиленко Инга Юрьевна</td>
      <td class="col-in">96</td>
      <td class="col-miss">33</td>
      <td class="col-pct pct-warn">74%</td>
      <td class="col-out">66</td>
    </tr>
    <tr>
      <td class="col-num">14</td>
      <td class="col-fio">Мунарева Виктория Игоревна</td>
      <td class="col-in">42</td>
      <td class="col-miss">3</td>
      <td class="col-pct pct-good">93%</td>
      <td class="col-out">131</td>
    </tr>
    <tr>
      <td class="col-num">15</td>
      <td class="col-fio">Ершова Алла Николаевна</td>
      <td class="col-in">84</td>
      <td class="col-miss">14</td>
      <td class="col-pct pct-good">86%</td>
      <td class="col-out">64</td>
    </tr>
    <tr>
      <td class="col-num">16</td>
      <td class="col-fio">Лазарева Екатерина Николаевна</td>
      <td class="col-in">61</td>
      <td class="col-miss">12</td>
      <td class="col-pct pct-good">84%</td>
      <td class="col-out">49</td>
    </tr>
  </tbody>
</table>
    </div>
  </div>
  <div class="dept-item">
    <input type="checkbox" id="dept-Октябрь-9" class="dept-checkbox">
    <label for="dept-Октябрь-9" class="dept-row">
      <span class="dept-name">Отдел расчётов с поставщиками, подрядчиками</span>
      <span class="dept-summary">
        <span class="ds-cell"><span class="ds-label">принято:</span> <b>1082</b></span>
        <span class="ds-cell"><span class="ds-label">пропущено:</span> <b>247</b></span>
        <span class="ds-cell"><span class="ds-label">исходящих:</span> <b>965</b></span>
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
    <col class="col-pct">
    <col class="col-stat">
  </colgroup>
  <thead>
    <tr>
      <th rowspan="2" class="col-num">№</th>
      <th rowspan="2" class="col-fio">ФИО</th>
      <th colspan="2">Входящие</th>
      <th rowspan="2" class="col-pct">Принято, %</th>
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
      <td class="col-in">136</td>
      <td class="col-miss">77</td>
      <td class="col-pct pct-warn">64%</td>
      <td class="col-out">153</td>
    </tr>
    <tr>
      <td class="col-num">2</td>
      <td class="col-fio">Карташова Мария Александровна</td>
      <td class="col-in">139</td>
      <td class="col-miss">26</td>
      <td class="col-pct pct-good">84%</td>
      <td class="col-out">180</td>
    </tr>
    <tr>
      <td class="col-num">3</td>
      <td class="col-fio">Якута Светлана Михайловна</td>
      <td class="col-in">100</td>
      <td class="col-miss">29</td>
      <td class="col-pct pct-warn">78%</td>
      <td class="col-out">124</td>
    </tr>
    <tr>
      <td class="col-num">4</td>
      <td class="col-fio">Мухамадеева Танзиля Рафкатовна</td>
      <td class="col-in">121</td>
      <td class="col-miss">12</td>
      <td class="col-pct pct-good">91%</td>
      <td class="col-out">117</td>
    </tr>
    <tr>
      <td class="col-num">5</td>
      <td class="col-fio">Кузнецова Надежда Александровна</td>
      <td class="col-in">122</td>
      <td class="col-miss">24</td>
      <td class="col-pct pct-good">84%</td>
      <td class="col-out">96</td>
    </tr>
    <tr>
      <td class="col-num">6</td>
      <td class="col-fio">Нурлубаева Алина Залимхановна</td>
      <td class="col-in">112</td>
      <td class="col-miss">31</td>
      <td class="col-pct pct-warn">78%</td>
      <td class="col-out">59</td>
    </tr>
    <tr>
      <td class="col-num">7</td>
      <td class="col-fio">Дмитриенко Татьяна Валерьевна</td>
      <td class="col-in">115</td>
      <td class="col-miss">9</td>
      <td class="col-pct pct-good">93%</td>
      <td class="col-out">76</td>
    </tr>
    <tr>
      <td class="col-num">8</td>
      <td class="col-fio">Обломкина Лариса Ивановна</td>
      <td class="col-in">89</td>
      <td class="col-miss">19</td>
      <td class="col-pct pct-good">82%</td>
      <td class="col-out">91</td>
    </tr>
    <tr>
      <td class="col-num">9</td>
      <td class="col-fio">Кундаль Нина Валерьевна</td>
      <td class="col-in">69</td>
      <td class="col-miss">10</td>
      <td class="col-pct pct-good">87%</td>
      <td class="col-out">27</td>
    </tr>
    <tr>
      <td class="col-num">10</td>
      <td class="col-fio">Иванова Любовь Васильевна</td>
      <td class="col-in">39</td>
      <td class="col-miss">7</td>
      <td class="col-pct pct-good">85%</td>
      <td class="col-out">24</td>
    </tr>
    <tr>
      <td class="col-num">11</td>
      <td class="col-fio">Горохова Алёна Павловна</td>
      <td class="col-in">40</td>
      <td class="col-miss">3</td>
      <td class="col-pct pct-good">93%</td>
      <td class="col-out">18</td>
    </tr>
  </tbody>
</table>
    </div>
  </div>
</div>

### Нагрузка отделов

<div class="calls-source">Сводные показатели по подразделениям. «Доля пропущенных» — процент входящих вызовов, не завершившихся разговором. «Индекс исх./вх.» — отношение исходящих к сумме входящих (>1 — отдел больше инициирует, <1 — больше принимает).</div>

<div class="load-chart">
<div class="load-chart-row">
  <div class="load-chart-name" title="Отдел расчётов с персоналом">Отдел расчётов с персоналом</div>
  <div class="load-chart-bar-wrap">
    <div class="load-chart-bar" style="width: 100.00%;">
      <div class="load-chart-seg seg-in" style="width: 40.41%;" title="Принятые: 2506"></div>
      <div class="load-chart-seg seg-miss" style="width: 11.16%;" title="Пропущенные: 692"></div>
      <div class="load-chart-seg seg-out" style="width: 48.44%;" title="Исходящие: 3004"></div>
    </div>
  </div>
  <div class="load-chart-value">6202</div>
</div>
<div class="load-chart-row">
  <div class="load-chart-name" title="Отдел учета основных средств и запасов">Отдел учета основных средств и запасов</div>
  <div class="load-chart-bar-wrap">
    <div class="load-chart-bar" style="width: 46.29%;">
      <div class="load-chart-seg seg-in" style="width: 43.99%;" title="Принятые: 1263"></div>
      <div class="load-chart-seg seg-miss" style="width: 5.57%;" title="Пропущенные: 160"></div>
      <div class="load-chart-seg seg-out" style="width: 50.44%;" title="Исходящие: 1448"></div>
    </div>
  </div>
  <div class="load-chart-value">2871</div>
</div>
<div class="load-chart-row">
  <div class="load-chart-name" title="Администрация">Администрация</div>
  <div class="load-chart-bar-wrap">
    <div class="load-chart-bar" style="width: 42.28%;">
      <div class="load-chart-seg seg-in" style="width: 43.44%;" title="Принятые: 1139"></div>
      <div class="load-chart-seg seg-miss" style="width: 20.21%;" title="Пропущенные: 530"></div>
      <div class="load-chart-seg seg-out" style="width: 36.35%;" title="Исходящие: 953"></div>
    </div>
  </div>
  <div class="load-chart-value">2622</div>
</div>
<div class="load-chart-row">
  <div class="load-chart-name" title="Отдел СР и ТП">Отдел СР и ТП</div>
  <div class="load-chart-bar-wrap">
    <div class="load-chart-bar" style="width: 41.05%;">
      <div class="load-chart-seg seg-in" style="width: 41.48%;" title="Принятые: 1056"></div>
      <div class="load-chart-seg seg-miss" style="width: 29.89%;" title="Пропущенные: 761"></div>
      <div class="load-chart-seg seg-out" style="width: 28.63%;" title="Исходящие: 729"></div>
    </div>
  </div>
  <div class="load-chart-value">2546</div>
</div>
<div class="load-chart-row">
  <div class="load-chart-name" title="Отдел расчётов с поставщиками, подрядчиками">Отдел расчётов с поставщиками, подрядчиками</div>
  <div class="load-chart-bar-wrap">
    <div class="load-chart-bar" style="width: 36.99%;">
      <div class="load-chart-seg seg-in" style="width: 47.17%;" title="Принятые: 1082"></div>
      <div class="load-chart-seg seg-miss" style="width: 10.77%;" title="Пропущенные: 247"></div>
      <div class="load-chart-seg seg-out" style="width: 42.07%;" title="Исходящие: 965"></div>
    </div>
  </div>
  <div class="load-chart-value">2294</div>
</div>
<div class="load-chart-row">
  <div class="load-chart-name" title="Отдел учета доходов">Отдел учета доходов</div>
  <div class="load-chart-bar-wrap">
    <div class="load-chart-bar" style="width: 27.85%;">
      <div class="load-chart-seg seg-in" style="width: 50.03%;" title="Принятые: 864"></div>
      <div class="load-chart-seg seg-miss" style="width: 7.59%;" title="Пропущенные: 131"></div>
      <div class="load-chart-seg seg-out" style="width: 42.39%;" title="Исходящие: 732"></div>
    </div>
  </div>
  <div class="load-chart-value">1727</div>
</div>
<div class="load-chart-row">
  <div class="load-chart-name" title="Отдел кадрового и правового обеспечения">Отдел кадрового и правового обеспечения</div>
  <div class="load-chart-bar-wrap">
    <div class="load-chart-bar" style="width: 26.12%;">
      <div class="load-chart-seg seg-in" style="width: 36.85%;" title="Принятые: 597"></div>
      <div class="load-chart-seg seg-miss" style="width: 12.59%;" title="Пропущенные: 204"></div>
      <div class="load-chart-seg seg-out" style="width: 50.56%;" title="Исходящие: 819"></div>
    </div>
  </div>
  <div class="load-chart-value">1620</div>
</div>
<div class="load-chart-row">
  <div class="load-chart-name" title="Отдел подготовки отчетности">Отдел подготовки отчетности</div>
  <div class="load-chart-bar-wrap">
    <div class="load-chart-bar" style="width: 24.04%;">
      <div class="load-chart-seg seg-in" style="width: 43.59%;" title="Принятые: 650"></div>
      <div class="load-chart-seg seg-miss" style="width: 7.85%;" title="Пропущенные: 117"></div>
      <div class="load-chart-seg seg-out" style="width: 48.56%;" title="Исходящие: 724"></div>
    </div>
  </div>
  <div class="load-chart-value">1491</div>
</div>
<div class="load-chart-row">
  <div class="load-chart-name" title="Отдел информационной безопасности">Отдел информационной безопасности</div>
  <div class="load-chart-bar-wrap">
    <div class="load-chart-bar" style="width: 9.88%;">
      <div class="load-chart-seg seg-in" style="width: 52.53%;" title="Принятые: 322"></div>
      <div class="load-chart-seg seg-miss" style="width: 16.31%;" title="Пропущенные: 100"></div>
      <div class="load-chart-seg seg-out" style="width: 31.16%;" title="Исходящие: 191"></div>
    </div>
  </div>
  <div class="load-chart-value">613</div>
</div>
  <div class="load-chart-legend">
    <span class="load-chart-legend-item"><span class="load-chart-legend-dot legend-in"></span>принятые</span>
    <span class="load-chart-legend-item"><span class="load-chart-legend-dot legend-miss"></span>пропущенные</span>
    <span class="load-chart-legend-item"><span class="load-chart-legend-dot legend-out"></span>исходящие</span>
  </div>
</div>

<div class="facts-grid">
<div class="fact-card fact-out">
  <div class="fact-label">Наибольшее число исходящих</div>
  <div class="fact-value">Отдел расчётов с персоналом</div>
  <div class="fact-sub">3004 исходящих звонков</div>
</div>
<div class="fact-card fact-in">
  <div class="fact-label">Наибольшее число принятых</div>
  <div class="fact-value">Отдел расчётов с персоналом</div>
  <div class="fact-sub">2506 принятых звонков</div>
</div>
<div class="fact-card fact-miss">
  <div class="fact-label">Наибольшая доля пропущенных</div>
  <div class="fact-value">Отдел СР и ТП</div>
  <div class="fact-sub">761 из 1817 входящих · 41.9%</div>
</div>
<div class="fact-card fact-in">
  <div class="fact-label">Наилучший приём вызовов</div>
  <div class="fact-value">Отдел учета основных средств и запасов</div>
  <div class="fact-sub">1263 из 1423 входящих · принято 88.8%</div>
</div>
<div class="fact-card fact-out">
  <div class="fact-label">Преобладание исходящих связей</div>
  <div class="fact-value">Отдел кадрового и правового обеспечения</div>
  <div class="fact-sub">Индекс исх./вх. = 1.02 — отдел больше инициирует, чем принимает</div>
</div>
<div class="fact-card fact-in">
  <div class="fact-label">Преобладание входящих связей</div>
  <div class="fact-value">Отдел СР и ТП</div>
  <div class="fact-sub">Индекс исх./вх. = 0.40 — отдел больше принимает, чем инициирует</div>
</div>
<div class="fact-card fact-hour">
  <div class="fact-label">Средняя нагрузка на сотрудника</div>
  <div class="fact-value">275 звонков / мес.</div>
  <div class="fact-sub">Всего: 21986 звонков, 80 сотрудников</div>
</div>
<div class="fact-card fact-pair">
  <div class="fact-label">Наибольший суммарный объём</div>
  <div class="fact-value">Отдел расчётов с персоналом</div>
  <div class="fact-sub">6202 звонков всех типов</div>
</div>
</div>

### Нагрузка сотрудников

<div class="facts-grid">
<div class="fact-card fact-time">
  <div class="fact-label">Максимальная длительность звонка</div>
  <div class="fact-value">Останин Иван Георгиевич → Худышкин Сергей Николаевич</div>
  <div class="fact-sub">Длительность: 27 мин 50 с · 2026-09-29 10:31:00</div>
</div>
<div class="fact-card fact-pair">
  <div class="fact-label">Наиболее частая пара абонентов</div>
  <div class="fact-value">Родина Наталья Васильевна ⇄ Ядрова Анна Викторовна</div>
  <div class="fact-sub">Всего звонков: 173</div>
</div>
<div class="fact-card fact-out">
  <div class="fact-label">Лидер по исходящим звонкам</div>
  <div class="fact-value">Ядрова Анна Викторовна</div>
  <div class="fact-sub">Исходящих: 392</div>
</div>
<div class="fact-card fact-in">
  <div class="fact-label">Лидер по принятым звонкам</div>
  <div class="fact-value">Родина Наталья Васильевна</div>
  <div class="fact-sub">Принятых: 458</div>
</div>
<div class="fact-card fact-miss">
  <div class="fact-label">Наибольшая доля пропущенных звонков</div>
  <div class="fact-value">Чечеткин Михаил Игоревич</div>
  <div class="fact-sub">276 из 362 входящих · 76%</div>
</div>
<div class="fact-card fact-in">
  <div class="fact-label">Наилучший приём звонков</div>
  <div class="fact-value">Вернер Елена Викторовна</div>
  <div class="fact-sub">58 из 59 входящих · 98%</div>
</div>
<div class="fact-card fact-hour">
  <div class="fact-label">Час пиковой нагрузки</div>
  <div class="fact-value">15:00 – 15:59</div>
  <div class="fact-sub">Звонков: 2503</div>
</div>
</div>

---

## Сентябрь

<div class="calls-total">
  <div class="ct-label">Всего звонков</div>
  <div class="ct-cell ct-in"><div class="ct-value">8966</div><div class="ct-caption">Принятые</div></div>
  <div class="ct-cell ct-miss"><div class="ct-value">2979</div><div class="ct-caption">Пропущенные</div></div>
  <div class="ct-cell ct-out"><div class="ct-value">9112</div><div class="ct-caption">Исходящие</div></div>
</div>

### Детализация по подразделениям

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-Сентябрь-1" class="dept-checkbox">
    <label for="dept-Сентябрь-1" class="dept-row">
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
    <col class="col-pct">
    <col class="col-stat">
  </colgroup>
  <thead>
    <tr>
      <th rowspan="2" class="col-num">№</th>
      <th rowspan="2" class="col-fio">ФИО</th>
      <th colspan="2">Входящие</th>
      <th rowspan="2" class="col-pct">Принято, %</th>
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
      <td class="col-pct pct-warn">62%</td>
      <td class="col-out">355</td>
    </tr>
    <tr>
      <td class="col-num">2</td>
      <td class="col-fio">Родина Наталья Васильевна</td>
      <td class="col-in">435</td>
      <td class="col-miss">183</td>
      <td class="col-pct pct-warn">70%</td>
      <td class="col-out">352</td>
    </tr>
    <tr>
      <td class="col-num">3</td>
      <td class="col-fio">Гареева Регина Рафаэлевна</td>
      <td class="col-in">102</td>
      <td class="col-miss">63</td>
      <td class="col-pct pct-warn">62%</td>
      <td class="col-out">207</td>
    </tr>
    <tr>
      <td class="col-num">4</td>
      <td class="col-fio">Жданова Галина Игоревна</td>
      <td class="col-in">132</td>
      <td class="col-miss">52</td>
      <td class="col-pct pct-warn">72%</td>
      <td class="col-out">169</td>
    </tr>
    <tr>
      <td class="col-num">5</td>
      <td class="col-fio">Галямов Азат Ахтамович</td>
      <td class="col-in">100</td>
      <td class="col-miss">47</td>
      <td class="col-pct pct-warn">68%</td>
      <td class="col-out">89</td>
    </tr>
  </tbody>
</table>
    </div>
  </div>
  <div class="dept-item">
    <input type="checkbox" id="dept-Сентябрь-2" class="dept-checkbox">
    <label for="dept-Сентябрь-2" class="dept-row">
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
    <col class="col-pct">
    <col class="col-stat">
  </colgroup>
  <thead>
    <tr>
      <th rowspan="2" class="col-num">№</th>
      <th rowspan="2" class="col-fio">ФИО</th>
      <th colspan="2">Входящие</th>
      <th rowspan="2" class="col-pct">Принято, %</th>
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
      <td class="col-pct pct-good">83%</td>
      <td class="col-out">71</td>
    </tr>
    <tr>
      <td class="col-num">2</td>
      <td class="col-fio">Ананьев Евгений Сергеевич</td>
      <td class="col-in">69</td>
      <td class="col-miss">32</td>
      <td class="col-pct pct-warn">68%</td>
      <td class="col-out">109</td>
    </tr>
    <tr>
      <td class="col-num">3</td>
      <td class="col-fio">Лычев Антон Владимирович</td>
      <td class="col-in">120</td>
      <td class="col-miss">37</td>
      <td class="col-pct pct-warn">76%</td>
      <td class="col-out">39</td>
    </tr>
    <tr>
      <td class="col-num">4</td>
      <td class="col-fio">Шляпин Денис Олегович</td>
      <td class="col-in">48</td>
      <td class="col-miss">13</td>
      <td class="col-pct pct-warn">79%</td>
      <td class="col-out">34</td>
    </tr>
  </tbody>
</table>
    </div>
  </div>
  <div class="dept-item">
    <input type="checkbox" id="dept-Сентябрь-3" class="dept-checkbox">
    <label for="dept-Сентябрь-3" class="dept-row">
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
    <col class="col-pct">
    <col class="col-stat">
  </colgroup>
  <thead>
    <tr>
      <th rowspan="2" class="col-num">№</th>
      <th rowspan="2" class="col-fio">ФИО</th>
      <th colspan="2">Входящие</th>
      <th rowspan="2" class="col-pct">Принято, %</th>
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
      <td class="col-pct pct-bad">44%</td>
      <td class="col-out">271</td>
    </tr>
    <tr>
      <td class="col-num">2</td>
      <td class="col-fio">Роганова Анна Анатольевна</td>
      <td class="col-in">318</td>
      <td class="col-miss">224</td>
      <td class="col-pct pct-warn">59%</td>
      <td class="col-out">82</td>
    </tr>
    <tr>
      <td class="col-num">3</td>
      <td class="col-fio">Сапогов Михаил Дмитриевич</td>
      <td class="col-in">171</td>
      <td class="col-miss">69</td>
      <td class="col-pct pct-warn">71%</td>
      <td class="col-out">179</td>
    </tr>
    <tr>
      <td class="col-num">4</td>
      <td class="col-fio">Кошик Владимир Иванович</td>
      <td class="col-in">126</td>
      <td class="col-miss">16</td>
      <td class="col-pct pct-good">89%</td>
      <td class="col-out">135</td>
    </tr>
    <tr>
      <td class="col-num">5</td>
      <td class="col-fio">Худышкин Сергей Николаевич</td>
      <td class="col-in">90</td>
      <td class="col-miss">19</td>
      <td class="col-pct pct-good">83%</td>
      <td class="col-out">97</td>
    </tr>
    <tr>
      <td class="col-num">6</td>
      <td class="col-fio">Мулявин Яков Владиславович</td>
      <td class="col-in">69</td>
      <td class="col-miss">8</td>
      <td class="col-pct pct-good">90%</td>
      <td class="col-out">55</td>
    </tr>
    <tr>
      <td class="col-num">7</td>
      <td class="col-fio">Гасанов Сархан Нураддин</td>
      <td class="col-in">53</td>
      <td class="col-miss">13</td>
      <td class="col-pct pct-good">80%</td>
      <td class="col-out">45</td>
    </tr>
    <tr>
      <td class="col-num">8</td>
      <td class="col-fio">Ставер Андрей Петрович</td>
      <td class="col-in">4</td>
      <td class="col-miss">22</td>
      <td class="col-pct pct-bad">15%</td>
      <td class="col-out">8</td>
    </tr>
    <tr>
      <td class="col-num">9</td>
      <td class="col-fio">Обмолова Валентина Витальевна</td>
      <td class="col-in">0</td>
      <td class="col-miss">24</td>
      <td class="col-pct pct-bad">0%</td>
      <td class="col-out">0</td>
    </tr>
  </tbody>
</table>
    </div>
  </div>
  <div class="dept-item">
    <input type="checkbox" id="dept-Сентябрь-4" class="dept-checkbox">
    <label for="dept-Сентябрь-4" class="dept-row">
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
    <col class="col-pct">
    <col class="col-stat">
  </colgroup>
  <thead>
    <tr>
      <th rowspan="2" class="col-num">№</th>
      <th rowspan="2" class="col-fio">ФИО</th>
      <th colspan="2">Входящие</th>
      <th rowspan="2" class="col-pct">Принято, %</th>
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
      <td class="col-pct pct-warn">64%</td>
      <td class="col-out">379</td>
    </tr>
    <tr>
      <td class="col-num">2</td>
      <td class="col-fio">Чернов Андрей Анатольевич</td>
      <td class="col-in">319</td>
      <td class="col-miss">98</td>
      <td class="col-pct pct-warn">76%</td>
      <td class="col-out">205</td>
    </tr>
    <tr>
      <td class="col-num">3</td>
      <td class="col-fio">Полякова Анна Викторовна</td>
      <td class="col-in">99</td>
      <td class="col-miss">22</td>
      <td class="col-pct pct-good">82%</td>
      <td class="col-out">110</td>
    </tr>
    <tr>
      <td class="col-num">4</td>
      <td class="col-fio">Суханова Ирина Константиновна</td>
      <td class="col-in">9</td>
      <td class="col-miss">12</td>
      <td class="col-pct pct-bad">43%</td>
      <td class="col-out">50</td>
    </tr>
    <tr>
      <td class="col-num">5</td>
      <td class="col-fio">Цветнова Наталья Геннадьевна</td>
      <td class="col-in">2</td>
      <td class="col-miss">4</td>
      <td class="col-pct pct-bad">33%</td>
      <td class="col-out">2</td>
    </tr>
  </tbody>
</table>
    </div>
  </div>
  <div class="dept-item">
    <input type="checkbox" id="dept-Сентябрь-5" class="dept-checkbox">
    <label for="dept-Сентябрь-5" class="dept-row">
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
    <col class="col-pct">
    <col class="col-stat">
  </colgroup>
  <thead>
    <tr>
      <th rowspan="2" class="col-num">№</th>
      <th rowspan="2" class="col-fio">ФИО</th>
      <th colspan="2">Входящие</th>
      <th rowspan="2" class="col-pct">Принято, %</th>
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
      <td class="col-pct pct-good">87%</td>
      <td class="col-out">251</td>
    </tr>
    <tr>
      <td class="col-num">2</td>
      <td class="col-fio">Стрельникова Ольга Сергеевна</td>
      <td class="col-in">184</td>
      <td class="col-miss">37</td>
      <td class="col-pct pct-good">83%</td>
      <td class="col-out">142</td>
    </tr>
    <tr>
      <td class="col-num">3</td>
      <td class="col-fio">Щирская Ксения Васильевна</td>
      <td class="col-in">93</td>
      <td class="col-miss">18</td>
      <td class="col-pct pct-good">84%</td>
      <td class="col-out">207</td>
    </tr>
    <tr>
      <td class="col-num">4</td>
      <td class="col-fio">Зуева Галия Парвасьевна</td>
      <td class="col-in">109</td>
      <td class="col-miss">7</td>
      <td class="col-pct pct-good">94%</td>
      <td class="col-out">160</td>
    </tr>
    <tr>
      <td class="col-num">5</td>
      <td class="col-fio">Петрова Наталья Александровна</td>
      <td class="col-in">100</td>
      <td class="col-miss">7</td>
      <td class="col-pct pct-good">93%</td>
      <td class="col-out">122</td>
    </tr>
    <tr>
      <td class="col-num">6</td>
      <td class="col-fio">Минакова Ольга Фахрутдиновна</td>
      <td class="col-in">82</td>
      <td class="col-miss">12</td>
      <td class="col-pct pct-good">87%</td>
      <td class="col-out">129</td>
    </tr>
    <tr>
      <td class="col-num">7</td>
      <td class="col-fio">Филиппова Олеся Валерьевна</td>
      <td class="col-in">99</td>
      <td class="col-miss">11</td>
      <td class="col-pct pct-good">90%</td>
      <td class="col-out">110</td>
    </tr>
    <tr>
      <td class="col-num">8</td>
      <td class="col-fio">Шибанаева Татьяна Викторовна</td>
      <td class="col-in">99</td>
      <td class="col-miss">7</td>
      <td class="col-pct pct-good">93%</td>
      <td class="col-out">91</td>
    </tr>
    <tr>
      <td class="col-num">9</td>
      <td class="col-fio">Вернер Елена Викторовна</td>
      <td class="col-in">57</td>
      <td class="col-miss">1</td>
      <td class="col-pct pct-good">98%</td>
      <td class="col-out">55</td>
    </tr>
    <tr>
      <td class="col-num">10</td>
      <td class="col-fio">Ильницкая Светлана Викторовна</td>
      <td class="col-in">29</td>
      <td class="col-miss">6</td>
      <td class="col-pct pct-good">83%</td>
      <td class="col-out">26</td>
    </tr>
    <tr>
      <td class="col-num">11</td>
      <td class="col-fio">Бусыгина Ирина Сергеевна</td>
      <td class="col-in">20</td>
      <td class="col-miss">8</td>
      <td class="col-pct pct-warn">71%</td>
      <td class="col-out">32</td>
    </tr>
  </tbody>
</table>
    </div>
  </div>
  <div class="dept-item">
    <input type="checkbox" id="dept-Сентябрь-6" class="dept-checkbox">
    <label for="dept-Сентябрь-6" class="dept-row">
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
    <col class="col-pct">
    <col class="col-stat">
  </colgroup>
  <thead>
    <tr>
      <th rowspan="2" class="col-num">№</th>
      <th rowspan="2" class="col-fio">ФИО</th>
      <th colspan="2">Входящие</th>
      <th rowspan="2" class="col-pct">Принято, %</th>
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
      <td class="col-pct pct-warn">76%</td>
      <td class="col-out">158</td>
    </tr>
    <tr>
      <td class="col-num">2</td>
      <td class="col-fio">Шевелева Ксения Викторовна</td>
      <td class="col-in">111</td>
      <td class="col-miss">21</td>
      <td class="col-pct pct-good">84%</td>
      <td class="col-out">107</td>
    </tr>
    <tr>
      <td class="col-num">3</td>
      <td class="col-fio">Янова Екатерина Анатольевна</td>
      <td class="col-in">55</td>
      <td class="col-miss">7</td>
      <td class="col-pct pct-good">89%</td>
      <td class="col-out">65</td>
    </tr>
    <tr>
      <td class="col-num">4</td>
      <td class="col-fio">Лейпожих Алёна Алексеевна</td>
      <td class="col-in">24</td>
      <td class="col-miss">12</td>
      <td class="col-pct pct-warn">67%</td>
      <td class="col-out">21</td>
    </tr>
    <tr>
      <td class="col-num">5</td>
      <td class="col-fio">Чистякова Елена Дмитриевна</td>
      <td class="col-in">16</td>
      <td class="col-miss">6</td>
      <td class="col-pct pct-warn">73%</td>
      <td class="col-out">20</td>
    </tr>
    <tr>
      <td class="col-num">6</td>
      <td class="col-fio">Яковлева Вилена Фаильевна</td>
      <td class="col-in">18</td>
      <td class="col-miss">3</td>
      <td class="col-pct pct-good">86%</td>
      <td class="col-out">14</td>
    </tr>
    <tr>
      <td class="col-num">7</td>
      <td class="col-fio">Павлова Надежда Григорьевна</td>
      <td class="col-in">14</td>
      <td class="col-miss">2</td>
      <td class="col-pct pct-good">88%</td>
      <td class="col-out">17</td>
    </tr>
    <tr>
      <td class="col-num">8</td>
      <td class="col-fio">Ребась Кристина Владимировна</td>
      <td class="col-in">4</td>
      <td class="col-miss">0</td>
      <td class="col-pct pct-good">100%</td>
      <td class="col-out">9</td>
    </tr>
  </tbody>
</table>
    </div>
  </div>
  <div class="dept-item">
    <input type="checkbox" id="dept-Сентябрь-7" class="dept-checkbox">
    <label for="dept-Сентябрь-7" class="dept-row">
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
    <col class="col-pct">
    <col class="col-stat">
  </colgroup>
  <thead>
    <tr>
      <th rowspan="2" class="col-num">№</th>
      <th rowspan="2" class="col-fio">ФИО</th>
      <th colspan="2">Входящие</th>
      <th rowspan="2" class="col-pct">Принято, %</th>
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
      <td class="col-pct pct-warn">69%</td>
      <td class="col-out">174</td>
    </tr>
    <tr>
      <td class="col-num">2</td>
      <td class="col-fio">Жукова Анастасия Сергеевна</td>
      <td class="col-in">152</td>
      <td class="col-miss">24</td>
      <td class="col-pct pct-good">86%</td>
      <td class="col-out">138</td>
    </tr>
    <tr>
      <td class="col-num">3</td>
      <td class="col-fio">Лаба Вера Алексеевна</td>
      <td class="col-in">112</td>
      <td class="col-miss">26</td>
      <td class="col-pct pct-good">81%</td>
      <td class="col-out">117</td>
    </tr>
    <tr>
      <td class="col-num">4</td>
      <td class="col-fio">Каргаполова Алёна Андреевна</td>
      <td class="col-in">100</td>
      <td class="col-miss">20</td>
      <td class="col-pct pct-good">83%</td>
      <td class="col-out">97</td>
    </tr>
    <tr>
      <td class="col-num">5</td>
      <td class="col-fio">Юшкевич Татьяна Владимировна</td>
      <td class="col-in">89</td>
      <td class="col-miss">5</td>
      <td class="col-pct pct-good">95%</td>
      <td class="col-out">87</td>
    </tr>
    <tr>
      <td class="col-num">6</td>
      <td class="col-fio">Занина Ирина Александровна</td>
      <td class="col-in">81</td>
      <td class="col-miss">13</td>
      <td class="col-pct pct-good">86%</td>
      <td class="col-out">71</td>
    </tr>
    <tr>
      <td class="col-num">7</td>
      <td class="col-fio">Леванских Людмила Владимировна</td>
      <td class="col-in">77</td>
      <td class="col-miss">6</td>
      <td class="col-pct pct-good">93%</td>
      <td class="col-out">65</td>
    </tr>
    <tr>
      <td class="col-num">8</td>
      <td class="col-fio">Кропотов Иван Александрович</td>
      <td class="col-in">68</td>
      <td class="col-miss">3</td>
      <td class="col-pct pct-good">96%</td>
      <td class="col-out">47</td>
    </tr>
    <tr>
      <td class="col-num">9</td>
      <td class="col-fio">Фаузер Татьяна Леовна</td>
      <td class="col-in">76</td>
      <td class="col-miss">4</td>
      <td class="col-pct pct-good">95%</td>
      <td class="col-out">13</td>
    </tr>
    <tr>
      <td class="col-num">10</td>
      <td class="col-fio">Семенова Наталья Викторовна</td>
      <td class="col-in">50</td>
      <td class="col-miss">1</td>
      <td class="col-pct pct-good">98%</td>
      <td class="col-out">35</td>
    </tr>
    <tr>
      <td class="col-num">11</td>
      <td class="col-fio">Мицура Ираида Илдаровна</td>
      <td class="col-in">30</td>
      <td class="col-miss">4</td>
      <td class="col-pct pct-good">88%</td>
      <td class="col-out">31</td>
    </tr>
  </tbody>
</table>
    </div>
  </div>
  <div class="dept-item">
    <input type="checkbox" id="dept-Сентябрь-8" class="dept-checkbox">
    <label for="dept-Сентябрь-8" class="dept-row">
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
    <col class="col-pct">
    <col class="col-stat">
  </colgroup>
  <thead>
    <tr>
      <th rowspan="2" class="col-num">№</th>
      <th rowspan="2" class="col-fio">ФИО</th>
      <th colspan="2">Входящие</th>
      <th rowspan="2" class="col-pct">Принято, %</th>
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
      <td class="col-pct pct-warn">75%</td>
      <td class="col-out">423</td>
    </tr>
    <tr>
      <td class="col-num">2</td>
      <td class="col-fio">Ильдеркина Ирина Николаевна</td>
      <td class="col-in">272</td>
      <td class="col-miss">77</td>
      <td class="col-pct pct-warn">78%</td>
      <td class="col-out">269</td>
    </tr>
    <tr>
      <td class="col-num">3</td>
      <td class="col-fio">Павлова Ирина Игоревна</td>
      <td class="col-in">274</td>
      <td class="col-miss">80</td>
      <td class="col-pct pct-warn">77%</td>
      <td class="col-out">187</td>
    </tr>
    <tr>
      <td class="col-num">4</td>
      <td class="col-fio">Конева Елена Ивановна</td>
      <td class="col-in">196</td>
      <td class="col-miss">45</td>
      <td class="col-pct pct-good">81%</td>
      <td class="col-out">281</td>
    </tr>
    <tr>
      <td class="col-num">5</td>
      <td class="col-fio">Мунарева Виктория Игоревна</td>
      <td class="col-in">131</td>
      <td class="col-miss">20</td>
      <td class="col-pct pct-good">87%</td>
      <td class="col-out">353</td>
    </tr>
    <tr>
      <td class="col-num">6</td>
      <td class="col-fio">Алыкова Татьяна Валерьевна</td>
      <td class="col-in">173</td>
      <td class="col-miss">35</td>
      <td class="col-pct pct-good">83%</td>
      <td class="col-out">212</td>
    </tr>
    <tr>
      <td class="col-num">7</td>
      <td class="col-fio">Казанцева Лариса Анатольевна</td>
      <td class="col-in">151</td>
      <td class="col-miss">53</td>
      <td class="col-pct pct-warn">74%</td>
      <td class="col-out">208</td>
    </tr>
    <tr>
      <td class="col-num">8</td>
      <td class="col-fio">Букреева Елена Николаевна</td>
      <td class="col-in">197</td>
      <td class="col-miss">67</td>
      <td class="col-pct pct-warn">75%</td>
      <td class="col-out">124</td>
    </tr>
    <tr>
      <td class="col-num">9</td>
      <td class="col-fio">Сафаралеева Елена Хайрулловна</td>
      <td class="col-in">140</td>
      <td class="col-miss">45</td>
      <td class="col-pct pct-warn">76%</td>
      <td class="col-out">129</td>
    </tr>
    <tr>
      <td class="col-num">10</td>
      <td class="col-fio">Россолова Екатерина Сергеевна</td>
      <td class="col-in">152</td>
      <td class="col-miss">24</td>
      <td class="col-pct pct-good">86%</td>
      <td class="col-out">89</td>
    </tr>
    <tr>
      <td class="col-num">11</td>
      <td class="col-fio">Злобина Мария Александровна</td>
      <td class="col-in">100</td>
      <td class="col-miss">20</td>
      <td class="col-pct pct-good">83%</td>
      <td class="col-out">144</td>
    </tr>
    <tr>
      <td class="col-num">12</td>
      <td class="col-fio">Шахова Галина Максимовна</td>
      <td class="col-in">75</td>
      <td class="col-miss">35</td>
      <td class="col-pct pct-warn">68%</td>
      <td class="col-out">91</td>
    </tr>
    <tr>
      <td class="col-num">13</td>
      <td class="col-fio">Манджиева Алевтина Алексеевна</td>
      <td class="col-in">66</td>
      <td class="col-miss">17</td>
      <td class="col-pct pct-warn">80%</td>
      <td class="col-out">102</td>
    </tr>
    <tr>
      <td class="col-num">14</td>
      <td class="col-fio">Ершова Алла Николаевна</td>
      <td class="col-in">103</td>
      <td class="col-miss">15</td>
      <td class="col-pct pct-good">87%</td>
      <td class="col-out">64</td>
    </tr>
    <tr>
      <td class="col-num">15</td>
      <td class="col-fio">Лазарева Екатерина Николаевна</td>
      <td class="col-in">32</td>
      <td class="col-miss">8</td>
      <td class="col-pct pct-good">80%</td>
      <td class="col-out">24</td>
    </tr>
    <tr>
      <td class="col-num">16</td>
      <td class="col-fio">Русмиленко Инга Юрьевна</td>
      <td class="col-in">41</td>
      <td class="col-miss">8</td>
      <td class="col-pct pct-good">84%</td>
      <td class="col-out">12</td>
    </tr>
  </tbody>
</table>
    </div>
  </div>
  <div class="dept-item">
    <input type="checkbox" id="dept-Сентябрь-9" class="dept-checkbox">
    <label for="dept-Сентябрь-9" class="dept-row">
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
    <col class="col-pct">
    <col class="col-stat">
  </colgroup>
  <thead>
    <tr>
      <th rowspan="2" class="col-num">№</th>
      <th rowspan="2" class="col-fio">ФИО</th>
      <th colspan="2">Входящие</th>
      <th rowspan="2" class="col-pct">Принято, %</th>
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
      <td class="col-pct pct-warn">60%</td>
      <td class="col-out">194</td>
    </tr>
    <tr>
      <td class="col-num">2</td>
      <td class="col-fio">Кузнецова Надежда Александровна</td>
      <td class="col-in">103</td>
      <td class="col-miss">17</td>
      <td class="col-pct pct-good">86%</td>
      <td class="col-out">67</td>
    </tr>
    <tr>
      <td class="col-num">3</td>
      <td class="col-fio">Обломкина Лариса Ивановна</td>
      <td class="col-in">80</td>
      <td class="col-miss">14</td>
      <td class="col-pct pct-good">85%</td>
      <td class="col-out">87</td>
    </tr>
    <tr>
      <td class="col-num">4</td>
      <td class="col-fio">Нурлубаева Алина Залимхановна</td>
      <td class="col-in">119</td>
      <td class="col-miss">21</td>
      <td class="col-pct pct-good">85%</td>
      <td class="col-out">39</td>
    </tr>
    <tr>
      <td class="col-num">5</td>
      <td class="col-fio">Дмитриенко Татьяна Валерьевна</td>
      <td class="col-in">105</td>
      <td class="col-miss">10</td>
      <td class="col-pct pct-good">91%</td>
      <td class="col-out">64</td>
    </tr>
    <tr>
      <td class="col-num">6</td>
      <td class="col-fio">Мухамадеева Танзиля Рафкатовна</td>
      <td class="col-in">88</td>
      <td class="col-miss">13</td>
      <td class="col-pct pct-good">87%</td>
      <td class="col-out">74</td>
    </tr>
    <tr>
      <td class="col-num">7</td>
      <td class="col-fio">Карташова Мария Александровна</td>
      <td class="col-in">63</td>
      <td class="col-miss">15</td>
      <td class="col-pct pct-good">81%</td>
      <td class="col-out">81</td>
    </tr>
    <tr>
      <td class="col-num">8</td>
      <td class="col-fio">Горохова Алёна Павловна</td>
      <td class="col-in">69</td>
      <td class="col-miss">18</td>
      <td class="col-pct pct-warn">79%</td>
      <td class="col-out">51</td>
    </tr>
    <tr>
      <td class="col-num">9</td>
      <td class="col-fio">Кундаль Нина Валерьевна</td>
      <td class="col-in">70</td>
      <td class="col-miss">11</td>
      <td class="col-pct pct-good">86%</td>
      <td class="col-out">48</td>
    </tr>
    <tr>
      <td class="col-num">10</td>
      <td class="col-fio">Якута Светлана Михайловна</td>
      <td class="col-in">35</td>
      <td class="col-miss">18</td>
      <td class="col-pct pct-warn">66%</td>
      <td class="col-out">41</td>
    </tr>
    <tr>
      <td class="col-num">11</td>
      <td class="col-fio">Иванова Любовь Васильевна</td>
      <td class="col-in">0</td>
      <td class="col-miss">2</td>
      <td class="col-pct pct-bad">0%</td>
      <td class="col-out">0</td>
    </tr>
  </tbody>
</table>
    </div>
  </div>
</div>

### Нагрузка отделов

<div class="calls-source">Сводные показатели по подразделениям. «Доля пропущенных» — процент входящих вызовов, не завершившихся разговором. «Индекс исх./вх.» — отношение исходящих к сумме входящих (>1 — отдел больше инициирует, <1 — больше принимает).</div>

<div class="load-chart">
<div class="load-chart-row">
  <div class="load-chart-name" title="Отдел расчётов с персоналом">Отдел расчётов с персоналом</div>
  <div class="load-chart-bar-wrap">
    <div class="load-chart-bar" style="width: 100.00%;">
      <div class="load-chart-seg seg-in" style="width: 41.21%;" title="Принятые: 2343"></div>
      <div class="load-chart-seg seg-miss" style="width: 11.08%;" title="Пропущенные: 630"></div>
      <div class="load-chart-seg seg-out" style="width: 47.70%;" title="Исходящие: 2712"></div>
    </div>
  </div>
  <div class="load-chart-value">5685</div>
</div>
<div class="load-chart-row">
  <div class="load-chart-name" title="Администрация">Администрация</div>
  <div class="load-chart-bar-wrap">
    <div class="load-chart-bar" style="width: 52.24%;">
      <div class="load-chart-seg seg-in" style="width: 40.17%;" title="Принятые: 1193"></div>
      <div class="load-chart-seg seg-miss" style="width: 20.37%;" title="Пропущенные: 605"></div>
      <div class="load-chart-seg seg-out" style="width: 39.46%;" title="Исходящие: 1172"></div>
    </div>
  </div>
  <div class="load-chart-value">2970</div>
</div>
<div class="load-chart-row">
  <div class="load-chart-name" title="Отдел СР и ТП">Отдел СР и ТП</div>
  <div class="load-chart-bar-wrap">
    <div class="load-chart-bar" style="width: 47.32%;">
      <div class="load-chart-seg seg-in" style="width: 40.56%;" title="Принятые: 1091"></div>
      <div class="load-chart-seg seg-miss" style="width: 27.03%;" title="Пропущенные: 727"></div>
      <div class="load-chart-seg seg-out" style="width: 32.42%;" title="Исходящие: 872"></div>
    </div>
  </div>
  <div class="load-chart-value">2690</div>
</div>
<div class="load-chart-row">
  <div class="load-chart-name" title="Отдел учета основных средств и запасов">Отдел учета основных средств и запасов</div>
  <div class="load-chart-bar-wrap">
    <div class="load-chart-bar" style="width: 45.00%;">
      <div class="load-chart-seg seg-in" style="width: 42.49%;" title="Принятые: 1087"></div>
      <div class="load-chart-seg seg-miss" style="width: 5.71%;" title="Пропущенные: 146"></div>
      <div class="load-chart-seg seg-out" style="width: 51.80%;" title="Исходящие: 1325"></div>
    </div>
  </div>
  <div class="load-chart-value">2558</div>
</div>
<div class="load-chart-row">
  <div class="load-chart-name" title="Отдел учета доходов">Отдел учета доходов</div>
  <div class="load-chart-bar-wrap">
    <div class="load-chart-bar" style="width: 35.76%;">
      <div class="load-chart-seg seg-in" style="width: 48.40%;" title="Принятые: 984"></div>
      <div class="load-chart-seg seg-miss" style="width: 8.56%;" title="Пропущенные: 174"></div>
      <div class="load-chart-seg seg-out" style="width: 43.04%;" title="Исходящие: 875"></div>
    </div>
  </div>
  <div class="load-chart-value">2033</div>
</div>
<div class="load-chart-row">
  <div class="load-chart-name" title="Отдел расчётов с поставщиками, подрядчиками">Отдел расчётов с поставщиками, подрядчиками</div>
  <div class="load-chart-bar-wrap">
    <div class="load-chart-bar" style="width: 33.44%;">
      <div class="load-chart-seg seg-in" style="width: 47.50%;" title="Принятые: 903"></div>
      <div class="load-chart-seg seg-miss" style="width: 13.26%;" title="Пропущенные: 252"></div>
      <div class="load-chart-seg seg-out" style="width: 39.24%;" title="Исходящие: 746"></div>
    </div>
  </div>
  <div class="load-chart-value">1901</div>
</div>
<div class="load-chart-row">
  <div class="load-chart-name" title="Отдел кадрового и правового обеспечения">Отдел кадрового и правового обеспечения</div>
  <div class="load-chart-bar-wrap">
    <div class="load-chart-bar" style="width: 28.44%;">
      <div class="load-chart-seg seg-in" style="width: 38.65%;" title="Принятые: 625"></div>
      <div class="load-chart-seg seg-miss" style="width: 15.21%;" title="Пропущенные: 246"></div>
      <div class="load-chart-seg seg-out" style="width: 46.13%;" title="Исходящие: 746"></div>
    </div>
  </div>
  <div class="load-chart-value">1617</div>
</div>
<div class="load-chart-row">
  <div class="load-chart-name" title="Отдел подготовки отчетности">Отдел подготовки отчетности</div>
  <div class="load-chart-bar-wrap">
    <div class="load-chart-bar" style="width: 14.99%;">
      <div class="load-chart-seg seg-in" style="width: 41.67%;" title="Принятые: 355"></div>
      <div class="load-chart-seg seg-miss" style="width: 10.09%;" title="Пропущенные: 86"></div>
      <div class="load-chart-seg seg-out" style="width: 48.24%;" title="Исходящие: 411"></div>
    </div>
  </div>
  <div class="load-chart-value">852</div>
</div>
<div class="load-chart-row">
  <div class="load-chart-name" title="Отдел информационной безопасности">Отдел информационной безопасности</div>
  <div class="load-chart-bar-wrap">
    <div class="load-chart-bar" style="width: 13.21%;">
      <div class="load-chart-seg seg-in" style="width: 51.26%;" title="Принятые: 385"></div>
      <div class="load-chart-seg seg-miss" style="width: 15.05%;" title="Пропущенные: 113"></div>
      <div class="load-chart-seg seg-out" style="width: 33.69%;" title="Исходящие: 253"></div>
    </div>
  </div>
  <div class="load-chart-value">751</div>
</div>
  <div class="load-chart-legend">
    <span class="load-chart-legend-item"><span class="load-chart-legend-dot legend-in"></span>принятые</span>
    <span class="load-chart-legend-item"><span class="load-chart-legend-dot legend-miss"></span>пропущенные</span>
    <span class="load-chart-legend-item"><span class="load-chart-legend-dot legend-out"></span>исходящие</span>
  </div>
</div>

<div class="facts-grid">
<div class="fact-card fact-out">
  <div class="fact-label">Наибольшее число исходящих</div>
  <div class="fact-value">Отдел расчётов с персоналом</div>
  <div class="fact-sub">2712 исходящих звонков</div>
</div>
<div class="fact-card fact-in">
  <div class="fact-label">Наибольшее число принятых</div>
  <div class="fact-value">Отдел расчётов с персоналом</div>
  <div class="fact-sub">2343 принятых звонков</div>
</div>
<div class="fact-card fact-miss">
  <div class="fact-label">Наибольшая доля пропущенных</div>
  <div class="fact-value">Отдел СР и ТП</div>
  <div class="fact-sub">727 из 1818 входящих · 40.0%</div>
</div>
<div class="fact-card fact-in">
  <div class="fact-label">Наилучший приём вызовов</div>
  <div class="fact-value">Отдел учета основных средств и запасов</div>
  <div class="fact-sub">1087 из 1233 входящих · принято 88.2%</div>
</div>
<div class="fact-card fact-out">
  <div class="fact-label">Преобладание исходящих связей</div>
  <div class="fact-value">Отдел учета основных средств и запасов</div>
  <div class="fact-sub">Индекс исх./вх. = 1.07 — отдел больше инициирует, чем принимает</div>
</div>
<div class="fact-card fact-in">
  <div class="fact-label">Преобладание входящих связей</div>
  <div class="fact-value">Отдел СР и ТП</div>
  <div class="fact-sub">Индекс исх./вх. = 0.48 — отдел больше принимает, чем инициирует</div>
</div>
<div class="fact-card fact-hour">
  <div class="fact-label">Средняя нагрузка на сотрудника</div>
  <div class="fact-value">263 звонков / мес.</div>
  <div class="fact-sub">Всего: 21057 звонков, 80 сотрудников</div>
</div>
<div class="fact-card fact-pair">
  <div class="fact-label">Наибольший суммарный объём</div>
  <div class="fact-value">Отдел расчётов с персоналом</div>
  <div class="fact-sub">5685 звонков всех типов</div>
</div>
</div>

### Нагрузка сотрудников

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

---
