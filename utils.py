"""
Общие утилиты для проектов ГИС «Смета ЯНАО»
"""
import os
import html
from typing import List, Dict, Any, Optional
from datetime import datetime


def detect_encoding(filepath: str) -> str:
    """
    Определение кодировки файла методом перебора.
    
    Args:
        filepath: Путь к файлу
        
    Returns:
        Название кодировки (utf-8-sig, utf-8, windows-1251, cp1251)
    """
    encodings = ['utf-8-sig', 'utf-8', 'windows-1251', 'cp1251']
    for enc in encodings:
        try:
            with open(filepath, 'r', encoding=enc) as f:
                f.read()
            return enc
        except (UnicodeDecodeError, UnicodeError):
            continue
    return 'utf-8'


def escape_html(text: str) -> str:
    """
    Экранирование HTML-символов для защиты от XSS.
    
    Args:
        text: Исходный текст
        
    Returns:
        Экранированный текст
    """
    if not text:
        return ''
    return html.escape(str(text))


def generate_html_table(
    data: List[Dict[str, Any]],
    title: str,
    subtitle: str = '',
    columns: Optional[List[str]] = None,
    output_path: str = 'output.html'
) -> str:
    """
    Генерация HTML-страницы с таблицей данных.
    
    Args:
        data: Список словарей с данными
        title: Заголовок страницы
        subtitle: Подзаголовок/статистика
        columns: Список колонок (если None, берутся из первого элемента)
        output_path: Путь для сохранения файла
        
    Returns:
        Путь к сохранённому файлу
    """
    if not data:
        print("  ⚠️ Нет данных для генерации HTML")
        return ''
    
    if columns is None:
        columns = list(data[0].keys())
    
    # Базовые стили
    css = """
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', sans-serif; background: #f0f4f8; padding: 30px; }
        .container { max-width: 1200px; margin: 0 auto; }
        .header {
            background: linear-gradient(135deg, #2b6cb0, #2c5282);
            color: white;
            padding: 30px;
            border-radius: 12px;
            margin-bottom: 30px;
        }
        .header h1 { font-size: 28px; }
        .stats { display: flex; gap: 20px; margin-top: 10px; flex-wrap: wrap; }
        .stats span { background: rgba(255,255,255,0.15); padding: 6px 16px; border-radius: 20px; }
        table { width: 100%; border-collapse: collapse; background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
        th { background: #edf2f7; padding: 14px; text-align: left; font-weight: 600; }
        td { padding: 12px 14px; border-bottom: 1px solid #e2e8f0; }
        tr:hover { background: #f7fafc; }
        .footer { text-align: center; margin-top: 30px; color: #a0aec0; }
        @media (max-width: 600px) { body { padding: 15px; } th, td { padding: 8px 10px; font-size: 12px; } }
    """
    
    html_content = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{escape_html(title)}</title>
    <style>{css}</style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{escape_html(title)}</h1>
            <div class="stats">
                <span>📦 Всего: {len(data)}</span>
                <span>🔄 Обновлено: {datetime.now().strftime('%d.%m.%Y %H:%M')}</span>
                {subtitle}
            </div>
        </div>
        <table>
            <thead>
                <tr>
"""
    
    # Заголовки таблицы
    for col in columns:
        html_content += f"                    <th>{escape_html(col)}</th>\n"
    
    html_content += """                </tr>
            </thead>
            <tbody>
"""
    
    # Данные таблицы с экранированием
    for row in data:
        html_content += "                <tr>\n"
        for col in columns:
            value = escape_html(str(row.get(col, '')))
            html_content += f"                    <td>{value}</td>\n"
        html_content += "                </tr>\n"
    
    html_content += f"""            </tbody>
        </table>
        <div class="footer">{escape_html(title)} • Сгенерировано: {datetime.now().strftime('%d.%m.%Y %H:%M')}</div>
    </div>
</body>
</html>
"""
    
    # Создаём директорию если нужно
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    
    # Сохраняем файл
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"  ✅ HTML сгенерирован: {output_path}")
    return output_path


def safe_get(dictionary: Dict, key: str, default: Any = '') -> Any:
    """
    Безопасное получение значения из словаря.
    
    Args:
        dictionary: Исходный словарь
        key: Ключ для получения
        default: Значение по умолчанию
        
    Returns:
        Значение или default
    """
    return dictionary.get(key, default) if dictionary else default


def format_price(price_value: float, currency: str = '₽') -> str:
    """
    Форматирование цены для отображения.
    
    Args:
        price_value: Числовое значение цены
        currency: Символ валюты
        
    Returns:
        Отформатированная строка (например, "1 234 567,89 ₽")
    """
    formatted = f"{price_value:,.2f}".replace(',', ' ').replace('.', ',')
    return f"{formatted} {currency}"
