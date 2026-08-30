import os
import time
import csv
import requests
from datetime import datetime

# ========== НАСТРОЙКИ ==========
USERNAME = "mdsapogov@yanao.ru"
PASSWORD = "Ntyybc123"
LOGIN_URL = "https://help.krista.ru/login"
EXPORT_URL = "https://help.krista.ru/deferredFiles/6700409a-9318-4d39-b9f0-d2917f44ef40"

DOWNLOAD_DIR = os.path.join(os.getcwd(), "downloads_tickets")
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def login_and_download():
    """Авторизация и скачивание файла"""
    print("=" * 60)
    print("ЗАГРУЗКА ЗАЯВОК help.krista.ru")
    print("=" * 60)
    
    # Создаём сессию
    session = requests.Session()
    
    # Заголовки как у браузера
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://help.krista.ru",
        "Referer": "https://help.krista.ru/login",
    }
    
    # Данные для входа
    login_data = {
        "username": USERNAME,
        "password": PASSWORD,
        "rememberMe": "true",
    }
    
    print("\n  🔑 Авторизация...")
    
    try:
        # Шаг 1: Отправляем запрос на вход
        response = session.post(LOGIN_URL, data=login_data, headers=headers, timeout=30)
        
        # Проверяем, что авторизация прошла
        if "login" in response.url.lower():
            print("  ❌ Авторизация не удалась. Проверьте логин/пароль.")
            return
        
        print("  ✅ Авторизация успешна")
        
        # Шаг 2: Скачиваем файл
        print(f"\n  📤 Скачивание файла...")
        
        file_response = session.get(EXPORT_URL, headers=headers, timeout=30)
        
        if file_response.status_code == 200:
            # Определяем расширение
            content_type = file_response.headers.get("Content-Type", "")
            ext = ".csv" if "csv" in content_type else ".xlsx" if "excel" in content_type else ".csv"
            
            filename = f"tickets_{datetime.now().strftime('%Y%m%d_%H%M%S')}{ext}"
            filepath = os.path.join(DOWNLOAD_DIR, filename)
            
            with open(filepath, "wb") as f:
                f.write(file_response.content)
            
            print(f"  ✅ Файл скачан: {filename} ({len(file_response.content)} байт)")
            
            # Шаг 3: Парсим CSV
            tickets = parse_tickets(filepath)
            if tickets:
                html_path = generate_html(tickets)
                print(f"\n  ✅ HTML сгенерирован: {html_path}")
                print(f"  📊 Всего заявок: {len(tickets)}")
        else:
            print(f"  ❌ Ошибка скачивания: HTTP {file_response.status_code}")
            
    except requests.exceptions.Timeout:
        print("  ❌ Таймаут. Попробуйте позже.")
    except Exception as e:
        print(f"  ❌ Ошибка: {e}")

def parse_tickets(csv_path):
    """Парсинг CSV с автоопределением кодировки"""
    print("\n  📊 Парсинг заявок...")
    
    encodings = ["utf-8-sig", "utf-8", "windows-1251", "cp1251"]
    content = None
    
    for enc in encodings:
        try:
            with open(csv_path, "r", encoding=enc) as f:
                content = f.read()
            print(f"  ✅ Кодировка: {enc}")
            break
        except:
            continue
    
    if content is None:
        print("  ❌ Не удалось прочитать файл")
        return []
    
    tickets = []
    try:
        reader = csv.DictReader(content.splitlines(), delimiter=";")
        tickets = list(reader)
    except:
        try:
            reader = csv.DictReader(content.splitlines(), delimiter=",")
            tickets = list(reader)
        except Exception as e:
            print(f"  ❌ Ошибка парсинга: {e}")
            return []
    
    print(f"  ✅ Обработано заявок: {len(tickets)}")
    return tickets

def generate_html(tickets):
    """Генерация HTML-страницы"""
    print("\n  📄 Генерация HTML...")
    
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Заявки help.krista.ru</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Segoe UI', sans-serif; background: #f0f4f8; padding: 30px; }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        .header {{
            background: linear-gradient(135deg, #2b6cb0, #2c5282);
            color: white;
            padding: 30px;
            border-radius: 12px;
            margin-bottom: 30px;
        }}
        .header h1 {{ font-size: 28px; }}
        .stats {{ display: flex; gap: 20px; margin-top: 10px; flex-wrap: wrap; }}
        .stats span {{ background: rgba(255,255,255,0.15); padding: 6px 16px; border-radius: 20px; }}
        table {{ width: 100%; border-collapse: collapse; background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }}
        th {{ background: #edf2f7; padding: 14px; text-align: left; font-weight: 600; }}
        td {{ padding: 12px 14px; border-bottom: 1px solid #e2e8f0; }}
        tr:hover {{ background: #f7fafc; }}
        .footer {{ text-align: center; margin-top: 30px; color: #a0aec0; }}
        @media (max-width: 600px) {{ body {{ padding: 15px; }} th, td {{ padding: 8px 10px; font-size: 12px; }} }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📋 Заявки help.krista.ru</h1>
            <div class="stats">
                <span>📦 Всего: {len(tickets)}</span>
                <span>🔄 Обновлено: {datetime.now().strftime('%d.%m.%Y %H:%M')}</span>
            </div>
        </div>
        <table>
            <thead><tr>
"""
    
    if tickets:
        for key in tickets[0].keys():
            html += f"<th>{key}</th>"
    
    html += "</tr></thead><tbody>"
    
    for t in tickets:
        html += "<tr>"
        for value in t.values():
            html += f"<td>{value}</td>"
        html += "</tr>"
    
    html += """
            </tbody>
        </table>
        <div class="footer">help.krista.ru • Заявки</div>
    </div>
</body>
</html>
    """
    
    path = os.path.join(DOWNLOAD_DIR, "tickets.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    
    return path

if __name__ == "__main__":
    login_and_download()