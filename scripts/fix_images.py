# fix_images.py
import re
import requests
import os
import sys
from urllib.parse import urlparse, urljoin

def download_image(url, folder="docs/media"):
    os.makedirs(folder, exist_ok=True)
    
    # Улучшенные заголовки для Google
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Referer": "https://docs.google.com/",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        
        # Определяем расширение по Content-Type или имени
        content_type = response.headers.get('content-type', '')
        ext = '.png'
        if 'jpeg' in content_type or 'jpg' in content_type:
            ext = '.jpg'
        elif 'gif' in content_type:
            ext = '.gif'
        elif 'webp' in content_type:
            ext = '.webp'
        
        # Генерируем имя файла
        filename = f"img_{hash(url) % 100000}{ext}"
        path = os.path.join(folder, filename)
        
        with open(path, "wb") as f:
            f.write(response.content)
        
        return f"media/{filename}"
    except Exception as e:
        print(f"❌ Не удалось скачать {url}: {e}")
        return None

def process_md(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Поддерживаем оба формата:
    # 1. https://docs.google.com/uc?id=...&export=download
    # 2. https://drive.google.com/uc?id=...
    pattern = r'!\[([^\]]*)\]\(\s*(https?://(?:docs\.google\.com|drive\.google\.com)/uc\?[^)\s]+)\s*\)'
    matches = list(re.finditer(pattern, content))

    for match in reversed(matches):
        alt, url = match.groups()
        local_path = download_image(url)
        if local_path:
            new_link = f"![{alt}]({local_path})"
            content = content[:match.start()] + new_link + content[match.end():]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Обработан: {filepath}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python fix_images.py <файл.md>")
        sys.exit(1)
    process_md(sys.argv[1])