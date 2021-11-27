# task 5
"""Выведите n-ое число Фибоначчи, используя только временные
переменные, циклические операторы и условные операторы. n - вводится"""
n = int(input("Введите n: "))
number1 = 0
number2 = 1
for i in range(0, n):
    number1, number2 = number2, number1 + number2
print(number1)
