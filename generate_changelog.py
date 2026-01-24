import subprocess
import os
import sys

def get_git_log():
    """Получает историю коммитов"""
    try:
        result = subprocess.run(
            ['git', 'log', '--pretty=format:%h|%an|%ad|%s', '--date=short', '-n', '20'],
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        return result.stdout.strip().split('\n')
    except Exception as e:
        print(f"Ошибка: {e}")
        return []

def main():
    commits = get_git_log()
    
    if not commits:
        print("Нет коммитов или не Git репозиторий")
        return
    
    content = ["# Журнал изменений\n", "\n"]
    current_date = ""
    
    for line in commits:
        if not line:
            continue
            
        parts = line.split('|', 3)
        if len(parts) < 4:
            continue
            
        hash_, author, date, message = parts
        
        if date != current_date:
            current_date = date
            content.append(f"## {date}\n")
        
        content.append(f"* **{hash_}** - {message} ({author})\n")
    
    # Записываем в файл
    os.makedirs('docs', exist_ok=True)
    
    # ЯВНО указываем UTF-8 с BOM для Windows
    with open('docs/changelog.md', 'w', encoding='utf-8-sig') as f:
        f.writelines(content)
    
    print("✓ Changelog успешно обновлен!")

if __name__ == "__main__":
    main()
