/* Синхронизация статусов roadmap между всеми пользователями через /api/statuses */
(function () {
    'use strict';

    var API_URL = '/api/statuses';
    var POLL_INTERVAL_MS = 3000;
    var TABLE_SELECTOR = '#projectTable';
    var COLOR_COLUMNS_START = 2; // колонки с номером (0) и названием (1) не закрашиваем
    var STATUS_CLASSES = ['status-done', 'status-work', 'status-wait'];

    var lastJson = '';       // сериализованные данные, применённые последними
    var dropdown = null;
    var activeCell = null;

    function cellKey(rowIndex, colIndex) {
        return rowIndex + '_' + colIndex;
    }

    /* ---- чтение статуса ячейки из DOM ---- */
    function readStatus(cell) {
        for (var i = 0; i < STATUS_CLASSES.length; i++) {
            if (cell.classList.contains(STATUS_CLASSES[i])) {
                return STATUS_CLASSES[i].replace('status-', '');
            }
        }
        return null;
    }

    function setCellStatus(cell, status) {
        STATUS_CLASSES.forEach(function (c) { cell.classList.remove(c); });
        if (status && STATUS_CLASSES.indexOf('status-' + status) !== -1) {
            cell.classList.add('status-' + status);
        }
    }

    /* ---- применить объект статусов к таблице ---- */
    function applyToDom(table, statuses) {
        var rows = table.querySelectorAll('tbody tr');
        rows.forEach(function (row, rowIndex) {
            var cells = row.querySelectorAll('td');
            cells.forEach(function (cell, colIndex) {
                if (colIndex < COLOR_COLUMNS_START) return;
                var s = statuses[cellKey(rowIndex, colIndex)];
                if (s === undefined) {
                    setCellStatus(cell, null);
                } else if (readStatus(cell) !== s) {
                    setCellStatus(cell, s);
                }
            });
        });
    }

    /* ---- сеть ---- */
    function fetchStatuses() {
        return fetch(API_URL, { cache: 'no-store' })
            .then(function (r) { return r.ok ? r.json() : Promise.reject(new Error('HTTP ' + r.status)); });
    }

    function pushStatuses(statuses) {
        return fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(statuses),
            cache: 'no-store'
        }).then(function (r) { return r.ok ? r.json() : Promise.reject(new Error('HTTP ' + r.status)); });
    }

    function poll() {
        var table = document.querySelector(TABLE_SELECTOR);
        if (!table) return;
        if (activeCell) return; // не перетирать чужими данными во время редактирования

        fetchStatuses().then(function (data) {
            var json = JSON.stringify(data || {});
            if (json !== lastJson) {
                lastJson = json;
                applyToDom(table, data || {});
            }
        }).catch(function () {
            /* сервер ещё не запущен или временная ошибка — попробуем в следующий раз */
        });
    }

    /* ---- выпадающий выбор цвета ---- */
    function createDropdown() {
        var dd = document.createElement('div');
        dd.className = 'color-dropdown';
        dd.style.display = 'none';

        [
            { name: 'done', label: 'Выполнено' },
            { name: 'work', label: 'В работе' },
            { name: 'wait', label: 'Не начато' }
        ].forEach(function (color) {
            var option = document.createElement('div');
            option.className = 'color-option';
            option.dataset.color = color.name;
            option.title = color.label;
            dd.appendChild(option);
        });

        document.body.appendChild(dd);
        return dd;
    }

    function init() {
        var table = document.querySelector(TABLE_SELECTOR);
        if (!table) return;

        dropdown = createDropdown();

        // начальная загрузка состояния с сервера
        fetchStatuses().then(function (data) {
            lastJson = JSON.stringify(data || {});
            applyToDom(table, data || {});
        }).catch(function () {
            console.warn('roadmap-sync: сервер статусов недоступен, работаем локально');
        });

        setInterval(poll, POLL_INTERVAL_MS);

        table.addEventListener('click', function (e) {
            var cell = e.target.closest('td');
            if (!cell) return;

            var cells = Array.from(cell.parentElement.children);
            var colIndex = cells.indexOf(cell);
            if (colIndex < COLOR_COLUMNS_START) return;

            e.stopPropagation();

            if (activeCell === cell && dropdown.style.display === 'flex') {
                dropdown.style.display = 'none';
                activeCell = null;
                return;
            }

            cell.classList.remove('highlight-red');
            activeCell = cell;

            var rect = cell.getBoundingClientRect();
            dropdown.style.display = 'flex';
            dropdown.style.left = (rect.left + window.scrollX) + 'px';
            dropdown.style.top = (rect.bottom + window.scrollY + 4) + 'px';
        });

        dropdown.addEventListener('click', function (e) {
            var option = e.target.closest('.color-option');
            if (!option || !activeCell) return;

            setCellStatus(activeCell, option.dataset.color);

            var rows = Array.from(table.querySelectorAll('tbody tr'));
            var rowIndex = rows.indexOf(activeCell.parentElement);
            var colIndex = Array.from(activeCell.parentElement.children).indexOf(activeCell);

            // обновляем локальную копию и сохраняем на сервер
            var current = JSON.parse(lastJson || '{}');
            var key = cellKey(rowIndex, colIndex);
            if (option.dataset.color === 'wait') {
                delete current[key];
            } else {
                current[key] = option.dataset.color;
            }
            lastJson = JSON.stringify(current);
            pushStatuses(current).catch(function (err) {
                console.warn('roadmap-sync: не удалось сохранить:', err);
            });

            dropdown.style.display = 'none';
            activeCell = null;
        });

        document.addEventListener('click', function (e) {
            if (!dropdown.contains(e.target) && !e.target.closest(TABLE_SELECTOR)) {
                dropdown.style.display = 'none';
                activeCell = null;
            }
        });

        window.addEventListener('scroll', function () {
            dropdown.style.display = 'none';
            activeCell = null;
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
