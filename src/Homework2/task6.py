'''
6. Определите, является ли число палиндромом
(читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины.
Задача требует работать только с числами
(без конвертации числа в строку или что-нибудь еще)
Задачу поместите в файл task6.py в папке src/homework2.
'''
while True:
    chislo_in = int(input('Введите число: '))
    chislo = chislo_in
    chislo_rev = int()
    while chislo > 0:
        chislo_rev = chislo_rev * 10 + chislo % 10
        chislo = chislo // 10
    if chislo_in == chislo_rev:
        print('Это палиндром')
    else:
        print('Это не палиндром')
