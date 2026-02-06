# 💬 Комментарии и обратная связь

<div class="comment-form" style="background: #f5f5f5; padding: 20px; border-radius: 10px; margin: 20px 0;">
  <h3>📝 Добавить комментарий</h3>
  <form id="github-comment-form">
    <div style="margin-bottom: 15px;">
      <label for="comment-title" style="display: block; margin-bottom: 5px; font-weight: bold;">
        Заголовок комментария:
      </label>
      <input type="text" id="comment-title" name="title" 
             placeholder="Например: Вопрос по анализу заявок" 
             required
             style="width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 5px;">
    </div>
    
    <div style="margin-bottom: 15px;">
      <label for="comment-body" style="display: block; margin-bottom: 5px; font-weight: bold;">
        Текст комментария:
      </label>
      <textarea id="comment-body" name="body" 
                placeholder="Опишите ваш вопрос или предложение..." 
                rows="5" required
                style="width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 5px;"></textarea>
    </div>
    
    <div style="margin-bottom: 15px;">
      <label for="comment-labels" style="display: block; margin-bottom: 5px; font-weight: bold;">
        Категория:
      </label>
      <select id="comment-labels" name="labels"
              style="width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 5px;">
        <option value="вопрос">❓ Вопрос</option>
        <option value="предложение">💡 Предложение</option>
        <option value="ошибка">🐛 Ошибка</option>
        <option value="благодарность">🙏 Благодарность</option>
      </select>
    </div>
    
    <button type="button" onclick="submitGitHubComment()"
            style="background: #2ea44f; color: white; padding: 12px 24px; 
                   border: none; border-radius: 6px; cursor: pointer; font-size: 16px;">
      📤 Отправить через GitHub
    </button>
  </form>
</div>

## 📋 Последние комментарии

<div id="issues-container" style="margin-top: 30px;">
  <p>Загрузка комментариев с GitHub...</p>
</div>

<script>
// Данные вашего репозитория
const REPO_OWNER = 'mihailsapogov1978-arch';
const REPO_NAME = 'my-docs';

// Функция для отправки комментария через GitHub
function submitGitHubComment() {
  const title = document.getElementById('comment-title').value;
  const body = document.getElementById('comment-body').value;
  const label = document.getElementById('comment-labels').value;
  
  if (!title || !body) {
    alert('Пожалуйста, заполните все поля');
    return;
  }
  
  // Формируем URL для создания Issue
  const issueUrl = `https://github.com/${REPO_OWNER}/${REPO_NAME}/issues/new?` + 
                   `title=${encodeURIComponent(title)}&` +
                   `body=${encodeURIComponent(body)}&` +
                   `labels=${encodeURIComponent(label)}`;
  
  // Открываем в новой вкладке
  window.open(issueUrl, '_blank');
  
  // Очищаем форму
  document.getElementById('github-comment-form').reset();
  
  // Показываем сообщение
  alert('Комментарий будет отправлен через GitHub Issues. ' +
        'Если вы не авторизованы в GitHub, пожалуйста, войдите в систему.');
}

// Функция для загрузки существующих Issues
async function loadGitHubIssues() {
  const container = document.getElementById('issues-container');
  
  try {
    const response = await fetch(
      `https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/issues?state=open&sort=created&direction=desc&per_page=10`
    );
    
    if (!response.ok) throw new Error('Ошибка загрузки');
    
    const issues = await response.json();
    
    if (issues.length === 0) {
      container.innerHTML = '<p>Пока нет комментариев. Будьте первым!</p>';
      return;
    }
    
    let html = '<div class="issues-list">';
    
    issues.forEach(issue => {
      const date = new Date(issue.created_at).toLocaleDateString('ru-RU');
      const labels = issue.labels.map(label => 
        `<span style="background: #${label.color}; color: white; padding: 3px 8px; 
                     border-radius: 12px; font-size: 0.8em; margin-right: 5px;">
          ${label.name}
        </span>`
      ).join('');
      
      html += `
        <div style="border: 1px solid #e1e4e8; border-radius: 6px; padding: 16px; margin-bottom: 16px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <h4 style="margin: 0;">
              <a href="${issue.html_url}" target="_blank" style="color: #0366d6; text-decoration: none;">
                ${issue.title}
              </a>
            </h4>
            <span style="color: #6a737d; font-size: 0.9em;">${date}</span>
          </div>
          <div style="margin-bottom: 8px;">
            ${labels}
          </div>
          <p style="margin: 0; color: #24292e;">${issue.body.substring(0, 200)}${issue.body.length > 200 ? '...' : ''}</p>
          <div style="margin-top: 8px; display: flex; align-items: center;">
            <img src="${issue.user.avatar_url}" 
                 style="width: 20px; height: 20px; border-radius: 50%; margin-right: 8px;">
            <span style="color: #586069;">${issue.user.login}</span>
            <span style="margin-left: auto; color: #586069;">
              💬 ${issue.comments} ответов
            </span>
          </div>
        </div>
      `;
    });
    
    html += '</div>';
    container.innerHTML = html;
    
  } catch (error) {
    console.error('Ошибка:', error);
    container.innerHTML = `
      <p style="color: #d73a49;">Не удалось загрузить комментарии. 
      <a href="https://github.com/${REPO_OWNER}/${REPO_NAME}/issues" target="_blank">
        Посмотреть все Issues на GitHub
      </a></p>
    `;
  }
}

// Загружаем Issues при загрузке страницы
document.addEventListener('DOMContentLoaded', loadGitHubIssues);

// Кнопка для обновления
container.innerHTML += `
  <button onclick="loadGitHubIssues()" 
          style="margin-top: 20px; padding: 8px 16px; background: #f6f8fa; 
                 border: 1px solid #d1d5da; border-radius: 6px; cursor: pointer;">
    🔄 Обновить комментарии
  </button>
`;
</script>

---

## 📌 Как это работает?

1. **Отправка комментария**: Форма создает новое Issue в вашем репозитории GitHub
2. **Просмотр комментариев**: Загружаются последние Issues и отображаются на странице
3. **Ответы**: Ответить можно прямо в GitHub Issue
4. **Уведомления**: Вы будете получать уведомления на email о новых Issues

## 🔧 Настройка GitHub

Для работы системы убедитесь, что:

1. Репозиторий публичный (или у пользователей есть доступ)
2. Issues включены в репозитории (Settings → Features → Issues)
3. Созданы label (метки) для категорий:
   - `вопрос` (зеленый)
   - `предложение` (желтый)
   - `ошибка` (красный)
   - `благодарность` (синий)