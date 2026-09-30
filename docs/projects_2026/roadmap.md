# План проектов на 2026 год

<style>
/* ===== ПЛИТКИ СВОДКИ ===== */
.summary {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    margin: 20px 0 25px 0;
}
.summary-card {
    background: #fff;
    border-radius: 10px;
    padding: 18px 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    border-left: 5px solid #3182ce;
}
.summary-card .label {
    font-size: 13px;
    color: #4a5568;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    margin-bottom: 6px;
}
.summary-card .value {
    font-size: 32px;
    font-weight: 700;
    color: #2c3e50;
    line-height: 1;
}
.summary-card.done  { border-left-color: #38a169; }
.summary-card.work  { border-left-color: #e6b800; }
.summary-card.late  { border-left-color: #e53e3e; }
.summary-card.done .value { color: #2f855a; }
.summary-card.work .value { color: #b7791f; }
.summary-card.late .value { color: #c53030; }

@media (max-width: 720px) {
    .summary { grid-template-columns: repeat(2, 1fr); }
}

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

/* ===== SELECT / INPUT В ТАБЛИЦЕ ===== */
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

/* цветной select статуса — перекрашивается через JS */
select.status-select option { background: #fff; color: #2c3e50; }
select.status-select.status-done { background: #90ee90; }
select.status-select.status-work { background: #f0e085; }
select.status-select.status-late { background: #f5a6a6; }

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

<!-- ==================== СВОДКА ДЛЯ РУКОВОДИТЕЛЯ ==================== -->
<div class="summary" id="summary">
    <div class="summary-card">
        <div class="label">Всего</div>
        <div class="value" id="sum-total">—</div>
    </div>
    <div class="summary-card work">
        <div class="label">В работе</div>
        <div class="value" id="sum-work">—</div>
    </div>
    <div class="summary-card late">
        <div class="label">Просрочено</div>
        <div class="value" id="sum-late">—</div>
    </div>
    <div class="summary-card done">
        <div class="label">Готово</div>
        <div class="value" id="sum-done">—</div>
    </div>
</div>

<!-- ==================== КОМПАКТНАЯ ТАБЛИЦА ==================== -->
<table class="boss-table" id="bossTable">
    <thead>
        <tr>
            <th style="width:32px;">№</th>
            <th>Мероприятие</th>
            <th style="width:130px;">Ответственный</th>
            <th style="width:130px;">Этап</th>
            <th style="width:130px;">Срок реализации</th>
            <th style="width:120px;">Статус</th>
        </tr>
    </thead>
    <tbody>
        <tr data-key="1" data-status="work" data-deadline="2026-04-20">
            <td>1</td>
            <td>Интеграция с Тэзис</td>
            <td>
                <select class="boss-select" data-field="assignee">
                    <option value="">—</option>
                    <option>Сапогов М.Д.</option>
                    <option>Мулявин Я.В.</option>
                    <option>Чечеткин М.И.</option>
                    <option>Кошик В.И.</option>
                    <option>Роганова А.А.</option>
                    <option>Худышкин С.Н.</option>
                    <option>Гасанов С.Н.</option>
                </select>
            </td>
            <td>
                <select class="boss-select" data-field="stage">
                    <option value="">—</option>
                    <option>Согласование ТЗ</option>
                    <option>Торги</option>
                    <option>Тестирование</option>
                </select>
            </td>
            <td>
                <input type="date" class="boss-input" data-field="deadline" value="2026-04-20">
            </td>
            <td>
                <select class="boss-select status-select status-work" data-field="status">
                    <option value="late">Просрочено</option>
                    <option value="work" selected>В работе</option>
                    <option value="done">Выполнено</option>
                </select>
            </td>
        </tr>

        <tr data-key="2" data-status="work" data-deadline="2026-04-15">
            <td>2</td>
            <td>Интеграция ЛК/Сметы с сервисом по предоставлению справок</td>
            <td>
                <select class="boss-select" data-field="assignee">
                    <option value="">—</option>
                    <option>Сапогов М.Д.</option>
                    <option>Мулявин Я.В.</option>
                    <option>Чечеткин М.И.</option>
                    <option>Кошик В.И.</option>
                    <option>Роганова А.А.</option>
                    <option>Худышкин С.Н.</option>
                    <option>Гасанов С.Н.</option>
                </select>
            </td>
            <td>
                <select class="boss-select" data-field="stage">
                    <option value="">—</option>
                    <option>Согласование ТЗ</option>
                    <option>Торги</option>
                    <option>Тестирование</option>
                </select>
            </td>
            <td>
                <input type="date" class="boss-input" data-field="deadline" value="2026-04-15">
            </td>
            <td>
                <select class="boss-select status-select status-work" data-field="status">
                    <option value="late">Просрочено</option>
                    <option value="work" selected>В работе</option>
                    <option value="done">Выполнено</option>
                </select>
            </td>
        </tr>

        <tr data-key="3" data-status="late" data-deadline="2026-05-05">
            <td>3</td>
            <td>Интеграция имущества</td>
            <td>
                <select class="boss-select" data-field="assignee">
                    <option value="">—</option>
                    <option>Сапогов М.Д.</option>
                    <option>Мулявин Я.В.</option>
                    <option>Чечеткин М.И.</option>
                    <option>Кошик В.И.</option>
                    <option>Роганова А.А.</option>
                    <option>Худышкин С.Н.</option>
                    <option>Гасанов С.Н.</option>
                </select>
            </td>
            <td>
                <select class="boss-select" data-field="stage">
                    <option value="">—</option>
                    <option>Согласование ТЗ</option>
                    <option>Торги</option>
                    <option>Тестирование</option>
                </select>
            </td>
            <td>
                <input type="date" class="boss-input" data-field="deadline" value="2026-05-05">
            </td>
            <td>
                <select class="boss-select status-select status-late" data-field="status">
                    <option value="late" selected>Просрочено</option>
                    <option value="work">В работе</option>
                    <option value="done">Выполнено</option>
                </select>
            </td>
        </tr>

        <tr data-key="4" data-status="work" data-deadline="2026-04-12">
            <td>4</td>
            <td>Интеграция АПК</td>
            <td>
                <select class="boss-select" data-field="assignee">
                    <option value="">—</option>
                    <option>Сапогов М.Д.</option>
                    <option>Мулявин Я.В.</option>
                    <option>Чечеткин М.И.</option>
                    <option>Кошик В.И.</option>
                    <option>Роганова А.А.</option>
                    <option>Худышкин С.Н.</option>
                    <option>Гасанов С.Н.</option>
                </select>
            </td>
            <td>
                <select class="boss-select" data-field="stage">
                    <option value="">—</option>
                    <option>Согласование ТЗ</option>
                    <option>Торги</option>
                    <option>Тестирование</option>
                </select>
            </td>
            <td>
                <input type="date" class="boss-input" data-field="deadline" value="2026-04-12">
            </td>
            <td>
                <select class="boss-select status-select status-work" data-field="status">
                    <option value="late">Просрочено</option>
                    <option value="work" selected>В работе</option>
                    <option value="done">Выполнено</option>
                </select>
            </td>
        </tr>

        <tr data-key="5" data-status="work" data-deadline="2026-04-18">
            <td>5</td>
            <td>Интеграция Росдормонитор</td>
            <td>
                <select class="boss-select" data-field="assignee">
                    <option value="">—</option>
                    <option>Сапогов М.Д.</option>
                    <option>Мулявин Я.В.</option>
                    <option>Чечеткин М.И.</option>
                    <option>Кошик В.И.</option>
                    <option>Роганова А.А.</option>
                    <option>Худышкин С.Н.</option>
                    <option>Гасанов С.Н.</option>
                </select>
            </td>
            <td>
                <select class="boss-select" data-field="stage">
                    <option value="">—</option>
                    <option>Согласование ТЗ</option>
                    <option>Торги</option>
                    <option>Тестирование</option>
                </select>
            </td>
            <td>
                <input type="date" class="boss-input" data-field="deadline" value="2026-04-18">
            </td>
            <td>
                <select class="boss-select status-select status-work" data-field="status">
                    <option value="late">Просрочено</option>
                    <option value="work" selected>В работе</option>
                    <option value="done">Выполнено</option>
                </select>
            </td>
        </tr>

        <tr data-key="6" data-status="late" data-deadline="2026-05-05">
            <td>6</td>
            <td>Настройка Родительской платы</td>
            <td>
                <select class="boss-select" data-field="assignee">
                    <option value="">—</option>
                    <option>Сапогов М.Д.</option>
                    <option>Мулявин Я.В.</option>
                    <option>Чечеткин М.И.</option>
                    <option>Кошик В.И.</option>
                    <option>Роганова А.А.</option>
                    <option>Худышкин С.Н.</option>
                    <option>Гасанов С.Н.</option>
                </select>
            </td>
            <td>
                <select class="boss-select" data-field="stage">
                    <option value="">—</option>
                    <option>Согласование ТЗ</option>
                    <option>Торги</option>
                    <option>Тестирование</option>
                </select>
            </td>
            <td>
                <input type="date" class="boss-input" data-field="deadline" value="2026-05-05">
            </td>
            <td>
                <select class="boss-select status-select status-late" data-field="status">
                    <option value="late" selected>Просрочено</option>
                    <option value="work">В работе</option>
                    <option value="done">Выполнено</option>
                </select>
            </td>
        </tr>

        <tr data-key="7" data-status="late" data-deadline="2026-05-10">
            <td>7</td>
            <td>Настройка Опеки и попечительства</td>
            <td>
                <select class="boss-select" data-field="assignee">
                    <option value="">—</option>
                    <option>Сапогов М.Д.</option>
                    <option>Мулявин Я.В.</option>
                    <option>Чечеткин М.И.</option>
                    <option>Кошик В.И.</option>
                    <option>Роганова А.А.</option>
                    <option>Худышкин С.Н.</option>
                    <option>Гасанов С.Н.</option>
                </select>
            </td>
            <td>
                <select class="boss-select" data-field="stage">
                    <option value="">—</option>
                    <option>Согласование ТЗ</option>
                    <option>Торги</option>
                    <option>Тестирование</option>
                </select>
            </td>
            <td>
                <input type="date" class="boss-input" data-field="deadline" value="2026-05-10">
            </td>
            <td>
                <select class="boss-select status-select status-late" data-field="status">
                    <option value="late" selected>Просрочено</option>
                    <option value="work">В работе</option>
                    <option value="done">Выполнено</option>
                </select>
            </td>
        </tr>

        <tr data-key="8" data-status="late" data-deadline="2026-05-15">
            <td>8</td>
            <td>Интеграция с медицинскими инф. системами</td>
            <td>
                <select class="boss-select" data-field="assignee">
                    <option value="">—</option>
                    <option>Сапогов М.Д.</option>
                    <option>Мулявин Я.В.</option>
                    <option>Чечеткин М.И.</option>
                    <option>Кошик В.И.</option>
                    <option>Роганова А.А.</option>
                    <option>Худышкин С.Н.</option>
                    <option>Гасанов С.Н.</option>
                </select>
            </td>
            <td>
                <select class="boss-select" data-field="stage">
                    <option value="">—</option>
                    <option>Согласование ТЗ</option>
                    <option>Торги</option>
                    <option>Тестирование</option>
                </select>
            </td>
            <td>
                <input type="date" class="boss-input" data-field="deadline" value="2026-05-15">
            </td>
            <td>
                <select class="boss-select status-select status-late" data-field="status">
                    <option value="late" selected>Просрочено</option>
                    <option value="work">В работе</option>
                    <option value="done">Выполнено</option>
                </select>
            </td>
        </tr>

        <tr data-key="9" data-status="done" data-deadline="2026-05-20">
            <td>9</td>
            <td>Интеграция с ГИС ЕСКУ</td>
            <td>
                <select class="boss-select" data-field="assignee">
                    <option value="">—</option>
                    <option>Сапогов М.Д.</option>
                    <option>Мулявин Я.В.</option>
                    <option>Чечеткин М.И.</option>
                    <option>Кошик В.И.</option>
                    <option>Роганова А.А.</option>
                    <option>Худышкин С.Н.</option>
                    <option>Гасанов С.Н.</option>
                </select>
            </td>
            <td>
                <select class="boss-select" data-field="stage">
                    <option value="">—</option>
                    <option>Согласование ТЗ</option>
                    <option>Торги</option>
                    <option>Тестирование</option>
                </select>
            </td>
            <td>
                <input type="date" class="boss-input" data-field="deadline" value="2026-05-20">
            </td>
            <td>
                <select class="boss-select status-select status-done" data-field="status">
                    <option value="late">Просрочено</option>
                    <option value="work">В работе</option>
                    <option value="done" selected>Выполнено</option>
                </select>
            </td>
        </tr>

        <tr data-key="10" data-status="late" data-deadline="2026-05-25">
            <td>10</td>
            <td>Техподдержка ГИС "Смета ЯНАО"</td>
            <td>
                <select class="boss-select" data-field="assignee">
                    <option value="">—</option>
                    <option>Сапогов М.Д.</option>
                    <option>Мулявин Я.В.</option>
                    <option>Чечеткин М.И.</option>
                    <option>Кошик В.И.</option>
                    <option>Роганова А.А.</option>
                    <option>Худышкин С.Н.</option>
                    <option>Гасанов С.Н.</option>
                </select>
            </td>
            <td>
                <select class="boss-select" data-field="stage">
                    <option value="">—</option>
                    <option>Согласование ТЗ</option>
                    <option>Торги</option>
                    <option>Тестирование</option>
                </select>
            </td>
            <td>
                <input type="date" class="boss-input" data-field="deadline" value="2026-05-25">
            </td>
            <td>
                <select class="boss-select status-select status-late" data-field="status">
                    <option value="late" selected>Просрочено</option>
                    <option value="work">В работе</option>
                    <option value="done">Выполнено</option>
                </select>
            </td>
        </tr>

        <tr data-key="11" data-status="work" data-deadline="2026-06-05">
            <td>11</td>
            <td>Слияние баз</td>
            <td>
                <select class="boss-select" data-field="assignee">
                    <option value="">—</option>
                    <option>Сапогов М.Д.</option>
                    <option>Мулявин Я.В.</option>
                    <option>Чечеткин М.И.</option>
                    <option>Кошик В.И.</option>
                    <option>Роганова А.А.</option>
                    <option>Худышкин С.Н.</option>
                    <option>Гасанов С.Н.</option>
                </select>
            </td>
            <td>
                <select class="boss-select" data-field="stage">
                    <option value="">—</option>
                    <option>Согласование ТЗ</option>
                    <option>Торги</option>
                    <option>Тестирование</option>
                </select>
            </td>
            <td>
                <input type="date" class="boss-input" data-field="deadline" value="2026-06-05">
            </td>
            <td>
                <select class="boss-select status-select status-work" data-field="status">
                    <option value="late">Просрочено</option>
                    <option value="work" selected>В работе</option>
                    <option value="done">Выполнено</option>
                </select>
            </td>
        </tr>

        <tr data-key="12" data-status="work" data-deadline="2026-06-08">
            <td>12</td>
            <td>Настройка контроля колич-х и качественных показателей обработки документов ИИ</td>
            <td>
                <select class="boss-select" data-field="assignee">
                    <option value="">—</option>
                    <option>Сапогов М.Д.</option>
                    <option>Мулявин Я.В.</option>
                    <option>Чечеткин М.И.</option>
                    <option>Кошик В.И.</option>
                    <option>Роганова А.А.</option>
                    <option>Худышкин С.Н.</option>
                    <option>Гасанов С.Н.</option>
                </select>
            </td>
            <td>
                <select class="boss-select" data-field="stage">
                    <option value="">—</option>
                    <option>Согласование ТЗ</option>
                    <option>Торги</option>
                    <option>Тестирование</option>
                </select>
            </td>
            <td>
                <input type="date" class="boss-input" data-field="deadline" value="2026-06-08">
            </td>
            <td>
                <select class="boss-select status-select status-work" data-field="status">
                    <option value="late">Просрочено</option>
                    <option value="work" selected>В работе</option>
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
    statuses:  {},   // "1".."12" -> "done"|"work"|"late"
    assignees: {},   // "1".."12" -> ФИО
    stages:    {},   // "1".."12" -> "Согласование ТЗ"|"Торги"|"Тестирование"
    deadlines: {}    // "1".."12" -> "YYYY-MM-DD"
  };

  const rows = document.querySelectorAll('#bossTable tbody tr');

  // ====== 1. Сводка ======
  function recalcSummary() {
    let total = rows.length, work = 0, done = 0, late = 0;
    rows.forEach(tr => {
      const s = tr.dataset.status || 'work';
      if (s === 'work') work++;
      if (s === 'done') done++;
      if (s === 'late') late++;
    });
    document.getElementById('sum-total').textContent = total;
    document.getElementById('sum-work').textContent  = work;
    document.getElementById('sum-late').textContent  = late;
    document.getElementById('sum-done').textContent  = done;
  }

  // ====== 2. Применение цвета к select статуса ======
  function applyStatusColor(sel) {
    sel.classList.remove('status-done', 'status-work', 'status-late');
    sel.classList.add('status-' + sel.value);
  }

  // ====== 3. Первичная инициализация из data-атрибутов ======
  rows.forEach(tr => {
    const key = tr.dataset.key;
    state.statuses[key]  = tr.dataset.status || 'work';
    state.deadlines[key] = tr.dataset.deadline || '';

    // статус — select
    const statusSel = tr.querySelector('select[data-field="status"]');
    if (statusSel) applyStatusColor(statusSel);
  });

  recalcSummary();

  // ====== 4. Обработчики ======
  document.querySelectorAll('#bossTable select, #bossTable input').forEach(el => {
    el.addEventListener('change', function () {
      const tr    = this.closest('tr');
      const key   = tr.dataset.key;
      const field = this.dataset.field;

      if (field === 'assignee') {
        state.assignees[key] = this.value;
      } else if (field === 'stage') {
        state.stages[key] = this.value;
      } else if (field === 'deadline') {
        state.deadlines[key] = this.value;
        tr.dataset.deadline = this.value;
      } else if (field === 'status') {
        state.statuses[key] = this.value;
        tr.dataset.status = this.value;
        applyStatusColor(this);
        recalcSummary();
      }
      saveState();
    });
  });

  // ====== 5. Загрузка сохранённых значений ======
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
      if (saved.assignees) {
        Object.keys(saved.assignees).forEach(k => {
          const sel = document.querySelector('#bossTable tbody tr[data-key="' + k + '"] select[data-field="assignee"]');
          if (sel) { sel.value = saved.assignees[k]; state.assignees[k] = saved.assignees[k]; }
        });
      }
      if (saved.stages) {
        Object.keys(saved.stages).forEach(k => {
          const sel = document.querySelector('#bossTable tbody tr[data-key="' + k + '"] select[data-field="stage"]');
          if (sel) { sel.value = saved.stages[k]; state.stages[k] = saved.stages[k]; }
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
      recalcSummary();
    })
    .catch(() => {});

  // ====== 6. Сохранение ======
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