import pandas as pd
import os

def generate_zayavky_report():
    # Чтение файла Excel (лист "Заявки")
    file_path = "zayavky.xlsx"
    df = pd.read_excel(file_path, sheet_name="Заявки", dtype=str)
    
    # 1. Общая статистика
    total = len(df)
    resolved = df[df['Статус'] == 'Решено'].shape[0]
    in_work = df[df['Статус'] == 'В работе'].shape[0]
    
    # 2. Топ-3 активных инициаторов
    initiator_counts = df['Инициатор'].value_counts().head(3)
    
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
    
    print(f"✅ Отчёт сохранён в: {output_path}")
    return md_content

if __name__ == "__main__":
    report = generate_zayavky_report()
    print("\nСодержимое файла:")
    print(report)