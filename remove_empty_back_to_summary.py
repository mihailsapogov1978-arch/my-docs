#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from pathlib import Path

def replace_with_sticky():
    base = Path("docs/Meropriyatia")
    if not base.exists():
        print("❌ Папка docs/Meropriyatia не найдена")
        return

    updated = 0
    for year_dir in base.iterdir():
        if year_dir.is_dir() and year_dir.name.isdigit() and len(year_dir.name) == 4:
            for md_file in year_dir.glob("contract-019020000032*.md"):
                try:
                    content = md_file.read_text(encoding='utf-8')
                except Exception as e:
                    print(f"⚠ Не удалось прочитать {md_file}: {e}")
                    continue

                # Удаляем все старые упоминания ссылки
                content = re.sub(
                    r'\[← Вернуться к сводной информации\]\([^)]*\)',
                    '',
                    content
                )
                content = re.sub(
                    r'<div class="back-to-summary">.*?</div>',
                    '',
                    content,
                    flags=re.DOTALL
                )

                # Убираем пустые строки в начале
                lines = [line for line in content.splitlines() if line.strip() != '']
                content = '\n'.join(lines)

                # Добавляем новую прилипающую ссылку в самое начало
                new_link = '''<div class="back-to-summary-sticky">
  <a href="/Meropriyatia/svod_gk/">← Вернуться к сводной информации</a>
</div>'''

                new_content = new_link + "\n\n" + content

                md_file.write_text(new_content, encoding='utf-8')
                print(f"✅ Обновлена ссылка в {md_file}")
                updated += 1

    print(f"\n🎉 Готово: обновлено {updated} файлов.")

if __name__ == "__main__":
    replace_with_sticky()