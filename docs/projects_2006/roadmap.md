# План проектов на 2026 год

<style>


/* Принудительное размещение лога в правой колонке */
.md-sidebar--secondary {
    position: relative;
}

.md-sidebar__scrollwrap {
    display: flex;
    flex-direction: column;
}

/* Стили для лога внутри TOC */
.toc-log-wrapper {
    margin-top: 20px;
    padding-top: 15px;
    border-top: 2px solid #3498db;
}

.toc-log-title {
    font-size: 14px;
    font-weight: 600;
    color: #2c3e50;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 6px;
}

.toc-log-content {
    font-size: 12px;
    line-height: 1.5;
    max-height: 400px;
    overflow-y: auto;
    padding-right: 8px;
}

.toc-log-content ul {
    padding-left: 20px;
}

.toc-log-content li {
    margin-bottom: 8px;
    color: #4a5568;
}
/* ===== TOOLTIP ===== */
.tooltip {
    position: relative;
    cursor: help;
    border-bottom: 1px dotted #999;  /* пунктирное подчёркивание */
}

.tooltip:hover .tooltip-text {
    visibility: visible;
    opacity: 1;
}

.tooltip-text {
    visibility: hidden;
    opacity: 0;
    width: 200px;
    background-color: #2c3e50;
    color: #fff;
    text-align: left;
    padding: 8px 12px;
    border-radius: 4px;
    font-size: 11px;
    line-height: 1.4;
    
    /* Позиционирование */
    position: absolute;
    z-index: 1000;
    bottom: 130%;
    left: 50%;
    transform: translateX(-50%);
    
    /* Анимация */
    transition: opacity 0.2s;
    
    /* Тень */
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    
    /* Отключаем перенос */
    white-space: normal;
    word-wrap: break-word;
}

/* Стрелочка снизу */
.tooltip-text::after {
    content: "";
    position: absolute;
    top: 100%;
    left: 50%;
    margin-left: -5px;
    border-width: 5px;
    border-style: solid;
    border-color: #2c3e50 transparent transparent transparent;
}

/* ===== ЛЕГЕНДА ===== */
.legend {
    display: flex;
    gap: 20px;
    margin-bottom: 20px;
}
.legend-item {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 12px;
}
.legend-color {
    width: 20px;
    height: 20px;
    border-radius: 4px;
}
.legend-color.done { background-color: #90ee90; }
.legend-color.work { background-color: #f0e085; }
.legend-color.plan { background-color: #bde0fe; }
.legend-color.wait { background-color: #ffffff; border: 1px solid #ccc; }

.status-done { background-color: #90ee90 !important; }  /* ЗЕЛЁНЫЙ */
.status-work { background-color: #f0e085 !important; } /* ЖЁЛТЫЙ */
.status-plan { background-color: #bde0fe !important; }  /* ГОЛУБОЙ */
.status-wait { background-color: #ffffff !important; }  /* БЕЛЫЙ */

/* ===== ТАБЛИЦА КАК В ПРИМЕРЕ ===== */
.project-table {
    border-collapse: collapse;
    width: 100%;
    font-size: 11px;
    line-height: 1.2;
    table-layout: fixed;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
    background-color: #ffffff;
}

/* ===== ЗАГОЛОВКИ — ОБЩИЕ ===== */
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

/* ===== ПЕРВЫЕ ДВА ЗАГОЛОВКА — ГОРИЗОНТАЛЬНЫЕ ===== */
.project-table th:nth-child(1),
.project-table th:nth-child(2) {
    writing-mode: horizontal-tb;
    transform: none;
    font-size: 14px;
    height: 36px;
    white-space: normal;
    text-align: center;
    vertical-align: middle;
}

/* ===== ОСТАЛЬНЫЕ ЗАГОЛОВКИ — ВЕРТИКАЛЬНЫЕ ===== */
.project-table th:nth-child(3),
.project-table th:nth-child(4),
.project-table th:nth-child(5),
.project-table th:nth-child(6),
.project-table th:nth-child(7) {
    writing-mode: vertical-rl;
    text-orientation: mixed;
    transform: rotate(180deg);
    font-size: 14px;
    height: 120px;
    white-space: nowrap;
    line-height: 1.1;
}

/* ===== ЯЧЕЙКИ — БЕЛЫЙ ФОН, УВЕЛИЧЕННАЯ ВЫСОТА ===== */
.project-table td {
    padding: 6px 3px;        /* УВЕЛИЧЕН ВЕРТИКАЛЬНЫЙ ПАДДИНГ */
    border: 1px solid #e0e4e8;
    vertical-align: middle;
    height: 40px;            /* УВЕЛИЧЕНА ВЫСОТА С 28px ДО 36px */
    word-wrap: break-word;
    background-color: #ffffff;
}

/* ===== ПРИНУДИТЕЛЬНАЯ ШИРИНА КОЛОНОК ===== */
.project-table th:nth-child(1) { width: 38px; }
.project-table td:nth-child(1) { 
    width: 28px; 
    text-align: center; 
    font-weight: 500;
    font-size: 11px;
}

.project-table th:nth-child(2) { width: 200px; }
.project-table td:nth-child(2) { 
    width: 250px; 
    padding-left: 8px; 
    font-weight: normal; 
    white-space: normal;
    font-size: 12px;
}

.project-table th:nth-child(3) { width: 48px; }
.project-table td:nth-child(3) { width: 48px; text-align: center; font-size: 11px; }

.project-table th:nth-child(4) { width: 48px; }
.project-table td:nth-child(4) { width: 48px; text-align: center; font-size: 11px; }

.project-table th:nth-child(5) { width: 48px; }
.project-table td:nth-child(5) { width: 48px; text-align: center; font-size: 11px; }

.project-table th:nth-child(6) { width: 48px; }
.project-table td:nth-child(6) { width: 48px; text-align: center; font-size: 11px; }

.project-table th:nth-child(7) { width: 48px; }
.project-table td:nth-child(7) { width: 48px; text-align: center; font-size: 11px; }

/* ===== ВСЕ ЯЧЕЙКИ — БЕЛЫЙ ФОН ===== */
.project-table tbody tr:nth-child(even) td,
.project-table tbody tr:nth-child(odd) td {
    background-color: #ffffff;
}

/* ===== ПОДСВЕТКА ПРИ НАВЕДЕНИИ ===== */
.project-table tbody tr:hover td {
    background-color: #fafbfc;
}

/* ===== УБИРАЕМ МАРКЕРЫ ТОЛЬКО У ЛОГА ===== */
#toc-log-display ul {
    list-style-type: none !important;
    padding-left: 0 !important;
}

#toc-log-display li {
    list-style-type: none !important;
    padding-left: 0 !important;
}

/* ===== МАРКЕРЫ ДЛЯ ЛОГА В TOC ===== */
#toc-log-display ul {
    list-style-type: none !important;
    padding-left: 0 !important;
}

#toc-log-display li {
    list-style-type: none !important;
    padding-left: 24px !important;
    position: relative;
    margin-bottom: 8px;
    line-height: 1.4;
}

/* БАЗОВЫЙ МАРКЕР — СЕРЫЙ КРУЖОК (НЕ НАЧАТО) */
#toc-log-display li::before {
    content: "○";
    position: absolute;
    left: 0;
    color: #95a5a6;
    font-size: 14px;
    font-weight: normal;
}

/* ВЫПОЛНЕНО — ЗЕЛЁНАЯ ГАЛОЧКА */
#toc-log-display li.done::before {
    content: "✓";
    color: #27ae60;
    font-weight: bold;
    font-size: 14px;
}

/* В РАБОТЕ — ЖЁЛТЫЙ КРУЖОК */
#toc-log-display li.work::before {
    content: "●";
    color: #f39c12;
    font-size: 14px;
}

/* ЗАПЛАНИРОВАНО — ГОЛУБОЙ КРУЖОК */
#toc-log-display li.plan::before {
    content: "◉";
    color: #3498db;
    font-size: 14px;
}

/* ===== СТИЛИ ДЛЯ ФОРМЫ ДОБАВЛЕНИЯ ЗАПИСЕЙ ===== */
.log-add-form {
    margin-top: 2px;
    padding: 6px;
    background-color: #f8fafc;
    border-radius: 6px;
    border: 1px solid #e2e8f0;
    flex-shrink: 0;
}

.log-add-title {
    font-size: 14px;
    font-weight: 600;
    color: #2c3e50;
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 6px;
}

/* Компактная сетка формы */
.form-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-bottom: 12px;
}

.form-group {
    margin-bottom: 0;
}

.form-group.full-width {
    grid-column: 1 / -1;
    margin-bottom: 12px;
}

.form-label {
    display: block;
    font-size: 11px;
    font-weight: 600;
    color: #2c3e50;
    margin-bottom: 4px;
    text-transform: uppercase;
    letter-spacing: 0.3px;
}

.form-input {
    width: 100%;
    padding: 8px 10px;
    font-size: 13px;
    border: 1px solid #cbd5e0;
    border-radius: 4px;
    background-color: white;
    box-sizing: border-box;
}

.form-input:focus {
    outline: none;
    border-color: #3498db;
    box-shadow: 0 0 0 2px rgba(52, 152, 219, 0.2);
}

/* Увеличенная высота для поля описания */
.form-input.textarea-like {
    min-height: 70px;
    resize: vertical;
}

.form-select {
    width: 100%;
    padding: 8px 10px;
    font-size: 13px;
    border: 1px solid #cbd5e0;
    border-radius: 4px;
    background-color: white;
    cursor: pointer;
}

.form-select:focus {
    outline: none;
    border-color: #3498db;
    box-shadow: 0 0 0 2px rgba(52, 152, 219, 0.2);
}

.form-actions {
    display: flex;
    gap: 8px;
    margin-top: 0px;
    flex-wrap: wrap;
}

.btn {
    padding: 8px 12px;
    font-size: 13px;
    font-weight: 500;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.2s;
    flex: 1;
    min-width: 80px;
}

.btn-primary {
    background-color: #27ae60;
    color: white;
}

.btn-primary:hover {
    background-color: #219a52;
}

.btn-primary:disabled {
    background-color: #95a5a6;
    cursor: not-allowed;
}

.btn-secondary {
    background-color: #e2e8f0;
    color: #2d3748;
}

.btn-secondary:hover {
    background-color: #cbd5e0;
}

.btn-info {
    background-color: #3498db;
    color: white;
}

.btn-info:hover {
    background-color: #2980b9;
}

.status-preview {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 16px;
    font-size: 12px;
    font-weight: 600;
    margin-top: 0px;
}

.status-preview.done {
    background-color: #90ee90;
    color: #1e3a1e;
}

.status-preview.work {
    background-color: #f0e085;
    color: #7d5e1a;
}

.status-preview.plan {
    background-color: #bde0fe;
    color: #1e4a6b;
}

.status-preview.wait {
    background-color: #ffffff;
    border: 1px solid #ccc;
    color: #4a5568;
}

/* Стили для контейнера с логом - без внешней прокрутки */
.log-scroll-area {
    max-height: none;
    overflow-y: visible;
    margin-bottom: 16px;
    padding-right: 4px;
    border: none;
    background-color: transparent;
}

/* Внутренняя прокрутка только если нужно */
.log-scroll-area.scroll-active {
    max-height: 300px;
    overflow-y: auto;
    border: 1px solid #edf2f7;
    border-radius: 4px;
    background-color: #ffffff;
    padding: 8px;
}

/* Стили для содержимого лога */
#log-content {
    font-size: 13px;
    line-height: 1.5;
}

#log-content ul {
    margin: 0;
    padding-left: 24px;
}

#log-content li {
    margin-bottom: 8px;
    color: #2d3748;
}

/* Стили для календаря Flatpickr - компактная версия */
.flatpickr-calendar {
    font-family: inherit;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    width: 240px !important;
    font-size: 12px;
}

.flatpickr-months {
    padding: 4px 0;
}

.flatpickr-month {
    height: 30px !important;
}

.flatpickr-current-month {
    font-size: 14px !important;
    padding: 0 !important;
}

.flatpickr-weekdays {
    height: 24px !important;
}

.flatpickr-weekday {
    font-size: 11px !important;
    font-weight: 500 !important;
}

.flatpickr-days {
    width: 240px !important;
}

.dayContainer {
    width: 240px !important;
    min-width: 240px !important;
    max-width: 240px !important;
}

.flatpickr-day {
    max-width: 32px !important;
    height: 28px !important;
    line-height: 28px !important;
    font-size: 11px !important;
    margin: 1px !important;
}

.flatpickr-day.selected {
    background-color: #3498db !important;
    border-color: #3498db !important;
    font-weight: bold;
}

.flatpickr-day.today {
    border-color: #3498db;
}

.flatpickr-prev-month, .flatpickr-next-month {
    padding: 4px !important;
}

/* Скрываем дублирующиеся заголовки в логах */
.project-log h4 {
    display: none;
}

/* Делаем отступы более компактными */
#log-content ul {
    margin-top: 0;
    padding-top: 0;
}

#log-content li:first-child {
    margin-top: 0;
}

/* Стили для уведомлений */
.custom-notification {
    position: fixed;
    top: 20px;
    right: 20px;
    padding: 12px 20px;
    background-color: #27ae60;
    color: white;
    border-radius: 4px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    z-index: 9999;
    font-size: 14px;
    animation: slideIn 0.3s ease;
}

@keyframes slideIn {
    from {
        transform: translateX(100%);
        opacity: 0;
    }
    to {
        transform: translateX(0);
        opacity: 1;
    }
}

@keyframes slideOut {
    from {
        transform: translateX(0);
        opacity: 1;
    }
    to {
        transform: translateX(100%);
        opacity: 0;
    }
}
</style>

<!-- ЛЕГЕНДА -->
<div class="legend">
    <div class="legend-item"><span class="legend-color done"></span> Выполнено</div>
    <div class="legend-item"><span class="legend-color work"></span> В работе</div>
    <div class="legend-item"><span class="legend-color plan"></span> Запланировано</div>
    <div class="legend-item"><span class="legend-color wait"></span> Не начато</div>
</div>


<!-- Скрытый блок для логов мероприятий -->
<div id="project-log-container" style="display: none;">
    <div id="log-1" class="project-log">
        <h4 style="display: none;">Интеграция с Тэзис</h4>
        <ul>
            <li class="done">02.10.25 — Разработана бизнес-модель взаимодействия</li>
            <li class="done">02.10.25 — Согласованы тезисы</li>
            <li class="done">26.01.26 — Разработаны и согласованы форматы ЭД</li>
            <li class="done">26.01.26 — Проведен ВКС</li>
            <li class="work">25.10.25 — Подготовка ТЗ</li>
            <li class="plan">17.02.26 — Запланирован ВКС</li>
            <li>20.11.25 — ТЗ утверждено</li>
            <li>10.12.25 — Старт разработки</li>
            <li>15.01.26 — Готово к тестированию</li>
        </ul>
    </div>
    
    <div id="log-2" class="project-log">
        <h4 style="display: none;">Интеграция ЛК/Сметы с сервисом по предоставлению справок</h4>
        <ul>
            <li class="done">03.01.2026 — Проект ТЗ высланы Евдокимову и Орлову. Принято в работу.</li>
            <li class="done">30.01.2026 — В ТЗ внесены правки - добавлен СНИЛС.</li>
            <li class="done">03.02.2026 — Провели ВКС - меняем логику работы</li>
            <li class="work">06.02.2026 — В ТЗ внесены правки, высланы в Техфаргос.</li>
        </ul>
    </div>
    
    <div id="log-3" class="project-log">
        <h4 style="display: none;">Интеграция c ГИС "Имущество"</h4>
        <ul>
            <!-- Пустой список, записи будут добавляться через интерфейс -->
        </ul>
    </div>
    
    <div id="log-4" class="project-log">
        <h4 style="display: none;">Интеграция c ГИС "АПК"</h4>
        <ul>
            <!-- Пустой список, записи будут добавляться через интерфейс -->
        </ul>
    </div>
    
    <div id="log-5" class="project-log">
        <h4 style="display: none;">Интеграция Росдормонитор</h4>
        <ul>
            <!-- Пустой список, записи будут добавляться через интерфейс -->
        </ul>
    </div>
    
    <div id="log-6" class="project-log">
        <h4 style="display: none;">Настройка Родительской платы</h4>
        <ul>
            <!-- Пустой список, записи будут добавляться через интерфейс -->
        </ul>
    </div>
    
    <div id="log-7" class="project-log">
        <h4 style="display: none;">Настройка Опеки и попечительства</h4>
        <ul>
            <!-- Пустой список, записи будут добавляться через интерфейс -->
        </ul>
    </div>
    
    <div id="log-8" class="project-log">
        <h4 style="display: none;">Интеграция с медицинскими инф. системами</h4>
        <ul>
            <!-- Пустой список, записи будут добавляться через интерфейс -->
        </ul>
    </div>
    
    <div id="log-9" class="project-log">
        <h4 style="display: none;">Интеграция с ГИС ЕСКУ</h4>
        <ul>
            <!-- Пустой список, записи будут добавляться через интерфейс -->
        </ul>
    </div>
    
    <div id="log-10" class="project-log">
        <h4 style="display: none;">Техподдержка ГИС "Смета ЯНАО"</h4>
        <ul>
            <!-- Пустой список, записи будут добавляться через интерфейс -->
        </ul>
    </div>
    
    <div id="log-11" class="project-log">
        <h4 style="display: none;">Слияние баз</h4>
        <ul>
            <!-- Пустой список, записи будут добавляться через интерфейс -->
        </ul>
    </div>
    
    <div id="log-12" class="project-log">
        <h4 style="display: none;">Настройка контроля колич-х и качественных показателей обработки документов ИИ</h4>
        <ul>
            <!-- Пустой список, записи будут добавляться через интерфейс -->
        </ul>
    </div>
</div>


<table class="project-table">
<thead>
    <tr>
        <th>№</th>
        <th>Мероприятие</th>
        <th>Согласовали<br>постановку задачи</th>
        <th>Согласовали<br>ТЗ</th>
        <th>Запустились на торги</th>
        <th>Тестовая эксплуатация</th>
        <th>Пром</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td>1</td>
        <td>Интеграция с Тэзис</td>
        <td class="status-done">10.02.26<br>Ставер</td>
        <td class="status-work">01.03.26</td>
        <td>15.03.26</td>
        <td>01.04.26</td>
        <td>20.04.26</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Интеграция ЛК/Сметы с сервисом по предоставлению справок</td>
        <td class="status-done tooltip">05.02.26<br>Сапогов
          <span class="tooltip-text">
            <strong>Этап 1. Согласование постановки задачи</strong><br>
            Ответственный: Ставер<br>
            Срок: 10.02.2026<br>
            Статус: Выполнено
          </span>
        </td>
        <td class="status-work">20.02.26<br>Сапогов</td>
        <td>10.03.26</td>
        <td>25.03.26</td>
        <td>15.04.26</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Интеграция имущества</td>
        <td>12.02.26<br>Обмолова</td>
        <td>05.03.26</td>
        <td>20.03.26</td>
        <td>10.04.26</td>
        <td>05.05.26</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Интеграция АПК</td>
        <td class="status-work">01.02.26<br>Гасанов</td>
        <td>18.02.26</td>
        <td>05.03.26</td>
        <td>22.03.26</td>
        <td>12.04.26</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Интеграция Росдормонитор</td>
        <td class="status-work">08.02.26<br>Сапогов</td>
        <td class="status-work">25.02.26<br>Сапогов</td>
        <td>12.03.26</td>
        <td>28.03.26</td>
        <td>18.04.26</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Настройка Родительской платы</td>
        <td class="status-work">15.02.26</td>
        <td>08.03.26</td>
        <td>25.03.26</td>
        <td>12.04.26</td>
        <td>05.05.26</td>
    </tr>
    <tr>
        <td>7</td>
        <td>Настройка Опеки и попечительства</td>
        <td class="status-work">18.02.26<br>Сапогов</td>
        <td>12.03.26</td>
        <td>30.03.26</td>
        <td>18.04.26</td>
        <td>10.05.26</td>
    </tr>
    <tr>
        <td>8</td>
        <td>Интеграция с медицинскими инф. системами</td>
        <td>20.02.26</td>
        <td>15.03.26</td>
        <td>05.04.26</td>
        <td>25.04.26</td>
        <td>15.05.26</td>
    </tr>
    <tr>
        <td>9</td>
        <td>Интеграция с ГИС ЕСКУ</td>
        <td>25.02.26</td>
        <td>20.03.26</td>
        <td>10.04.26</td>
        <td>30.04.26</td>
        <td>20.05.26</td>
    </tr>
    <tr>
        <td>10</td>
        <td>Техподдержка ГИС "Смета ЯНАО"</td>
        <td>01.03.26</td>
        <td>22.03.26</td>
        <td>12.04.26</td>
        <td>05.05.26</td>
        <td>25.05.26</td>
    </tr>
    <tr>
        <td>11</td>
        <td>Слияние баз</td>
        <td class="status-done">10.03.26</td>
        <td class="status-work">05.04.26</td>
        <td>25.04.26</td>
        <td>15.05.26</td>
        <td>05.06.26</td>
    </tr>
    <tr>
        <td>12</td>
        <td>Настройка контроля колич-х и качественных показателей обработки документов ИИ</td>
        <td class="status-work">15.03.26<br>Ставер</td>
        <td>08.04.26</td>
        <td>28.04.26</td>
        <td>18.05.26</td>
        <td>08.06.26</td>
    </tr>
</tbody>
</table>

<!-- Подключаем Flatpickr для календаря -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flatpickr/dist/flatpickr.min.css">
<script src="https://cdn.jsdelivr.net/npm/flatpickr"></script>
<script src="https://cdn.jsdelivr.net/npm/flatpickr/dist/l10n/ru.js"></script>

<script>
document.addEventListener('DOMContentLoaded', function() {
    // ===== НАСТРОЙКИ GITHUB =====
    const GITHUB_TOKEN = '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'; 
    const GITHUB_REPO = 'mihailsapogov1978-arch/my-docs';
    const GITHUB_PATH = 'docs/projects_2006/roadmap.md';
    const GITHUB_BRANCH = 'main';

    // Функция показа уведомлений
    function showNotification(message, type = 'success') {
        const oldNotifications = document.querySelectorAll('.custom-notification');
        oldNotifications.forEach(n => n.remove());
        
        const notification = document.createElement('div');
        notification.className = 'custom-notification';
        notification.style.backgroundColor = type === 'success' ? '#27ae60' : type === 'info' ? '#3498db' : '#e74c3c';
        notification.textContent = message;
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.style.animation = 'slideOut 0.3s ease';
            setTimeout(() => notification.remove(), 300);
        }, 5000);
    }

    // ===== ФУНКЦИЯ ЗАГРУЗКИ ЛОГОВ С GITHUB =====
    async function loadLogsFromGitHub() {
        try {
            const url = `https://api.github.com/repos/${GITHUB_REPO}/contents/${GITHUB_PATH}?ref=${GITHUB_BRANCH}`;
            
            const response = await fetch(url, {
                headers: {
                    'Authorization': `token ${GITHUB_TOKEN}`,
                    'Accept': 'application/vnd.github.v3+json'
                }
            });
            
            if (!response.ok) {
                console.log('Не удалось загрузить логи с GitHub, используем локальные');
                return;
            }
            
            const data = await response.json();
            const content = decodeURIComponent(escape(atob(data.content)));
            
            // Массив с названиями проектов
            const projectNames = [
                'Интеграция с Тэзис',
                'Интеграция ЛК/Сметы с сервисом по предоставлению справок',
                'Интеграция c ГИС "Имущество"',
                'Интеграция c ГИС "АПК"',
                'Интеграция Росдормонитор',
                'Настройка Родительской платы',
                'Настройка Опеки и попечительства',
                'Интеграция с медицинскими инф. системами',
                'Интеграция с ГИС ЕСКУ',
                'Техподдержка ГИС "Смета ЯНАО"',
                'Слияние баз',
                'Настройка контроля колич-х и качественных показателей обработки документов ИИ'
            ];
            
            // Парсим логи из загруженного контента
            const logs = {};
            
            // Ищем все div с id="log-1", "log-2" и т.д.
            for (let i = 1; i <= 12; i++) {
                const logRegex = new RegExp(`<div id="log-${i}"[^>]*>\\s*<h4[^>]*>.*?</h4>\\s*<ul>([\\s\\S]*?)</ul>`, 'i');
                const match = content.match(logRegex);
                
                if (match) {
                    // Извлекаем содержимое ul
                    const ulContent = match[1];
                    
                    // Извлекаем все li элементы
                    const liRegex = /<li[^>]*>(.*?)<\/li>/g;
                    const listItems = [];
                    let liMatch;
                    
                    while ((liMatch = liRegex.exec(ulContent)) !== null) {
                        const fullTag = liMatch[0];
                        let text = liMatch[1].trim();
                        
                        // Очищаем текст от HTML сущностей
                        text = text.replace(/&nbsp;/g, ' ').replace(/&mdash;/g, '—').replace(/&amp;/g, '&').trim();
                        
                        // Пропускаем пустые записи
                        if (!text || text === '' || text === ' ' || text.includes('nbsp')) {
                            continue;
                        }
                        
                        // Определяем класс
                        let className = '';
                        const classMatch = fullTag.match(/class\s*=\s*["']([^"']*)["']/);
                        if (classMatch) {
                            className = classMatch[1];
                        }
                        
                        listItems.push({
                            text: text,
                            className: className
                        });
                    }
                    
                    logs[i] = listItems;
                } else {
                    logs[i] = [];
                }
            }
            
            // Обновляем локальные логи
            for (let i = 1; i <= 12; i++) {
                const logElement = document.getElementById(`log-${i}`);
                if (logElement) {
                    // Обновляем заголовок
                    let h4 = logElement.querySelector('h4');
                    if (!h4) {
                        h4 = document.createElement('h4');
                        h4.style.display = 'none';
                        logElement.appendChild(h4);
                    }
                    h4.textContent = projectNames[i-1];
                    
                    // Обновляем список
                    let ul = logElement.querySelector('ul');
                    if (!ul) {
                        ul = document.createElement('ul');
                        logElement.appendChild(ul);
                    }
                    
                    ul.innerHTML = ''; // Очищаем
                    
                    if (logs[i] && logs[i].length > 0) {
                        logs[i].forEach(item => {
                            const li = document.createElement('li');
                            li.textContent = item.text;
                            if (item.className) {
                                li.className = item.className;
                            }
                            ul.appendChild(li);
                        });
                    }
                    // Не добавляем пустые li
                }
            }
            
            console.log('Логи загружены с GitHub');
            showNotification('📥 Логи загружены с GitHub', 'info');
            
            // Обновляем отображение если открыт какой-то проект
            if (typeof window.currentProjectId !== 'undefined' && window.currentProjectId) {
                const logElement = document.getElementById(`log-${window.currentProjectId}`);
                const logContent = document.getElementById('log-content');
                const tocLogDisplay = document.getElementById('toc-log-display');
                
                if (logElement && logContent && tocLogDisplay && tocLogDisplay.style.display === 'block') {
                    logContent.innerHTML = logElement.innerHTML;
                    const logLis = logContent.querySelectorAll('li');
                    logLis.forEach(li => {
                        if (li.className) {
                            li.classList.add(li.className);
                        }
                    });
                }
            }
            
        } catch (error) {
            console.error('Ошибка загрузки логов:', error);
        }
    }

    // ===== ФУНКЦИЯ СОХРАНЕНИЯ В GITHUB =====
    async function saveToGitHub(silent = false) {
        try {
            // 1. Получаем текущий файл с GitHub
            const getUrl = `https://api.github.com/repos/${GITHUB_REPO}/contents/${GITHUB_PATH}?ref=${GITHUB_BRANCH}`;
            
            const getResponse = await fetch(getUrl, {
                headers: {
                    'Authorization': `token ${GITHUB_TOKEN}`,
                    'Accept': 'application/vnd.github.v3+json'
                }
            });
            
            if (!getResponse.ok) {
                throw new Error('Не удалось получить файл с GitHub. Проверьте токен и репозиторий.');
            }
            
            const fileData = await getResponse.json();
            const sha = fileData.sha;
            
            // 2. Собираем текущие логи
            const logs = {};
            for (let i = 1; i <= 12; i++) {
                const logElement = document.getElementById(`log-${i}`);
                if (logElement) {
                    const ul = logElement.querySelector('ul');
                    if (ul) {
                        const items = [];
                        ul.querySelectorAll('li').forEach(li => {
                            const text = li.textContent.trim();
                            if (text && text !== '' && text !== '&nbsp;' && text !== '\u00A0') {
                                items.push({
                                    text: li.textContent,
                                    className: li.className || ''
                                });
                            }
                        });
                        logs[i] = items;
                    }
                }
            }
            
            // 3. Формируем новую секцию с логами
            let newLogSection = '<!-- Скрытый блок для логов мероприятий -->\n';
            newLogSection += '<div id="project-log-container" style="display: none;">\n';
            
            const projectNames = [
                'Интеграция с Тэзис',
                'Интеграция ЛК/Сметы с сервисом по предоставлению справок',
                'Интеграция c ГИС "Имущество"',
                'Интеграция c ГИС "АПК"',
                'Интеграция Росдормонитор',
                'Настройка Родительской платы',
                'Настройка Опеки и попечительства',
                'Интеграция с медицинскими инф. системами',
                'Интеграция с ГИС ЕСКУ',
                'Техподдержка ГИС "Смета ЯНАО"',
                'Слияние баз',
                'Настройка контроля колич-х и качественных показателей обработки документов ИИ'
            ];
            
            for (let i = 1; i <= 12; i++) {
                newLogSection += `    <div id="log-${i}" class="project-log">\n`;
                newLogSection += `        <h4 style="display: none;">${projectNames[i-1]}</h4>\n`;
                newLogSection += `        <ul>\n`;
                
                if (logs[i] && logs[i].length > 0) {
                    logs[i].forEach(item => {
                        const className = item.className ? ` class="${item.className}"` : '';
                        newLogSection += `            <li${className}>${item.text}</li>\n`;
                    });
                }
                
                newLogSection += `        </ul>\n`;
                newLogSection += `    </div>\n\n`;
            }
            
            newLogSection += `</div>\n`;
            
            // 4. Декодируем текущий контент и заменяем секцию
            const currentContent = decodeURIComponent(escape(atob(fileData.content)));
            
            // Ищем старую секцию
            const logSectionRegex = /<!-- Скрытый блок для логов мероприятий -->[\s\S]*?<\/div>\s*\n/;
            let newContent;
            
            if (logSectionRegex.test(currentContent)) {
                newContent = currentContent.replace(logSectionRegex, newLogSection);
            } else {
                const bodyEndRegex = /<\/body>/i;
                if (bodyEndRegex.test(currentContent)) {
                    newContent = currentContent.replace(bodyEndRegex, newLogSection + '\n</body>');
                } else {
                    newContent = currentContent + '\n\n' + newLogSection;
                }
            }
            
            // 5. Сохраняем на GitHub
            const updateUrl = `https://api.github.com/repos/${GITHUB_REPO}/contents/${GITHUB_PATH}`;
            
            const updateResponse = await fetch(updateUrl, {
                method: 'PUT',
                headers: {
                    'Authorization': `token ${GITHUB_TOKEN}`,
                    'Content-Type': 'application/json',
                    'Accept': 'application/vnd.github.v3+json'
                },
                body: JSON.stringify({
                    message: `📝 Обновление логов ${new Date().toLocaleString('ru-RU')}`,
                    content: btoa(unescape(encodeURIComponent(newContent))),
                    sha: sha,
                    branch: GITHUB_BRANCH
                })
            });
            
            if (!updateResponse.ok) {
                const error = await updateResponse.json();
                throw new Error(error.message || 'Ошибка сохранения');
            }
            
            if (!silent) {
                showNotification('✅ Логи сохранены на GitHub!', 'success');
            }
            
        } catch (error) {
            console.error('Ошибка:', error);
            if (!silent) {
                showNotification('❌ Ошибка: ' + error.message, 'error');
            }
            throw error;
        }
    }

    // ===== ФУНКЦИЯ ДОБАВЛЕНИЯ И СОХРАНЕНИЯ ЗАПИСИ =====
    async function addAndSaveToGitHub() {
        const date = document.getElementById('log-date').value.trim();
        const description = document.getElementById('log-description').value.trim();
        const status = document.getElementById('log-status').value;
        const addBtn = document.getElementById('add-save-btn');
        
        // Получаем ссылки на элементы внутри функции
        const tocLogDisplay = document.getElementById('toc-log-display');
        const logContent = document.getElementById('log-content');
        const statusPreview = document.getElementById('status-preview');
        
        if (!date || !description) {
            alert('Пожалуйста, заполните дату и описание');
            return;
        }
        
        try {
            addBtn.textContent = '⏳ Сохранение...';
            addBtn.disabled = true;
            
            // 1. Добавляем запись в локальный лог
            const logElement = document.getElementById(`log-${currentProjectId}`);
            
            if (!logElement) {
                throw new Error('Лог не найден');
            }
            
            let ul = logElement.querySelector('ul');
            if (!ul) {
                ul = document.createElement('ul');
                logElement.appendChild(ul);
            }
            
            const newLi = document.createElement('li');
            newLi.textContent = `${date} — ${description}`;
            
            if (status !== 'wait') {
                newLi.className = status;
            }
            
            ul.appendChild(newLi);
            
            // Функция сортировки записей по дате (новые сверху)
            function sortLogEntries(ul) {
                const items = Array.from(ul.children);
                items.sort((a, b) => {
                    const dateA = a.textContent.split(' — ')[0];
                    const dateB = b.textContent.split(' — ')[0];
                    // Преобразуем даты для сравнения (ДД.ММ.ГГГГ)
                    const parseDate = (dateStr) => {
                        const parts = dateStr.split(/[.\-]/);
                        if (parts.length === 3) {
                            const [day, month, year] = parts;
                            return new Date(year, month - 1, day);
                        }
                        return new Date(0); // Если дата не распарсилась
                    };
                    return parseDate(dateB) - parseDate(dateA);
                });
                
                ul.innerHTML = '';
                items.forEach(item => ul.appendChild(item));
            }
            
            // Сортируем записи
            sortLogEntries(ul);
            
            // 2. Обновляем отображение в TOC
            if (tocLogDisplay && tocLogDisplay.style.display === 'block' && logContent) {
                logContent.innerHTML = logElement.innerHTML;
                const logLis = logContent.querySelectorAll('li');
                logLis.forEach(li => {
                    if (li.className) {
                        li.classList.add(li.className);
                    }
                });
                
                // Вызываем функцию проверки прокрутки
                if (typeof window.checkScrollNeeded === 'function') {
                    window.checkScrollNeeded();
                }
                
                const scrollArea = document.querySelector('.log-scroll-area');
                if (scrollArea && scrollArea.classList.contains('scroll-active')) {
                    scrollArea.scrollTop = scrollArea.scrollHeight;
                }
            }
            
            // 3. Сохраняем на GitHub
            await saveToGitHub(true); // true = не показывать уведомление
            
            // 4. Очищаем форму
            document.getElementById('log-description').value = '';
            document.getElementById('log-status').value = 'wait';
            if (statusPreview) {
                statusPreview.className = 'status-preview wait';
                statusPreview.textContent = 'Не начато';
            }
            
            const today = new Date();
            const day = String(today.getDate()).padStart(2, '0');
            const month = String(today.getMonth() + 1).padStart(2, '0');
            const year = today.getFullYear();
            document.getElementById('log-date').value = `${day}.${month}.${year}`;
            
            showNotification('✅ Запись добавлена и сохранена на GitHub!');
            
        } catch (error) {
            console.error('Ошибка:', error);
            showNotification('❌ Ошибка: ' + error.message, 'error');
        } finally {
            addBtn.textContent = '💾 Добавить и сохранить';
            addBtn.disabled = false;
        }
    }

    // Ждём, пока сформируется правая колонка
    setTimeout(function() {
        // Находим правый сайдбар (TOC)
        const tocSidebar = document.querySelector('.md-sidebar--secondary .md-nav--secondary');
        if (!tocSidebar) return;
        
        // Функция проверки необходимости прокрутки
        window.checkScrollNeeded = function() {
            const logDisplay = document.getElementById('toc-log-display');
            const logContent = document.getElementById('log-content');
            const scrollArea = document.querySelector('.log-scroll-area');
            
            if (!logDisplay || logDisplay.style.display !== 'block' || !logContent || !scrollArea) return;
            
            scrollArea.classList.remove('scroll-active');
            
            setTimeout(() => {
                const logHeight = logContent.scrollHeight;
                const availableSpace = window.innerHeight - scrollArea.getBoundingClientRect().top - 300;
                
                if (logHeight > 300 || logHeight > availableSpace) {
                    scrollArea.classList.add('scroll-active');
                } else {
                    scrollArea.classList.remove('scroll-active');
                }
            }, 10);
        };
        
        // СОЗДАЁМ КОНТЕЙНЕР ДЛЯ ЛОГА И ФОРМЫ
        const logContainer = document.createElement('div');
        logContainer.id = 'toc-log-container';
        logContainer.innerHTML = `
            <div id="toc-log-display" style="display: none;">
                <h3 style="font-size: 16px; margin: 0 0 12px 0; color: #2c3e50; display: flex; align-items: center; gap: 8px;">
                    <span>📋 Ход работ</span>
                    <span id="current-project-name" style="font-weight: normal; font-size: 13px; color: #3498db;"></span>
                </h3>
                <div class="log-scroll-area">
                    <div id="log-content"></div>
                </div>
            </div>
            
            <!-- ФОРМА ДОБАВЛЕНИЯ НОВЫХ ЗАПИСЕЙ -->
            <div id="log-add-form-container" class="log-add-form">
                <div class="log-add-title">
                    <span>➕ Добавить запись</span>
                </div>
                
                <div class="form-grid">
                    <div class="form-group">
                        <label class="form-label">Дата</label>
                        <input type="text" id="log-date" class="form-input" placeholder="ДД.ММ.ГГГГ">
                    </div>
                    
                    <div class="form-group">
                        <label class="form-label">Статус</label>
                        <select id="log-status" class="form-select">
                            <option value="wait">Не начато</option>
                            <option value="work">В работе</option>
                            <option value="plan">Запланировано</option>
                            <option value="done">Выполнено</option>
                        </select>
                    </div>
                </div>
                
                <div class="form-group full-width">
                    <label class="form-label">Описание</label>
                    <input type="text" id="log-description" class="form-input textarea-like" placeholder="Что сделано">
                </div>
                
                <div id="status-preview" class="status-preview wait" style="margin-bottom: 12px;">Не начато</div>
                
                <!-- Кнопки -->
                <div class="form-actions">
                    <button id="add-save-btn" class="btn btn-primary" style="flex: 3;">💾 Добавить и сохранить</button>
                    <button id="clear-form-btn" class="btn btn-secondary" style="flex: 1;">Очистить</button>
                    <button id="load-github-btn" class="btn btn-info" style="flex: 1;">📥 Загрузить</button>
                </div>
                <div style="margin-top: 8px; font-size: 11px; color: #7f8c8d; text-align: center;">
                    ⚡ Одна кнопка: добавляет запись и сразу сохраняет на GitHub
                </div>
            </div>
        `;
        
        tocSidebar.appendChild(logContainer);
        
        // Загружаем логи с GitHub при открытии страницы
        setTimeout(() => {
            loadLogsFromGitHub();
        }, 1000);
        
        window.addEventListener('resize', window.checkScrollNeeded);
        
        // ===== ИНИЦИАЛИЗАЦИЯ КАЛЕНДАРЯ =====
        const dateInput = document.getElementById('log-date');
        if (dateInput) {
            const today = new Date();
            const day = String(today.getDate()).padStart(2, '0');
            const month = String(today.getMonth() + 1).padStart(2, '0');
            const year = today.getFullYear();
            dateInput.value = `${day}.${month}.${year}`;
            
            flatpickr(dateInput, {
                locale: 'ru',
                dateFormat: 'd.m.Y',
                defaultDate: 'today',
                allowInput: true,
                showMonths: 1,
                static: true
            });
        }
        
        // ===== ПЕРЕМЕННЫЕ ДЛЯ ТЕКУЩЕГО ПРОЕКТА =====
        let currentProjectId = 1;
        let currentProjectName = '';
        window.currentProjectId = currentProjectId;
        
        // ===== ОБНОВЛЕНИЕ ПРЕДПРОСМОТРА СТАТУСА =====
        const statusSelect = document.getElementById('log-status');
        const statusPreview = document.getElementById('status-preview');
        
        if (statusSelect && statusPreview) {
            statusSelect.addEventListener('change', function() {
                const status = this.value;
                const statusText = this.options[this.selectedIndex].text;
                statusPreview.className = 'status-preview ' + status;
                statusPreview.textContent = statusText;
            });
        }
        
        // ===== ОЧИСТКА ФОРМЫ =====
        const clearFormBtn = document.getElementById('clear-form-btn');
        if (clearFormBtn) {
            clearFormBtn.addEventListener('click', function() {
                const today = new Date();
                const day = String(today.getDate()).padStart(2, '0');
                const month = String(today.getMonth() + 1).padStart(2, '0');
                const year = today.getFullYear();
                dateInput.value = `${day}.${month}.${year}`;
                
                document.getElementById('log-description').value = '';
                document.getElementById('log-status').value = 'wait';
                statusPreview.className = 'status-preview wait';
                statusPreview.textContent = 'Не начато';
            });
        }
        
        // ===== ЛОГИКА КЛИКА ПО МЕРОПРИЯТИЯМ =====
        const projectCells = document.querySelectorAll('.project-table td:nth-child(2)');
        const tocLogDisplay = document.getElementById('toc-log-display');
        const logContent = document.getElementById('log-content');
        const currentProjectNameSpan = document.getElementById('current-project-name');
        
        projectCells.forEach((cell, index) => {
            if (!cell.querySelector('.log-icon')) {
                cell.style.cursor = 'pointer';
                cell.style.position = 'relative';
                cell.innerHTML = cell.innerHTML + ' <span class="log-icon" style="font-size: 12px; color: #3498db; margin-left: 5px;">📋</span>';
            }
            
            cell.addEventListener('click', function(e) {
                e.stopPropagation();
                
                const projectId = index + 1;
                const logElement = document.getElementById(`log-${projectId}`);
                let projectName = '';
                
                const cellText = cell.innerText.replace('📋', '').trim();
                projectName = cellText.split('\n')[0].trim();
                
                currentProjectId = projectId;
                window.currentProjectId = projectId;
                currentProjectName = projectName;
                
                if (currentProjectNameSpan) {
                    currentProjectNameSpan.textContent = `[${projectName}]`;
                }
                
                if (logElement) {
                    tocLogDisplay.style.display = 'block';
                    logContent.innerHTML = logElement.innerHTML;
                    
                    const logLis = logContent.querySelectorAll('li');
                    logLis.forEach(li => {
                        if (li.className) {
                            li.classList.add(li.className);
                        }
                    });
                    
                    window.checkScrollNeeded();
                }
            });
        });
        
        // ===== ОБРАБОТЧИК КНОПКИ ДОБАВЛЕНИЯ И СОХРАНЕНИЯ =====
        const addSaveBtn = document.getElementById('add-save-btn');
        if (addSaveBtn) {
            addSaveBtn.addEventListener('click', addAndSaveToGitHub);
        }
        
        // ===== ОБРАБОТЧИК КНОПКИ ЗАГРУЗКИ =====
        const loadBtn = document.getElementById('load-github-btn');
        if (loadBtn) {
            loadBtn.addEventListener('click', function() {
                loadLogsFromGitHub();
            });
        }
        
        // ===== СТИЛИ ДЛЯ ЛОГА И ФОРМЫ =====
        const style = document.createElement('style');
        style.textContent = `
            #toc-log-container {
                margin-top: 30px;
                padding: 0 12px;
                display: flex;
                flex-direction: column;
            }
            #toc-log-display {
                flex-shrink: 1;
                display: flex;
                flex-direction: column;
                min-height: 0;
                margin-bottom: 16px;
            }
            #toc-log-display h4 {
                font-size: 14px;
                margin: 8px 0 12px 0;
                color: #2c3e50;
            }
            #toc-log-display ul {
                padding-left: 24px;
                margin: 8px 0;
            }
            #toc-log-display li {
                margin-bottom: 8px;
                color: #4a5568;
                list-style-type: none;
                font-size: 13px;
            }
            .md-sidebar--secondary .md-nav--secondary {
                display: flex;
                flex-direction: column;
            }
            .log-add-form {
                flex-shrink: 0;
            }
            .project-table td:nth-child(2):hover {
                background-color: #ebf8ff !important;
            }
            .md-sidebar__scrollwrap {
                overflow: visible !important;
            }
            .md-sidebar--secondary::-webkit-scrollbar {
                display: none;
            }
        `;
        document.head.appendChild(style);
        
    }, 500);
});
</script>