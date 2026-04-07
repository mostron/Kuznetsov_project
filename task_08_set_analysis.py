materials_1 = {"Кирпич", "Бетон", "Доски", "Гвозди", "Цемент"}
materials_2 = {"Гвозди", "Цемент", "Пена монтажная", "Бетон", "Рубероид"}
materials_3 = {"Бетон", "Цемент", "Рубероид", "Гипсокартон", "Гвозди"}

print(
    f"Все уникальные материалы: {materials_1 | materials_2 | materials_3}\n"
    f"Общие для всех: {materials_1 & materials_2 & materials_3}\n"
    f"Только у первого: {materials_1 - materials_2 - materials_3}\n"
    f"Ровно у двух: {((materials_1 & materials_2) | (materials_1 & materials_3) | (materials_2 & materials_3)) - (materials_1 & materials_2 & materials_3)}"
)