import pandas as pd
import os

# загрузка данных
df = pd.read_csv("5 train.csv")

# ============= ЗАДАЧА 4: Сохраните в CSV таблицу: средняя температура и среднее число поездок по каждому месяцу =============

df["datetime"] = pd.to_datetime(df["datetime"])

month_summary = df.groupby(df["datetime"].dt.month).agg({
    "temp": "mean",
    "count": "mean"
}).round(1)

# Месяцы
month_names = {
    1: "Январь",
    2: "Февраль",
    3: "Март",
    4: "Апрель",
    5: "Май",
    6: "Июнь",
    7: "Июль",
    8: "Август",
    9: "Сентябрь",
    10: "Октябрь",
    11: "Ноябрь",
    12: "Декабрь"
}

month_summary.index = [month_names[i] for i in month_summary.index]
month_summary.columns = ["Средняя температура", "Среднее число поездок"]

# Заменяем точку на запятую для чисел
month_summary = month_summary.astype(str)
for col in month_summary.columns:
    month_summary[col] = month_summary[col].str.replace('.', ',')

# Сохраняем в CSV
output_file = "month_summary.csv"
month_summary.to_csv(output_file, sep=";", encoding="utf-8-sig")

# Выводим информацию о сохранении
print(f"Файл сохранён: {os.path.abspath(output_file)}")