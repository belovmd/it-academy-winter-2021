print("Стороны:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5

if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует")
    print("Площадь треугольника:", s)
else:
    print("Ошибка, это не треугольник")
