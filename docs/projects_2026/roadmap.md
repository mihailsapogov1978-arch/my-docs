# Реализация проектов в 2026 году

<style>
/* ===== ОСНОВНАЯ ТАБЛИЦА ===== */
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

/* Подсветка раскрытой главной строки */
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
.status-badge.status-postanovka { background: #e2e8f0; color: #2d3748; }

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
    resize: vertical;              /* разрешаем тянуть вниз вручную */
    min-height: 30px;
    max-height: 200px;
    overflow-y: hidden;            /* скролл не нужен — растёт по высоте */
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
            <th style="width:170px;">Этап</th>
        </tr>
    </thead>
    <tbody>

        <!-- ============ 1 ============ -->
        <tr class="main-row" data-key="1" data-status="torgi" data-deadline="2026-04-20">
            <td>1</td>
            <td class="meropriyatie-cell">Интеграция ГИС "Смета ЯНАО" с РСЭД "Тэзис" <span class="row-toggle">⌄</span></td>
            <td><input type="date" class="boss-input" data-field="deadline" value="2026-04-20"></td>
            <td><span class="status-badge status-torgi" data-field="status-badge">Торги</span></td>
        </tr>
        <tr class="detail-row" data-detail-for="1" style="display:none;">
            <td colspan="4">
                <div class="detail-wrap">
                    <table class="detail-table">
                        <thead>
                            <tr>
                                <th>Этап</th>
                                <th style="width:120px;">Дата</th>
                                <th style="width:180px;">Ответственный</th>
                                <th>Комментарий</th>
                                <th style="width:50px; text-align:center;">✓</th>
                            </tr>
                        </thead>
                        <tbody data-steps-for="1">
                            <tr data-step="1">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-02-10"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—">Резолюция № 12</textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done" checked></td>
                            </tr>
                            <tr data-step="2">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-03-01"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—">Протокол ВКС</textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="3">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-03-15"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—">Извещение № 017320000123</textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="4">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-04-01"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="5">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-04-20"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </td>
        </tr>

        <!-- ============ 2 ============ -->
        <tr class="main-row" data-key="2" data-status="torgi" data-deadline="2026-04-15">
            <td>2</td>
            <td class="meropriyatie-cell">Интеграция ЛК/Сметы с сервисом по предоставлению справок <span class="row-toggle">⌄</span></td>
            <td><input type="date" class="boss-input" data-field="deadline" value="2026-04-15"></td>
            <td><span class="status-badge status-torgi" data-field="status-badge">Торги</span></td>
        </tr>
        <tr class="detail-row" data-detail-for="2" style="display:none;">
            <td colspan="4">
                <div class="detail-wrap">
                    <table class="detail-table">
                        <thead>
                            <tr>
                                <th>Этап</th>
                                <th style="width:120px;">Дата</th>
                                <th style="width:180px;">Ответственный</th>
                                <th>Комментарий</th>
                                <th style="width:50px; text-align:center;">✓</th>
                            </tr>
                        </thead>
                        <tbody data-steps-for="2">
                            <tr data-step="1">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-02-05"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done" checked></td>
                            </tr>
                            <tr data-step="2">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-02-20"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="3">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-03-10"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="4">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-03-25"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="5">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-04-15"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </td>
        </tr>

        <!-- ============ 3 ============ -->
        <tr class="main-row" data-key="3" data-status="soglasovanie" data-deadline="2026-05-05">
            <td>3</td>
            <td class="meropriyatie-cell">Интеграция ГИС "Смета ЯНАО" с ГИС "Имущество" <span class="row-toggle">⌄</span></td>
            <td><input type="date" class="boss-input" data-field="deadline" value="2026-05-05"></td>
            <td><span class="status-badge status-soglasovanie" data-field="status-badge">Согласование ТЗ</span></td>
        </tr>
        <tr class="detail-row" data-detail-for="3" style="display:none;">
            <td colspan="4">
                <div class="detail-wrap">
                    <table class="detail-table">
                        <thead>
                            <tr>
                                <th>Этап</th>
                                <th style="width:120px;">Дата</th>
                                <th style="width:180px;">Ответственный</th>
                                <th>Комментарий</th>
                                <th style="width:50px; text-align:center;">✓</th>
                            </tr>
                        </thead>
                        <tbody data-steps-for="3">
                            <tr data-step="1">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-02-12"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="2">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-03-05"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="3">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-03-20"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="4">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-04-10"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="5">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-05-05"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </td>
        </tr>

        <!-- ============ 4 ============ -->
        <tr class="main-row" data-key="4" data-status="soglasovanie" data-deadline="2026-04-12">
            <td>4</td>
            <td class="meropriyatie-cell">Интеграция ГИС "Смета ЯНАО" с ГИС "АПК" <span class="row-toggle">⌄</span></td>
            <td><input type="date" class="boss-input" data-field="deadline" value="2026-04-12"></td>
            <td><span class="status-badge status-soglasovanie" data-field="status-badge">Согласование ТЗ</span></td>
        </tr>
        <tr class="detail-row" data-detail-for="4" style="display:none;">
            <td colspan="4">
                <div class="detail-wrap">
                    <table class="detail-table">
                        <thead>
                            <tr>
                                <th>Этап</th>
                                <th style="width:120px;">Дата</th>
                                <th style="width:180px;">Ответственный</th>
                                <th>Комментарий</th>
                                <th style="width:50px; text-align:center;">✓</th>
                            </tr>
                        </thead>
                        <tbody data-steps-for="4">
                            <tr data-step="1">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-02-01"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="2">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-02-18"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="3">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-03-05"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="4">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-03-22"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="5">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-04-12"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </td>
        </tr>

        <!-- ============ 5 ============ -->
        <tr class="main-row" data-key="5" data-status="torgi" data-deadline="2026-04-18">
            <td>5</td>
            <td class="meropriyatie-cell">Интеграция ГИС "Смета ЯНАО" с КТГ-Услуга (Росдормонитор) <span class="row-toggle">⌄</span></td>
            <td><input type="date" class="boss-input" data-field="deadline" value="2026-04-18"></td>
            <td><span class="status-badge status-torgi" data-field="status-badge">Торги</span></td>
        </tr>
        <tr class="detail-row" data-detail-for="5" style="display:none;">
            <td colspan="4">
                <div class="detail-wrap">
                    <table class="detail-table">
                        <thead>
                            <tr>
                                <th>Этап</th>
                                <th style="width:120px;">Дата</th>
                                <th style="width:180px;">Ответственный</th>
                                <th>Комментарий</th>
                                <th style="width:50px; text-align:center;">✓</th>
                            </tr>
                        </thead>
                        <tbody data-steps-for="5">
                            <tr data-step="1">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-02-08"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done" checked></td>
                            </tr>
                            <tr data-step="2">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-02-25"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="3">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-03-12"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="4">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-03-28"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="5">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-04-18"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </td>
        </tr>

        <!-- ============ 6 ============ -->
        <tr class="main-row" data-key="6" data-status="soglasovanie" data-deadline="2026-05-05">
            <td>6</td>
            <td class="meropriyatie-cell">Настройка Родительской платы <span class="row-toggle">⌄</span></td>
            <td><input type="date" class="boss-input" data-field="deadline" value="2026-05-05"></td>
            <td><span class="status-badge status-soglasovanie" data-field="status-badge">Согласование ТЗ</span></td>
        </tr>
        <tr class="detail-row" data-detail-for="6" style="display:none;">
            <td colspan="4">
                <div class="detail-wrap">
                    <table class="detail-table">
                        <thead>
                            <tr>
                                <th>Этап</th>
                                <th style="width:120px;">Дата</th>
                                <th style="width:180px;">Ответственный</th>
                                <th>Комментарий</th>
                                <th style="width:50px; text-align:center;">✓</th>
                            </tr>
                        </thead>
                        <tbody data-steps-for="6">
                            <tr data-step="1">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-02-15"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="2">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-03-08"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="3">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-03-25"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="4">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-04-12"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="5">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-05-05"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </td>
        </tr>

        <!-- ============ 7 ============ -->
        <tr class="main-row" data-key="7" data-status="soglasovanie" data-deadline="2026-05-10">
            <td>7</td>
            <td class="meropriyatie-cell">Настройка Опеки и попечительства <span class="row-toggle">⌄</span></td>
            <td><input type="date" class="boss-input" data-field="deadline" value="2026-05-10"></td>
            <td><span class="status-badge status-soglasovanie" data-field="status-badge">Согласование ТЗ</span></td>
        </tr>
        <tr class="detail-row" data-detail-for="7" style="display:none;">
            <td colspan="4">
                <div class="detail-wrap">
                    <table class="detail-table">
                        <thead>
                            <tr>
                                <th>Этап</th>
                                <th style="width:120px;">Дата</th>
                                <th style="width:180px;">Ответственный</th>
                                <th>Комментарий</th>
                                <th style="width:50px; text-align:center;">✓</th>
                            </tr>
                        </thead>
                        <tbody data-steps-for="7">
                            <tr data-step="1">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-02-18"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="2">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-03-12"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="3">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-03-30"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="4">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-04-18"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="5">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-05-10"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </td>
        </tr>

        <!-- ============ 8 ============ -->
        <tr class="main-row" data-key="8" data-status="soglasovanie" data-deadline="2026-05-15">
            <td>8</td>
            <td class="meropriyatie-cell">Интеграция ГИС "Смета ЯНАО" с медицинскими инф. системами <span class="row-toggle">⌄</span></td>
            <td><input type="date" class="boss-input" data-field="deadline" value="2026-05-15"></td>
            <td><span class="status-badge status-soglasovanie" data-field="status-badge">Согласование ТЗ</span></td>
        </tr>
        <tr class="detail-row" data-detail-for="8" style="display:none;">
            <td colspan="4">
                <div class="detail-wrap">
                    <table class="detail-table">
                        <thead>
                            <tr>
                                <th>Этап</th>
                                <th style="width:120px;">Дата</th>
                                <th style="width:180px;">Ответственный</th>
                                <th>Комментарий</th>
                                <th style="width:50px; text-align:center;">✓</th>
                            </tr>
                        </thead>
                        <tbody data-steps-for="8">
                            <tr data-step="1">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-02-20"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="2">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-03-15"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="3">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-04-05"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="4">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-04-25"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="5">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-05-15"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </td>
        </tr>

        <!-- ============ 9 ============ -->
        <tr class="main-row" data-key="9" data-status="done" data-deadline="2026-05-20">
            <td>9</td>
            <td class="meropriyatie-cell">Интеграция ГИС "Смета ЯНАО" с ГИС ЕСКУ <span class="row-toggle">⌄</span></td>
            <td><input type="date" class="boss-input" data-field="deadline" value="2026-05-20"></td>
            <td><span class="status-badge status-done" data-field="status-badge">Выполнено</span></td>
        </tr>
        <tr class="detail-row" data-detail-for="9" style="display:none;">
            <td colspan="4">
                <div class="detail-wrap">
                    <table class="detail-table">
                        <thead>
                            <tr>
                                <th>Этап</th>
                                <th style="width:120px;">Дата</th>
                                <th style="width:180px;">Ответственный</th>
                                <th>Комментарий</th>
                                <th style="width:50px; text-align:center;">✓</th>
                            </tr>
                        </thead>
                        <tbody data-steps-for="9">
                            <tr data-step="1">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-02-25"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done" checked></td>
                            </tr>
                            <tr data-step="2">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-03-20"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done" checked></td>
                            </tr>
                            <tr data-step="3">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-04-10"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done" checked></td>
                            </tr>
                            <tr data-step="4">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-04-30"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done" checked></td>
                            </tr>
                            <tr data-step="5">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-05-20"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done" checked></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </td>
        </tr>

        <!-- ============ 10 ============ -->
        <tr class="main-row" data-key="10" data-status="soglasovanie" data-deadline="2026-05-25">
            <td>10</td>
            <td class="meropriyatie-cell">Техподдержка ГИС "Смета ЯНАО" <span class="row-toggle">⌄</span></td>
            <td><input type="date" class="boss-input" data-field="deadline" value="2026-05-25"></td>
            <td><span class="status-badge status-soglasovanie" data-field="status-badge">Согласование ТЗ</span></td>
        </tr>
        <tr class="detail-row" data-detail-for="10" style="display:none;">
            <td colspan="4">
                <div class="detail-wrap">
                    <table class="detail-table">
                        <thead>
                            <tr>
                                <th>Этап</th>
                                <th style="width:120px;">Дата</th>
                                <th style="width:180px;">Ответственный</th>
                                <th>Комментарий</th>
                                <th style="width:50px; text-align:center;">✓</th>
                            </tr>
                        </thead>
                        <tbody data-steps-for="10">
                            <tr data-step="1">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-03-01"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="2">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-03-22"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="3">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-04-12"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="4">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-05-05"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="5">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-05-25"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </td>
        </tr>

        <!-- ============ 11 ============ -->
        <tr class="main-row" data-key="11" data-status="done" data-deadline="2026-06-05">
            <td>11</td>
            <td class="meropriyatie-cell">Слияние баз <span class="row-toggle">⌄</span></td>
            <td><input type="date" class="boss-input" data-field="deadline" value="2026-06-05"></td>
            <td><span class="status-badge status-done" data-field="status-badge">Выполнено</span></td>
        </tr>
        <tr class="detail-row" data-detail-for="11" style="display:none;">
            <td colspan="4">
                <div class="detail-wrap">
                    <table class="detail-table">
                        <thead>
                            <tr>
                                <th>Этап</th>
                                <th style="width:120px;">Дата</th>
                                <th style="width:180px;">Ответственный</th>
                                <th>Комментарий</th>
                                <th style="width:50px; text-align:center;">✓</th>
                            </tr>
                        </thead>
                        <tbody data-steps-for="11">
                            <tr data-step="1">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-03-10"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done" checked></td>
                            </tr>
                            <tr data-step="2">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-04-05"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="3">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-04-25"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="4">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-05-15"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="5">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value="2026-06-05"></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </td>
        </tr>
<!-- ============ 12 ============ -->
        <tr class="main-row" data-key="12" data-status="soglasovanie" data-deadline="2026-06-30">
            <td>12</td>
            <td class="meropriyatie-cell">Настройка функционала администрирования ГИС "Смета ЯНАО" <span class="row-toggle">⌄</span></td>
            <td><input type="date" class="boss-input" data-field="deadline" value="2026-06-30"></td>
            <td><span class="status-badge status-soglasovanie" data-field="status-badge">Согласование ТЗ</span></td>
        </tr>
        <tr class="detail-row" data-detail-for="12" style="display:none;">
            <td colspan="4">
                <div class="detail-wrap">
                    <table class="detail-table">
                        <thead>
                            <tr>
                                <th>Этап</th>
                                <th style="width:120px;">Дата</th>
                                <th style="width:180px;">Ответственный</th>
                                <th>Комментарий</th>
                                <th style="width:50px; text-align:center;">✓</th>
                            </tr>
                        </thead>
                        <tbody data-steps-for="12">
                            <tr data-step="1">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value=""></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="2">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value=""></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="3">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value=""></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="4">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value=""></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
                            <tr data-step="5">
                                <td class="step-name"></td>
                                <td><input type="date" class="detail-input" data-step-field="date" value=""></td>
                                <td><select class="detail-select" data-step-field="assignee"></select></td>
                                <td><textarea class="detail-input detail-textarea" data-step-field="comment" rows="1" placeholder="—"></textarea></td>
                                <td style="text-align:center;"><input type="checkbox" class="detail-checkbox" data-step-field="done"></td>
                            </tr>
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

  // ===== Справочники (один раз для всей страницы) =====
  const ASSIGNEES = [
    'Останин И.Г.',
    'Сапогов М.Д.',
    'Ставер А.П.',
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
    1: 'Постановка задачи',
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
    postanovka:   'Постановка задачи',
    soglasovanie: 'Согласование ТЗ',
    torgi:        'Торги',
    raboty:       'Работы по ГК',
    done:         'Выполнено',
  };

  // ===== Авторасширение textarea для комментариев =====
  function autoGrow(el) {
    el.style.height = 'auto';
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
    details:   {}
  };

  // ===== Главная строка: инициализация бейджа =====
  function initMainRow(tr) {
    const key = tr.dataset.key;
    state.statuses[key]  = tr.dataset.status || 'soglasovanie';
    state.deadlines[key] = tr.dataset.deadline || '';
    renderStatusBadge(tr);
  }

  function renderStatusBadge(tr) {
    const key = tr.dataset.key;
    const status = state.statuses[key];
    const badge = tr.querySelector('[data-field="status-badge"]');
    if (!badge) return;
    badge.className = 'status-badge status-' + status;
    badge.textContent = STATUS_LABEL[status] || status;
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

    // Пересчёт высоты textarea при раскрытии
    if (!isOpen) {
      detail.querySelectorAll('textarea[data-step-field="comment"]').forEach(autoGrow);
    }   // ← подсветка главной строки
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
          const detailRow = document.querySelector('#bossTable tr.detail-row[data-detail-for="' + k + '"]');
          if (!detailRow) return;
          const stepsBody = detailRow.querySelector('tbody[data-steps-for]');
          const steps = (saved.details[k] && saved.details[k].steps) || {};
          Object.keys(steps).forEach(stepNum => {
            const row = stepsBody.querySelector('tr[data-step="' + stepNum + '"]');
            if (!row) return;
            const st = steps[stepNum];
            const a = row.querySelector('[data-step-field="assignee"]');
            const c = row.querySelector('[data-step-field="comment"]');
            const d = row.querySelector('[data-step-field="date"]');
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
      fetch('/api/statuses', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(state)
      }).catch(() => {});
    }, 200);
  }
})();
</script>