# План проектов на 2026 год

<style>
/* ===== ЛЕГЕНДА ===== */
.legend {
    display: flex;
    gap: 20px;
    margin-bottom: 20px;
    flex-wrap: wrap;
}
.legend-item {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 13px;
}
.legend-color {
    width: 20px;
    height: 20px;
    border-radius: 4px;
}
.legend-color.done { background-color: #90ee90; }
.legend-color.work { background-color: #f0e085; }
.legend-color.wait { background-color: #ffffff; border: 1px solid #ccc; }

/* ===== ЦВЕТА СТАТУСОВ ===== */
.status-done { background-color: #90ee90 !important; }
.status-work { background-color: #f0e085 !important; }
.status-wait { background-color: #ffffff !important; }

/* ===== ТАБЛИЦА ===== */
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

/* ===== ОСТАЛЬНЫЕ ЗАГОЛОВКИ — ВЕРТИКАЛЬНЫЕ С ПЕРЕНОСОМ ===== */
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

/* ===== ЯЧЕЙКИ ===== */
.project-table td {
    padding: 6px 3px;
    border: 1px solid #e0e4e8;
    vertical-align: middle;
    height: 40px;
    word-wrap: break-word;
    background-color: #ffffff;
    cursor: pointer;
    transition: background-color 0.15s ease;
    position: relative;
}

/* ===== ШИРИНА КОЛОНОК ===== */
.project-table th:nth-child(1) { width: 38px; }
.project-table td:nth-child(1) {
    width: 28px;
    text-align: center;
    font-weight: 500;
    font-size: 11px;
    cursor: default;
}

.project-table th:nth-child(2) { width: 200px; }
.project-table td:nth-child(2) {
    width: 250px;
    padding-left: 8px;
    font-weight: normal;
    white-space: normal;
    font-size: 12px;
    cursor: default;
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

/* ===== КРАСНАЯ РАМКА ===== */
.highlight-red {
    outline: 2px solid #e74c3c;
    outline-offset: -2px;
}

/* ===== ВЫПАДАЮЩИЙ СПИСОК ЦВЕТОВ ===== */
.color-dropdown {
    position: absolute;
    z-index: 1000;
    background: #fff;
    border: 1px solid #ccc;
    border-radius: 6px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    padding: 6px;
    display: flex;
    gap: 6px;
}
.color-dropdown .color-option {
    width: 24px;
    height: 24px;
    border-radius: 4px;
    cursor: pointer;
    border: 1px solid #ddd;
    transition: transform 0.1s;
}
.color-dropdown .color-option:hover {
    transform: scale(1.15);
}
.color-option[data-color="done"] { background-color: #90ee90; }
.color-option[data-color="work"] { background-color: #f0e085; }
.color-option[data-color="wait"] { background-color: #ffffff; }
</style>

<div class="legend">
    <div class="legend-item">
        <div class="legend-color done"></div>
        <span>Выполнено</span>
    </div>
    <div class="legend-item">
        <div class="legend-color work"></div>
        <span>В работе</span>
    </div>
    <div class="legend-item">
        <div class="legend-color wait"></div>
        <span>Не начато</span>
    </div>
</div>

<table class="project-table" id="projectTable">
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
            <td>1</td>
            <td>Интеграция с Тэзис</td>
            <td class="status-done highlight-red">10.02.26<br>Ставер</td>
            <td class="status-work">01.03.26</td>
            <td>15.03.26</td>
            <td>01.04.26</td>
            <td>20.04.26</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Интеграция ЛК/Сметы с сервисом по предоставлению справок</td>
            <td class="status-done">05.02.26<br>Сапогов</td>
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
            <td class="status-done">08.02.26<br>Сапогов</td>
            <td class="status-work">25.02.26<br>Сапогов</td>
            <td>12.03.26</td>
            <td>28.03.26</td>
            <td>18.04.26</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Настройка Родительской платы</td>
            <td>15.02.26</td>
            <td>08.03.26</td>
            <td>25.03.26</td>
            <td>12.04.26</td>
            <td>05.05.26</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Настройка Опеки и попечительства</td>
            <td>18.02.26<br>Сапогов</td>
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
            <td class="status-done">25.02.26</td>
            <td class="status-done">20.03.26</td>
            <td class="status-done">10.04.26</td>
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

<script>
(function() {
    const STORAGE_KEY = 'roadmap_statuses_v2';
    const TABLE_SELECTOR = '#projectTable';
    const CELL_SELECTOR = 'td';
    const COLOR_COLUMNS_START = 3;

    function loadStatuses() {
        try {
            const raw = localStorage.getItem(STORAGE_KEY);
            return raw ? JSON.parse(raw) : {};
        } catch (e) {
            console.warn('Не удалось загрузить статусы:', e);
            return {};
        }
    }

    function saveStatuses(statuses) {
        try {
            localStorage.setItem(STORAGE_KEY, JSON.stringify(statuses));
        } catch (e) {
            console.warn('Не удалось сохранить статусы:', e);
        }
    }

    function applySavedStatuses() {
        const statuses = loadStatuses();
        const table = document.querySelector(TABLE_SELECTOR);
        if (!table) return;

        const rows = table.querySelectorAll('tbody tr');
        rows.forEach((row, rowIndex) => {
            const cells = row.querySelectorAll(CELL_SELECTOR);
            cells.forEach((cell, colIndex) => {
                if (colIndex < COLOR_COLUMNS_START - 1) return;
                const key = rowIndex + '_' + colIndex;
                if (statuses[key]) {
                    cell.classList.remove('status-done', 'status-work', 'status-wait');
                    cell.classList.add('status-' + statuses[key]);
                }
            });
        });
    }

    function createDropdown() {
        const dropdown = document.createElement('div');
        dropdown.className = 'color-dropdown';
        dropdown.style.display = 'none';

        const colors = [
            { name: 'done', label: 'Выполнено' },
            { name: 'work', label: 'В работе' },
            { name: 'wait', label: 'Не начато' }
        ];

        colors.forEach(color => {
            const option = document.createElement('div');
            option.className = 'color-option';
            option.dataset.color = color.name;
            option.title = color.label;
            dropdown.appendChild(option);
        });

        document.body.appendChild(dropdown);
        return dropdown;
    }

    document.addEventListener('DOMContentLoaded', function() {
        const table = document.querySelector(TABLE_SELECTOR);
        if (!table) return;

        const dropdown = createDropdown();
        let activeCell = null;

        applySavedStatuses();

        table.addEventListener('click', function(e) {
            const cell = e.target.closest('td');
            if (!cell) return;

            const row = cell.parentElement;
            const cells = Array.from(row.children);
            const colIndex = cells.indexOf(cell);

            if (colIndex < COLOR_COLUMNS_START - 1) return;

            e.stopPropagation();

            if (activeCell === cell && dropdown.style.display === 'flex') {
                dropdown.style.display = 'none';
                activeCell = null;
                return;
            }

            cell.classList.remove('highlight-red');
            activeCell = cell;

            const rect = cell.getBoundingClientRect();
            dropdown.style.display = 'flex';
            dropdown.style.left = (rect.left + window.scrollX) + 'px';
            dropdown.style.top = (rect.bottom + window.scrollY + 4) + 'px';
        });

        dropdown.addEventListener('click', function(e) {
            const option = e.target.closest('.color-option');
            if (!option || !activeCell) return;

            const color = option.dataset.color;

            activeCell.classList.remove('status-done', 'status-work', 'status-wait');
            activeCell.classList.add('status-' + color);

            const table = document.querySelector(TABLE_SELECTOR);
            const rows = Array.from(table.querySelectorAll('tbody tr'));
            const rowIndex = rows.indexOf(activeCell.parentElement);
            const colIndex = Array.from(activeCell.parentElement.children).indexOf(activeCell);
            const key = rowIndex + '_' + colIndex;

            const statuses = loadStatuses();
            statuses[key] = color;
            saveStatuses(statuses);

            dropdown.style.display = 'none';
            activeCell = null;
        });

        document.addEventListener('click', function(e) {
            if (!dropdown.contains(e.target) && !e.target.closest(TABLE_SELECTOR)) {
                dropdown.style.display = 'none';
                activeCell = null;
            }
        });

        window.addEventListener('scroll', function() {
            dropdown.style.display = 'none';
            activeCell = null;
        });
    });
})();
</script>