<style>
.cal-table {
    width: 100%;
    border-collapse: collapse;
    background: #fff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    overflow: hidden;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 13.5px;
    margin: 16px 0 24px 0;
}
.cal-table th {
    background: #f5f7fa;
    color: #2c3e50;
    font-weight: 600;
    text-align: left;
    padding: 10px 14px;
    border-bottom: 1px solid #e2e8f0;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 0.03em;
}
.cal-table td {
    padding: 10px 14px;
    border-bottom: 1px solid #eef2f6;
    vertical-align: middle;
}
.cal-table tr:last-child td { border-bottom: none; }

.cal-date {
    white-space: nowrap;
    font-weight: 700;
    color: #2c3e50;
}
.cal-days {
    text-align: right;
    white-space: nowrap;
    color: #718096;
    font-size: 12.5px;
}

.cal-row.overdue td { background: #fff5f5; }
.cal-row.overdue .cal-date { color: #c53030; }
.cal-row.soon td    { background: #fffaf0; }
.cal-row.soon .cal-date { color: #b7791f; }
.cal-row.near td    { background: #f0f8ff; }
.cal-row.near .cal-date { color: #2b6cb0; }

.cal-kind {
    display: inline-block;
    padding: 2px 10px;
    border-radius: 10px;
    font-size: 11.5px;
    font-weight: 600;
    white-space: nowrap;
}
.cal-kind.k-roadmap  { background: #ebf8ff; color: #2b6cb0; }
.cal-kind.k-report   { background: #f0fff4; color: #2f855a; }
.cal-kind.k-meeting  { background: #faf5ff; color: #6b46c1; }
.cal-kind.k-contract { background: #fffaf0; color: #b7791f; }
.cal-kind.k-other    { background: #edf2f7; color: #4a5568; }

.cal-summary {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin: 12px 0 22px 0;
}
.cal-summary .cs-card {
    background: #fff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 14px 16px;
    border-left: 4px solid #3182ce;
}
.cal-summary .cs-card.cs-overdue { border-left-color: #c53030; }
.cal-summary .cs-card.cs-soon    { border-left-color: #b7791f; }
.cal-summary .cs-card.cs-near    { border-left-color: #2b6cb0; }
.cal-summary .cs-card.cs-total   { border-left-color: #4a5568; }
.cal-summary .cs-value {
    font-size: 24px;
    font-weight: 700;
    color: #2c3e50;
    line-height: 1.1;
}
.cal-summary .cs-label {
    font-size: 11.5px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #718096;
    font-weight: 700;
    margin-top: 6px;
}
@media (max-width: 720px) {
    .cal-summary { grid-template-columns: repeat(2, 1fr); }
}
</style>

# Календарь ключевых дат

*Обновлено: 13 октября 2026*

<div class="cal-summary">
<div class="cs-card cs-overdue">
    <div class="cs-value">1</div>
    <div class="cs-label">Просрочено</div>
</div>
<div class="cs-card cs-soon">
    <div class="cs-value">0</div>
    <div class="cs-label">В течение 7 дней</div>
</div>
<div class="cs-card cs-near">
    <div class="cs-value">3</div>
    <div class="cs-label">В течение 30 дней</div>
</div>
<div class="cs-card cs-total">
    <div class="cs-value">11</div>
    <div class="cs-label">Всего в календаре</div>
</div>
</div>

<table class="cal-table">
<thead><tr><th style="width:130px;">Дата</th><th style="width:130px;">Тип</th><th>Событие</th><th style="width:110px; text-align:right;">Осталось</th></tr></thead>
<tbody>
<tr class="cal-row overdue"><td class="cal-date">15.05.2026</td><td><span class="cal-kind k-roadmap">Мероприятие</span></td><td>Интеграция ГИС "Смета ЯНАО" с медицинскими инф. системами <span style="color:#718096;font-size:12px;">— Постановка задачи</span></td><td class="cal-days">просрочено на 151 дн.</td></tr>
<tr class="cal-row near"><td class="cal-date">26.10.2026</td><td><span class="cal-kind k-report">Отчётность</span></td><td>Отчет по аудиту ПО в ДИТиС <span style="color:#718096;font-size:12px;">— Отчет</span></td><td class="cal-days">13 дн.</td></tr>
<tr class="cal-row near"><td class="cal-date">01.11.2026</td><td><span class="cal-kind k-roadmap">Мероприятие</span></td><td>Интеграция ЛК/Сметы с сервисом по предоставлению справок <span style="color:#718096;font-size:12px;">— Работы по ГК</span></td><td class="cal-days">19 дн.</td></tr>
<tr class="cal-row near"><td class="cal-date">01.11.2026</td><td><span class="cal-kind k-report">Отчётность</span></td><td>Отчёт по импортозамещению <span style="color:#718096;font-size:12px;">— ДИТиС</span></td><td class="cal-days">19 дн.</td></tr>
<tr class="cal-row"><td class="cal-date">25.11.2026</td><td><span class="cal-kind k-roadmap">Мероприятие</span></td><td>Настройка Опеки и попечительства <span style="color:#718096;font-size:12px;">— Торги</span></td><td class="cal-days">43 дн.</td></tr>
<tr class="cal-row"><td class="cal-date">01.12.2026</td><td><span class="cal-kind k-roadmap">Мероприятие</span></td><td>Слияние баз <span style="color:#718096;font-size:12px;">— Торги</span></td><td class="cal-days">49 дн.</td></tr>
<tr class="cal-row"><td class="cal-date">10.12.2026</td><td><span class="cal-kind k-roadmap">Мероприятие</span></td><td>Интеграция ГИС "Смета ЯНАО" с РСЭД "Тэзис" <span style="color:#718096;font-size:12px;">— Согласование ТЗ</span></td><td class="cal-days">58 дн.</td></tr>
<tr class="cal-row"><td class="cal-date">10.12.2026</td><td><span class="cal-kind k-roadmap">Мероприятие</span></td><td>Настройка Родительской платы <span style="color:#718096;font-size:12px;">— Работы по ГК</span></td><td class="cal-days">58 дн.</td></tr>
<tr class="cal-row"><td class="cal-date">25.12.2026</td><td><span class="cal-kind k-roadmap">Мероприятие</span></td><td>Интеграция ГИС "Смета ЯНАО" с ГИС "Имущество" <span style="color:#718096;font-size:12px;">— Работы по ГК</span></td><td class="cal-days">73 дн.</td></tr>
<tr class="cal-row"><td class="cal-date">25.12.2026</td><td><span class="cal-kind k-roadmap">Мероприятие</span></td><td>Интеграция ГИС "Смета ЯНАО" с ГИС "АПК" <span style="color:#718096;font-size:12px;">— Работы по ГК</span></td><td class="cal-days">73 дн.</td></tr>
<tr class="cal-row"><td class="cal-date">25.12.2026</td><td><span class="cal-kind k-roadmap">Мероприятие</span></td><td>Настройка функционала администрирования ГИС "Смета ЯНАО" <span style="color:#718096;font-size:12px;">— Торги</span></td><td class="cal-days">73 дн.</td></tr>
</tbody></table>
