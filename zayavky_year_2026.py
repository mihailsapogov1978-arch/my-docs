import pandas as pd
import os
import re

# --- КОНФИГУРАЦИЯ ---
FILE_PATHS = [
    'docs/calls/part1.xlsx',
    'docs/calls/part2.xlsx'
]
OUTPUT_MD_FILE = os.path.join('docs', 'calls', 'report.md')

COL_ORG = 0
COL_ID = 1
COL_DATE = 2
COL_STATUS = 4
COL_THEME = 5
COL_DESC = 6
COL_EXECUTOR = 7
COL_SOLUTION = 8
COL_SERVICE = 9

# ============================================================
# НАПРАВЛЕНИЯ И КЛЮЧЕВЫЕ МАРКЕРЫ
# ============================================================
# ВАЖНО: порядок словаря = порядок приоритета.
# Более специфичные категории идут ВЫШЕ общих.
DIRECTIONS = {
    # --- Специфичные ---
    'Некорректное состояние справочников и классификаторов (задвоение ИНН/КПП, отсутствие аналитики, ошибки в иерархии)': {
        'require_any': [
            'справочник', 'классификатор', 'инн', 'кпп', 'задвоен', 'дубл', 'иерарх',
            'некорректное состояние', 'ошибка в справочнике', 'аналитик', 'местонахождение',
            'неверно указан инн', 'сведения об организации', 'групповой учет', 'объединение контрагент',
            'объединение сотрудников', 'объединение организаций', 'адрес', 'контрагент', 'номенклатура',
            'задвоение', 'некорректно', 'ошибка в данных'
        ],
        'exclude': [
            'права доступа', 'роль', 'подпись', 'сертификат', 'эцп', 'больничный', 'реестр',
            'уведомление', 'оплата', 'начисление', 'зарплата', 'табель', 'кадры'
        ]
    },
    'Личный кабинет подотчетного лица (ЛК ПОЛ)': {
        'require_any': [
            'лк пол', 'личный кабинет', 'кабинет подотчетного', 'подотчетное лицо', 'лк подотчет',
            'авансовый отчет', 'отчет о расходах', 'сервис подотчетного', 'командировочные', 'командировка',
            'пол', 'подотчет'
        ],
        'exclude': [
            'права доступа', 'роль', 'подпись', 'сертификат', 'эцп', 'договор', 'контрагент'
        ]
    },
    'Взаимодействие с внешними системами (РКС, ЕИС, ГИС Имущество, банки и прочие)': {
        'require_any': [
            'ркс', 'еис', 'гис имущество', 'интеграц', 'выгрузка', 'загрузка',
            'обмен', 'смэв', 'сбер', 'втб', 'казначейств', 'гмп', 'апк', 'астрал',
            'синхронизац', 'заявка мир', 'карты мир', 'эквайринг', 'гисп', 'закупки',
            'гисп', 'жилфонд', 'гис жкх', 'гис гмп', 'импорт', 'экспорт', 'внешн',
            'контракт', 'веб-исполнение', 'web-исполнение', 'веб-консолидация', 'web-консолидация',
            'унп', 'гис апк', 'гис гмп'
        ],
        'exclude': [
            'зарплата', 'табель', 'кадры', 'бухгалтер', 'отчетность', 'справочник'
        ]
    },
    'Формирование регламентированной отчетности (в ФНС, СФР, Росстат, Астрал)': {
        'require_any': [
            'отчетност', 'регламент', 'фнс', 'сфр', 'росстат', 'астрал',
            'статистик', 'декларац', 'сзв', '6-ндфл', 'рсв', 'форма',
            'отчет по', 'ефс-1', '4-фсс', 'свод', 'анализ счета', 'регистр',
            'п-4', 'зп-прочие', 'зп-культура', 'п-2', 'т-1', '1-т', 'псв', 'отчет'
        ],
        'exclude': [
            'аналитика', 'пользовательск', 'лист', 'визуализац', 'печатн'
        ]
    },
    'Кадровый учет (ГИС ТК, СЗВ-ТД, больничные, отпуска, ГИС КУ, ГИС ЕСКУ)': {
        'require_any': [
            'кадр', 'гис тк', 'сзв-тд', 'больнич', 'отпуск', 'гис ку',
            'еску', 'прием', 'увольн', 'перевод', 'табел', 'график',
            'сотрудник', 'физлицо', 'стаж', 'уход за ребенком', 'декрет', 'больничный лист',
            'отвлечен', 'прогул', 'совместитель', 'совместительство', 'штатн', 'анкетн',
            'система кадрового учета', 'кадровый учет'
        ],
        'exclude': [
            'права доступа', 'зарплата', 'бухгалтер', 'проводк', 'эцп'
        ]
    },
    'Бухгалтерский учет и налогообложение (операции, зарплата, налоги, закрытие периода и т.д.)': {
        'require_any': [
            'бухучет', 'бухгалтер', 'проводк', 'операц', 'зарплат', 'налог',
            'закрыти', 'ндфл', 'ндс', 'прибыль', 'усн', 'енс', 'взнос',
            'начислен', 'удержан', 'авансовый отчет', 'касс', 'банк',
            'санкционирован', 'договор', 'обязательств', 'оплата', 'начисление',
            'баланс', 'главная книга', 'журнал', 'ордер', 'осаг', 'рсв', 'платеж'
        ],
        'exclude': []
    },
    # Пункт 2: Технические проблемы — сюда же переносим ключевые слова из старого пункта 10
    # (Заявки без описания и служебные обращения)
    'Технические проблемы (запуск, обновления, права доступа, зависания, ЭП)': {
        'require_any': [
            # --- технические проблемы ---
            'запуск', 'обновлен', 'права доступ', 'зависа', 'эцп', 'эп',
            'сертификат', 'крипто', 'пароль', 'логин', 'подпис', 'активац',
            'разблок', 'техническ', 'вылет', 'глюк', 'доступ запрещен',
            'не работает', 'ошибка запуска', 'лицензи', 'установк', 'обновлен',
            'разблокирова', 'роль', 'подпись', 'пользовател', 'доступ', 'ошибка',
            # --- перенесено из "Заявки без описания и служебные обращения" ---
            'без темы', 'дубль', 'дубликат', 'тест', 'проверка', 'автоматически',
            'спасибо', 'благодарю', 'отмена заявки', 'закрыто автоматически',
            'перенаправлено', 'не актуально', 'просьба удалить', 'удалить заявку',
            'дополнение к заявке', 'обращение по', 'отправлено из', 'heic', 'image-',
            'fwd', 're:', 'пересылаемое'
        ],
        'exclude': []
    },
    'Дополнительный функционал и сервисы (аналитика, планирование, API)': {
        'require_any': [
            'аналитик', 'планирован', 'api', 'конструктор', 'мониторинг',
            'сервис', 'доп функционал', 'пользовательск', 'настройк',
            'шаблон', 'печатн', 'форма', 'отчет', 'пользовательский отчет',
            'разработк', 'доработк', 'функционал'
        ],
        'exclude': [
            'техническая', 'запуск', 'обновление', 'права', 'доступ', 'ошибка',
            'бухгалтер', 'зарплата', 'кадры'
        ]
    },

    # --- Две НОВЫЕ категории из прошлой итерации (кроме удалённой "Заявки без описания") ---
    'Консультации и разъяснения порядка работы (вопросы «как сделать», «где найти», «подскажите»)': {
        'require_any': [
            'подскажите', 'как сделать', 'как настроить', 'как заполнить', 'как создать',
            'как выгрузить', 'как загрузить', 'как посмотреть', 'как найти', 'где найти',
            'где настроить', 'где заполнить', 'где создается', 'где находится',
            'разъясните', 'поясните', 'разъяснение', 'не могу найти', 'не могу понять',
            'можно ли', 'возможно ли', 'вопрос по', 'прошу разъяснить', 'прошу пояснить',
            'как правильно', 'как изменить', 'как исправить', 'что делать', 'дайте инструкцию',
            'направьте инструкцию', 'пришлите инструкцию', 'консультац', 'обучение', 'вебинар'
        ],
        'exclude': [
            'ошибка', 'не работает', 'не запускается', 'не открывается', 'вылетает',
            'задвоен', 'некорректн', 'сбой', 'некорректно'
        ]
    },
    'Ошибки и сбои при работе в системе (прочие)': {
        'require_any': [
            'ошибка', 'сбой', 'не работает', 'не открывается', 'не сохраняется',
            'не проводится', 'не подтягивается', 'не отображается', 'выдает',
            'зависает', 'некорректно', 'неправильно', 'неверно', 'проблема',
            'не получается', 'не удается', 'вылетает', 'глючит', 'баг'
        ],
        'exclude': [
            'консультац', 'подскажите', 'разъясн'
        ]
    },
}

# ============================================================
# ПОДКАТЕГОРИИ
# ============================================================
# Пункт 3: Кадровый учет → подкатегория ЕСКУ
SUB_DIRECTIONS_KADR = {
    'Из них ГИС ЕСКУ': {
        'require_any': [
            'еску', 'система кадрового учета', 'кадровый учет', 'гис еску',
            'выгрузка из еску', 'загрузка из еску'
        ]
    }
}

# Пункт 4: Регламентированная отчетность → подкатегория Астрал
SUB_DIRECTIONS_REPORTING = {
    'Из них по Астралу': {
        'require_any': [
            'астрал', 'астрал отчет', 'астрал-отчет', 'сдача через астрал',
            'выгрузка в астрал', 'загрузка в астрал', 'астрал отчетность'
        ]
    }
}

# Пункт 7 (в новом порядке — пункт 3 или 4): Внешние системы → подкатегории по ГИС
SUB_DIRECTIONS_EXTERNAL = {
    'ГИС "Имущество"': {
        'require_any': [
            'гис имущество', 'имущество', 'выгрузка имущества', 'гис "имущество"'
        ]
    },
    'РКС (ЕИС)': {
        'require_any': [
            'ркс', 'еис', 'контракт', 'закупк', 'реестр контрактов',
            'синхронизац', 'выгрузка договор', 'загрузка договор'
        ]
    },
    'ГИС "ГМП" (УНП)': {
        'require_any': [
            'гмп', 'гис гмп', 'унп', 'гис "гмп"', 'начисление', 'квитирован'
        ]
    },
    'ГИС "АПК"': {
        'require_any': [
            'апк', 'гис апк', 'гис "апк"'
        ]
    },
    'ГИС "Web-Исполнение"': {
        'require_any': [
            'web-исполнение', 'веб-исполнение', 'исполнение бюджета', 'выгрузка в исполнение'
        ]
    },
    'ГИС "Web-Консолидация"': {
        'require_any': [
            'web-консолидация', 'веб-консолидация', 'консолидация', 'выгрузка в консолидацию'
        ]
    }
}


def clean_text_field(text):
    if not isinstance(text, str):
        return ""
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def classify_direction(text, direction_cfg):
    text_lower = text.lower()
    if any(re.search(r'\b' + re.escape(ex) + r'\b', text_lower) for ex in direction_cfg.get('exclude', [])):
        return False
    require_any = direction_cfg.get('require_any', [])
    if not require_any:
        keywords = direction_cfg.get('keywords', [])
        return any(re.search(r'\b' + re.escape(k) + r'\b', text_lower) for k in keywords)
    return any(re.search(r'\b' + re.escape(r) + r'\b', text_lower) for r in require_any)


def parse_excel_files(file_paths):
    all_data = []
    for file_path in file_paths:
        if not os.path.exists(file_path):
            print(f"Файл не найден: {file_path}")
            continue
        try:
            df_raw = pd.read_excel(file_path, header=None)
            header_row = None
            for i, row in df_raw.iterrows():
                if 'Номер' in row.values and 'Дата и время регистрации' in row.values:
                    header_row = i
                    break
            if header_row is None:
                print(f"Не найден заголовок в файле: {file_path}")
                continue
            data_start_row = header_row + 2
            headers = df_raw.iloc[header_row].tolist()
            headers = [str(h).strip() if pd.notna(h) else f'Unnamed_{i}' for i, h in enumerate(headers)]
            df = df_raw.iloc[data_start_row:].copy()
            df.columns = headers
            df.dropna(how='all', inplace=True)
            all_data.append(df)
        except Exception as e:
            print(f"Ошибка чтения {file_path}: {e}")
            continue
    if not all_data:
        return pd.DataFrame()
    combined_df = pd.concat(all_data, ignore_index=True)
    combined_df['Учреждение'] = None
    current_org = None
    for index, row in combined_df.iterrows():
        org_cell = row.iloc[COL_ORG] if COL_ORG < len(row) else None
        id_cell = row.iloc[COL_ID] if COL_ID < len(row) else None
        if pd.isna(id_cell) and pd.notna(org_cell) and str(org_cell).strip() not in ['', 'Номер']:
            current_org = str(org_cell).strip()
            combined_df.loc[index, 'Учреждение'] = current_org
        elif current_org is not None:
            combined_df.loc[index, 'Учреждение'] = current_org
    combined_df = combined_df[pd.notna(combined_df.iloc[:, COL_ID])].copy()
    combined_df = combined_df[pd.to_numeric(combined_df.iloc[:, COL_ID], errors='coerce').notna()].copy()
    return combined_df


def generate_report(df):
    if df.empty:
        return "# Анализ заявок\n\nНет данных."

    df['Дата'] = pd.to_datetime(df.iloc[:, COL_DATE], errors='coerce', dayfirst=True)
    df['Тема'] = df.iloc[:, COL_THEME].apply(clean_text_field)
    df['Описание'] = df.iloc[:, COL_DESC].apply(clean_text_field)
    df['Решение'] = df.iloc[:, COL_SOLUTION].apply(clean_text_field)

    df['search_text'] = (
        df['Тема'].fillna('') + ' || ' +
        df['Описание'].fillna('') + ' || ' +
        df['Решение'].fillna('')
    )

    df['Год'] = df['Дата'].dt.year
    current_year_df = df[df['Год'] == 2026].copy()

    if current_year_df.empty:
        return "# Анализ заявок за 2026 год\n\nНет данных."

    total = len(current_year_df)

    # --- Классификация ---
    current_year_df['category'] = 'Иные (не классифицировано)'
    for direction_name, cfg in DIRECTIONS.items():
        mask = current_year_df['category'] == 'Иные (не классифицировано)'
        if not mask.any():
            break
        classified_mask = current_year_df.loc[mask, 'search_text'].apply(lambda t: classify_direction(t, cfg))
        current_year_df.loc[mask & classified_mask, 'category'] = direction_name

    # --- Основная сводка ---
    summary = []
    for direction_name in DIRECTIONS.keys():
        count = len(current_year_df[current_year_df['category'] == direction_name])
        summary.append({'name': direction_name, 'count': count, 'sub': []})

    # --- Подкатегории ---

    # Пункт 3: Кадровый учет → ЕСКУ
    kadr_name = 'Кадровый учет (ГИС ТК, СЗВ-ТД, больничные, отпуска, ГИС КУ, ГИС ЕСКУ)'
    kadr_df = current_year_df[current_year_df['category'] == kadr_name]
    if not kadr_df.empty:
        for sub_name, sub_cfg in SUB_DIRECTIONS_KADR.items():
            sub_mask = kadr_df['search_text'].apply(lambda t: classify_direction(t, sub_cfg))
            sub_count = int(sub_mask.sum())
            if sub_count > 0:
                for item in summary:
                    if item['name'] == kadr_name:
                        item['sub'].append({'name': sub_name, 'count': sub_count})
                        break

    # Пункт 4: Регламентированная отчетность → Астрал
    reporting_name = 'Формирование регламентированной отчетности (в ФНС, СФР, Росстат, Астрал)'
    reporting_df = current_year_df[current_year_df['category'] == reporting_name]
    if not reporting_df.empty:
        for sub_name, sub_cfg in SUB_DIRECTIONS_REPORTING.items():
            sub_mask = reporting_df['search_text'].apply(lambda t: classify_direction(t, sub_cfg))
            sub_count = int(sub_mask.sum())
            if sub_count > 0:
                for item in summary:
                    if item['name'] == reporting_name:
                        item['sub'].append({'name': sub_name, 'count': sub_count})
                        break

    # Пункт про внешние системы → подкатегории по ГИС
    external_name = 'Взаимодействие с внешними системами (РКС, ЕИС, ГИС Имущество, банки и прочие)'
    external_df = current_year_df[current_year_df['category'] == external_name]
    if not external_df.empty:
        for sub_name, sub_cfg in SUB_DIRECTIONS_EXTERNAL.items():
            sub_mask = external_df['search_text'].apply(lambda t: classify_direction(t, sub_cfg))
            sub_count = int(sub_mask.sum())
            if sub_count > 0:
                for item in summary:
                    if item['name'] == external_name:
                        item['sub'].append({'name': sub_name, 'count': sub_count})
                        break

    # --- Сортировка: все категории по убыванию, но "Иные" — всегда последняя ---
    summary.sort(key=lambda x: x['count'], reverse=True)

    other_count = len(current_year_df[current_year_df['category'] == 'Иные (не классифицировано)'])
    other_item = None
    if other_count > 0:
        other_item = {'name': 'Иные (не классифицировано)', 'count': other_count, 'sub': []}
        # Все остальные уже отсортированы, Иные добавим в конец
        summary = summary + [other_item]

    # ============================================================
    # CSS + HTML
    # ============================================================
    css = """
<style>
:root {
    --emp-border: #e2e8f0;
    --emp-bg-hover: #f7fafc;
    --emp-text: #2d3748;
    --emp-muted: #718096;
    --emp-accent: #2b6cb0;
    --emp-accent-light: #ebf8ff;
    --emp-accent-border: #bee3f8;
}

.cat-list {
    margin: 16px 0;
    border: 1px solid var(--emp-border);
    border-radius: 10px;
    overflow: hidden;
    background: #fff;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}

.cat-row,
.cat-sub-item {
    display: grid;
    grid-template-columns: 32px minmax(0, 1fr) 150px 20px;
    align-items: center;
    column-gap: 12px;
    padding: 12px 16px;
    border-bottom: 1px solid var(--emp-border);
    font-size: 14px;
    line-height: 1.4;
    margin: 0;
}

.cat-row:last-child { border-bottom: none; }

.cat-row.has-sub {
    cursor: pointer;
    transition: background 0.15s;
}
.cat-row.has-sub:hover { background: var(--emp-bg-hover); }

.cat-num {
    font-weight: 700;
    color: var(--emp-muted);
    text-align: right;
}

.cat-name {
    font-weight: 600;
    color: var(--emp-text);
    min-width: 0;
}

.cat-count {
    font-weight: 700;
    color: var(--emp-accent);
    white-space: nowrap;
    text-align: right;
}
.cat-count span {
    font-weight: 400;
    color: var(--emp-muted);
    font-size: 12px;
    margin-left: 4px;
}

.cat-toggle {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    color: var(--emp-accent);
    font-size: 16px;
    font-weight: 700;
    transition: transform 0.15s;
    user-select: none;
}
.cat-row.has-sub.open .cat-toggle {
    transform: rotate(90deg);
}

.cat-checkbox {
    display: none;
}

.cat-details {
    display: none;
    background: #fafbfc;
    border-bottom: 1px solid var(--emp-border);
    padding: 0;
}
.cat-checkbox:checked ~ .cat-details {
    display: block;
}
.cat-checkbox:checked ~ .cat-row .cat-toggle {
    transform: rotate(90deg);
}

.cat-sub-list {
    margin: 0;
    padding: 0;
    list-style: none;
    background: #fafbfc;
}

.cat-sub-item {
    padding-left: 28px;
    padding-right: 16px;
    font-size: 13.5px;
    border-bottom: 1px dashed var(--emp-border);
}
.cat-sub-item:last-child { border-bottom: 1px solid var(--emp-border); }

.cat-sub-name {
    color: var(--emp-text);
    font-style: italic;
    min-width: 0;
    grid-column: 2;
}

.cat-sub-count {
    font-weight: 600;
    color: var(--emp-accent);
    white-space: nowrap;
    text-align: right;
    grid-column: 3;
}
.cat-sub-count span {
    font-weight: 400;
    color: var(--emp-muted);
    font-size: 12px;
    margin-left: 4px;
}

.cat-sub-empty {
    grid-column: 4;
}

.cat-total {
    display: grid;
    grid-template-columns: 1fr 150px;
    align-items: center;
    column-gap: 12px;
    background: var(--emp-accent-light);
    border: 1px solid var(--emp-accent-border);
    border-radius: 8px;
    padding: 14px 20px;
    margin: 10px 0 16px 0;
    font-size: 14px;
    color: var(--emp-accent);
    font-weight: 600;
}
.cat-total-value { text-align: right; font-size: 16px; }

@media (max-width: 700px) {
    .cat-row,
    .cat-sub-item {
        grid-template-columns: 28px minmax(0, 1fr) 20px;
        row-gap: 4px;
    }
    .cat-count,
    .cat-sub-count {
        grid-column: 2;
        text-align: left;
    }
    .cat-toggle { grid-row: 1; grid-column: 3; }
    .cat-sub-empty { display: none; }
    .cat-sub-item { padding-left: 16px; }
    .cat-total { grid-template-columns: 1fr; row-gap: 6px; }
    .cat-total-value { text-align: left; }
}
</style>
"""

    lines = []
    lines.append(css)
    lines.append("")
    lines.append("# Анализ заявок за 2026 год по направлениям")
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append('<div class="cat-total">')
    lines.append('  <span class="cat-total-label">Всего заявок за 2026 год</span>')
    lines.append(f'  <span class="cat-total-value">{total}</span>')
    lines.append('</div>')
    lines.append("")

    lines.append('<div class="cat-list">')

    for i, row in enumerate(summary, start=1):
        name = row['name']
        count = row['count']
        share = (count / total * 100) if total else 0
        sub = row.get('sub', [])
        safe_name = name.replace('|', '\\|').replace('<', '&lt;').replace('>', '&gt;')
        has_sub = len(sub) > 0
        uid = f"cat-{i}"

        if has_sub:
            lines.append(f'  <input type="checkbox" id="{uid}" class="cat-checkbox">')
            lines.append(f'  <label for="{uid}" class="cat-row has-sub">')
            lines.append(f'    <span class="cat-num">{i}</span>')
            lines.append(f'    <span class="cat-name">{safe_name}</span>')
            lines.append(f'    <span class="cat-count">{count}<span>/ {share:.2f}%</span></span>')
            lines.append(f'    <span class="cat-toggle">›</span>')
            lines.append(f'  </label>')
            lines.append(f'  <div class="cat-details">')
            lines.append(f'    <ul class="cat-sub-list">')
            for sub_row in sub:
                sub_name = sub_row['name']
                sub_count = sub_row['count']
                sub_share = (sub_count / total * 100) if total else 0
                safe_sub_name = sub_name.replace('|', '\\|').replace('<', '&lt;').replace('>', '&gt;')
                lines.append(f'      <li class="cat-sub-item">')
                lines.append(f'        <span></span>')
                lines.append(f'        <span class="cat-sub-name">{safe_sub_name}</span>')
                lines.append(f'        <span class="cat-sub-count">{sub_count}<span>/ {sub_share:.2f}%</span></span>')
                lines.append(f'        <span class="cat-sub-empty"></span>')
                lines.append(f'      </li>')
            lines.append(f'    </ul>')
            lines.append(f'  </div>')
        else:
            lines.append(f'  <div class="cat-row">')
            lines.append(f'    <span class="cat-num">{i}</span>')
            lines.append(f'    <span class="cat-name">{safe_name}</span>')
            lines.append(f'    <span class="cat-count">{count}<span>/ {share:.2f}%</span></span>')
            lines.append(f'    <span></span>')
            lines.append(f'  </div>')

    lines.append('</div>')
    lines.append("")

    return "\n".join(lines)


def main():
    print("Генерация отчета...")
    output_dir = os.path.dirname(OUTPUT_MD_FILE)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    df = parse_excel_files(FILE_PATHS)
    if df.empty:
        print("Нет данных.")
        return
    report = generate_report(df)
    with open(OUTPUT_MD_FILE, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"Готово: {OUTPUT_MD_FILE}")


if __name__ == "__main__":
    main()