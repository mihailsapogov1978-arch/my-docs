Портал предназначен для быстрого доступа к информации по заключенным контрактам, мероприятиям планов информатизации, отслеживания состояния работы по проектам и тому подобного.

Посмотрите интерактивные подсказки ниже чтобы было легче ориентироваться на портале

<div class="hints-wrap">
  <img src="assets/screenshot.png" alt="Подсказки по интерфейсу портала">

  <!-- № 1: Поиск — синий -->
  <div class="hint hint--blue" style="top: 6%; left: 88%;">
    <div class="marker">1</div>
    <div class="tip tip--left" style="top: 40px; left: -280px;">
      <b>Быстрый поиск</b> по всей документации. Введите ключевое слово — система найдёт все упоминания
    </div>
  </div>

  <!-- № 2: Левое меню — зелёный -->
  <div class="hint hint--green" style="top: 22%; left: 10%;">
    <div class="marker">2</div>
    <div class="tip tip--right" style="top: 40px; left: 50px;">
      <b>Навигация по разделам портала</b>
    </div>
  </div>

  <!-- № 3: Заголовок раздела — оранжевый -->
  <div class="hint hint--orange" style="top: 18%; left: 30%;">
    <div class="marker">3</div>
    <div class="tip tip--bottom" style="top: 50px; left: -100px;">
      <b>Текущий раздел.</b> Показывает, где вы находитесь
    </div>
  </div>

  <!-- № 4: Оглавление справа — фиолетовый -->
  <div class="hint hint--purple" style="top: 38%; left: 88%;">
    <div class="marker">4</div>
    <div class="tip tip--left" style="top: -10px; left: -280px;">
      <b>Навигация по текущему разделу</b>
    </div>
  </div>

  <!-- № 5: Таблица контрактов — бирюзовый -->
  <div class="hint hint--teal" style="top: 70%; left: 45%;">
    <div class="marker">5</div>
    <div class="tip tip--top" style="top: -70px; left: -110px;">
      <b>Информация раздела</b>
    </div>
  </div>
</div>

<style>
  /* ============================================
     ОБЩИЙ КОНТЕЙНЕР
     ============================================ */

/* Убрать верхний отступ у списка меню */
.md-nav--primary > .md-nav__list {
  padding-top: 0 !important;
  margin-top: 0 !important;
}

/* Скрыть заголовок только на этой странице */
.md-content__inner > h1:first-child {
  display: none;
}
/* Убрать верхний отступ у контейнера контента */
.md-content__inner {
  padding-top: 0 !important;
}

/* Убрать отступ у первого блока после скрытого заголовка */
.md-content__inner > *:first-child {
  margin-top: 0 !important;
}

/* Скрыть заголовок бокового меню */
.md-nav--primary > .md-nav__title {
  display: none;
}

  .hints-wrap {
    position: relative;
    display: inline-block;
    max-width: 100%;
    margin-top: 24px;
    border-radius: 8px;
    overflow: visible;
    box-shadow: 0 6px 24px rgba(0, 0, 0, 0.08);
    background: #fff;
  }

  .hints-wrap img {
    display: block;
    max-width: 100%;
    height: auto;
    border-radius: 8px;
  }

  /* ============================================
     ОБЁРТКА КАЖДОЙ ПОДСКАЗКИ
     ============================================ */
  .hint {
    position: absolute;
    transform: translate(-50%, -50%);
    z-index: 10;
  }

  /* ============================================
     МАРКЕР — базовый стиль
     ============================================ */
  .marker {
    position: relative;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    color: #fff;
    font-size: 15px;
    font-weight: 700;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 0 0 3px #fff, 0 0 0 5px rgba(0, 0, 0, 0.08);
    cursor: help;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
  }

  /* Невидимая зона захвата 56×56 */
  .marker::after {
    content: '';
    position: absolute;
    top: 50%; left: 50%;
    width: 56px; height: 56px;
    transform: translate(-50%, -50%);
    border-radius: 50%;
  }

  .hint:hover .marker {
    transform: scale(1.08);
  }

  /* ============================================
     ЦВЕТА МАРКЕРОВ И ПОДСКАЗОК ПО ТИПАМ
     ============================================ */

  /* Синий — поиск */
  .hint--blue .marker {
    background: #5c8df6;
    box-shadow: 0 0 0 3px #fff, 0 0 0 5px rgba(92, 141, 246, 0.25);
  }
  .hint--blue:hover .marker {
    background: #3a75f0;
    box-shadow: 0 0 0 3px #fff, 0 0 0 7px rgba(92, 141, 246, 0.4);
  }

  /* Зелёный — навигация */
  .hint--green .marker {
    background: #4caf7d;
    box-shadow: 0 0 0 3px #fff, 0 0 0 5px rgba(76, 175, 125, 0.25);
  }
  .hint--green:hover .marker {
    background: #2e9e63;
    box-shadow: 0 0 0 3px #fff, 0 0 0 7px rgba(76, 175, 125, 0.4);
  }

  /* Оранжевый — текущий раздел */
  .hint--orange .marker {
    background: #f5a623;
    box-shadow: 0 0 0 3px #fff, 0 0 0 5px rgba(245, 166, 35, 0.25);
  }
  .hint--orange:hover .marker {
    background: #e0901a;
    box-shadow: 0 0 0 3px #fff, 0 0 0 7px rgba(245, 166, 35, 0.4);
  }

  /* Фиолетовый — оглавление */
  .hint--purple .marker {
    background: #9c6ade;
    box-shadow: 0 0 0 3px #fff, 0 0 0 5px rgba(156, 106, 222, 0.25);
  }
  .hint--purple:hover .marker {
    background: #7f4dd1;
    box-shadow: 0 0 0 3px #fff, 0 0 0 7px rgba(156, 106, 222, 0.4);
  }

  /* Бирюзовый — таблицы */
  .hint--teal .marker {
    background: #26b6b0;
    box-shadow: 0 0 0 3px #fff, 0 0 0 5px rgba(38, 182, 176, 0.25);
  }
  .hint--teal:hover .marker {
    background: #1e9a94;
    box-shadow: 0 0 0 3px #fff, 0 0 0 7px rgba(38, 182, 176, 0.4);
  }

  /* ============================================
     ПОДСКАЗКА — светлая с мягкой тенью
     ============================================ */
  .tip {
    position: absolute;
    max-width: 260px;
    width: max-content;
    background: #ffffff;
    color: #1f2937;
    font-size: 12.5px;
    line-height: 1.5;
    padding: 10px 14px;
    border-radius: 8px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1),
                0 2px 6px rgba(0, 0, 0, 0.06);
    z-index: 20;

    opacity: 0;
    visibility: hidden;
    transform: translateY(-4px);
    transition: opacity 0.15s ease, transform 0.15s ease,
                visibility 0s linear 0.15s;
    pointer-events: none;
  }

  .hint:hover .tip {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
    transition-delay: 0s;
    pointer-events: auto;
  }

  /* Жирный текст в подсказке — наследует цвет маркера */
  .tip b { font-weight: 600; }

  .hint--blue   .tip b { color: #3a75f0; }
  .hint--green  .tip b { color: #2e9e63; }
  .hint--orange .tip b { color: #e0901a; }
  .hint--purple .tip b { color: #7f4dd1; }
  .hint--teal   .tip b { color: #1e9a94; }

  /* ============================================
     Стрелочки — белые, чтобы совпадали с фоном подсказки
     ============================================ */
  .tip::before {
    content: '';
    position: absolute;
    width: 0;
    height: 0;
    border: 7px solid transparent;
  }

  /* Левая стрелка (подсказка справа от маркера) */
  .tip--left::before {
    left: -13px; top: 50%; transform: translateY(-50%);
    border-right-color: #ffffff;
    filter: drop-shadow(-2px 0 2px rgba(0, 0, 0, 0.06));
  }

  /* Правая стрелка (подсказка слева от маркера) */
  .tip--right::before {
    right: -13px; top: 50%; transform: translateY(-50%);
    border-left-color: #ffffff;
    filter: drop-shadow(2px 0 2px rgba(0, 0, 0, 0.06));
  }

  /* Верхняя стрелка (подсказка снизу от маркера) */
  .tip--top::before {
    top: -13px; left: 50%; transform: translateX(-50%);
    border-bottom-color: #ffffff;
    filter: drop-shadow(0 -2px 2px rgba(0, 0, 0, 0.06));
  }

  /* Нижняя стрелка (подсказка сверху от маркера) */
  .tip--bottom::before {
    bottom: -13px; left: 50%; transform: translateX(-50%);
    border-top-color: #ffffff;
    filter: drop-shadow(0 2px 2px rgba(0, 0, 0, 0.06));
  }

  /* ============================================
     Тач-устройства
     ============================================ */
  @media (hover: none) {
    .hint:focus-within .tip,
    .hint:active .tip {
      opacity: 1;
      visibility: visible;
      transform: translateY(0);
    }
  }
</style>