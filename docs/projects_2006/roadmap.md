# План проектов на 2026 год

<style>
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
.legend-color.wait { background-color: #ffffff; border: 1px solid #ccc; }

.status-done { background-color: #90ee90 !important; }  /* ЗЕЛЁНЫЙ */
.status-work { background-color: #f0e085 !important; } /* ЖЁЛТЫЙ */
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
</style>

<!-- ЛЕГЕНДА -->
<div class="legend">
    <div class="legend-item"><span class="legend-color done"></span> Выполнено</div>
    <div class="legend-item"><span class="legend-color work"></span> В работе</div>
    <div class="legend-item"><span class="legend-color wait"></span> Не начато</div>
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
        <td class = "status-work">10.02.26<br>Ставер</td>
        <td>01.03.26</td>
        <td>15.03.26</td>
        <td>01.04.26</td>
        <td>20.04.26</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Интеграция ЛК/Сметы с сервисом по предоставлению справок</td>
        <td class = "status-work">05.02.26<br>Сапогов</td>
        <td>20.02.26</td>
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
        <td class = "status-work">01.02.26<br>Гасанов</td>
        <td>18.02.26</td>
        <td>05.03.26</td>
        <td>22.03.26</td>
        <td>12.04.26</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Интеграция Росдорм</td>
        <td class = "status-work">08.02.26<br>Сапогов</td>
        <td>25.02.26</td>
        <td>12.03.26</td>
        <td>28.03.26</td>
        <td>18.04.26</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Настройка Родительской платы</td>
        <td class = "status-work">15.02.26</td>
        <td>08.03.26</td>
        <td>25.03.26</td>
        <td>12.04.26</td>
        <td>05.05.26</td>
    </tr>
    <tr>
        <td>7</td>
        <td>Настройка Опеки и попечительства</td>
        <td class = "status-work">18.02.26<br>Сапогов</td>
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
        <td>10.03.26</td>
        <td>05.04.26</td>
        <td>25.04.26</td>
        <td>15.05.26</td>
        <td>05.06.26</td>
    </tr>
    <tr>
        <td>12</td>
        <td>Настройка функции контроля количественных и качественных показателей обработки документов ИИ</td>
        <td class = "status-work">15.03.26<br>Ставер</td>
        <td>08.04.26</td>
        <td>28.04.26</td>
        <td>18.05.26</td>
        <td>08.06.26</td>
    </tr>
</tbody>
</table>



