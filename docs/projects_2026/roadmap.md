# План проектов на 2026 год

<style>
/* ===== КОМПАКТНАЯ ТАБЛИЦА РУКОВОДИТЕЛЯ ===== */
.boss-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 12px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
    background: #fff;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    border-radius: 10px;
    overflow: hidden;
    table-layout: fixed;
    margin-top: 20px;
}
.boss-table th {
    background: #f5f7fa;
    color: #2c3e50;
    font-weight: 600;
    text-align: left;
    padding: 8px 10px;
    border-bottom: 1px solid #e0e4e8;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.03em;
}
.boss-table td {
    padding: 6px 8px;
    border-bottom: 1px solid #eef2f6;
    vertical-align: middle;
    font-size: 12px;
}
.boss-table tr:last-child td { border-bottom: none; }
.boss-table tr:hover td { background: #fafbfc; }

/* ===== SELECT / INPUT ===== */
.boss-select,
.boss-input {
    width: 100%;
    box-sizing: border-box;
    font-size: 11px;
    font-family: inherit;
    padding: 3px 4px;
    border: 1px solid #cfd6dd;
    border-radius: 6px;
    background: #fff;
    color: #2c3e50;
    cursor: pointer;
    outline: none !important;
    box-shadow: none !important;
}
.boss-select:focus,
.boss-select:focus-visible,
.boss-input:focus,
.boss-input:focus-visible {
    outline: none !important;
    box-shadow: 0 0 0 2px rgba(49,130,206,0.25) !important;
    border-color: #3182ce;
}

/* ===== ЦВЕТА СТАТУСОВ ===== */
select.status-select.status-soglasovanie { background: #bde0fe; }
select.status-select.status-torgi         { background: #f8c8d4; }
select.status-select.status-raboty        { background: #f0e085; }
select.status-select.status-done          { background: #90ee90; }

/* ===== РАСКРЫВАЮЩИЙСЯ БЛОК ДЕТАЛИЗАЦИИ ===== */
details.details-block {
    margin-top: 40px;
    border: 1px solid #e0e4e8;
    border-radius: 10px;
    padding: 12px 18px;
    background: #fafbfc;
}
details.details-block > summary {
    cursor: pointer;
    font-size: 15px;
    font-weight: 600;
    color: #2c3e50;
    outline: none;
    list-style: none;
    padding: 4px 0;
}
details.details-block > summary::-webkit-details-marker { display: none; }
details.details-block > summary::before { content: "▸ "; color: #3182ce; }
details.details-block[open] > summary::before { content: "▾ "; }

/* ===== ДЕТАЛЬНАЯ ТАБЛИЦА ===== */
.status-done { background-color: #90ee90 !important; }
.status-work { background-color: #f0e085 !important; }
.status-wait { background-color: #ffffff !important; }

.project-table {
    border-collapse: collapse;
    width: 100%;
    font-size: 11px;
    line-height: 1.2;
    table-layout: fixed;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
    background: #fff;
    margin-top: 12px;
}
.project-table th {
    background-color: #f5f7fa;
    color: #2c3e50;
    padding: 4px 2px;
    font-weight: 500;
    text-align: center;
    border: 1px solid #e0e4e8;
    vertical-align: middle;
    word-wrap: break-word;
}
.project-table th:nth-child(1),
.project-table th:nth-child(2) {
    writing-mode: horizontal-tb;
    font-size: 14px;
    height: 36px;
    white-space: normal;
}
.project-table th:nth-child(3),
.project-table th:nth-child(4),
.project-table th:nth-child(5),
.project-table th:nth-child(6),
.project-table th:nth-child(7) {
    writing-mode: vertical-rl;
    text-orientation: mixed;
    transform: rotate(180deg);
    font-size: 12px;
    height: 140px;
    white-space: normal;
    word-break: break-word;
    line-height: 1.1;
    padding: 6px 2px;
}
.project-table td {
    padding: 6px 3px;
    border: 1px solid #e0e4e8;
    vertical-align: middle;
    height: 40px;
    word-wrap: break-word;
    background-color: #ffffff;
}
.project-table th:nth-child(1) { width: 38px; }
.project-table td:nth-child(1) { width: 28px; text-align: center; font-weight: 500; font-size: 11px; }
.project-table th:nth-child(2) { width: 200px; }
.project-table td:nth-child(2) { width: 250px; padding-left: 8px; white-space: normal; font-size: 12px; }
.project-table th:nth-child(n+3) { width: 48px; }
.project-table td:nth-child(n+3) { width: 48px; text-align: center; font-size: 11px; }
</style>

<!-- ==================== КОМПАКТНАЯ ТАБЛИЦА ==================== -->
<table class="boss-table" id="bossTable">
    <thead>
        <tr>
            <th style="width:32px;">№</th>
            <th>Мероприятие</th>
            <th style="width:130px;">Срок реализации</th>
            <th style="width:180px;">Статус</th>
        </tr>
    </thead>
    <tbody>
        <tr data-key="1" data-status="torgi" data-deadline="2026-04-20">
            <td>1</td>
            <td>Интеграция с Тэзис</td>
            <td><input type="date" class="boss-input" data-field="deadline" value="2026-04-20"></td>
            <td>
                <select class="boss-select status-select status-torgi" data-field="status">
                    <option value="soglasovanie">Согласование ТЗ</option>
                    <option value="torgi" selected>Торги</option>
                    <option value="raboty">Работы по ГК</option>
                    <option value="done">Выполнено</option>
                </select>
            </td>
        </tr>

        <tr data-key="2" data-status="torgi" data-deadline="2026-04-15">
            <td>2</td>
            <td>Интеграция ЛК/Сметы с сервисом по предоставлению справок</td>
            <td><input type="date" class="boss-input" data-field="deadline" value="2026-04-15"></td>
            <td>
                <select class="boss-select status-select status-torgi" data-field="status">
                    <option value="soglasovanie">Согласование ТЗ</option>
                    <option value="torgi" selected>Торги</option>
                    <option value="raboty">Работы по ГК</option>
                    <option value="done">Выполнено</option>
                </select>
            </td>
        </tr>

        <tr data-key="3" data-status="soglasovanie" data-deadline="2026-05-05">
            <td>3</td>
            <td>Интеграция имущества</td>
            <td><input type="date" class="boss-input" data-field="deadline" value="2026-05-05"></td>
            <td>
                <select class="boss-select status-select status-soglasovanie" data-field="status">
                    <option value="soglasovanie" selected>Согласование ТЗ</option>
                    <option value="torgi">Торги</option>
                    <option value="raboty">Работы по ГК</option>
                    <option value="done">Выполнено</option>
                </select>
            </td>
        </tr>

        <tr data-key="4" data-status="soglasovanie" data-deadline="2026-04-12">
            <td>4</td>
            <td>Интеграция АПК</td>
            <td><input type="date" class="boss-input" data-field="deadline" value="2026-04-12"></td>
            <td>
                <select class="boss-select status-select status-soglasovanie" data-field="status">
                    <option value="soglasovanie" selected>Согласование ТЗ</option>
                    <option value="torgi">Торги</option>
                    <option value="raboty">Работы по ГК</option>
                    <option value="done">Выполнено</option>
                </select>
            </td>
        </tr>

        <tr data-key="5" data-status="torgi" data-deadline="2026-04-18">
            <td>5</td>
            <td>Интеграция Росдормонитор</td>
            <td><input type="date" class="boss-input" data-field="deadline" value="2026-04-18"></td>
            <td>
                <select class="boss-select status-select status-torgi" data-field="status">
                    <option value="soglasovanie">Согласование ТЗ</option>
                    <option value="torgi" selected>Торги</option>
                    <option value="raboty">Работы по ГК</option>
                    <option value="done">Выполнено</option>
                </select>
            </td>
        </tr>

        <tr data-key="6" data-status="soglasovanie" data-deadline="2026-05-05">
            <td>6</td>
            <td>Настройка Родительской платы</td>
            <td><input type="date" class="boss-input" data-field="deadline" value="2026-05-05"></td>
            <td>
                <select class="boss-select status-select status-soglasovanie" data-field="status">
                    <option value="soglasovanie" selected>Согласование ТЗ</option>
                    <option value="torgi">Торги</option>
                    <option value="raboty">Работы по ГК</option>
                    <option value="done">Выполнено</option>
                </select>
            </td>
        </tr>

        <tr data-key="7" data-status="soglasovanie" data-deadline="2026-05-10">
            <td>7</td>
            <td>Настройка Опеки и попечительства</td>
            <td><input type="date" class="boss-input" data-field="deadline" value="2026-05-10"></td>
            <td>
                <select class="boss-select status-select status-soglasovanie" data-field="status">
                    <option value="soglasovanie" selected>Согласование ТЗ</option>
                    <option value="torgi">Торги</option>
                    <option value="raboty">Работы по ГК</option>
                    <option value="done">Выполнено</option>
                </select>
            </td>
        </tr>

        <tr data-key="8" data-status="soglasovanie" data-deadline="2026-05-15">
            <td>8</td>
            <td>Интеграция с медицинскими инф. системами</td>
            <td><input type="date" class="boss-input" data-field="deadline" value="2026-05-15"></td>
            <td>
                <select class="boss-select status-select status-soglasovanie" data-field="status">
                    <option value="soglasovanie" selected>Согласование ТЗ</option>
                    <option value="torgi">Торги</option>
                    <option value="raboty">Работы по ГК</option>
                    <option value="done">Выполнено</option>
                </select>
            </td>
        </tr>

        <tr data-key="9" data-status="done" data-deadline="2026-05-20">
            <td>9</td>
            <td>Интеграция с ГИС ЕСКУ</td>
            <td><input type="date" class="boss-input" data-field="deadline" value="2026-05-20"></td>
            <td>
                <select class="boss-select status-select status-done" data-field="status">
                    <option value="soglasovanie">Согласование ТЗ</option>
                    <option value="torgi">Торги</option>
                    <option value="raboty">Работы по ГК</option>
                    <option value="done" selected>Выполнено</option>
                </select>
            </td>
        </tr>

        <tr data-key="10" data-status="soglasovanie" data-deadline="2026-05-25">
            <td>10</td>
            <td>Техподдержка ГИС "Смета ЯНАО"</td>
            <td><input type="date" class="boss-input" data-field="deadline" value="2026-05-25"></td>
            <td>
                <select class="boss-select status-select status-soglasovanie" data-field="status">
                    <option value="soglasovanie" selected>Согласование ТЗ</option>
                    <option value="torgi">Торги</option>
                    <option value="raboty">Работы по ГК</option>
                    <option value="done">Выполнено</option>
                </select>
            </td>
        </tr>

        <tr data-key="11" data-status="done" data-deadline="2026-06-05">
            <td>11</td>
            <td>Слияние баз</td>
            <td><input type="date" class="boss-input" data-field="deadline" value="2026-06-05"></td>
            <td>
                <select class="boss-select status-select status-done" data-field="status">
                    <option value="soglasovanie">Согласование ТЗ</option>
                    <option value="torgi">Торги</option>
                    <option value="raboty">Работы по ГК</option>
                    <option value="done" selected>Выполнено</option>
                </select>
            </td>
        </tr>

        <tr data-key="12" data-status="torgi" data-deadline="2026-06-08">
            <td>12</td>
            <td>Настройка контроля колич-х и качественных показателей обработки документов ИИ</td>
            <td><input type="date" class="boss-input" data-field="deadline" value="2026-06-08"></td>
            <td>
                <select class="boss-select status-select status-torgi" data-field="status">
                    <option value="soglasovanie">Согласование ТЗ</option>
                    <option value="torgi" selected>Торги</option>
                    <option value="raboty">Работы по ГК</option>
                    <option value="done">Выполнено</option>
                </select>
            </td>
        </tr>
    </tbody>
</table>

<!-- ==================== ДЕТАЛИЗАЦИЯ ПО ЭТАПАМ ==================== -->
<details class="details-block">
<summary>Показать детализацию по этапам</summary>

<table class="project-table">
    <thead>
        <tr>
            <th>№</th>
            <th>Мероприятие</th>
            <th>Согласовали постановку задачи</th>
            <th>Согласовали ТЗ</th>
            <th>Запустились на торги</th>
            <th>Тестовая эксплуатация</th>
            <th>Выполнено</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td><td>Интеграция с Тэзис</td>
            <td class="status-done">10.02.26<br>Ставер</td>
            <td class="status-work">01.03.26</td>
            <td>15.03.26</td><td>01.04.26</td><td>20.04.26</td>
        </tr>
        <tr>
            <td>2</td><td>Интеграция ЛК/Сметы с сервисом по предоставлению справок</td>
            <td class="status-done">05.02.26<br>Сапогов</td>
            <td class="status-work">20.02.26<br>Сапогов</td>
            <td>10.03.26</td><td>25.03.26</td><td>15.04.26</td>
        </tr>
        <tr>
            <td>3</td><td>Интеграция имущества</td>
            <td>12.02.26<br>Обмолова</td>
            <td>05.03.26</td><td>20.03.26</td><td>10.04.26</td><td>05.05.26</td>
        </tr>
        <tr>
            <td>4</td><td>Интеграция АПК</td>
            <td class="status-work">01.02.26<br>Гасанов</td>
            <td>18.02.26</td><td>05.03.26</td><td>22.03.26</td><td>12.04.26</td>
        </tr>
        <tr>
            <td>5</td><td>Интеграция Росдормонитор</td>
            <td class="status-done">08.02.26<br>Сапогов</td>
            <td class="status-work">25.02.26<br>Сапогов</td>
            <td>12.03.26</td><td>28.03.26</td><td>18.04.26</td>
        </tr>
        <tr>
            <td>6</td><td>Настройка Родительской платы</td>
            <td>15.02.26</td><td>08.03.26</td><td>25.03.26</td><td>12.04.26</td><td>05.05.26</td>
        </tr>
        <tr>
            <td>7</td><td>Настройка Опеки и попечительства</td>
            <td>18.02.26<br>Сапогов</td>
            <td>12.03.26</td><td>30.03.26</td><td>18.04.26</td><td>10.05.26</td>
        </tr>
        <tr>
            <td>8</td><td>Интеграция с медицинскими инф. системами</td>
            <td>20.02.26</td><td>15.03.26</td><td>05.04.26</td><td>25.04.26</td><td>15.05.26</td>
        </tr>
        <tr>
            <td>9</td><td>Интеграция с ГИС ЕСКУ</td>
            <td class="status-done">25.02.26</td>
            <td class="status-done">20.03.26</td>
            <td class="status-done">10.04.26</td>
            <td>30.04.26</td><td>20.05.26</td>
        </tr>
        <tr>
            <td>10</td><td>Техподдержка ГИС "Смета ЯНАО"</td>
            <td>01.03.26</td><td>22.03.26</td><td>12.04.26</td><td>05.05.26</td><td>25.05.26</td>
        </tr>
        <tr>
            <td>11</td><td>Слияние баз</td>
            <td class="status-done">10.03.26</td>
            <td class="status-work">05.04.26</td>
            <td>25.04.26</td><td>15.05.26</td><td>05.06.26</td>
        </tr>
        <tr>
            <td>12</td><td>Настройка контроля колич-х и качественных показателей обработки документов ИИ</td>
            <td class="status-work">15.03.26<br>Ставер</td>
            <td>08.04.26</td><td>28.04.26</td><td>18.05.26</td><td>08.06.26</td>
        </tr>
    </tbody>
</table>

</details>

<script>
(function () {
  'use strict';

  // ====== СОСТОЯНИЕ ======
  const state = {
    statuses:  {},   // "1".."12" -> "soglasovanie"|"torgi"|"raboty"|"done"
    deadlines: {}    // "1".."12" -> "YYYY-MM-DD"
  };

  const rows = document.querySelectorAll('#bossTable tbody tr');

  // ====== 1. Цвет статуса ======
  function applyStatusColor(sel) {
    sel.classList.remove('status-soglasovanie','status-torgi','status-raboty','status-done');
    sel.classList.add('status-' + sel.value);
  }

  // ====== 2. Инициализация из data-атрибутов ======
  rows.forEach(tr => {
    const key = tr.dataset.key;
    state.statuses[key]  = tr.dataset.status || 'soglasovanie';
    state.deadlines[key] = tr.dataset.deadline || '';
    const statusSel = tr.querySelector('select[data-field="status"]');
    if (statusSel) applyStatusColor(statusSel);
  });

  // ====== 3. Обработчики ======
  document.querySelectorAll('#bossTable select, #bossTable input').forEach(el => {
    el.addEventListener('change', function () {
      const tr    = this.closest('tr');
      const key   = tr.dataset.key;
      const field = this.dataset.field;

      if (field === 'deadline') {
        state.deadlines[key] = this.value;
        tr.dataset.deadline = this.value;
      } else if (field === 'status') {
        state.statuses[key] = this.value;
        tr.dataset.status = this.value;
        applyStatusColor(this);
      }
      saveState();
    });
  });

  // ====== 4. Загрузка сохранённых значений ======
  fetch('/api/statuses', { cache: 'no-store' })
    .then(r => r.ok ? r.json() : {})
    .then(saved => {
      if (saved.statuses) {
        Object.keys(saved.statuses).forEach(k => {
          const tr = document.querySelector('#bossTable tbody tr[data-key="' + k + '"]');
          if (!tr) return;
          const val = saved.statuses[k];
          const sel = tr.querySelector('select[data-field="status"]');
          if (sel) { sel.value = val; applyStatusColor(sel); }
          tr.dataset.status = val;
          state.statuses[k] = val;
        });
      }
      if (saved.deadlines) {
        Object.keys(saved.deadlines).forEach(k => {
          const inp = document.querySelector('#bossTable tbody tr[data-key="' + k + '"] input[data-field="deadline"]');
          if (inp) {
            inp.value = saved.deadlines[k];
            state.deadlines[k] = saved.deadlines[k];
            const tr = inp.closest('tr');
            if (tr) tr.dataset.deadline = saved.deadlines[k];
          }
        });
      }
    })
    .catch(() => {});

  // ====== 5. Сохранение ======
  let saveTimer = null;
  function saveState() {
    clearTimeout(saveTimer);
    saveTimer = setTimeout(() => {
      fetch('/api/statuses', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(state)
      }).catch(() => {});
    }, 150);
  }
})();
</script>