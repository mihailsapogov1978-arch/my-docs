<div style="max-width: 800px; margin: 0 auto;">

<!-- Навигация -->
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; padding-bottom: 10px; border-bottom: 1px solid #e0e0e0;">
  <a href="../spravky_educaition/" 
     style="color: #1976d2; text-decoration: none; display: flex; align-items: center; gap: 6px; font-size: 0.9em;">
    ← Назад к документации
  </a>
  
  <span style="color: #666; font-size: 0.85em;" id="last-update">
    🕐 Автообновление
  </span>
</div>

<h1 style="margin-bottom: 15px; font-size: 1.5em;">📝 Лог проекта "Справки Образование"</h1>

<div style="background: #f0f7ff; padding: 12px; border-radius: 6px; margin-bottom: 20px; border-left: 4px solid #1976d2;">
  <div style="display: flex; align-items: center; gap: 10px;">
    <div style="font-size: 1.2em;">⚡</div>
    <div style="font-size: 0.9em;">
      <strong>Автоматическое сохранение</strong>
      <div style="color: #666; font-size: 0.85em;">Просто пишите — всё сохраняется без открытия GitHub</div>
    </div>
  </div>
</div>

<!-- Форма для добавления -->
<div style="background: #f8f9fa; padding: 20px; border-radius: 8px; margin-bottom: 25px; border: 1px solid #ddd;">
  <h3 style="margin-top: 0; margin-bottom: 15px; font-size: 1.1em;">➕ Новая запись</h3>
  
  <div style="margin-bottom: 12px;">
    <label style="display: block; margin-bottom: 5px; font-weight: 500; font-size: 0.9em;">Текст записи:</label>
    <textarea id="log-entry" 
              placeholder="Что нового по проекту? Какие задачи выполнены? Что нужно обсудить?"
              rows="3"
              style="width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px; font-size: 0.95em; font-family: inherit;"></textarea>
  </div>
  
  <div style="margin-bottom: 12px;">
    <label style="display: block; margin-bottom: 5px; font-weight: 500; font-size: 0.9em;">Тип записи:</label>
    <div style="display: flex; gap: 8px; flex-wrap: wrap;">
      <button onclick="addEntry('note')"
              style="background: #1976d2; color: white; padding: 8px 12px; 
                     border: none; border-radius: 4px; cursor: pointer; font-size: 0.85em; flex: 1; min-width: 80px;">
        📝 Заметка
      </button>
      <button onclick="addEntry('task')"
              style="background: #4caf50; color: white; padding: 8px 12px; 
                     border: none; border-radius: 4px; cursor: pointer; font-size: 0.85em; flex: 1; min-width: 80px;">
        ✅ Задача
      </button>
      <button onclick="addEntry('question')"
              style="background: #ff9800; color: white; padding: 8px 12px; 
                     border: none; border-radius: 4px; cursor: pointer; font-size: 0.85em; flex: 1; min-width: 80px;">
        ❓ Вопрос
      </button>
      <button onclick="addEntry('idea')"
              style="background: #9c27b0; color: white; padding: 8px 12px; 
                     border: none; border-radius: 4px; cursor: pointer; font-size: 0.85em; flex: 1; min-width: 80px;">
        💡 Идея
      </button>
    </div>
  </div>
  
  <div id="add-status" style="margin-top: 10px; font-size: 0.85em;"></div>
  
  <div style="font-size: 0.8em; color: #666; margin-top: 10px; padding-top: 8px; border-top: 1px solid #e0e0e0;">
    Ctrl+Enter для быстрой отправки заметки
  </div>
</div>

<!-- Лог записей -->
<div id="log-container">
  <div style="text-align: center; padding: 30px; color: #666;">
    <div style="font-size: 2em; margin-bottom: 10px;">⏳</div>
    <p style="font-size: 0.9em;">Загрузка лога...</p>
  </div>
</div>

<!-- Статистика -->
<div id="stats" style="margin-top: 20px; padding: 10px; background: #f5f5f5; border-radius: 6px; text-align: center;">
  <small style="font-size: 0.85em;">Статистика загружается...</small>
</div>

<!-- Отладка (можно скрыть) -->
<div id="debug-info" style="margin-top: 20px; padding: 10px; background: #fff3cd; border-radius: 4px; font-size: 0.8em; color: #856404; display: none;">
  <strong>Отладка:</strong>
  <div id="debug-content"></div>
</div>

</div>

<script>
// ================= КОНФИГУРАЦИЯ =================
const CONFIG = {
  repoOwner: 'mihailsapogov1978-arch',
  repoName: 'my-docs',
  label: 'Spravky_obr',
  
  // Токен будет запрашиваться у пользователя при первом использовании
  // или взят из localStorage
  githubToken: null, // <-- Токен удален для безопасности
  
  // Спросите у пользователя при первом использовании
  askForToken: true
};

// ================= ОТЛАДКА =================
function showDebugInfo(message) {
  const debugDiv = document.getElementById('debug-info');
  const debugContent = document.getElementById('debug-content');
  
  debugDiv.style.display = 'block';
  debugContent.innerHTML += `<div>${new Date().toLocaleTimeString()}: ${message}</div>`;
}

// ================= ОСНОВНЫЕ ФУНКЦИИ =================

// Получить токен
function getGitHubToken() {
  // Проверяем localStorage
  const savedToken = localStorage.getItem('github_token');
  if (savedToken) {
    showDebugInfo('Используется токен из localStorage');
    return savedToken;
  }
  
  // Запрашиваем у пользователя
  if (CONFIG.askForToken) {
    showDebugInfo('Запрашивается токен у пользователя');
    const token = prompt(
      'Для автоматического сохранения записей нужен GitHub токен.\n\n' +
      '1. Перейдите: https://github.com/settings/tokens\n' +
      '2. Создайте новый токен с правами "repo"\n' +
      '3. Вставьте его здесь:\n\n' +
      '(Токен сохранится только в вашем браузере)',
      ''
    );
    
    if (token && token.trim()) {
      localStorage.setItem('github_token', token.trim());
      showDebugInfo('Токен сохранен в localStorage');
      return token.trim();
    }
  }
  
  showDebugInfo('Токен не найден');
  return null;
}

// Проверить доступность GitHub API
async function testGitHubAPI() {
  try {
    showDebugInfo('Тестирование подключения к GitHub API...');
    const response = await fetch('https://api.github.com');
    
    if (response.ok) {
      showDebugInfo('GitHub API доступен');
      return true;
    } else {
      showDebugInfo(`GitHub API недоступен: ${response.status}`);
      return false;
    }
  } catch (error) {
    showDebugInfo(`Ошибка подключения к GitHub API: ${error.message}`);
    return false;
  }
}

// Проверить доступ к репозиторию
async function testRepoAccess() {
  const token = getGitHubToken();
  if (!token) {
    showDebugInfo('Токен не найден для проверки доступа к репозиторию');
    return false;
  }
  
  try {
    showDebugInfo('Проверка доступа к репозиторию...');
    const response = await fetch(
      `https://api.github.com/repos/${CONFIG.repoOwner}/${CONFIG.repoName}`,
      {
        headers: {
          'Authorization': `token ${token}`,
          'Accept': 'application/vnd.github.v3+json'
        }
      }
    );
    
    if (response.ok) {
      showDebugInfo('Доступ к репозиторию есть');
      return true;
    } else {
      showDebugInfo(`Нет доступа к репозиторию: ${response.status}`);
      return false;
    }
  } catch (error) {
    showDebugInfo(`Ошибка проверки доступа к репозиторию: ${error.message}`);
    return false;
  }
}

// Добавить запись
async function addEntry(type) {
  const text = document.getElementById('log-entry').value.trim();
  if (!text) {
    showStatus('Введите текст записи', 'error');
    return;
  }
  
  const token = getGitHubToken();
  if (!token) {
    showStatus('Требуется GitHub токен для автоматического сохранения', 'error');
    return;
  }
  
  showStatus('Сохранение...', 'loading');
  
  try {
    const { title, body } = createIssueContent(text, type);
    showDebugInfo(`Создание issue: ${title.substring(0, 50)}...`);
    
    const issueId = await createGitHubIssue(title, body, type, token);
    
    if (issueId) {
      showStatus('✅ Запись сохранена!', 'success');
      document.getElementById('log-entry').value = '';
      showDebugInfo(`Issue создан с ID: ${issueId}`);
      
      setTimeout(() => {
        loadLogEntries();
        updateStats();
      }, 1000);
    }
  } catch (error) {
    console.error('Ошибка сохранения:', error);
    showDebugInfo(`Ошибка сохранения: ${error.message}`);
    showStatus('❌ Ошибка сохранения. Проверьте токен.', 'error');
  }
}

// Создать контент для Issue
function createIssueContent(text, type) {
  const now = new Date();
  const dateStr = now.toLocaleString('ru-RU');
  const dateShort = now.toLocaleDateString('ru-RU');
  
  const types = {
    note: { icon: '📝', prefix: 'Заметка', color: '#1976d2' },
    task: { icon: '✅', prefix: 'Задача', color: '#4caf50' },
    question: { icon: '❓', prefix: 'Вопрос', color: '#ff9800' },
    idea: { icon: '💡', prefix: 'Идея', color: '#9c27b0' }
  };
  
  const typeInfo = types[type] || types.note;
  
  let title = `${typeInfo.icon} ${dateShort}: ${text.substring(0, 50)}`;
  if (text.length > 50) title += '...';
  
  let body = `${text}\n\n---\n*Дата: ${dateStr}*\n*Тип: ${typeInfo.prefix}*`;
  
  return { title, body };
}

// Создать Issue через GitHub API
async function createGitHubIssue(title, body, type, token) {
  const response = await fetch(
    `https://api.github.com/repos/${CONFIG.repoOwner}/${CONFIG.repoName}/issues`,
    {
      method: 'POST',
      headers: {
        'Authorization': `token ${token}`,
        'Accept': 'application/vnd.github.v3+json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        title: title,
        body: body,
        labels: [CONFIG.label, type]
      })
    }
  );
  
  if (response.ok) {
    const data = await response.json();
    return data.number;
  } else {
    const errorText = await response.text();
    showDebugInfo(`GitHub API error: ${response.status} - ${errorText}`);
    throw new Error(`GitHub API error: ${response.status}`);
  }
}

// Загрузить лог записей
async function loadLogEntries() {
  const container = document.getElementById('log-container');
  showDebugInfo('Начало загрузки лога...');
  
  try {
    showDebugInfo(`Запрос к API: issues с меткой "${CONFIG.label}"`);
    
    // Сначала попробуем без токена (публичный доступ)
    let apiUrl = `https://api.github.com/repos/${CONFIG.repoOwner}/${CONFIG.repoName}/issues?labels=${encodeURIComponent(CONFIG.label)}&sort=created&direction=desc&per_page=50`;
    
    showDebugInfo(`URL запроса: ${apiUrl}`);
    
    const response = await fetch(apiUrl, {
      headers: {
        'Accept': 'application/vnd.github.v3+json'
      }
    });
    
    showDebugInfo(`Статус ответа: ${response.status} ${response.statusText}`);
    
    if (response.ok) {
      const issues = await response.json();
      showDebugInfo(`Получено ${issues.length} записей`);
      
      document.getElementById('last-update').innerHTML = 
        `🕐 ${new Date().toLocaleTimeString('ru-RU', { hour: '2-digit', minute: '2-digit' })}`;
      
      if (issues.length === 0) {
        container.innerHTML = `
          <div style="text-align: center; padding: 30px; color: #666;">
            <div style="font-size: 2em; margin-bottom: 10px;">📭</div>
            <p style="font-size: 0.9em;">Лог пуст. Нет записей с меткой "${CONFIG.label}"</p>
          </div>
        `;
        return;
      }
      
      let html = `
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
          <h3 style="margin: 0; font-size: 1.1em;">📚 Записи (${issues.length})</h3>
          <button onclick="loadLogEntries()" 
                  style="background: #f5f5f5; border: 1px solid #ddd; padding: 6px 12px; border-radius: 4px; cursor: pointer; font-size: 0.85em;">
            🔄 Обновить
          </button>
        </div>
      `;
      
      issues.forEach((issue, index) => {
        const date = new Date(issue.created_at).toLocaleString('ru-RU', {
          day: 'numeric',
          month: 'short',
          hour: '2-digit',
          minute: '2-digit'
        });
        
        // Определяем тип по меткам
        const typeLabels = issue.labels.filter(l => l.name !== CONFIG.label);
        const typeLabel = typeLabels[0] || { name: 'note' };
        
        const types = {
          note: { icon: '📝', color: '#f0f7ff', textColor: '#424242' },
          task: { icon: '✅', color: '#f0f9f0', textColor: '#424242' },
          question: { icon: '❓', color: '#fff8e1', textColor: '#424242' },
          idea: { icon: '💡', color: '#f5e6f9', textColor: '#424242' }
        };
        
        const typeInfo = types[typeLabel.name] || types.note;
        
        // Убираем префикс даты из заголовка для отображения
        let displayTitle = issue.title;
        const dateMatch = issue.title.match(/^\S+\s+\d{2}\.\d{2}\.\d{4}:\s*/);
        if (dateMatch) {
          displayTitle = issue.title.substring(dateMatch[0].length);
        }
        
        // Убираем иконку из заголовка
        const iconMatch = displayTitle.match(/^[^\w\s]+\s/);
        if (iconMatch) {
          displayTitle = displayTitle.substring(iconMatch[0].length);
        }
        
        html += `
          <div style="background: ${typeInfo.color}; border-radius: 6px; padding: 12px; margin-bottom: 10px; position: relative; border-left: 4px solid ${getTypeBorderColor(typeLabel.name)};">
            <div style="display: flex; align-items: flex-start; gap: 10px;">
              <div style="font-size: 1.2em; flex-shrink: 0; padding-top: 2px;">
                ${typeInfo.icon}
              </div>
              
              <div style="flex-grow: 1;">
                <div style="color: ${typeInfo.textColor}; background: rgba(255,255,255,0.7); padding: 8px 10px; border-radius: 4px; margin-bottom: 10px; font-size: 0.95em; line-height: 1.4;">
                  ${formatIssueBody(issue.body)}
                </div>
                
                <div style="display: flex; justify-content: space-between; align-items: center; font-size: 0.8em; color: #666;">
                  <div>
                    <span>📅 ${date}</span>
                    <span style="margin-left: 10px;">
                      ${issue.state === 'open' ? '🔵 Открыто' : '✅ Закрыто'}
                    </span>
                    ${issue.comments > 0 ? 
                      `<span style="margin-left: 10px;">💬 ${issue.comments}</span>` : 
                      ''}
                  </div>
                  
                  <div>
                    <a href="${issue.html_url}" target="_blank" 
                       style="color: #666; text-decoration: none; font-size: 0.85em;">
                      GitHub →
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        `;
      });
      
      container.innerHTML = html;
      showDebugInfo('Лог успешно загружен и отображен');
    } else {
      const errorText = await response.text();
      showDebugInfo(`Ошибка API: ${response.status} - ${errorText}`);
      container.innerHTML = `
        <div style="background: #ffebee; padding: 15px; border-radius: 6px; text-align: center;">
          <div style="font-size: 2em; margin-bottom: 10px;">⚠️</div>
          <p style="margin: 0; color: #c62828; font-size: 0.9em;">
            Ошибка загрузки лога: ${response.status}
          </p>
          <p style="margin: 10px 0 0 0; color: #666; font-size: 0.8em;">
            Проверьте название репозитория и метку
          </p>
          <button onclick="testConnection()"
                  style="background: #1976d2; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer; margin-top: 10px; font-size: 0.85em;">
            Проверить подключение
          </button>
        </div>
      `;
    }
  } catch (error) {
    console.error('Ошибка загрузки лога:', error);
    showDebugInfo(`Ошибка загрузки: ${error.message}`);
    container.innerHTML = `
      <div style="background: #ffebee; padding: 15px; border-radius: 6px; text-align: center;">
        <div style="font-size: 2em; margin-bottom: 10px;">🚫</div>
        <p style="margin: 0; color: #c62828; font-size: 0.9em;">
          Не удалось загрузить лог
        </p>
        <p style="margin: 10px 0 0 0; color: #666; font-size: 0.8em;">
          ${error.message}
        </p>
      </div>
    `;
  }
}

// Функция проверки подключения
function testConnection() {
  showDebugInfo('Запуск теста подключения...');
  
  Promise.all([
    testGitHubAPI(),
    testRepoAccess()
  ]).then(([apiAvailable, repoAccess]) => {
    if (apiAvailable && repoAccess) {
      showStatus('✅ Подключение к GitHub работает', 'success');
      loadLogEntries();
    } else if (!apiAvailable) {
      showStatus('❌ GitHub API недоступен', 'error');
    } else {
      showStatus('❌ Нет доступа к репозиторию', 'error');
    }
  });
}

// Получить цвет границы для типа
function getTypeBorderColor(type) {
  const colors = {
    note: '#1976d2',
    task: '#4caf50',
    question: '#ff9800',
    idea: '#9c27b0'
  };
  return colors[type] || '#666';
}

// Обновить статистику
async function updateStats() {
  try {
    const response = await fetch(
      `https://api.github.com/repos/${CONFIG.repoOwner}/${CONFIG.repoName}/issues?labels=${CONFIG.label}`
    );
    
    if (response.ok) {
      const issues = await response.json();
      const openIssues = issues.filter(i => i.state === 'open').length;
      const closedIssues = issues.filter(i => i.state === 'closed').length;
      const completed = issues.length > 0 ? Math.round((closedIssues / issues.length) * 100) : 0;
      
      document.getElementById('stats').innerHTML = `
        <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
          <div>
            <div style="font-size: 1.2em; font-weight: bold;">${issues.length}</div>
            <div style="font-size: 0.8em; color: #666;">Всего</div>
          </div>
          <div>
            <div style="font-size: 1.2em; font-weight: bold; color: #1976d2;">${openIssues}</div>
            <div style="font-size: 0.8em; color: #666;">Открыто</div>
          </div>
          <div>
            <div style="font-size: 1.2em; font-weight: bold; color: #4caf50;">${closedIssues}</div>
            <div style="font-size: 0.8em; color: #666;">Закрыто</div>
          </div>
          <div>
            <div style="font-size: 1.2em; font-weight: bold; color: #9c27b0;">${completed}%</div>
            <div style="font-size: 0.8em; color: #666;">Выполнено</div>
          </div>
        </div>
      `;
    }
  } catch (error) {
    console.error('Ошибка загрузки статистики:', error);
  }
}

// ================= ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ =================

function formatIssueBody(text) {
  if (!text) return '';
  
  let formatted = text;
  const metaIndex = formatted.lastIndexOf('\n---\n');
  if (metaIndex !== -1) {
    formatted = formatted.substring(0, metaIndex);
  }
  
  formatted = formatted.trim();
  
  if (formatted.length > 200) {
    formatted = formatted.substring(0, 200) + '...';
  }
  
  return formatted.replace(/\n/g, '<br>');
}

function showStatus(message, type) {
  const statusDiv = document.getElementById('add-status');
  const colors = {
    success: '#4caf50',
    error: '#f44336',
    loading: '#ff9800'
  };
  
  statusDiv.innerHTML = `
    <div style="background: ${colors[type]}; color: white; padding: 8px 12px; border-radius: 4px; font-size: 0.9em;">
      ${message}
    </div>
  `;
  
  if (type !== 'loading') {
    setTimeout(() => {
      statusDiv.innerHTML = '';
    }, 2000);
  }
}

// ================= ИНИЦИАЛИЗАЦИЯ =================

document.addEventListener('DOMContentLoaded', function() {
  showDebugInfo('Страница загружена');
  
  // Включаем отладку
  document.getElementById('debug-info').style.display = 'block';
  
  const token = getGitHubToken();
  if (!token && CONFIG.askForToken) {
    setTimeout(() => {
      const setupToken = getGitHubToken();
      if (setupToken) {
        showStatus('✅ Токен сохранен! Можно добавлять записи.', 'success');
      }
    }, 1000);
  }
  
  // Загружаем данные
  showDebugInfo('Начало загрузки данных...');
  loadLogEntries();
  updateStats();
  
  // Автообновление каждые 30 секунд
  setInterval(() => {
    loadLogEntries();
    updateStats();
  }, 30000);
  
  // Фокус на поле ввода
  document.getElementById('log-entry').focus();
  
  // Добавляем обработчик Enter (Ctrl+Enter для отправки)
  document.getElementById('log-entry').addEventListener('keydown', function(e) {
    if (e.ctrlKey && e.key === 'Enter') {
      addEntry('note');
    }
  });
  
  // Кнопка для тестирования подключения
  const testBtn = document.createElement('button');
  testBtn.innerHTML = '🔧 Тест подключения';
  testBtn.style = 'background: #6c757d; color: white; border: none; padding: 6px 12px; border-radius: 4px; cursor: pointer; font-size: 0.8em; margin-top: 10px;';
  testBtn.onclick = testConnection;
  document.getElementById('debug-info').appendChild(testBtn);
});
</script>