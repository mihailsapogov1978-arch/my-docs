#!/bin/bash
# Создаёт шаблон новой доработки

if [ $# -ne 2 ]; then
    echo "Использование: $0 <год> <короткое-имя>"
    echo "Пример: $0 2024 интеграция-с-фнс"
    exit 1
fi

YEAR="$1"
SLUG="$2"
DIR="docs/Meropriyatia/$YEAR"
FILE="$DIR/$SLUG.md"

mkdir -p "$DIR"

cat > "$FILE" <<EOF
---
title: 
year: $YEAR
status: в работе
contract: 
related_systems: []
tags: []
---

# 

## Контекст

## Требования

## Диаграмма процесса
<!-- ![BPMN](../../bpmn/$SLUG.svg) -->

## Результат

## Связанные доработки
EOF

echo "✅ Создано: $FILE"