
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


# Реестр оферт

> Данные актуальны на 11.11.2026 15:23

## Губкинский

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-губкинский-terr-мку-quot-городской-центр-информационных-технологий-quot-цитадель-quot" class="dept-checkbox">
    <label for="dept-terr-губкинский-terr-мку-quot-городской-центр-информационных-технологий-quot-цитадель-quot" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">МКУ &quot;Городской Центр Информационных Технологий &quot;ЦИТАДЕЛЬ&quot; <span class="org-count">(учреждений: 10)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>МКУ &quot;Городской Центр Информационных Технологий &quot;ЦИТАДЕЛЬ&quot;</td>
            <td>8913009022</td>
            <td>89-172-27/1-07/20</td>
            <td>15.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36017030" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Администрация города Губкинского</td>
            <td>8911006178</td>
            <td>89-172-01/1-07/394</td>
            <td>21.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36169168" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Контрольно-счетная палата городского округа город Губкинский</td>
            <td>8911026350</td>
            <td>89-172-24/1-07/3</td>
            <td>16.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36051921" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Дума города Губкинского</td>
            <td>8913002676</td>
            <td>89-172-1/1-04/3</td>
            <td>16.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36072011" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное учреждение &quot;Муниципальная управляющая компания&quot;</td>
            <td>8911028566</td>
            <td>89-172-41/1-06/77</td>
            <td>21.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36175145" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное учреждение &quot;Молодежный центр &quot;Современник&quot;</td>
            <td>8913009343</td>
            <td>89-172-3121/1-07/47</td>
            <td>17.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36104888" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление по делам молодежи и туризму</td>
            <td>8913005028</td>
            <td>89-172-31/1-06/50</td>
            <td>17.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36117127" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное казенное учреждение &quot;Управление организации строительства&quot;</td>
            <td>8913007850</td>
            <td>89-172-25/1-07/140</td>
            <td>17.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36081679" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ «Автодорсервис»</td>
            <td>8911031777</td>
            <td>89-172-28/1-07/519</td>
            <td>19.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37285013" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ &quot;Губкинская телерадиокомпания &quot;Вектор&quot;</td>
            <td>8911015486</td>
            <td>89-172-26/1-07/38</td>
            <td>17.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36098528" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-губкинский-terr-мку-центр-по-обслуживанию-деятельности-учреждений-культуры-и-искусства" class="dept-checkbox">
    <label for="dept-terr-губкинский-terr-мку-центр-по-обслуживанию-деятельности-учреждений-культуры-и-искусства" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">МКУ «Центр по обслуживанию деятельности учреждений культуры и искусства» <span class="org-count">(учреждений: 11)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>МКУ «Центр по обслуживанию деятельности учреждений культуры и искусства»</td>
            <td>8911032202</td>
            <td>89-172-3325/1-08/8</td>
            <td>07.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37871123" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ «Губкинский музей освоения Севера»</td>
            <td>8913001880</td>
            <td>89-172-3323/1-07/53</td>
            <td>07.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37879687" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное учреждение дополнительного образования «Губкинская детская школа искусств имени Г.В. Свиридова»</td>
            <td>8911007647</td>
            <td>89-172-3324/1-08/68</td>
            <td>19.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37276632" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление культуры Администрации города Губкинского</td>
            <td>8913000534</td>
            <td>89-172-33/1-06/231</td>
            <td>07.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37871524" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное учреждение «Централизованная библиотечная система города Губкинского»</td>
            <td>8913007184</td>
            <td>89-172-3322/1-07</td>
            <td>07.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37880243" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное учреждение «Централизованная клубная система города Губкинского»</td>
            <td>8911000641</td>
            <td>89-172-3321/1-06</td>
            <td>07.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37871603" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление по физической культуре и спорту Администрации города Губкинского</td>
            <td>8913000492</td>
            <td>89-172-35/1-06/358</td>
            <td>06.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37842389" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ СШ «Арктика»</td>
            <td>8911003681</td>
            <td>89-172-3522/1-08.1/353</td>
            <td>06.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37846277" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ СШ «Зенит»</td>
            <td>8911025580</td>
            <td>89-172-3524/1-08.1/214</td>
            <td>06.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37853039" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ СШ «Олимп»</td>
            <td>8913001560</td>
            <td>89-172-3523/1-05/261</td>
            <td>06.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37850892" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ ДО СШОР &quot;Фортуна&quot;</td>
            <td>8913009880</td>
            <td>89-172-3521/1-08/166</td>
            <td>06.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37846516" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-губкинский-terr-мку-quot-дирекция-по-ресурсному-обеспечению-системы-образования-quot" class="dept-checkbox">
    <label for="dept-terr-губкинский-terr-мку-quot-дирекция-по-ресурсному-обеспечению-системы-образования-quot" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">МКУ &quot;Дирекция по ресурсному обеспечению системы образования&quot; <span class="org-count">(учреждений: 23)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>МКУ &quot;Дирекция по ресурсному обеспечению системы образования&quot;</td>
            <td>8911032040</td>
            <td>89-172-3240/1-07/395</td>
            <td>25.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38461260" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ «Брусничка»</td>
            <td>8911028580</td>
            <td>89-172-3234/01-07/48</td>
            <td>28.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38605063" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ «Школа им. Ярослава Василенко»</td>
            <td>8911016627</td>
            <td>89-172-3243/1-07/64</td>
            <td>28.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38612875" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ «Старшая школа «Высотка»</td>
            <td>8911032989</td>
            <td>89-172-3222/1-07/162</td>
            <td>28.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38607768" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ «ДДТ»</td>
            <td>8911019427</td>
            <td>89-172-3247/1-07/106</td>
            <td>27.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38464765" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ «Звездочка»</td>
            <td>8911017490</td>
            <td>89-172-3245/01-04/98</td>
            <td>27.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38563644" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ «Лицей»</td>
            <td>8911015849</td>
            <td>89-172-3225/1-07/77</td>
            <td>27.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38567810" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ «Непоседы»</td>
            <td>8911031664</td>
            <td>89-172-3236/1-06-01/92</td>
            <td>28.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38563367" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ «Радость»</td>
            <td>8913002147</td>
            <td>89-172-3233/1-07/92</td>
            <td>25.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38463815" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ «Русалочка»</td>
            <td>8913001520</td>
            <td>89-172-3238/1-07/49</td>
            <td>27.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38556995" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ «Светлячок»</td>
            <td>8913001552</td>
            <td>89-172-3239/01-07/56</td>
            <td>28.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38555737" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ ЦРР д/с «Сказка»</td>
            <td>8913001506</td>
            <td>89-172-3230/01-08/50</td>
            <td>26.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38468199" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ «СКОШ»</td>
            <td>8913001915</td>
            <td>89-172-3228/1-06/42</td>
            <td>28.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38603814" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ «Солнышко»</td>
            <td>8913001626</td>
            <td>89-172-3231/1-07/37</td>
            <td>27.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38469033" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ «СОШ №1»</td>
            <td>8911015817</td>
            <td>137</td>
            <td>28.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38598897" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ «СТУПЕНИ»</td>
            <td>8911033559</td>
            <td>389</td>
            <td>28.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38612297" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАОУ «СОШ №4»</td>
            <td>8913001270</td>
            <td>89-172-3224/1-07-01/258</td>
            <td>28.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38580879" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ «СОШ №7»</td>
            <td>8913000580</td>
            <td>89-172-3227/1-07/87</td>
            <td>28.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38603937" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ «СОШ №9»</td>
            <td>8911016641</td>
            <td>89-172-3241/01-06/83</td>
            <td>28.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38578680" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ «СТТ»</td>
            <td>8913009287</td>
            <td>89-172-3237/1-07/23</td>
            <td>27.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38570263" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ «Теремок»</td>
            <td>8913001721</td>
            <td>89-172-3232/1-07/68</td>
            <td>27.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38550706" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ «Умка»</td>
            <td>8911030685</td>
            <td>89-172-3235/1-07/138</td>
            <td>25.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38467402" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление образования Администрации города Губкинского</td>
            <td>8911013256</td>
            <td>89-172-32/1-07/1036</td>
            <td>25.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38487028" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-губкинский-terr-организация-не-указана-нет-бу" class="dept-checkbox">
    <label for="dept-terr-губкинский-terr-организация-не-указана-нет-бу" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">Организация не указана (нет БУ) <span class="org-count">(учреждений: 3)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Управление по труду и социальной защите населения Администрации города Губкинского</td>
            <td>8911016056</td>
            <td>89-172-34/1-07/-00070</td>
            <td>18.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37237086" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент финансов г.Губкинского</td>
            <td>8911015863</td>
            <td>89-172-30/1-07-01/66</td>
            <td>10.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36933687" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент по управлению муниципальным имуществом города Губкинского</td>
            <td>8911016017</td>
            <td>89-172-40/01-07/698</td>
            <td>19.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37271606" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

## Красноселькупский район <span class="toc-badge">2</span>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-красноселькупский-район-terr-мку-quot-централизованная-бухгалтерия-красноселькупского-района-quot" class="dept-checkbox">
    <label for="dept-terr-красноселькупский-район-terr-мку-quot-централизованная-бухгалтерия-красноселькупского-района-quot" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">МКУ &quot;Централизованная бухгалтерия Красноселькупского района&quot; <span class="org-count">(учреждений: 13 <span class="no-requests">| нет заявок: 1</span>)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Администрация Красноселькупского района</td>
            <td>8912001648</td>
            <td>153/04-07/6900</td>
            <td>25.09.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=44124608" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное казенное учреждение &quot;Служба технического обеспечения&quot;</td>
            <td>8912002747</td>
            <td>153-26/01-07/140</td>
            <td>07.10.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=44582199" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Администрация Красноселькупского района Доходы 801</td>
            <td>8912001648</td>
            <td>153/04-07/7353</td>
            <td>09.10.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=44671711" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Администрация Красноселькупского района Доходы 863</td>
            <td>8912001648</td>
            <td>153/04-07/7353</td>
            <td>09.10.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=44671711" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление финансов Администрации Красноселькупского района</td>
            <td>8912001662</td>
            <td>153-07/01-07/289</td>
            <td>21.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42930974" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление муниципальным имуществом Администрации Красноселькупского района</td>
            <td>8912000605</td>
            <td>153-08/01-07/1996</td>
            <td>03.09.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=43335123" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Администрация села Толька</td>
            <td>8911032153</td>
            <td>153-912-20/01-07/1161</td>
            <td>10.10.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=44728055" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Дума Красноселькупского района</td>
            <td>8912002338</td>
            <td>153-1/01-07/69</td>
            <td>25.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=43012109" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ &quot;Единая дежурная диспетчерская служба&quot;</td>
            <td>8911032594</td>
            <td>153-27/01-07/228</td>
            <td>26.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=43052544" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ &quot;Комитет по управлению капитальным строительством&quot;</td>
            <td>8912002112</td>
            <td>153-25/01-07/962</td>
            <td>28.09.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=43124931" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ Управление жилищно - коммунального хозяйства, дорожной деятельности и благоустройства</td>
            <td>8911034270</td>
            <td>153-29/01-07/36</td>
            <td>22.01.2026</td>
            <td><a href="https://doc.yanao.ru/app/o?u=48301985" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ &quot;Централизованная бухгалтерия Красноселькупского района&quot;</td>
            <td>8911034217</td>
            <td>153-28/01-07/4</td>
            <td>30.09.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=45503785" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>КСП Красноселькупского района</td>
            <td>8912002874</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-красноселькупский-район-terr-организация-не-указана-нет-бу" class="dept-checkbox">
    <label for="dept-terr-красноселькупский-район-terr-организация-не-указана-нет-бу" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">Организация не указана (нет БУ) <span class="org-count">(учреждений: 3)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Управление по труду и социальной защите населения Администрации Красноселькупского района</td>
            <td>8912001790</td>
            <td>153-12/01-07/571</td>
            <td>21.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40304653" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МДОУ детский сад &quot;Березка&quot;</td>
            <td>8912001743</td>
            <td>186</td>
            <td>30.09.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=44287738" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МУДО &quot;Толькинский центр дополнительного образования детей&quot;</td>
            <td>8912002507</td>
            <td>43</td>
            <td>30.09.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=44287916" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-красноселькупский-район-terr-мку-quot-центр-обеспечения-деятельности-управления-по-культуре-молодёжной-политике-и-спорту-quot" class="dept-checkbox">
    <label for="dept-terr-красноселькупский-район-terr-мку-quot-центр-обеспечения-деятельности-управления-по-культуре-молодёжной-политике-и-спорту-quot" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">МКУ &quot;Центр обеспечения деятельности Управления по культуре, молодёжной политике и спорту&quot; <span class="org-count">(учреждений: 11)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>УКПМС Администрации Красноселькупкого района</td>
            <td>8912002056</td>
            <td>153-09/01-07/902</td>
            <td>05.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42510921" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ &quot;Центр обеспечения деятельности Упрасления по культуре, молодёжной политике и спорту&quot;</td>
            <td>8911012799</td>
            <td>153-09/01-07/901</td>
            <td>05.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42514590" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МУДО «Красноселькупская детская школа искусств»</td>
            <td>8912001535</td>
            <td>153-0921/01-07/31</td>
            <td>05.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42511937" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУДО «Толькинская детская школа искусств»</td>
            <td>8912001599</td>
            <td>153-09/01-07/914</td>
            <td>08.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42610286" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ МП МЦ «Школа Ямолод. Красноселькупский район</td>
            <td>8912002955</td>
            <td>153-0926/01-07/105</td>
            <td>06.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42511479" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МУ культуры «Красноселькупский районный краеведческий музей»</td>
            <td>8912002708</td>
            <td>153-09/01-07/913</td>
            <td>08.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42610375" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МУ культуры «Централизованная библиотечная система»</td>
            <td>8912002962</td>
            <td>00001</td>
            <td>05.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42513645" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МУ культуры «Централизованная клубная система»</td>
            <td>8912002987</td>
            <td>153-0925/01-07/50</td>
            <td>06.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42513745" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МУ культуры «Районный Дом ремесел»</td>
            <td>8912002970</td>
            <td>153-0924/01-07/31</td>
            <td>06.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42513825" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУДО «Красноселькупская районная спортивная школа»</td>
            <td>8911030533</td>
            <td>01-07/87</td>
            <td>05.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42513948" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ «Центр обеспечения и развития физической культуры и спорта Красноселькупского района»</td>
            <td>8911031350</td>
            <td>153-0928/01-08/172</td>
            <td>06.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42554949" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-красноселькупский-район-terr-му-quot-центр-по-обеспечению-деятельности-муниципальной-системы-образования-quot" class="dept-checkbox">
    <label for="dept-terr-красноселькупский-район-terr-му-quot-центр-по-обеспечению-деятельности-муниципальной-системы-образования-quot" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">МУ &quot;Центр по обеспечению деятельности муниципальной системы образования&quot; <span class="org-count">(учреждений: 7 <span class="no-requests">| нет заявок: 1</span>)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Управление образования Администрации Красноселькупского района</td>
            <td>8912001616</td>
            <td>153-10/01-07/2363</td>
            <td>29.09.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=44238788" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МУ &quot;Центр по обеспечению деятельности муниципальной системы образования&quot;</td>
            <td>8911012936</td>
            <td>153-1020/01-07/836</td>
            <td>29.09.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=44236247" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МДОУ детский сад &quot;Морошка&quot;</td>
            <td>8912001704</td>
            <td>00529</td>
            <td>30.09.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=44261761" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МУДО &quot;Красноселькупский центр дополнительного образования детей&quot;</td>
            <td>8912002419</td>
            <td>153-1027/01-08-01/241</td>
            <td>30.09.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=44261614" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МОУ Красноселькупская средняя образовательная школа &quot;Радуга&quot;</td>
            <td>8912002426</td>
            <td>153-1021/01-08-01/563</td>
            <td>29.09.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=44245530" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МОУ &quot;Раттовская школа-интернат основного общего образования им. С.И. Ирикова&quot;</td>
            <td>8912001528</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>МОУ &quot;Толькинская школа-интернат среднего общего образования&quot;</td>
            <td>8912001207</td>
            <td>528</td>
            <td>30.09.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=44291968" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

## Лабытнанги Приуральский район <span class="toc-badge">1</span>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-лабытнанги-приуральский-район-terr-мку-центр-бюджетного-учета-и-отчетности" class="dept-checkbox">
    <label for="dept-terr-лабытнанги-приуральский-район-terr-мку-центр-бюджетного-учета-и-отчетности" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">МКУ Центр бюджетного учета и отчетности <span class="org-count">(учреждений: 18 <span class="no-requests">| нет заявок: 1</span>)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>МКУ Центр бюджетного учета и отчетности</td>
            <td>8901043879</td>
            <td>89-173/01-10-01/5</td>
            <td>03.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=41638636" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Администрация Приуральского района</td>
            <td>8901044128</td>
            <td>89-173/01-10-03/78</td>
            <td>01.11.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=45573443" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Дума Приуральского района</td>
            <td>8901044054</td>
            <td>89-173/01-10-03/78</td>
            <td>01.11.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=45573443" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>ДЕПАРТАМЕНТ  ФИНАНСОВ АДМИНИСТРАЦИИ ПРИУРАЛЬСКОГО РАЙОНА</td>
            <td>8901044167</td>
            <td>89-173/01-10-03/106</td>
            <td>02.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=46630792" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>ДЕПАРТАМЕНТ  ГРАДОСТРОИТЕЛЬСТВА, ЗЕМЛЕПОЛЬЗОВАНИЯ И    ИМУЩЕСТВЕННЫХ ОТНОШЕНИЙ АДМИНИСТРАЦИИ ПРИУРАЛЬСКОГО РАЙОНА</td>
            <td>8901044255</td>
            <td>89-173/01-10-03/106</td>
            <td>02.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=46630792" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>ДЕПАРТАМЕНТ  ОБРАЗОВАНИЯ АДМИНИСТРАЦИИ ПРИУРАЛЬСКОГО РАЙОНА</td>
            <td>8901044230</td>
            <td>89-173/01-10-03/106</td>
            <td>02.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=46630792" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>УПРАВЛЕНИЕ  КУЛЬТУРЫ АДМИНИСТРАЦИИ ПРИУРАЛЬСКОГО РАЙОНА</td>
            <td>8901044223</td>
            <td>89-173/01-10-03/106</td>
            <td>02.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=46630792" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>УПРАВЛЕНИЕ  МОЛОДЕЖНОЙ ПОЛИТИКИ АДМИНИСТРАЦИИ ПРИУРАЛЬСКОГО РАЙОНА</td>
            <td>8901044248</td>
            <td>89-173/01-10-03/106</td>
            <td>02.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=46630792" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ &quot;Управление капитального строительства города Лабытнанги&quot;</td>
            <td>8902003396</td>
            <td>89-173/01001-07/102</td>
            <td>25.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38455745" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МУ &quot;Центр обеспечения деятельности системы Градостроительства&quot;</td>
            <td>8901035638</td>
            <td>89-173/01101-07/164</td>
            <td>24.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38436021" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МУ &quot;Дирекция по обеспечению деятельности в сфере жилищно-коммунального хозяйства&quot;</td>
            <td>8901038639</td>
            <td>89-173/071-01-07/235</td>
            <td>21.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38350097" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>КОНТРОЛЬНО-СЧЕТНАЯ ПАЛАТА ПРИУРАЛЬСКОГО РАЙОНА</td>
            <td>8901044400</td>
            <td>89-173/01-10-03/137</td>
            <td>26.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47684453" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>УПРАВЛЕНИЕ ЖИЛИЩНО-КОММУНАЛЬНОГО ХОЗЯЙСТВА, ТРАНСПОРТА И СВЯЗИ АДМИНИСТРАЦИИ ПРИУРАЛЬСКОГО РАЙОНА</td>
            <td>8901044270</td>
            <td>89-173/01-10-03/106</td>
            <td>02.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=46630792" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>УПРАВЛЕНИЕ ПО ТРУДУ И СОЦИАЛЬНОЙ ЗАЩИТЕ НАСЕЛЕНИЯ АДМИНИСТРАЦИИ ПРИУРАЛЬСКОГО РАЙОНА</td>
            <td>8901044216</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>МУНИЦИПАЛЬНОЕ  УЧРЕЖДЕНИЕ &quot;ЕДИНАЯ ДЕЖУРНО-ДИСПЕТЧЕРСКАЯ СЛУЖБА ГОРОДА ЛАБЫТНАНГИ&quot;</td>
            <td>8902012834</td>
            <td>89-173/0401-07/48</td>
            <td>20.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38323891" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МУНИЦИПАЛЬНОЕ  УЧРЕЖДЕНИЕ &quot;ЦЕНТР МАТЕРИАЛЬНО-ТЕХНИЧЕСКОГО ОБЕСПЕЧЕНИЯ&quot;</td>
            <td>8901033983</td>
            <td>89-173/0601-07/107</td>
            <td>20.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38322532" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>УПРАВЛЕНИЕ  ФИЗИЧЕСКОЙ КУЛЬТУРЫ И СПОРТА АДМИНИСТРАЦИИ ПРИУРАЛЬСКОГО РАЙОНА</td>
            <td>8901044262</td>
            <td>89-173/01-10-03/106</td>
            <td>02.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=46630792" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>ДЕПАРТАМЕНТ СТРОИТЕЛЬСТВА, АРХИТЕКТУРЫ И ЖИЛИЩНОЙ ПОЛИТИКИ АДМИНИСТРАЦИИ ПРИУРАЛЬСКОГО РАЙОНА</td>
            <td>8901045097</td>
            <td>89-939/01-10-03/178</td>
            <td>03.08.2026</td>
            <td><a href="https://doc.yanao.ru/app/o?u=55119212" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-лабытнанги-приуральский-район-terr-мку-кц-по-омсо-г-лабытнанги" class="dept-checkbox">
    <label for="dept-terr-лабытнанги-приуральский-район-terr-мку-кц-по-омсо-г-лабытнанги" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">МКУ КЦ по ОМСО г.Лабытнанги <span class="org-count">(учреждений: 23)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>МКУ КЦ по ОМСО г.Лабытнанги</td>
            <td>8901034088</td>
            <td>89-173/08101-01-07/239</td>
            <td>24.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38429136" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАОУ Средняя общеобразовательная школа №1</td>
            <td>8902008370</td>
            <td>89-173/08601-07/68</td>
            <td>25.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38429803" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАОУ Средняя общеобразовательная школа №3 с углубленным изучением отдельных предметов</td>
            <td>8902008517</td>
            <td>89-173/088/01-36/120</td>
            <td>24.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38433861" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАОУ Средняя общеобразовательная школа №5</td>
            <td>8902008436</td>
            <td>89-173/08701-07/130</td>
            <td>24.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38433037" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАОУ Средняя общеобразовательная школа № 7 с углубленным изучением отдельных предметов</td>
            <td>8901041737</td>
            <td>89-173/0819-01-07/112</td>
            <td>24.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38434007" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАОУ Средняя общеобразовательная школа №8</td>
            <td>8902008330</td>
            <td>89-173/084/01-07/126</td>
            <td>24.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38433751" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАОУ Гимназия города Лабытнанги</td>
            <td>8902008940</td>
            <td>89-173/085/01-07/107</td>
            <td>24.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38434327" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАОУ Школа п. Харп</td>
            <td>8902008468</td>
            <td>89-173/01-07/149</td>
            <td>25.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38434431" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАОУ дополнительного образования «Центр технического творчества»</td>
            <td>8902011358</td>
            <td>89-173/0817-01-07/55</td>
            <td>24.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38434622" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ Волшебница г.Лабытнанги</td>
            <td>8902012016</td>
            <td>89-173/01-07/80</td>
            <td>24.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38435014" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ детский сад «Едэйко»</td>
            <td>8902009461</td>
            <td>89-173/0811-01-07/44</td>
            <td>24.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38435085" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ детский сад «Ромашка»</td>
            <td>8902009510</td>
            <td>89-173/0813-01-07/98</td>
            <td>25.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38435333" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ детский сад &quot;Снежинка&quot;</td>
            <td>8902009503</td>
            <td>89-173/0815/01-46/66</td>
            <td>24.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38435402" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ детский сад «Улыбка»</td>
            <td>8902008309</td>
            <td>89-173/0812-01-07/40</td>
            <td>24.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38435513" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное общеобразовательное учреждение  Школа с. Аксарка</td>
            <td>8908000962</td>
            <td>00093</td>
            <td>24.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39557531" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное дошкольное общеобразовательное учреждение &quot;Солнышко&quot;</td>
            <td>8908001532</td>
            <td>106/108-01/19</td>
            <td>18.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39377537" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное учреждение дополнительного образования Центр детского творчества</td>
            <td>8908000955</td>
            <td>00010</td>
            <td>03.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38805341" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное общеобразовательное учреждение  Школа Анны Неркаги</td>
            <td>8908001109</td>
            <td>01-08/110</td>
            <td>11.06.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=41025107" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное общеобразовательное учреждение Школа с. Белоярск</td>
            <td>8908000970</td>
            <td>00042</td>
            <td>24.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39573347" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное дошкольное общеобразовательное учреждение &quot;Брусничка&quot;</td>
            <td>8908000916</td>
            <td>00004</td>
            <td>26.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40443735" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное общеобразовательное учреждение &quot;Школа с. Катравож имени героя советского союза А.М. Зверева&quot;</td>
            <td>8908001074</td>
            <td>00013</td>
            <td>26.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40459064" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное общеобразовательное учреждение &quot;Начальная школа п. Зеленый Яр &quot;</td>
            <td>8908001229</td>
            <td>00005</td>
            <td>16.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40160633" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное общеобразовательное учреждение &quot;Школа с. Харсаим&quot;</td>
            <td>8908000930</td>
            <td>00011</td>
            <td>28.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40541772" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-лабытнанги-приуральский-район-terr-мку-кцо-уксми-г-лабытнанги" class="dept-checkbox">
    <label for="dept-terr-лабытнанги-приуральский-район-terr-мку-кцо-уксми-г-лабытнанги" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">МКУ КЦО УКСМИ г.Лабытнанги <span class="org-count">(учреждений: 9)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>МКУ КЦО УКСМИ г.Лабытнанги</td>
            <td>8901035155</td>
            <td>89-173/09301-07/41</td>
            <td>21.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38335120" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАУ дополнительного образования &quot;Детская школа искусств&quot;</td>
            <td>8902009599</td>
            <td>89-173/09701-07/80</td>
            <td>21.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38345583" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАУ культуры &quot;Централизованная библиотечная система&quot;</td>
            <td>8902012760</td>
            <td>89-173/09201-07/18</td>
            <td>21.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38339003" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАУ культуры &quot;Городской краеведческий музей&quot;</td>
            <td>8902012753</td>
            <td>89-173/09601-07/24</td>
            <td>21.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38345538" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАУ культуры &quot;Централизованная клубная система&quot;</td>
            <td>8901029225</td>
            <td>89-173/09101-07/137</td>
            <td>21.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38338241" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУК &quot;Приуральская централизованная клубная система&quot;</td>
            <td>8908002582</td>
            <td>89-158-85001-07-00070</td>
            <td>16.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39292579" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУК &quot;Приуральский районный краеведческий музей&quot;</td>
            <td>8908002430</td>
            <td>89-158-853/1-07//20</td>
            <td>15.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39225034" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУК &quot;Приуральская межпоселенческая библиотечная система&quot;</td>
            <td>8908002014</td>
            <td>89-158-852/1-07/-00015</td>
            <td>14.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39191995" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ ДО &quot;Аксарковская детская школа искусств&quot;</td>
            <td>8908000715</td>
            <td>89-158-851/1-07/15</td>
            <td>12.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39157211" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-лабытнанги-приуральский-район-terr-мку-quot-кцо-фксмпит-quot-лабытнаги" class="dept-checkbox">
    <label for="dept-terr-лабытнанги-приуральский-район-terr-мку-quot-кцо-фксмпит-quot-лабытнаги" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">МКУ &quot;КЦО ФКСМПИТ&quot; Лабытнаги <span class="org-count">(учреждений: 7)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>МКУ МКУ &quot;КЦО ФКСМПИТ&quot; Лабытнаги</td>
            <td>8901035162</td>
            <td>89-173/05101-07/107</td>
            <td>21.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38364994" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАУДО спортивная школа &quot;Юность&quot;</td>
            <td>8902013980</td>
            <td>89-173/05201-07/184</td>
            <td>21.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38366220" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАУ &quot;Молодёжный центр города лабытнанги&quot;</td>
            <td>8901034874</td>
            <td>89-173/05401-07/90</td>
            <td>21.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38367242" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАУ &quot;Центр активного отдыха&quot;</td>
            <td>8901042410</td>
            <td>89-173/05601-07/25</td>
            <td>21.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38367544" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ ДО &quot;Спортивная школа Приуральского района &quot;Полярный медведь&quot;</td>
            <td>8908001821</td>
            <td>89-158-856/1-07/14</td>
            <td>05.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39819858" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МУ &quot;Районный спортивно-оздоровительный комплекс&quot;</td>
            <td>8908002127</td>
            <td>89-158-857/1-10-00028</td>
            <td>15.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39223619" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАУ &quot;Центр спортивной и физкультурно-массовой работы&quot;</td>
            <td>8901033920</td>
            <td>89-173 /05301-07/108</td>
            <td>21.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38366723" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-лабытнанги-приуральский-район-terr-организация-не-указана-нет-бу" class="dept-checkbox">
    <label for="dept-terr-лабытнанги-приуральский-район-terr-организация-не-указана-нет-бу" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">Организация не указана (нет БУ) <span class="org-count">(учреждений: 36)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Администрация Приуральского района</td>
            <td>8908001902</td>
            <td>89-158-1/01-07/2592</td>
            <td>29.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39698029" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>АДМИНИСТРАЦИЯ ГОРОДА ЛАБЫТНАНГИ</td>
            <td>8902002956</td>
            <td>89-173/101-07/1298</td>
            <td>19.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38161817" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент финансов Администрации Приуральского района</td>
            <td>8908002039</td>
            <td>89-158-5/01-06/89</td>
            <td>11.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39127252" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>КОНТРОЛЬНО-СЧЕТНАЯ ПАЛАТА ПРИУРАЛЬСКОГО РАЙОНА Л/К</td>
            <td>8908002913</td>
            <td>104-01-00281</td>
            <td>11.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39120231" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МУ Контрольно-счетная палата города Лабытнанги</td>
            <td>8902014567</td>
            <td>89-173/301-01-07/6</td>
            <td>17.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38179417" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МУ Управление физической культуры, спорта, молодежной политики и туризма Администрации города Лабытнанги</td>
            <td>8902008323</td>
            <td>89-173/0501-07/451</td>
            <td>21.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38360408" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МУ «Департамент финансов Администрации города Лабытнанги»</td>
            <td>8902003452</td>
            <td>89-173/0201-07/192</td>
            <td>24.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38335846" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление образования Администрации Приуральского района</td>
            <td>8908002053</td>
            <td>89-158-11/01-06/00913</td>
            <td>16.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40157784" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МУ Управление образования Администрации города Лабытнанги</td>
            <td>8902003170</td>
            <td>89-173/0801-07/1130</td>
            <td>24.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38429379" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление культуры, молодежной политики и спорта Администрации Приуральского района</td>
            <td>8908002007</td>
            <td>89-158-08/01-07/344</td>
            <td>16.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39285737" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МУ Управление культуры Администрации города Лабытнанги</td>
            <td>8902007200</td>
            <td>89-173/0901-07/303</td>
            <td>21.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38336425" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Дума Приуральского района</td>
            <td>8908001853</td>
            <td>89-158-11/01-07/24</td>
            <td>29.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39703649" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Дума города Лабытнанги</td>
            <td>8902011630</td>
            <td>89-173/201-07/43</td>
            <td>20.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38324869" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент имущественных отношений Администрации Приуральскогорайона</td>
            <td>8908002134</td>
            <td>89-158-6/01-06/1257</td>
            <td>16.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39283450" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МУ &quot;Департамент градостроительства, землепользования и имущественных отношений Администрации города Лабытнанги&quot;</td>
            <td>8901035910</td>
            <td>89-173/0101-07/577</td>
            <td>25.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38459074" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ детский сад «Ягодка»</td>
            <td>8902009574</td>
            <td>89-173/08901-07/108</td>
            <td>24.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38435924" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление строительства и жилищной политики Администрации Приуральского района</td>
            <td>8908003025</td>
            <td>89-158-12/01-06/728</td>
            <td>22.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39478660" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление по труду и социаной защите населения Администрации Приуральского района</td>
            <td>8908002021</td>
            <td>89-158-7/01-07/00374</td>
            <td>22.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39497300" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент жилищно-коммунального комплекса Администрации Приуральского района</td>
            <td>8901040469</td>
            <td>89-158-4/01-06/922</td>
            <td>14.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38102305" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МУ &quot;Управление жилищно-коммунального хозяйства и транспорта Администрации города Лабытнанги&quot;</td>
            <td>8902008394</td>
            <td>89-173/0701-07/307</td>
            <td>21.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38351718" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МУ &quot;Управление по труду и социальной защите населения Администрации города Лабытнанги&quot;</td>
            <td>8902007792</td>
            <td>89-173/0301-07/487</td>
            <td>21.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38350908" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ &quot;ЦБ учреждений культуры, молодежной политики и спорта&quot;</td>
            <td>8908001941</td>
            <td>89-158-857/1-07/-00021</td>
            <td>11.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39118620" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МУ &quot;ЦБ образовательных организаций Приуральского района&quot;</td>
            <td>8908001966</td>
            <td>01-08/72</td>
            <td>22.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39485436" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное казенное учреждение &quot;Ресурсно-методический центр развития системы образования Приуральского района&quot;</td>
            <td>8901037184</td>
            <td>01-06/105</td>
            <td>27.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40162249" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАУ &quot;Информационное агенство &quot;Лабытнанги&quot;</td>
            <td>8902010474</td>
            <td>89-173/09501-07/84</td>
            <td>21.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38339349" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ &quot;Районный молодежный центр&quot;</td>
            <td>8908002335</td>
            <td>89-158-854/01-07/73</td>
            <td>11.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39131784" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное учреждение &quot;Информационное агенство &quot;Приуралье&quot;</td>
            <td>8908001363</td>
            <td>89-158-150/01-09/-00305</td>
            <td>11.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39147080" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МУНИЦИПАЛЬНОЕ  КАЗЕННОЕ УЧРЕЖДЕНИЕ &quot;СЛУЖБА РАЗМЕЩЕНИЯ МУНИЦИПАЛЬНОГО ЗАКАЗА&quot;  ПРИУРАЛЬСКОГО РАЙОНА</td>
            <td>8908003145</td>
            <td>00266</td>
            <td>12.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39972845" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное казенное учреждение «Служба эксплуатации и технического обслуживания Администрации  Приуральского района»</td>
            <td>8908002840</td>
            <td>03-800-03-00651</td>
            <td>28.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39679197" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ &quot;Управление капитального строительства&quot;</td>
            <td>8908001451</td>
            <td>14-500-02/291</td>
            <td>02.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38755223" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ «Жемчужинка»</td>
            <td>8902009479</td>
            <td>89-173/0810-01-07/58</td>
            <td>25.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38435240" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ «Улыбка пгт. Харп»</td>
            <td>8902009581</td>
            <td>89-173/0816-01-07/37</td>
            <td>24.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38435589" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАУ дополнительного образования Дом детского творчества &quot;Левша&quot;</td>
            <td>8902008443</td>
            <td>89-173/0818-02-05/059</td>
            <td>24.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38434758" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАОУ начальная  школа п. Харп</td>
            <td>8902008475</td>
            <td>89-173/08301-07/60</td>
            <td>24.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38434513" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАУ дополнительного образования &quot;Детская школа искусств п. Харп&quot;</td>
            <td>8902009609</td>
            <td>89-173/09801-07/14</td>
            <td>21.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38345601" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное общеобразовательное учреждение  &quot;Начальная школа п. Щучье&quot;</td>
            <td>8908001028</td>
            <td>01-08/109</td>
            <td>11.06.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=41021974" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

## Муравленко <span class="toc-badge">2</span>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-муравленко-terr-казенное-учреждение-quot-централизованная-бухгалтерия-органов-местного-самоуправления-quot" class="dept-checkbox">
    <label for="dept-terr-муравленко-terr-казенное-учреждение-quot-централизованная-бухгалтерия-органов-местного-самоуправления-quot" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">Казенное учреждение &quot;централизованная бухгалтерия органов местного самоуправления&quot; <span class="org-count">(учреждений: 9 <span class="no-requests">| нет заявок: 1</span>)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>МКУ &quot;ЕДДС МО город Муравленко&quot;</td>
            <td>8905056283</td>
            <td>175-0451/01-07/34</td>
            <td>08.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38982597" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>УМИ Администрации города Муравленко</td>
            <td>8906004016</td>
            <td>18/01-07.1/888</td>
            <td>11.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39114664" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>ПОМО Городская Дума города Муравленко</td>
            <td>8906007338</td>
            <td>175-1/01-07/15</td>
            <td>21.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39427971" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>КСП Муравленко</td>
            <td>8905051510</td>
            <td>89-175-2/01-08/24</td>
            <td>21.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39427848" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление финансов Администрации города Муравленко</td>
            <td>8906004150</td>
            <td>175-11/01-07/4</td>
            <td>22.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36273026" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление жилищно-коммунального хозяйства Администрации города Муравленко</td>
            <td>8906008596</td>
            <td>175-16/01-07/58</td>
            <td>21.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36173102" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ «Управление коммунального заказа»</td>
            <td>8906006158</td>
            <td>175-1651/01-07/16</td>
            <td>27.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36403195" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>КАЗЕННОЕ УЧРЕЖДЕНИЕ &quot;ЦЕНТРАЛИЗОВАННАЯ БУХГАЛТЕРИЯ ОРГАНОВ МЕСТНОГО САМОУПРАВЛЕНИЯ&quot;</td>
            <td>8905069483</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>АДМИНИСТРАЦИЯ ГОРОДА МУРАВЛЕНКО</td>
            <td>8906003365</td>
            <td>175/01-07/259</td>
            <td>06.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36867676" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-муравленко-terr-организация-не-указана-нет-бу" class="dept-checkbox">
    <label for="dept-terr-муравленко-terr-организация-не-указана-нет-бу" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">Организация не указана (нет БУ) <span class="org-count">(учреждений: 7)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Управление социальной защиты населения Администрации города Муравленко</td>
            <td>8906005524</td>
            <td>175-15/01-07/262</td>
            <td>07.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39908759" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ «Детский сад «Сказка»</td>
            <td>8906004721</td>
            <td>1263/01-07.1/103</td>
            <td>29.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39679221" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ «Детский сад «Оленёнок»</td>
            <td>8906005605</td>
            <td>1265/01-07.1/144</td>
            <td>05.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39680256" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ дополнительного образования &quot;Детская музыкальная школа&quot;</td>
            <td>8906004947</td>
            <td>1352/01-07.1/55</td>
            <td>09.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39022298" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ дополнительного образования &quot;Детская художественная школа&quot;</td>
            <td>8906006045</td>
            <td>1353/01-05/136</td>
            <td>09.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39070454" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ «Детский сад «Ладушки»</td>
            <td>8905068070</td>
            <td>1273/01-07.1/109</td>
            <td>28.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39679867" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное учреждение &quot;Муравленко медиа&quot;</td>
            <td>8906006091</td>
            <td>175-0751/01-07/2</td>
            <td>25.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39610338" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-муравленко-terr-мку-quot-центр-обслуживания-культуры-quot" class="dept-checkbox">
    <label for="dept-terr-муравленко-terr-мку-quot-центр-обслуживания-культуры-quot" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">МКУ &quot;Центр обслуживания культуры&quot; <span class="org-count">(учреждений: 11)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Управление молодёжной политики Администрации города Муравленко</td>
            <td>8905070425</td>
            <td>13/01-07.1/1532</td>
            <td>17.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47252651" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>УФКС Администрации города Муравленко</td>
            <td>8905054455</td>
            <td>89-175-14/01-06/118</td>
            <td>10.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37903789" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАУДО «Спортивная школа «Муравленко»</td>
            <td>8905059358</td>
            <td>175-14/01-07/36</td>
            <td>31.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36653061" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАУДО «Спортивная школа «Арктика»</td>
            <td>8906008821</td>
            <td>175-14/01-07/36</td>
            <td>31.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36653061" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ &quot;Центр обслуживания культуры&quot;</td>
            <td>8905068828</td>
            <td>175-1358/01-07/1</td>
            <td>09.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38996565" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление культуры и молодежной политики Администрации города Муравленко</td>
            <td>8906004859</td>
            <td>175-13/01-07/51</td>
            <td>09.09.2026</td>
            <td><a href="https://doc.yanao.ru/app/o?u=56251602" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАУ культуры &quot;Централизованная клубная система города Муравленко&quot;</td>
            <td>8906006479</td>
            <td>1354/01-05/332</td>
            <td>09.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39019610" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ дополнительного образования &quot;Детская школа искусств&quot;</td>
            <td>8906005531</td>
            <td>175-1351/01-07/2</td>
            <td>09.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39008682" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ &quot;Многофункциональный клуб молодежных инициатив&quot;</td>
            <td>8906009617</td>
            <td>175-1357/01-07/8</td>
            <td>09.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38992553" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ культуры &quot;Централизованная библиотечная система г. Муравленко&quot;</td>
            <td>8906006856</td>
            <td>89-175-1356/01-08/13</td>
            <td>09.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39029326" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ культуры &quot;Эколог-краеведческий музей города Муравленко&quot;</td>
            <td>8906007793</td>
            <td>00007</td>
            <td>15.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39250374" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-муравленко-terr-муниципальное-казённое-учреждение-quot-центр-по-ресурсному-обеспечению-системы-образования-quot" class="dept-checkbox">
    <label for="dept-terr-муравленко-terr-муниципальное-казённое-учреждение-quot-центр-по-ресурсному-обеспечению-системы-образования-quot" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">Муниципальное казённое учреждение &quot;центр по ресурсному обеспечению системы образования&quot; <span class="org-count">(учреждений: 16 <span class="no-requests">| нет заявок: 1</span>)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>МУНИЦИПАЛЬНОЕ КАЗЁННОЕ УЧРЕЖДЕНИЕ &quot;ЦЕНТР ПО РЕСУРСНОМУ ОБЕСПЕЧЕНИЮ СИСТЕМЫ ОБРАЗОВАНИЯ&quot;</td>
            <td>8905069518</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Управление образования Администрации города Муравленко</td>
            <td>8906004009</td>
            <td>89-175-12/01-07/1010</td>
            <td>30.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39723677" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ «Детский сад «Дельфин»</td>
            <td>8906005612</td>
            <td>1266/01-07.1/178</td>
            <td>28.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39678434" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ «Детский сад «Снежинка»</td>
            <td>8906004802</td>
            <td>1268/01-07.1/193</td>
            <td>28.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39687330" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ «Детский сад «Теремок»</td>
            <td>8906001030</td>
            <td>1262/01-07.1/127</td>
            <td>28.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39679467" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ «Детский сад «Солнышко»</td>
            <td>8906005588</td>
            <td>1269/01-07.1/144</td>
            <td>28.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39680640" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ «Детский сад «Непоседы»</td>
            <td>8905056269</td>
            <td>1271/01-07.1/235</td>
            <td>28.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39684468" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАОУ «Прогимназия «Эврика»</td>
            <td>8905062576</td>
            <td>1258/01-07.1/244</td>
            <td>29.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39683342" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАОУ «Школа № 1 имени В.И. Муравленко»</td>
            <td>8906005147</td>
            <td>1251/01-07.1/267</td>
            <td>28.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39680939" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАОУ «ЦО «Школа Роста» (МАОУ «Школа № 2»)</td>
            <td>8906005154</td>
            <td>175-1252/01-07/9</td>
            <td>28.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39682504" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАОУ «Школа № 4»</td>
            <td>8906005179</td>
            <td>1254/01-07.1/239</td>
            <td>28.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39683006" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАОУ «Школа № 5»</td>
            <td>8906005186</td>
            <td>89-175-1255/01-08/94</td>
            <td>28.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39683125" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАОУ «Многопрофильный лицей»</td>
            <td>8906007360</td>
            <td>1257/01-07.1/183</td>
            <td>29.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39681763" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАОУ «Взлёт»</td>
            <td>8905068666</td>
            <td>1274/01-07.1/276</td>
            <td>28.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39682053" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАУДО «Центр дополнительного образования «Протон»</td>
            <td>8906005228</td>
            <td>1260/01-07.1/129</td>
            <td>29.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39682736" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ «Центр развития образования»</td>
            <td>8905068240</td>
            <td>175-1272/01-07/10</td>
            <td>28.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39676517" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

## Надымский

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-надымский-terr-муниципальное-казенное-учреждение-quot-централизованная-бухгалтерия-надымского-района-quot" class="dept-checkbox">
    <label for="dept-terr-надымский-terr-муниципальное-казенное-учреждение-quot-централизованная-бухгалтерия-надымского-района-quot" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">Муниципальное казенное учреждение &quot;Централизованная бухгалтерия Надымского района&quot; <span class="org-count">(учреждений: 35)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Департамент финансов Администрации Надымского района</td>
            <td>8903015595</td>
            <td>174-14/01-07/8</td>
            <td>15.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36017121" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ &quot;Надымское&quot;</td>
            <td>8903033570</td>
            <td>174-24/01-07/6</td>
            <td>27.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36409358" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Администрация Надымского района</td>
            <td>8903008622</td>
            <td>174-1/01-07/215</td>
            <td>28.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36425390" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное казённое учреждение  &quot;Единая дежурно-диспетчерская служба Надымского района&quot;</td>
            <td>8903036010</td>
            <td>174-23/01-07/5</td>
            <td>27.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36427145" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Контрольно-счетная палата  Надымского района</td>
            <td>8903031149</td>
            <td>174-3/01-07/21</td>
            <td>27.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36428688" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Дума Надымского района</td>
            <td>8903025385</td>
            <td>174-2/01-07/1</td>
            <td>29.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36509500" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Территориальный орган Администрации Надымского района Администрация  п. Заполярный</td>
            <td>8903036806</td>
            <td>174-31/01-07/61</td>
            <td>27.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36430347" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Территориальный орган Администрации Надымского района Администрация п. Правохеттинский</td>
            <td>8903036845</td>
            <td>174-33/01-07/62</td>
            <td>27.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36431978" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Территориальный орган Администрации Надымского района Администрация п. Ныда</td>
            <td>8903036852</td>
            <td>174-36/01-07/25</td>
            <td>27.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36427940" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Территориальный орган Администрации Надымского района Администрация п. Кутопьюган</td>
            <td>8903036820</td>
            <td>174-37/01-07/76</td>
            <td>27.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36430658" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент  градостроительной политики, строительного комплекса и земельных отношений Надымского района</td>
            <td>8903037207</td>
            <td>89-174-10/01-06/268</td>
            <td>27.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36425967" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Территориальный орган Администрации Надымского района Администрация поселка Приозерный</td>
            <td>8903036838</td>
            <td>89-174-34/01-06/76</td>
            <td>03.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36690337" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Территориальный орган Администрации Надымского района Администрация поселка Лонгъюган</td>
            <td>8903036813</td>
            <td>174-32/01-07/40</td>
            <td>04.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36729769" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Территориальный орган Администрации Надымского района Администрация п. Ягельный</td>
            <td>8903036877</td>
            <td>174-35/01-07/45</td>
            <td>03.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36690305" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление  культуры Администрации  Надымского района</td>
            <td>8903017112</td>
            <td>174-15/01-07/49</td>
            <td>03.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36710888" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное учреждение дополнительного образования &quot;Детская школа искусств № 1 города надыма&quot;</td>
            <td>8903021207</td>
            <td>174-1515/01-07/14</td>
            <td>03.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36685611" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное учреждение дополнительного образования детей &quot;Детская школа искусств №2 г. Надыма&quot;</td>
            <td>8903021180</td>
            <td>174-1516/01-07/12</td>
            <td>03.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36684657" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное учреждение культуры &quot;Музей истории и археологии г. Надыма&quot;</td>
            <td>8903021454</td>
            <td>174-1512/01-07/11</td>
            <td>03.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36681182" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное учреждение культуры &quot;Надымская централизованная библиотечная система&quot;</td>
            <td>8903026879</td>
            <td>174-1513/01-07/10</td>
            <td>03.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36688128" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное учреждение культуры &quot;Надымская районная клубная система&quot;</td>
            <td>8903032946</td>
            <td>174-1514/01-07/15</td>
            <td>03.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36700672" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Территориальный орган Администрации Надымского района Администрация поселка Пангоды</td>
            <td>8903036860</td>
            <td>174-30/01-07/44</td>
            <td>28.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36426469" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент муниципального хозяйства Администрации Надымского района</td>
            <td>8903032907</td>
            <td>174-12/01-07/124</td>
            <td>20.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37275853" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное казенное учреждение &quot;Централизованная бухгалтерия Надымского района&quot;</td>
            <td>8903037214</td>
            <td>174-28/01-07/1</td>
            <td>27.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36421527" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное казенное учреждение Служба муниципального заказчика по управлению парком и муниципальным хозяйством</td>
            <td>8903034245</td>
            <td>174-27/01-07/63</td>
            <td>18.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37224895" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление по физической культуре и спорту Администрации  Надымского района</td>
            <td>8903032760</td>
            <td>174-18/01-07/128</td>
            <td>12.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37032842" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное учреждение физической культуры &quot;Центр развития физической культуры и спорта&quot;</td>
            <td>8903036725</td>
            <td>89-174-1811/01-07/22</td>
            <td>19.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37277380" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное учреждение дополнительного образования &quot;Спортивная школа Арктика&quot;</td>
            <td>8903036570</td>
            <td>174-1812/01-07/99</td>
            <td>12.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37042147" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное  автономное  учреждение дополнительного образования &quot;Спортивная школа Арктур&quot;</td>
            <td>8903034189</td>
            <td>174-18/01-07/47</td>
            <td>12.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37051658" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное учреждение дополнительного образования &quot;Спортивная школа Лидер&quot;</td>
            <td>8903021133</td>
            <td>89-174-18/01-06/15</td>
            <td>13.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37065408" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление по делам молодежи и туризму Администрации Надымского района</td>
            <td>8903036891</td>
            <td>174-17/01-07/64</td>
            <td>12.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37029069" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное учреждение &quot;Дом молодежи&quot;</td>
            <td>8903033837</td>
            <td>174-1712/01-07/27</td>
            <td>19.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37279635" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент муниципального имущества Администрации Надымского района</td>
            <td>8903001095</td>
            <td>174-11/01-07/21</td>
            <td>17.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36119196" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципального учреждения &quot;Управление капитального строительства и капитального ремонта&quot;</td>
            <td>8903027978</td>
            <td>174-19/01-07/52</td>
            <td>20.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37297860" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное учреждение муниципального округа Надымский район Ямало-Ненецкого автономного округа &quot;Телерадиокомпания Надым&quot;</td>
            <td>8903036179</td>
            <td>174-22/01-07/53</td>
            <td>12.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38029162" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное учреждение   &quot;Бизнес - инкубатор&quot;</td>
            <td>8903029615</td>
            <td>174-20/01-07/10</td>
            <td>13.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37083201" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-надымский-terr-муниципальное-казенное-учреждение-quot-дирекция-бухгалтерского-и-финансово-экономического-обеспечения-quot" class="dept-checkbox">
    <label for="dept-terr-надымский-terr-муниципальное-казенное-учреждение-quot-дирекция-бухгалтерского-и-финансово-экономического-обеспечения-quot" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">Муниципальное казенное учреждение &quot;Дирекция бухгалтерского и финансово-экономического обеспечения&quot; <span class="org-count">(учреждений: 37)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Департамент образования Администрации Надымского района</td>
            <td>8903008439</td>
            <td>174-13/01-07/1412</td>
            <td>17.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47169381" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное казенное учреждение Дирекция по организационно- хозяйственному и методическому сопровождению</td>
            <td>8903037687</td>
            <td>89-174-39/01-08/130</td>
            <td>17.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47162893" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное казенное учреждение Дирекция бухгалтерского и фининсово – экономического обеспечения</td>
            <td>8903037694</td>
            <td>174-38/01-07/26</td>
            <td>30.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36565924" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное общеобразовательное учреждение &quot;Средняя общеобразовательная школа №1 с углубленным изучением отдельных предметов&quot;</td>
            <td>8903019166</td>
            <td>89-174-1311/01-08/33</td>
            <td>17.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47240609" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное общеобразовательное учреждение &quot;Средняя общеобразовательная школа №2&quot;</td>
            <td>8903020098</td>
            <td>174-11-1312/01-07/236</td>
            <td>17.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47216583" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное общеобразовательное учреждение &quot;Средняя общеобразовательная школа №3&quot;</td>
            <td>8903020073</td>
            <td>174-1313/01-07/319</td>
            <td>17.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47214719" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное общеобразовательное учреждение &quot;Средняя общеобразовательная школа №4&quot;</td>
            <td>8903020059</td>
            <td>174-1314/01-07/331</td>
            <td>18.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47209854" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное общеобразовательное учреждение &quot;Средняя общеобразовательная школа №6 с углубленным изучением отдельных предметов&quot;</td>
            <td>8903020122</td>
            <td>174-1316/01-07/213</td>
            <td>17.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47209631" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное общеобразовательное учреждение &quot;Средняя общеобразовательная школа №9&quot;</td>
            <td>8903019173</td>
            <td>174-1317/01-07/246</td>
            <td>18.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47209219" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное общеобразовательное учреждение &quot;Гимназия г.Надыма&quot;</td>
            <td>8903020108</td>
            <td>174-1318/01-07/152</td>
            <td>17.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47219395" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное общеобразовательное учреждение &quot;Ягельная средняя общеобразовательная школа&quot;</td>
            <td>8903020161</td>
            <td>174-1324/01-07/108</td>
            <td>17.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47194310" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное общеобразовательное учреждение &quot;Приозёрная средняя общеобразовательная школа&quot;</td>
            <td>8903020010</td>
            <td>174-1323/01-07/108</td>
            <td>18.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47199220" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное общеобразовательное учреждение &quot;Норинская начальная общеобразовательная школа&quot;</td>
            <td>8903020147</td>
            <td>174-1327/01-07/25</td>
            <td>17.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47201830" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное общеобразовательное учреждение &quot;Заполярная средняя общеобразовательная школа&quot;</td>
            <td>8903020500</td>
            <td>174-1320/01-07/50</td>
            <td>17.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47183738" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное общеобразовательное учреждение дополнительного образования детей &quot;Центр детского творчества&quot;</td>
            <td>8903020130</td>
            <td>174-1354/01-07/77</td>
            <td>17.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47219985" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное общеобразовательное учреждение дополнительного образования детей &quot;Центр развития творчества детей и юношества &quot;Созвездие&quot;</td>
            <td>8903020027</td>
            <td>89-174-1355/01-08/57</td>
            <td>17.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47208739" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное общеобразовательное учреждение дополнительного образования детей &quot;Детско-юшошеский центр &quot;Альфа&quot;</td>
            <td>8903021447</td>
            <td>174-1356/01-07/157</td>
            <td>17.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47220581" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное общеобразовательное учреждение &quot;Правохеттинская средняя общеобразовательная школа&quot;</td>
            <td>8903020482</td>
            <td>00051</td>
            <td>17.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47200799" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное общеобразовательное учреждение &quot;Школа-интернат среднего общего образования с. Ныда&quot;</td>
            <td>8903020041</td>
            <td>174-1326/01-07/144</td>
            <td>17.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47191617" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное общеобразовательное учреждение &quot;Школа-интернат среднего общего образования п. Кутопьюган &quot;</td>
            <td>8903020154</td>
            <td>7</td>
            <td>18.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47204685" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное общеобразовательное учреждение «Лонгъюганская средняя общеобразовательная школа»</td>
            <td>8903020490</td>
            <td>174-1321/01-07/124</td>
            <td>17.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47203218" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное общеобразовательное учреждение &quot;Средняя общеобразовательная школа №1 п.Пангоды&quot;</td>
            <td>8903020524</td>
            <td>174-1319/01-07/137</td>
            <td>17.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47207908" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное общеобразовательное учреждение &quot;Центр образования&quot;</td>
            <td>8903020517</td>
            <td>174-1353/01-07/198</td>
            <td>17.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47205508" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное дошкольное образовательное учреждение «Детский сад «Ромашка» г. Надыма»</td>
            <td>8903036732</td>
            <td>174-1337/01-07/65</td>
            <td>17.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47134804" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное дошкольное образовательное учреждение &quot;Детский сад &quot;Аленький цветочек&quot; г. Надыма</td>
            <td>8903034333</td>
            <td>174-1328/01-07/44</td>
            <td>17.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47141007" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное дошкольное образовательное учреждение &quot;Детский сад &quot;Медвеженок&quot; г. Надыма&quot;</td>
            <td>8903034870</td>
            <td>174-1334/01-07/107</td>
            <td>17.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47139790" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное дошкольное образовательное учреждение &quot;Детский сад &quot;Солнышко&quot; г. Надыма&quot;</td>
            <td>8903035545</td>
            <td>174-1340/01-07/49</td>
            <td>17.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47138880" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное дошкольное образовательное учреждение &quot;Газовичок&quot;</td>
            <td>8903036161</td>
            <td>174-1331/01-07/47</td>
            <td>17.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47136378" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное дошкольное образовательное учреждение &quot;Детский сад &quot;Мечта&quot; п. Пангоды&quot;</td>
            <td>8903035680</td>
            <td>89-174-1345/01-08/108</td>
            <td>18.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47137543" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное дошкольное образовательное учреждение &quot;Детский сад &quot;Сказка&quot; г. Надыма&quot;</td>
            <td>8903020355</td>
            <td>174-1339/01-07/88</td>
            <td>17.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47145798" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное дошкольное образовательное учреждение &quot;Детский сад &quot;Буратино&quot; г. Надыма&quot;</td>
            <td>8903020436</td>
            <td>174-1330/01-07/55</td>
            <td>17.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47156155" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное дошкольное образовательное учреждение &quot;Детский сад &quot;Ёлочка&quot; г. Надыма&quot;</td>
            <td>8903020370</td>
            <td>00221</td>
            <td>17.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47153381" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное дошкольное образовательное учреждение &quot;Детский сад &quot;Чебурашка&quot; с. Ныда Надымского района&quot;</td>
            <td>8903020429</td>
            <td>89-174-1351/01-08/1</td>
            <td>18.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47154771" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное дошкольное образовательное учреждение &quot;Детский сад &quot;Золотой петушок&quot; п. Пангоды Надымского района&quot;</td>
            <td>8903020450</td>
            <td>174-1343/01-07/57</td>
            <td>17.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47142806" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное дошкольное образовательное учреждение &quot;Детский сад &quot;Родничок&quot; г. Надыма&quot;</td>
            <td>8903031357</td>
            <td>174-1336/01-07/83</td>
            <td>17.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47149032" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное дошкольное образовательное учреждение &quot;Центр развития ребёнка &quot;Детский сад &quot;Умка&quot; г. Надыма&quot;</td>
            <td>8903002162</td>
            <td>174-1342/01-07/131</td>
            <td>17.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47158351" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное дошкольное образовательное учреждение комбинированного вида  &quot;Детский сад &quot;Росинка&quot; г. Надыма&quot;</td>
            <td>8903020387</td>
            <td>89-174-1338/01-08/69</td>
            <td>17.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47148419" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-надымский-terr-организация-не-указана-нет-бу" class="dept-checkbox">
    <label for="dept-terr-надымский-terr-организация-не-указана-нет-бу" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">Организация не указана (нет БУ) <span class="org-count">(учреждений: 2)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Управление социальных программ Администрации Надымского района</td>
            <td>8903017779</td>
            <td>174-16/01-07/112</td>
            <td>18.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37242080" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное казённое учреждение &quot;Управление по содержанию муниципального имущества&quot;</td>
            <td>8903032470</td>
            <td>174-25/01-07/25</td>
            <td>20.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37337504" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

## Новый Уренгой <span class="toc-badge">4</span>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-новый-уренгой-terr-муниципальное-казенное-учреждение-quot-централизованная-бухгалтерия-quot" class="dept-checkbox">
    <label for="dept-terr-новый-уренгой-terr-муниципальное-казенное-учреждение-quot-централизованная-бухгалтерия-quot" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">Муниципальное казенное учреждение &quot;Централизованная бухгалтерия&quot; <span class="org-count">(учреждений: 75 <span class="no-requests">| нет заявок: 4</span>)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>МБОУ СОШ № 1</td>
            <td>8904016506</td>
            <td>89-176-0831/01-06/244</td>
            <td>21.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36231660" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ СШ № 5</td>
            <td>8904031720</td>
            <td>89-176-0835/01-07/292</td>
            <td>21.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36214572" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ СШ № 7</td>
            <td>8904032498</td>
            <td>89-176/0837/01-07/681</td>
            <td>21.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36219923" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ СШ № 8</td>
            <td>8904031631</td>
            <td>176-0838/01-06//4</td>
            <td>24.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36380975" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ СШ № 9</td>
            <td>8904031938</td>
            <td>89-176-0839/01-06/24</td>
            <td>21.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36230331" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ СШ № 11</td>
            <td>8904012195</td>
            <td>89-176-0840/01-07/04</td>
            <td>22.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36246112" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ СОШ № 15</td>
            <td>8904031663</td>
            <td>89-176-0843/01-03/42</td>
            <td>28.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36446837" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ СШ № 16</td>
            <td>8904031864</td>
            <td>89-176-0844/01-06/20</td>
            <td>21.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36218628" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ СШ № 17</td>
            <td>8904057911</td>
            <td>89-176-0845/01-07/16</td>
            <td>23.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36293617" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ СКШ № 18</td>
            <td>8904017193</td>
            <td>176-0847/01-06/14</td>
            <td>22.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36265082" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ СШ им. Д.И. Коротчаева</td>
            <td>8904037432</td>
            <td>89-176-0836/01-06/23</td>
            <td>21.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36222183" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ КСОШ имени Героя РФ В.И. Шарпатова</td>
            <td>8904032025</td>
            <td>89-176-0842/01-07/20</td>
            <td>21.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36226222" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ Детская экологическая станция</td>
            <td>8904033075</td>
            <td>176-0883/01-06/19</td>
            <td>22.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36260608" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ Арктический лицей</td>
            <td>8904032787</td>
            <td>176-0841/01-06/21</td>
            <td>22.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36252302" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ ДС &quot;Снегурочка</td>
            <td>8904057799</td>
            <td>176-0865/01-06/20</td>
            <td>21.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36223865" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ ДС Семицветик</td>
            <td>8904033029</td>
            <td>89-176-0871/01-06/23</td>
            <td>21.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36234569" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ ДС Лада</td>
            <td>8904032716</td>
            <td>176-0858/01-06/23</td>
            <td>22.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36264419" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ ДС Ивушка</td>
            <td>8904032949</td>
            <td>89-176-0862/01-06//27</td>
            <td>23.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36313383" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ ДС Теремок</td>
            <td>8904032000</td>
            <td>89-176-0853/01-08/23</td>
            <td>21.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36229864" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ ДС Огонек</td>
            <td>8904032924</td>
            <td>89-176-0851/01-07/26</td>
            <td>21.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36233864" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ ДС Ёлочка</td>
            <td>8904031889</td>
            <td>89-176-0857/01-07/15</td>
            <td>22.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36280120" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ ДС Северная сказка</td>
            <td>8904033011</td>
            <td>89-176-0867/01-07/10</td>
            <td>21.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36224929" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ ДС Руслан</td>
            <td>8904029287</td>
            <td>176-0852/01-06/25</td>
            <td>22.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36246659" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ ДС Белоснежка</td>
            <td>8904032699</td>
            <td>89-176-0855/01-07/05</td>
            <td>21.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36219659" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАУ ДО МУК Эврика</td>
            <td>8904010254</td>
            <td>176-0878/01-06/19</td>
            <td>21.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36231212" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАОУ СОШ №4</td>
            <td>8904031649</td>
            <td>89-176-0834/01-07/33</td>
            <td>21.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36230827" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАОУ СОШ №3</td>
            <td>8904024666</td>
            <td>176-0833/01-07/1/12</td>
            <td>22.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36231906" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАОУ СШ Перспектива</td>
            <td>8904024480</td>
            <td>89-176-0832/01-07/41</td>
            <td>22.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36244308" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ ДО ГДТ Академия талантов</td>
            <td>8904022796</td>
            <td>89-176-0879/01-07/42</td>
            <td>21.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36230482" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ ЦРР Умка</td>
            <td>8904070944</td>
            <td>89-176-0873/01-06/26</td>
            <td>21.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36238411" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ Мальвина</td>
            <td>8904010215</td>
            <td>89-176-0872/01-06</td>
            <td>21.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36229790" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ ДС Звездочка</td>
            <td>8904031991</td>
            <td>176-0861/01-06/40</td>
            <td>22.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36253621" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ ДС Радуга</td>
            <td>8904057686</td>
            <td>89-176-0864/01-07/15</td>
            <td>22.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36255128" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ ДС Непоседы</td>
            <td>8904076167</td>
            <td>176-0875/01-06-20</td>
            <td>21.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36231013" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ ДС Метелица</td>
            <td>8904057823</td>
            <td>9-176-0863/01-08/18</td>
            <td>21.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36230311" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ ДС Калинка</td>
            <td>8904052335</td>
            <td>89-176-0850/01-06/19</td>
            <td>21.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36252735" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ ДС Ручеек</td>
            <td>8904031906</td>
            <td>89-176-0856/01-07/23</td>
            <td>22.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36255115" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ ДС Оленёнок</td>
            <td>8904031960</td>
            <td>89-176-0869/01-07/04</td>
            <td>21.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36223928" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление организации закупок Администрации города Новый Уренгой</td>
            <td>8904074184</td>
            <td>89-176-14/01-07/318</td>
            <td>03.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=46655937" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное казённое учреждение «Управление муниципального хозяйства»</td>
            <td>8904036823</td>
            <td>176-0231/01-07/962</td>
            <td>18.04.2024</td>
            <td><a href="https://doc.yanao.ru/app/o?u=27301399" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ «Единая дежурно-диспетчерская служба муниципального образования город Новый Уренгой» переименовано МКУ&quot;Служба экстренного реагирования&quot;</td>
            <td>8904038210</td>
            <td>89-176-032/01-07/18</td>
            <td>17.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36124588" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ &quot;Уренгойская городская специализированная компания&quot;</td>
            <td>8904093395</td>
            <td>89-176-0431/01-07/54</td>
            <td>20.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36175245" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ &quot;Городской центр имущественных и жилищных отношений&quot;</td>
            <td>8904067412</td>
            <td>176-0331/01-07/147</td>
            <td>04.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36723701" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Контрольно-счётная палата Нового Уренгоя</td>
            <td>8904067846</td>
            <td>89-176-2/01-07/54</td>
            <td>17.04.2024</td>
            <td><a href="https://doc.yanao.ru/app/o?u=27227678" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент строительства и жилищно-коммунального комплекса Администрации города Новый Уренгой</td>
            <td>8904067613</td>
            <td>89-176-02/01-07/711</td>
            <td>24.04.2024</td>
            <td><a href="https://doc.yanao.ru/app/o?u=27477984" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент образования Администрации города Новый Уренгой</td>
            <td>8904009795</td>
            <td>89-176-08/01-06/255</td>
            <td>21.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36222897" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент имущественных и жилищных отношений Администрации города Новый Уренгой</td>
            <td>8904013329</td>
            <td>176-03/01-07/431</td>
            <td>05.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36734300" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Городская Дума муниципального образования город Новый Уренгой</td>
            <td>8904055142</td>
            <td>89-176-1/01-07/90</td>
            <td>17.04.2024</td>
            <td><a href="https://doc.yanao.ru/app/o?u=27246807" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Администрация города Новый Уренгой</td>
            <td>8904028004</td>
            <td>89-176/02-07/666</td>
            <td>25.04.2024</td>
            <td><a href="https://doc.yanao.ru/app/o?u=27493003" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент городского хозяйства и жизнеобеспечения районов лимбяяха и коротчаево администрации города новый уренгой</td>
            <td>8904095804</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>МАУ МПМЦ &quot;ШКОЛА ЯМОЛОД. НОВЫЙ УРЕНГОЙ&quot;</td>
            <td>8904039380</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Муниципальное казенное учреждение &quot;дирекция по обеспечению деятельности органов местного самоуправления&quot;</td>
            <td>8904096050</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Управление физической культуры и спорта администрации города новый уренгой</td>
            <td>8904095811</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Департамент финансов Администрации города Новый Уренгой</td>
            <td>8904012702</td>
            <td>89-176/09-07/83-04</td>
            <td>08.02.2024</td>
            <td><a href="https://doc.yanao.ru/app/o?u=24816130" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент культуры, молодежной политики, физической культуры и спорта Администрации города Новый Уренгой</td>
            <td>8904091408</td>
            <td>89-176-07/01-07/604</td>
            <td>01.04.2024</td>
            <td><a href="https://doc.yanao.ru/app/o?u=26246978" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное казенное учреждение &quot;Централизованная бухгалтерия&quot;</td>
            <td>8904070694</td>
            <td>89-176-0431/01-07/123</td>
            <td>01.02.2024</td>
            <td><a href="https://doc.yanao.ru/app/o?u=24526738" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное казенное учреждение &quot;Центр финансово-хозяйственного обеспечения деятельности учреждений муниципальной системы образования&quot;</td>
            <td>8904067814</td>
            <td>176-0885/01-06/01/327</td>
            <td>26.02.2024</td>
            <td><a href="https://doc.yanao.ru/app/o?u=25387364" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное учреждение дополнительного образования спортивная школа &quot;Сибирские медведи&quot;</td>
            <td>8904040805</td>
            <td>89-176-0743/01-07/171</td>
            <td>22.02.2024</td>
            <td><a href="https://doc.yanao.ru/app/o?u=25297214" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное учреждение дополнительного образования Детская школа искусств № 3 город Новый Уренгой</td>
            <td>8904037577</td>
            <td>89-176-0733/01-07/135</td>
            <td>27.02.2024</td>
            <td><a href="https://doc.yanao.ru/app/o?u=25440502" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное учреждение дополнительного образования &quot;Детская школа искусств имени С.В. Рахманинова&quot; город Новый Уренгой</td>
            <td>8904037552</td>
            <td>89-176-0731/01-07/66</td>
            <td>20.02.2024</td>
            <td><a href="https://doc.yanao.ru/app/o?u=25237558" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное учреждение культуры Централизованная клубная система</td>
            <td>8904042182</td>
            <td>89-176-0735/01-07/224</td>
            <td>21.02.2024</td>
            <td><a href="https://doc.yanao.ru/app/o?u=25291178" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное учреждение культуры Централизованная библиотечная система</td>
            <td>8904041830</td>
            <td>00001</td>
            <td>05.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42513645" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное учреждение культуры Центр культуры и досуга “Магистраль” город Новый Уренгой</td>
            <td>8904041735</td>
            <td>89-176-0737/01-07/8</td>
            <td>21.02.2024</td>
            <td><a href="https://doc.yanao.ru/app/o?u=25253883" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное учреждение дополнительного образования спортивная школа “Норд”</td>
            <td>8904050391</td>
            <td>89-176-0746/01-07/63</td>
            <td>21.02.2024</td>
            <td><a href="https://doc.yanao.ru/app/o?u=25299453" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное учреждение “Центр развития физической культуры и спорта”</td>
            <td>8904039662</td>
            <td>89-176-0741/01-07/146</td>
            <td>20.02.2024</td>
            <td><a href="https://doc.yanao.ru/app/o?u=25234132" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное учреждение “Дворец спорта “Звездный”</td>
            <td>8904082403</td>
            <td>89-176-0742/01-07/90</td>
            <td>26.02.2024</td>
            <td><a href="https://doc.yanao.ru/app/o?u=25347004" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное учреждение дополнительного образования спортивная школа «Арктика»</td>
            <td>8904087916</td>
            <td>176-0745/01-06/195</td>
            <td>04.03.2024</td>
            <td><a href="https://doc.yanao.ru/app/o?u=25450177" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное  дошкольное образовательное учреждение  «Детский  сад  «Загадка»</td>
            <td>8904031487</td>
            <td>89-176-0860/01-07/35</td>
            <td>28.02.2024</td>
            <td><a href="https://doc.yanao.ru/app/o?u=25479621" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное общеобразовательное учреждение прогимназия “Центр детства”</td>
            <td>8904032106</td>
            <td>89-176/01-07/79</td>
            <td>28.02.2024</td>
            <td><a href="https://doc.yanao.ru/app/o?u=25492773" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное дошкольное образовательное учреждение &quot;Детский сад &quot;Виниклюзия&quot;</td>
            <td>8904089092</td>
            <td>176-0877/01-06/113</td>
            <td>29.02.2024</td>
            <td><a href="https://doc.yanao.ru/app/o?u=25557225" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное дошкольное образовательное учреждение «Детский сад «Журавушка»</td>
            <td>8904057679</td>
            <td>89-176-0848/01-07/50</td>
            <td>29.02.2024</td>
            <td><a href="https://doc.yanao.ru/app/o?u=25562761" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное общеобразовательное учреждение Гимназия</td>
            <td>8904009668</td>
            <td>89-176-0846/07-07/103</td>
            <td>01.03.2024</td>
            <td><a href="https://doc.yanao.ru/app/o?u=25592263" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное учреждение дополнительного образования «Спортивная школа имени К. Еременко»</td>
            <td>8904046589</td>
            <td>89-176-0744/01-07/239</td>
            <td>27.02.2024</td>
            <td><a href="https://doc.yanao.ru/app/o?u=25434966" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное учреждение дополнительного образования спортивная школа &quot;Контакт&quot;</td>
            <td>8904032970</td>
            <td>89-176-0748/01-07/127 89-176-0748/01-07/128</td>
            <td>26.02.2024</td>
            <td><a href="https://doc.yanao.ru/app/o?u=25313248" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное учреждение дополнительного образования спортивная школа &quot;Юность&quot;</td>
            <td>8904010695</td>
            <td>89-176-0747/01-06/105</td>
            <td>21.02.2024</td>
            <td><a href="https://doc.yanao.ru/app/o?u=25244199" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-новый-уренгой-terr-организация-не-указана-нет-бу" class="dept-checkbox">
    <label for="dept-terr-новый-уренгой-terr-организация-не-указана-нет-бу" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">Организация не указана (нет БУ) <span class="org-count">(учреждений: 8)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Управление по труду и социальной защите населения Администрации города Новый Уренгой</td>
            <td>8904093807</td>
            <td>89-176-10/01-07/2050</td>
            <td>27.12.2024</td>
            <td><a href="https://doc.yanao.ru/app/o?u=35659472" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ ДС Цветок Уренгоя</td>
            <td>8904031896</td>
            <td>89-176-0870/01-06/21</td>
            <td>22.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36262757" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное дошкольное образовательное учреждение &quot;Детский сад &quot;Гнёздышко&quot;</td>
            <td>8904057693</td>
            <td>89-176-0859/01-07/68</td>
            <td>27.02.2024</td>
            <td><a href="https://doc.yanao.ru/app/o?u=25432208" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное дошкольное образовательное учреждение &quot;Детский сад &quot;Золотой петушок&quot;</td>
            <td>8904032811</td>
            <td>54</td>
            <td>27.02.2024</td>
            <td><a href="https://doc.yanao.ru/app/o?u=25434849" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ ДС Берёзка</td>
            <td>8904045680</td>
            <td>89-176-0874/01-07/14</td>
            <td>22.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36257848" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАУ Информационное агентство Импульс Севера</td>
            <td>8904011924</td>
            <td>89-176-031/01-06/41</td>
            <td>22.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36251758" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ «Финансово-бюджетное управление сферы образования»</td>
            <td>8904077763</td>
            <td>176-0886/01-06/07</td>
            <td>21.01.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36222759" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное учреждение дополнительного образования Детская школа искусств №2 город Новый Уренгой</td>
            <td>8904037560</td>
            <td>176-0732/01-06/170</td>
            <td>21.02.2024</td>
            <td><a href="https://doc.yanao.ru/app/o?u=25260137" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

## Ноябрьск

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-ноябрьск-terr-муниципальное-казенное-учреждение-quot-централизованная-бухгалтерия-органов-местного-самоуправления-и-муниципальных-учреждений-города-ноябрьска-quot" class="dept-checkbox">
    <label for="dept-terr-ноябрьск-terr-муниципальное-казенное-учреждение-quot-централизованная-бухгалтерия-органов-местного-самоуправления-и-муниципальных-учреждений-города-ноябрьска-quot" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">Муниципальное казенное учреждение &quot;Централизованная бухгалтерия органов местного самоуправления и муниципальных учреждений города Ноябрьска&quot; <span class="org-count">(учреждений: 10)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Администрация города Ноябрьска</td>
            <td>8905001855</td>
            <td>89-178-1/101-07/2609</td>
            <td>25.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39584299" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент финансов Администрации города Ноябрьска</td>
            <td>8905020167</td>
            <td>89-178-1/01-07/1090</td>
            <td>22.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39491562" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Дума города Ноябрьска</td>
            <td>8905033078</td>
            <td>89-178-2/01-18-01/232</td>
            <td>24.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39587179" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент имущественных отношений Администрации города Ноябрьска</td>
            <td>8905017830</td>
            <td>89-178-1/02-12/6511</td>
            <td>24.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39557150" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ &quot;ЕДДС &quot; МО г. Ноябрьск</td>
            <td>8905052761</td>
            <td>89-178-1/02-12/6511</td>
            <td>24.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39557150" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>НТИА &quot;МИГ&quot;</td>
            <td>8905002305</td>
            <td>89-178-10125/10125-06/405</td>
            <td>25.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39609648" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ &quot;ЦРП&quot;Бизнесинергия&quot; МО г.Ноябрьск</td>
            <td>8905050926</td>
            <td>00023</td>
            <td>28.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39669324" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление жилищно-коммунального хозяйства, транспорта, энергетики и связи г.Ноябрьск</td>
            <td>8905048846</td>
            <td>89-178-1/106-02/1541</td>
            <td>23.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39520313" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МУ&quot;Дирекция муниципального заказа&quot;</td>
            <td>8905027532</td>
            <td>78-10121/10121-08/2522</td>
            <td>23.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39541187" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ &quot;Централизованная бухгалтерия органов местного самоуправления и муниципальных учреждений города Ноябрьска&quot;</td>
            <td>8905070182</td>
            <td>89-178-1/01-21/1</td>
            <td>-</td>
            <td>-</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-ноябрьск-terr-организация-не-указана-нет-бу" class="dept-checkbox">
    <label for="dept-terr-ноябрьск-terr-организация-не-указана-нет-бу" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">Организация не указана (нет БУ) <span class="org-count">(учреждений: 7)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Счетная палата города Ноябрьск</td>
            <td>8905043132</td>
            <td>300-02-07-01625</td>
            <td>26.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=43048479" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление социальной защиты населения Администрации города Ноябрьска</td>
            <td>8905017904</td>
            <td>89-178-1/05-07/5798</td>
            <td>22.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42978887" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ &quot;Управление городского хозяйства&quot; г. Ноябрьск</td>
            <td>8905067285</td>
            <td>178-10621/10621-04/407</td>
            <td>24.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39555811" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ «Централизованное обслуживание муниципальных учреждений в сфере молодежной политики Администрации города Ноябрьска»</td>
            <td>8905057456</td>
            <td>89-178-0721/0721-07/96</td>
            <td>11.06.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40996521" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ «Ресурсный центр добровольчества и патриотического воспитания «Кадет»</td>
            <td>8905028127</td>
            <td>89-178-0725/0725/381</td>
            <td>16.06.2025</td>
            <td>-</td>
          </tr>
          <tr>
            <td>МБУ «Многофункциональный центр по работе с семьей и молодежью «Доверие»</td>
            <td>8905028783</td>
            <td>89-178-0723/0723-07/379</td>
            <td>10.06.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40956284" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАУ «Центр туризма и отдыха»</td>
            <td>8905028078</td>
            <td>89-178-0722/0722-07/417</td>
            <td>25.06.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=41358701" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-ноябрьск-terr-муниципальное-казенное-учреждение-quot-финансовая-дирекция-муниципальных-учреждений-спорта-и-молодежной-политики-quot" class="dept-checkbox">
    <label for="dept-terr-ноябрьск-terr-муниципальное-казенное-учреждение-quot-финансовая-дирекция-муниципальных-учреждений-спорта-и-молодежной-политики-quot" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">Муниципальное казенное учреждение &quot;финансовая дирекция муниципальных учреждений спорта и молодежной политики&quot; <span class="org-count">(учреждений: 11)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Управление  молодежной политики Администрации города Ноябрьска</td>
            <td>8905018351</td>
            <td>89-178-07/07-07/1187</td>
            <td>11.06.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40997531" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАУ «Арт-резиденция «Миксер»</td>
            <td>8905028293</td>
            <td>89-178-0726/0726-07/686</td>
            <td>17.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42038666" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ  «Централизованное обслуживание муниципальных учреждений сферы физической  культуры и спорта Администрации города Ноябрьска»</td>
            <td>8905057618</td>
            <td>89-178-0821/01-07/80</td>
            <td>07.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39915277" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ дополнительного образования «Спортивная школа олимпийского  резерва «Альтис»</td>
            <td>8905026666</td>
            <td>89-178-0822/01-07/174</td>
            <td>13.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40024116" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ дополнительного образования «Спортивная школа олимпийского  резерва «Арктика»</td>
            <td>8905019250</td>
            <td>89-178-0823/01-07/131</td>
            <td>13.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40022637" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ дополнительного образования «Спортивная школа «Авангард»</td>
            <td>8905027469</td>
            <td>89-178-0825/01-08/140</td>
            <td>13.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40021951" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ дополнительного образования «Спортивная школа «Олимпиец»</td>
            <td>8905021315</td>
            <td>89-178-0824/01-07/170</td>
            <td>14.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40064219" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАУ «Физкультурно-оздоровительный комплекс Здоровье»</td>
            <td>8905028617</td>
            <td>178-0826/01-07/117</td>
            <td>12.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39986558" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАУ «Центр спортивных мероприятий и физкультурно-массовой  работы»</td>
            <td>8905027420</td>
            <td>89-178-0828/01-07/432</td>
            <td>12.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39992519" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАУ «Спортивно-оздоровительный комплекс «Зенит»</td>
            <td>8905052472</td>
            <td>89-178-0827/01-07/313</td>
            <td>12.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40000133" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление по физической культуре и спорту Администрации города  Ноябрьска</td>
            <td>8905017855</td>
            <td>89-178-08/01-07/893</td>
            <td>07.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39915475" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-ноябрьск-terr-мку-quot-централизованное-обслуживание-муниципальных-учреждений-в-сфере-культуры-администрации-города-ноябрьска-quot" class="dept-checkbox">
    <label for="dept-terr-ноябрьск-terr-мку-quot-централизованное-обслуживание-муниципальных-учреждений-в-сфере-культуры-администрации-города-ноябрьска-quot" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">МКУ &quot;Централизованное обслуживание муниципальных учреждений в сфере культуры Администрации города Ноябрьска&quot; <span class="org-count">(учреждений: 9)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>МКУ &quot;Централизованное обслуживание муниципальных учреждений в сфере культуры Администрации города Ноябрьска&quot;</td>
            <td>8905057505</td>
            <td>89-178-0621/0621-07/69</td>
            <td>10.06.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40963496" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление культуры Администрации города Ноябрьска</td>
            <td>8905001862</td>
            <td>89-178-06/06-08/540</td>
            <td>11.06.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40965909" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ ДО  ДМШ 2 им. В.А. Коха</td>
            <td>8905021650</td>
            <td>89-178-0622/0622-07/191</td>
            <td>24.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39566285" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАУ ДО ДШИ им.П.И. Чайковского</td>
            <td>8905021629</td>
            <td>89-178-0628/0628-07/524</td>
            <td>01.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=41318107" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ культуры «Музейный ресурсный  центр» муниципального образования город Ноябрьск»</td>
            <td>8905029385</td>
            <td>89-178-0624/0634-07/371</td>
            <td>20.06.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=41227561" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ  культуры «Центр досуга  «Нефтяник» муниципального образования город Ноябрьск</td>
            <td>8905027821</td>
            <td>89-178-0627/0627-07/532</td>
            <td>29.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40234573" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ  культуры Городской Дворец  культуры и кино «Русь»</td>
            <td>8905021675</td>
            <td>89-178-0625/0625-07/294</td>
            <td>21.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39721996" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАУК  культуры «Централизованная  библиотечная система» муниципального образования город Ноябрьск</td>
            <td>8905028060</td>
            <td>89-178-0623/0623-08/200</td>
            <td>23.06.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=41295378" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ культуры «КСК «Ямал»</td>
            <td>8905027620</td>
            <td>89-178-0626/0626-07/219</td>
            <td>11.06.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40975279" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-ноябрьск-terr-мку-централизованное-обслуживание-муниципальных-учреждений-системы-образования-администрации-города-ноябрьск" class="dept-checkbox">
    <label for="dept-terr-ноябрьск-terr-мку-централизованное-обслуживание-муниципальных-учреждений-системы-образования-администрации-города-ноябрьск" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">МКУ «Централизованное обслуживание муниципальных учреждений системы образования Администрации города Ноябрьск» <span class="org-count">(учреждений: 48)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Муниципальное  казенное учреждение «Централизованное обслуживание муниципальных учреждений  системы образования Администрации города Ноябрьск»</td>
            <td>8905057544</td>
            <td>89-178-0321/0321-08/185</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42423123" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Депапртамент образования администрации города Ноябрьск</td>
            <td>8905002087</td>
            <td>89-178-1/03-07/4108</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42420832" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ &quot;Аленький цветочек&quot;</td>
            <td>8905023908</td>
            <td>89-178-0356/0356-07/57</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42426022" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ &quot;Белоснежка&quot;</td>
            <td>8905024884</td>
            <td>89-178-0362/0362-07-00071</td>
            <td>05.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42505757" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ &quot;Волошка&quot;</td>
            <td>8905025359</td>
            <td>178-0357/0357-08/16</td>
            <td>04.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42439467" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ &quot;Гимназия №1&quot;</td>
            <td>8905017809</td>
            <td>89-178-0322/0322-07-00123</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42419642" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ &quot;ДД &quot;Семья&quot;</td>
            <td>8905001936</td>
            <td>89-178-0339/0339-07/315</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42433061" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ &quot;Дюймовочка&quot;</td>
            <td>8905065552</td>
            <td>89-178-0366/0366-07/29</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42421747" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ &quot;Золотой ключик&quot;</td>
            <td>8905026627</td>
            <td>89-178-0351/0351-07/95</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42416022" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ &quot;Золотая рыбка&quot;</td>
            <td>8905024620</td>
            <td>89-178-0340/0340-07/58</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42419571" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ &quot;Золушка&quot;</td>
            <td>8905026835</td>
            <td>89-178-0341/0341-07/62</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42425718" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАОУ ДО &quot;Детский технопак &quot;КВАНТОРИУМ&quot;</td>
            <td>8905068553</td>
            <td>89-178-0369/0369-07-00055</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42430820" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ &quot;Колобок&quot;</td>
            <td>8905025239</td>
            <td>89-178-0345/0345-07/60</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42421194" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ &quot;Колокольчик&quot;</td>
            <td>8905024718</td>
            <td>89-178-0349/0349-07/56</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42434117" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ &quot;Крепыш&quot;</td>
            <td>8905026465</td>
            <td>89-178-0363/0363-07/68</td>
            <td>31.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42399954" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ &quot;Ласточка&quot;</td>
            <td>8905024891</td>
            <td>178-0352/0352-08/69</td>
            <td>31.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42401738" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ &quot;Лукоморье&quot;</td>
            <td>8905024122</td>
            <td>89-178-0350/0350-07/31</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42436004" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ &quot;Лучик&quot;</td>
            <td>8905067630</td>
            <td>89-178-0344/0344-08/59</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42421635" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ &quot;Малыш&quot;</td>
            <td>8905035484</td>
            <td>89-178-0364/0364-07/52</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42415425" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ &quot;Мальвина&quot;</td>
            <td>8905024676</td>
            <td>89-178-0348/0348-07/53-ДСП</td>
            <td>05.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42501760" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАОУ СОШ № 2 УИИЯ</td>
            <td>8905020128</td>
            <td>89-178-0323/0323-07/207</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42422739" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ &quot;Машенька&quot;</td>
            <td>8905024877</td>
            <td>89-178-0368/0368-07-00008</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42415771" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ СОШ мкр. Вынгапуровский</td>
            <td>8905017862</td>
            <td>89-178-0334/0334-07/92</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42418291" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ &quot;СОШ №10 С УИФИТД&quot;</td>
            <td>8905020390</td>
            <td>89-178-0330/0330-08/335</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42418974" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ &quot;СОШ №12&quot;</td>
            <td>8905017774</td>
            <td>89-178-0331/0331-07/181</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42428487" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ &quot;СОШ №13 С УИП ЭСТЕТИЧЕСКОГО ЦИКЛА&quot;</td>
            <td>8905020030</td>
            <td>89-178/0332/0332-07/112</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42420781" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ СОШ №14</td>
            <td>8905003740</td>
            <td>89-178-0333/0333-07/223</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42418952" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ СОШ №3</td>
            <td>8905017742</td>
            <td>89-178-0324/0324-07/199</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42425282" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ СОШ №5</td>
            <td>8905019965</td>
            <td>89-178-0325/0325-07/580</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42414294" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ СОШ №6</td>
            <td>8905002111</td>
            <td>89-178-0326/0326-07/148</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42423419" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ СОШ №7</td>
            <td>8905018947</td>
            <td>89-178-0327/0327-07/454</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42432130" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ СОШ №8</td>
            <td>8905002560</td>
            <td>89-178-0328/0328-07/458</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42422815" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ СОШ №9</td>
            <td>8905017799</td>
            <td>89-178-0329/0329-07/245</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42431590" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ &quot;Морозко&quot;</td>
            <td>8905065545</td>
            <td>89-178-0365/0365-07/34</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42427343" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ &quot;Надежда&quot;</td>
            <td>8905029949</td>
            <td>89-178-0342/0342-07/55</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42416789" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ &quot;Ромашка&quot;</td>
            <td>8905025180</td>
            <td>89-0353/0353-07/18</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42422021" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ &quot;Росинка&quot;</td>
            <td>8905024852</td>
            <td>178-0343/0343-08/27</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42433100" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ &quot;Ручеек&quot;</td>
            <td>8905023785</td>
            <td>89-178-0355/0355-07/39</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42428435" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ &quot;Синеглазка&quot;</td>
            <td>8905023898</td>
            <td>89-178-0346/0346-07/64</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42425777" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ &quot;Сказка&quot;</td>
            <td>8905057671</td>
            <td>89-178-0367/0367-07/52</td>
            <td>31.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42397489" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКОУ &quot;С(К)ОШ&quot;</td>
            <td>8905017848</td>
            <td>89-178-0335/0335-08/63</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42438651" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ &quot;Снегурочка&quot;</td>
            <td>8905024820</td>
            <td>89-178-0359/0359-07-00132</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42416994" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ &quot;Теремок&quot;</td>
            <td>8905026754</td>
            <td>89-178-0361/0361-07/32</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42429307" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ &quot;Улыбка&quot;</td>
            <td>8905023859</td>
            <td>178-0358/0358-08/46</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42420993" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАДОУ &quot;Умка&quot;</td>
            <td>8905030574</td>
            <td>89-178-0347/0347-07/74</td>
            <td>31.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42399150" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУДО &quot;ЦДТ&quot;</td>
            <td>8905027148</td>
            <td>89-178-0337/0337-08/1/60</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42440673" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУДО ЦЕНТР ЮВЕНТА</td>
            <td>8905027170</td>
            <td>89-178-0338/0338-07/129</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42417681" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ &quot;Ягодка&quot;</td>
            <td>8905026722</td>
            <td>89-178-0354/0354-07/53</td>
            <td>01.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42413986" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

## Пуровский район

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-пуровский-район-terr-мку-quot-централизованная-бухгалтерия-органов-местного-самоуправления-пуровского-района-quot" class="dept-checkbox">
    <label for="dept-terr-пуровский-район-terr-мку-quot-централизованная-бухгалтерия-органов-местного-самоуправления-пуровского-района-quot" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">МКУ &quot;Централизованная бухгалтерия органов местного самоуправления Пуровского района&quot; <span class="org-count">(учреждений: 12)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>МКУ Централизованная бухгалтерия органов местного самоуправления Пуровского района</td>
            <td>8911033728</td>
            <td>89-160/255101-07/1</td>
            <td>03.12.2024</td>
            <td><a href="https://doc.yanao.ru/app/o?u=34601763" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент имущественных и земельных отношений Пуровского  района</td>
            <td>8911004036</td>
            <td>89-160/2701-07/472</td>
            <td>10.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36954337" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление молодежной политики Администрации Пуровского района</td>
            <td>8911020574</td>
            <td>305101-06/36</td>
            <td>12.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37044613" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Администрация  поселка городского типа Уренгой</td>
            <td>8911031576</td>
            <td>89-160/4101-07/413</td>
            <td>17.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38162094" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Администрация села Самбург</td>
            <td>8911031600</td>
            <td>89 160/4001 07/288</td>
            <td>17.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38164942" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Администрация поселка Ханымей</td>
            <td>8911031590</td>
            <td>89-160/4201-06/113</td>
            <td>16.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39260283" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент финансов и казначейства Администрации Пуровского района</td>
            <td>8911018590</td>
            <td>89-160/2501-07/718</td>
            <td>11.09.2024</td>
            <td><a href="https://doc.yanao.ru/app/o?u=31759713" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент строительства, архитектуры и жилищной политики Администрации Пуровского района</td>
            <td>8911026248</td>
            <td>89-160/2801-07/490</td>
            <td>12.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38026820" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент транспорта, связи и систем жизнеобеспечения Администрации Пуровского района</td>
            <td>8911018720</td>
            <td>89-160/2901-07/3045</td>
            <td>11.09.2024</td>
            <td><a href="https://doc.yanao.ru/app/o?u=31755631" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Администрация Пуровского района</td>
            <td>8911003762</td>
            <td>89-160/001-07/151</td>
            <td>07.05.2026</td>
            <td><a href="https://doc.yanao.ru/app/o?u=52270113э" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Дума Пуровского района</td>
            <td>8911021480</td>
            <td>89-160/101-07/309</td>
            <td>29.06.2026</td>
            <td><a href="https://doc.yanao.ru/app/o?u=54015535" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Контрольно-счетная палата Пуровского района</td>
            <td>8911026270</td>
            <td>01-07/266</td>
            <td>30.06.2026</td>
            <td><a href="https://doc.yanao.ru/app/o?u=54069247" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-пуровский-район-terr-организация-не-указана-нет-бу" class="dept-checkbox">
    <label for="dept-terr-пуровский-район-terr-организация-не-указана-нет-бу" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">Организация не указана (нет БУ) <span class="org-count">(учреждений: 9)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>МКУ  &quot;Дирекция по обслуживанию деятельности органов местного самоуправления  Пуровского района&quot;</td>
            <td>8911023769</td>
            <td>89-160/4101-07/69</td>
            <td>13.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37119082" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ &quot;Управление городского хозяйства&quot; г.Тарко Сале</td>
            <td>8911024650</td>
            <td>89-160/295001-07/134</td>
            <td>03.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36671659" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное учреждение &quot;Управление базой  отдыха &quot;ЭЛЛАДА&quot;</td>
            <td>2355015000</td>
            <td>89-160/3554-01-07/22</td>
            <td>13.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37109671" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАУ &quot;Районный ресурсный молодежный центр&quot;</td>
            <td>8911026985</td>
            <td>305101-06/36</td>
            <td>12.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37044613" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное казенное учреждение «Уренгойское хозяйство»</td>
            <td>8911010907</td>
            <td>38/УХ</td>
            <td>17.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38159883" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ &quot;Комитет по строительству и архитектуре Пуровского  района&quot;</td>
            <td>8911014080</td>
            <td>89-160/285001-07/343</td>
            <td>10.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37949750" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление социальной политики Администрации Пуровского района  (ДЕПАРТАМЕНТ ПО ТРУДУ И СОЦИАЛЬНОЙ ЗАЩИТЕ НАСЕЛЕНИЯ АДМИНИСТРАЦИИ ПУРОВСКОГО  РАЙОНА)</td>
            <td>8911018670</td>
            <td>89-160/3001-07/898</td>
            <td>10.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39075160" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное казенное учреждение «Управление муниципального  хозяйства и обеспечения деятельности органов местного самоуправления»</td>
            <td>8911030484</td>
            <td>01-14/131</td>
            <td>16.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39276222" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное казённое учреждение «Единая дежурно-диспетчерская служба Пуровского района»</td>
            <td>8911028252</td>
            <td>89-160/4601-06/28</td>
            <td>03.10.2024</td>
            <td><a href="https://doc.yanao.ru/app/o?u=32468760" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-пуровский-район-terr-мку-quot-централизованная-бухгалтерия-по-физической-культуре-и-спорту-администрации-пуровского-района-quot" class="dept-checkbox">
    <label for="dept-terr-пуровский-район-terr-мку-quot-централизованная-бухгалтерия-по-физической-культуре-и-спорту-администрации-пуровского-района-quot" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">МКУ &quot;Централизованная бухгалтерия по физической культуре и спорту Администрации Пуровского района&quot; <span class="org-count">(учреждений: 7)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>МКУ  &quot;Централизованная бухгалтерия по физической культуре и спорту  Администрации Пуровского района&quot;</td>
            <td>8911031745</td>
            <td>305101-06/36</td>
            <td>12.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37044613" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление по физической культуре и спорту Администрации  Пуровского района</td>
            <td>8911006587</td>
            <td>305101-06/36</td>
            <td>12.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37044613" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МАУ ДО Пуровская районная спортивная школа олимпийского резерва «Авангард»</td>
            <td>8911017821</td>
            <td>305101-06/36</td>
            <td>12.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37044613" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ ДО Пуровская районная спортивная школа «Виктория»</td>
            <td>8911017571</td>
            <td>305101-06/36</td>
            <td>12.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37044613" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ ДО спортивная школа «Геолог»</td>
            <td>8911019836</td>
            <td>305101-06/36</td>
            <td>12.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37044613" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ ДО спортивная  школа &quot;Геолог&quot; город Тарко-Сале</td>
            <td>8911024610</td>
            <td>305101-06/36</td>
            <td>12.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37044613" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ ДО спортивная школа «Хыльмик</td>
            <td>8911019410</td>
            <td>305101-06/36</td>
            <td>12.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37044613" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-пуровский-район-terr-мку-центр-бухгалтерского-и-технического-обслуживания-управления-культуры-администрации-пуровского-района" class="dept-checkbox">
    <label for="dept-terr-пуровский-район-terr-мку-центр-бухгалтерского-и-технического-обслуживания-управления-культуры-администрации-пуровского-района" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">МКУ «Центр бухгалтерского и технического обслуживания Управления культуры Администрации Пуровского района» <span class="org-count">(учреждений: 8)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>МКУ «Центр бухгалтерского и технического обслуживания  Управления культуры Администрации Пуровского района»</td>
            <td>8911026343</td>
            <td>345101-07/17</td>
            <td>03.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=36707201" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление культуры Администрации Пуровского района</td>
            <td>8911010054</td>
            <td>345101-07/40</td>
            <td>28.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37573707" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ ДО  «Детская школа искусств им.И.О.Дунаевского»</td>
            <td>8911012830</td>
            <td>345101-07/40</td>
            <td>28.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37573707" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ ДО  «Уренгойская детская школа искусств»</td>
            <td>8911019642</td>
            <td>345101-07/40</td>
            <td>28.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37573707" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ культуры «Пуровский районный  историко-краеведческий музей»</td>
            <td>8911017719</td>
            <td>345101-07/40</td>
            <td>28.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37573707" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ  культуры «Пуровский районный  цент национальных культур»</td>
            <td>8911017003</td>
            <td>345101-07/40</td>
            <td>28.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37573707" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ  культуры «Централизованная  библиотечная система муниципального образования Пуровский район»</td>
            <td>8911023222</td>
            <td>345101-07/40</td>
            <td>28.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37573707" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ культуры «Централизованная  клубная система Пуровского района»</td>
            <td>8911012608</td>
            <td>345101-07/40</td>
            <td>28.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37573707" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-пуровский-район-terr-мку-quot-централизованная-бухгалтерия-департамента-образования-администрации-пуровского-района-quot" class="dept-checkbox">
    <label for="dept-terr-пуровский-район-terr-мку-quot-централизованная-бухгалтерия-департамента-образования-администрации-пуровского-района-quot" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">МКУ &quot;Централизованная бухгалтерия Департамента образования Администрации Пуровского района&quot; <span class="org-count">(учреждений: 27)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>МКУ  &quot;Централизованная бухгалтерия Департамента образования Администрации  Пуровского района&quot;</td>
            <td>8911026336</td>
            <td>89-160/3251-01-07/189</td>
            <td>28.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38600267" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент  образования Администрации Пуровского района»</td>
            <td>8911014010</td>
            <td>89-160/3201-07/958</td>
            <td>28.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38600334" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное  казенное учреждение &quot;Центр методического и ресурсного обеспечения  системы образования Пуровского района&quot;</td>
            <td>8911021120</td>
            <td>89-160/3252-01-07/356</td>
            <td>27.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38559942" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное  бюджетное дошкольное образовательное учреждение «Детский сад «Золотой ключик»  г. Тарко-Сале</td>
            <td>8911015630</td>
            <td>89-160/3273-01-07/72</td>
            <td>26.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38501472" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное  бюджетное общеобразовательное учреждение «Школа-интернат среднего общего  образования» г. Тарко-Сале</td>
            <td>8911013746</td>
            <td>89-160/3257-01-08/118</td>
            <td>26.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38513381" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное  бюджетное общеобразовательное учреждение «Школа-интернат основного общего  образования» с. Халясавэй</td>
            <td>8911013601</td>
            <td>89-160/3265-01-07/9</td>
            <td>27.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38576403" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное  бюджетное общеобразовательное учреждение «Школа-интернат основного общего  образования» д. Харампур Пуровского района</td>
            <td>8911019459</td>
            <td>89-160/3266-01-08/118</td>
            <td>25.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38485591" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное  бюджетное дошкольное образовательное учреждение «Детский сад «Сказка» п.г.т.  Уренгой Пуровского района</td>
            <td>8911017290</td>
            <td>00046</td>
            <td>27.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38559124" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Средняя    общеобразовательная школа № 6  С.  СЫВДАРМА</td>
            <td>8911013591</td>
            <td>89-160/3259-01-07/81</td>
            <td>27.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38563946" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное  бюджетное общеобразовательное учреждение «Средняя общеобразовательная школа №  2» г. Тарко-Сале Пуровского района</td>
            <td>8911013714</td>
            <td>89-160/3255-01-07/151</td>
            <td>26.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38512307" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное  бюджетное общеобразовательное учреждение «Средняя общеобразовательная школа №  1» п.г.т. Уренгой Пуровского района</td>
            <td>8911020447</td>
            <td>89-160/3260-01-07/33</td>
            <td>26.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38503691" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКОУ  «СОШ № 4» Г.ТАРКО-САЛЕ  (МУНИЦИПАЛЬНОЕ  БЮДЖЕТНОЕ ОБЩЕОБРАЗОВАТЕЛЬНОЕ УЧРЕЖДЕНИЕ &quot;СТАРШАЯ ШКОЛА&quot; Г.  ТАРКО-САЛЕ ПУРОВСКОГО РАЙОНА)</td>
            <td>8911032555</td>
            <td>89-160/3253-01-07/93</td>
            <td>25.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38484727" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное  бюджетное общеобразовательное учреждение &quot;Средняя общеобразовательная  школа № 2&quot; п.г.т. Уренгой Пуровского района</td>
            <td>8911012478</td>
            <td>89-160/3261-01-07/64</td>
            <td>27.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38563715" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное  бюджетное дошкольное образовательное учреждение «Детский сад  «Солнышко» п.г.т. Уренгой Пуровского района</td>
            <td>8911016698</td>
            <td>89-160/3279-01-07/18</td>
            <td>25.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38486999" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ «Образовательный центр «Атмосфера» («СОШ №1») п. Ханымей Пуровского района</td>
            <td>8911016786</td>
            <td>89-160/3262-01-08/44</td>
            <td>26.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38511292" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное  бюджетное образовательное учреждение дополнительного образования «Центр  естественных наук»</td>
            <td>8911012580</td>
            <td>89-160/3285-01-07/74</td>
            <td>25.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38488242" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное  бюджетное дошкольное образовательное учреждение &quot;Детский сад  &quot;Белочка&quot; г. Тарко-Сале</td>
            <td>8911014355</td>
            <td>89-160/3268-01-07/57</td>
            <td>26.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38516011" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное  бюджетное дошкольное образовательное учреждение &quot;Детский сад  &quot;Брусничка&quot;</td>
            <td>8911016680</td>
            <td>89-160/3267-01-07/92</td>
            <td>27.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38561216" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное  бюджетное образовательное учреждение дополнительного образования  «Дом детского творчества» г. Тарко-Сале</td>
            <td>8911015704</td>
            <td>89-160/3282-01-07/111</td>
            <td>26.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38489051" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное  бюджетное общеобразовательное учреждение «Школа-интернат среднего общего  образования» с.Самбург</td>
            <td>8911013834</td>
            <td>89-160/3264-01-07/15</td>
            <td>27.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38549469" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное  автономное дошкольное образовательное учреждение «Центр развития ребенка –  детский сад «Радуга» г. Тарко-Сале Пуровского района</td>
            <td>8911021240</td>
            <td>89-160/3272-01-07/9</td>
            <td>26.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38531643" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное  бюджетное дошкольное образовательное учреждение «Детский сад «Сказка» с.  Самбург Пуровского района</td>
            <td>8911017187</td>
            <td>89-160/3280-01-07/87</td>
            <td>27.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38562475" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное  бюджетное образовательное учреждение   дополнительного образования «Центр эстетического воспитания детей  «Сударушка» г. Тарко-Сале Пуровского р-на</td>
            <td>8911020408</td>
            <td>89/160/3184-01-07/98</td>
            <td>26.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38560678" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МУНИЦИПАЛЬНОЕ БЮДЖЕТНОЕ ОБЩЕОБРАЗОВАТЕЛЬНОЕ УЧРЕЖДЕНИЕ &quot;ОСНОВНАЯ ОБЩЕОБРАЗОВАТЕЛЬНАЯ ШКОЛА № 3&quot; Г. ТАРКО-САЛЕ ПУРОВСКОГО РАЙОНА</td>
            <td>8911017589</td>
            <td>89-160/3256-01-07/167</td>
            <td>26.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38513538" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МУНИЦИПАЛЬНОЕ БЮДЖЕТНОЕ ОБЩЕОБРАЗОВАТЕЛЬНОЕ УЧРЕЖДЕНИЕ &quot;ОСНОВНАЯ ОБЩЕОБРАЗОВАТЕЛЬНАЯ ШКОЛА № 1&quot; Г. ТАРКО-САЛЕ ПУРОВСКОГО РАЙОНА</td>
            <td>8911013721</td>
            <td>89-160/3254-01-07/109</td>
            <td>27.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38559528" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МУНИЦИПАЛЬНОЕ БЮДЖЕТНОЕ ДОШКОЛЬНОЕ ОБРАЗОВАТЕЛЬНОЕ УЧРЕЖДЕНИЕ &quot;ДЕТСКИЙ САД &quot;НОВАТОРИЯ&quot; Г.ТАРКО-САЛЕ ПУРОВСКОГО РАЙОНА</td>
            <td>8911016810</td>
            <td>00218</td>
            <td>26.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38505382" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное казенное общеобразовательное учреждение &quot;образовательный центр &quot;новашкола&quot; г. Тарко-сале пуровского района</td>
            <td>8911034200</td>
            <td>2786-01-08 /54</td>
            <td>26.06.2026</td>
            <td><a href="https://doc.yanao.ru/app/o?u=54020606" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

## Салехард

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-салехард-terr-муниципальное-казенное-учреждение-quot-дирекция-по-финансовому-сопровождению-quot" class="dept-checkbox">
    <label for="dept-terr-салехард-terr-муниципальное-казенное-учреждение-quot-дирекция-по-финансовому-сопровождению-quot" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">Муниципальное казенное учреждение &quot;Дирекция по финансовому сопровождению&quot; <span class="org-count">(учреждений: 13)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Департамент строительства, архитектуры и земельных отношений Администрации муниципального образования город Салехард</td>
            <td>8901022170</td>
            <td>171-14/01-05-02/202</td>
            <td>25.06.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=41371971" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное казенное учреждение &quot;Управление капитального строительства&quot;</td>
            <td>8901027972</td>
            <td>171-1411/01-05-01/193</td>
            <td>30.06.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=41514616" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное казенное учреждение &quot;Дирекция по финансовому сопровождению&quot;</td>
            <td>8901036279</td>
            <td>171-003/01-07-03/849</td>
            <td>27.06.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=41458458" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Администрация муниципального образования город Салехард</td>
            <td>8901003315</td>
            <td>171/01-05-01/1068</td>
            <td>02.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=41551114" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент транспорта и городского хозяйства Администрации муниципального образования город Салехард</td>
            <td>8901039079</td>
            <td>171-13/01-05-01/413</td>
            <td>15.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=41962924" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Городская Дума муниципального образования город Салехард</td>
            <td>8901017501</td>
            <td>171-1/01-05-01/7</td>
            <td>10.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=41842331" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное казенное учреждение &quot;Производственно-техническое управление&quot;</td>
            <td>8901024643</td>
            <td>171-002/01-05-01/3</td>
            <td>02.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=41597451" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное казенное учреждение &quot;Информационно-техническое управление&quot;</td>
            <td>8901025245</td>
            <td>171-001/01-07-03/37</td>
            <td>27.06.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=41453495" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Контрольно-Счетная палата муниципального образования город Салехард</td>
            <td>8901023632</td>
            <td>171-1211/01-05-02/44</td>
            <td>11.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=41879766" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное казенное учреждение &quot;Салехардская дирекция единого заказчика&quot;</td>
            <td>8901015840</td>
            <td>171-1311/01-05-02/28</td>
            <td>14.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=41928876" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное казенное учреждение &quot;Единая дежурно-диспетчерская служба города Салехарда&quot;</td>
            <td>8901022484</td>
            <td>171-1911/01-05-02/1</td>
            <td>30.06.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=41483867" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление имущественных отношений Администрации города Салехарда</td>
            <td>8901022251</td>
            <td>171-11/01-05-02/25</td>
            <td>15.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=41949311" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент по труду и социальной защите населения Администрации муниципального образования город Салехард</td>
            <td>8901002368</td>
            <td>171-15/01-05-02/450</td>
            <td>15.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=41960801" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-салехард-terr-муниципальное-казенное-учреждение-quot-финансовая-дирекция-культуры-молодежной-политики-и-спорта-quot" class="dept-checkbox">
    <label for="dept-terr-салехард-terr-муниципальное-казенное-учреждение-quot-финансовая-дирекция-культуры-молодежной-политики-и-спорта-quot" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">Муниципальное казенное учреждение &quot;Финансовая дирекция культуры, молодежной политики и спорта&quot; <span class="org-count">(учреждений: 11)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Муниципальное казенное учреждение &quot;Финансовая дирекция культуры, молодежной политики и спорта&quot;</td>
            <td>8901030492</td>
            <td>171-1811/01-07-03/236</td>
            <td>30.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42341352" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление по физической культуре и спорту Администрации города Салехарда</td>
            <td>8901022364</td>
            <td>171-16/01-07-03/608</td>
            <td>30.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42344770" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное учреждение дополнительного образования &quot;Спортивная школа «Фаворит»</td>
            <td>8901012574</td>
            <td>171-1613/01-07-03/341</td>
            <td>30.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42355835" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное учреждение дополнительного образования &quot;Спортивная школа &quot;Старт&quot;</td>
            <td>8901014282</td>
            <td>171-1614/01-05-02/2</td>
            <td>30.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42353372" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное учреждение &quot;Центр физической культуры и спорта&quot;</td>
            <td>8901035772</td>
            <td>171-1612/01-07-03/191</td>
            <td>30.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42357136" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление культуры и молодежной политики Администрации города Салехарда</td>
            <td>8901022195</td>
            <td>171-18/01-07-03/855</td>
            <td>30.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42346208" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное образовательное учреждение дополнительного образования &quot;Детская школа искусств имени Е.В. Образцовой&quot;</td>
            <td>8901014275</td>
            <td>171-1817/01-05-02/2</td>
            <td>30.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42351945" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное учреждение культуры &quot;Центр культуры и спорта &quot;Геолог&quot;</td>
            <td>8901022580</td>
            <td>171-1813/01-05-02/11</td>
            <td>30.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42347542" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное учреждение &quot;Салехардский центр молодёжи&quot;</td>
            <td>8901022572</td>
            <td>171-1816/01-05-02/26</td>
            <td>30.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42350370" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное учреждение культуры &quot;Централизованная библиотечная система&quot;</td>
            <td>8901014290</td>
            <td>171-1815/01-07-03/189</td>
            <td>30.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42348731" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление молодёжной политики Администрации города Салехарда</td>
            <td>8901044551</td>
            <td>Без номера подписана рукой</td>
            <td>30.04.2026</td>
            <td>-</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-салехард-terr-муниципальное-казенное-учреждение-quot-дирекция-по-финансовому-сопровождению-муниципальной-системы-образования-quot" class="dept-checkbox">
    <label for="dept-terr-салехард-terr-муниципальное-казенное-учреждение-quot-дирекция-по-финансовому-сопровождению-муниципальной-системы-образования-quot" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">Муниципальное казенное учреждение &quot;Дирекция по финансовому сопровождению муниципальной системы образования&quot; <span class="org-count">(учреждений: 31)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Муниципальное казенное учреждение &quot;Дирекция по финансовому сопровождению муниципальной системы образования&quot;</td>
            <td>8901026016</td>
            <td>171-911/01-05-02/1</td>
            <td>23.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42147085" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент образования Администрации муниципального образования город Салехард</td>
            <td>8901002456</td>
            <td>171-9/01-05-01/548</td>
            <td>15.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42757347" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное казенное учреждение &quot;Дирекция по административно-хозяйственному обслуживанию муниципальной системы образования&quot;</td>
            <td>8901024932</td>
            <td>171-912/01-07-03/1146</td>
            <td>14.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42736838" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное дошкольное образовательное учреждение &quot;Детский сад &quot;Бережок&quot;</td>
            <td>8901010457</td>
            <td>171-945/01-07-03/247</td>
            <td>24.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42218273" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное учреждение дополнительного образования &quot;Детско-юношеский центр&quot;</td>
            <td>8901024072</td>
            <td>171-916/01-05-02/4</td>
            <td>12.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42679162" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное дошкольное образовательное учреждение &quot;Детский сад &quot;Журавушка&quot;</td>
            <td>8901016681</td>
            <td>171-936/01-07-03/318</td>
            <td>12.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42680498" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное дошкольное образовательное учреждение &quot;Детский сад &quot;Золотая рыбка&quot;</td>
            <td>8901010094</td>
            <td>171-947/01-07-03/268</td>
            <td>18.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42074429" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное дошкольное образовательное учреждение &quot;Детский сад &quot;Кристаллик&quot;</td>
            <td>8901024080</td>
            <td>171-939/01-07-03/236</td>
            <td>26.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=43058659" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное дошкольное образовательное учреждение &quot;Детский сад &quot;Крылышки&quot;</td>
            <td>8901010087</td>
            <td>171-937/01-07-03/234</td>
            <td>23.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42166892" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное общеобразовательное учреждение &quot;Лицей&quot;</td>
            <td>8901040973</td>
            <td>171-927/01-05-01/2</td>
            <td>22.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42961094" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное дошкольное образовательное учреждение &quot;Детский сад &quot;Мамонтенок&quot;</td>
            <td>8901034200</td>
            <td>171-931/01-07-03/234</td>
            <td>18.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42062876" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное дошкольное образовательное учреждение &quot;Детский сад &quot;Мозаика&quot;</td>
            <td>8901034218</td>
            <td>171-946/01-07-03/244</td>
            <td>25.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42249950" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное дошкольное образовательное учреждение &quot;Детский сад &quot;Морошка&quot;</td>
            <td>8901039294</td>
            <td>171-941/01-07-03/235</td>
            <td>22.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42144051" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное казенное учреждение &quot;Методический центр развития образования&quot;</td>
            <td>8901025686</td>
            <td>171-913/01-05-02/41</td>
            <td>13.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42727184" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное общеобразовательное учреждение &quot;Обдорская гимназия&quot;</td>
            <td>8901010859</td>
            <td>171-925/01-05-01/52</td>
            <td>19.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42876088" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>муниципальное бюджетное дошкольное образовательное учреждение &quot;Детский сад &quot;Олененок&quot;</td>
            <td>8901039304</td>
            <td>171-938/01-05-02/1</td>
            <td>28.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42289111" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное дошкольное образовательное учреждение &quot;Детский сад &quot;Росинка&quot;</td>
            <td>8901010915</td>
            <td>171-933/01-07-03/404</td>
            <td>07.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42580254" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное дошкольное образовательное учреждение &quot;Центр развития ребенка - детский сад &quot;Рябинка&quot;</td>
            <td>8901010030</td>
            <td>171-935/01-05-02/1</td>
            <td>21.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42099974" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное дошкольное образовательное учреждение &quot;Детский сад &quot;Светлячок&quot;</td>
            <td>8901010048</td>
            <td>171-948/01-07-03/308</td>
            <td>21.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42112813" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное дошкольное образовательное учреждение &quot;Детский сад &quot;Северное сияние&quot;</td>
            <td>8901039287</td>
            <td>171-932/01-07-03/185</td>
            <td>31.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42398596" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное дошкольное образовательное учреждение &quot;Детский сад &quot;Синяя птица&quot;</td>
            <td>8901010055</td>
            <td>171-949/01-07-03/237</td>
            <td>21.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42106582" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ &quot;Детский сад &quot;Снегурочка&quot;</td>
            <td>8901010070</td>
            <td>171-934/01-07-03/183</td>
            <td>21.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42116790" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное автономное общеобразовательное учреждение &quot;Средняя общеобразовательная школа № 1 имени Героя Советского Союза И.В. Королькова&quot;</td>
            <td>8901007133</td>
            <td>171-921/01-07-03/777</td>
            <td>22.09.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=43963253" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>муниципальное бюджетное общеобразовательное учреждение &quot;Средняя общеобразовательная школа № 2&quot;</td>
            <td>8901007214</td>
            <td>171-922/01-07-03/754</td>
            <td>20.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42901684" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>муниципальное бюджетное общеобразовательное учреждение &quot;Средняя общеобразовательная школа № 3&quot;</td>
            <td>8901007221</td>
            <td>171-923/01-07-03/646</td>
            <td>18.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42843067" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>муниципальное бюджетное общеобразовательное учреждение &quot;Средняя общеобразовательная школа № 4&quot;</td>
            <td>8901007912</td>
            <td>171-924/01-07-03/661</td>
            <td>23.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42163155" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное общеобразовательное учреждение &quot;Средняя общеобразовательная школа № 6&quot;</td>
            <td>8901007239</td>
            <td>171-926/01-07-03/661</td>
            <td>28.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42292259" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное дошкольное образовательное учреждение &quot;Детский сад &quot;Улыбка&quot;</td>
            <td>8901027429</td>
            <td>171-944/01-07-03/256</td>
            <td>12.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42685659" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное дошкольное образовательное учреждение &quot;Детский сад &quot;Умка&quot;</td>
            <td>8901028542</td>
            <td>171-943/01-07-03/268</td>
            <td>21.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42103662" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>муниципальное бюджетное учреждение дополнительного образования &quot;Центр внешкольной работы&quot;</td>
            <td>8901006845</td>
            <td>171-914/01-07-03/151</td>
            <td>20.08.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42898332" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МУНИЦИПАЛЬНОЕ БЮДЖЕТНОЕ УЧРЕЖДЕНИЕ ДОПОЛНИТЕЛЬНОГО ОБРАЗОВАНИЯ &quot;ЦЕНТР ДЕТСКОГО ТВОРЧЕСТВА &quot;НАДЕЖДА&quot;</td>
            <td>8901007528</td>
            <td>171-915/01-07-03/252</td>
            <td>25.07.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=42243895" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-салехард-terr-организация-не-указана-нет-бу" class="dept-checkbox">
    <label for="dept-terr-салехард-terr-организация-не-указана-нет-бу" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">Организация не указана (нет БУ) <span class="org-count">(учреждений: 1)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Департамент финансов Администрации города Салехарда</td>
            <td>8901005947</td>
            <td>171-10/01-05-02/12</td>
            <td>30.06.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=41493588" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

## Тазовский район <span class="toc-badge">1</span>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-тазовский-район-terr-мку-центр-бюджетного-учета-тазовского-района" class="dept-checkbox">
    <label for="dept-terr-тазовский-район-terr-мку-центр-бюджетного-учета-тазовского-района" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">МКУ «Центр бюджетного учета Тазовского района» <span class="org-count">(учреждений: 15 <span class="no-requests">| нет заявок: 1</span>)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Администрация Тазовского района</td>
            <td>8910003576</td>
            <td>89-1/01-07/3186</td>
            <td>14.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39167456" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Дума Тазовского района</td>
            <td>8910003671</td>
            <td>89-2/01-07/50</td>
            <td>17.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39332417" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент финансов Администрации Тазовского района</td>
            <td>8910002244</td>
            <td>89-5/01-07/608</td>
            <td>25.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39609164" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ &quot;Дирекция по обслуживанию деятельности органов местного самоуправления Тазовского района&quot;</td>
            <td>8910006104</td>
            <td>89-14/01-11/116</td>
            <td>14.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39178797" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ «Центр по обеспечению жизнедеятельности коренных малочисленных народов Севера Тазовского района»</td>
            <td>8910006288</td>
            <td>89-10-51/01-11/1/86-2025</td>
            <td>12.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39993301" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление по делам коренных малочисленных народов Севера и агропромышленного комплекса Тазовского района</td>
            <td>8910002830</td>
            <td>89-10/01-09/288</td>
            <td>12.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39995199" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент строительства и жилищной политики Администрации Тазовского района</td>
            <td>8904090838</td>
            <td>9-08/01-07/1107</td>
            <td>02.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39997909" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ «Управление капитального строительства Тазовского района»</td>
            <td>8910006224</td>
            <td>89-8-51/01-10/1101</td>
            <td>13.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39997909" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент муниципального хозяйства Администрации Тазовского района</td>
            <td>8910064441</td>
            <td>89-9/01-07/2290</td>
            <td>15.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40102760" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ &quot;УК &quot;Тазовская&quot;</td>
            <td>8904092169</td>
            <td>89-9-51/01-11/165</td>
            <td>12.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39991545" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент имущественных и земельных отношений Администрации Тазовского района</td>
            <td>8910004474</td>
            <td>89-4/01-07/2360</td>
            <td>16.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39274268" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ «Центр бюджетного учета Тазовского района»</td>
            <td>8904096928</td>
            <td>89-5/01-07/1514</td>
            <td>08.10.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=44583242" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное учреждение «Средства массовой информации Тазовского района»</td>
            <td>8910000166</td>
            <td>89-13/01-11/67</td>
            <td>13.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40042122" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление по делам гражданской обороны, предупреждению и ликвидации чрезвычайных ситуаций Администрации Тазовского района</td>
            <td>8910003390</td>
            <td>89-8/01-09/377</td>
            <td>01.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38673579" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ &quot;СЗ ЖКУ&quot;</td>
            <td>8910003167</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-тазовский-район-terr-организация-не-указана-нет-бу" class="dept-checkbox">
    <label for="dept-terr-тазовский-район-terr-организация-не-указана-нет-бу" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">Организация не указана (нет БУ) <span class="org-count">(учреждений: 4)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Контрольно-счетная палата Тазовского района</td>
            <td>8910003689</td>
            <td>89-3/01-07/151</td>
            <td>13.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40028829" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент социального развития Администрации Тазовского района</td>
            <td>8910004481</td>
            <td>89-7/01-10/984</td>
            <td>02.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38772986" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление молодежной политики Администрации    Тазовского района</td>
            <td>8904094857</td>
            <td>89-11-51/01-07/31</td>
            <td>21.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38371725" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ &quot;Дирекция жилищной политики Тазовского района&quot;</td>
            <td>8910003400</td>
            <td>89-11-52/01-10/156</td>
            <td>12.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39973207" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-тазовский-район-terr-мку-дирекция-по-финансово-экономическому-сопровождению-и-организационно-техническому-обслуживанию-муниципальной-системы-образования" class="dept-checkbox">
    <label for="dept-terr-тазовский-район-terr-мку-дирекция-по-финансово-экономическому-сопровождению-и-организационно-техническому-обслуживанию-муниципальной-системы-образования" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">МКУ Дирекция по финансово-экономическому сопровождению и организационно-техническому обслуживанию муниципальной системы образования <span class="org-count">(учреждений: 14)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>МКУ Дирекция по финансово-экономическому сопровождению и организационно-техническому обслуживанию муниципальной системы образования</td>
            <td>8910006270</td>
            <td>89-6-51/01-07/1144</td>
            <td>14.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39160937" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент  образования Администрации Тазовского района</td>
            <td>8910004509</td>
            <td>89-6/01-07/1480</td>
            <td>15.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39160957" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ ЦО &quot;Полярная звезда&quot;</td>
            <td>8904095297</td>
            <td>01128</td>
            <td>15.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39250392" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ ДО &quot;Тазовский РДТ&quot;</td>
            <td>8910002149</td>
            <td>262</td>
            <td>16.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39281370" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ Детский сад &quot;Теремок&quot;</td>
            <td>8910002928</td>
            <td>89-6-63/01-39/267</td>
            <td>16.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39281233" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ детский сад &quot;Звездочка&quot;</td>
            <td>8910002702</td>
            <td>255</td>
            <td>16.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39281125" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ детский сад &quot;Солнышко&quot;</td>
            <td>8910002910</td>
            <td>89-6-62/01-09/159</td>
            <td>14.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39204687" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ детский сад &quot;Рыбка&quot;</td>
            <td>8904082153</td>
            <td>89-6-63/01-12/210</td>
            <td>15.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39234093" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКОУ ГШИ имени Н. И. ЯПТУНАЙ</td>
            <td>8910002195</td>
            <td>455</td>
            <td>11.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39122321" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ детский сад &quot;Северяночка&quot;</td>
            <td>8910002710</td>
            <td>00863</td>
            <td>14.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39179851" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКОУ АШИ</td>
            <td>8910001963</td>
            <td>89-6-56/01-28/223</td>
            <td>18.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39384516" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МУНИЦИПАЛЬНОЕ БЮДЖЕТНОЕ ДОШКОЛЬНОЕ ОБРАЗОВАТЕЛЬНОЕ УЧРЕЖДЕНИЕ ЦЕНТР ДОШКОЛЬНОГО ОБРАЗОВАНИЯ &quot;ПЛАНЕТА ДЕТСТВА&quot;</td>
            <td>8904081720</td>
            <td>89-6-60/01-10/398</td>
            <td>11.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39122030" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ детский сад &quot;Радуга&quot;</td>
            <td>8910064508</td>
            <td>00597</td>
            <td>16.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39280659" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ ННОШ</td>
            <td>8910003199</td>
            <td>89-6-55/01-20-2/219</td>
            <td>11.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39136862" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-тазовский-район-terr-мку-дирекция-по-финансово-экономическому-сопровождению-и-организационно-техническому-обслуживанию-учреждений-культуры-физической-культуры-и-спорта-молодежной-политики-и-туризма" class="dept-checkbox">
    <label for="dept-terr-тазовский-район-terr-мку-дирекция-по-финансово-экономическому-сопровождению-и-организационно-техническому-обслуживанию-учреждений-культуры-физической-культуры-и-спорта-молодежной-политики-и-туризма" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">МКУ «Дирекция по финансово-экономическому сопровождению и организационно-техническому обслуживанию учреждений культуры, физической культуры и спорта, молодежной политики и туризма» <span class="org-count">(учреждений: 9)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>МКУ  «Дирекция по финансово-экономическому сопровождению и  организационно-техническому обслуживанию учреждений культуры, физической  культуры и спорта, молодежной политики и туризма»</td>
            <td>8910006150</td>
            <td>89-11-51/01-07/31</td>
            <td>21.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38371725" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление культуры, физической культуры и спорта Администрации  Тазовского района</td>
            <td>8910004499</td>
            <td>89-11-51/01-07/31</td>
            <td>21.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38371725" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ ДО «Тазовская детская школа искусств»</td>
            <td>8910003079</td>
            <td>89-11-51/01-07/31</td>
            <td>21.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38371725" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ «Молодежный центр»</td>
            <td>8910003505</td>
            <td>89-11-51/01-07/31</td>
            <td>21.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38371725" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ ДО «Тазовская спортивная школа»</td>
            <td>8910002283</td>
            <td>89-11-51/01-07/31</td>
            <td>21.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38371725" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ «Тазовский районный краеведческий музей»</td>
            <td>8910005213</td>
            <td>89-11-51/01-07/31</td>
            <td>21.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38371725" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ «Центр развития физической культуры и спорта»</td>
            <td>8910003512</td>
            <td>89-11-51/01-07/31</td>
            <td>21.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38371725" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ «Централизованная библиотечная сеть»</td>
            <td>8910006312</td>
            <td>89-11-51/01-07/31</td>
            <td>21.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38371725" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ «Централизованная сеть культурно-досуговых учреждений  Тазовского района»</td>
            <td>8910002540</td>
            <td>89-11-51/01-07/31</td>
            <td>21.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38371725" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

## Шурышкарский район

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-шурышкарский-район-terr-организация-не-указана-нет-бу" class="dept-checkbox">
    <label for="dept-terr-шурышкарский-район-terr-организация-не-указана-нет-бу" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">Организация не указана (нет БУ) <span class="org-count">(учреждений: 4)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Департамент  финансов Администрации Шурышкарского района</td>
            <td>8907000938</td>
            <td>01-01-07/321</td>
            <td>08.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38976102" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление социальной защиты населения Администрации  Шурышкарского района</td>
            <td>8907000984</td>
            <td>08-01-07/521</td>
            <td>26.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38527528" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное дошкольное образовательное учреждение  «Детский сад «Теремок»</td>
            <td>8907001025</td>
            <td>ликвидировался 10.03.2025</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>МБУ «Информационное телевизионное радиовещательное агентство «ТРВ-Мужи»/Мужи ИНФОРМ</td>
            <td>8907001650</td>
            <td>1</td>
            <td>11.12.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=47016827" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-шурышкарский-район-terr-муниципальное-казенное-учреждение-quot-централизованная-бухгалтерия-органов-местного-самоуправления-шурышкарского-района-quot" class="dept-checkbox">
    <label for="dept-terr-шурышкарский-район-terr-муниципальное-казенное-учреждение-quot-централизованная-бухгалтерия-органов-местного-самоуправления-шурышкарского-района-quot" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">Муниципальное казенное учреждение &quot;Централизованная бухгалтерия органов местного самоуправления Шурышкарского района&quot; <span class="org-count">(учреждений: 11)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Администрация Шурышкарского района</td>
            <td>8907000920</td>
            <td>101-07/3167</td>
            <td>14.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39198830" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Дума Шурышкарского района</td>
            <td>8907002068</td>
            <td>2-01-08/182</td>
            <td>16.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39292278" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Контрольно-счётная палата Шурышкарского района</td>
            <td>8907002389</td>
            <td>301-07/33</td>
            <td>16.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39291387" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ &quot;Служба заказчика муниципального округа Шурышкарский  район&quot;</td>
            <td>8907002413</td>
            <td>0621-01-07/240</td>
            <td>24.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37421890" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент строительства, архитектуры и земельных отношений  Администрации Шурышкарского района</td>
            <td>8907002364</td>
            <td>06-01-07/345</td>
            <td>21.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37376165" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ &quot;Инвентаризации и оценки имущества&quot;</td>
            <td>8907001716</td>
            <td>05-05-01/84</td>
            <td>03.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37660809" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление имущества Администрации Шурышкарского района</td>
            <td>8907002420</td>
            <td>05-01-07/530</td>
            <td>27.02.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=37579882" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент жилищно-коммунального комплекса Администрации  Шурышкарского района</td>
            <td>8907001730</td>
            <td>09-01-07/1417</td>
            <td>16.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39276608" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ &quot;СпецТрансСервис&quot;</td>
            <td>8901041906</td>
            <td>0921-0107/6</td>
            <td>16.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39279910" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ &quot;Производственно-техническое объединение&quot;</td>
            <td>8907002396</td>
            <td>123-01-09/52</td>
            <td>04.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38862494" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МУНИЦИПАЛЬНОЕ КАЗЕННОЕ УЧРЕЖДЕНИЕ &quot;ЦЕНТРАЛИЗОВАННАЯ БУХГАЛТЕРИЯ ОРГАНОВ МЕСТНОГО САМОУПРАВЛЕНИЯ ШУРЫШКАРСКОГО РАЙОНА</td>
            <td>8901043974</td>
            <td>01-01-09/34</td>
            <td>30.04.2026</td>
            <td><a href="https://doc.yanao.ru/app/o?u=52054121" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-шурышкарский-район-terr-мку-quot-комплексный-центр-по-обслуживанию-учреждений-сферы-образования-шурышкарского-района-quot" class="dept-checkbox">
    <label for="dept-terr-шурышкарский-район-terr-мку-quot-комплексный-центр-по-обслуживанию-учреждений-сферы-образования-шурышкарского-района-quot" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">МКУ &quot;Комплексный центр по обслуживанию учреждений сферы образования Шурышкарского района&quot; <span class="org-count">(учреждений: 16)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>МКУ  &quot;Комплексный центр по обслуживанию учреждений сферы образования  Шурышкарского района&quot;</td>
            <td>8901036293</td>
            <td>0722-01-07/152</td>
            <td>21.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38349464" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление образования Администрации Шурышкарского района</td>
            <td>8907000913</td>
            <td>07-01-07/695</td>
            <td>19.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38266361" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное   общеобразовательное учреждение «Горковская специальная (коррекционная)  общеобразовательная школа - интернат для обучающихся, воспитанников с  ограниченными возможностями здоровья»</td>
            <td>8907001177</td>
            <td>0723-01-0735</td>
            <td>07.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38931733" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное дошкольное образовательное учреждение  «Детский сад «Аленушка»</td>
            <td>8907001032</td>
            <td>0730-01-07/24</td>
            <td>03.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38833344" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное дошкольное образовательное учреждение  «Детский сад «Буратино»</td>
            <td>8907001113</td>
            <td>0729-01-07/15</td>
            <td>03.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38825697" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное дошкольное образовательное учреждение  «Детский сад «Олененок»</td>
            <td>8907001138</td>
            <td>0731-01-07/43</td>
            <td>03.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38825832" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное дошкольное образовательное учреждение  «Детский сад «Северяночка»</td>
            <td>8907001120</td>
            <td>0732-01-07/25</td>
            <td>04.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38856016" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное общеобразовательное учреждение  «Горковская средняя общеобразовательная школа»</td>
            <td>8907001191</td>
            <td>0727-01-07/100</td>
            <td>03.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38814990" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное общеобразовательное учреждение  «Мужевская средняя общеобразовательная школа имени Н.В.Архангельского»</td>
            <td>8907001265</td>
            <td>0724-01-07/184</td>
            <td>03.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38828205" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное общеобразовательное учреждение «Азовская  СОШ «Образовательно-воспитательный центр»</td>
            <td>8907001152</td>
            <td>0735-01-07/87</td>
            <td>03.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38826311" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное общеобразовательное учреждение  «Восяховская СОШ «Образовательный центр»</td>
            <td>8907001160</td>
            <td>0736-01-06/64</td>
            <td>09.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39021664" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное общеобразовательное учреждение  «Питлярская СОШ «Образовательный центр»</td>
            <td>8907001258</td>
            <td>0726-01-06/74</td>
            <td>03.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38812375" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное общеобразовательное учреждение  «Шурышкарская СОШ «Образовательный центр»</td>
            <td>8907001240</td>
            <td>0725-01-06/36</td>
            <td>09.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39016986" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное учреждение дополнительного образования  «Центр воспитания и дополнительного образования с.Мужи и Шурышкарского  района»</td>
            <td>8907001219</td>
            <td>0721-01-10-00146</td>
            <td>03.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38828024" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное общеобразовательное учреждение «Социокультурный  центр» с.Лопхари</td>
            <td>8907001184</td>
            <td>0733-01-07/100</td>
            <td>03.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38824595" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ &quot;Овгортская СОШ &quot;Образовательный центр&quot;.</td>
            <td>8907001201</td>
            <td>0728-01-08/508</td>
            <td>18.11.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=46084190" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-шурышкарский-район-terr-мку-централизованная-бухгалтерия-сферы-культуры-шурышкарского-района" class="dept-checkbox">
    <label for="dept-terr-шурышкарский-район-terr-мку-централизованная-бухгалтерия-сферы-культуры-шурышкарского-района" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">МКУ «Централизованная бухгалтерия сферы культуры Шурышкарского района» <span class="org-count">(учреждений: 10)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>МКУ «Централизованная бухгалтерия сферы культуры Шурышкарского  района»</td>
            <td>8901036303</td>
            <td>0227-01-07/6</td>
            <td>13.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38055166" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление культуры, спорта, молодежной политики и туризма  Администрации Шурышкарского района</td>
            <td>8907004428</td>
            <td>0227-01-07/6</td>
            <td>13.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38055166" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ «Центр производственно-технического обслуживания учреждений  сферы культуры»</td>
            <td>8901037804</td>
            <td>0227-01-07/6</td>
            <td>13.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38055166" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное образовательное учреждение  дополнительного образования «Шурышкарская районная детская школа искусств»</td>
            <td>8907001434</td>
            <td>0227-01-07/6</td>
            <td>13.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38055166" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное учреждение «Шурышкарский районный  музейный комплекс им. Г.С. Пузырёва»</td>
            <td>8907002460</td>
            <td>0227-01-07/6</td>
            <td>13.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38055166" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное учреждение «Шурышкарский районный  молодежный центр»</td>
            <td>8907002558</td>
            <td>0227-01-07/6</td>
            <td>13.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38055166" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное учреждение «Шурышкарская  централизованная библиотечная система»</td>
            <td>8907000261</td>
            <td>0227-01-07/6</td>
            <td>13.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38055166" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное учреждение «Шурышкарская  централизованная клубная система»</td>
            <td>8907002540</td>
            <td>0227-01-07/6</td>
            <td>13.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38055166" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное учреждение «Центр физкультуры и спорта»</td>
            <td>8907002156</td>
            <td>0227-01-07/6</td>
            <td>13.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38055166" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Муниципальное бюджетное учреждение дополнительного образования  «Спортивная школа «Юниор»</td>
            <td>8907001106</td>
            <td>0227-01-07/6</td>
            <td>13.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38055166" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

## ЯНАО (ГКУ, ГУ, ГБУ, ГАУ) <span class="toc-badge">47</span>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-янао-гку-гу-гбу-гау-terr-организация-не-указана-нет-бу" class="dept-checkbox">
    <label for="dept-terr-янао-гку-гу-гбу-гау-terr-организация-не-указана-нет-бу" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">Организация не указана (нет БУ) <span class="org-count">(учреждений: 85 <span class="no-requests">| нет заявок: 38</span>)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Государственное бюджетное учреждение  «Окружной центр ветеринарии»</td>
            <td>8901022283</td>
            <td>89-3452/01-06/314</td>
            <td>01.02.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=12973514" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Автономное учреждение Ямало-Ненецкого  автономного округа «Управление государственной экспертизы проектной  документации»</td>
            <td>8901019636</td>
            <td>89-0451/01-05/00025</td>
            <td>02.02.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=12996450" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Государственное казенное учреждение  «Дирекция капитального строительства и инвестиций Ямало-Ненецкого автономного  округа»</td>
            <td>8901017526</td>
            <td>89-0450/01-16/1117</td>
            <td>01.02.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=12973040" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Государственное казенное учреждение  «Аппарат Общественной Палаты Ямало-Ненецкого автономного округа»</td>
            <td>8901019298</td>
            <td>89-11-50-06/104</td>
            <td>07.02.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=13164068" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Государственное казенное учреждение  «Ситуационный центр Ямало-Ненецкого автономного округа»</td>
            <td>8901026048</td>
            <td>8901026048</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Государственное казенное учреждение  «Ресурсы Ямала»</td>
            <td>8901010785</td>
            <td>89-0350/01-06/230</td>
            <td>01.02.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=12950235" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Государственное учреждение  Ямало-Ненецкого автономного округа «Многофункциональный центр предоставления  государственных и муниципальных услуг»</td>
            <td>8901022910</td>
            <td>89-0351/01-06/0460</td>
            <td>03.02.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=13071885" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Государственное учреждение  «Производственно-техническое объединение управления делами Правительства  Ямало-Ненецкого автономного округа»</td>
            <td>8901020511</td>
            <td>89-1250/01-06/781</td>
            <td>07.02.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=13108805" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Государственное казенное учреждение  Ямало-Ненецкого автономного округа «Гостиница «Юрибей»</td>
            <td>8901025735</td>
            <td>89-1251/01-06/52</td>
            <td>01.01.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=12920121" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Государственное казенное учреждение  Ямало-Ненецкого автономного округа «Гостинично-транспортный комплекс  «Ямальский»</td>
            <td>8901024890</td>
            <td>89-1252/01-06/265</td>
            <td>10.02.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=13259246" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>ГАУ  Ямало-Ненецкого автономного округа «Научный центр изучения Арктики»</td>
            <td>8901024210</td>
            <td>89-2150/01-05/414</td>
            <td>27.05.2026</td>
            <td><a href="https://doc.yanao.ru/app/o?u=52973066" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>ГБУ  Ямало-Ненецкого автономного округа «Государственная кадастровая оценка»</td>
            <td>8901036328</td>
            <td>89-553/01-05/2413</td>
            <td>20.05.2026</td>
            <td><a href="https://doc.yanao.ru/app/o?u=52717670" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Государственное казенное учреждение  «Государственный архив Ямало-Ненецкого автономного округа»</td>
            <td>8901027041</td>
            <td>89-3750/01-06/789</td>
            <td>27.04.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=15726409" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Государственное автономное учреждение Ямало-Ненецкого  автономного округа «Спортивная школа «Полярная шахматная школа Анатолия  Карпова»</td>
            <td>8901012310</td>
            <td>89-3111/01-06/229</td>
            <td>25.04.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=15632171" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Государственное автономное учреждение Ямало-Ненецкого  автономного округа «Центр спортивной подготовки»</td>
            <td>8901011235</td>
            <td>89-3201-01-06/2369</td>
            <td>26.04.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=15687956" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>ГАУ Ямало-Ненецкого  автономного округа «Спортивная школа олимпийского резерва имени Т.В.  Ахатовой»</td>
            <td>8902008362</td>
            <td>нет</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Государственное автономное учреждение Ямало-Ненецкого  автономного округа «Спортивная школа по северному многоборью»</td>
            <td>8901003820</td>
            <td>89-3141-01-06/174</td>
            <td>28.04.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=15830823" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Государственное автономное учреждение Ямало-Ненецкого  автономного округа «Спортивная школа «Ямал»</td>
            <td>8901012214</td>
            <td>89-3191-01-06/747</td>
            <td>25.04.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=15679159" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Государственное  казенное учреждение «Центр занятости  населения Ямало-Ненецкого автономного округа»</td>
            <td>8901039086</td>
            <td>89-1749-01-06/5997</td>
            <td>25.04.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=15654841" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>ГКУ Ямало-Ненецкого автономного округа «Управление  по контролю за техническим состоянием, энергосбережением и энергоэффективностью  зданий и сооружений»</td>
            <td>8901024474</td>
            <td>нет</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Государственное бюджетное учреждение  Ямало-Ненецкого автономного округа «Региональный центр патриотического  воспитания «Авангард»</td>
            <td>8905039785</td>
            <td>89-2453-01-06/274</td>
            <td>27.04.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=15773591" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>ГБУ  Ямало-Ненецкого автономного округа «Арктический центр добровольчества»</td>
            <td>8901033542</td>
            <td>нет</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Государственное  автономное учреждение Ямало-Ненецкого автономного округа «Национальная библиотека  Ямало-Ненецкого автономного округа»</td>
            <td>8901017847</td>
            <td>89-2353/01-06/174</td>
            <td>26.04.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=15697810" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Государственное казённое учреждение  Ямало-Ненецкого автономного округа «Информационно-аналитический центр»</td>
            <td>8901026859</td>
            <td>89-2355/01-06/88</td>
            <td>25.04.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=15677045" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Государственное  автономное учреждение Ямало-Ненецкого автономного округа  «Ямало-Ненецкий окружной музейно-выставочный комплекс  имени И.С. Шемановского»</td>
            <td>8901014010</td>
            <td>89-2351/01-06/420</td>
            <td>27.04.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=15743402" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Государственное автономное учреждение Ямало-Ненецкого автономного округа «Ямальская филармония»</td>
            <td>8901019153</td>
            <td>89-2352/01-06/749</td>
            <td>27.04.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=15756965" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Государственное автономное учреждение культуры  Ямало-Ненецкого автономного округа «Окружной Дом ремёсел»</td>
            <td>8901010739</td>
            <td>89-2350/01-06/250</td>
            <td>05.05.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=16021579" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Государственное  автономное учреждение культуры Ямало-Ненецкого автономного округа  «Окружной Центр национальных культур»</td>
            <td>8901008419</td>
            <td>89-2354-01-06/149</td>
            <td>05.05.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=16012952" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Государственное  казенное учреждение Ямало-Ненецкого автономного округа «Управление по  обеспечению содействия федеральным органам государственной власти и  деятельности мировых судей Ямало-Ненецкого автономного округа»</td>
            <td>8901025372</td>
            <td>89-1450/01-06/2638</td>
            <td>02.08.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=18540050" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Государственное бюджетное учреждение  «Дирекция особо охраняемых природных территорий регионального значения  Ямало-Ненецкого автономного округа»</td>
            <td>8901018255</td>
            <td>89-2754-01-05/445</td>
            <td>03.06.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40749914" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>ГКУ «Служба по охране, контролю и регулированию использования биоресурсов Ямало-Ненецкого  автономного округа»</td>
            <td>8901010954</td>
            <td>нет</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>ГКУ  «Дирекция дорожного хозяйства Ямало-Ненецкого автономного округа»</td>
            <td>8901008916</td>
            <td>нет</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Государственное бюджетное  профессиональное образовательное учреждение Ямало-Ненецкого автономного  округа «Губкинский профессиональный колледж»</td>
            <td>8911033090</td>
            <td>89-08/01-18//019</td>
            <td>22.12.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=23355452" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Окружное автономного учреждение «Леса  Ямала»</td>
            <td>8901022501</td>
            <td>нет</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>ГКУ  «Управление аварийно-спасательной службы Ямало-Ненецкого автономного округа»</td>
            <td>8901002625</td>
            <td>89-1650/01-05/1271</td>
            <td>28.05.2026</td>
            <td><a href="https://doc.yanao.ru/app/o?u=52995973" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>ГКУ  «Противопожарная служба Ямало-Ненецкого автономного округа»</td>
            <td>8901025333</td>
            <td>89-1652/01-05/5027</td>
            <td>29.05.2026</td>
            <td><a href="https://doc.yanao.ru/app/o?u=53042432" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Государственное учреждение  дополнительного профессионального образования «Учебно-методический центр по  гражданской обороне, чрезвычайным ситуациям и пожарной безопасности  Ямало-Ненецкого автономного округа»</td>
            <td>8903029005</td>
            <td>89-1653/01-05/245</td>
            <td>29.05.2026</td>
            <td><a href="https://doc.yanao.ru/app/o?u=53070529" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент  здравоохранения Ямало-Ненецкого  автономного  округа</td>
            <td>8901016995</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Государственное  бюджетное учреждение  здравоохранения  Ямало-Ненецкого автономного округа  «Аксарковская  центральная районная больница»</td>
            <td>8908000497</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Государственное  автономное учреждение Ямало-  Ненецкого  автономного округа «Дирекция по  финансированию  и материально-техническому  обеспечению  учреждений в сфере здравоохранения»</td>
            <td>8901017967</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Государственное  бюджетное учреждение  здравоохранения  Ямало-Ненецкого автономного округа  «Красноселькупская  центральная районная больница»</td>
            <td>8912001623</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Государственное бюджетное учреждение здравоохранения Ямало-Ненецкого автономного округа «Лабытнангская центральная районная больница»</td>
            <td>8902002635</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Государственное  бюджетное учреждение  здравоохранения  Ямало-Ненецкого автономного округа  «Муравленковская  городская больница»</td>
            <td>8906005041</td>
            <td>89-1858/01-05/695</td>
            <td>21.04.2026</td>
            <td><a href="https://doc.yanao.ru/app/o?u=51640024" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Государственное  бюджетное учреждение  здравоохранения  Ямало-Ненецкого автономного округа  «Надымская  центральная районная больница»</td>
            <td>8903009263</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Государственное  бюджетное учреждение  здравоохранения  Ямало-Ненецкого автономного округа  «Новоуренгойский  психоневрологический диспансер»</td>
            <td>8904018119</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Государственное  бюджетное учреждение  здравоохранения  Ямало-Ненецкого автономного округа  «Новоуренгойская  центральная городская больница»</td>
            <td>8904012710</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Государственное  бюджетное учреждение  здравоохранения  Ямало-Ненецкого автономного округа  «Тарко-Салинская  центральная районная больница»</td>
            <td>8911001324</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Государственное  казенное учреждение здравоохранения  «Бюро  судебно-медицинской экспертизы Ямало-  Ненецкого  автономного округа»</td>
            <td>8901003523</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Государственное бюджетное учреждение  Ямало-Ненецкого автономного округа «Центр социального обслуживания населения  «Доверие» в муниципальном образовании город Салехард»</td>
            <td>8901010665</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Государственное  автономное учреждение  здравоохранения  «Медицинский информационно-  аналитический  центр Ямало-Ненецкого автономного  округа»</td>
            <td>8901025037</td>
            <td>89-1850/01-05/489</td>
            <td>28.05.2026</td>
            <td><a href="https://doc.yanao.ru/app/o?u=53013557" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Государственное  бюджетное учреждение  здравоохранения  Ямало-Ненецкого автономного округа  «Ноябрьский  психоневрологический диспансер»</td>
            <td>8905026948</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Государственное  бюджетное учреждение  здравоохранения  Ямало-Ненецкого автономного округа  «Ноябрьская  станция скорой медицинской помощи»</td>
            <td>8905020181</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Государственное  бюджетное учреждение  здравоохранения  Ямало-Ненецкого автономного округа  «Ноябрьская  центральная городская больница»</td>
            <td>8905018707</td>
            <td>89-1865/01-05/25298</td>
            <td>27.11.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=46400594" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Государственное  бюджетное учреждение  здравоохранения  «Ямало-Ненецкий окружной  психоневрологический  диспансер»</td>
            <td>8901008433</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Государственное  бюджетное учреждение  здравоохранения  Ямало-Ненецкого автономного округа  «Психиатрическая  больница»</td>
            <td>7216003825</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Государственное  бюджетное учреждение  здравоохранения  «Ямало-Ненецкий окружной  противотуберкулезный  диспансер»</td>
            <td>8901008426</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Государственное  бюджетное учреждение  здравоохранения  «Ямало-Ненецкий окружной центр  профилактики  и борьбы со СПИД»</td>
            <td>8905025856</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Государственное  бюджетное учреждение  здравоохранения  Ямало-Ненецкого автономного округа  «Салехардская  станция скорой медицинской помощи»</td>
            <td>8901003202</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Государственное  бюджетное учреждение  здравоохранения  Ямало-Ненецкого автономного округа  «Центр  общественного здоровья и медицинской  профилактики»</td>
            <td>8903033107</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Государственное  казенное учреждение Ямало-Ненецкого  автономного  округа «Центр ресурсного обеспечения в  сфере  здравоохранения»</td>
            <td>8901007006</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Государственное  бюджетное учреждение  здравоохранения  «Салехардская окружная клиническая  больница»</td>
            <td>8901004862</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Государственное  бюджетное учреждение  здравоохранения  Ямало-Ненецкого автономного округа  «Губкинская  городская больница»</td>
            <td>8911013954</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Государственное  бюджетное учреждение  здравоохранения  Ямало-Ненецкого автономного округа  «Мужевская  центральная районная больница»</td>
            <td>8907000906</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Государственное  бюджетное учреждение  здравоохранения  Ямало-Ненецкого автономного округа  «Надымская  станция скорой медицинской помощи»</td>
            <td>8903017218</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Государственное  бюджетное учреждение  здравоохранения  Ямало-Ненецкого автономного округа  «Новоуренгойская  станция скорой медицинской помощи»</td>
            <td>8904013713</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Государственное  бюджетное учреждение  здравоохранения  Ямало-Ненецкого автономного округа  «Тазовская  центральная районная больница»</td>
            <td>8910002124</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Государственное  бюджетное учреждение  здравоохранения  Ямало-Ненецкого автономного округа  «Яр-Салинская  центральная районная больница  имени  Е.А. Кесельмана»</td>
            <td>8909000370</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Государственное казенное учреждение  Ямало-Ненецкого автономного округа «Детский дом «Сияние Севера»</td>
            <td>7216003800</td>
            <td>89-0851/01-06/465</td>
            <td>27.07.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=18392768" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Государственное казенное учреждение  Ямало-Ненецкого автономного округа «Дирекция по организационному обеспечению  департамента образования Ямало-Ненецкого автономного округа и финансовому‚  материально-техническому обеспечению деятельности подведомственных  образовательных учреждений»</td>
            <td>8901025510</td>
            <td>89-0851/01-06/465</td>
            <td>27.07.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=18392768" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Государственное бюджетное  профессиональное образовательное учреждение Ямало-Ненецкого автономного  округа «Муравленковский многопрофильный колледж»</td>
            <td>8906005757</td>
            <td>89-0854/01-06//2443</td>
            <td>28.07.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=18417634" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Государственное профессиональное  образовательное учреждение Ямало-Ненецкого автономного округа «Надымский  профессиональный колледж»</td>
            <td>8903016503</td>
            <td>89-0858/01-16/293</td>
            <td>26.07.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=18365982" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Государственное бюджетное  профессиональное образовательное учреждение Ямало-Ненецкого автономного  округа «Новоуренгойский многопрофильный колледж»</td>
            <td>8904012815</td>
            <td>89-0856/01-16/495</td>
            <td>26.07.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=18353646" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Государственное бюджетное  профессиональное образовательное учреждение Ямало-Ненецкого автономного  округа «Ноябрьский колледж профессиональных и информационных технологий»</td>
            <td>8905037259</td>
            <td>89-0855/01-16/782</td>
            <td>01.08.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=18499767" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Государственное бюджетное  профессиональное образовательное учреждение Ямало-Ненецкого автономного  округа «Тарко-Салинский профессиональный колледж»</td>
            <td>8911019804</td>
            <td>89-0857/01-06/396</td>
            <td>31.07.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=18443774" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Государственное бюджетное  профессиональное образовательное учреждение Ямало-Ненецкого автономного  округа «Ямальский многопрофильный колледж»</td>
            <td>8901018760</td>
            <td>89-0851/01-06/465</td>
            <td>27.07.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=18392768" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Государственное казенное  общеобразовательное учреждение Ямало-Ненецкого автономного округа «Окружная  санаторно-лесная школа»</td>
            <td>8901008384</td>
            <td>89-0853/01-16/138</td>
            <td>26.07.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=18354262" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Государственное автономное учреждение  дополнительного профессионального образования Ямало-Ненецкого автономного  округа «Региональный институт развития образования»</td>
            <td>8901006490</td>
            <td>89-0851/01-06/465</td>
            <td>27.07.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=18392768" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Государственное автономное учреждение  Ямало-Ненецкого автономного округа «Региональный центр оценки качества  образования»</td>
            <td>8901025527</td>
            <td>89-0850/01-06/1044</td>
            <td>27.07.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=18393095" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Государственное автономное учреждение  Ямало-Ненецкого автономного округа «Региональный центр  психолого-педагогической‚ медицинской и социальной помощи»</td>
            <td>8901037787</td>
            <td>00276</td>
            <td>26.07.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=18362153" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Государственное автономное учреждение  Ямало-Ненецкого автономного округа «Центр выявления и поддержки одаренных  детей в Ямало-Ненецком автономном округе»</td>
            <td>8901038903</td>
            <td>89-0851/01-06/465</td>
            <td>27.07.2023</td>
            <td><a href="https://doc.yanao.ru/app/o?u=18392768" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>ГКУ ЯНАО «ЦБ ОГВ ЯНАО»</td>
            <td>8901038364</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>ГАУ ЯНАО «Центр детского отдыха»</td>
            <td>8901043501</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>ГАУ ЯНАО «Методологический центр «Ямолод»</td>
            <td>8901043519</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>ГБУ ЯНАО «ЦСОН «Садко»</td>
            <td>8904040210</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>ГАУ ЯНАО «Новоуренгойский государственный музей»</td>
            <td>8904042016</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-янао-гку-гу-гбу-гау-terr-гку-ямало-ненецкого-автономного-округа-центр-социальных-технологий-ямало-ненецкого-автономного-округа" class="dept-checkbox">
    <label for="dept-terr-янао-гку-гу-гбу-гау-terr-гку-ямало-ненецкого-автономного-округа-центр-социальных-технологий-ямало-ненецкого-автономного-округа" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">ГКУ Ямало-Ненецкого автономного округа «Центр социальных технологий  Ямало-Ненецкого автономного округа» <span class="org-count">(учреждений: 11 <span class="no-requests">| нет заявок: 9</span>)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>ГБУ Ямало-Ненецкого автономного округа «Центр социального  обслуживания населения «Милосердие» в муниципальном образовании  Красноселькупский район»</td>
            <td>8912001976</td>
            <td>нет</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>ГБУ  Ямало-Ненецкого автономного округа «Центр социального обслуживания населения  «Домашний очаг» в муниципальном образовании Надымский район»</td>
            <td>8903019007</td>
            <td>нет</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>ГБУ Ямало-Ненецкого автономного округа «Центр социального обслуживания населения  «Елена» в муниципальном образовании город Губкинский»</td>
            <td>8913002080</td>
            <td>нет</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>ГБУ Ямало-Ненецкого автономного округа «Центр социального обслуживания населения  в муниципальном образовании город Муравленко»</td>
            <td>8906008892</td>
            <td>нет</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>ГБУ  Ямало-Ненецкого автономного округа «Центр социального обслуживания населения  «Гармония» в муниципальном образовании город Ноябрьск»</td>
            <td>8905066429</td>
            <td>нет</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>ГБУ  Ямало-Ненецкого автономного округа «Центр социального обслуживания населения  в муниципальном образовании Пуровский район»</td>
            <td>8911018712</td>
            <td>нет</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>ГБУ  Ямало-Ненецкого автономного округа «Центр социального обслуживания населения  «Забота» в муниципальном образовании Тазовский район»</td>
            <td>8910003520</td>
            <td>нет</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>ГБУ Ямало-Ненецкого автономного округа «Харпский дом-интернат для престарелых и  инвалидов «Мядико»</td>
            <td>8902007337</td>
            <td>нет</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>ГБУ Ямало-Ненецкого автономного округа «Реабилитационный центр «Большой  Тараскуль»</td>
            <td>7203500763</td>
            <td>нет</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>ГКУ Ямало-Ненецкого автономного округа «Центр социальных технологий  Ямало-Ненецкого автономного округа»</td>
            <td>8901026030</td>
            <td>89-0750/01-05/1235</td>
            <td>26.05.2026</td>
            <td><a href="https://doc.yanao.ru/app/o?u=52937638" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>ГКУ Ямало-Ненецкого автономного округа «Социальное казначейство Ямало-Ненецкого автономного округа»</td>
            <td>8901045210</td>
            <td>89-0777/01-05/1</td>
            <td>02.09.2026</td>
            <td><a href="https://doc.yanao.ru/app/o?u=56038871" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

## Органы власти <span class="toc-badge">31</span>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-органы-власти-terr-организация-не-указана-нет-бу" class="dept-checkbox">
    <label for="dept-terr-органы-власти-terr-организация-не-указана-нет-бу" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">Организация не указана (нет БУ) <span class="org-count">(учреждений: 31 <span class="no-requests">| нет заявок: 31</span>)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Государственно-правовой департамент ЯНАО</td>
            <td>8901017413</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Департамент агропромышленного комплекса ЯНАО</td>
            <td>8901017237</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Департамент внутренней политики ЯНАО</td>
            <td>8901019770</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Департамент государственного жилищного надзора ЯНАО</td>
            <td>8901017533</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Департамент государственного заказа ЯНАО</td>
            <td>8901017607</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Департамент гражданской защиты и пожарной безопасности ЯНАО</td>
            <td>8901017188</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Департамент занятости населения ЯНАО</td>
            <td>8901019178</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Департамент имущественных отношений ЯНАО</td>
            <td>8901017357</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Департамент информационных технологий и связи ЯНАО</td>
            <td>8901017212</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Департамент культуры ЯНАО</td>
            <td>8901017276</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Департамент молодёжной политики ЯНАО</td>
            <td>8901017283</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Департамент образования ЯНАО</td>
            <td>8901017131</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Департамент по делам коренных малочисленных народов Севера ЯНАО</td>
            <td>8901017117</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Департамент по физической культуре и спорту ЯНАО</td>
            <td>8901017460</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Департамент природных ресурсов и экологии ЯНАО</td>
            <td>8901017195</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Департамент региональной безопасности ЯНАО</td>
            <td>8901019869</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Департамент строительства и жилищной политики ЯНАО</td>
            <td>8901018311</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Департамент энергетики и коммунального комплекса ЯНАО</td>
            <td>8901017727</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Департамент тарифной политики ЯНАО</td>
            <td>8901045227</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Департамент транспорта и дорожного хозяйства ЯНАО</td>
            <td>8901017340</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Департамент экономики ЯНАО</td>
            <td>8901017406</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Служба ветеринарии ЯНАО</td>
            <td>8901017364</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Служба государственного строительного надзора ЯНАО</td>
            <td>8901020536</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Служба государственной охраны объектов культурного наследия ЯНАО</td>
            <td>8901034761</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Служба ЗАГС ЯНАО</td>
            <td>8901017090</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Служба по делам архивов ЯНАО</td>
            <td>8901017371</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Служба технадзора ЯНАО</td>
            <td>8901017156</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Управление делами Правительства ЯНАО</td>
            <td>8901012616</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Департамент финансов ЯНАО</td>
            <td>8901017477</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Департамент социальной защиты населения ЯНАО</td>
            <td>8901017082</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>Аппарат Губернатора ЯНАО</td>
            <td>8901012609</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

## Ямальский район <span class="toc-badge">2</span>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-ямальский-район-terr-организация-не-указана-нет-бу" class="dept-checkbox">
    <label for="dept-terr-ямальский-район-terr-организация-не-указана-нет-бу" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">Организация не указана (нет БУ) <span class="org-count">(учреждений: 26 <span class="no-requests">| нет заявок: 1</span>)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Департамент  финансов Администрации Ямальского района</td>
            <td>8909000411</td>
            <td>89-168-16/01-12/245</td>
            <td>24.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38439148" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ &quot;Ямальская служба заказчика&quot;</td>
            <td>8909002458</td>
            <td>89-168-2601/01-12/335</td>
            <td>21.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38379862" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ «Образовательный центр «Созвездие»</td>
            <td>8901043580</td>
            <td>89-168-2326/101</td>
            <td>17.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38167409" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУДО «Ямальский центр внешкольной работы»</td>
            <td>8909000891</td>
            <td>89-168-2334/01-12//134</td>
            <td>02.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38763872" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ «Ямальская школа-интернат им. В.Давыдова»</td>
            <td>8909001091</td>
            <td>89-168-2321/01-09/141 Вн от  89-168-2321/01-09/142  Вн</td>
            <td>02.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38771879" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ &quot;ЦБ с. Новый Порт&quot;</td>
            <td>8909002345</td>
            <td>89-168-0000/01-06/30</td>
            <td>14.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39162277" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ &quot;АэроЯмал&quot;</td>
            <td>8901043212</td>
            <td>89-168-2822/01-09/18</td>
            <td>14.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39192018" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ &quot;Полюс&quot;</td>
            <td>8901043220</td>
            <td>89-168-2023/01-09/14</td>
            <td>10.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39049303" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ «Сюнай-Салинская начальная школа-детский сад»</td>
            <td>8909001503</td>
            <td>00016</td>
            <td>17.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39274764" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент социальной защиты населения</td>
            <td>8909000316</td>
            <td>89-168-24/01-04/2158</td>
            <td>19.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40234971" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ &quot;Производственно-техническое объединение&quot;</td>
            <td>8909003148</td>
            <td>2501-12/204</td>
            <td>21.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40306880" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ  «Новопортовская школа-интернат им.Л.В. Лапцуя»</td>
            <td>8909001006</td>
            <td>89-168-2323/01-26/268</td>
            <td>02.06.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40684376" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ «Новопортовский детский сад «Теремок»</td>
            <td>8909001510</td>
            <td>89-168-2330/01-40/151</td>
            <td>02.06.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40684409" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКОУ «Образовательного центра имени Володи Солдатова»</td>
            <td>8901044030</td>
            <td>89-168-2324/07-04/29</td>
            <td>27.01.2026</td>
            <td><a href="https://doc.yanao.ru/app/o?u=48474577" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКОУ &quot;Панаевский образовательный центр&quot;</td>
            <td>8901044047</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
          <tr>
            <td>МКОУ «Салемальская школа-интернат им.В.Солдатова»</td>
            <td>8909000965</td>
            <td>89-168-2324/01-37/166</td>
            <td>11.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39143640" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ «Салемальский детский сад «Золотая рыбка»</td>
            <td>8909001581</td>
            <td>89-168-2327/01-30/70</td>
            <td>11.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39143973" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ «Сеяхинская школа-интернат»</td>
            <td>8909000958</td>
            <td>89-168-2322/01-09/146</td>
            <td>17.06.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=41101105" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ  &quot;ЦБ с. Панаевск&quot;</td>
            <td>8909002352</td>
            <td>89-168*25/01-10/0053</td>
            <td>21.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40442228" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ &quot;ЦБ с. Сеяха&quot;</td>
            <td>8909002313</td>
            <td>00171</td>
            <td>21.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40318511" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ &quot;ЦБ с. Мыс Каменный&quot;</td>
            <td>8909002909</td>
            <td>00065</td>
            <td>25.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38459722" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКОУ «Панаевская школа-интернат</td>
            <td>8909001574</td>
            <td>89-168-2325/01-07/362</td>
            <td>26.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40444751" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ «Панаевский детский сад «Красная шапочка»</td>
            <td>8909001126</td>
            <td>89-168-2328/01-17/68</td>
            <td>28.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40523310" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБДОУ «Сеяхинский детский сад «Олененок»</td>
            <td>8909002056</td>
            <td>89-168-2329/01-07/57</td>
            <td>03.06.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40741063" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ &quot;ЦБ с. Салемал&quot;</td>
            <td>8909002338</td>
            <td>89-168-2336/01-10-014</td>
            <td>08.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38970839" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ информационное агентство &quot;Яр-Сале ТВ&quot;</td>
            <td>8909001158</td>
            <td>89-168-3121/01-06/1</td>
            <td>16.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39220331" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-ямальский-район-terr-мку-quot-централизованная-бухгалтерия-омс-quot" class="dept-checkbox">
    <label for="dept-terr-ямальский-район-terr-мку-quot-централизованная-бухгалтерия-омс-quot" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">МКУ &quot;Централизованная бухгалтерия ОМС&quot; <span class="org-count">(учреждений: 13)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Департамент строительства и архитектуры</td>
            <td>8909005160</td>
            <td>89-168-21/01-04/358</td>
            <td>24.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38413655" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Администрация  Ямальского района</td>
            <td>8909000394</td>
            <td>89-168/01-07/1274</td>
            <td>26.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38488508" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Дума  Ямальского района</td>
            <td>8909002095</td>
            <td>89-168-14/08-28/46</td>
            <td>26.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38489584" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент муниципального хозяйства и транспорта Администрации  Ямальского района</td>
            <td>8909000482</td>
            <td>89-168-28/01-04/930</td>
            <td>09.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38999149" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление по делам малочисленных народов Севера Администрации  Ямальского района</td>
            <td>8901040540</td>
            <td>89-168-22/01-07/366</td>
            <td>10.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39067374" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Контрольно-счетная палата</td>
            <td>8909005561</td>
            <td>89-168-3/01-12/15</td>
            <td>14.03.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38104015" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление культуры и молодежной политики</td>
            <td>8909001824</td>
            <td>89-168-26/01-05/476</td>
            <td>23.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39497093" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Управление физической культуры и спорта</td>
            <td>8909001817</td>
            <td>89-168-26/01-05/498</td>
            <td>28.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39678901" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ дополнительного образования спортивная школа  &quot;Лидер&quot;</td>
            <td>8909003290</td>
            <td>89-168-2621/01-14//173</td>
            <td>24.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39562729" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент имущественных отношений</td>
            <td>8901039921</td>
            <td>89-168-20/01-11/3243</td>
            <td>19.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40203862" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>Департамент образования</td>
            <td>8909002112</td>
            <td>89-168-23/01-04/1592</td>
            <td>27.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40460603" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ &quot;Централизованная бухгалтерия органов местного самоуправления&quot;</td>
            <td>8901044008</td>
            <td>89-168-1616/01-07/40</td>
            <td>17.04.2026</td>
            <td><a href="https://doc.yanao.ru/app/o?u=51566163" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУ «Ямальский молодежный центр «Импульс»</td>
            <td>8901036350</td>
            <td>89-168-2522/01-04/4</td>
            <td>30.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39789019" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-ямальский-район-terr-мку-quot-централизованная-бухгалтерия-яр-сале-quot" class="dept-checkbox">
    <label for="dept-terr-ямальский-район-terr-мку-quot-централизованная-бухгалтерия-яр-сале-quot" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">МКУ &quot;Централизованная бухгалтерия Яр-Сале&quot; <span class="org-count">(учреждений: 3 <span class="no-requests">| нет заявок: 1</span>)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>МБДОУ «Ярсалинский детский сад «Солнышко»</td>
            <td>8909001052</td>
            <td>89-168-2331/53</td>
            <td>16.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39274125" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ &quot;ЦБ Яр-Сале&quot;</td>
            <td>8901029240</td>
            <td>89-168-2339/01-07/11</td>
            <td>02.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=38769753" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МКУ &quot;Сеяхинский центр развития и образования&quot;</td>
            <td>8901044061</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="dept-list">
  <div class="dept-item">
    <input type="checkbox" id="dept-terr-ямальский-район-terr-мку-quot-центр-обслуживания-учреждений-культуры-и-молодежной-политики-quot" class="dept-checkbox">
    <label for="dept-terr-ямальский-район-terr-мку-quot-центр-обслуживания-учреждений-культуры-и-молодежной-политики-quot" class="dept-row">
      <span class="dept-name">
        <span class="org-label">Организация, ведущая БУ</span>
        <span class="org-text">МКУ &quot;Центр обслуживания учреждений культуры и молодежной политики&quot; <span class="org-count">(учреждений: 5)</span></span>
      </span>
      <span class="dept-toggle">›</span>
    </label>
    <div class="dept-details">
      <table class="calls-table">
        <colgroup>
          <col style="width: 40%;">
          <col style="width: 15%;">
          <col style="width: 20%;">
          <col style="width: 12%;">
          <col style="width: 13%;">
        </colgroup>
        <thead>
          <tr>
            <th>Наименование учреждения</th>
            <th>ИНН</th>
            <th>№ заявки</th>
            <th>Дата заявки</th>
            <th>Ссылка на заявку</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>МКУ  &quot;Центр обслуживания учреждений культуры и молодежной политики&quot;</td>
            <td>8901037392</td>
            <td>89-168-2523/01-04/11</td>
            <td>30.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39764746" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБОУ ДО «Ямальская детская музыкальная школа»</td>
            <td>8909001870</td>
            <td>00003</td>
            <td>30.04.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=39767190" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУК  «Ямальская централизованная библиотечная система»</td>
            <td>8909006572</td>
            <td>00011</td>
            <td>15.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40107098" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУК «Ямальский районный музей»</td>
            <td>8909001214</td>
            <td>00004</td>
            <td>13.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40044459" target="_blank">Ссылка</a></td>
          </tr>
          <tr>
            <td>МБУК «Ямальская централизованная клубная система»</td>
            <td>8901034031</td>
            <td>00018</td>
            <td>13.05.2025</td>
            <td><a href="https://doc.yanao.ru/app/o?u=40050957" target="_blank">Ссылка</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

