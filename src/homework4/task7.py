# Даны два натуральных числа.
# Вычислите их наибольший общий делитель
# при помощи алгоритма Евклида (мы не знаем функции и рекурсию).

num1, num2 = int(input('input num1 = ')), int(input('input num2 = '))

while num1 != 0 and num2 != 0:
    if num1 > num2:
        num1 = num1 % num2
    else:
        num2 = num2 % num1

print('greatest common divisor = ' + str(num1 + num2))
