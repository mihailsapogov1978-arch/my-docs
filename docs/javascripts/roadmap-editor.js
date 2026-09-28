/**
 * Редактор карты мероприятий (roadmap).
 *
 * Клик по ячейке таблицы .project-table открывает режим редактирования:
 * можно менять текст и цвет статуса. Сохранение (✓) отправляет PATCH-запрос
 * на dev-сервер mkdocs (плагин mkdocs-roadmap-save), который изменяет
 * исходный файл docs/projects_2026/roadmap.md. Mkdocs live-reload ловит
 * изменение файла и пересобирает сайт — обновления получают ВСЕ клиенты
 * (достаточно F5 или встроенного live-reload).
 *
 * На продакшн-сайте (GitHub Pages) endpoint недоступен — там редактор
 * работает в локальном режиме localStorage (виден только на вашей машине).
 */
(function () {
    'use strict';

    var STATUS_CLASSES = ['status-done', 'status-work', 'status-plan', 'status-wait'];
    var STATUS_LABELS = {
        'status-done': 'Выполнено',
        'status-work': 'В работе',
        'status-plan': 'Запланировано',
        'status-wait': 'Не начато'
    };

    var editingCell = null;      // текущая редактируемая td
    var originalHTML = '';        // исходное содержимое ячейки
    var toolbar = null;           // панель инструментов

    function getTable() {
        return document.querySelector('table.project-table');
    }

    // ---------- координаты ячейки в исходном markdown ----------
    function cellPosition(table, td) {
        var tr = td.parentNode;
        var rows = Array.prototype.slice.call(table.querySelectorAll('tbody tr'));
        var rowIndex = rows.indexOf(tr);
        var cells = Array.prototype.slice.call(tr.children);
        var colIndex = cells.indexOf(td);
        if (rowIndex < 0 || colIndex < 0) return null;
        return { row: rowIndex + 1, col: colIndex + 1 }; // 1-based
    }

    // ---------- панель инструментов цвета ----------
    function buildToolbar() {
        toolbar = document.createElement('div');
        toolbar.className = 'roadmap-toolbar';
        toolbar.style.cssText =
            'position:absolute;z-index:9999;display:none;background:#fff;' +
            'border:1px solid #ccc;border-radius:8px;padding:6px 8px;' +
            'box-shadow:0 4px 12px rgba(0,0,0,.25);font-size:12px;' +
            'display:none;align-items:center;gap:6px;font-family:inherit;';

        STATUS_CLASSES.forEach(function (cls) {
            var btn = document.createElement('button');
            btn.type = 'button';
            btn.textContent = STATUS_LABELS[cls];
            btn.dataset.status = cls;
            btn.title = 'Цвет: ' + STATUS_LABELS[cls];
            btn.style.cssText =
                'cursor:pointer;border:1px solid #bbb;border-radius:4px;' +
                'padding:2px 6px;margin:0 2px;font-size:11px;background:' +
                ({ 'status-done': '#90ee90', 'status-work': '#f0e085',
                   'status-plan': '#bde0fe', 'status-wait': '#ffffff' })[cls];
            btn.addEventListener('mousedown', function (e) {
                e.preventDefault();
                applyStatus(cls);
            });
            toolbar.appendChild(btn);
        });

        var sep = document.createElement('span');
        sep.textContent = '|';
        sep.style.color = '#aaa';
        toolbar.appendChild(sep);

        toolbar.appendChild(makeActionBtn('✕', 'Отмена', cancelEdit));
        toolbar.appendChild(makeActionBtn('✓', 'Сохранить', saveEdit));

        document.body.appendChild(toolbar);
    }

    function makeActionBtn(text, title, handler) {
        var b = document.createElement('button');
        b.type = 'button';
        b.textContent = text;
        b.title = title;
        b.style.cssText =
            'cursor:pointer;border:1px solid #3f51b5;border-radius:4px;' +
            'padding:2px 8px;margin:0 2px;font-weight:bold;color:#3f51b5;background:#fff;';
        b.addEventListener('mousedown', function (e) {
            e.preventDefault();
            handler();
        });
        return b;
    }

    var pendingStatus = null;

    function applyStatus(cls) {
        pendingStatus = cls;
        if (editingCell) {
            STATUS_CLASSES.forEach(function (c) { editingCell.classList.remove(c); });
            if (cls !== 'status-wait') editingCell.classList.add(cls);
        }
    }

    // ---------- редактирование ----------
    function startEdit(td) {
        if (editingCell === td) return;
        if (editingCell) cancelEdit();

        editingCell = td;
        pendingStatus = null;
        originalHTML = td.innerHTML;
        td.classList.add('cell-editing');
        td.contentEditable = 'true';
        td.focus();

        // выделяем текст целиком для быстрой замены
        try {
            var range = document.createRange();
            range.selectNodeContents(td);
            var sel = window.getSelection();
            sel.removeAllRanges();
            sel.addRange(range);
        } catch (e) { /* ignore */ }

        positionToolbar(td);
        toolbar.style.display = 'flex';
    }

    function positionToolbar(td) {
        var r = td.getBoundingClientRect();
        toolbar.style.top = (r.bottom + window.scrollY + 4) + 'px';
        toolbar.style.left = Math.max(4, r.left + window.scrollX - 4) + 'px';
    }

    function cleanup() {
        if (!editingCell) return;
        editingCell.contentEditable = 'false';
        editingCell.classList.remove('cell-editing');
        editingCell = null;
        pendingStatus = null;
        if (toolbar) toolbar.style.display = 'none';
    }

    function cancelEdit() {
        if (!editingCell) return;
        var html = originalHTML;
        var cell = editingCell;
        cleanup();
        cell.innerHTML = html;
    }

    function saveEdit() {
        if (!editingCell) return;
        var table = getTable();
        var pos = cellPosition(table, editingCell);
        var content = editingCell.innerHTML;
        var statusCls = pendingStatus || getCurrentStatus(editingCell);

        cleanup();

        // нормализуем: <br> оставляем, вычищаем служебные обёртки
        content = normalizeCellHTML(content);

        // 1. мгновенно обновляем DOM (для себя)
        editingDomRefresh(table, pos, content, statusCls);

        // 2. сохраняем в исходник roadmap.md через dev-сервер
        persistToSource(pos, content, statusCls);
    }

    function getCurrentStatus(td) {
        for (var i = 0; i < STATUS_CLASSES.length; i++) {
            if (td.classList.contains(STATUS_CLASSES[i])) return STATUS_CLASSES[i];
        }
        return 'status-wait';
    }

    function normalizeCellHTML(html) {
        var div = document.createElement('div');
        div.innerHTML = html;
        // убираем span-обёртки от contenteditable, сохраняя переводы строк
        var out = '';
        Array.prototype.slice.call(div.childNodes).forEach(function (node) {
            if (node.nodeType === 3) {
                out += node.textContent.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
            } else if (node.nodeName === 'BR') {
                out += '<br>';
            } else {
                out += (node.textContent || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
            }
        });
        return out.trim();
    }

    function editingDomRefresh(table, pos, content, statusCls) {
        if (!table || !pos) return;
        var tr = table.querySelectorAll('tbody tr')[pos.row - 1];
        if (!tr) return;
        var td = tr.children[pos.col - 1];
        if (!td) return;
        td.innerHTML = content;
        STATUS_CLASSES.forEach(function (c) { td.classList.remove(c); });
        if (statusCls !== 'status-wait') td.classList.add(statusCls);
    }

    function persistToSource(pos, content, statusCls) {
        var payload = JSON.stringify({
            row: pos.row,
            col: pos.col,
            html: content,
            status: statusCls
        });

        // учитываем корень сайта (dev_addr + use_directory_urls), чтобы
        // запрос шёл на тот же origin и через тот же префикс /my-docs/
        var base = (window.__md_scope && window.__md_scope.pathname) || '/';
        fetch(base.replace(/\/$/, '') + '/_roadmap/save', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: payload
        }).then(function (resp) {
            if (resp.ok) {
                flashSaved('✓ Сохранено в roadmap.md — у коллег обновится автоматически');
            } else {
                throw new Error('HTTP ' + resp.status);
            }
        }).catch(function () {
            // fallback: сервер недоступен (prod / не установлен плагин) —
            // сохраняем локально, изменения видны только на этой машине
            saveLocal(pos, content, statusCls);
            flashSaved('⚠ Dev-сервер недоступен — изменения сохранены только локально (в браузере)');
        });
    }

    // ---------- локальный fallback (localStorage) ----------
    function localKey() {
        return 'roadmap-overrides-v1';
    }

    function loadLocal() {
        try {
            return JSON.parse(localStorage.getItem(localKey()) || '{}');
        } catch (e) { return {}; }
    }

    function saveLocal(pos, content, statusCls) {
        var data = loadLocal();
        data[pos.row + ':' + pos.col] = { html: content, status: statusCls };
        try { localStorage.setItem(localKey(), JSON.stringify(data)); } catch (e) { /* ignore */ }
    }

    function applyLocalOverrides() {
        var table = getTable();
        if (!table) return;
        var data = loadLocal();
        Object.keys(data).forEach(function (key) {
            var parts = key.split(':');
            var tr = table.querySelectorAll('tbody tr')[parseInt(parts[0], 10) - 1];
            if (!tr) return;
            var td = tr.children[parseInt(parts[1], 10) - 1];
            if (!td) return;
            td.innerHTML = data[key].html;
            STATUS_CLASSES.forEach(function (c) { td.classList.remove(c); });
            if (data[key].status && data[key].status !== 'status-wait') {
                td.classList.add(data[key].status);
            }
        });
    }

    // ---------- уведомление ----------
    var flashTimer = null;
    function flashSaved(msg) {
        var el = document.getElementById('roadmap-flash');
        if (!el) {
            el = document.createElement('div');
            el.id = 'roadmap-flash';
            el.style.cssText =
                'position:fixed;bottom:20px;left:50%;transform:translateX(-50%);' +
                'background:#323232;color:#fff;padding:8px 16px;border-radius:6px;' +
                'font-size:13px;z-index:10000;box-shadow:0 2px 8px rgba(0,0,0,.3);';
            document.body.appendChild(el);
        }
        el.textContent = msg;
        el.style.display = 'block';
        clearTimeout(flashTimer);
        flashTimer = setTimeout(function () { el.style.display = 'none'; }, 3500);
    }

    // ---------- инициализация ----------
    function init() {
        var table = getTable();
        if (!table) return;

        buildToolbar();
        applyLocalOverrides();

        table.addEventListener('click', function (e) {
            var td = e.target.closest('tbody td');
            if (!td) return;
            // колонки № и «Мероприятие» тоже редактируем — это безопасно
            startEdit(td);
        });

        document.addEventListener('keydown', function (e) {
            if (!editingCell) return;
            if (e.key === 'Escape') { cancelEdit(); }
            if (e.key === 'Enter' && !e.shiftKey && editingCell === document.activeElement) {
                e.preventDefault();
                saveEdit();
            }
        });

        // клик вне ячейки/панели — отмена
        document.addEventListener('mousedown', function (e) {
            if (!editingCell) return;
            if (editingCell.contains(e.target)) return;
            if (toolbar && toolbar.contains(e.target)) return;
            cancelEdit();
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
