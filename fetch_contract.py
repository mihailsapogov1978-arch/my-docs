# fetch_contract.py
import requests
from bs4 import BeautifulSoup
import sys
import re
import os

def fetch_contract_details(reestr_number):
    """Получает детали конкретного контракта с zakupki.gov.ru"""
    url = f"https://zakupki.gov.ru/epz/contract/contractCard/common-info.html?reestrNumber={reestr_number}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        def find_value(label_text):
            label = soup.find(string=re.compile(label_text))
            if label:
                parent = label.parent
                value_elem = parent.find_next(['span', 'div'], class_=re.compile(r'cardMainInfo__content|section__info'))
                if value_elem:
                    return value_elem.get_text(strip=True)
            return "Не указано"

        data = {
            "reestr_number": reestr_number,
            "status": find_value(r"Статус контракта"),
            "contract_date": find_value(r"Дата заключения контракта"),
            "contract_number": find_value(r"Номер контракта"),
            "subject": find_value(r"Предмет контракта"),
            "price": find_value(r"Цена контракта"),
            "start_date": find_value(r"Дата начала исполнения контракта"),
            "end_date": find_value(r"Дата окончания исполнения контракта"),
            "stages_count": find_value(r"Количество этапов исполнения контракта"),
            "url": url
        }
        
        # Улучшаем даты: если "не указана", пытаемся найти в другом месте
        if data["start_date"] == "Не указано":
            # Ищем в блоке "Сроки исполнения"
            period_block = soup.find(string=re.compile(r"Сроки исполнения"))
            if period_block:
                next_span = period_block.find_next('span', class_='cardMainInfo__content')
                if next_span:
                    text = next_span.get_text(strip=True)
                    # Пример: "с 14.01.2026 по 28.07.2026"
                    dates = re.findall(r'\d{2}\.\d{2}\.\d{4}', text)
                    if len(dates) >= 2:
                        data["start_date"] = dates[0]
                        data["end_date"] = dates[1]
                    elif len(dates) == 1:
                        data["start_date"] = dates[0]

        return data
        
    except Exception as e:
        print(f"❌ Ошибка при получении контракта {reestr_number}: {e}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Использование: python fetch_contract.py <реестровый_номер> [год]", file=sys.stderr)
        sys.exit(1)
        
    reestr = sys.argv[1]
    year = sys.argv[2] if len(sys.argv) > 2 else "2026"
    
    data = fetch_contract_details(reestr)
    if not data:
        return
    
    # Формируем путь к файлу
    output_dir = f"docs/Meropriyatia/{year}"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "tehn-podderzhka-2026.md")
    
    # Генерируем Markdown
    content = f"""---
title: "{data['subject'][:60]}..."
reestr_number: {data['reestr_number']}
year: {year}
status: "{data['status']}"
tags: [техподдержка, zakupki.gov.ru]
---

# {data['subject']}

## Основная информация

- **Реестровый номер**: {data['reestr_number']}
- **Статус**: {data['status']}
- **Дата заключения контракта**: {data['contract_date']}
- **Номер контракта**: {data['contract_number']}
- **Предмет контракта**: {data['subject']}
- **Цена контракта**: {data['price']}
- **Дата начала исполнения**: {data['start_date']}
- **Дата окончания исполнения**: {data['end_date']}

[Полный контракт на zakupki.gov.ru]({data['url']})

## Требования к технической поддержке

- Консультационная поддержка: 8:30–17:30 (пн–пт, МСК+2)
- Обновления системы: до вступления в силу изменений в законодательстве РФ
- Резервное копирование: ежедневно + ежемесячно
- Удалённое подключение: через защищённую сеть ViPNet

## Поддерживаемые интеграции

- ФНС, СФР, Росстат
- ЕИС, ЕСИА
- ГИС «Региональный электронный бюджет ЯНАО»
- ГИС «Кадровый учёт»

## План мероприятий

Таблица «КАЛЕНДАРНЫЙ ПЛАН» будет добавлена позже.

## Связанные доработки

- [Первое подключение к ГИС «Смета ЯНАО»](../Pervoe_podkluchenie/index.md)
- [Настройка прав на документооборот](../Nastroyka-prav-Interfeys-Dokumentooborot/index.md)
"""
    
    # Записываем файл
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"✅ Файл сохранён: {output_path}", file=sys.stderr)

if __name__ == "__main__":
    main()