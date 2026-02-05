import pandas as pd
import os

def generate_zayavky_report():
    # Чтение файла Excel (лист "Заявки")
    file_path = "zayavky.xlsx"
    
    try:
        # Читаем Excel файл
        df = pd.read_excel(file_path, sheet_name="Заявки", dtype=str)
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return
    
    # Заполняем NaN значения пустыми строками
    df = df.fillna('')
    
    # Отладочная информация
    print(f"Всего строк: {len(df)}")
    print(f"Названия колонок: {list(df.columns)}")
    
    # Проверяем, есть ли колонка "Статус"
    if 'Статус' not in df.columns:
        print("Колонка 'Статус' не найдена!")
        # Пробуем найти колонку с другим регистром или пробелами
        for col in df.columns:
            if 'статус' in col.lower():
                print(f"Возможно колонка статусов: '{col}'")
                df['Статус'] = df[col]
                break
    
    # Очищаем значения в колонке Статус от лишних пробелов и HTML-тегов
    df['Статус'] = df['Статус'].astype(str).str.strip()
    
    # Убираем возможные HTML-теги
    df['Статус'] = df['Статус'].str.replace(r'<br>', '', regex=True)
    df['Статус'] = df['Статус'].str.replace(r'<.*?>', '', regex=True)
    
    # 1. Общая статистика
    total = len(df)
    
    # Подсчет статусов
    status_counts = df['Статус'].value_counts()
    
    print("\nРаспределение статусов:")
    for status, count in status_counts.items():
        print(f"  '{status}': {count}")
    
    # Получаем точные значения
    resolved = status_counts.get('Решено', 0)
    in_work = status_counts.get('В работе', 0)
    
    # 2. Топ-3 активных инициаторов
    # Очищаем имена инициаторов от лишних пробелов
    if 'Инициатор' in df.columns:
        df['Инициатор'] = df['Инициатор'].astype(str).str.strip()
        initiator_counts = df['Инициатор'].value_counts().head(3)
    else:
        print("Колонка 'Инициатор' не найдена!")
        initiator_counts = pd.Series()
    
    # Создаем таблицу для топ-3
    top_3_table = "| Инициатор | Количество заявок |\n|:---|---:|\n"
    for name, count in initiator_counts.items():
        top_3_table += f"| {name} | {count} |\n"
    
    # Формируем содержимое Markdown
    md_content = f"""## 1. ОБЩАЯ СТАТИСТИКА

Всего заявок: {total} из них
решено: {resolved}, в работе: {in_work}

## 2. Топ-3 активных инициаторов

{top_3_table}"""
    
    # Сохраняем в файл
    output_dir = "docs"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "zayavky.md")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    
    print(f"\n✅ Отчёт сохранён в: {output_path}")
    print("\nСодержимое файла:")
    print(md_content)
    
    return md_content

if __name__ == "__main__":
    report = generate_zayavky_report()