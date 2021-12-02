# task 7
"""Даны: три стороны треугольника.
Требуется: проверить, действительно ли это стороны треугольника.
Если стороны определяют треугольник, найти его площадь.
Если нет, вывести сообщение о неверных данных."""
side1 = float(input("Введите 1ую сторону треугольника: "))
side2 = float(input("Введите 2ую сторону треугольника: "))
side3 = float(input("Введите 3ю сторону треугольника: "))
if ((side2 - side3 < side1 < side2 + side3) and
        (side1 - side3 < side2 < side1 + side3) and
        (side1 - side2 < side3 < side1 + side2)):

    half_per = (side1 + side2 + side3) / 2
    square = (half_per * (half_per - side1) * (half_per - side2) * (half_per - side3)) ** 0.5
    print(f"Площадь треугольниква со сторонами {side1, side2, side3} равна: {square}")
else:
    print("Такого треугольника не существует. Проверьте введённые данные")
