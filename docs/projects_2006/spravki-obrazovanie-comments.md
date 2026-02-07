[
    ← Назад к документации
](../spravky_educaition/)

📝 Лог проекта "Справки Образование"  
🕐 Автообновление  
⚡ Автоматическое сохранение  
Просто пишите — всё сохраняется без открытия GitHub  

➕ Новая запись  
<textarea id="log-entry" placeholder="Текст записи..." style="width: 100%; height: 80px; padding: 8px; margin: 8px 0; border: 1px solid #ccc; border-radius: 4px;"></textarea>

<div style="margin: 8px 0;">
  <label><input type="radio" name="entry-type" value="note" checked> 📝 Заметка</label>
  <label><input type="radio" name="entry-type" value="task"> ✅ Задача</label>
  <label><input type="radio" name="entry-type" value="question"> ❓ Вопрос</label>
  <label><input type="radio" name="entry-type" value="idea"> 💡 Идея</label>
</div>

<button onclick="addEntry()" style="background: #1976d2; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">Отправить</button>
<small>Ctrl+Enter для быстрой отправки заметки</small>

<div id="token-prompt" style="display: none; background: #e3f2fd; padding: 16px; border-radius: 8px; margin: 20px 0;">
  <h3>🔑 Авторизация в GitHub</h3>
  <p>Для работы с логом требуется <strong>Personal Access Token</strong> с правами <code>repo</code>.</p>
  <input type="password" id="github-token-input" placeholder="Введите ваш GitHub Token..." style="width: 100%; padding: 8px; margin: 8px 0; border: 1px solid #ccc; border-radius: 4px;">
  <button onclick="saveToken()" style="background: #1976d2; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">Сохранить и продолжить</button>
  <p style="font-size: 0.85em; color: #666; margin-top: 8px;">
    Токен хранится только в вашем браузере (<code>localStorage</code>). Он <strong>не передаётся на сервер</strong> и не попадает в Git.
  </p>
</div>

<div id="connection-info" style="padding: 12px; border-left: 4px solid #4caf50; margin: 20px 0; background: #e8f5e8; border-radius: 4px;">
  <strong id="connection-status">⏳ Проверка подключения...</strong>
</div>

<div id="add-status"></div>

<h3>Статистика</h3>
<div id="stats" style="padding: 10px; background: #f9f9f9; border-radius: 4px; margin: 10px 0;">Загрузка...</div>

<h3>Лог записей</h3>
<div id="log-container">⏳ Загрузка лога...</div>

<script>
// ================= КОНФИГУРАЦИЯ =================
const CONFIG = {
  repoOwner: 'mihailsapogov1978-arch',
  repoName: 'my-docs',
  label: 'Spravky_obr'
};

// ================= ОСНОВНЫЕ ФУНКЦИИ =================

// Получить токен из localStorage
function getGitHubToken() {
  return localStorage.getItem('github_token');
}

// Сохранить токен и скрыть форму
function saveToken() {
  const tokenInput = document.getElementById('github-token-input');
  const token = tokenInput.value.trim();
  
  if (!token) {
    alert('Пожалуйста, введите токен.');
    return;
  }
  
  localStorage.setItem('github_token', token);
  document.getElementById('token-prompt').style.display = 'none';
  checkConnection();
  loadLogEntries();
  updateStats();
}

// Показать форму ввода токена
function showTokenPrompt() {
  document.getElementById('token-prompt').style.display = 'block';
  document.getElementById('log-container').innerHTML = '<p>Введите токен для доступа к записям.</p>';
}

// Обновить статус подключения
function updateConnectionStatus(message, isError = false) {
  const statusEl = document.getElementById('connection-status');
  const infoEl = document.getElementById('connection-info');
  
  if (!statusEl || !infoEl) return;
  
  statusEl.innerHTML = message;
  
  if (isError) {
    infoEl.style.background = '#ffebee';
    infoEl.style.borderLeftColor = '#f44336';
    infoEl.style.color = '#c62828';
  } else {
    infoEl.style.background = '#e8f5e8';
    infoEl.style.borderLeftColor = '#4caf50';
    infoEl.style.color = '#2e7d32';
  }
}

// Проверить подключение
async function checkConnection() {
  const token = getGitHubToken();
  if (!token) {
    showTokenPrompt();
    return;
  }
  
  updateConnectionStatus('⏳ Проверка подключения...');
  
  try {
    const userResponse = await fetch('https://api.github.com/user', {
      headers: {
        'Authorization': `token ${token}`,
        'Accept': 'application/vnd.github.v3+json'
      }
    });
    
    if (!userResponse.ok) {
      updateConnectionStatus(`❌ Токен недействителен (${userResponse.status})`, true);
      showTokenPrompt();
      return;
    }
    
    const userData = await userResponse.json();
    const username = userData.login || 'неизвестно';
    
    const repoResponse = await fetch(
      `https://api.github.com/repos/${CONFIG.repoOwner}/${CONFIG.repoName}`,
      {
        headers: {
          'Authorization': `token ${token}`,
          'Accept': 'application/vnd.github.v3+json'
        }
      }
    );
    
    if (!repoResponse.ok) {
      updateConnectionStatus(`❌ Нет доступа к репозиторию (${repoResponse.status})`, true);
      showTokenPrompt();
      return;
    }
    
    updateConnectionStatus(`✅ Подключено: ${username} → ${CONFIG.repoName}`);
  } catch (error) {
    updateConnectionStatus(`❌ Ошибка: ${error.message}`, true);
    showTokenPrompt();
  }
}

// Добавить запись
async function addEntry() {
  const text = document.getElementById('log-entry').value.trim();
  if (!text) {
    showStatus('Введите текст записи', 'error');
    return;
  }
  
  const type = document.querySelector('input[name="entry-type"]:checked').value;
  
  const token = getGitHubToken();
  if (!token) {
    showTokenPrompt();
    return;
  }
  
  showStatus('Сохранение...', 'loading');
  
  try {
    const { title, body } = createIssueContent(text, type);
    
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
      showStatus('✅ Запись сохранена!', 'success');
      document.getElementById('log-entry').value = '';
      
      setTimeout(() => {
        loadLogEntries();
        updateStats();
      }, 1000);
    } else {
      throw new Error(`GitHub API: ${response.status}`);
    }
  } catch (error) {
    showStatus('❌ Ошибка сохранения', 'error');
    updateConnectionStatus('❌ Ошибка при сохранении', true);
  }
}

// Создать контент для Issue
function createIssueContent(text, type) {
  const now = new Date();
  const dateStr = now.toLocaleString('ru-RU');
  const dateShort = now.toLocaleDateString('ru-RU');
  
  const types = {
    note: { icon: '📝', prefix: 'Заметка' },
    task: { icon: '✅', prefix: 'Задача' },
    question: { icon: '❓', prefix: 'Вопрос' },
    idea: { icon: '💡', prefix: 'Идея' }
  };
  
  const typeInfo = types[type] || types.note;
  
  let title = `${typeInfo.icon} ${dateShort}: ${text.substring(0, 50)}`;
  if (text.length > 50) title += '...';
  
  let body = `${text}\n\n---\n*Дата: ${dateStr}*\n*Тип: ${typeInfo.prefix}*`;
  
  return { title, body };
}

// Закрыть issue
async function closeIssue(issueNumber, button) {
  if (!confirm('Закрыть эту запись?')) return;
  
  const token = getGitHubToken();
  if (!token) {
    showTokenPrompt();
    return;
  }
  
  button.innerHTML = '⏳ Закрываем...';
  button.disabled = true;
  button.style.background = '#ccc';
  
  try {
    const response = await fetch(
      `https://api.github.com/repos/${CONFIG.repoOwner}/${CONFIG.repoName}/issues/${issueNumber}`,
      {
        method: 'PATCH',
        headers: {
          'Authorization': `token ${token}`,
          'Accept': 'application/vnd.github.v3+json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ state: 'closed' })
      }
    );
    
    if (response.ok) {
      showStatus('✅ Запись закрыта!', 'success');
      
      const issueElement = document.getElementById(`issue-${issueNumber}`);
      issueElement.style.transition = 'opacity 0.3s, max-height 0.3s';
      issueElement.style.opacity = '0';
      issueElement.style.maxHeight = '0';
      issueElement.style.padding = '0';
      issueElement.style.margin = '0';
      issueElement.style.overflow = 'hidden';
      
      setTimeout(() => {
        loadLogEntries();
        updateStats();
      }, 300);
    } else {
      throw new Error(`Ошибка: ${response.status}`);
    }
  } catch (error) {
    showStatus('❌ Ошибка закрытия', 'error');
    button.innerHTML = '✕ Закрыть';
    button.disabled = false;
    button.style.background = '#ff6b6b';
  }
}

// Переключить показ закрытых записей
function toggleShowClosed() {
  const current = localStorage.getItem('show_closed_issues') === 'true';
  localStorage.setItem('show_closed_issues', !current);
  loadLogEntries();
}

// Загрузить лог записей
async function loadLogEntries() {
  const container = document.getElementById('log-container');
  if (!container) return;
  
  const token = getGitHubToken();
  if (!token) {
    showTokenPrompt();
    return;
  }
  
  updateConnectionStatus('⏳ Загрузка записей...');
  
  try {
    let apiUrl = `https://api.github.com/repos/${CONFIG.repoOwner}/${CONFIG.repoName}/issues?labels=${encodeURIComponent(CONFIG.label)}&sort=created&direction=desc`;
    
    const headers = { 'Accept': 'application/vnd.github.v3+json' };
    headers['Authorization'] = `token ${token}`;
    
    const response = await fetch(apiUrl, { headers });
    
    if (response.ok) {
      const issues = await response.json();
      
      if (issues.length === 0) {
        container.innerHTML = `
          <div style="text-align: center; padding: 30px; color: #666;">
            <div style="font-size: 2em; margin-bottom: 10px;">📭</div>
            <p style="font-size: 0.9em;">Лог пуст. Нет записей с меткой "${CONFIG.label}"</p>
          </div>
        `;
        updateConnectionStatus(`✅ Нет записей с меткой "${CONFIG.label}"`);
        return;
      }
      
      const showClosed = localStorage.getItem('show_closed_issues') === 'true';
      
      let html = `
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
          <h3 style="margin: 0; font-size: 1.1em;">📚 Записи (${issues.length})</h3>
          <div>
            <button onclick="toggleShowClosed()" 
                    style="background: #f5f5f5; border: 1px solid #ddd; padding: 6px 12px; border-radius: 4px; cursor: pointer; font-size: 0.85em; margin-right: 8px;">
              ${showClosed ? '🔽 Скрыть закрытые' : '🔼 Показать закрытые'}
            </button>
            <button onclick="loadLogEntries()" 
                    style="background: #f5f5f5; border: 1px solid #ddd; padding: 6px 12px; border-radius: 4px; cursor: pointer; font-size: 0.85em;">
              🔄 Обновить
            </button>
          </div>
        </div>
      `;
      
      let visibleCount = 0;
      issues.forEach((issue) => {
        if (issue.state === 'closed' && !showClosed) return;
        
        visibleCount++;
        const date = new Date(issue.created_at).toLocaleString('ru-RU', {
          day: 'numeric',
          month: 'short',
          hour: '2-digit',
          minute: '2-digit'
        });
        
        const typeLabels = issue.labels.filter(l => l.name !== CONFIG.label);
        const typeLabel = typeLabels[0] || { name: 'note' };
        
        const types = {
          note: { icon: '📝', color: '#f0f7ff' },
          task: { icon: '✅', color: '#f0f9f0' },
          question: { icon: '❓', color: '#fff8e1' },
          idea: { icon: '💡', color: '#f5e6f9' }
        };
        
        const typeInfo = types[typeLabel.name] || types.note;
        const closedStyle = issue.state === 'closed' ? 'opacity: 0.7; background: #f9f9f9;' : '';
        
        html += `
          <div id="issue-${issue.number}" 
               style="background: ${typeInfo.color}; border-radius: 6px; padding: 12px; margin-bottom: 10px; position: relative; ${closedStyle}">
            
            ${issue.state === 'closed' ? `
              <div style="position: absolute; top: 8px; right: 8px; background: #4caf50; color: white; padding: 2px 6px; border-radius: 3px; font-size: 0.7em; font-weight: bold;">
                ✓ ЗАКРЫТО
              </div>
            ` : `
              <div style="position: absolute; top: 8px; right: 8px;">
                <button onclick="closeIssue(${issue.number}, this)" 
                         style="background: #ff6b6b; color: white; border: none; padding: 4px 10px; border-radius: 3px; cursor: pointer; font-size: 0.8em;">
                  ✕ Закрыть
                </button>
              </div>
            `}
            
            <div style="display: flex; align-items: flex-start; gap: 10px; margin-right: 80px;">
              <div style="font-size: 1.2em; padding-top: 2px;">
                ${typeInfo.icon}
              </div>
              
              <div style="flex-grow: 1;">
                <div style="background: rgba(255,255,255,0.7); padding: 8px 10px; border-radius: 4px; margin-bottom: 10px; font-size: 0.95em;">
                  ${formatIssueBody(issue.body)}
                </div>
                
                <div style="display: flex; justify-content: space-between; align-items: center; font-size: 0.8em; color: #666;">
                  <div>
                    <span>📅 ${date}</span>
                    <span style="margin-left: 10px;">
                      ${issue.state === 'open' ? '🔵 Открыто' : '✅ Закрыто'}
                    </span>
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
      
      if (visibleCount === 0) {
        html += `
          <div style="text-align: center; padding: 20px; color: #666; background: #f9f9f9; border-radius: 6px;">
            <div style="font-size: 2em; margin-bottom: 10px;">📭</div>
            <p style="margin: 0; font-size: 0.9em;">Нет открытых записей</p>
            <button onclick="toggleShowClosed()" 
                    style="background: #1976d2; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer; margin-top: 10px;">
              Показать закрытые записи
            </button>
          </div>
        `;
      }
      
      container.innerHTML = html;
      updateConnectionStatus(`✅ Загружено ${issues.length} записей`);
      
    } else {
      container.innerHTML = `
        <div style="background: #ffebee; padding: 15px; border-radius: 6px; text-align: center;">
          <div style="font-size: 2em; margin-bottom: 10px;">⚠️</div>
          <p style="margin: 0; color: #c62828; font-size: 0.9em;">
            Ошибка ${response.status}: ${getErrorMessage(response.status)}
          </p>
          <p style="margin: 10px 0 0 0; color: #666; font-size: 0.8em;">
            ${getErrorDescription(response.status)}
          </p>
          <button onclick="checkConnection()"
                  style="background: #1976d2; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer; margin-top: 10px;">
            Проверить подключение
          </button>
        </div>
      `;
      updateConnectionStatus(`❌ Ошибка ${response.status}`, true);
    }
  } catch (error) {
    container.innerHTML = `
      <div style="background: #ffebee; padding: 15px; border-radius: 6px; text-align: center;">
        <div style="font-size: 2em; margin-bottom: 10px;">🚫</div>
        <p style="margin: 0; color: #c62828; font-size: 0.9em;">
          Ошибка сети: ${error.message}
        </p>
      </div>
    `;
    updateConnectionStatus(`❌ Ошибка сети`, true);
  }
}

// Обновить статистику
async function updateStats() {
  const token = getGitHubToken();
  if (!token) return;
  
  try {
    const headers = { 
      'Accept': 'application/vnd.github.v3+json',
      'Authorization': `token ${token}`
    };
    
    const response = await fetch(
      `https://api.github.com/repos/${CONFIG.repoOwner}/${CONFIG.repoName}/issues?labels=${CONFIG.label}`,
      { headers }
    );
    
    if (response.ok) {
      const issues = await response.json();
      const openIssues = issues.filter(i => i.state === 'open').length;
      const closedIssues = issues.filter(i => i.state === 'closed').length;
      const completed = issues.length > 0 ? Math.round((closedIssues / issues.length) * 100) : 0;
      
      document.getElementById('stats').innerHTML = `
        <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
          <div><div style="font-size: 1.2em; font-weight: bold;">${issues.length}</div><div style="font-size: 0.8em; color: #666;">Всего</div></div>
          <div><div style="font-size: 1.2em; font-weight: bold; color: #1976d2;">${openIssues}</div><div style="font-size: 0.8em; color: #666;">Открыто</div></div>
          <div><div style="font-size: 1.2em; font-weight: bold; color: #4caf50;">${closedIssues}</div><div style="font-size: 0.8em; color: #666;">Закрыто</div></div>
          <div><div style="font-size: 1.2em; font-weight: bold; color: #9c27b0;">${completed}%</div><div style="font-size: 0.8em; color: #666;">Выполнено</div></div>
        </div>
      `;
    }
  } catch (error) {
    console.error('Ошибка статистики:', error);
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
  if (!statusDiv) return;
  
  const colors = {
    success: '#4caf50',
    error: '#f44336',
    loading: '#ff9800'
  };
   
  statusDiv.innerHTML = `
    <div style="background: ${colors[type]}; color: white; padding: 8px 12px; border-radius: 4px; font-size: 0.9em; margin: 10px 0;">
      ${message}
    </div>
  `;
  
  if (type !== 'loading') {
    setTimeout(() => {
      statusDiv.innerHTML = '';
    }, 2000);
  }
}

function getErrorMessage(status) {
  switch(status) {
    case 401: return 'Неавторизован';
    case 403: return 'Доступ запрещен';
    case 404: return 'Не найдено';
    default: return `Ошибка ${status}`;
  }
}

function getErrorDescription(status) {
  switch(status) {
    case 401: return 'Токен недействителен или отсутствует';
    case 403: return 'У токена нет прав доступа к репозиторию';
    case 404: return 'Репозиторий не найден';
    default: return 'Проверьте настройки';
  }
}

// ================= ИНИЦИАЛИЗАЦИЯ =================

document.addEventListener('DOMContentLoaded', function() {
  // Проверяем токен
  const token = getGitHubToken();
  if (!token) {
    showTokenPrompt();
  } else {
    updateConnectionStatus('⏳ Проверка подключения...');
    setTimeout(checkConnection, 500);
  }
  
  // Загружаем данные
  loadLogEntries();
  updateStats();
  
  // Автообновление
  setInterval(() => {
    loadLogEntries();
    updateStats();
  }, 30000);
  
  // Ctrl+Enter для отправки
  document.getElementById('log-entry').addEventListener('keydown', function(e) {
    if (e.ctrlKey && e.key === 'Enter') {
      addEntry();
    }
  });
});
</script>