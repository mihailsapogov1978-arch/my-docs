# Ежедневник

Форма для внесения ежемесячных отчетов о выполненной работе. Заполните и нажмите «Сохранить».

<form id="daily-form" class="daily-form">
    <label id="df-employee-label">
        Сотрудник
        <select id="df-employee" required>
            <option value="">— выберите —</option>
            <option data-slug="staver"     value="Ставер">Ставер</option>
            <option data-slug="sapogov"    value="Сапогов">Сапогов</option>
            <option data-slug="mulyavin"   value="Мулявин">Мулявин</option>
            <option data-slug="chechetkin" value="Чечеткин">Чечеткин</option>
            <option data-slug="roganova"   value="Роганова">Роганова</option>
            <option data-slug="obmolova"   value="Обмолова">Обмолова</option>
            <option data-slug="koshik"     value="Кошик">Кошик</option>
            <option data-slug="gasanov"    value="Гасанов">Гасанов</option>
            <option data-slug="hudyshkin"  value="Худышкин">Худышкин</option>
        </select>
    </label>

    <label>
        Дата
        <input type="date" id="df-date" required>
        <small id="df-date-hint" style="color:#718096;font-size:11px;"></small>
    </label>

    <label>
        Что сделал (одна строка — одна задача)
        <textarea id="df-text" rows="8" required
            placeholder="Обработал 6 обращений МО по ошибкам ЕСКУ–Смета. Закрыл 4, 2 передал в НПО «Криста»."></textarea>
    </label>

    <details class="df-example">
        <summary>Показать пример заполнения</summary>
        <ol>
            <li>Написано инструкций и выложено на сайт ЦБ ОГВ — 3.</li>
            <li>Настройка ЭДО Астрал для Департамента тарифной политики — 1.</li>
            <li>Оформлено МЧД в ФНС, Росстат для Департамента тарифной политики — 6.</li>
            <li>Внедрение и отработка механизма кроссподписания при передаче имущества из муниципального в региональный бюджет (ф.0510448, ф.0504805) — Пуровский р-н — 1.</li>
            <li>Подготовлен свод по работе МО с документами 61н.</li>
            <li>Направлено / решено заявок (обращений) от МО через чаты и по телефону — 100.</li>
            <li>Направлено заявок в техподдержку (ГИС «Смета ЯНАО») — 15.</li>
        </ol>
    </details>

    <div class="df-actions">
        <button type="submit" id="df-submit">Сохранить</button>
        <span id="df-status"></span>
    </div>
</form>

<style>
.daily-form { max-width: 640px; display: flex; flex-direction: column; gap: 14px; padding: 16px; background: #fff; border: 1px solid #e2e8f0; border-radius: 10px; }
.daily-form label { display: flex; flex-direction: column; gap: 4px; font-size: 13px; color: #2c3e50; }
.daily-form select, .daily-form input, .daily-form textarea { font-family: inherit; font-size: 13px; padding: 6px 8px; border: 1px solid #cfd6dd; border-radius: 6px; outline: none; }
.daily-form select:focus, .daily-form input:focus, .daily-form textarea:focus { border-color: #3182ce; box-shadow: 0 0 0 2px rgba(49,130,206,0.25); }
.daily-form textarea { resize: vertical; min-height: 140px; line-height: 1.45; }

.df-example { border: 1px solid #e2e8f0; border-radius: 8px; padding: 10px 14px; background: #f7fafc; font-size: 12.5px; }
.df-example summary { cursor: pointer; font-weight: 600; color: #2b6cb0; outline: none; }
.df-example ol { margin: 10px 0 4px 0; padding-left: 22px; color: #2d3748; line-height: 1.5; }
.df-example ol li { margin-bottom: 4px; }

.df-actions { display: flex; gap: 12px; align-items: center; }
.df-actions button { background: #3182ce; color: #fff; border: none; border-radius: 6px; padding: 8px 18px; font-size: 13px; cursor: pointer; }
.df-actions button:hover { background: #2b6cb0; }
.df-actions button[disabled] { background: #a0aec0; cursor: wait; }
#df-status { font-size: 12.5px; color: #2f855a; }
#df-status.error { color: #c53030; }
</style>

<script>
(function() {
  const form = document.getElementById('daily-form');
  const status = document.getElementById('df-status');
  const submit = document.getElementById('df-submit');

  // Слаг из URL: /daily/mulyavin/ → mulyavin
  const m = location.pathname.match(/\/daily\/([a-z\-]+)\/?$/i);
  const slug = m ? m[1].toLowerCase() : null;

  // === Диапазон допустимых дат ===
  const dateInput = document.getElementById('df-date');
  const dateHint = document.getElementById('df-date-hint');
  const today = new Date();
  const todayISO = today.toISOString().slice(0, 10);

  const firstThisMonth = new Date(today.getFullYear(), today.getMonth(), 1);
  const prevMonthLast = new Date(firstThisMonth.getTime() - 86400000);
  const earliest = new Date(prevMonthLast.getFullYear(), prevMonthLast.getMonth(), 1);
  const earliestISO = earliest.toISOString().slice(0, 10);

  const latest = new Date(today.getTime() + 86400000);
  const latestISO = latest.toISOString().slice(0, 10);

  dateInput.min = earliestISO;
  dateInput.max = latestISO;
  dateInput.value = todayISO;
  dateHint.textContent = 'Разрешено: с ' + earliestISO + ' по ' + latestISO;

  // Если пришли по персональной ссылке — скрываем выбор сотрудника
  if (slug) {
    const label = document.getElementById('df-employee-label');
    const empSelect = document.getElementById('df-employee');

    let foundValue = null;
    for (const opt of empSelect.options) {
      if ((opt.dataset.slug || '').toLowerCase() === slug) {
        foundValue = opt.value;
        break;
      }
    }
    empSelect.value = foundValue || '';

    if (label) label.style.display = 'none';

    const who = document.createElement('div');
    who.className = 'df-who';
    who.textContent = 'Сотрудник: ' + (foundValue || slug);
    who.style.cssText = 'font-weight:600;color:#2c5282;font-size:13px;';
    form.insertBefore(who, form.firstChild);
  }

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    status.className = '';
    status.textContent = '';

    const employee = document.getElementById('df-employee').value.trim();
    const date = document.getElementById('df-date').value.trim();
    const text = document.getElementById('df-text').value.trim();

    if (!date || !text || (!slug && !employee)) {
      status.className = 'error';
      status.textContent = 'Заполните все поля';
      return;
    }

    const d = new Date(date + 'T00:00:00');
    const dEarliest = new Date(earliestISO + 'T00:00:00');
    const dLatest = new Date(latestISO + 'T00:00:00');
    if (d < dEarliest || d > dLatest) {
      status.className = 'error';
      status.textContent = 'Дата должна быть в диапазоне ' + earliestISO + ' … ' + latestISO;
      return;
    }

    submit.setAttribute('disabled', 'disabled');
    submit.textContent = 'Сохраняю...';

    const url = slug ? '/api/daily/' + slug : '/api/daily';
    const body = slug ? { date, text } : { employee, date, text };

    try {
      const resp = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body)
      });
      const data = await resp.json();
      if (!resp.ok || !data.ok) throw new Error(data.error || 'Ошибка сохранения');
      status.textContent = 'Сохранено: ' + data.path;
      document.getElementById('df-text').value = '';
    } catch (err) {
      status.className = 'error';
      status.textContent = 'Ошибка: ' + err.message;
    } finally {
      submit.removeAttribute('disabled');
      submit.textContent = 'Сохранить';
    }
  });
})();
</script>