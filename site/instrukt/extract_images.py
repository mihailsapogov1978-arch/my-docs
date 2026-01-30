import re
import base64
import os
import zipfile

# Имя входного файла с данными
INPUT_FILE = "input.txt"
# Имя выходного ZIP-архива
OUTPUT_ZIP = "extracted_images.zip"

def extract_and_save_images():
    # Читаем весь текст
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Регулярное выражение для поиска base64 PNG
    pattern = r'data:image/png;base64,([A-Za-z0-9+/=]+)'
    matches = re.findall(pattern, content)

    if not matches:
        print("Изображения не найдены.")
        return

    # Создаём временную папку
    temp_dir = "temp_images"
    os.makedirs(temp_dir, exist_ok=True)

    image_count = 0
    for b64_data in matches:
        try:
            # Декодируем base64
            image_data = base64.b64decode(b64_data)
            # Сохраняем как PNG
            filename = f"image_{image_count:03d}.png"
            filepath = os.path.join(temp_dir, filename)
            with open(filepath, "wb") as img_file:
                img_file.write(image_data)
            image_count += 1
        except Exception as e:
            print(f"Ошибка при обработке изображения {image_count}: {e}")

    if image_count == 0:
        print("Ни одно изображение не было успешно сохранено.")
        return

    # Упаковываем в ZIP
    with zipfile.ZipFile(OUTPUT_ZIP, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(temp_dir):
            for file in files:
                zipf.write(os.path.join(root, file), arcname=file)

    # Удаляем временную папку
    for root, _, files in os.walk(temp_dir):
        for file in files:
            os.remove(os.path.join(root, file))
    os.rmdir(temp_dir)

    print(f"Сохранено {image_count} изображений в архив '{OUTPUT_ZIP}'.")

if __name__ == "__main__":
    extract_and_save_images()