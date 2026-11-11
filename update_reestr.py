import requests
from datetime import datetime
import sys
from collections import defaultdict
import html
import re

# 1. Настройки
BASE_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3OTQ0NjIzNTQsImR0YWJsZV91dWlkIjoiY2E0MTYyYWEtMzM0ZS00Y2Y4LWE1YTMtOGZiMDYwYTA5NWE0IiwicGVybWlzc2lvbiI6InJ3Iiwib3JnX2lkIjotMSwib3duZXJfaWQiOiI3YjU3NjEzOTg3N2U0MTYxODdhZGY2ZDcwYTkyNGQ1ZEBhdXRoLmxvY2FsIiwiYXBwX25hbWUiOiJteV90b2tlbiIsInVzZXJuYW1lIjoiIiwiaWRfaW5fb3JnIjoiIiwidXNlcl9kZXBhcnRtZW50X2lkc19tYXAiOnsiY3VycmVudF91c2VyX2RlcGFydG1lbnRfaWRzIjpbXSwiY3VycmVudF91c2VyX2RlcGFydG1lbnRfYW5kX3N1Yl9pZHMiOltdfX0.MAG8ri1e0XRPsqEf_W1kVvCUCC1YuJAVCxXVtcoIrKM"
DTABLE_UUID = "ca4162aa-334e-4cf8-a5a3-8fb060a095a4"
TABLE_NAME = "Реестр оферт"
OUTPUT_FILE = "docs/reestr_offert.md"

# Словарь соответствия ID территорий и их названий
TERRITORY_MAP = {
    "645429": "Лабытнанги Приуральский район",
    "492986": "Ноябрьск",
    "892603": "Муравленко",
    "208431": "Губкинский",
    "823564": "Новый Уренгой",
    "132955": "Красноселькупский район",
    "471772": "Тазовский район",
    "650319": "Шурышкарский район",
    "329011": "Пуровский район",
    "870588": "Ямальский район",
    "272923": "Надымский",
    "147110": "Салехард",
    "310017": "ЯНАО (ГКУ, ГУ, ГБУ, ГАУ)"
}

url = f"https://ditable.yanao.ru/api-gateway/api/v2/dtables/{DTABLE_UUID}/rows/"
params = {"table_name": TABLE_NAME}
headers = {
    "accept": "application/json",
    "authorization": f"Bearer {BASE_TOKEN}"
}

print("Получение данных из SeaTable...")

try:
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print(f"Ошибка API (Код {response.status_code}): {response.text}")
        sys.exit(1)
    data = response.json()
except Exception as e:
    print(f"Ошибка при выполнении запроса: {e}")
    sys.exit(1)

print("Генерация Markdown файла...")

def get_text(val):
    if isinstance(val, dict):
        text = str(val.get("name", "-"))
    else:
        text = str(val) if val else "-"
    if text == "None" or text == "": return "-"
    return html.escape(text.replace("\n", " "))

def format_date(date_str):
    if not date_str or date_str == "-":
        return "-"
    clean_date = str(date_str)[:10]
    if re.match(r'^\d{4}-\d{2}-\d{2}$', clean_date):
        year, month, day = clean_date.split('-')
        return f"{day}.{month}.{year}"
    return date_str

def make_anchor(text):
    anchor = re.sub(r'[^a-zA-Z0-9а-яА-ЯёЁ]', '-', text.lower())
    anchor = re.sub(r'-+', '-', anchor).strip('-')
    return f"terr-{anchor}"

# 3. Группируем данные
grouped_data = defaultdict(lambda: defaultdict(list))

# Ключевые слова для определения "Органов власти" (только окружные)
GOV_KEYWORDS = ["Департамент", "Служба", "Управление", "Аппарат", "Государственно-правовой"]

for row in data.get("rows", []):
    terr_raw = row.get("FpUL")
    
    if isinstance(terr_raw, dict):
        terr_id = str(terr_raw.get("id", ""))
        terr = TERRITORY_MAP.get(terr_id, terr_raw.get("name", "Без территории"))
    else:
        terr_str = str(terr_raw) if terr_raw else ""
        terr = TERRITORY_MAP.get(terr_str, terr_str if terr_str else "Без территории")

    if not terr or terr == "-": terr = "Без территории"

    org_raw = get_text(row.get("4Fov"))
    if org_raw == "-" or org_raw == "None" or org_raw.strip() == "":
        org = "Организация не указана (нет БУ)"
    else:
        org = org_raw

    name_raw = get_text(row.get("0000"))
    
    # УЛУЧШЕННАЯ ЛОГИКА ВЫНОСА В "ОРГАНЫ ВЛАСТИ"
    # 1. Название должно начинаться с ключевого слова
    # 2. В названии должно быть "ЯНАО" или "Ямало-Ненецкого автономного округа"
    # 3. В названии НЕ должно быть слова "Администрации" (чтобы не выносить муниципалитеты)
    is_gov = False
    if any(name_raw.startswith(kw) for kw in GOV_KEYWORDS):
        if "ЯНАО" in name_raw or "Ямало-Ненецкого автономного округа" in name_raw:
            if "Администрации" not in name_raw:
                is_gov = True

    if is_gov:
        terr = "Органы власти"

    app_num_raw = get_text(row.get("yqcp"))
    
    record = {
        "name": name_raw,       
        "inn": get_text(row.get("9QbV")),        
        "app_num": app_num_raw,
        "app_date": format_date(row.get("wmZY")),  
        "app_link_raw": row.get("3k49")
    }
    
    link_val = record["app_link_raw"]
    if link_val and isinstance(link_val, str) and link_val.startswith("http"):
        record["app_link"] = f'<a href="{html.escape(link_val)}" target="_blank">Ссылка</a>'
    else:
        record["app_link"] = "-"
    
    grouped_data[terr][org].append(record)

# 4. Кастомная сортировка (ЯНАО в конец, Органы власти в самый конец)
def sort_territories(terr):
    if terr == "ЯНАО (ГКУ, ГУ, ГБУ, ГАУ)":
        return "ЯЯЯ_1"
    if terr == "Органы власти":
        return "ЯЯЯ_2"
    return terr

# 5. CSS-стили
CSS_STYLES = """
<style>
:root {
    --emp-border: #e2e8f0;
    --emp-bg-hover: #f7fafc;
    --emp-text: #2d3748;
    --emp-accent: #2b6cb0;
    --emp-accent-border: #bee3f8;
}
* { scrollbar-width: none; }
*::-webkit-scrollbar { display: none; }

/* 1. В заголовках на самой странице цифру СКРЫВАЕМ полностью */
.md-content h2 .toc-badge {
    display: none !important;
}

/* 2. В правом меню (TOC) цифру ПОКАЗЫВАЕМ и КРАСИМ в красный */
.md-nav--secondary .md-nav__link .toc-badge {
    display: inline !important;
    color: #e53e3e !important;
    font-weight: 700 !important;
    margin-left: 6px;
}

.dept-list {
    margin: 16px 0;
    border: 1px solid var(--emp-border);
    border-radius: 10px;
    overflow: hidden;
    background: #fff;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}
.dept-item { border-bottom: 1px solid var(--emp-border); }
.dept-item:last-child { border-bottom: none; }
.dept-row {
    display: grid;
    grid-template-columns: minmax(0, 1fr) 20px;
    align-items: center;
    column-gap: 12px;
    padding: 14px 18px;
    font-size: 14px;
    line-height: 1.4;
    cursor: pointer;
    transition: background 0.15s;
    margin: 0;
}
.dept-row:hover { background: var(--emp-bg-hover); }

.dept-name { font-weight: 600; color: var(--emp-text); min-width: 0; display: flex; flex-direction: column; gap: 4px; }
.org-label { font-size: 11px; color: #718096; text-transform: uppercase; letter-spacing: 0.05em; font-weight: 700; }
.org-text { color: var(--emp-accent); }
.org-count { font-size: 12px; color: #a0aec0; font-weight: normal; margin-left: 8px; }

.no-requests { color: #e53e3e; font-weight: 700; margin-left: 6px; }

.dept-toggle {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    color: var(--emp-accent);
    font-size: 18px;
    font-weight: 700;
    transition: transform 0.18s;
    user-select: none;
}
.dept-checkbox { display: none; }
.dept-checkbox:checked ~ .dept-row .dept-toggle { transform: rotate(90deg); }
.dept-checkbox:checked ~ .dept-details { display: block; }
.dept-details { display: none; background: #fafbfc; padding: 0; overflow-x: auto; }

.calls-table {
    width: 100%;
    border-collapse: collapse;
    background: #fff;
    font-size: 13.5px;
    table-layout: fixed;
    min-width: 700px;
}
.calls-table thead th {
    background: #f0f7ff;
    color: var(--emp-accent);
    font-weight: 700;
    font-size: 11px;
    text-transform: uppercase;
    padding: 8px 10px;
    border-bottom: 1px solid var(--emp-accent-border);
    border-right: 1px solid var(--emp-accent-border);
    text-align: left;
    vertical-align: middle;
    white-space: normal;
    word-wrap: break-word;
}
.calls-table thead th:last-child { border-right: none; }
.calls-table tbody td {
    padding: 8px 10px;
    border-bottom: 1px solid var(--emp-border);
    border-right: 1px solid var(--emp-border);
    color: var(--emp-text);
    vertical-align: top;
    word-wrap: break-word;
}
.calls-table tbody td:last-child { border-right: none; }
.calls-table tbody tr:last-child td { border-bottom: none; }
.calls-table tbody tr:hover { background-color: #f9fbfd; }
</style>
"""

# 6. Записываем в файл
try:
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(CSS_STYLES)
        f.write("\n\n# Реестр оферт\n\n")
        f.write(f"> Данные актуальны на {datetime.now().strftime('%d.%m.%Y %H:%M')}\n\n")
        
        sorted_territories = sorted(grouped_data.keys(), key=sort_territories)
        
        for terr_name in sorted_territories:
            terr_no_apps = 0
            for org_rows in grouped_data[terr_name].values():
                terr_no_apps += sum(1 for r in org_rows if r["app_num"] == "-" or r["app_num"].lower() == "нет" or not r["app_num"])
            
            toc_suffix = ""
            if terr_no_apps > 0:
                toc_suffix = f' <span class="toc-badge">{terr_no_apps}</span>'
            
            f.write(f"## {terr_name}{toc_suffix}\n\n")
            
            for org_name, rows in grouped_data[terr_name].items():
                no_apps_count = sum(1 for r in rows if r["app_num"] == "-" or r["app_num"].lower() == "нет" or not r["app_num"])
                
                stats_html = f'<span class="org-count">(учреждений: {len(rows)}'
                if no_apps_count > 0:
                    stats_html += f' <span class="no-requests">| нет заявок: {no_apps_count}</span>'
                stats_html += ')</span>'

                f.write('<div class="dept-list">\n')
                chk_id = f"dept-{make_anchor(terr_name)}-{make_anchor(org_name)}"
                
                f.write(f'  <div class="dept-item">\n')
                f.write(f'    <input type="checkbox" id="{chk_id}" class="dept-checkbox">\n')
                f.write(f'    <label for="{chk_id}" class="dept-row">\n')
                
                f.write(f'      <span class="dept-name">\n')
                f.write(f'        <span class="org-label">Организация, ведущая БУ</span>\n')
                f.write(f'        <span class="org-text">{org_name} {stats_html}</span>\n')
                f.write(f'      </span>\n')
                
                f.write(f'      <span class="dept-toggle">›</span>\n')
                f.write(f'    </label>\n')
                f.write(f'    <div class="dept-details">\n')
                
                f.write('      <table class="calls-table">\n')
                f.write('        <colgroup>\n')
                f.write('          <col style="width: 40%;">\n')
                f.write('          <col style="width: 15%;">\n')
                f.write('          <col style="width: 20%;">\n')
                f.write('          <col style="width: 12%;">\n')
                f.write('          <col style="width: 13%;">\n')
                f.write('        </colgroup>\n')
                
                f.write('        <thead>\n')
                f.write('          <tr>\n')
                f.write('            <th>Наименование учреждения</th>\n')
                f.write('            <th>ИНН</th>\n')
                f.write('            <th>№ заявки</th>\n')
                f.write('            <th>Дата заявки</th>\n')
                f.write('            <th>Ссылка на заявку</th>\n')
                f.write('          </tr>\n')
                f.write('        </thead>\n')
                f.write('        <tbody>\n')
                
                for r in rows:
                    f.write('          <tr>\n')
                    f.write(f'            <td>{r["name"]}</td>\n')
                    f.write(f'            <td>{r["inn"]}</td>\n')
                    f.write(f'            <td>{r["app_num"]}</td>\n')
                    f.write(f'            <td>{r["app_date"]}</td>\n')
                    f.write(f'            <td>{r["app_link"]}</td>\n')
                    f.write('          </tr>\n')
                
                f.write('        </tbody>\n')
                f.write('      </table>\n')
                f.write('    </div>\n')
                f.write('  </div>\n')
                f.write('</div>\n\n')
            
    print(f"Успех! Файл '{OUTPUT_FILE}' успешно создан. Территорий: {len(grouped_data)}.")
    
except Exception as e:
    print(f"Ошибка при записи файла: {e}")