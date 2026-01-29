# format_contract_files.py
import os
import re

def format_contract_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Извлекаем метаданные из начала файла (если есть)
    title_match = re.search(r'title:\s*"([^"]+)"', content)
    reestr_match = re.search(r'reestr_number:\s*"([^"]+)"', content)
    year_match = re.search(r'year:\s*(\d+)', content)
    status_match = re.search(r'status:\s*"([^"]+)"', content)
    tags_match = re.search(r'tags:\s*$(.*?)$', content, re.DOTALL)

    title = title_match.group(1) if title_match else ""
    reestr = reestr_match.group(1) if reestr_match else ""
    year = year_match.group(1) if year_match else "2025"
    status = status_match.group(1) if status_match else "Не указан"
    tags = tags_match.group(1).strip() if tags_match else "[закупка, 44-ФЗ]"

    # 2. Извлекаем основной текст (всё после метаданных)
    body_start = content.find("Оказание услуг")
    if body_start == -1:
        body_start = 0
    body = content[body_start:].strip()

    # 3. Разбиваем на логические блоки
    lines = body.splitlines()
    formatted_lines = []

    # Добавляем YAML front matter
    formatted_lines.append("---")
    formatted_lines.append(f'title: "{title}"')
    formatted_lines.append(f'reestr_number: "{reestr}"')
    formatted_lines.append(f'year: {year}')
    formatted_lines.append(f'status: "{status}"')
    formatted_lines.append(f'tags: {tags}')
    formatted_lines.append("---")
    formatted_lines.append("")

    # Обрабатываем остальное
    in_table = False
    table_buffer = []

    i = 0
    while i < len(lines):
        line = lines[i].rstrip()

        # Пропускаем пустые строки в начале
        if not formatted_lines[-1] and not line:
            i += 1
            continue

        # Определяем заголовки
        if re.match(r'^\d+\.\s*\S', line):  # 1. Общие сведения
            formatted_lines.append(f"## {line.strip()}")
        elif re.match(r'^\d+\.\d+\.\s*\S', line):  # 5.1. Требования...
            formatted_lines.append(f"### {line.strip()}")
        elif line.startswith("ТЕХНИЧЕСКОЕ ЗАДАНИЕ"):
            formatted_lines.append("## ТЕХНИЧЕСКОЕ ЗАДАНИЕ")
        elif line.startswith("Основная информация"):
            formatted_lines.append("## Основная информация")
        elif line.startswith("Приложение") and "Календарный план" in line:
            formatted_lines.append("## Приложение № 2 - Календарный план")
        elif line.startswith("CПЕЦИФИКАЦИЯ") or line.startswith("СПЕЦИФИКАЦИЯ"):
            formatted_lines.append("## СПЕЦИФИКАЦИЯ")
        elif line.startswith("Перечень терминов") or line.startswith("Перечень ЭД"):
            formatted_lines.append("### " + line.strip())
        elif re.match(r'^\s*-\s*\S', line):  # Список
            formatted_lines.append(line)
        elif "|" in line and ("---" in line or "Термин" in line or "№ п/п" in line or "Наименование товара" in line):
            # Начало таблицы
            if not in_table:
                in_table = True
                table_buffer = []
            table_buffer.append(line)
        elif in_table and "|" in line:
            table_buffer.append(line)
        elif in_table and ("|" not in line or not line.strip()):
            # Конец таблицы
            in_table = False
            # Форматируем таблицу
            for tbl_line in table_buffer:
                formatted_lines.append(tbl_line)
            if line.strip():
                formatted_lines.append(line)
        else:
            # Обычный абзац
            if line.strip():
                formatted_lines.append(line)
            else:
                formatted_lines.append("")

        i += 1

    # Если остались данные в буфере таблицы — добавляем
    if in_table and table_buffer:
        for tbl_line in table_buffer:
            formatted_lines.append(tbl_line)

    # Удаляем лишние пустые строки
    cleaned = []
    prev_empty = False
    for line in formatted_lines:
        if line == "":
            if not prev_empty:
                cleaned.append(line)
            prev_empty = True
        else:
            cleaned.append(line)
            prev_empty = False

    # Записываем результат
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(cleaned))

    print(f"✅ Отформатирован: {filepath}")

def main():
    base_dir = "docs/Meropriyatia"
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.startswith("contract-") and file.endswith(".md"):
                full_path = os.path.join(root, file)
                format_contract_file(full_path)

if __name__ == "__main__":
    main()