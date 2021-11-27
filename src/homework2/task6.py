# task 6
"""Определите, является ли число палиндромом
(читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины.
Задача требует работать только с числами
(без конвертации числа в строку или что-нибудь еще)"""

number = int(input("Введите число: "))
reverse = 0
while number != 0:
    digit = number % 10
    result = reverse * 10 + digit
    number //= 10
if reverse == number:
    print("Palindrome")
else:
    print("Not a palindrome")
