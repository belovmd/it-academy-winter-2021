﻿'''
1. Проверьте делимость числа на 17.
2. Если число нечетное, выведите “ого”, если четное “ага”.
3. Если число нечетное, выведите “ого” если число четное, и
отрицательное, выведите “маловато”, если число четное и
положительное, выведите “нормально”, если число равно
нулю, выведите “на нет спроса нет”.
4. Переписать оператор or через вложенные условные
операторы.
'''
while True:
    a = int(input('Введите число: '))
    if a % 17 == 0:
        print('1. ', a, 'делится на 17')
    else:
        print('1. ', a, 'не делится на 17')
    if a % 2 > 0:
        print('2. ого')
    else:
        print('2. ага')
    if a % 2 > 0:
        print('3. ого')
    if a % 2 == 0 and a < 0:
        print('3. маловато')
    elif a % 2 == 0 and a > 0:
        print('3. нормально')
    elif a == 0:
        print('3. на нет спроса нет')
