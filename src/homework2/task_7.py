# 7. Даны: три стороны треугольника.
# Требуется: проверить, действительно ли это стороны треугольника.
# Если стороны определяют треугольник, найти его площадь.
# Если нет, вывести сообщение о неверных данных.


side_a = float(input('Enter side a: '))
side_b = float(input('Enter side b: '))
side_c = float(input('Enter side c: '))

if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:

    p = (side_a + side_b + side_c) / 2
    square = (p * (p - side_a) * (p - side_b) * (p - side_c)) ** 0.5

    print('Square of triangle: {square}'.format(square=square))

else:
    print('Incorrect data')
