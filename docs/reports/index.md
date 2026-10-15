<style>
/* ===== Таблица отчёта ===== */
.report-table {
    width: 100%;
    border-collapse: collapse;
    background: #fff;
    border: 1px solid #e0e4e8;
    border-radius: 8px;
    overflow: hidden;
    margin: 16px 0 28px 0;
    table-layout: fixed;
}
.report-table thead th {
    background: #f5f7fa;
    color: #2c3e50;
    text-align: left;
    font-weight: 600;
    font-size: 14px;
    padding: 10px 14px;
    border-bottom: 1px solid #e0e4e8;
    white-space: nowrap;
}
.report-table tbody td {
    padding: 10px 14px;
    border-bottom: 1px solid #eef2f6;
    vertical-align: middle;
    color: #2d3748;
    font-size: 14px;
}
.report-table tbody tr:last-child td { border-bottom: none; }

/* Сводная строка отдела */
.report-summary-row td {
    background: #fafbfc;
    font-weight: 600;
    color: #2c3e50;
    border-bottom: 2px solid #e0e4e8;
}
.report-summary-row small {
    display: block;
    color: #718096;
    font-weight: 400;
    font-size: 12.5px;
    margin-top: 2px;
}

/* Кликабельная ячейка имени */
.report-name {
    cursor: pointer;
    user-select: none;
}
.report-name:hover {
    color: #2b6cb0;
}

/* Маркер раскрытия */
.report-toggle {
    display: inline-block;
    color: #718096;
    font-size: 15px;
    font-weight: 700;
    margin-right: 6px;
    transition: transform 0.15s;
}
.report-toggle.open {
    transform: rotate(90deg);
}

.report-num {
    text-align: left;
    white-space: nowrap;
}

/* Подсветка раскрытой строки сотрудника */
.report-row.open td {
    background: #eaf4ff;
    border-bottom-color: #bee3f8;
}
.report-row.open td:first-child {
    box-shadow: inset 3px 0 0 #3182ce;
}
.report-row.open:hover td {
    background: #e1efff;
}

/* Строка с раскрытыми задачами */
.report-tasks-row > td {
    background: #fafbfc;
    padding: 10px 14px 14px 46px;
    border-bottom: 1px solid #eef2f6;
}
.report-tasks {
    margin: 0;
    padding-left: 18px;
    font-size: 14px;
    line-height: 1.55;
    color: #2d3748;
    font-weight: 400;
}
.report-tasks li { margin-bottom: 4px; }

@media (max-width: 720px) {
    .report-table thead th,
    .report-table tbody td { padding: 8px 8px; }
}
</style>

# Отчёты отдела СРТП

## Сентябрь 2026

<table class="report-table">
  <thead>
    <tr>
      <th style="width:240px;">Сотрудник</th>
      <th style="width:110px;">Звонков</th>
      <th style="width:110px;">Заявок</th>
      <th style="width:110px;">Задач</th>
      <th style="width:120px;">Резолюций</th>
    </tr>
  </thead>
  <tbody>
    <tr class="report-summary-row">
      <td><b>Отдел СРТП</b><br><small>Сотрудников: 7</small></td>
      <td><b>2873</b></td>
      <td><b>47</b></td>
      <td><b>43</b></td>
      <td><b>9</b></td>
    </tr>
    <tr class="report-row" data-emp="1">
      <td class="report-name" onclick="toggleReportRow(this)">
        <span class="report-toggle">›</span>
        Сапогов
      </td>
      <td class="report-num">513</td>
      <td class="report-num">8</td>
      <td class="report-num">9</td>
      <td class="report-num">9</td>
    </tr>
    <tr class="report-tasks-row" style="display:none;">
      <td colspan="5">
        <ul class="report-tasks"><li>Подготовил изменения в Положение о ГИС &quot;Смета ЯНАО&quot;</li><li>Актуализировал пакет документов (заявка) на регистрацию модуля ИИ в Роспатент. Заявка рассмотрена положительно, модуль (программа) внесено в реестр программ для ЭВМ.</li><li>Скорректировал предварительный ПИ на 2027 год. Предварительно согласован ДИТиС.</li><li>Скорректировал ПИ на 2026 год, согласован ДИТиС.</li><li>Принял участие в актуализации списков организаций (муниципальных и окружных)</li><li>Направил ежемесячные отчеты по аудиту ПО и импортзамещению в ДИТиС (через депфин).</li><li>Актуализировал и направил на согласование ТЗ по администрированию Сметы</li><li>Подготовил новость (не публиковали еще) для работников органов власти об использовании приложения для агрегации сформированных отчетов об отпуске или командировке.</li><li>Подготовил письмо в РЦОКО для взаимодействия с ГИС «Ямал Образование» через СМЭВ.</li></ul>
      </td>
    </tr>
    <tr class="report-row" data-emp="2">
      <td class="report-name" onclick="toggleReportRow(this)">
        <span class="report-toggle">›</span>
        Мулявин
      </td>
      <td class="report-num">151</td>
      <td class="report-num">8</td>
      <td class="report-num">6</td>
      <td class="report-num">—</td>
    </tr>
    <tr class="report-tasks-row" style="display:none;">
      <td colspan="5">
        <ul class="report-tasks"><li>Завершена проработка перехода на «Астрал»: подготовлены итоговые материалы и дорожная карта, уточнены вопросы с НПО «Криста», задача закрыта в РСЭД «ТЕЗИС».</li><li>Разработан Excel-парсер на Python для автоматической обработки и агрегации отчётных данных. Приложение протестировано на Windows и RedOS 7.3/8, подготовлена версия для распространения пользователям, а также инструкции по работе, в том числе пошаговая инструкция со скриншотами.</li><li>Развернут и настроен тестовый агент СМЭВ4: проверено подключение к брокерам и выполнение запросов. При тестировании доступа к витрине выявлено отсутствие необходимых прав, организовано взаимодействие с РЦОКО для их предоставления.</li><li>Проведена работа по применению ИИ для распознавания документов: протестирован Extraction Studio, изучено взаимодействие через Swagger API и проработан Python-контур для автоматического распознавания и извлечения данных из документов.</li><li>Продолжена работа по ЕСКУ: обработка обращений и ошибок, анализ выгрузок и показателей дашбордов FIN_04 и аппарата, а также собственной выгрузки за двухмесячный период. По выявленным проблемам направлялись обращения и проверялись результаты исправлений.</li><li>Разработан бот для автоматизации уведомлений о паролях для отдела информационной безопасности.</li></ul>
      </td>
    </tr>
    <tr class="report-row" data-emp="3">
      <td class="report-name" onclick="toggleReportRow(this)">
        <span class="report-toggle">›</span>
        Кошик
      </td>
      <td class="report-num">325</td>
      <td class="report-num">2</td>
      <td class="report-num">9</td>
      <td class="report-num">—</td>
    </tr>
    <tr class="report-tasks-row" style="display:none;">
      <td colspan="5">
        <ul class="report-tasks"><li>Аудит по использованию Сметы и подготовка общего свода (Надымский р-н - 77, Губкинский - 47, Салехард - 57, Пуровский р-н - 64).</li><li>Сбор недостающих оферт по ГУ и МО - 2.</li><li>Написано инструкций и выложено на сайт ЦБ ОГВ - 3.</li><li>Настройка ЭДО Астрал для Департамента тарифной политики - 1.</li><li>Оформлено МЧД в ФНС, Росстат для Департамента тарифной политики - 6.</li><li>Внедрение и отработка механизма кроссподписания при передаче имущества из муниципального в региональный бюджет (ф.0510448, ф.0504805) - Пуровский р-н - 1</li><li>Подготовка свода по работе МО с документами 61н. - 1</li><li>Заявки / обращения от МО через чаты и по телефону &gt;= 100.</li><li>Взаимодействие с представителями подрядчиков (Fargos, Krista) по централизации Сметы в рабочих чатах MAX.</li></ul>
      </td>
    </tr>
    <tr class="report-row" data-emp="4">
      <td class="report-name" onclick="toggleReportRow(this)">
        <span class="report-toggle">›</span>
        Худышкин
      </td>
      <td class="report-num">313</td>
      <td class="report-num">3</td>
      <td class="report-num">7</td>
      <td class="report-num">—</td>
    </tr>
    <tr class="report-tasks-row" style="display:none;">
      <td colspan="5">
        <ul class="report-tasks"><li>Консультирование и техническая поддержка муниципальных образований по вопросам подключения, настройки и эксплуатации централизованной ГИС «Смета ЯНАО». Анализ используемых настроек и функционала, выявление участков, требующих дополнительной настройки или консультационного сопровождения.</li><li>Проведение аудита баз муниципальных образований на предмет   использования функциональных возможностей, предусмотренных ГИС «Смета  ЯНАО».</li><li>Работа с учреждениями и ответственными специалистами:</li><li>Сбор, проверка и актуализация контактных данных ответственных лиц  учреждений, кадровых работников и специалистов бухгалтерских служб.</li><li>Оповещение учреждений о необходимости проведения сопоставления  справочников в ГИС ЕСКУ и ГИС «Смета ЯНАО». Консультирование кадровых  работников и бухгалтеров по вопросам подготовки данных и организации  интеграционного взаимодействия.</li><li>Координация действий учреждений при возникновении вопросов и ошибок в  процессе обмена данными между информационными системами.</li><li>Консультирование и настройка функционала, связанного с перечислением  денежных средств на карты платёжной системы «Мир» в базах муниципальных  образований.</li></ul>
      </td>
    </tr>
    <tr class="report-row" data-emp="5">
      <td class="report-name" onclick="toggleReportRow(this)">
        <span class="report-toggle">›</span>
        Чечеткин
      </td>
      <td class="report-num">1104</td>
      <td class="report-num">20</td>
      <td class="report-num">6</td>
      <td class="report-num">—</td>
    </tr>
    <tr class="report-tasks-row" style="display:none;">
      <td colspan="5">
        <ul class="report-tasks"><li>Приказы на доступ ОУ - 6</li><li>Оферты по МБТ - 5</li><li>Приказы ЦБ на доступ - 5</li><li>Замещение с 02.09 по 06.09 Начальника отдела и Ведущих специалистов отдела</li><li>Исправление ошибок ГИС &quot;ГМП&quot; после смены реквизитов Казначейства</li><li>Работа по подписанию между базами ф.0504805 05104548</li></ul>
      </td>
    </tr>
    <tr class="report-row" data-emp="6">
      <td class="report-name" onclick="toggleReportRow(this)">
        <span class="report-toggle">›</span>
        Гасанов
      </td>
      <td class="report-num">89</td>
      <td class="report-num">1</td>
      <td class="report-num">3</td>
      <td class="report-num">—</td>
    </tr>
    <tr class="report-tasks-row" style="display:none;">
      <td colspan="5">
        <ul class="report-tasks"><li>до 11.09 находился в отпуске, Акутализация сдений в &quot;Реестр Оферт&quot;</li><li>Взаимодействие с представителями подрядчиков (Fargos, Krista) по заявочным вопросам Сметы в рабочих чатах МАКС.</li><li>Консультация / тех. поддержка / маршрутизация заявок муниципалитетов (ГИС ГМП, МИР, ПП).</li></ul>
      </td>
    </tr>
    <tr class="report-row" data-emp="7">
      <td class="report-name" onclick="toggleReportRow(this)">
        <span class="report-toggle">›</span>
        Роганова
      </td>
      <td class="report-num">378</td>
      <td class="report-num">5</td>
      <td class="report-num">3</td>
      <td class="report-num">—</td>
    </tr>
    <tr class="report-tasks-row" style="display:none;">
      <td colspan="5">
        <ul class="report-tasks"><li>Обработано приказов на временное / постоянное распределения обязанностей сотрудников ЦБ в Смете - 7 шт.</li><li>Обработано заявлений о присоединении (Оферта) - 2 шт.</li><li>Обработано приказов о предоставлении доступа к ГИС Смета (ИОГВ) - 5 шт.</li></ul>
      </td>
    </tr>
  </tbody>
</table>


## Август 2026

<table class="report-table">
  <thead>
    <tr>
      <th style="width:240px;">Сотрудник</th>
      <th style="width:110px;">Звонков</th>
      <th style="width:110px;">Заявок</th>
      <th style="width:110px;">Задач</th>
      <th style="width:120px;">Резолюций</th>
    </tr>
  </thead>
  <tbody>
    <tr class="report-summary-row">
      <td><b>Отдел СРТП</b><br><small>Сотрудников: 5</small></td>
      <td><b>1923</b></td>
      <td><b>54</b></td>
      <td><b>20</b></td>
      <td><b>13</b></td>
    </tr>
    <tr class="report-row" data-emp="1">
      <td class="report-name" onclick="toggleReportRow(this)">
        <span class="report-toggle">›</span>
        Сапогов
      </td>
      <td class="report-num">803</td>
      <td class="report-num">24</td>
      <td class="report-num">6</td>
      <td class="report-num">13</td>
    </tr>
    <tr class="report-tasks-row" style="display:none;">
      <td colspan="5">
        <ul class="report-tasks"><li>Проводилась подготовка ТЗ на выполнение работ по интеграции с РСЭД Тезис</li><li>Организация и взаимодействие с участниками и техподдержкой по настройке и тестировании  кроссподписания.</li><li>Проверка мероприятий предварительных ПИ на 2027 год среди МО и департамента здравоохранения.</li><li>Проводилась работа по администрированию, настройке прав, технической поддержке и решения иных вопросов на период отсутствия Чечеткина М.И., Обмоловой В.В. Рогановой А.И.</li><li>Подготовлены критерии для отчета по отслеживанию динамики авторизации через ЕСИА, сформулированы требования для отчета по командировкам и отпускам (заявки), решены несколько вопросов по ошибкам при импорте данных УКТ-Услуга, направлен отзыв заявки на регистрацию программы для ЭВМ (ИИ) чтобы повторно не платить пошлину.</li><li>Направлены ежемесячные отчеты по аудиту ПО и импортзамещению в ДИТиС (через депфин)</li></ul>
      </td>
    </tr>
    <tr class="report-row" data-emp="2">
      <td class="report-name" onclick="toggleReportRow(this)">
        <span class="report-toggle">›</span>
        Кошик
      </td>
      <td class="report-num">45</td>
      <td class="report-num">2</td>
      <td class="report-num">1</td>
      <td class="report-num">—</td>
    </tr>
    <tr class="report-tasks-row" style="display:none;">
      <td colspan="5">
        <ul class="report-tasks"><li>Сбор статистики по муниципалитетам - использования интеграции по направлениям: МИР, ПП, ЭДО, СФР, Имущество и т.п.</li></ul>
      </td>
    </tr>
    <tr class="report-row" data-emp="3">
      <td class="report-name" onclick="toggleReportRow(this)">
        <span class="report-toggle">›</span>
        Худышкин
      </td>
      <td class="report-num">206</td>
      <td class="report-num">13</td>
      <td class="report-num">6</td>
      <td class="report-num">—</td>
    </tr>
    <tr class="report-tasks-row" style="display:none;">
      <td colspan="5">
        <ul class="report-tasks"><li>Работа Техфоргосом, Мароп и Аппаратом Губернатора для утверждения и построения рабочего процесса (консолидация информации всеми сторонами) интеграции с ЕСКУ.</li><li>Восстановление подключений Imon ГКУ.drx . Поддержка и администрирование ИОГВ с 04.08.2026 по 12.08.2026. Поддержка, администрирование  и консультация по  ГИС АПК и Астралу.  Работа по организации интеграции ГИС ЕСКУ и ГИС Сметы. Оповещеие учреждений о сопостовлении справочников, консультация.    Взаимодействие с представителями подрядчиков (Мароп, Хендисофт, Аппарат Губернатора) для согласования и реализации доработок по интеграции.</li><li>Взаимодействие с представителями подрядчиков (Fargos, Krista) по централизации Сметы в рабочих чатах Мах и по телефону.</li><li>Консультация / тех. поддержка / маршрутизация заявок муниципалитетов в части подключения и настройки централизованной Сметы ЯНАО.</li><li>Поддержка по настройкам ГИС ГМП, ГИС Имущество, перечеисление на карты МИР в базах муниципалитетов.</li><li>Работы с базами муниципалитетов. Курирование работы функционала интеграции ГИС ЕСКУ и Сметы в ЦБ ОГВ ЯНАО.</li></ul>
      </td>
    </tr>
    <tr class="report-row" data-emp="4">
      <td class="report-name" onclick="toggleReportRow(this)">
        <span class="report-toggle">›</span>
        Чечеткин
      </td>
      <td class="report-num">677</td>
      <td class="report-num">7</td>
      <td class="report-num">3</td>
      <td class="report-num">—</td>
    </tr>
    <tr class="report-tasks-row" style="display:none;">
      <td colspan="5">
        <ul class="report-tasks"><li>Предоставление доступа сотрудника ОУ - 3 приказа;</li><li>Устранение проблемы с созданием МЧД;</li><li>Работа по внедрению подписания ф.0510448 и 0504805 между базами и устранение ошибок;</li></ul>
      </td>
    </tr>
    <tr class="report-row" data-emp="5">
      <td class="report-name" onclick="toggleReportRow(this)">
        <span class="report-toggle">›</span>
        Мулявин
      </td>
      <td class="report-num">192</td>
      <td class="report-num">8</td>
      <td class="report-num">4</td>
      <td class="report-num">—</td>
    </tr>
    <tr class="report-tasks-row" style="display:none;">
      <td colspan="5">
        <ul class="report-tasks"><li>Проведена работа по переходу на «Астрал»: изучены текущий и целевой бизнес-процессы сдачи отчётности, собрана обратная связь пользователей и уточнены вопросы с НПО «Криста». Подготовлены дорожная карта перехода и BPMN-схемы процессов работы через «Контур» и «Астрал».</li><li>Для загрузки данных по медалистам с помощью Python-скрипта обработаны данные по 537 детям, выполнена сверка и распределение по 13 территориям, подготовлены 13 Excel- и 13 CSV-файлов для загрузки в ГИС «Смета ЯНАО».</li><li>Проводилась обработка обращений пользователей по ЕСКУ и другим вопросам ГИС «Смета ЯНАО»: анализ ошибок, проверка выгрузок и данных, подготовка заявок в НПО «Криста» и контроль исправлений.</li><li>Оказана помощь в проработке нового ТЗ по платёжным поручениям: рассмотрено совмещение планируемых доработок со стороны НПО «Криста» и функционала РСЭД «ТЕЗИС».</li></ul>
      </td>
    </tr>
  </tbody>
</table>


## Июль 2026

<table class="report-table">
  <thead>
    <tr>
      <th style="width:240px;">Сотрудник</th>
      <th style="width:110px;">Звонков</th>
      <th style="width:110px;">Заявок</th>
      <th style="width:110px;">Задач</th>
      <th style="width:120px;">Резолюций</th>
    </tr>
  </thead>
  <tbody>
    <tr class="report-summary-row">
      <td><b>Отдел СРТП</b><br><small>Сотрудников: 9</small></td>
      <td><b>2350</b></td>
      <td><b>27</b></td>
      <td><b>26</b></td>
      <td><b>13</b></td>
    </tr>
    <tr class="report-row" data-emp="1">
      <td class="report-name" onclick="toggleReportRow(this)">
        <span class="report-toggle">›</span>
        Ставер
      </td>
      <td class="report-num">354</td>
      <td class="report-num">1</td>
      <td class="report-num">1</td>
      <td class="report-num">11</td>
    </tr>
    <tr class="report-tasks-row" style="display:none;">
      <td colspan="5">
        <ul class="report-tasks"><li>Проведены консультации на тему ввода нового функционала с разработчиками Сметы; с департаментом ИТ и связи на тему мероприятий по плану информатизации; методологами на тему бизнес-процессов действующих интеграций в целях выявления ошибок в пограничных зонах ответственности. Выполнена настройка и тестирование авторизации через ЕСИА в ЛК ПОЛ</li></ul>
      </td>
    </tr>
    <tr class="report-row" data-emp="2">
      <td class="report-name" onclick="toggleReportRow(this)">
        <span class="report-toggle">›</span>
        Сапогов
      </td>
      <td class="report-num">99</td>
      <td class="report-num">3</td>
      <td class="report-num">3</td>
      <td class="report-num">2</td>
    </tr>
    <tr class="report-tasks-row" style="display:none;">
      <td colspan="5">
        <ul class="report-tasks"><li>Актуализировано и направлено на согласование ТЗ на выполнение работ по интеграции с РСЭД Тезис с учетом замечаний от ДИТиС. Работа по размещению предварительного ПИ на 2027 год.</li><li>Выполнение настроек уведомлений для сотрудников отдела расчетов с персоналом (авансники).</li><li>Проводиться работа по размещению предварительного плана информатизации на 2027 год.</li></ul>
      </td>
    </tr>
    <tr class="report-row" data-emp="3">
      <td class="report-name" onclick="toggleReportRow(this)">
        <span class="report-toggle">›</span>
        Обмолова
      </td>
      <td class="report-num">448</td>
      <td class="report-num">0</td>
      <td class="report-num">1</td>
      <td class="report-num">—</td>
    </tr>
    <tr class="report-tasks-row" style="display:none;">
      <td colspan="5">
        <ul class="report-tasks"><li>Исправление ошибок при синхронизации с ЕСКУ; Работа с муниципальными учреждениям Здравоохранения ЯНАО, подготовка к полугодовой отчетности</li></ul>
      </td>
    </tr>
    <tr class="report-row" data-emp="4">
      <td class="report-name" onclick="toggleReportRow(this)">
        <span class="report-toggle">›</span>
        Кошик
      </td>
      <td class="report-num">180</td>
      <td class="report-num">1</td>
      <td class="report-num">2</td>
      <td class="report-num">—</td>
    </tr>
    <tr class="report-tasks-row" style="display:none;">
      <td colspan="5">
        <ul class="report-tasks"><li>Сбор статистики по муниципалитетам - использования интеграции по направлениям: МИР, ПП, ЭДО, СФР, Имущество и т.п.</li><li>Взаимодействие с представителями подрядчиков (Fargos, Krista) по централизации Сметы в рабочих чатах MAX.</li></ul>
      </td>
    </tr>
    <tr class="report-row" data-emp="5">
      <td class="report-name" onclick="toggleReportRow(this)">
        <span class="report-toggle">›</span>
        Худышкин
      </td>
      <td class="report-num">32</td>
      <td class="report-num">0</td>
      <td class="report-num">2</td>
      <td class="report-num">—</td>
    </tr>
    <tr class="report-tasks-row" style="display:none;">
      <td colspan="5">
        <ul class="report-tasks"><li>Сбор статистики предоставленных муниципалитетами актов о принятии работ по интеграции с ЕСКУ</li><li>Взаимодействие с представителями подрядчиков (Fargos, Krista) по централизации Сметы в рабочих чатах MAX.</li></ul>
      </td>
    </tr>
    <tr class="report-row" data-emp="6">
      <td class="report-name" onclick="toggleReportRow(this)">
        <span class="report-toggle">›</span>
        Гасанов
      </td>
      <td class="report-num">171</td>
      <td class="report-num">2</td>
      <td class="report-num">3</td>
      <td class="report-num">—</td>
    </tr>
    <tr class="report-tasks-row" style="display:none;">
      <td colspan="5">
        <ul class="report-tasks"><li>Сбор статистики по муниципалитетам - использования интеграции по направлениям: МИР, ПП, ЭДО, СФР, Имущество и т.п.</li><li>Взаимодействие с представителями подрядчиков (Fargos, Krista) по заявочным вопросам Сметы в рабочих чатах Max.</li><li>Консультация / тех. поддержка / маршрутизация заявок муниципалитетов (ГИС ГМП, МИР, ПП).</li></ul>
      </td>
    </tr>
    <tr class="report-row" data-emp="7">
      <td class="report-name" onclick="toggleReportRow(this)">
        <span class="report-toggle">›</span>
        Чечеткин
      </td>
      <td class="report-num">501</td>
      <td class="report-num">3</td>
      <td class="report-num">5</td>
      <td class="report-num">—</td>
    </tr>
    <tr class="report-tasks-row" style="display:none;">
      <td colspan="5">
        <ul class="report-tasks"><li>Дежурство 4-5 июля по запросу отдела подготовки отчетности на совещание;</li><li>Предоставление доступа Аудиторам -1;</li><li>Приказы ОУ на доступ -1;</li><li>Решение проблем при созданий МЧД в ГИС &quot;СМЕТА ЯНАО&quot;;</li><li>Принятия участия в устранениях последствий после аваринного отключения электроэнергий.</li></ul>
      </td>
    </tr>
    <tr class="report-row" data-emp="8">
      <td class="report-name" onclick="toggleReportRow(this)">
        <span class="report-toggle">›</span>
        Роганова
      </td>
      <td class="report-num">431</td>
      <td class="report-num">7</td>
      <td class="report-num">3</td>
      <td class="report-num">—</td>
    </tr>
    <tr class="report-tasks-row" style="display:none;">
      <td colspan="5">
        <ul class="report-tasks"><li>Обработано приказов на временное / постоянное распределения обязанностей сотрудников ЦБ в Смете - 6 шт.</li><li>Обработано заявлений о присоединении (Оферта) - 2 шт.</li><li>Обработано приказов о предоставлении доступа к ГИС Смета (ИОГВ) - 3 шт.</li></ul>
      </td>
    </tr>
    <tr class="report-row" data-emp="9">
      <td class="report-name" onclick="toggleReportRow(this)">
        <span class="report-toggle">›</span>
        Мулявин
      </td>
      <td class="report-num">134</td>
      <td class="report-num">10</td>
      <td class="report-num">6</td>
      <td class="report-num">—</td>
    </tr>
    <tr class="report-tasks-row" style="display:none;">
      <td colspan="5">
        <ul class="report-tasks"><li>Проведён анализ ошибок интеграции с ЕСКУ по 50 организациям: обработано около 100 тыс. записей, выявлены основные типы и частота ошибок, подготовлен отчёт.</li><li>Разработаны BPMN-схемы текущего и целевого процесса обмена ЕСКУ — Смета с предварительной проверкой данных, возвратом статусов 200/400, передачей перечня ошибок и блокировкой отправки некорректного пакета.</li><li>Проводился регулярный контроль выгрузок и дашборда ЕСКУ: сверка организаций по ИНН, выявление отсутствующих и некорректных данных, направление обращений в НПО «Криста» и проверка исправлений.</li><li>Подготовлен проект письма в Департамент финансов. Отдельно составлена BPMN-схема внутреннего процесса обработки МБТ в ЦБ.</li><li>Подготовлен свод по платёжным поручениям Ямальского и Приуральского районов, проведены анализ данных и созвоны с организациями, у которых ПП синхронизировались, но не велись в ГИС «Смета ЯНАО».</li><li>Проведена первичная и повторная сверка архива из 589 PDF-файлов договоров: проверены ИНН и наименования организаций, выявленные несоответствия переданы для исправления.</li></ul>
      </td>
    </tr>
  </tbody>
</table>


<script>
function toggleReportRow(cell) {
    var tr = cell.closest('tr');
    if (!tr) return;
    var next = tr.nextElementSibling;
    var tog = cell.querySelector('.report-toggle');
    if (!next || !next.classList.contains('report-tasks-row')) return;

    if (next.style.display === 'none') {
        next.style.display = '';
        tr.classList.add('open');
        if (tog) tog.classList.add('open');
    } else {
        next.style.display = 'none';
        tr.classList.remove('open');
        if (tog) tog.classList.remove('open');
    }
}
</script>
