# 7. Даны: три стороны треугольника. Требуется: проверить, действительно ли это стороны треугольника.
# Если стороны определяют треугольник, найти его площадь. Если нет, вывести сообщение о неверных данных.

side_a = int(input("Сторона a:"))
side_b = int(input("Сторона b:"))
side_c = int(input("Сторона c:"))

if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
    half_meter = (side_a + side_b + side_c) / 2     # Формула Герона
    square = (half_meter * half_meter - side_a) * (half_meter - side_b) * (half_meter - side_c) ** 0.5
    print("Треугольник существует, его площадь =", square)
else:
    print("Треугольник не существует")