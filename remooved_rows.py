# pip install openpyxl
import openpyxl
import re

ETALON_FILE = "Перечень учреждений ИО_ГУ_ОМСУ_МУ на 24.09.2026.xlsx"
ESKU_FILE = "ОбменЕСКУ с 31.10 по 06.11.2026.xlsx"
OUTPUT_FILE = "ОбменЕСКУ_final_732.xlsx"

# 1. Читаем эталон (все 732 записи)
print("Чтение эталона...")
wb_etalon = openpyxl.load_workbook(ETALON_FILE, read_only=True, data_only=True)
etalon_list = []  # Список кортежей (ИНН, Название)
for sheet_name in wb_etalon.sheetnames:
    ws = wb_etalon[sheet_name]
    for row in ws.iter_rows(values_only=True):
        inn_val = None
        name_val = None
        for cell in row:
            if not cell: continue
            cell_str = str(cell).strip()
            if re.fullmatch(r"\d{10}", cell_str):
                inn_val = cell_str
            elif len(cell_str) > 10 and "наименование" not in cell_str.lower():
                name_val = cell_str
        if inn_val and name_val:
            etalon_list.append((inn_val, name_val))
wb_etalon.close()
print(f"Всего организаций в эталоне: {len(etalon_list)}")

# 2. Открываем файл ЕСКУ (с сохранением форматирования)
print("Открытие файла ЕСКУ...")
wb_esku = openpyxl.load_workbook(ESKU_FILE)
ws_esku = wb_esku["Обмен ЕСКУ"]

# Собираем индексы строк из ЕСКУ (начиная с 3-й строки, так как шапка занимает 1-2 строки)
# Внимание: в вашем файле на скриншоте шапка занимает 3 строки! 
# Если данные начинаются с 4-й строки, измените 3 на 4 в range()
START_ROW = 3 

esku_rows = {}
for r_idx in range(START_ROW, ws_esku.max_row + 1):
    inn = str(ws_esku.cell(row=r_idx, column=2).value or "").strip()
    name = str(ws_esku.cell(row=r_idx, column=3).value or "").strip()
    if inn:
        esku_rows[inn] = {
            "row_idx": r_idx,
            "name": name,
            "data": [ws_esku.cell(row=r_idx, column=c).value for c in range(4, ws_esku.max_column + 1)]
        }

print(f"Строк с ИНН в ЕСКУ: {len(esku_rows)}")

# 3. Формируем итоговый список
# Мы должны оставить все строки, которые есть в эталоне. 
# Плюс удалить дубли в ЕСКУ (если есть).
rows_to_keep = []
matched_inns = set()

for inn, etalon_name in etalon_list:
    if inn in esku_rows:
        # Организация есть в ЕСКУ
        esku_info = esku_rows[inn]
        rows_to_keep.append({
            "inn": inn,
            "name": etalon_name, # Берем название из эталона для порядка
            "data": esku_info["data"],
            "original_row_idx": esku_info["row_idx"] # Запоминаем, откуда взяли
        })
        matched_inns.add(inn)
    else:
        # Организации нет в ЕСКУ (опечатка или не выгрузилась)
        rows_to_keep.append({
            "inn": inn,
            "name": etalon_name,
            "data": None,
            "original_row_idx": None
        })

# Находим строки в ЕСКУ, которых нет в эталоне (мусор)
rows_to_delete = []
for r_idx in range(START_ROW, ws_esku.max_row + 1):
    inn = str(ws_esku.cell(row=r_idx, column=2).value or "").strip()
    name = str(ws_esku.cell(row=r_idx, column=3).value or "").strip()
    
    # Если ИНН нет в эталоне, или это пустая/техническая строка — на удаление
    if not name or not inn:
        rows_to_delete.append(r_idx)
    elif inn not in matched_inns:
        # Если ИНН не совпал ни с одной эталонной организацией
        rows_to_delete.append(r_idx)
    elif r_idx not in [r["original_row_idx"] for r in rows_to_keep if r["original_row_idx"]]:
        # Если это дубль (ИНН совпал, но мы уже взяли строку для этой организации)
        rows_to_delete.append(r_idx)

print(f"Строк мусора к удалению: {len(rows_to_delete)}")

# 4. Удаляем мусорные строки (снизу вверх)
for r_idx in reversed(rows_to_delete):
    ws_esku.delete_rows(r_idx)

# 5. Обновляем данные и нумерацию
# Нам нужно пройтись по оставшимся строкам и присвоить им правильные номера
# Но так как мы удалили лишние, у нас остались только те строки, которые есть в эталоне
# Просто перенумеруем их по порядку

# ВАЖНО: Некоторые организации из эталона не были в ЕСКУ. Их нужно добавить в конец.
# Для этого найдем последнюю заполненную строку
current_row = ws_esku.max_row
# Если последняя строка пустая, начинаем с неё, иначе +1
if ws_esku.cell(row=current_row, column=2).value:
    current_row += 1

for item in rows_to_keep:
    if item["original_row_idx"] is None:
        # Добавляем новую строку (копируем стиль с предыдущей)
        ws_esku.cell(row=current_row, column=2).value = item["inn"]
        ws_esku.cell(row=current_row, column=3).value = item["name"]
        # Копируем стиль ячеек (чтобы границы и шрифт были как у всех)
        for c in range(1, ws_esku.max_column + 1):
            ws_esku.cell(row=current_row, column=c)._style = ws_esku.cell(row=current_row-1, column=c)._style
        current_row += 1

# 6. Перенумерация (с 1)
print("Обновление нумерации...")
counter = 1
for r_idx in range(START_ROW, ws_esku.max_row + 1):
    if ws_esku.cell(row=r_idx, column=2).value:
        ws_esku.cell(row=r_idx, column=1).value = counter
        counter += 1

print(f"Итоговое количество строк: {counter - 1}")

# 7. Сохранение
wb_esku.save(OUTPUT_FILE)
print(f"Готово! Файл сохранен как: {OUTPUT_FILE}")