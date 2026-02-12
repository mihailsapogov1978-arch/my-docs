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

/* ===== УБИРАЕМ МАРКЕРЫ ТОЛЬКО У ЛОГА ===== */
#toc-log-display ul {
    list-style-type: none !important;
    padding-left: 0 !important;
}

#toc-log-display li {
    list-style-type: none !important;
    padding-left: 0 !important;
}

</style>

<!-- ЛЕГЕНДА -->
<div class="legend">
    <div class="legend-item"><span class="legend-color done"></span> Выполнено</div>
    <div class="legend-item"><span class="legend-color work"></span> В работе</div>
    <div class="legend-item"><span class="legend-color wait"></span> Не начато</div>
</div>


<!-- Скрытый блок для логов мероприятий -->
<div id="project-log-container" style="display: none;">
    <div id="log-1" class="project-log">
        <h4>Интеграция с Тэзис</h4>
        <ul>
            <li>02.10.25 — Провели ВКС, условились использовать СНИЛС как идентификатор</li>
            <li>15.10.25 — Направлен проект ТЗ на согласование</li>
            <li>25.10.25 — Получены замечания от заказчика</li>
            <li>05.11.25 — Доработано ТЗ, повторное согласование</li>
            <li>20.11.25 — ТЗ утверждено</li>
            <li>10.12.25 — Старт разработки</li>
            <li>15.01.26 — Готово к тестированию</li>
        </ul>
    </div>
    
    <div id="log-2" class="project-log">
        <h4>Интеграция ЛК/Сметы с сервисом по предоставлению справок</h4>
        <ul>
            <li>05.12.25 — ВКС с заказчиком</li>
            <li>18.12.25 — Определены форматы обмена</li>
            <li>25.01.26 — Подготовлен прототип</li>
            <li>01.02.26 — Начало интеграционных тестов</li>
        </ul>
    </div>
    
    <!-- Добавьте аналогично для всех 12 проектов -->
    <div id="log-3" class="project-log">
        <h4>Интеграция имущества</h4>
        <ul>
            <li>10.01.26 — Старт проекта</li>
            <li>25.01.26 — Согласование API</li>
        </ul>
    </div>
    
    <!-- И так далее до log-12 -->
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
        <td class = "status-done tooltip">05.02.26<br>Сапогов
          <span class="tooltip-text">
            <strong>Этап 1. Согласование постановки задачи</strong><br>
            Ответственный: Ставер<br>
            Срок: 10.02.2026<br>
            Статус: Выполнено
          </span>
        </td>
        <td class = "status-work">20.02.26<br>Сапогов</a></td>
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
        <td>Интеграция Росдормонитор</td>
        <td class = "status-work">08.02.26<br>Сапогов</td>
        <td class = "status-work">25.02.26<br>Сапогов</td>
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
        <td>Настройка контроля колич-х и качественных показателей обработки документов ИИ</td>
        <td class = "status-work">15.03.26<br>Ставер</td>
        <td>08.04.26</td>
        <td>28.04.26</td>
        <td>18.05.26</td>
        <td>08.06.26</td>
    </tr>
</tbody>
</table>


<script>
document.addEventListener('DOMContentLoaded', function() {
    // Находим все ячейки с названиями мероприятий (вторая колонка)
    const projectCells = document.querySelectorAll('.project-table td:nth-child(2)');
    const tocLogDisplay = document.getElementById('toc-log-display');
    const logContent = document.getElementById('log-content');
    
    // Добавляем каждой ячейке стиль "кликабельности"
    projectCells.forEach((cell, index) => {
        cell.style.cursor = 'pointer';
        cell.style.position = 'relative';
        
        // Добавляем иконку для наглядности
        cell.innerHTML = cell.innerHTML + ' <span style="font-size: 11px; color: #3498db; margin-left: 5px;"></span>';
        
        // Обработчик клика
        cell.addEventListener('click', function(e) {
            e.stopPropagation();
            
            // Номер проекта (индекс + 1)
            const projectId = index + 1;
            
            // Получаем лог проекта
            const logElement = document.getElementById(`log-${projectId}`);
            
            if (logElement) {
                // Показываем контейнер лога
                tocLogDisplay.style.display = 'block';
                
                // Вставляем содержимое лога
                logContent.innerHTML = logElement.innerHTML;
                
                // Прокручиваем к TOC (правой колонке)
                const tocSidebar = document.querySelector('.md-sidebar--secondary');
                if (tocSidebar) {
                    tocSidebar.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            }
        });
    });
    
    // Добавляем стили для TOC-лога в правую колонку
    const style = document.createElement('style');
    style.textContent = `
        .md-sidebar--secondary .md-nav--secondary {
            max-height: none !important;
        }
        .md-sidebar--secondary .md-nav__title {
            margin-bottom: 8px;
        }
        #toc-log-display {
            margin-top: 20px;
            padding: 0 12px;
            font-size: 12px;
        }
        #toc-log-display h4 {
            font-size: 13px;
            margin-bottom: 10px;
            color: #2c3e50;
            border-bottom: 1px solid #eee;
            padding-bottom: 5px;
        }
        #toc-log-display ul {
            padding-left: 20px;
            margin: 0;
        }
        #toc-log-display li {
            margin-bottom: 6px;
            line-height: 1.4;
            color: #555;
            list-style-type: disc;
        }
        .project-table td:nth-child(2):hover {
            background-color: #f0f7ff !important;
            transition: background-color 0.2s;
        }
    `;
    document.head.appendChild(style);
});
</script>
<script>
document.addEventListener('DOMContentLoaded', function() {
    // Ждём, пока сформируется правая колонка
    setTimeout(function() {
        // Находим правый сайдбар (TOC)
        const tocSidebar = document.querySelector('.md-sidebar--secondary .md-nav--secondary');
        if (!tocSidebar) return;
        
        // Создаём контейнер для лога
        const logContainer = document.createElement('div');
        logContainer.id = 'toc-log-container';
        logContainer.innerHTML = `
            <div id="toc-log-display" style="display: none;">
                <h3 style="font-size: 14px; margin-bottom: 12px; color: #2c3e50; display: flex; align-items center; gap: 6px;">
                    <span>Ход работ</span>
                </h3>
                <div id="log-content" style="font-size: 12px; line-height: 1.5;"></div>
            </div>
        `;
        
        // Добавляем лог ПОСЛЕ оглавления
        tocSidebar.appendChild(logContainer);
        
        // ===== ЛОГИКА КЛИКА ПО МЕРОПРИЯТИЯМ =====
        const projectCells = document.querySelectorAll('.project-table td:nth-child(2)');
        const tocLogDisplay = document.getElementById('toc-log-display');
        const logContent = document.getElementById('log-content');
        
        // Добавляем иконки и обработчики
        projectCells.forEach((cell, index) => {
            // Добавляем иконку если её нет
            if (!cell.querySelector('.log-icon')) {
                cell.style.cursor = 'pointer';
                cell.style.position = 'relative';
                cell.innerHTML = cell.innerHTML + ' <span class="log-icon" style="font-size: 11px; color: #3498db; margin-left: 5px;"></span>';
            }
            
            cell.addEventListener('click', function(e) {
                e.stopPropagation();
                
                const projectId = index + 1;
                const logElement = document.getElementById(`log-${projectId}`);
                
                if (logElement) {
                    tocLogDisplay.style.display = 'block';
                    logContent.innerHTML = logElement.innerHTML;
                    
                    // Плавный скролл к логу
                    setTimeout(() => {
                        tocLogDisplay.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                    }, 100);
                }
            });
        });
        
        // Стили для лога в TOC
        const style = document.createElement('style');
        style.textContent = `
            #toc-log-container {
                margin-top: 30px;
                padding: 0 8px;
            }
            #toc-log-display h4 {
                font-size: 13px;
                margin: 0 0 12px 0;
                color: #2c3e50;
                border-bottom: 1px solid #e0e4e8;
                padding-bottom: 6px;
            }
            #toc-log-display ul {
                padding-left: 20px;
                margin: 0;
            }
            #toc-log-display li {
                margin-bottom: 8px;
                color: #4a5568;
                list-style-type: disc;
            }
            .md-sidebar--secondary .md-nav--secondary {
                display: flex;
                flex-direction: column;
            }
        `;
        document.head.appendChild(style);
        
    }, 500); // Ждём полсекунды, чтобы MkDocs построил TOC
});
</script>