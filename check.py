import pandas as pd
df = pd.read_excel("zayavky.xlsx")
print("Колонки:", list(df.columns))
print("Первые 3 строки:")
print(df.head(3))