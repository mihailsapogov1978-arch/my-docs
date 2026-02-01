import re
import os

# Указываем точный путь к нужному файлу
md_file = r'docs\instrukt\poladmin.md'
print(f"🔍 Обрабатываю файл: {md_file}")

# Проверяем существование
if not os.path.isfile(md_file):
    print("❌ Файл не найден!")
    exit(1)

# Чтение
with open(md_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Замена ![](lk_images/imageN.png) → ![][imageN]
pattern = r'!\[([^\]]*)\]\(lk_images/image(\d+)\.png\)'
def replace_match(match):
    alt_text = match.group(1).strip()
    num = match.group(2)
    if not alt_text:
        alt_text = f"Рисунок {num}"
    return f"![{alt_text}][image{num}]"

new_content, n = re.subn(pattern, replace_match, content)
print(f"🔄 Заменено {n} ссылок")

# Генерация определений
image_dir = r'docs\instrukt\lk_images'
if os.path.isdir(image_dir):
    image_files = sorted([
        f for f in os.listdir(image_dir)
        if f.startswith('image') and f.endswith('.png')
    ])
    definitions = []
    for f in image_files:
        num_match = re.search(r'image(\d+)\.png', f)
        if num_match:
            n = num_match.group(1)
            caption = f"Рисунок {n}"
            definitions.append(f"[image{n}]: lk_images/{f} \"{caption}\"")
    
    if definitions:
        new_content += "\n\n" + "\n".join(definitions)
        print(f"✅ Добавлено {len(definitions)} определений")

# Сохранение
with open(md_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ Готово! Файл обновлён.")