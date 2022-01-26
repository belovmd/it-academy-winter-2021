'''
7.	Оглянемся назад. Числа
Даны два натуральных числа. Вычислите их наибольший общий делитель
при помощи алгоритма Евклида (мы не знаем функции и рекурсию).
Задачу поместите в файл task7.py в папке src/homework4.
'''
a = int()
b = int()
c = int()
nod = []
m = int(input('Введите первое число: '))
n = int(input('Введите второе число: '))
if m > n:
    a = m
    b = n
elif n > m:
    a = n
    b = m
if m == n:
    a = b = m
while c != b and a != c and b != c:
    if b == a:
        nod.append(b)
    elif a > b:
        c = a - b
    while c > b:
        c = c - b
    if c == b:
        nod.append(c)
    elif b > c:
        a = b - c
    while a > c:
        a = a - c
    if a == c:
        nod.append(a)
    elif c > a:
        b = c - a
    while b > a:
        b = b - a
else:
    print(nod[0])
