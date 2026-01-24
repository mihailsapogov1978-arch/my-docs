#!/bin/bash
# Исправляет пути к изображениям в index.md (для Windows PowerShell)

set -e

if [ $# -ne 1 ]; then
    echo "Использование: $0 <имя_папки>"
    exit 1
fi

NAME="$1"
INDEX_MD="docs/$NAME/index.md"

echo "🔧 Исправляем пути к изображениям для: $NAME"

# Проверяем, что файл существует
if [ ! -f "$INDEX_MD" ]; then
    echo "❌ Файл не найден: $INDEX_MD"
    exit 1
fi

# Заменяем docs/ИмяПапки/media/ → media/
sed -i "s|docs/$NAME/media/|media/|g" "$INDEX_MD"

echo "✅ Пути исправлены: $INDEX_MD"