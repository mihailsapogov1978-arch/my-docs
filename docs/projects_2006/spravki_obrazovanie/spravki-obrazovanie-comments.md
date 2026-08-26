[← Назад к документации](spravky_educaition.md)

# Лог проекта «Справки Образование»

Новые записи создаются как issues на GitHub. Токен в браузере не нужен: достаточно нажать «Отправить» — откроется форма GitHub.

<textarea id="log-entry" placeholder="Текст записи..." rows="4"></textarea>

<div>
  <label><input type="radio" name="entry-type" value="note" checked> Заметка</label>
  <label><input type="radio" name="entry-type" value="task"> Задача</label>
  <label><input type="radio" name="entry-type" value="question"> Вопрос</label>
  <label><input type="radio" name="entry-type" value="idea"> Идея</label>
</div>

<p><button type="button" id="log-submit" class="md-button md-button--primary">Отправить</button>
<small>Ctrl+Enter открывает форму GitHub</small></p>

<p id="connection-status">Проверка подключения...</p>

## Статистика

<div id="stats">Загрузка...</div>

## Лог записей

<div id="log-container" class="project-log">Загрузка лога...</div>
