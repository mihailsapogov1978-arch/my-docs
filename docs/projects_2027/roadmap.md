# Карта мероприятий 2027 года

<style>
.boss-table {
    width: 100%;
    border-collapse: collapse;
    font-family: inherit;
    font-size: 14px;
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
    padding: 10px 12px;
    border-bottom: 1px solid #e0e4e8;
}
.boss-table td {
    padding: 10px 12px;
    border-bottom: 1px solid #eef2f6;
    vertical-align: middle;
}
.boss-table tr.main-row:hover td { background: #fafbfc; }

.boss-table tr.main-row.open td {
    background: #eaf4ff;
    border-bottom-color: #bee3f8;
}
.boss-table tr.main-row.open td:first-child {
    box-shadow: inset 3px 0 0 #3182ce;
}
.boss-table tr.main-row.open:hover td {
    background: #e1efff;
}

.boss-input {
    width: 100%;
    box-sizing: border-box;
    font-family: inherit;
    font-size: 14px;
    padding: 6px 8px;
    border: 1px solid #cfd6dd;
    border-radius: 6px;
    background: #fff;
    color: #2c3e50;
    cursor: pointer;
    outline: none !important;
    box-shadow: none !important;
}
.boss-input:focus,
.boss-input:focus-visible {
    outline: none !important;
    box-shadow: 0 0 0 2px rgba(49,130,206,0.25) !important;
    border-color: #3182ce;
}

.status-badge {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 6px;
    font-size: 14px;
    font-weight: 500;
    text-align: center;
    width: 100%;
    box-sizing: border-box;
}
.status-badge.status-soglasovanie { background: #bde0fe; color: #1a365d; }
.status-badge.status-torgi         { background: #f8c8d4; color: #742a2a; }
.status-badge.status-raboty        { background: #f0e085; color: #744210; }
.status-badge.status-done          { background: #90ee90; color: #22543d; }
.status-badge.status-postanovka    { background: #e2e8f0; color: #2d3748; }

.meropriyatie-cell { cursor: pointer; user-select: none; }
.meropriyatie-cell:hover { color: #2b6cb0; }

.row-toggle {
    display: inline-block;
    float: right;
    width: 20px;
    height: 20px;
    line-height: 18px;
    text-align: center;
    color: #3182ce;
    font-size: 16px;
    font-weight: 700;
    user-select: none;
    transition: transform 0.15s;
    margin-left: 8px;
}
.row-toggle.open { transform: rotate(180deg); }

.detail-row > td {
    padding: 0 !important;
    background: #fafbfc;
    border-bottom: 1px solid #e0e4e8;
}
.detail-wrap { padding: 12px 16px 16px 16px; }
.detail-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
    background: #fff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    overflow: hidden;
}
.detail-table th {
    background: #edf2f7;
    color: #2c3e50;
    font-weight: 600;
    text-align: left;
    padding: 8px 12px;
    border-bottom: 1px solid #e2e8f0;
    font-size: 12.5px;
}
.detail-table td {
    padding: 6px 8px;
    border-bottom: 1px solid #f0f4f8;
    vertical-align: middle;
}
.detail-table tr:last-child td { border-bottom: none; }

.detail-input,
.detail-select {
    width: 100%;
    box-sizing: border-box;
    font-family: inherit;
    font-size: 13px;
    padding: 4px 6px;
    border: 1px solid #cfd6dd;
    border-radius: 5px;
    background: #fff;
    color: #2c3e50;
    outline: none;
}
.detail-textarea {
    resize: vertical;
    min-height: 30px;
    max-height: 200px;
    overflow-y: hidden;
    line-height: 1.35;
    font-family: inherit;
    white-space: pre-wrap;
    word-break: break-word;
}
.detail-input:focus,
.detail-select:focus {
    box-shadow: 0 0 0 2px rgba(49,130,206,0.25);
    border-color: #3182ce;
}
.detail-checkbox {
    width: 18px;
    height: 18px;
    cursor: pointer;
    display: block;
    margin: 0 auto;
}
</style>

<table class="boss-table" id="bossTable">
    <thead>
        <tr>
            <th style="width:40px;">№</th>
            <th>Мероприятие</th>
            <th style="width:135px;">Срок реализации</th>
            <th style="width:175px;">Этап</th>
        </tr>
    </thead>
    <tbody>

        <!-- 2027 · 1 -->
        <tr class="main-row" data-key="2027-1" data-status="soglasovanie" data-deadline="">
            <td>1</td>
            <td class="meropriyatie-cell">Оказание услуг по технической поддержке программного продукта «Автоматизированная система бюджетного учета «Смета» <span class="row-toggle">⌄</span></td>
            <td><input type="date" class="boss-input" data-field="deadline" value=""></td>
            <td><span class="status-badge status-soglasovanie" data-field="status-badge">Согласование ТЗ</span></td>
        </tr>
        <tr class="detail-row" data-detail-for="2027-1" style="display:none;">
            <td colspan="4">
                <div class="detail-wrap">
                    <table class="detail-table">
                        <thead><tr><th>Этап</th><th style="width:120px;">Дата</th><th style="width:180px;">Ответственный</th><th>Комментарий</th><th style="width:50px; text-align:center;">✓</th></tr></thead>
                        <tbody data-steps-for="2027-1">
                            <tr data-step="1"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="2"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="3"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="4"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="5"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                        </tbody>
                    </table>
                </div>
            </td>
        </tr>

        <!-- 2027 · 2 -->
        <tr class="main-row" data-key="2027-2" data-status="soglasovanie" data-deadline="">
            <td>2</td>
            <td class="meropriyatie-cell">Оказание услуг по настройке функционала администрирования ГИС «Смета ЯНАО» <span class="row-toggle">⌄</span></td>
            <td><input type="date" class="boss-input" data-field="deadline" value=""></td>
            <td><span class="status-badge status-soglasovanie" data-field="status-badge">Согласование ТЗ</span></td>
        </tr>
        <tr class="detail-row" data-detail-for="2027-2" style="display:none;">
            <td colspan="4">
                <div class="detail-wrap">
                    <table class="detail-table">
                        <thead><tr><th>Этап</th><th style="width:120px;">Дата</th><th style="width:180px;">Ответственный</th><th>Комментарий</th><th style="width:50px; text-align:center;">✓</th></tr></thead>
                        <tbody data-steps-for="2027-2">
                            <tr data-step="1"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="2"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="3"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="4"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="5"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                        </tbody>
                    </table>
                </div>
            </td>
        </tr>

        <!-- 2027 · 3 -->
        <tr class="main-row" data-key="2027-3" data-status="soglasovanie" data-deadline="">
            <td>3</td>
            <td class="meropriyatie-cell">Оказание услуг по настройке в ГИС «Смета ЯНАО» механизма централизованного извлечения данных для формирования дашбордов и электронного взаимодействия (интеграции) с внешней информационной системой ГИС РСУД (Дашборды) <span class="row-toggle">⌄</span></td>
            <td><input type="date" class="boss-input" data-field="deadline" value=""></td>
            <td><span class="status-badge status-soglasovanie" data-field="status-badge">Согласование ТЗ</span></td>
        </tr>
        <tr class="detail-row" data-detail-for="2027-3" style="display:none;">
            <td colspan="4">
                <div class="detail-wrap">
                    <table class="detail-table">
                        <thead><tr><th>Этап</th><th style="width:120px;">Дата</th><th style="width:180px;">Ответственный</th><th>Комментарий</th><th style="width:50px; text-align:center;">✓</th></tr></thead>
                        <tbody data-steps-for="2027-3">
                            <tr data-step="1"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="2"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="3"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="4"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="5"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                        </tbody>
                    </table>
                </div>
            </td>
        </tr>

        <!-- 2027 · 4 -->
        <tr class="main-row" data-key="2027-4" data-status="soglasovanie" data-deadline="">
            <td>4</td>
            <td class="meropriyatie-cell">Оказание услуг по настройке ГИС «Смета ЯНАО» в части электронного взаимодействия (интеграции) с внешней информационной системой ГИС «Имущество ЯНАО» <span class="row-toggle">⌄</span></td>
            <td><input type="date" class="boss-input" data-field="deadline" value=""></td>
            <td><span class="status-badge status-soglasovanie" data-field="status-badge">Согласование ТЗ</span></td>
        </tr>
        <tr class="detail-row" data-detail-for="2027-4" style="display:none;">
            <td colspan="4">
                <div class="detail-wrap">
                    <table class="detail-table">
                        <thead><tr><th>Этап</th><th style="width:120px;">Дата</th><th style="width:180px;">Ответственный</th><th>Комментарий</th><th style="width:50px; text-align:center;">✓</th></tr></thead>
                        <tbody data-steps-for="2027-4">
                            <tr data-step="1"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="2"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="3"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="4"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="5"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                        </tbody>
                    </table>
                </div>
            </td>
        </tr>

        <!-- 2027 · 5 -->
        <tr class="main-row" data-key="2027-5" data-status="soglasovanie" data-deadline="">
            <td>5</td>
            <td class="meropriyatie-cell">Оказание услуг по настройке в ГИС «Смета ЯНАО» механизма централизованного извлечения данных для передачи во внешнюю информационную систему ИАС «Мониторинг Ямал» <span class="row-toggle">⌄</span></td>
            <td><input type="date" class="boss-input" data-field="deadline" value=""></td>
            <td><span class="status-badge status-soglasovanie" data-field="status-badge">Согласование ТЗ</span></td>
        </tr>
        <tr class="detail-row" data-detail-for="2027-5" style="display:none;">
            <td colspan="4">
                <div class="detail-wrap">
                    <table class="detail-table">
                        <thead><tr><th>Этап</th><th style="width:120px;">Дата</th><th style="width:180px;">Ответственный</th><th>Комментарий</th><th style="width:50px; text-align:center;">✓</th></tr></thead>
                        <tbody data-steps-for="2027-5">
                            <tr data-step="1"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="2"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="3"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="4"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="5"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                        </tbody>
                    </table>
                </div>
            </td>
        </tr>

        <!-- 2027 · 6 -->
        <tr class="main-row" data-key="2027-6" data-status="soglasovanie" data-deadline="">
            <td>6</td>
            <td class="meropriyatie-cell">Оказание услуг по настройке ГИС «Смета ЯНАО» <span class="row-toggle">⌄</span></td>
            <td><input type="date" class="boss-input" data-field="deadline" value=""></td>
            <td><span class="status-badge status-soglasovanie" data-field="status-badge">Согласование ТЗ</span></td>
        </tr>
        <tr class="detail-row" data-detail-for="2027-6" style="display:none;">
            <td colspan="4">
                <div class="detail-wrap">
                    <table class="detail-table">
                        <thead><tr><th>Этап</th><th style="width:120px;">Дата</th><th style="width:180px;">Ответственный</th><th>Комментарий</th><th style="width:50px; text-align:center;">✓</th></tr></thead>
                        <tbody data-steps-for="2027-6">
                            <tr data-step="1"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="2"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="3"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="4"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="5"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                        </tbody>
                    </table>
                </div>
            </td>
        </tr>

        <!-- 2027 · 7 -->
        <tr class="main-row" data-key="2027-7" data-status="soglasovanie" data-deadline="">
            <td>7</td>
            <td class="meropriyatie-cell">Оказание услуг по настройке ГИС «Смета ЯНАО» в части электронного взаимодействия (интеграции) с внешней информационной системой ГИС ЕСКУ <span class="row-toggle">⌄</span></td>
            <td><input type="date" class="boss-input" data-field="deadline" value=""></td>
            <td><span class="status-badge status-soglasovanie" data-field="status-badge">Согласование ТЗ</span></td>
        </tr>
        <tr class="detail-row" data-detail-for="2027-7" style="display:none;">
            <td colspan="4">
                <div class="detail-wrap">
                    <table class="detail-table">
                        <thead><tr><th>Этап</th><th style="width:120px;">Дата</th><th style="width:180px;">Ответственный</th><th>Комментарий</th><th style="width:50px; text-align:center;">✓</th></tr></thead>
                        <tbody data-steps-for="2027-7">
                            <tr data-step="1"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="2"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="3"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="4"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="5"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                        </tbody>
                    </table>
                </div>
            </td>
        </tr>

        <!-- 2027 · 8 -->
        <tr class="main-row" data-key="2027-8" data-status="soglasovanie" data-deadline="">
            <td>8</td>
            <td class="meropriyatie-cell">Оказание услуг по миграции данных в ГИС «Смета ЯНАО» учреждений в связи с их реорганизацией/ликвидацией <span class="row-toggle">⌄</span></td>
            <td><input type="date" class="boss-input" data-field="deadline" value=""></td>
            <td><span class="status-badge status-soglasovanie" data-field="status-badge">Согласование ТЗ</span></td>
        </tr>
        <tr class="detail-row" data-detail-for="2027-8" style="display:none;">
            <td colspan="4">
                <div class="detail-wrap">
                    <table class="detail-table">
                        <thead><tr><th>Этап</th><th style="width:120px;">Дата</th><th style="width:180px;">Ответственный</th><th>Комментарий</th><th style="width:50px; text-align:center;">✓</th></tr></thead>
                        <tbody data-steps-for="2027-8">
                            <tr data-step="1"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="2"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="3"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="4"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="5"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                        </tbody>
                    </table>
                </div>
            </td>
        </tr>

        <!-- 2027 · 9 -->
        <tr class="main-row" data-key="2027-9" data-status="soglasovanie" data-deadline="">
            <td>9</td>
            <td class="meropriyatie-cell">Оказание услуг по настройке ГИС «Смета ЯНАО» в части автоматизации учетных процессов учреждений сферы здравоохранения <span class="row-toggle">⌄</span></td>
            <td><input type="date" class="boss-input" data-field="deadline" value=""></td>
            <td><span class="status-badge status-soglasovanie" data-field="status-badge">Согласование ТЗ</span></td>
        </tr>
        <tr class="detail-row" data-detail-for="2027-9" style="display:none;">
            <td colspan="4">
                <div class="detail-wrap">
                    <table class="detail-table">
                        <thead><tr><th>Этап</th><th style="width:120px;">Дата</th><th style="width:180px;">Ответственный</th><th>Комментарий</th><th style="width:50px; text-align:center;">✓</th></tr></thead>
                        <tbody data-steps-for="2027-9">
                            <tr data-step="1"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="2"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="3"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="4"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="5"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                        </tbody>
                    </table>
                </div>
            </td>
        </tr>

        <!-- 2027 · 10 -->
        <tr class="main-row" data-key="2027-10" data-status="soglasovanie" data-deadline="">
            <td>10</td>
            <td class="meropriyatie-cell">Приобретение права использования программного обеспечения (операционная система) на условиях простой (неисключительной) лицензии ОС «Альт 8 СП» («Альт СП») Сервер релиз 10 <span class="row-toggle">⌄</span></td>
            <td><input type="date" class="boss-input" data-field="deadline" value=""></td>
            <td><span class="status-badge status-soglasovanie" data-field="status-badge">Согласование ТЗ</span></td>
        </tr>
        <tr class="detail-row" data-detail-for="2027-10" style="display:none;">
            <td colspan="4">
                <div class="detail-wrap">
                    <table class="detail-table">
                        <thead><tr><th>Этап</th><th style="width:120px;">Дата</th><th style="width:180px;">Ответственный</th><th>Комментарий</th><th style="width:50px; text-align:center;">✓</th></tr></thead>
                        <tbody data-steps-for="2027-10">
                            <tr data-step="1"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="2"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="3"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="4"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="5"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                        </tbody>
                    </table>
                </div>
            </td>
        </tr>

        <!-- 2027 · 11 -->
        <tr class="main-row" data-key="2027-11" data-status="soglasovanie" data-deadline="">
            <td>11</td>
            <td class="meropriyatie-cell">Приобретение простой (неисключительной) лицензии на право использования программного обеспечения Дистрибутив ViPNet Client 5 for Linux <span class="row-toggle">⌄</span></td>
            <td><input type="date" class="boss-input" data-field="deadline" value=""></td>
            <td><span class="status-badge status-soglasovanie" data-field="status-badge">Согласование ТЗ</span></td>
        </tr>
        <tr class="detail-row" data-detail-for="2027-11" style="display:none;">
            <td colspan="4">
                <div class="detail-wrap">
                    <table class="detail-table">
                        <thead><tr><th>Этап</th><th style="width:120px;">Дата</th><th style="width:180px;">Ответственный</th><th>Комментарий</th><th style="width:50px; text-align:center;">✓</th></tr></thead>
                        <tbody data-steps-for="2027-11">
                            <tr data-step="1"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="2"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="3"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="4"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="5"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                        </tbody>
                    </table>
                </div>
            </td>
        </tr>

        <!-- 2027 · 12 -->
        <tr class="main-row" data-key="2027-12" data-status="soglasovanie" data-deadline="">
            <td>12</td>
            <td class="meropriyatie-cell">Приобретение программно-аппаратного комплекса ViPNet Coordinator HW 2000 Q5 в количестве 2-х (двух) юнитов <span class="row-toggle">⌄</span></td>
            <td><input type="date" class="boss-input" data-field="deadline" value=""></td>
            <td><span class="status-badge status-soglasovanie" data-field="status-badge">Согласование ТЗ</span></td>
        </tr>
        <tr class="detail-row" data-detail-for="2027-12" style="display:none;">
            <td colspan="4">
                <div class="detail-wrap">
                    <table class="detail-table">
                        <thead><tr><th>Этап</th><th style="width:120px;">Дата</th><th style="width:180px;">Ответственный</th><th>Комментарий</th><th style="width:50px; text-align:center;">✓</th></tr></thead>
                        <tbody data-steps-for="2027-12">
                            <tr data-step="1"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="2"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="3"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="4"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                            <tr data-step="5"><td class="step-name"></td><td><input type="date" class="detail-input" data-step-field="date" value=""></td><td><select class="detail-select" data-step-field="assignee"></select></td><td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td><td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td></tr>
                        </tbody>
                    </table>
                </div>
            </td>
        </tr>

    </tbody>
</table>

<script>
(function () {
  'use strict';

  const ASSIGNEES = [
    'Останин И.Г.',
    'Сапогов М.Д.',
    'Лычев А.В.',
    'Мулявин Я.В.',
    'Чечеткин М.И.',
    'Кошик В.И.',
    'Роганова А.А.',
    'Худышкин С.Н.',
    'Гасанов С.Н.',
    'Обмолова В.В.',
    'Суханова И.К.',
    'НПО Криста',
  ];

  const STEP_NAMES = {
    1: 'Обоснование',
    2: 'Согласовали ТЗ',
    3: 'Запустились на торги',
    4: 'Тестовая эксплуатация',
    5: 'Выполнено',
  };

  const STEP_TO_STATUS = {
    1: 'postanovka',
    2: 'soglasovanie',
    3: 'torgi',
    4: 'raboty',
    5: 'done',
  };

  const STATUS_LABEL = {
    postanovka:   'Обоснование',
    soglasovanie: 'Согласование ТЗ',
    torgi:        'Торги',
    raboty:       'Работы по ГК',
    done:         'Выполнено',
  };

  // ===== Авторасширение textarea =====
  function autoGrow(el) {
    if (!el || el.tagName !== 'TEXTAREA') return;
    el.style.height = '0px';
    el.style.overflowY = 'hidden';
    el.style.height = (el.scrollHeight + 2) + 'px';
  }

  document.querySelectorAll('#bossTable textarea[data-step-field="comment"]').forEach(t => {
    autoGrow(t);
    t.addEventListener('input', function () { autoGrow(this); saveState(); });
  });

  // ===== Разово: заполняем селекты и подписи этапов =====
  const optionsHTML = '<option value="">—</option>' +
    ASSIGNEES.map(n => '<option>' + n + '</option>').join('');

  document.querySelectorAll('#bossTable select[data-step-field="assignee"]').forEach(sel => {
    if (!sel.innerHTML.trim()) sel.innerHTML = optionsHTML;
  });

  document.querySelectorAll('#bossTable tr[data-step]').forEach(tr => {
    const cell = tr.querySelector('.step-name');
    if (cell && !cell.textContent.trim()) {
      cell.textContent = STEP_NAMES[tr.dataset.step] || '';
    }
  });

  // ===== СОСТОЯНИЕ =====
  const state = {
    statuses:  {},
    deadlines: {},
    details:   {},
  };

  function renderStatusBadge(tr) {
    const key = tr.dataset.key;
    const status = state.statuses[key];
    const badge = tr.querySelector('[data-field="status-badge"]');
    if (!badge) return;
    badge.className = 'status-badge status-' + status;
    badge.textContent = STATUS_LABEL[status] || status;
  }

  function initMainRow(tr) {
    const key = tr.dataset.key;
    state.statuses[key]  = tr.dataset.status || 'soglasovanie';
    state.deadlines[key] = tr.dataset.deadline || '';
    renderStatusBadge(tr);
  }

  document.querySelectorAll('#bossTable tr.main-row').forEach(initMainRow);

  // ===== Раскрытие / сворачивание =====
  function toggleDetail(mainRow) {
    const key = mainRow.dataset.key;
    const detail = document.querySelector('#bossTable tr.detail-row[data-detail-for="' + key + '"]');
    if (!detail) return;
    const toggle = mainRow.querySelector('.row-toggle');
    const isOpen = detail.style.display !== 'none';

    detail.style.display = isOpen ? 'none' : '';
    if (toggle) toggle.classList.toggle('open', !isOpen);
    mainRow.classList.toggle('open', !isOpen);

    if (!isOpen) {
      detail.querySelectorAll('textarea[data-step-field="comment"]').forEach(autoGrow);
    }
  }

  document.querySelectorAll('#bossTable td.meropriyatie-cell').forEach(td => {
    td.addEventListener('click', function () {
      const mainRow = this.closest('tr.main-row');
      if (mainRow) toggleDetail(mainRow);
    });
  });

  // ===== Дата в главной строке =====
  document.querySelectorAll('#bossTable tr.main-row input[data-field="deadline"]').forEach(inp => {
    inp.addEventListener('change', function () {
      const tr = this.closest('tr.main-row');
      const key = tr.dataset.key;
      state.deadlines[key] = this.value || '';
      tr.dataset.deadline = this.value || '';
      saveState();
    });
  });

  // ===== Детализация =====
  function calcStatusFromSteps(stepsBody) {
    let lastChecked = 0;
    stepsBody.querySelectorAll('tr[data-step]').forEach(row => {
      const step = parseInt(row.dataset.step, 10);
      const cb = row.querySelector('input[data-step-field="done"]');
      if (cb && cb.checked) lastChecked = Math.max(lastChecked, step);
    });
    return STEP_TO_STATUS[lastChecked] || 'soglasovanie';
  }

  function collectSteps(stepsBody) {
    const result = {};
    stepsBody.querySelectorAll('tr[data-step]').forEach(row => {
      const step = row.dataset.step;
      const assignee = row.querySelector('[data-step-field="assignee"]').value;
      const comment  = row.querySelector('[data-step-field="comment"]').value;
      const date     = row.querySelector('[data-step-field="date"]').value;
      const done     = row.querySelector('[data-step-field="done"]').checked;
      result[step] = { assignee, comment, date, done };
    });
    return result;
  }

  function refreshStatusFromSteps(mainRow, stepsBody) {
    const newStatus = calcStatusFromSteps(stepsBody);
    const key = mainRow.dataset.key;
    state.statuses[key] = newStatus;
    mainRow.dataset.status = newStatus;
    renderStatusBadge(mainRow);
  }

  document.querySelectorAll('#bossTable tr.detail-row').forEach(detailRow => {
    const mainRow = document.querySelector('#bossTable tr.main-row[data-key="' + detailRow.dataset.detailFor + '"]');
    const stepsBody = detailRow.querySelector('tbody[data-steps-for]');
    if (!mainRow || !stepsBody) return;

    const key = mainRow.dataset.key;

    stepsBody.addEventListener('change', function () {
      state.details[key] = { steps: collectSteps(stepsBody) };
      refreshStatusFromSteps(mainRow, stepsBody);
      saveState();
    });
    stepsBody.addEventListener('input', function (e) {
      if (e.target && e.target.dataset.stepField === 'comment') {
        state.details[key] = { steps: collectSteps(stepsBody) };
        saveState();
      }
    });
  });

  // ===== Загрузка сохранённых значений =====
  fetch('/api/statuses', { cache: 'no-store' })
    .then(r => r.ok ? r.json() : {})
    .then(saved => {
      if (saved.statuses) {
        Object.keys(saved.statuses).forEach(k => {
          if (!k.startsWith('2027-')) return;
          const tr = document.querySelector('#bossTable tr.main-row[data-key="' + k + '"]');
          if (!tr) return;
          const val = saved.statuses[k];
          state.statuses[k] = val;
          tr.dataset.status = val;
          renderStatusBadge(tr);
        });
      }
      if (saved.deadlines) {
        Object.keys(saved.deadlines).forEach(k => {
          if (!k.startsWith('2027-')) return;
          const inp = document.querySelector('#bossTable tr.main-row[data-key="' + k + '"] input[data-field="deadline"]');
          if (inp) {
            inp.value = saved.deadlines[k];
            state.deadlines[k] = saved.deadlines[k];
            const tr = inp.closest('tr.main-row');
            if (tr) tr.dataset.deadline = saved.deadlines[k];
          }
        });
      }
      if (saved.details) {
        Object.keys(saved.details).forEach(k => {
          if (!k.startsWith('2027-')) return;
          const detailRow = document.querySelector('#bossTable tr.detail-row[data-detail-for="' + k + '"]');
          if (!detailRow) return;
          const stepsBody = detailRow.querySelector('tbody[data-steps-for]');
          const steps = (saved.details[k] && saved.details[k].steps) || {};
          Object.keys(steps).forEach(stepNum => {
            const row = stepsBody.querySelector('tr[data-step="' + stepNum + '"]');
            if (!row) return;
            const st = steps[stepNum];
            const a  = row.querySelector('[data-step-field="assignee"]');
            const c  = row.querySelector('[data-step-field="comment"]');
            const d  = row.querySelector('[data-step-field="date"]');
            const cb = row.querySelector('[data-step-field="done"]');
            if (a && st.assignee != null) a.value = st.assignee;
            if (c && st.comment != null) c.value = st.comment;
            if (c && c.tagName === 'TEXTAREA') autoGrow(c);
            if (d && st.date != null) d.value = st.date;
            if (cb) cb.checked = !!st.done;
          });
          state.details[k] = { steps: collectSteps(stepsBody) };
          const mainRow = document.querySelector('#bossTable tr.main-row[data-key="' + k + '"]');
          if (mainRow) refreshStatusFromSteps(mainRow, stepsBody);
        });
      }
    })
    .catch(() => {});

  // ===== Сохранение =====
  let saveTimer = null;
  function saveState() {
    clearTimeout(saveTimer);
    saveTimer = setTimeout(() => {
      const payload = {
        statuses:  {},
        deadlines: {},
        details:   {},
      };
      Object.keys(state.statuses).forEach(k => {
        if (k.startsWith('2027-')) payload.statuses[k] = state.statuses[k];
      });
      Object.keys(state.deadlines).forEach(k => {
        if (k.startsWith('2027-')) payload.deadlines[k] = state.deadlines[k];
      });
      Object.keys(state.details).forEach(k => {
        if (k.startsWith('2027-')) payload.details[k] = state.details[k];
      });

      fetch('/api/statuses', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      }).catch(() => {});
    }, 200);
  }
})();
</script>