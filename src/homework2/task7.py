a, b, c = 5, 4, 3
if a + b > c and b + c > a and a + c > b:
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(s)
else:
    print('Введены неверное данные')
