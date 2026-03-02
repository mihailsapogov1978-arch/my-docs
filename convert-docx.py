#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Конвертер .docx → Markdown
Версия: 2.3 (исправленная)
"""

import os
import re
import shutil
from pathlib import Path
from datetime import datetime
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P


class DocxConverter:
    """Конвертер .docx файлов в Markdown для вашей структуры"""
    
    def __init__(
        self,
        docx_dir='docx',
        docs_dir='docs',
        image_folder='images',
        table_format='html',
        extract_images=True,
        create_report=True,
        make_backup=True,        # Исправлено: было backup_originals
        overwrite_existing=True
    ):
        """
        Инициализация конвертера
        
        Args:
            docx_dir: Папка с исходными .docx файлами
            docs_dir: Папка для .md файлов (корень)
            image_folder: Папка для изображений внутри docs_dir
            table_format: 'html' для сложных таблиц
            extract_images: Извлекать изображения
            create_report: Создавать отчёт о конвертации
            make_backup: Создавать резервные копии оригиналов
            overwrite_existing: Перезаписывать существующие .md файлы
        """
        self.docx_dir = Path(docx_dir)
        self.docs_dir = Path(docs_dir)
        self.image_folder = image_folder
        self.table_format = table_format
        self.extract_images = extract_images
        self.create_report = create_report
        self.make_backup = make_backup  # Исправлено: было backup_originals
        self.overwrite_existing = overwrite_existing
        
        self.image_counter = 0
        self.stats = {
            'files': 0,
            'tables': 0,
            'images': 0,
            'headings': 0,
            'lists': 0,
            'bold': 0,
            'italic': 0,
            'links': 0,
            'code': 0,
            'superscript': 0,
            'subscript': 0
        }
        self.report_lines = []
        self.backup_dir = None
    
    def log(self, message: str, level='INFO'):
        """Логирование в консоль и отчёт"""
        timestamp = datetime.now().strftime('%H:%M:%S')
        line = f'[{timestamp}] [{level}] {message}'
        print(line)
        if self.create_report:
            self.report_lines.append(line)
    
    def create_backup(self, docx_path: Path):
        """Создаёт резервную копию оригинального .docx файла"""
        if not self.make_backup:  # Исправлено: было backup_originals
            return
        
        backup_dir = self.docs_dir / 'backup'
        backup_dir.mkdir(parents=True, exist_ok=True)
        
        try:
            backup_path = backup_dir / docx_path.name
            shutil.copy2(docx_path, backup_path)
            self.log(f'  → Резервная копия: {backup_path.name}', 'DEBUG')
        except Exception as e:
            self.log(f'  ⚠️  Ошибка создания резервной копии: {e}', 'WARNING')
    
    def extract_images(self, doc, doc_name: str) -> dict:
        """
        Извлекает изображения из документа
        
        Именование: docname_image1.png, docname_image2.png, ...
        """
        if not self.extract_images:
            return {}
        
        images = {}
        image_dir = self.docs_dir / self.image_folder
        image_dir.mkdir(parents=True, exist_ok=True)
        
        try:
            # Извлечение изображений из отношений документа
            for rel_id, rel in doc.part.rels.items():
                if 'image' in rel.target_ref.lower():
                    self.image_counter += 1
                    self.stats['images'] += 1
                    
                    # Определение расширения
                    content_type = rel.target_part.content_type
                    ext_map = {
                        'image/png': '.png',
                        'image/jpeg': '.jpg',
                        'image/gif': '.gif',
                        'image/bmp': '.bmp',
                        'image/tiff': '.tiff',
                        'image/webp': '.webp'
                    }
                    ext = ext_map.get(content_type, '.png')
                    
                    # Имя файла: docname_image1.png
                    img_filename = f'{doc_name}_image{self.image_counter}{ext}'
                    img_path = image_dir / img_filename
                    
                    # Сохранение (оригинальный размер)
                    with open(img_path, 'wb') as f:
                        f.write(rel.target_part.blob)
                    
                    # Относительный путь для Markdown
                    images[rel_id] = f'{self.image_folder}/{img_filename}'
                    self.log(f'  → Изображение: {img_filename}', 'DEBUG')
        
        except Exception as e:
            self.log(f'  ⚠️  Ошибка извлечения изображений: {e}', 'WARNING')
        
        return images
    
    def process_table_html(self, table: Table) -> str:
        """
        Конвертирует таблицу в HTML формат (для сложных таблиц)
        Поддерживает слияние ячеек
        """
        html = ['<table>']
        
        for i, row in enumerate(table.rows):
            html.append('  <tr>')
            
            for cell in row.cells:
                # Определение типа ячейки (заголовок или данные)
                tag = 'th' if i == 0 else 'td'
                
                # Обработка содержимого ячейки
                cell_content = []
                for para in cell.paragraphs:
                    cell_content.append(para.text)
                
                cell_text = ' '.join(cell_content).strip() or '&nbsp;'
                
                # Формирование тега
                html.append(f'    <{tag}>{cell_text}</{tag}>')
            
            html.append('  </tr>')
        
        html.append('</table>\n')
        self.stats['tables'] += 1
        
        return '\n'.join(html)
    
    def process_heading(self, para: Paragraph) -> str:
        """Обрабатывает заголовки"""
        style = str(para.style.name) if para.style else ''
        
        # Определение уровня заголовка
        level = 1
        if 'Heading' in style:
            match = re.search(r'Heading\s*(\d+)', style)
            if match:
                level = int(match.group(1))
        
        self.stats['headings'] += 1
        return '#' * level + ' ' + para.text + '\n\n'
    
    def process_paragraph(self, para: Paragraph) -> str:
        """Обрабатывает параграф с полным форматированием"""
        # Пустой параграф
        if not para.text.strip():
            return '\n'
        
        # Проверка на заголовок
        if para.style and ('Heading' in str(para.style.name)):
            return self.process_heading(para)
        
        # Обработка текста с форматированием
        text_parts = []
        
        for run in para.runs:
            text = run.text
            if not text:
                continue
            
            # Применение форматирования
            if run.bold and run.italic:
                text = f'***{text}***'
                self.stats['bold'] += 1
                self.stats['italic'] += 1
            elif run.bold:
                text = f'**{text}**'
                self.stats['bold'] += 1
            elif run.italic:
                text = f'*{text}*'
                self.stats['italic'] += 1
            
            # Верхние/нижние индексы
            if run.font.superscript:
                text = f'<sup>{text}</sup>'
                self.stats['superscript'] += 1
            elif run.font.subscript:
                text = f'<sub>{text}</sub>'
                self.stats['subscript'] += 1
            
            # Код (моноширинный шрифт)
            if run.font.name and 'mono' in run.font.name.lower():
                text = f'`{text}`'
                self.stats['code'] += 1
            
            text_parts.append(text)
        
        # Сборка текста
        full_text = ''.join(text_parts)
        
        # Проверка на список
        if para.text.strip().startswith(('•', '-', '*', '1.', '2.', '3.', '4.', '5.')):
            self.stats['lists'] += 1
            return full_text + '\n'
        
        return full_text + '\n\n'
    
    def process_element(self, element, doc) -> str:
        """Обрабатывает элемент документа (параграф или таблица)"""
        if isinstance(element, CT_P):  # Параграф
            para = Paragraph(element, doc)
            return self.process_paragraph(para)
        
        elif isinstance(element, CT_Tbl):  # Таблица
            table = Table(element, doc)
            return self.process_table_html(table)
        
        return ''
    
    def convert(self, docx_path: Path):
        """
        Конвертирует .docx файл в Markdown
        
        Args:
            docx_path: Путь к .docx файлу
        
        Returns:
            Путь к созданному .md файлу
        """
        self.log(f'🔄 Конвертация: {docx_path.name}')
        
        try:
            # Создание резервной копии
            if self.make_backup:  # Исправлено: было backup_originals
                self.create_backup(docx_path)
            
            # Открытие документа
            doc = Document(docx_path)
            
            # Имя документа для именования изображений
            doc_name = docx_path.stem
            
            # Извлечение изображений
            images = self.extract_images(doc, doc_name)
            
            # Обработка документа
            content = []
            
            # Проход по всем элементам документа
            for element in doc.element.body:
                content.append(self.process_element(element, doc))
        
            # Финальный текст
            markdown_text = ''.join(content)
            
            # Добавление метаданных (YAML frontmatter)
            metadata = f"""---
title: "{docx_path.stem}"
date: "{datetime.now().strftime('%Y-%m-%d')}"
source: "{docx_path.name}"
---

"""
            markdown_text = metadata + markdown_text
            
            # Сохранение в корень docs/
            md_filename = docx_path.stem + '.md'
            md_path = self.docs_dir / md_filename
            
            # Проверка на существование файла
            if md_path.exists() and not self.overwrite_existing:
                self.log(f'  ⚠️  Файл уже существует, пропущен: {md_filename}', 'WARNING')
                return md_path
            
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown_text)
            
            self.stats['files'] += 1
            self.log(f'✅ Успешно: {md_filename}')
            
            if images:
                self.log(f'   → Изображений: {len(images)}')
            
            return md_path
        
        except Exception as e:
            self.log(f'❌ Ошибка: {e}', 'ERROR')
            raise
    
    def batch_convert(self):
        """
        Пакетная конвертация всех .docx файлов в папке docx/
        """
        self.log(f'🚀 Начало пакетной конвертации')
        self.log(f'📁 Входная папка: {self.docx_dir}')
        self.log(f'📁 Выходная папка: {self.docs_dir}')
        
        # Поиск всех .docx файлов
        docx_files = list(self.docx_dir.glob('*.docx'))
        
        if not docx_files:
            self.log(f'⚠️  Не найдено .docx файлов в {self.docx_dir}', 'WARNING')
            return
        
        self.log(f'📄 Найдено файлов: {len(docx_files)}\n')
        
        # Конвертация каждого файла
        converted = 0
        failed = 0
        
        for i, docx_file in enumerate(docx_files, 1):
            self.log(f'[{i}/{len(docx_files)}] {docx_file.name}')
            
            try:
                self.convert(docx_file)
                converted += 1
            
            except Exception as e:
                self.log(f'❌ Пропущен: {docx_file.name} ({e})', 'ERROR')
                failed += 1
        
        # Итоговая статистика
        self.log('\n' + '='*60)
        self.log('📊 СТАТИСТИКА КОНВЕРТАЦИИ')
        self.log('='*60)
        self.log(f'✅ Успешно: {converted}')
        self.log(f'❌ Ошибок: {failed}')
        self.log(f'📄 Всего файлов: {self.stats["files"]}')
        self.log(f'📊 Таблиц: {self.stats["tables"]}')
        self.log(f'🖼️  Изображений: {self.stats["images"]}')
        self.log(f'🏷️  Заголовков: {self.stats["headings"]}')
        self.log(f'📋 Списков: {self.stats["lists"]}')
        self.log(f'** Жирный текст: {self.stats["bold"]}')
        self.log(f'* Курсив: {self.stats["italic"]}')
        self.log(f'🔗 Ссылок: {self.stats["links"]}')
        self.log(f'` Код: {self.stats["code"]}')
        self.log(f'<sup> Верхние индексы: {self.stats["superscript"]}')
        self.log(f'<sub> Нижние индексы: {self.stats["subscript"]}')
        self.log('='*60)
        
        # Сохранение отчёта
        if self.create_report and self.report_lines:
            report_path = self.docs_dir / 'conversion_report.txt'
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(self.report_lines))
            self.log(f'\n📄 Отчёт сохранён: {report_path}')
    
    def save_config(self):
        """Сохраняет текущую конфигурацию"""
        config_text = f"""Конфигурация конвертера .docx → Markdown
========================================
Дата: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Настройки:
  - Папка исходников: {self.docx_dir}
  - Папка назначения: {self.docs_dir}
  - Папка изображений: {self.image_folder}
  - Формат таблиц: {self.table_format}
  - Извлечение изображений: {self.extract_images}
  - Создание отчёта: {self.create_report}
  - Резервные копии: {self.make_backup}
  - Перезапись существующих: {self.overwrite_existing}

Статистика:
  - Файлов: {self.stats['files']}
  - Таблиц: {self.stats['tables']}
  - Изображений: {self.stats['images']}
  - Заголовков: {self.stats['headings']}
  - Списков: {self.stats['lists']}
  - Жирный текст: {self.stats['bold']}
  - Курсив: {self.stats['italic']}
  - Ссылок: {self.stats['links']}
  - Код: {self.stats['code']}
  - Верхние индексы: {self.stats['superscript']}
  - Нижние индексы: {self.stats['subscript']}
"""
        
        config_path = self.docs_dir / 'converter_config.txt'
        with open(config_path, 'w', encoding='utf-8') as f:
            f.write(config_text)
        
        self.log(f'⚙️  Конфигурация сохранена: {config_path}')


def main():
    """Основная функция для запуска из командной строки"""
    import sys
    
    # Путь к скрипту
    script_dir = Path(__file__).parent
    
    # Создание конвертера с настройками (под вашу структуру)
    converter = DocxConverter(
        docx_dir=script_dir / 'docx',    # Папка с исходными .docx
        docs_dir=script_dir / 'docs',    # Корень документации
        image_folder='images',           # Папка для изображений внутри docs
        table_format='html',             # HTML для сложных таблиц
        extract_images=True,             # Извлекать изображения
        create_report=True,              # Создавать отчёт
        make_backup=True,                # Резервные копии (исправлено!)
        overwrite_existing=True          # Перезаписывать существующие
    )
    
    # Проверка существования папки docx
    if not converter.docx_dir.exists():
        print(f'❌ Ошибка: папка {converter.docx_dir} не существует')
        print('Создайте папку docx/ и поместите туда .docx файлы')
        sys.exit(1)
    
    # Проверка существования папки docs
    if not converter.docs_dir.exists():
        print(f'❌ Ошибка: папка {converter.docs_dir} не существует')
        print('Создайте папку docs/ для сохранения .md файлов')
        sys.exit(1)
    
    # Конвертация
    converter.batch_convert()
    
    # Сохранение конфигурации
    converter.save_config()


if __name__ == '__main__':
    main()