#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import re

def fix_links():
    base = Path("docs/Meropriyatia")
    if not base.exists():
        print("❌ Папка docs/Meropriyatia не найдена")
        return

    fixed = 0
    for year_dir in base.iterdir():
        if year_dir.is_dir() and year_dir.name.isdigit() and len(year_dir.name) == 4:
            for md_file in year_dir.glob("contract-019020000032*.md"):
                try:
                    content = md_file.read_text(encoding='utf-8')
                except Exception as e:
                    print(f"⚠ Не удалось прочитать {md_file}: {e}")
                    continue

                # Удаляем все старые ссылки
                content = re.sub(
                    r'\[← Вернуться к сводной информации\]\([^)]*\)',
                    '',
                    content
                )

                # Удаляем пустые строки в начале
                lines = [line for line in content.splitlines() if line.strip() != '']
                content = '\n'.join(lines)

                # Добавляем новую ссылку в самое начало
                new_link = '[← Вернуться к сводной информации](/Meropriyatia/svod_gk/)'
                new_content = new_link + '\n\n' + content

                # Сохраняем
                md_file.write_text(new_content, encoding='utf-8')
                print(f"✅ Исправлена ссылка в {md_file}")
                fixed += 1

    print(f"\n🎉 Готово: обновлено {fixed} файлов.")

if __name__ == "__main__":
    fix_links()