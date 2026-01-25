# create_folders.py
import os

# Года, которые нас интересуют
YEARS = list(range(2019, 2027))  # 2019-2026

def main():
    for year in YEARS:
        folder_path = f"docs/Meropriyatia/{year}"
        os.makedirs(folder_path, exist_ok=True)
        print(f"✅ Создана папка: {folder_path}")

if __name__ == "__main__":
    main()