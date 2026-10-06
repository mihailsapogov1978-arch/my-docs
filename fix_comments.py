#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Автозамена <input type="text" data-step-field="comment" value="..."> на
<textarea class="detail-input detail-textarea" data-step-field="comment" rows="1">...</textarea>
+ добавление CSS, авторасширения и пересчёта высоты при раскрытии.

Использование:
    python3 fix_comments.py
или с явным путём:
    python3 fix_comments.py docs/projects_2026/roadmap.md
"""
import os
import re
import sys

DEFAULT_PATH = os.path.join('docs', 'projects_2026', 'roadmap.md')


def html_escape_text(s):
    return (
        s.replace('&', '&amp;')
         .replace('<', '&lt;')
         .replace('>', '&gt;')
    )


def replace_inputs(text):
    pattern = re.compile(r'<input\b[^>]*>', re.IGNORECASE)

    def repl(match):
        tag = match.group(0)

        if 'data-step-field="comment"' not in tag:
            return tag

        value_m = re.search(r'\bvalue="([^"]*)"', tag)
        value = value_m.group(1) if value_m else ''

        esc_value = html_escape_text(value)

        return (
            '<textarea class="detail-input detail-textarea" '
            'data-step-field="comment" rows="1" '
            'placeholder="—">'
            + esc_value +
            '</textarea>'
        )

    return pattern.sub(repl, text)


def add_autogrow_script(text):
    if 'function autoGrow(' in text:
        return text

    marker = '  // ===== Разово: заполняем селекты и подписи этапов ====='
    if marker not in text:
        print('⚠️  Не нашёл блок «Разово: заполняем селекты...», авторасширение не добавлено.')
        return text

    insert_block = (
        '  // ===== Авторасширение textarea для комментариев =====\n'
        '  function autoGrow(el) {\n'
        '    if (!el || el.tagName !== \'TEXTAREA\') return;\n'
        '    el.style.height = \'0px\';\n'
        '    el.style.overflowY = \'hidden\';\n'
        '    el.style.height = (el.scrollHeight + 2) + \'px\';\n'
        '  }\n'
        '\n'
        "  document.querySelectorAll('#bossTable textarea[data-step-field=\"comment\"]').forEach(t => {\n"
        '    autoGrow(t);\n'
        "    t.addEventListener('input', function () { autoGrow(this); saveState(); });\n"
        '  });\n'
        '\n'
        '  // Пересчёт после полной загрузки (шрифты, тема Material)\n'
        "  window.addEventListener('load', function () {\n"
        "    document.querySelectorAll('#bossTable textarea[data-step-field=\"comment\"]').forEach(autoGrow);\n"
        '  });\n'
        '\n'
    )

    return text.replace(marker, insert_block + marker, 1)


def add_css(text):
    if '.detail-textarea' in text:
        return text

    anchor = '.detail-checkbox {'
    if anchor not in text:
        print('⚠️  Не нашёл .detail-checkbox в <style>, стили .detail-textarea не добавлены.')
        return text

    css = (
        '.detail-textarea {\n'
        '    resize: vertical;\n'
        '    min-height: 30px;\n'
        '    max-height: 200px;\n'
        '    overflow-y: hidden;\n'
        '    line-height: 1.35;\n'
        '    white-space: pre-wrap;\n'
        '    word-break: break-word;\n'
        '    box-sizing: border-box;\n'
        '    height: auto;\n'
        '}\n'
    )

    return text.replace(anchor, css + anchor, 1)


def patch_saved_values(text):
    needle = "if (c && st.comment != null) c.value = st.comment;"
    add = "\n            if (c && c.tagName === 'TEXTAREA') autoGrow(c);"

    if needle in text and "autoGrow(c)" not in text:
        return text.replace(needle, needle + add, 1)
    return text


def patch_toggle_detail(text):
    if "querySelectorAll('textarea[data-step-field=\"comment\"]').forEach(autoGrow)" in text:
        return text

    needle = "    if (toggle) toggle.classList.toggle('open', !isOpen);\n" \
             "    mainRow.classList.toggle('open', !isOpen);"
    add = (
        "\n\n"
        "    // Пересчёт высоты textarea при раскрытии\n"
        "    if (!isOpen) {\n"
        "      detail.querySelectorAll('textarea[data-step-field=\"comment\"]').forEach(autoGrow);\n"
        "    }"
    )

    if needle in text:
        return text.replace(needle, needle + add, 1)
    return text


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_PATH

    if not os.path.exists(path):
        print(f'Файл не найден: {path}')
        sys.exit(1)

    with open(path, 'r', encoding='utf-8') as f:
        original = f.read()

    text = original
    text = replace_inputs(text)
    text = add_css(text)
    text = add_autogrow_script(text)
    text = patch_saved_values(text)
    text = patch_toggle_detail(text)

    if text == original:
        print('Ничего не изменилось — вероятно, замена уже выполнена.')
        return

    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f'✅ Готово: {path}')


if __name__ == '__main__':
    main()