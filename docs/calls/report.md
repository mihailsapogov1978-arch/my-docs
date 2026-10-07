
<style>
:root {
    --emp-border: #e2e8f0;
    --emp-bg-hover: #f7fafc;
    --emp-text: #2d3748;
    --emp-muted: #718096;
    --emp-accent: #2b6cb0;
    --emp-accent-light: #ebf8ff;
    --emp-accent-border: #bee3f8;
}

.cat-list {
    margin: 16px 0;
    border: 1px solid var(--emp-border);
    border-radius: 10px;
    overflow: hidden;
    background: #fff;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}

.cat-row,
.cat-sub-item {
    display: grid;
    grid-template-columns: 32px minmax(0, 1fr) 150px 20px;
    align-items: center;
    column-gap: 12px;
    padding: 12px 16px;
    border-bottom: 1px solid var(--emp-border);
    font-size: 14px;
    line-height: 1.4;
    margin: 0;
}

.cat-row:last-child { border-bottom: none; }

.cat-row.has-sub {
    cursor: pointer;
    transition: background 0.15s;
}
.cat-row.has-sub:hover { background: var(--emp-bg-hover); }

.cat-num {
    font-weight: 700;
    color: var(--emp-muted);
    text-align: right;
}

.cat-name {
    font-weight: 600;
    color: var(--emp-text);
    min-width: 0;
}

.cat-count {
    font-weight: 700;
    color: var(--emp-accent);
    white-space: nowrap;
    text-align: right;
}
.cat-count span {
    font-weight: 400;
    color: var(--emp-muted);
    font-size: 12px;
    margin-left: 4px;
}

.cat-toggle {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    color: var(--emp-accent);
    font-size: 16px;
    font-weight: 700;
    transition: transform 0.15s;
    user-select: none;
}
.cat-row.has-sub.open .cat-toggle {
    transform: rotate(90deg);
}

.cat-checkbox {
    display: none;
}

.cat-details {
    display: none;
    background: #fafbfc;
    border-bottom: 1px solid var(--emp-border);
    padding: 0;
}
.cat-checkbox:checked ~ .cat-details {
    display: block;
}
.cat-checkbox:checked ~ .cat-row .cat-toggle {
    transform: rotate(90deg);
}

.cat-sub-list {
    margin: 0;
    padding: 0;
    list-style: none;
    background: #fafbfc;
}

.cat-sub-item {
    padding-left: 28px;
    padding-right: 16px;
    font-size: 13.5px;
    border-bottom: 1px dashed var(--emp-border);
}
.cat-sub-item:last-child { border-bottom: 1px solid var(--emp-border); }

.cat-sub-name {
    color: var(--emp-text);
    font-style: italic;
    min-width: 0;
    grid-column: 2;
}

.cat-sub-count {
    font-weight: 600;
    color: var(--emp-accent);
    white-space: nowrap;
    text-align: right;
    grid-column: 3;
}
.cat-sub-count span {
    font-weight: 400;
    color: var(--emp-muted);
    font-size: 12px;
    margin-left: 4px;
}

.cat-sub-empty {
    grid-column: 4;
}

.cat-total {
    display: grid;
    grid-template-columns: 1fr 150px;
    align-items: center;
    column-gap: 12px;
    background: var(--emp-accent-light);
    border: 1px solid var(--emp-accent-border);
    border-radius: 8px;
    padding: 14px 20px;
    margin: 10px 0 16px 0;
    font-size: 14px;
    color: var(--emp-accent);
    font-weight: 600;
}
.cat-total-value { text-align: right; font-size: 16px; }

@media (max-width: 700px) {
    .cat-row,
    .cat-sub-item {
        grid-template-columns: 28px minmax(0, 1fr) 20px;
        row-gap: 4px;
    }
    .cat-count,
    .cat-sub-count {
        grid-column: 2;
        text-align: left;
    }
    .cat-toggle { grid-row: 1; grid-column: 3; }
    .cat-sub-empty { display: none; }
    .cat-sub-item { padding-left: 16px; }
    .cat-total { grid-template-columns: 1fr; row-gap: 6px; }
    .cat-total-value { text-align: left; }
}
</style>


# Анализ заявок за 2026 год по направлениям

---

<div class="cat-total">
  <span class="cat-total-label">Всего заявок за 2026 год</span>
  <span class="cat-total-value">44994</span>
</div>

<div class="cat-list">
  <div class="cat-row">
    <span class="cat-num">1</span>
    <span class="cat-name">Технические проблемы (запуск, обновления, права доступа, зависания, ЭП)</span>
    <span class="cat-count">8095<span>/ 17.99%</span></span>
    <span></span>
  </div>
  <input type="checkbox" id="cat-2" class="cat-checkbox">
  <label for="cat-2" class="cat-row has-sub">
    <span class="cat-num">2</span>
    <span class="cat-name">Кадровый учет (ГИС ТК, СЗВ-ТД, больничные, отпуска, ГИС КУ, ГИС ЕСКУ)</span>
    <span class="cat-count">4743<span>/ 10.54%</span></span>
    <span class="cat-toggle">›</span>
  </label>
  <div class="cat-details">
    <ul class="cat-sub-list">
      <li class="cat-sub-item">
        <span></span>
        <span class="cat-sub-name">Из них ГИС ЕСКУ</span>
        <span class="cat-sub-count">362<span>/ 0.80%</span></span>
        <span class="cat-sub-empty"></span>
      </li>
    </ul>
  </div>
  <input type="checkbox" id="cat-3" class="cat-checkbox">
  <label for="cat-3" class="cat-row has-sub">
    <span class="cat-num">3</span>
    <span class="cat-name">Формирование регламентированной отчетности (в ФНС, СФР, Росстат, Астрал)</span>
    <span class="cat-count">4459<span>/ 9.91%</span></span>
    <span class="cat-toggle">›</span>
  </label>
  <div class="cat-details">
    <ul class="cat-sub-list">
      <li class="cat-sub-item">
        <span></span>
        <span class="cat-sub-name">Из них по Астралу</span>
        <span class="cat-sub-count">6<span>/ 0.01%</span></span>
        <span class="cat-sub-empty"></span>
      </li>
    </ul>
  </div>
  <div class="cat-row">
    <span class="cat-num">4</span>
    <span class="cat-name">Бухгалтерский учет и налогообложение (операции, зарплата, налоги, закрытие периода и т.д.)</span>
    <span class="cat-count">4248<span>/ 9.44%</span></span>
    <span></span>
  </div>
  <div class="cat-row">
    <span class="cat-num">5</span>
    <span class="cat-name">Некорректное состояние справочников и классификаторов (задвоение ИНН/КПП, отсутствие аналитики, ошибки в иерархии)</span>
    <span class="cat-count">3689<span>/ 8.20%</span></span>
    <span></span>
  </div>
  <input type="checkbox" id="cat-6" class="cat-checkbox">
  <label for="cat-6" class="cat-row has-sub">
    <span class="cat-num">6</span>
    <span class="cat-name">Взаимодействие с внешними системами (РКС, ЕИС, ГИС Имущество, банки и прочие)</span>
    <span class="cat-count">2526<span>/ 5.61%</span></span>
    <span class="cat-toggle">›</span>
  </label>
  <div class="cat-details">
    <ul class="cat-sub-list">
      <li class="cat-sub-item">
        <span></span>
        <span class="cat-sub-name">ГИС "Имущество"</span>
        <span class="cat-sub-count">213<span>/ 0.47%</span></span>
        <span class="cat-sub-empty"></span>
      </li>
      <li class="cat-sub-item">
        <span></span>
        <span class="cat-sub-name">РКС (ЕИС)</span>
        <span class="cat-sub-count">431<span>/ 0.96%</span></span>
        <span class="cat-sub-empty"></span>
      </li>
      <li class="cat-sub-item">
        <span></span>
        <span class="cat-sub-name">ГИС "ГМП" (УНП)</span>
        <span class="cat-sub-count">448<span>/ 1.00%</span></span>
        <span class="cat-sub-empty"></span>
      </li>
      <li class="cat-sub-item">
        <span></span>
        <span class="cat-sub-name">ГИС "АПК"</span>
        <span class="cat-sub-count">23<span>/ 0.05%</span></span>
        <span class="cat-sub-empty"></span>
      </li>
      <li class="cat-sub-item">
        <span></span>
        <span class="cat-sub-name">ГИС "Web-Исполнение"</span>
        <span class="cat-sub-count">86<span>/ 0.19%</span></span>
        <span class="cat-sub-empty"></span>
      </li>
      <li class="cat-sub-item">
        <span></span>
        <span class="cat-sub-name">ГИС "Web-Консолидация"</span>
        <span class="cat-sub-count">34<span>/ 0.08%</span></span>
        <span class="cat-sub-empty"></span>
      </li>
    </ul>
  </div>
  <div class="cat-row">
    <span class="cat-num">7</span>
    <span class="cat-name">Консультации и разъяснения порядка работы (вопросы «как сделать», «где найти», «подскажите»)</span>
    <span class="cat-count">2161<span>/ 4.80%</span></span>
    <span></span>
  </div>
  <div class="cat-row">
    <span class="cat-num">8</span>
    <span class="cat-name">Личный кабинет подотчетного лица (ЛК ПОЛ)</span>
    <span class="cat-count">1954<span>/ 4.34%</span></span>
    <span></span>
  </div>
  <div class="cat-row">
    <span class="cat-num">9</span>
    <span class="cat-name">Ошибки и сбои при работе в системе (прочие)</span>
    <span class="cat-count">1701<span>/ 3.78%</span></span>
    <span></span>
  </div>
  <div class="cat-row">
    <span class="cat-num">10</span>
    <span class="cat-name">Дополнительный функционал и сервисы (аналитика, планирование, API)</span>
    <span class="cat-count">450<span>/ 1.00%</span></span>
    <span></span>
  </div>
  <div class="cat-row">
    <span class="cat-num">11</span>
    <span class="cat-name">Иные (не классифицировано)</span>
    <span class="cat-count">10968<span>/ 24.38%</span></span>
    <span></span>
  </div>
</div>
