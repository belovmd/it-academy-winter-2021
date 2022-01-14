# Даны два натуральных числа.
# Вычислите их наибольший общий делитель при помощи алгоритма Евклида
# (мы не знаем функции и рекурсию).

first_number = 15
second_number = 5
list_ = []

if first_number and second_number:
    list_.append(first_number)
    list_.append(second_number)
    list_.sort(reverse=True)

    while list_[-1]:
        list_.append(list_[-2] % list_[-1])

    print("Greatest max divisor:", list_[-2])
else:
    print("Integer must be more than zero")
