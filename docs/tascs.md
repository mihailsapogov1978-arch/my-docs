# Еженедельные задачи

<style>
  .tasks-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 15px;
    margin: 20px 0;
    font-family: Arial, sans-serif;
  }

  .employee-column {
    background: #fff;
    border: 1px solid #ddd;
    border-radius: 4px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }

  .employee-header {
    background: #e6c378;
    padding: 8px 10px;
    font-weight: bold;
    text-align: center;
    border-bottom: 1px solid #ddd;
    font-size: 14px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 8px;
  }

  .employee-name {
    flex: 1;
    text-align: center;
  }

  .task-counter {
    font-size: 12px;
    background: rgba(255,255,255,0.6);
    padding: 2px 8px;
    border-radius: 10px;
    display: inline-block;
    font-weight: normal;
    white-space: nowrap;
  }

  .task-cell {
    padding: 10px;
    border-bottom: 1px solid #eee;
    min-height: 50px;
    font-size: 13px;
    line-height: 1.4;
    display: flex;
    align-items: flex-start;
    gap: 8px;
    transition: background 0.3s;
  }

  .task-cell:last-child {
    border-bottom: none;
  }

  .task-checkbox {
    margin-top: 3px;
    cursor: pointer;
    width: 16px;
    height: 16px;
    flex-shrink: 0;
  }

  .task-cell.completed {
    background: #d4edda;
    color: #155724;
    text-decoration: line-through;
  }

  .summary-completed {
    background: #d4edda !important;
    color: #155724 !important;
    position: relative;
  }
  
  .summary-completed::after {
    content: "✓";
    position: absolute;
    right: 10px;
    top: 50%;
    transform: translateY(-50%);
    font-weight: bold;
  }

  .section-title {
    grid-column: 1 / -1;
    font-size: 18px;
    font-weight: bold;
    margin: 30px 0 15px;
    padding: 10px;
    background: #f8f9fa;
    border-left: 4px solid #e6c378;
    border-radius: 4px;
  }

  .reset-btn {
    grid-column: 1 / -1;
    padding: 10px 20px;
    background: #dc3545;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 14px;
    margin: 10px 0;
  }

  .reset-btn:hover {
    background: #c82333;
  }

  @media (max-width: 1200px) {
    .tasks-grid { grid-template-columns: repeat(2, 1fr); }
  }
  @media (max-width: 768px) {
    .tasks-grid { grid-template-columns: 1fr; }
    .employee-header {
      flex-wrap: wrap;
    }
    .employee-name {
      width: 100%;
      margin-bottom: 5px;
    }
  }
  .week-container {
    border: 1px #e6c378 solid;
    border-radius: 14px;
    padding: 0 16px;
    margin-bottom: 20px;
  }
</style>

## 10-13 марта 2026 года {#week1}

<div class = "week-container">
    <div class="tasks-grid" id="week1-grid">
    <div class="employee-column" data-col="1">
        <div class="employee-header">
        <span class="employee-name">Ставер А.П.</span>
        <span class="task-counter">0/3</span>
        </div>
        <div class="task-cell"><input type="checkbox" class="task-checkbox" data-id="w1-s1-t1" data-employee="Ставер А.П." data-task="Настроить ЕСИА"><span>Настроить ЕСИА</span></div>
        <div class="task-cell"><input type="checkbox" class="task-checkbox" data-id="w1-s1-t2" data-employee="Ставер А.П." data-task="Написать новость"><span>Написать новость</span></div>
        <div class="task-cell"><input type="checkbox" class="task-checkbox" data-id="w1-s1-t3" data-employee="Ставер А.П." data-task="Провести ВКС по ЕСА"><span>Провести ВКС по ЕСА</span></div>
    </div>
    <div class="employee-column" data-col="2">
        <div class="employee-header">
        <span class="employee-name">Сапогов М.Д.</span>
        <span class="task-counter">0/2</span>
        </div>
        <div class="task-cell"><input type="checkbox" class="task-checkbox" data-id="w1-s2-t1" data-employee="Сапогов М.Д." data-task="Запустить ТЗ ИКТ-Услуга"><span>Согласовать ТЗ ИКТ-Услуга</span></div>
        <div class="task-cell"><input type="checkbox" class="task-checkbox" data-id="w1-s2-t2" data-employee="Сапогов М.Д." data-task="Запустить ТЗ Слияние баз"><span>Согласовать ТЗ на слияние баз</span></div>
        <div class="task-cell"><input type="checkbox" class="task-checkbox" data-id="w1-s2-t2" data-employee="Сапогов М.Д." data-task="Сделать канбан доску для отслеживания задач"><span>Сделать канбан доску для отслеживания задач</span></div>
    </div>
    <div class="employee-column" data-col="3">
        <div class="employee-header">
        <span class="employee-name">Кошик В.В.</span>
        <span class="task-counter">0/2</span>
        </div>
        <div class="task-cell"><input type="checkbox" class="task-checkbox" data-id="w1-s3-t1" data-employee="Кошик В.В." data-task="Список неподписанных МЧД"><span>Список неподписанных МЧД</span></div>
        <div class="task-cell"><input type="checkbox" class="task-checkbox" data-id="w1-s3-t2" data-employee="Кошик В.В." data-task="Предложения в регламент ГИС"><span>Предложения в регламент ГИС</span></div>
    </div>
    <div class="employee-column" data-col="4">
        <div class="employee-header">
        <span class="employee-name">Обмолова В.В.</span>
        <span class="task-counter">0/1</span>
        </div>
        <div class="task-cell"><input type="checkbox" class="task-checkbox" data-id="w1-s4-t1" data-employee="Обмолова В.В." data-task="Вопрос с МУ по оплате"><span>Вопрос с МУ по оплате</span></div>
    </div>
    <div class="employee-column" data-col="5">
        <div class="employee-header">
        <span class="employee-name">Роганова А.А.</span>
        <span class="task-counter">0/1</span>
        </div>
        <div class="task-cell"><input type="checkbox" class="task-checkbox" data-id="w1-s5-t1" data-employee="Роганова А.А." data-task="Распределение прав по приказу"><span>Распределение прав по приказу</span></div>
    </div>
    <div class="employee-column" data-col="6">
        <div class="employee-header">
        <span class="employee-name">Чечеткин М.И.</span>
        <span class="task-counter">0/1</span>
        </div>
        <div class="task-cell"><input type="checkbox" class="task-checkbox" data-id="w1-s6-t1" data-employee="Чечеткин М.И." data-task="Настройка прав по приказу"><span>Настройка прав по приказу</span></div>
    </div>
    <div class="employee-column" data-col="7">
        <div class="employee-header">
        <span class="employee-name">Гасанов С.Н.</span>
        <span class="task-counter">0/1</span>
        </div>
        <div class="task-cell"><input type="checkbox" class="task-checkbox" data-id="w1-s7-t1" data-employee="Гасанов С.Н." data-task="Предложения в регламент ГИС"><span>Предложения в регламент ГИС</span></div>
    </div>
    <div class="employee-column" data-col="8">
        <div class="employee-header">
        <span class="employee-name">Худышкин С.Н.</span>
        <span class="task-counter">0/1</span>
        </div>
        <div class="task-cell"><input type="checkbox" class="task-checkbox" data-id="w1-s8-t1" data-employee="Худышкин С.Н." data-task="Предложения в регламент ГИС"><span>Предложения в регламент ГИС</span></div>
    </div>
    </div>
</div>

## 16-20 марта 2026 года {#week2}

<div class = "week-container">
<div class="tasks-grid" id="week2-grid">
  <div class="employee-column" data-col="1">
    <div class="employee-header">
      <span class="employee-name">Ставер А.П.</span>
      <span class="task-counter">0/3</span>
    </div>
    <div class="task-cell"><input type="checkbox" class="task-checkbox" data-id="w2-s1-t1" data-employee="Ставер А.П." data-task="Собрать пшеницу"><span>Собрать пшеницу</span></div>
    <div class="task-cell"><input type="checkbox" class="task-checkbox" data-id="w2-s1-t2" data-employee="Ставер А.П." data-task="Написать повесть"><span>Написать повесть</span></div>
    <div class="task-cell"><input type="checkbox" class="task-checkbox" data-id="w2-s1-t3" data-employee="Ставер А.П." data-task="Спасти голубя"><span>Спасти голубя</span></div>
  </div>
  <div class="employee-column" data-col="2">
    <div class="employee-header">
      <span class="employee-name">Сапогов М.Д.</span>
      <span class="task-counter">0/2</span>
    </div>
    <div class="task-cell"><input type="checkbox" class="task-checkbox" data-id="w2-s2-t1" data-employee="Сапогов М.Д." data-task="Совершить подвиг"><span>Совершить подвиг</span></div>
    <div class="task-cell"><input type="checkbox" class="task-checkbox" data-id="w2-s2-t2" data-employee="Сапогов М.Д." data-task="Сплести 5 венков"><span>Сплести 5 венков</span></div>
  </div>
  <div class="employee-column" data-col="3">
    <div class="employee-header">
      <span class="employee-name">Кошик В.В.</span>
      <span class="task-counter">0/2</span>
    </div>
    <div class="task-cell"><input type="checkbox" class="task-checkbox" data-id="w2-s3-t1" data-employee="Кошик В.В." data-task="Построить дом"><span>Построить дом</span></div>
    <div class="task-cell"><input type="checkbox" class="task-checkbox" data-id="w2-s3-t2" data-employee="Кошик В.В." data-task="Посадить дерево"><span>Посадить дерево</span></div>
  </div>
  <div class="employee-column" data-col="4">
    <div class="employee-header">
      <span class="employee-name">Обмолова В.В.</span>
      <span class="task-counter">0/1</span>
    </div>
    <div class="task-cell"><input type="checkbox" class="task-checkbox" data-id="w2-s4-t1" data-employee="Обмолова В.В." data-task="Пересадить цветок Сапогову"><span>Пересадить цветок Сапогову</span></div>
  </div>
  <div class="employee-column" data-col="5">
    <div class="employee-header">
      <span class="employee-name">Роганова А.А.</span>
      <span class="task-counter">0/2</span>
    </div>
    <div class="task-cell"><input type="checkbox" class="task-checkbox" data-id="w2-s5-t1" data-employee="Роганова А.А." data-task="Разговоры по телефону"><span>Разговоры по телефону</span></div>
    <div class="task-cell"><input type="checkbox" class="task-checkbox" data-id="w2-s5-t2" data-employee="Роганова А.А." data-task="Контрольная по геометрии"><span>Контрольная по геометрии</span></div>
  </div>
  <div class="employee-column" data-col="6">
    <div class="employee-header">
      <span class="employee-name">Чечеткин М.И.</span>
      <span class="task-counter">0/2</span>
    </div>
    <div class="task-cell"><input type="checkbox" class="task-checkbox" data-id="w2-s6-t1" data-employee="Чечеткин М.И." data-task="Взять проектор (203 каб)"><span>Взять проектор (203 каб)</span></div>
    <div class="task-cell"><input type="checkbox" class="task-checkbox" data-id="w2-s6-t2" data-employee="Чечеткин М.И." data-task="Отнести проектор (203 каб)"><span>Отнести проектор (203 каб)</span></div>
  </div>
  <div class="employee-column" data-col="7">
    <div class="employee-header">
      <span class="employee-name">Гасанов С.Н.</span>
      <span class="task-counter">0/1</span>
    </div>
    <div class="task-cell"><input type="checkbox" class="task-checkbox" data-id="w2-s7-t1" data-employee="Гасанов С.Н." data-task="Отдыхать"><span>Отдыхать</span></div>
  </div>
  <div class="employee-column" data-col="8">
    <div class="employee-header">
      <span class="employee-name">Худышкин С.Н.</span>
      <span class="task-counter">0/1</span>
    </div>
    <div class="task-cell"><input type="checkbox" class="task-checkbox" data-id="w2-s8-t1" data-employee="Худышкин С.Н." data-task="Предложения в регламент ГИС"><span>Предложения в регламент ГИС</span></div>
  </div>
</div>
</div>

## Сводная информация — Март 2026 {#summary}
<div class = "week-container">
<div class="tasks-grid" id="summary-grid">
  <div class="employee-column" data-employee-col="Ставер А.П.">
    <div class="employee-header">
      <span class="employee-name">Ставер А.П.</span>
      <span class="task-counter">6 задач</span>
    </div>
    <div class="task-cell summary-task" data-employee="Ставер А.П." data-task="Настроить ЕСИА">• Настроить ЕСИА</div>
    <div class="task-cell summary-task" data-employee="Ставер А.П." data-task="Написать новость">• Написать новость</div>
    <div class="task-cell summary-task" data-employee="Ставер А.П." data-task="Провести ВКС по ЕСА">• Провести ВКС по ЕСА</div>
    <div class="task-cell summary-task" data-employee="Ставер А.П." data-task="Собрать пшеницу">• Собрать пшеницу</div>
    <div class="task-cell summary-task" data-employee="Ставер А.П." data-task="Написать повесть">• Написать повесть</div>
    <div class="task-cell summary-task" data-employee="Ставер А.П." data-task="Спасти голубя">• Спасти голубя</div>
  </div>
  <div class="employee-column" data-employee-col="Сапогов М.Д.">
    <div class="employee-header">
      <span class="employee-name">Сапогов М.Д.</span>
      <span class="task-counter">4 задачи</span>
    </div>
    <div class="task-cell summary-task" data-employee="Сапогов М.Д." data-task="Запустить ТЗ ИКТ-Услуга">• Запустить ТЗ ИКТ-Услуга</div>
    <div class="task-cell summary-task" data-employee="Сапогов М.Д." data-task="Запустить ТЗ Слияние баз">• Запустить ТЗ Слияние баз</div>
    <div class="task-cell summary-task" data-employee="Сапогов М.Д." data-task="Совершить подвиг">• Совершить подвиг</div>
    <div class="task-cell summary-task" data-employee="Сапогов М.Д." data-task="Сплести 5 венков">• Сплести 5 венков</div>
  </div>
  <div class="employee-column" data-employee-col="Кошик В.В.">
    <div class="employee-header">
      <span class="employee-name">Кошик В.В.</span>
      <span class="task-counter">4 задачи</span>
    </div>
    <div class="task-cell summary-task" data-employee="Кошик В.В." data-task="Список неподписанных МЧД">• Список неподписанных МЧД</div>
    <div class="task-cell summary-task" data-employee="Кошик В.В." data-task="Предложения в регламент ГИС">• Предложения в регламент ГИС</div>
    <div class="task-cell summary-task" data-employee="Кошик В.В." data-task="Построить дом">• Построить дом</div>
    <div class="task-cell summary-task" data-employee="Кошик В.В." data-task="Посадить дерево">• Посадить дерево</div>
  </div>
  <div class="employee-column" data-employee-col="Обмолова В.В.">
    <div class="employee-header">
      <span class="employee-name">Обмолова В.В.</span>
      <span class="task-counter">2 задачи</span>
    </div>
    <div class="task-cell summary-task" data-employee="Обмолова В.В." data-task="Вопрос с МУ по оплате">• Вопрос с МУ по оплате</div>
    <div class="task-cell summary-task" data-employee="Обмолова В.В." data-task="Пересадить цветок Сапогову">• Пересадить цветок Сапогову</div>
  </div>
  <div class="employee-column" data-employee-col="Роганова А.А.">
    <div class="employee-header">
      <span class="employee-name">Роганова А.А.</span>
      <span class="task-counter">3 задачи</span>
    </div>
    <div class="task-cell summary-task" data-employee="Роганова А.А." data-task="Распределение прав по приказу">• Распределение прав по приказу</div>
    <div class="task-cell summary-task" data-employee="Роганова А.А." data-task="Разговоры по телефону">• Разговоры по телефону</div>
    <div class="task-cell summary-task" data-employee="Роганова А.А." data-task="Контрольная по геометрии">• Контрольная по геометрии</div>
  </div>
  <div class="employee-column" data-employee-col="Чечеткин М.И.">
    <div class="employee-header">
      <span class="employee-name">Чечеткин М.И.</span>
      <span class="task-counter">3 задачи</span>
    </div>
    <div class="task-cell summary-task" data-employee="Чечеткин М.И." data-task="Настройка прав по приказу">• Настройка прав по приказу</div>
    <div class="task-cell summary-task" data-employee="Чечеткин М.И." data-task="Взять проектор (203 каб)">• Взять проектор (203 каб)</div>
    <div class="task-cell summary-task" data-employee="Чечеткин М.И." data-task="Отнести проектор (203 каб)">• Отнести проектор (203 каб)</div>
  </div>
  <div class="employee-column" data-employee-col="Гасанов С.Н.">
    <div class="employee-header">
      <span class="employee-name">Гасанов С.Н.</span>
      <span class="task-counter">2 задачи</span>
    </div>
    <div class="task-cell summary-task" data-employee="Гасанов С.Н." data-task="Предложения в регламент ГИС">• Предложения в регламент ГИС</div>
    <div class="task-cell summary-task" data-employee="Гасанов С.Н." data-task="Отдыхать">• Отдыхать</div>
  </div>
  <div class="employee-column" data-employee-col="Худышкин С.Н.">
    <div class="employee-header">
      <span class="employee-name">Худышкин С.Н.</span>
      <span class="task-counter">2 задачи</span>
    </div>
    <div class="task-cell summary-task" data-employee="Худышкин С.Н." data-task="Предложения в регламент ГИС">• Предложения в регламент ГИС (×2)</div>
  </div>
</div>
</div>
<button class="reset-btn" onclick="resetAllCheckboxes()">Сбросить все отметки</button>

<script>
  const STORAGE_KEY = 'tasks_checkboxes_state_v1';

  function loadCheckboxState() {
    const saved = localStorage.getItem(STORAGE_KEY);
    return saved ? JSON.parse(saved) : {};
  }

  function saveCheckboxState(state) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
  }

  function updateCounter(column) {
    const checkboxes = column.querySelectorAll('.task-checkbox');
    const completed = column.querySelectorAll('.task-checkbox:checked').length;
    const total = checkboxes.length;
    const counterSpan = column.querySelector('.task-counter');
    if(counterSpan) {
      counterSpan.textContent = `${completed}/${total}`;
    }
  }

  function updateAllCounters() {
    document.querySelectorAll('.employee-column').forEach(col => updateCounter(col));
  }
  
  function updateSummaryTasks() {
    const savedState = loadCheckboxState();
    
    // Сначала убираем все выделения в сводной таблице
    document.querySelectorAll('.summary-task').forEach(task => {
      task.classList.remove('summary-completed');
    });
    
    // Для каждой отмеченной задачи в сохраненном состоянии
    Object.keys(savedState).forEach(taskId => {
      // Находим чекбокс по data-id
      const checkbox = document.querySelector(`.task-checkbox[data-id="${taskId}"]`);
      if (checkbox) {
        const employee = checkbox.getAttribute('data-employee');
        const taskText = checkbox.getAttribute('data-task');
        
        // Находим соответствующую задачу в сводной таблице
        const summaryTasks = document.querySelectorAll('.summary-task');
        summaryTasks.forEach(summaryTask => {
          const summaryEmployee = summaryTask.getAttribute('data-employee');
          const summaryTaskText = summaryTask.getAttribute('data-task');
          
          // Сравниваем сотрудника и текст задачи
          if (summaryEmployee === employee && summaryTaskText === taskText) {
            summaryTask.classList.add('summary-completed');
          }
        });
      }
    });
  }

  document.addEventListener('DOMContentLoaded', function() {
    const savedState = loadCheckboxState();
    const grids = ['week1-grid', 'week2-grid'];

    grids.forEach(gridId => {
      const grid = document.getElementById(gridId);
      if(!grid) return;

      grid.querySelectorAll('.task-checkbox').forEach(checkbox => {
        const taskId = checkbox.getAttribute('data-id');
        if(savedState[taskId]) {
          checkbox.checked = true;
          const cell = checkbox.closest('.task-cell');
          if(cell) cell.classList.add('completed');
        }

        checkbox.addEventListener('change', function() {
          const cell = this.closest('.task-cell');
          const column = this.closest('.employee-column');
          const taskId = this.getAttribute('data-id');

          if(this.checked) {
            cell.classList.add('completed');
            savedState[taskId] = true;
          } else {
            cell.classList.remove('completed');
            delete savedState[taskId];
          }
          saveCheckboxState(savedState);
          updateCounter(column);
          updateSummaryTasks(); // Обновляем сводную информацию
        });
      });

      grid.querySelectorAll('.employee-column').forEach(col => updateCounter(col));
    });
    
    // Первоначальное обновление сводной информации
    updateSummaryTasks();
  });

  function resetAllCheckboxes() {
    if(confirm('Вы уверены, что хотите сбросить все отметки?')) {
      localStorage.removeItem(STORAGE_KEY);
      document.querySelectorAll('.task-checkbox').forEach(checkbox => {
        checkbox.checked = false;
        const cell = checkbox.closest('.task-cell');
        if(cell) cell.classList.remove('completed');
      });
      updateAllCounters();
      updateSummaryTasks(); // Обновляем сводную информацию после сброса
    }
  }
</script>