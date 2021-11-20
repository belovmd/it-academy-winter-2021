'''
Даны: три стороны треугольника.
Требуется: проверить, действительно ли это стороны треугольника.
Если стороны определяют треугольник, найти его площадь. Если
нет, вывести сообщение о неверных данных.
'''
s = float()
while True:
    a = float(input("Введите длину первой стороны: "))
    b = float(input("Введите длину второй стороны: "))
    c = float(input("Введите длину третьей стороны: "))
    if a + b > c or a + c > b or b + c > a:  # тест на треугольник
        p = float((a + b + c) / 2)
        s = (p * (p - a) * (p - b) * (p - c)) ** .5
        print('Площадь треугольника =', s)
    else:
        print('Это не треугольник')
