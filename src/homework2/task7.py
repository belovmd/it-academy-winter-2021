# Программа, проверяющая, действительность треугольника и вычисляющая его площадь

a = float(input('Сторона треугольника, см'))
b = float(input('Сторона треугольника, см'))
c = float(input('Сторона треугольника, см'))
p = (a + b + c)/2
square = (p * (p - a) * (p - b) * (p - c)) ** (1/2)
if a + b > c and b + c > a and c + a > b and a > 0 and b > 0 and c > 0:
    print('triangle,', 'square =', square)
else:
    print('invalid data, not triangle')
