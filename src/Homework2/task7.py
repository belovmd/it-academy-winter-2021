# Проверить, действительно ли введены стороны треугольника и посчитать его площадь

a = int(input("Введите сторону треуголтника a: "))
b = int(input("Введите сторону треуголтника b: "))
c = int(input("Введите сторону треуголтника c: "))

if a > 0 and b > 0 and c > 0:
    if a < b + c and b < a + c and c < a + b:
        p = (a + b + c) / 2
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print("Площадь тругольника равна : ", s)
    else:
        print("Невернные данные")
else:
    print("Невернные данные")
