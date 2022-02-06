# Даны два натуральных числа. Вычислите их наибольший общий делитель при помощи
# алгоритма Евклида (мы не знаем функции и рекурсию).

numb1, numb2 = int(input('Введите число: ')), int(input('Введите число: '))
while numb1 and numb2:
    if numb1 >= numb2:
        numb1 %= numb2
    else:
        numb2 %= numb1
print(numb1 + numb2)
