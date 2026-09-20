import os
import time
import csv
import re
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

# ========== НАСТРОЙКИ ==========
INN = os.getenv("ZAKUPKI_INN", "8901038364")
BASE_URL = "https://zakupki.gov.ru"

# Прямая ссылка на скачивание (все 67 записей)
DOWNLOAD_URL = f"https://zakupki.gov.ru/epz/order/orderCsvSettings/download.html?searchString={INN}&from=1&to=67&placementCsv=true&registryNumberCsv=true&stepOrderPlacementCsv=true&methodOrderPurchaseCsv=true&nameOrderCsv=true&purchaseNumbersCsv=true&numberLotCsv=true&nameLotCsv=true&maxContractPriceCsv=true&currencyCodeCsv=true&maxPriceContractCurrencyCsv=true&currencyCodeContractCurrencyCsv=true&scopeOkdpCsv=true&scopeOkpdCsv=true&scopeOkpd2Csv=true&scopeKtruCsv=true&ea615ItemCsv=true&customerNameCsv=true&organizationOrderPlacementCsv=true&publishDateCsv=true&lastDateChangeCsv=true&startDateRequestCsv=true&endDateRequestCsv=true&ea615DateCsv=true&featureOrderPlacementCsv=true"

DOWNLOAD_DIR = os.path.join(os.getcwd(), "downloads_csv")
os.makedirs(DOWNLOAD_DIR, exist_ok=True)


def escape_html(text):
    """Экранирование HTML-символов для защиты от XSS"""
    import html
    if not text:
        return ''
    return html.escape(str(text))

# ========== НАСТРОЙКА БРАУЗЕРА (Headless) ==========
def setup_driver(headless=True):
    chrome_options = Options()
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--ignore-ssl-errors")
    chrome_options.add_argument("--allow-insecure-localhost")
    
    if headless:
        chrome_options.add_argument("--headless=new")
        print("  🖥️ Браузер в фоновом режиме")
    
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return driver

# ========== СКАЧИВАНИЕ CSV ==========
def download_csv(driver):
    print("\n  Скачивание CSV...")
    cookies = driver.get_cookies()
    cookie_string = '; '.join([f"{c['name']}={c['value']}" for c in cookies])
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/csv,application/vnd.ms-excel,application/octet-stream',
        'Cookie': cookie_string,
        'Referer': 'https://zakupki.gov.ru/',
    }
    
    try:
        response = requests.get(DOWNLOAD_URL, headers=headers, verify=False, timeout=30)
        if response.status_code == 200:
            filename = f"contracts_{INN}.csv"  # ← Перезаписываем один файл
            filepath = os.path.join(DOWNLOAD_DIR, filename)
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print(f"  ✅ CSV скачан: {filename}")
            return filepath
        else:
            print(f"  ❌ Ошибка HTTP {response.status_code}")
            return None
    except Exception as e:
        print(f"  ❌ Ошибка: {e}")
        return None

# ========== ПАРСИНГ CSV ==========
def parse_csv(filepath):
    print("\n[3] Парсинг CSV...")
    
    encodings = ['utf-8-sig', 'utf-8', 'windows-1251', 'cp1251']
    content = None
    for enc in encodings:
        try:
            with open(filepath, 'r', encoding=enc) as f:
                content = f.read()
            print(f"  ✅ Кодировка: {enc}")
            break
        except:
            continue
    
    if content is None:
        print("  ❌ Не удалось прочитать файл")
        return []
    
    contracts = []
    reader = csv.DictReader(content.splitlines(), delimiter=';')
    for row in reader:
        ikz_raw = row.get('Идентификационный код закупки', '')
        ikz_match = re.search(r'(\d+)', ikz_raw)
        ikz = ikz_match.group(1) if ikz_match else ''
        
        price_raw = row.get('Начальная (максимальная) цена контракта', '0')
        try:
            price_float = float(price_raw.replace(',', '').replace(' ', '')) if price_raw else 0
        except:
            price_float = 0
        
        contracts.append({
            'reg_number': row.get('Реестровый номер закупки', '').strip(),
            'method': row.get('Способ определения поставщика (подрядчика, исполнителя), подрядной организации (размещения закупки)', '').strip(),
            'name': row.get('Наименование закупки', '').strip(),
            'ikz': ikz,
            'price': price_raw.strip(),
            'price_float': price_float,
            'publish_date': row.get('Дата размещения', '').strip(),
            'stage': row.get('Этап закупки', '').strip(),
        })
    
    print(f"  ✅ Обработано: {len(contracts)}")
    return contracts

# ========== ГЕНЕРАЦИЯ HTML ==========
def generate_html(contracts):
    print("\n[4] Генерация HTML...")
    
    years = {}
    for c in contracts:
        year = c['publish_date'][:4] if c['publish_date'] else 'Неизвестно'
        years.setdefault(year, []).append(c)
    
    html = f"""<!DOCTYPE html>
<html lang="ru">
<head><meta charset="UTF-8"><title>Контракты ИНН {INN}</title>
<style>
    *{{margin:0;padding:0;box-sizing:border-box}}
    body{{font-family:'Segoe UI',sans-serif;background:#f0f4f8;padding:30px}}
    .container{{max-width:1200px;margin:0 auto}}
    .header{{background:linear-gradient(135deg,#2b6cb0,#2c5282);color:#fff;padding:30px;border-radius:12px;margin-bottom:30px}}
    .header h1{{font-size:28px}}
    .stats{{display:flex;gap:20px;margin-top:10px;flex-wrap:wrap}}
    .stats span{{background:rgba(255,255,255,0.15);padding:6px 16px;border-radius:20px}}
    .year-section{{margin-bottom:30px}}
    .year-title{{font-size:22px;font-weight:700;border-bottom:2px solid #e2e8f0;padding-bottom:10px;margin-bottom:15px;display:flex;justify-content:space-between}}
    .cards{{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:16px}}
    .card{{background:#fff;border-radius:10px;padding:18px;box-shadow:0 2px 8px rgba(0,0,0,0.06);border-left:4px solid #3182ce}}
    .card .name{{font-weight:600;font-size:15px}}
    .card .meta{{font-size:13px;color:#4a5568;margin-top:8px;display:flex;gap:10px;flex-wrap:wrap}}
    .card .price{{font-weight:700;color:#2b6cb0;font-size:17px;margin-top:8px}}
    .card .badge{{display:inline-block;font-size:11px;padding:2px 12px;border-radius:12px;background:#c6f6d5;color:#276749}}
    .footer{{text-align:center;margin-top:30px;color:#a0aec0;font-size:14px}}
</style>
</head>
<body>
<div class="container">
    <div class="header">
        <h1>📋 Контракты по ИНН {INN}</h1>
        <div class="stats">
            <span>📦 Всего: {len(contracts)}</span>
            <span>💰 Сумма: {sum(c['price_float'] for c in contracts):,.2f} ₽</span>
        </div>
    </div>
"""
    
    for year in sorted(years.keys(), reverse=True):
        html += f'<div class="year-section"><div class="year-title">📅 {escape_html(year)} <span>{len(years[year])}</span></div><div class="cards">'
        for c in years[year]:
            stage = c.get('stage', '')
            badge = 'Завершен' if 'завершена' in stage.lower() else 'Отменен' if 'отменено' in stage.lower() else stage[:20] if stage else '—'
            html += f"""
            <div class="card">
                <div class="name">{escape_html(c.get('name', 'Без названия'))}</div>
                <div class="meta"><span>Метод: {escape_html(c.get('method', '—'))}</span><span>Статус: <span class="badge">{escape_html(badge)}</span></span></div>
                <div class="meta"><span>Дата: {escape_html(c.get('publish_date', '—'))}</span><span>ИКЗ: {escape_html(c.get('ikz', '—'))}</span></div>
                <div class="price">{escape_html(c.get('price', '0'))} ₽</div>
            </div>"""
        html += "</div></div>"
    
    html += f'<div class="footer">zakupki.gov.ru • ИНН {INN} • {len(contracts)} контрактов</div></div></body></html>'
    
    path = os.path.join(DOWNLOAD_DIR, "contracts.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  ✅ HTML: {path}")
    return path

# ========== ЗАПУСК ==========
def main():
    print("=" * 60)
    print(f"АВТОМАТИЧЕСКАЯ ВЫГРУЗКА КОНТРАКТОВ ПО ИНН {INN}")
    print("=" * 60)
    
    driver = setup_driver(headless=True)  # ← Браузер в фоне
    
    try:
        print("\n[1] Получение сессии...")
        driver.get(f"{BASE_URL}/epz/order/extendedsearch/results.html?searchString={INN}")
        time.sleep(5)
        print("  ✅ Сессия получена")
        
        csv_path = download_csv(driver)
        if not csv_path:
            return
        
        contracts = parse_csv(csv_path)
        if not contracts:
            return
        
        html_path = generate_html(contracts)
        
        print("\n" + "=" * 60)
        print("✅ ГОТОВО!")
        print(f"📁 CSV: {csv_path}")
        print(f"📄 HTML: {html_path}")
        print(f"📊 Контрактов: {len(contracts)}")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()