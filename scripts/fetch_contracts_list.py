# fetch_contracts_list.py
import re
import requests
import json
import time
import os

def get_contracts_by_inn(inn, years):
    """Получает список контрактов по ИНН через JSON-API"""
    contracts = []
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    for year in years:
        print(f"🔍 Поиск контрактов за {year} год...")
        
        url = "https://zakupki.gov.ru/epz/order/extendedsearch/getItems.html"
        params = {
            "searchString": inn,
            "orderYearFrom": year,
            "orderYearTo": year,
            "recordsPerPage": "_100",
            "sortDirection": "false",
            "sortBy": "UPDATE_DATE"
        }
        
        try:
            response = requests.get(url, params=params, headers=headers, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            if "data" in data and "items" in data["data"]:
                items = data["data"]["items"]
                print(f"  → Найдено {len(items)} контрактов")
                
                for item in items:
                    # Извлекаем реестровый номер из URL
                    href = item.get("href", "")
                    match = re.search(r'reestrNumber=(\d+)', href)
                    if match:
                        reestr_number = match.group(1)
                        contracts.append({
                            "reestr_number": reestr_number,
                            "year": year,
                            "url": f"https://zakupki.gov.ru{href}"
                        })
                        print(f"    → {reestr_number}")
            
            else:
                print("  → Нет данных")
                
            time.sleep(1)  # Пауза между запросами
            
        except Exception as e:
            print(f"❌ Ошибка при получении данных за {year}: {e}")
    
    return contracts

def main():
    INN = "8901038364"
    YEARS = list(range(2019, 2027))
    
    contracts = get_contracts_by_inn(INN, YEARS)
    
    # Сохраняем список в JSON
    with open("contracts_list.json", "w", encoding="utf-8") as f:
        json.dump(contracts, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Найдено {len(contracts)} контрактов")
    print("📋 Список сохранён в contracts_list.json")

if __name__ == "__main__":
    main()