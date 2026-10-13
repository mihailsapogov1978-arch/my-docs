<style>
.dash-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 14px;
    margin: 20px 0 30px 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}
.dash-card {
    display: block;
    background: #fff;
    border: 1px solid #e2e8f0;
    border-left: 4px solid #2b6cb0;
    border-radius: 10px;
    padding: 16px 18px;
    text-decoration: none !important;
    color: inherit !important;
    transition: box-shadow 0.15s, transform 0.15s;
}
.dash-card:hover {
    box-shadow: 0 4px 14px rgba(43, 108, 176, 0.10);
    transform: translateY(-1px);
}
.dash-card .dc-label {
    font-size: 11.5px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #718096;
    font-weight: 700;
    margin-bottom: 8px;
}
.dash-card .dc-value {
    font-size: 28px;
    font-weight: 700;
    color: #2c3e50;
    line-height: 1.1;
    margin-bottom: 6px;
}
.dash-card .dc-value.dc-good { color: #2f855a; }
.dash-card .dc-value.dc-warn { color: #b7791f; }
.dash-card .dc-value.dc-bad  { color: #c53030; }
.dash-card .dc-sub {
    font-size: 12.5px;
    color: #4a5568;
    font-weight: 500;
    line-height: 1.4;
}
.dash-card.dc-done    { border-left-color: #38a169; }
.dash-card.dc-work    { border-left-color: #e6b800; }
.dash-card.dc-late    { border-left-color: #e53e3e; }
.dash-card.dc-neutral { border-left-color: #805ad5; }
.dash-card.dc-info    { border-left-color: #3182ce; }

.attn-table {
    width: 100%;
    border-collapse: collapse;
    background: #fff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    overflow: hidden;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 13.5px;
    margin: 12px 0 24px 0;
}
.attn-table th {
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
.attn-table td {
    padding: 10px 14px;
    border-bottom: 1px solid #eef2f6;
    vertical-align: middle;
}
.attn-table tr:last-child td { border-bottom: none; }
.attn-table .at-deadline { white-space: nowrap; font-weight: 700; }
.attn-table .at-deadline.overdue { color: #c53030; }
.attn-table .at-deadline.soon    { color: #b7791f; }
.attn-table .at-deadline.near    { color: #2b6cb0; }

.attn-empty {
    padding: 14px 18px;
    background: #f0fff4;
    border: 1px solid #c6f6d5;
    border-radius: 8px;
    color: #276749;
    font-size: 13.5px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}
</style>

# Дашборд

*Обновлено: 13 октября 2026*

<div class="dash-grid">
<a class="dash-card dc-info" href="projects_2026/roadmap/">
    <div class="dc-label">Мероприятия 2026</div>
    <div class="dc-value">14</div>
    <div class="dc-sub">в работе 11 · выполнено 3</div>
</a>
<a class="dash-card dc-late" href="calendar/">
    <div class="dc-label">Просрочено</div>
    <div class="dc-value dc-bad">1</div>
    <div class="dc-sub">требует внимания</div>
</a>
<a class="dash-card dc-done" href="projects_2026/roadmap/">
    <div class="dc-label">Готово</div>
    <div class="dc-value dc-good">3</div>
    <div class="dc-sub">из 14 мероприятий</div>
</a>
<a class="dash-card dc-neutral" href="Contracts/svod_gk/">
    <div class="dc-label">Заключено контрактов за 2026 год</div>
    <div class="dc-value">8</div>
    <div class="dc-sub">на сумму 75 936 750,00 ₽</div>
</a>
<a class="dash-card dc-done" href="reports/">
    <div class="dc-label">Последний отчёт</div>
    <div class="dc-value" style="font-size:18px;">Сентября 2026</div>
    <div class="dc-sub">отчёты отдела СРиТП</div>
</a>
<a class="dash-card dc-info" href="calls/calls/">
    <div class="dc-label">Звонки за Сентябрь 2026</div>
    <div class="dc-value" style="font-size:22px;">21057</div>
    <div class="dc-sub">принятые 8966 · пропущенные 2979 · исходящие 9112</div>
</a>
</div>

## Требует внимания

<table class="attn-table">
<thead><tr><th>Мероприятие</th><th style="width:140px;">Срок</th><th style="width:170px;">Этап</th></tr></thead>
<tbody>
<tr><td>Интеграция ГИС "Смета ЯНАО" с медицинскими инф. системами</td><td class="at-deadline overdue">15.05.2026</td><td>Постановка задачи</td></tr>
<tr><td>Интеграция ЛК/Сметы с сервисом по предоставлению справок</td><td class="at-deadline near">01.11.2026</td><td>Работы по ГК</td></tr>
</tbody></table>
