# Оглянемся назад. Числа
# Даны два натуральных числа.
# Вычислите их наибольший общий делитель при помощи алгоритма Евклида
# (мы не знаем функции и рекурсию).


number = int(input('Enter number 1: '))
number_2 = int(input('Enter number 2: '))

while number != 0 and number_2 != 0:
    if number > number_2:
        number = number % number_2
    else:
        number_2 = number_2 % number
print(number + number_2)
