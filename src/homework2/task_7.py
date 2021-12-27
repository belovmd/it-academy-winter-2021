# 7. Даны: три стороны треугольника.
# Требуется: проверить, действительно ли это стороны треугольника.
# Если стороны определяют треугольник, найти его площадь.
# Если нет, вывести сообщение о неверных данных.


side_a = input('Enter side a: ')
side_b = input('Enter side b: ')
side_c = input('Enter side c: ')

if side_a + side_b > side_c:
    if side_a + side_c > side_b:
        if side_b + side_c > side_a:
            print('Is a triangle')
        else:
            print('Incorrect data')
    else:
        print('Incorrect data')
else:
    print('Incorrect data')
