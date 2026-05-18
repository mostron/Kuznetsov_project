import ifcopenshell

# Открываем модель
model = ifcopenshell.open("Example_1.ifc")

# Задаем критерий: ширина двери >= 900 мм
min_width = 900

# Фильтруем двери
filtered_doors = []
for door in model.by_type("IfcDoor"):
    if getattr(door, "OverallWidth", 0) >= min_width:
        filtered_doors.append(door)

# Создаем новую модель с той же схемой, что и исходная и копируем отфильтрованные двери
new_model = ifcopenshell.file(schema=model.schema)
for door in filtered_doors:
    new_model.add(door)

# Сохраняем подмодель
output = f"_doors_wide_{min_width}.ifc"
new_model.write(output)

# Проверка: открываем созданный файл и выводим количество дверей
check = ifcopenshell.open(output)
check_doors = check.by_type("IfcDoor")

print(f"Создан файл: {output}")
print(f"Дверей в подмодели: {len(check_doors)}")
print(f"Все двери имеют ширину >= {min_width} мм")