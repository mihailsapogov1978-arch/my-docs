#!/bin/bash
# Автоматическая конвертация DOCX → Markdown + очистка + подготовка к MkDocs

set -e  # Останавливаемся при первой ошибке

DOCX_FILE="rawdocs/Pervoe_podkluchenie.docx"
OUTPUT_DIR="docs/Pervoe_podkluchenie"
INDEX_MD="$OUTPUT_DIR/index.md"

echo "🚀 Начинаем конвертацию: $DOCX_FILE"

# Создаём целевую папку
mkdir -p "$OUTPUT_DIR"

# Конвертируем DOCX → Markdown с извлечением медиа
pandoc "$DOCX_FILE" \
  -o "$INDEX_MD" \
  --extract-media="$OUTPUT_DIR" \
  --wrap=none

echo "✅ Конвертация завершена"

# Очищаем Markdown от HTML и стилей
echo "🧹 Очищаем index.md от HTML-разметки..."

sed -i 's/<[^>]*>//g' "$INDEX_MD"              # Удаляем все HTML-теги
sed -i 's/{[^{}]*}//g' "$INDEX_MD"              # Удаляем {style=...}
sed -i 's/<img [^>]*src="\([^"]*\)"[^>]*>/![image](\1)/g' "$INDEX_MD"  # Заменяем <img> на ![image](...)

# Исправляем пути к изображениям (если Pandoc вставил абсолютный путь)
sed -i 's|!\[\](docs/Pervoe_podkluchenie/media/|!\[](media/|g' "$INDEX_MD"

echo "✅ Очистка завершена"

# Добавляем в mkdocs.yml (если ещё нет)
if ! grep -q "Pervoe_podkluchenie/index.md" mkdocs.yml; then
    echo "🔗 Добавляем страницу в mkdocs.yml..."
    sed -i '/nav:/a \  - Первое подключение: Pervoe_podkluchenie/index.md' mkdocs.yml
fi

echo "🎉 Готово! Теперь можно запускать:"
echo "   mkdocs serve --dev-addr=0.0.0.0:8000"