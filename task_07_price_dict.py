materials = {
    "щебень": 4200,
    "кирпич": 66,
    "цемент": 730,
    "гипс": 250,
    "песок": 600
}

materials["бетон"] = 2200
materials["арматура"] = 61000
materials["цемент"] *= 2.10
del materials["песок"]
average_price = sum(materials.values()) / len(materials)

print("Прайс-лист материалов:")
for material, price in materials.items():
    print(f"{material}: {price:.2f} руб.")

print(f"\nСредняя цена: {average_price:.2f} руб.")