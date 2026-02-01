import re
import sys
from pathlib import Path

def format_number_with_spaces(num_str):
    """Форматирует числа с пробелами между тысячами."""
    try:
        # Убираем все пробелы и точки
        cleaned = num_str.replace(' ', '').replace('.', '')
        num = float(cleaned)
        # Форматируем с пробелами вместо запятых
        formatted = f"{num:,.2f}".replace(',', ' ').replace('.', ',')
        return formatted
    except:
        return num_str

def create_toc(headings):
    """Создает оглавление (Table of Contents) на основе заголовков."""
    if not headings:
        return ""
    
    toc_lines = ["## Оглавление (Table of Contents)", ""]
    
    for level, title in headings:
        indent = "  " * (level - 2)  # Отступ для вложенных заголовков (начиная с h2)
        # Создаем anchor из заголовка
        anchor = title.lower().replace(' ', '-').replace('.', '').replace(',', '')
        anchor = re.sub(r'[^\w\-]', '', anchor)
        toc_lines.append(f"{indent}- [{title}](#{anchor})")
    
    return '\n'.join(toc_lines) + '\n\n'

def process_markdown_content(lines):
    """Обрабатывает содержимое Markdown и преобразует в стиль Material Theme."""
    processed_lines = []
    headings = []  # Для создания TOC
    in_table = False
    table_rows = []
    
    for i, line in enumerate(lines):
        # Обработка заголовков
        if line.startswith('#'):
            # Определяем уровень заголовка
            level = len(line.split()[0])
            title = line[level:].strip()
            
            # Сохраняем для TOC (только h2 и выше)
            if level >= 2:
                headings.append((level, title))
            
            # Обрабатываем разные уровни заголовков
            if level == 1:
                processed_lines.append(f"# {title}")
                processed_lines.append('')
            elif level == 2:
                processed_lines.append(f"## {title}")
                processed_lines.append('')
            elif level == 3:
                processed_lines.append(f"### {title}")
                processed_lines.append('')
            else:
                processed_lines.append(line)
        
        # Обработка таблиц
        elif '|' in line:
            if not in_table:
                in_table = True
                table_rows = [line]
            else:
                table_rows.append(line)
            
            # Проверяем, закончилась ли таблица
            if i + 1 >= len(lines) or '|' not in lines[i + 1]:
                in_table = False
                # Форматируем таблицу
                if len(table_rows) > 1:
                    # Добавляем строку заголовка
                    header = table_rows[0]
                    separator = '|' + '|'.join([':---' for _ in range(len(header.split('|')) - 2)]) + '|'
                    processed_lines.append(header)
                    processed_lines.append(separator)
                    processed_lines.extend(table_rows[1:])
                else:
                    processed_lines.extend(table_rows)
                processed_lines.append('')
        
        # Форматирование цен
        elif ('руб.' in line or 'рублей' in line or '₽' in line) and not in_table:
            # Ищем числа с плавающей точкой
            patterns = [
                r'(\d{1,3}(?:[ ,]\d{3})*\.\d{2})',  # 15925000.00
                r'(\d{1,3}(?:[ ,]\d{3})+)',         # 15925000
            ]
            
            for pattern in patterns:
                matches = re.findall(pattern, line)
                for match in matches:
                    formatted = format_number_with_spaces(match)
                    line = line.replace(match, formatted)
            
            processed_lines.append(line)
        
        # Обработка списков
        elif line.strip().startswith(('* ', '- ', '+ ', '1. ', '2. ', '3. ')):
            if line.strip().startswith('* '):
                # Маркированный список
                processed_lines.append(f"* {line.strip()[2:]}")
            elif line.strip().startswith(('- ', '+ ')):
                # Другие маркированные списки
                processed_lines.append(f"* {line.strip()[2:]}")
            elif re.match(r'^\d+\.', line.strip()):
                # Нумерованный список
                processed_lines.append(line)
            else:
                processed_lines.append(line)
        
        # Обработка блоков кода
        elif line.strip().startswith('```'):
            processed_lines.append(line)
        
        # Обычный текст
        else:
            processed_lines.append(line)
    
    return processed_lines, headings

def extract_frontmatter(content):
    """Извлекает frontmatter из документа."""
    lines = content.split('\n')
    frontmatter_lines = []
    main_content_lines = []
    in_frontmatter = False
    
    for line in lines:
        if line.strip() == '---' and not in_frontmatter:
            in_frontmatter = True
            frontmatter_lines.append(line)
        elif line.strip() == '---' and in_frontmatter:
            in_frontmatter = False
            frontmatter_lines.append(line)
        elif in_frontmatter:
            frontmatter_lines.append(line)
        else:
            main_content_lines.append(line)
    
    return frontmatter_lines, main_content_lines

def format_frontmatter_as_table(frontmatter_lines):
    """Форматирует frontmatter в виде таблицы Material Theme."""
    if not frontmatter_lines:
        return []
    
    formatted = []
    
    # Добавляем заголовок
    formatted.append("## Основная информация")
    formatted.append('')
    formatted.append('| Параметр | Значение |')
    formatted.append('|:--- |:--- |')
    
    for line in frontmatter_lines:
        if line.strip() == '---':
            continue
        
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            
            # Обработка специальных ключей
            if key == 'title':
                formatted.append(f"| **Заголовок** | {value} |")
            elif key == 'reestr_number':
                formatted.append(f"| **Реестровый номер** | {value} |")
            elif key == 'year':
                formatted.append(f"| **Год** | {value} |")
            elif key == 'status':
                formatted.append(f"| **Статус** | {value} |")
            elif key == 'tags':
                # Обработка тегов
                tags = value.strip('[]').replace('"', '').replace("'", '')
                formatted.append(f"| **Теги** | {tags} |")
            else:
                formatted.append(f"| {key} | {value} |")
    
    formatted.append('')
    return formatted

def process_markdown_file(input_file):
    """Обрабатывает Markdown файл и перезаписывает его в стиле Material Theme."""
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Извлекаем frontmatter и основное содержимое
    frontmatter_lines, main_content_lines = extract_frontmatter(content)
    
    # Обрабатываем основное содержимое
    processed_lines, headings = process_markdown_content(main_content_lines)
    
    # Собираем финальный документ
    final_content = []
    
    # 1. Добавляем frontmatter (если есть)
    if frontmatter_lines:
        final_content.extend(frontmatter_lines)
        final_content.append('')
    
    # 2. Добавляем заголовок из frontmatter (если есть)
    title = None
    for line in frontmatter_lines:
        if line.startswith('title:'):
            title = line.split(':', 1)[1].strip().strip('"\'')
            break
    
    if title:
        final_content.append(f"# {title}")
        final_content.append('')
    
    # 3. Добавляем таблицу с основной информацией (если есть frontmatter)
    if frontmatter_lines:
        frontmatter_table = format_frontmatter_as_table(frontmatter_lines)
        final_content.extend(frontmatter_table)
    
    # 4. Добавляем оглавление (если есть заголовки)
    if headings:
        toc = create_toc(headings)
        final_content.append(toc)
    
    # 5. Добавляем обработанное содержимое
    final_content.extend(processed_lines)
    
    # Записываем обратно
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(final_content))

def main():
    # Проверяем аргументы
    if len(sys.argv) != 2:
        print("Использование: python fetch_contract.py <файл.md>")
        print("Пример: python fetch_contract.py ./docs/Meropriyatia/2025/contract-0190200000325007340.md")
        sys.exit(1)
    
    # Получаем имя файла
    input_file = sys.argv[1]
    
    # Проверяем существование файла
    if not Path(input_file).exists():
        print(f"Ошибка: Файл '{input_file}' не найден!")
        sys.exit(1)
    
    try:
        print(f"Обработка файла: {input_file}")
        process_markdown_file(input_file)
        print(f"Файл успешно перезаписан в стиле Material Theme с оглавлением!")
        
    except Exception as e:
        print(f"Ошибка при обработке файла: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()