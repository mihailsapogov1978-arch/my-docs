# fetch_contract.py
import requests
from bs4 import BeautifulSoup
import sys
import re
import os

def fetch_contract(reestr_number):
    url = f"https://zakupki.gov.ru/epz/contract/contractCard/common-info.html?reestrNumber={reestr_number}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    print(f"Запрашиваем данные для реестрового номера: {reestr_number}", file=sys.stderr)
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    try:
        # Вспомогательная функция поиска по метке
        def find_value(label_text):
            label = soup.find(string=re.compile(label_text))
            if label:
                parent = label.parent
                # Ищем следующий элемент с данными
                value_elem = parent.find_next(['span', 'div'], class_=re.compile(r'cardMainInfo__content|section__info'))
                if value_elem:
                    return value_elem.get_text(strip=True)
            return "Не указано"

        # Извлечение данных
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

        # Извлечение этапов
        stages = []
        stages_section = soup.find(string=re.compile(r"Этапы исполнения контракта"))
        if stages_section:
            stage_rows = stages_section.find_all_next('tr')[1:]  # Пропускаем заголовок
            for row in stage_rows[:int(data["stages_count"]) if data["stages_count"].isdigit() else 0]:
                cols = row.find_all('td')
                if len(cols) >= 4:
                    stages.append({
                        "name": cols[0].get_text(strip=True),
                        "start": cols[1].get_text(strip=True),
                        "end": cols[2].get_text(strip=True),
                        "price": cols[3].get_text(strip=True)
                    })

        data["stages"] = stages
        return data
        
    except Exception as e:
        print(f"Ошибка при парсинге: {e}", file=sys.stderr)
        return {
            "reestr_number": reestr_number,
            "status": "Ошибка",
            "contract_date": "Ошибка",
            "contract_number": "Ошибка",
            "subject": "Ошибка",
            "price": "Ошибка",
            "start_date": "Ошибка",
            "end_date": "Ошибка",
            "stages_count": "Ошибка",
            "stages": [],
            "url": url
        }

def main():
    if len(sys.argv) < 2:
        print("Использование: python fetch_contract.py <реестровый_номер> [год]", file=sys.stderr)
        sys.exit(1)
        
    reestr = sys.argv[1]
    year = sys.argv[2] if len(sys.argv) > 2 else "2026"
    
    data = fetch_contract(reestr)
    
    # Формируем путь к файлу
    output_dir = f"docs/Meropriyatia/{year}"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"tehn-podderzhka-{year}.md")
    
    # Формируем таблицу этапов
    stages_table = ""
    if data["stages"]:
        stages_table = "\n## Этапы исполнения контракта\n\n"
        stages_table += "| Наименование этапа | Начало | Окончание | Цена этапа |\n"
        stages_table += "|-------------------|--------|-----------|------------|\n"
        for stage in data["stages"]:
            stages_table += f"| {stage['name']} | {stage['start']} | {stage['end']} | {stage['price']} |\n"
    
    # Записываем файл в UTF-8
    with open(output_path, "w", encoding="utf-8") as f:
        content = f"""---
title: "Техническая поддержка ГИС «Смета ЯНАО» ({year})"
reestr_number: {data['reestr_number']}
year: {year}
status: "{data['status']}"
tags: [техподдержка, zakupki.gov.ru]
---

# Техническая поддержка ГИС «Смета ЯНАО» ({year})

## Основная информация

- **Реестровый номер**: {data['reestr_number']}
- **Статус**: {data['status']}
- **Дата заключения контракта**: {data['contract_date']}
- **Номер контракта**: {data['contract_number']}
- **Предмет контракта**: {data['subject']}
- **Цена контракта**: {data['price']}
- **Дата начала исполнения**: {data['start_date']}
- **Дата окончания исполнения**: {data['end_date']}
- **Количество этапов**: {data['stages_count']}

[Полный контракт на zakupki.gov.ru]({data['url']})

{stages_table}

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

## Диаграмма процесса

> ⚠️ BPMN-схема находится в разработке.

## Связанные доработки

- [Первое подключение к ГИС «Смета ЯНАО»](../Pervoe_podkluchenie/index.md)
- [Настройка прав на документооборот](../Nastroyka-prav-Interfeys-Dokumentooborot/index.md)
"""
        f.write(content)
    
    print(f"✅ Файл сохранён: {output_path}", file=sys.stderr)

if __name__ == "__main__":
    main()