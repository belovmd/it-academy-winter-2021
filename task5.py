number = int(input('Введите число: '))

for el in range(number):
    degree = 2 ** el
    if degree >= number:
        number1 = 2 ** (el - 1)
        number2 = degree
        break

if number2 - number > number - number1:
    print(number1)
else:
    print(number2)
