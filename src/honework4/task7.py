# Даны два натуральных числа.
# Вычислите их наибольший общий делитель при помощи алгоритма Евклида
# (мы не знаем функции и рекурсию).

first_number = 4
second_number = 18
list_ = []

if first_number and second_number:
    list_.append(first_number)
    list_.append(second_number)
    list_.sort()
    list_.reverse()

    while list_[-1]:
        list_.append(list_[-2] % list_[-1])

    print("Max divide:",list_[-2])
else:
    print("Integer must be more than zero")
