# fetch_contract.py
import requests
from bs4 import BeautifulSoup
import sys

def fetch_contract(reestr_number):
    # ПРАВИЛЬНЫЙ URL
    url = f"https://zakupki.gov.ru/epz/contract/contractCard/document-info.html?reestrNumber={reestr_number}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    print(f"Запрашиваем данные для реестрового номера: {reestr_number}", file=sys.stderr)
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    try:
        # Название контракта
        title_elem = soup.select_one('h1.title')
        title = title_elem.get_text(strip=True) if title_elem else "Не указано"
        
        # Статус контракта
        status_row = soup.find('div', class_='cardMainInfo__section', string="Статус контракта")
        if status_row:
            status = status_row.find_next('span').get_text(strip=True)
        else:
            status = "Не найден"
        
        # Цена контракта
        price_row = soup.find('div', class_='cardMainInfo__section', string="Цена контракта")
        if price_row:
            price = price_row.find_next('span').get_text(strip=True)
        else:
            price = "Не указана"
            
        return {
            "title": title,
            "status": status,
            "price": price,
            "url": url
        }
    except Exception as e:
        print(f"Ошибка при парсинге: {e}", file=sys.stderr)
        return {
            "title": "Ошибка загрузки",
            "status": "Неизвестно",
            "price": "Неизвестно",
            "url": url
        }

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python fetch_contract.py <реестровый_номер>", file=sys.stderr)
        sys.exit(1)
        
    reestr = sys.argv[1]
    data = fetch_contract(reestr)
    
    # Формируем Markdown
    print(f"""---
title: "{data['title']}"
reestr_number: {reestr}
status: "{data['status']}"
price: "{data['price']}"
---

# {data['title']}

- **Статус**: {data['status']}
- **Цена**: {data['price']}
- **Реестровый номер**: {reestr}

[Полный контракт на zakupki.gov.ru]({data['url']})
""")