#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Парсит PI2027.xlsx (все годы на одном листе)
Группирует по годам и генерирует один Markdown файл с разделами
"""

import os
import re
import warnings
from datetime import datetime
from openpyxl import load_workbook

warnings.filterwarnings("ignore", message="Workbook contains no default style")

EXCEL_FILE = 'docs/plans/PI2027.xlsx'
OUTPUT_MD = 'docs/plans/plans.md'

RKS_LINKS = {
    2027: 'https://rks.yanao.ru/application/?format=storeLink&storeId=bbBfdai',
    2026: 'https://rks.yanao.ru/application/?format=storeLink&storeId=YOUR_2026_STORE_ID',
    2025: 'https://rks.yanao.ru/application/?format=storeLink&storeId=YOUR_2025_STORE_ID',
}

CURRENT_YEAR = 2026


def parse_excel(filepath):
    """Читает Excel и возвращает список записей"""
    if not os.path.exists(filepath):
        print(f'❌ Файл не найден: {filepath}')
        return None
    
    wb = load_workbook(filepath, data_only=True)
    ws = wb.worksheets[0]
    
    records = []
    
    for row in range(2, ws.max_row + 1):
        status = ws.cell(row=row, column=1).value
        event_num = ws.cell(row=row, column=2).value
        customer = ws.cell(row=row, column=4).value
        
        if not event_num:
            continue
        
        if customer != 'ГКУ ЯНАО "ЦБ ОГВ ЯНАО"':
            continue
        
        year_match = re.match(r'^(\d{4})\.', str(event_num).strip())
        if not year_match:
            continue
        year = int(year_match.group(1))
            
        records.append({
            'year': year,
            'status': status or '—',
            'event_num': str(event_num).strip(),
            'name': ws.cell(row=row, column=5).value or '—',
            'amount': ws.cell(row=row, column=6).value,
        })
    
    wb.close()
    return records


def fmt_amount(v):
    """Форматирует сумму"""
    if v is None or v == '':
        return '—'
    try:
        return f'{float(v):,.0f}'.replace(',', ' ')
    except (ValueError, TypeError):
        return str(v)


def build_table_html(records, year):
    """Генерирует HTML-таблицу для конкретного года"""
    
    total_amount = 0
    for r in records:
        try:
            total_amount += float(r['amount']) if r['amount'] and str(r['amount']).replace('.','').isdigit() else 0
        except:
            pass
    
    rows_html = ''
    for i, r in enumerate(records, start=1):
        amount = fmt_amount(r['amount'])
        name = r['name'].replace('\n', '<br>')
        status_badge = '✅ Согласовано' if 'Согласовано' in str(r['status']) else '⚠️ ' + str(r['status'])
        
        rows_html += '<tr>'
        rows_html += '<td style="width: 40px; text-align: center; vertical-align: top;">' + str(i) + '</td>'
        rows_html += '<td style="width: 120px; vertical-align: top; white-space: nowrap;">' + status_badge + '</td>'
        rows_html += '<td style="vertical-align: top;">' + name + '</td>'
        rows_html += '<td style="width: 150px; text-align: right; white-space: nowrap; vertical-align: top;">' + amount + ' ₽</td>'
        rows_html += '</tr>'

    rks_link = RKS_LINKS.get(year, '#')
    
    if year > CURRENT_YEAR:
        link_text = '[Смотреть предварительный ПИ' + str(year) + ' на rks.yanao.ru](' + rks_link + ')' if rks_link != '#' else ''
    else:
        link_text = '[Смотреть ПИ' + str(year) + ' на rks.yanao.ru](' + rks_link + ')' if rks_link != '#' else ''
    
    total_fmt = fmt_amount(total_amount)
    
    html = link_text + '\n\n'
    html += '<div style="overflow-x: auto;">\n'
    html += '<table style="width: 100%; border-collapse: collapse; font-size: 14px;">\n'
    html += '  <thead>\n'
    # ДОБАВЛЕНО font-weight: normal для всех ячеек заголовка
    html += '    <tr style="background-color: #f5f7fa; color: black">\n'
    html += '      <th style="width: 40px; text-align: center; padding: 10px; font-weight: normal;">№</th>\n'
    html += '      <th style="width: 120px; text-align: left; padding: 10px; font-weight: normal;">Согласовано</th>\n'
    html += '      <th style="text-align: left; padding: 10px; font-weight: normal;">Наименование мероприятия</th>\n'
    html += '      <th style="width: 150px; text-align: right; padding: 10px; font-weight: normal;">Объем расходов</th>\n'
    html += '    </tr>\n'
    html += '  </thead>\n'
    html += '  <tbody>\n'
    html += rows_html
    html += '    <tr style="background-color: #e8f4f8; font-size: 16px;">\n'
    html += '      <td colspan="3" style="text-align: right; padding: 10px;">ИТОГО:</td>\n'
    html += '      <td style="text-align: right; padding: 10px;">' + total_fmt + ' ₽</td>\n'
    html += '    </tr>\n'
    html += '  </tbody>\n'
    html += '</table>\n'
    html += '</div>\n'
    
    return html


def main():
    print('=' * 60)
    print('Генерация планов информатизации (все годы)')
    print('=' * 60)
    
    print('\n📖 Чтение ' + EXCEL_FILE + '...')
    records = parse_excel(EXCEL_FILE)
    
    if records is None:
        return
    
    print('📊 Всего найдено записей (ГКУ ЯНАО "ЦБ ОГВ ЯНАО"): ' + str(len(records)))
    
    if len(records) == 0:
        print('⚠️  Данные не найдены.')
        return
    
    plans_by_year = {}
    for r in records:
        year = r['year']
        if year not in plans_by_year:
            plans_by_year[year] = []
        plans_by_year[year].append(r)
    
    print('📅 Найдено годов: ' + str(sorted(plans_by_year.keys(), reverse=True)))
    
    md_content = '# План закупок по мероприятиям информатизации\n\n'
    
    for year in sorted(plans_by_year.keys(), reverse=True):
        year_records = plans_by_year[year]
        print('\n Генерация раздела для ' + str(year) + ' года (' + str(len(year_records)) + ' записей)...')
        
        md_content += '## ' + str(year) + ' год\n\n'
        md_content += build_table_html(year_records, year)
        md_content += '\n---\n\n'
    
    os.makedirs(os.path.dirname(OUTPUT_MD), exist_ok=True)
    with open(OUTPUT_MD, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    print('\n✅ Готово: ' + OUTPUT_MD)
    print('📑 Сгенерировано разделов: ' + str(len(plans_by_year)))


if __name__ == '__main__':
    main()