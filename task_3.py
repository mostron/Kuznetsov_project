import ifcopenshell
from ifcopenshell.util.element import get_psets

filepath = "Example_1.ifc"

# Открываем модель
model = ifcopenshell.open(filepath)

# Получаем все элементы типа IfcWall
walls = model.by_type("IfcWall")

# Получаем первый элемент
first_wall = walls[0]

# Получаем наборы свойств (Property Sets) для первой стены
psets = get_psets(first_wall)

# Выводим полный словарь наборов свойств
print("-" * 50)
print("Полный словарь Property Sets:")
print(psets)
print("-" * 50)

# Перебираем все наборы свойств и их параметры
for pset_name, properties in psets.items():
    print(f"Pset: {pset_name}")
    for prop_name, prop_value in properties.items():
        print(f"  {prop_name}: {prop_value}")
    print("-" * 50)
