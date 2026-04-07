student_name = "Дмитрий Кузнецов"
group_number = 502
project_name = "ЖК Распутин"  
floors = 24
height = 72
is_residential = True
construction_year = 2022

total_height = floors * height  

print(f"== ПАСПОРТ СТРОИТЕЛЬНОГО ОБЪЕКТА ==\n"
      f"Составитель: {student_name}\n"
      f"Группа: {group_number}\n"
      f"Объект: {project_name}\n"
      f"Этажность: {floors} этажей\n"
      f"Высота: {height} м\n"
      f"Тип: {'Жилой' if is_residential else 'Нежилой'}\n"
      f"Год постройки: {construction_year}")

# 13-я линия Васильевского острова, 50, Санкт-Петербург
# Проходил мимо, понравился