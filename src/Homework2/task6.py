'''
Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины. Задача требует работать только с числами
(без конвертации числа в строку или что-нибудь еще)
Задачу поместите в файл task6.py в папке src/homework2.
'''
import copy
while True:
    chislo = int(input('Введите число: '))
    lst_ = []
    lst_rev = []
    while chislo > 0:
        lst_.append(chislo % 10)
        chislo = chislo // 10
    lst_rev = copy.deepcopy(lst_)
    lst_rev.reverse()
    if lst_ == lst_rev:
        print('Это палиндром')
    else:
        print('Это не палиндром')
