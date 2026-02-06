# Справки Образование

## Требования к услугам

### Общие требования

![Схема1](img/schema_cpravky_totalv1.png) 

## Комментарии и обсуждение

<div style="background: #e3f2fd; padding: 20px; border-radius: 10px; margin: 30px 0;">
  <h3>Обсуждение раздела</h3>
  <p>Есть вопросы или предложения по этому разделу? Присоединяйтесь к обсуждению!</p>
  
  <div style="display: flex; gap: 15px; margin-top: 15px;">
    <a href="../spravki-obrazovanie-comments/"
       style="background: #1976d2; color: white; padding: 12px 24px; 
              border-radius: 6px; text-decoration: none; display: inline-block;">
      Перейти к комментариям
    </a>
    
    <a href="https://github.com/mihailsapogov1978-arch/my-docs/issues/new?labels=Spravky_obr&title=[Вопрос]%20по%20разделу%20'Справки%20Образование'"
       target="_blank"
       style="background: white; color: #1976d2; padding: 12px 24px; 
              border-radius: 6px; text-decoration: none; display: inline-block; border: 1px solid #1976d2;">
      🚀 Задать вопрос на GitHub
    </a>
  </div>
  
  <!-- Последние 3 комментария -->
  <div id="recent-comments" style="margin-top: 20px; background: white; padding: 15px; border-radius: 5px;">
    <p><small>Загрузка последних комментариев...</small></p>
  </div>
</div>

<script>
// Загрузка последних комментариев
async function loadRecentComments() {
  try {
    const response = await fetch(
      'https://api.github.com/repos/mihailsapogov1978-arch/my-docs/issues?labels=Spravky_obr&state=open&sort=updated&direction=desc&per_page=3'
    );
    
    if (response.ok) {
      const issues = await response.json();
      const container = document.getElementById('recent-comments');
      
      if (issues.length === 0) {
        container.innerHTML = '<p><small>Пока нет комментариев. Будьте первым!</small></p>';
        return;
      }
      
      let html = '<p style="margin: 0 0 10px 0; font-weight: bold;">📌 Последние обсуждения:</p>';
      issues.forEach(issue => {
        html += `
          <div style="border-bottom: 1px solid #eee; padding: 8px 0;">
            <a href="${issue.html_url}" target="_blank" style="color: #1976d2; text-decoration: none; font-size: 0.9em;">
              ${issue.title.replace('[Spravky_obr] ', '')}
            </a>
            <br>
            <small style="color: #666;">Обновлено: ${new Date(issue.updated_at).toLocaleDateString('ru-RU')}</small>
          </div>
        `;
      });
      
      container.innerHTML = html;
    }
  } catch (error) {
    console.error('Ошибка загрузки комментариев:', error);
  }
}

document.addEventListener('DOMContentLoaded', loadRecentComments);
</script>