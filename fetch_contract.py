#!/usr/bin/env python3
"""
Скрипт для оформления контрактов в стиле Markdown Material Theme
БЕЗ удаления изображений и данных Google Docs
"""
import sys
from pathlib import Path
import re


def add_material_frontmatter(file_path: str):
    """
    Добавляет YAML frontmatter Material Theme в начало файла.
    Весь остальной контент сохраняется без изменений (включая ![][imageX] и base64 данные).
    Перезаписывает исходный файл.
    """
    input_file = Path(file_path)
    if not input_file.is_file():
        raise FileNotFoundError(f"Файл не найден: {file_path}")

    # Чтение исходного содержимого
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Проверка наличия существующего frontmatter
    has_frontmatter = re.match(r'^---\s*\n', content)

    # Формирование нового frontmatter
    frontmatter = """---
title: "Оказание услуг по настройке подписания документов разных субъектов учета в едином интерфейсе ГИС «Смета ЯНАО»"
reestr_number: "0190200000325015002"
year: 2025
status: "Определение поставщика завершено"
tags: [закупка, 44-ФЗ]
---
"""

    # Формирование итогового содержимого
    if has_frontmatter:
        # Если frontmatter уже существует — заменяем его
        # Находим конец существующего frontmatter (второй ---)
        parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
        if len(parts) >= 3:
            new_content = frontmatter + parts[2].lstrip()
        else:
            new_content = frontmatter + content
    else:
        # Если frontmatter отсутствует — добавляем в начало
        new_content = frontmatter + '\n' + content

    # Перезапись исходного файла БЕЗ изменений содержимого (кроме добавления frontmatter)
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"✅ Файл оформлен в стиле Material Theme: {input_file}")
    print(f"   ВСЕ данные (изображения, base64) сохранены без изменений")


def main():
    if len(sys.argv) != 2:
        print("Использование: python fetch_contract.py <файл.md>")
        print("Пример: python fetch_contract.py contract-0190200000325015002.md")
        sys.exit(1)

    file_to_format = sys.argv[1]
    add_material_frontmatter(file_to_format)


if __name__ == "__main__":
    main()