<style>
/* ===== Единая сетка колонок для шапки и строк ===== */
.emp-total,
.md-typeset .emp-summary,
.emp-summary {
    display: grid !important;
    /*          ФИО    Сотрудников  Звонков  Задач   Заявок   Резолюций */
    grid-template-columns: 1fr  120px  130px  110px  110px  120px;
    align-items: center !important;
    gap: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
}

/* ===== Шапка отдела ===== */
.emp-total {
    background: #ebf8ff;
    border: 1px solid #bee3f8;
    border-radius: 8px;
    margin: 10px 0 12px 0 !important;
    font-size: 13px;
    color: #2c5282;
}
.emp-total > span {
    padding: 10px 8px;
    white-space: nowrap;
}
.emp-total-name {
    padding-left: 14px !important;
    font-weight: 600;
    color: #2b6cb0;
}
.emp-total b { color: #2b6cb0; }

/* ===== Список сотрудников ===== */
.emp-list {
    margin: 16px 0;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    overflow: hidden;
    background: #fff;
}

.md-typeset .emp-row,
.emp-row {
    border: none !important;
    outline: none !important;
    box-shadow: none !important;
    border-bottom: 1px solid #eef2f6 !important;
    margin: 0 !important;
    padding: 0 !important;
}
.emp-row:last-child { border-bottom: none !important; }

/* Summary — тоже grid, те же колонки */
.md-typeset .emp-summary,
.emp-summary {
    cursor: pointer;
    list-style: none !important;
    font-size: 13px;
    line-height: 1.3;
    transition: background 0.15s;
    outline: none !important;
    box-shadow: none !important;
    border: none !important;
    padding-inline-start: 0 !important;
}

/* Все маркеры summary — убрать */
.md-typeset .emp-summary::-webkit-details-marker,
.emp-summary::-webkit-details-marker { display: none !important; }
.md-typeset .emp-summary::marker,
.emp-summary::marker { display: none !important; content: "" !important; }
.md-typeset .emp-summary::before,
.emp-summary::before { display: none !important; content: none !important; }

.emp-summary:hover { background: #f7fafc; }

/* Без синей рамки фокуса */
.md-typeset .emp-row:focus,
.md-typeset .emp-row:focus-visible,
.md-typeset .emp-row:focus-within,
.md-typeset .emp-summary:focus,
.md-typeset .emp-summary:focus-visible {
    outline: none !important;
    box-shadow: none !important;
    border-color: transparent !important;
}

/* ===== Ячейки строки ===== */
.emp-summary > span {
    padding: 10px 8px;
    vertical-align: middle;
    white-space: nowrap;
}

.md-typeset .emp-name,
.emp-name {
    font-weight: 700;
    color: #2c3e50;
    text-transform: uppercase;
    letter-spacing: 0.02em;
    padding-left: 14px !important;
    text-align: left;
}

/* Чипы — «раскрываем» в те же ячейки grid-сетки */
.emp-chips { display: contents !important; }

.md-typeset .chip,
.chip {
    padding: 10px 8px !important;
    font-size: 12px;
    line-height: 1.3;
    white-space: nowrap !important;
    background: transparent !important;
    border-radius: 0 !important;
    text-align: left !important;
    width: auto !important;
}
.chip b { font-weight: 700; }

.chip.calls  { color: #2b6cb0; }
.chip.tasks  { color: #2c7a7b; }
.chip.tickets{ color: #744210; }
.chip.res    { color: #6b46c1; }

/* ===== Тело раскрытой карточки ===== */
.md-typeset .emp-body,
.emp-body {
    padding: 4px 14px 12px 14px !important;
    background: #fafbfc;
    font-size: 12.5px;
    color: #2d3748;
}
.emp-tasks {
    margin: 0;
    padding-left: 18px;
    line-height: 1.5;
}
.emp-tasks li { margin-bottom: 4px; }

/* Узкие экраны */
@media (max-width: 900px) {
    .emp-total,
    .md-typeset .emp-summary,
    .emp-summary {
        grid-template-columns: 1fr !important;
        gap: 6px !important;
    }
    .emp-total > span,
    .emp-summary > span { padding: 4px 14px; }
    .emp-chips {
        display: flex !important;
        flex-wrap: wrap;
        gap: 8px;
        padding-left: 14px;
    }
    .chip { padding: 2px 8px !important; }
}
</style>

# Отчёты отдела СРТП

## Сентябрь 2026

<div markdown="1">

<div class="emp-total"><span class="emp-total-name">Отдел СРТП</span><span class="emp-total-cell">Сотрудников: <b>7</b></span><span class="emp-total-cell">Звонков: <b>2873</b></span><span class="emp-total-cell">Задач: <b>43</b></span><span class="emp-total-cell">Заявок: <b>47</b></span><span class="emp-total-cell">Резолюций: <b>9</b></span></div>

<div class="emp-list">
<details class="emp-row"><summary class="emp-summary"><span class="emp-name">Сапогов</span><span class="emp-chips"><span class="chip calls">Звонков: <b>513</b></span><span class="chip tasks">Задач: <b>9</b></span><span class="chip tickets">Заявок: <b>8</b></span><span class="chip res">Резолюций: <b>9</b></span></span></summary><div class="emp-body"><ul class="emp-tasks"><li>Подготовил изменения в Положение о ГИС &quot;Смета ЯНАО&quot;</li><li>Актуализировал пакет документов (заявка) на регистрацию модуля ИИ в Роспатент. Заявка рассмотрена положительно, модуль (программа) внесено в реестр программ для ЭВМ.</li><li>Скорректировал предварительный ПИ на 2027 год. Предварительно согласован ДИТиС.</li><li>Скорректировал ПИ на 2026 год, согласован ДИТиС.</li><li>Принял участие в актуализации списков организаций (муниципальных и окружных)</li><li>Направил ежемесячные отчеты по аудиту ПО и импортзамещению в ДИТиС (через депфин).</li><li>Актуализировал и направил на согласование ТЗ по администрированию Сметы</li><li>Подготовил новость (не публиковали еще) для работников органов власти об использовании приложения для агрегации сформированных отчетов об отпуске или командировке.</li><li>Подготовил письмо в РЦОКО для взаимодействия с ГИС «Ямал Образование» через СМЭВ.</li></ul></div></details>
<details class="emp-row"><summary class="emp-summary"><span class="emp-name">Мулявин</span><span class="emp-chips"><span class="chip calls">Звонков: <b>151</b></span><span class="chip tasks">Задач: <b>6</b></span><span class="chip tickets">Заявок: <b>8</b></span></span></summary><div class="emp-body"><ul class="emp-tasks"><li>Завершена проработка перехода на «Астрал»: подготовлены итоговые материалы и дорожная карта, уточнены вопросы с НПО «Криста», задача закрыта в РСЭД «ТЕЗИС».</li><li>Разработан Excel-парсер на Python для автоматической обработки и агрегации отчётных данных. Приложение протестировано на Windows и RedOS 7.3/8, подготовлена версия для распространения пользователям, а также инструкции по работе, в том числе пошаговая инструкция со скриншотами.</li><li>Развернут и настроен тестовый агент СМЭВ4: проверено подключение к брокерам и выполнение запросов. При тестировании доступа к витрине выявлено отсутствие необходимых прав, организовано взаимодействие с РЦОКО для их предоставления.</li><li>Проведена работа по применению ИИ для распознавания документов: протестирован Extraction Studio, изучено взаимодействие через Swagger API и проработан Python-контур для автоматического распознавания и извлечения данных из документов.</li><li>Продолжена работа по ЕСКУ: обработка обращений и ошибок, анализ выгрузок и показателей дашбордов FIN_04 и аппарата, а также собственной выгрузки за двухмесячный период. По выявленным проблемам направлялись обращения и проверялись результаты исправлений.</li><li>Разработан бот для автоматизации уведомлений о паролях для отдела информационной безопасности.</li></ul></div></details>
<details class="emp-row"><summary class="emp-summary"><span class="emp-name">Кошик</span><span class="emp-chips"><span class="chip calls">Звонков: <b>325</b></span><span class="chip tasks">Задач: <b>9</b></span><span class="chip tickets">Заявок: <b>2</b></span></span></summary><div class="emp-body"><ul class="emp-tasks"><li>Аудит по использованию Сметы и подготовка общего свода (Надымский р-н - 77, Губкинский - 47, Салехард - 57, Пуровский р-н - 64).</li><li>Сбор недостающих оферт по ГУ и МО - 2.</li><li>Написано инструкций и выложено на сайт ЦБ ОГВ - 3.</li><li>Настройка ЭДО Астрал для Департамента тарифной политики - 1.</li><li>Оформлено МЧД в ФНС, Росстат для Департамента тарифной политики - 6.</li><li>Внедрение и отработка механизма кроссподписания при передаче имущества из муниципального в региональный бюджет (ф.0510448, ф.0504805) - Пуровский р-н - 1</li><li>Подготовка свода по работе МО с документами 61н. - 1</li><li>Заявки / обращения от МО через чаты и по телефону &gt;= 100.</li><li>Взаимодействие с представителями подрядчиков (Fargos, Krista) по централизации Сметы в рабочих чатах MAX.</li></ul></div></details>
<details class="emp-row"><summary class="emp-summary"><span class="emp-name">Худышкин</span><span class="emp-chips"><span class="chip calls">Звонков: <b>313</b></span><span class="chip tasks">Задач: <b>7</b></span><span class="chip tickets">Заявок: <b>3</b></span></span></summary><div class="emp-body"><ul class="emp-tasks"><li>Консультирование и техническая поддержка муниципальных образований по вопросам подключения, настройки и эксплуатации централизованной ГИС «Смета ЯНАО». Анализ используемых настроек и функционала, выявление участков, требующих дополнительной настройки или консультационного сопровождения.</li><li>Проведение аудита баз муниципальных образований на предмет   использования функциональных возможностей, предусмотренных ГИС «Смета  ЯНАО».</li><li>Работа с учреждениями и ответственными специалистами:</li><li>Сбор, проверка и актуализация контактных данных ответственных лиц  учреждений, кадровых работников и специалистов бухгалтерских служб.</li><li>Оповещение учреждений о необходимости проведения сопоставления  справочников в ГИС ЕСКУ и ГИС «Смета ЯНАО». Консультирование кадровых  работников и бухгалтеров по вопросам подготовки данных и организации  интеграционного взаимодействия.</li><li>Координация действий учреждений при возникновении вопросов и ошибок в  процессе обмена данными между информационными системами.</li><li>Консультирование и настройка функционала, связанного с перечислением  денежных средств на карты платёжной системы «Мир» в базах муниципальных  образований.</li></ul></div></details>
<details class="emp-row"><summary class="emp-summary"><span class="emp-name">Чечеткин</span><span class="emp-chips"><span class="chip calls">Звонков: <b>1104</b></span><span class="chip tasks">Задач: <b>6</b></span><span class="chip tickets">Заявок: <b>20</b></span></span></summary><div class="emp-body"><ul class="emp-tasks"><li>Приказы на доступ ОУ - 6</li><li>Оферты по МБТ - 5</li><li>Приказы ЦБ на доступ - 5</li><li>Замещение с 02.09 по 06.09 Начальника отдела и Ведущих специалистов отдела</li><li>Исправление ошибок ГИС &quot;ГМП&quot; после смены реквизитов Казначейства</li><li>Работа по подписанию между базами ф.0504805 05104548</li></ul></div></details>
<details class="emp-row"><summary class="emp-summary"><span class="emp-name">Гасанов</span><span class="emp-chips"><span class="chip calls">Звонков: <b>89</b></span><span class="chip tasks">Задач: <b>3</b></span><span class="chip tickets">Заявок: <b>1</b></span></span></summary><div class="emp-body"><ul class="emp-tasks"><li>до 11.09 находился в отпуске, Акутализация сдений в &quot;Реестр Оферт&quot;</li><li>Взаимодействие с представителями подрядчиков (Fargos, Krista) по заявочным вопросам Сметы в рабочих чатах МАКС.</li><li>Консультация / тех. поддержка / маршрутизация заявок муниципалитетов (ГИС ГМП, МИР, ПП).</li></ul></div></details>
<details class="emp-row"><summary class="emp-summary"><span class="emp-name">Роганова</span><span class="emp-chips"><span class="chip calls">Звонков: <b>378</b></span><span class="chip tasks">Задач: <b>3</b></span><span class="chip tickets">Заявок: <b>5</b></span></span></summary><div class="emp-body"><ul class="emp-tasks"><li>Обработано приказов на временное / постоянное распределения обязанностей сотрудников ЦБ в Смете - 7 шт.</li><li>Обработано заявлений о присоединении (Оферта) - 2 шт.</li><li>Обработано приказов о предоставлении доступа к ГИС Смета (ИОГВ) - 5 шт.</li></ul></div></details>
</div>

</div>


## Август 2026

<div markdown="1">

<div class="emp-total"><span class="emp-total-name">Отдел СРТП</span><span class="emp-total-cell">Сотрудников: <b>5</b></span><span class="emp-total-cell">Звонков: <b>1923</b></span><span class="emp-total-cell">Задач: <b>20</b></span><span class="emp-total-cell">Заявок: <b>54</b></span><span class="emp-total-cell">Резолюций: <b>13</b></span></div>

<div class="emp-list">
<details class="emp-row"><summary class="emp-summary"><span class="emp-name">Сапогов</span><span class="emp-chips"><span class="chip calls">Звонков: <b>803</b></span><span class="chip tasks">Задач: <b>6</b></span><span class="chip tickets">Заявок: <b>24</b></span><span class="chip res">Резолюций: <b>13</b></span></span></summary><div class="emp-body"><ul class="emp-tasks"><li>Проводилась подготовка ТЗ на выполнение работ по интеграции с РСЭД Тезис</li><li>Организация и взаимодействие с участниками и техподдержкой по настройке и тестировании  кроссподписания.</li><li>Проверка мероприятий предварительных ПИ на 2027 год среди МО и департамента здравоохранения.</li><li>Проводилась работа по администрированию, настройке прав, технической поддержке и решения иных вопросов на период отсутствия Чечеткина М.И., Обмоловой В.В. Рогановой А.И.</li><li>Подготовлены критерии для отчета по отслеживанию динамики авторизации через ЕСИА, сформулированы требования для отчета по командировкам и отпускам (заявки), решены несколько вопросов по ошибкам при импорте данных УКТ-Услуга, направлен отзыв заявки на регистрацию программы для ЭВМ (ИИ) чтобы повторно не платить пошлину.</li><li>Направлены ежемесячные отчеты по аудиту ПО и импортзамещению в ДИТиС (через депфин)</li></ul></div></details>
<details class="emp-row"><summary class="emp-summary"><span class="emp-name">Кошик</span><span class="emp-chips"><span class="chip calls">Звонков: <b>45</b></span><span class="chip tasks">Задач: <b>1</b></span><span class="chip tickets">Заявок: <b>2</b></span></span></summary><div class="emp-body"><ul class="emp-tasks"><li>Сбор статистики по муниципалитетам - использования интеграции по направлениям: МИР, ПП, ЭДО, СФР, Имущество и т.п.</li></ul></div></details>
<details class="emp-row"><summary class="emp-summary"><span class="emp-name">Худышкин</span><span class="emp-chips"><span class="chip calls">Звонков: <b>206</b></span><span class="chip tasks">Задач: <b>6</b></span><span class="chip tickets">Заявок: <b>13</b></span></span></summary><div class="emp-body"><ul class="emp-tasks"><li>Работа Техфоргосом, Мароп и Аппаратом Губернатора для утверждения и построения рабочего процесса (консолидация информации всеми сторонами) интеграции с ЕСКУ.</li><li>Восстановление подключений Imon ГКУ.drx . Поддержка и администрирование ИОГВ с 04.08.2026 по 12.08.2026. Поддержка, администрирование  и консультация по  ГИС АПК и Астралу.  Работа по организации интеграции ГИС ЕСКУ и ГИС Сметы. Оповещеие учреждений о сопостовлении справочников, консультация.    Взаимодействие с представителями подрядчиков (Мароп, Хендисофт, Аппарат Губернатора) для согласования и реализации доработок по интеграции.</li><li>Взаимодействие с представителями подрядчиков (Fargos, Krista) по централизации Сметы в рабочих чатах Мах и по телефону.</li><li>Консультация / тех. поддержка / маршрутизация заявок муниципалитетов в части подключения и настройки централизованной Сметы ЯНАО.</li><li>Поддержка по настройкам ГИС ГМП, ГИС Имущество, перечеисление на карты МИР в базах муниципалитетов.</li><li>Работы с базами муниципалитетов. Курирование работы функционала интеграции ГИС ЕСКУ и Сметы в ЦБ ОГВ ЯНАО.</li></ul></div></details>
<details class="emp-row"><summary class="emp-summary"><span class="emp-name">Чечеткин</span><span class="emp-chips"><span class="chip calls">Звонков: <b>677</b></span><span class="chip tasks">Задач: <b>3</b></span><span class="chip tickets">Заявок: <b>7</b></span></span></summary><div class="emp-body"><ul class="emp-tasks"><li>Предоставление доступа сотрудника ОУ - 3 приказа;</li><li>Устранение проблемы с созданием МЧД;</li><li>Работа по внедрению подписания ф.0510448 и 0504805 между базами и устранение ошибок;</li></ul></div></details>
<details class="emp-row"><summary class="emp-summary"><span class="emp-name">Мулявин</span><span class="emp-chips"><span class="chip calls">Звонков: <b>192</b></span><span class="chip tasks">Задач: <b>4</b></span><span class="chip tickets">Заявок: <b>8</b></span></span></summary><div class="emp-body"><ul class="emp-tasks"><li>Проведена работа по переходу на «Астрал»: изучены текущий и целевой бизнес-процессы сдачи отчётности, собрана обратная связь пользователей и уточнены вопросы с НПО «Криста». Подготовлены дорожная карта перехода и BPMN-схемы процессов работы через «Контур» и «Астрал».</li><li>Для загрузки данных по медалистам с помощью Python-скрипта обработаны данные по 537 детям, выполнена сверка и распределение по 13 территориям, подготовлены 13 Excel- и 13 CSV-файлов для загрузки в ГИС «Смета ЯНАО».</li><li>Проводилась обработка обращений пользователей по ЕСКУ и другим вопросам ГИС «Смета ЯНАО»: анализ ошибок, проверка выгрузок и данных, подготовка заявок в НПО «Криста» и контроль исправлений.</li><li>Оказана помощь в проработке нового ТЗ по платёжным поручениям: рассмотрено совмещение планируемых доработок со стороны НПО «Криста» и функционала РСЭД «ТЕЗИС».</li></ul></div></details>
</div>

</div>


## Июль 2026

<div markdown="1">

<div class="emp-total"><span class="emp-total-name">Отдел СРТП</span><span class="emp-total-cell">Сотрудников: <b>9</b></span><span class="emp-total-cell">Звонков: <b>2350</b></span><span class="emp-total-cell">Задач: <b>26</b></span><span class="emp-total-cell">Заявок: <b>27</b></span><span class="emp-total-cell">Резолюций: <b>13</b></span></div>

<div class="emp-list">
<details class="emp-row"><summary class="emp-summary"><span class="emp-name">Ставер</span><span class="emp-chips"><span class="chip calls">Звонков: <b>354</b></span><span class="chip tasks">Задач: <b>1</b></span><span class="chip tickets">Заявок: <b>1</b></span><span class="chip res">Резолюций: <b>11</b></span></span></summary><div class="emp-body"><ul class="emp-tasks"><li>Проведены консультации на тему ввода нового функционала с разработчиками Сметы; с департаментом ИТ и связи на тему мероприятий по плану информатизации; методологами на тему бизнес-процессов действующих интеграций в целях выявления ошибок в пограничных зонах ответственности. Выполнена настройка и тестирование авторизации через ЕСИА в ЛК ПОЛ</li></ul></div></details>
<details class="emp-row"><summary class="emp-summary"><span class="emp-name">Сапогов</span><span class="emp-chips"><span class="chip calls">Звонков: <b>99</b></span><span class="chip tasks">Задач: <b>3</b></span><span class="chip tickets">Заявок: <b>3</b></span><span class="chip res">Резолюций: <b>2</b></span></span></summary><div class="emp-body"><ul class="emp-tasks"><li>Актуализировано и направлено на согласование ТЗ на выполнение работ по интеграции с РСЭД Тезис с учетом замечаний от ДИТиС. Работа по размещению предварительного ПИ на 2027 год.</li><li>Выполнение настроек уведомлений для сотрудников отдела расчетов с персоналом (авансники).</li><li>Проводиться работа по размещению предварительного плана информатизации на 2027 год.</li></ul></div></details>
<details class="emp-row"><summary class="emp-summary"><span class="emp-name">Обмолова</span><span class="emp-chips"><span class="chip calls">Звонков: <b>448</b></span><span class="chip tasks">Задач: <b>1</b></span><span class="chip tickets">Заявок: <b>0</b></span></span></summary><div class="emp-body"><ul class="emp-tasks"><li>Исправление ошибок при синхронизации с ЕСКУ; Работа с муниципальными учреждениям Здравоохранения ЯНАО, подготовка к полугодовой отчетности</li></ul></div></details>
<details class="emp-row"><summary class="emp-summary"><span class="emp-name">Кошик</span><span class="emp-chips"><span class="chip calls">Звонков: <b>180</b></span><span class="chip tasks">Задач: <b>2</b></span><span class="chip tickets">Заявок: <b>1</b></span></span></summary><div class="emp-body"><ul class="emp-tasks"><li>Сбор статистики по муниципалитетам - использования интеграции по направлениям: МИР, ПП, ЭДО, СФР, Имущество и т.п.</li><li>Взаимодействие с представителями подрядчиков (Fargos, Krista) по централизации Сметы в рабочих чатах MAX.</li></ul></div></details>
<details class="emp-row"><summary class="emp-summary"><span class="emp-name">Худышкин</span><span class="emp-chips"><span class="chip calls">Звонков: <b>32</b></span><span class="chip tasks">Задач: <b>2</b></span><span class="chip tickets">Заявок: <b>0</b></span></span></summary><div class="emp-body"><ul class="emp-tasks"><li>Сбор статистики предоставленных муниципалитетами актов о принятии работ по интеграции с ЕСКУ</li><li>Взаимодействие с представителями подрядчиков (Fargos, Krista) по централизации Сметы в рабочих чатах MAX.</li></ul></div></details>
<details class="emp-row"><summary class="emp-summary"><span class="emp-name">Гасанов</span><span class="emp-chips"><span class="chip calls">Звонков: <b>171</b></span><span class="chip tasks">Задач: <b>3</b></span><span class="chip tickets">Заявок: <b>2</b></span></span></summary><div class="emp-body"><ul class="emp-tasks"><li>Сбор статистики по муниципалитетам - использования интеграции по направлениям: МИР, ПП, ЭДО, СФР, Имущество и т.п.</li><li>Взаимодействие с представителями подрядчиков (Fargos, Krista) по заявочным вопросам Сметы в рабочих чатах Max.</li><li>Консультация / тех. поддержка / маршрутизация заявок муниципалитетов (ГИС ГМП, МИР, ПП).</li></ul></div></details>
<details class="emp-row"><summary class="emp-summary"><span class="emp-name">Чечеткин</span><span class="emp-chips"><span class="chip calls">Звонков: <b>501</b></span><span class="chip tasks">Задач: <b>5</b></span><span class="chip tickets">Заявок: <b>3</b></span></span></summary><div class="emp-body"><ul class="emp-tasks"><li>Дежурство 4-5 июля по запросу отдела подготовки отчетности на совещание;</li><li>Предоставление доступа Аудиторам -1;</li><li>Приказы ОУ на доступ -1;</li><li>Решение проблем при созданий МЧД в ГИС &quot;СМЕТА ЯНАО&quot;;</li><li>Принятия участия в устранениях последствий после аваринного отключения электроэнергий.</li></ul></div></details>
<details class="emp-row"><summary class="emp-summary"><span class="emp-name">Роганова</span><span class="emp-chips"><span class="chip calls">Звонков: <b>431</b></span><span class="chip tasks">Задач: <b>3</b></span><span class="chip tickets">Заявок: <b>7</b></span></span></summary><div class="emp-body"><ul class="emp-tasks"><li>Обработано приказов на временное / постоянное распределения обязанностей сотрудников ЦБ в Смете - 6 шт.</li><li>Обработано заявлений о присоединении (Оферта) - 2 шт.</li><li>Обработано приказов о предоставлении доступа к ГИС Смета (ИОГВ) - 3 шт.</li></ul></div></details>
<details class="emp-row"><summary class="emp-summary"><span class="emp-name">Мулявин</span><span class="emp-chips"><span class="chip calls">Звонков: <b>134</b></span><span class="chip tasks">Задач: <b>6</b></span><span class="chip tickets">Заявок: <b>10</b></span></span></summary><div class="emp-body"><ul class="emp-tasks"><li>Проведён анализ ошибок интеграции с ЕСКУ по 50 организациям: обработано около 100 тыс. записей, выявлены основные типы и частота ошибок, подготовлен отчёт.</li><li>Разработаны BPMN-схемы текущего и целевого процесса обмена ЕСКУ — Смета с предварительной проверкой данных, возвратом статусов 200/400, передачей перечня ошибок и блокировкой отправки некорректного пакета.</li><li>Проводился регулярный контроль выгрузок и дашборда ЕСКУ: сверка организаций по ИНН, выявление отсутствующих и некорректных данных, направление обращений в НПО «Криста» и проверка исправлений.</li><li>Подготовлен проект письма в Департамент финансов. Отдельно составлена BPMN-схема внутреннего процесса обработки МБТ в ЦБ.</li><li>Подготовлен свод по платёжным поручениям Ямальского и Приуральского районов, проведены анализ данных и созвоны с организациями, у которых ПП синхронизировались, но не велись в ГИС «Смета ЯНАО».</li><li>Проведена первичная и повторная сверка архива из 589 PDF-файлов договоров: проверены ИНН и наименования организаций, выявленные несоответствия переданы для исправления.</li></ul></div></details>
</div>

</div>

