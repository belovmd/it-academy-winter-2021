# task 7 Оглянемся назад. Числа
"""
Даны два натуральных числа. Вычислите их наибольший общий делитель
при помощи алгоритма Евклида (мы не знаем функции и рекурсию).
"""

# Examples:
"""
Input:
Enter the 1st number: 625
Enter the 2nd number: 50
Output:
25
Input:
Enter the 1st number: 99
Enter the 2nd number: 66
Output:
33
Input:
Enter the 1st number: 4096
Enter the 2nd number: 768
Output:
256
"""

number_1, number_2 = int(input("Enter the 1st number: ")), int(input("Enter the 2nd number: "))
while number_1 != number_2:
    if number_1 > number_2:
        number_1 -= number_2
    else:
        number_2 -= number_1
print(number_1)
