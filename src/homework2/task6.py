# 6. Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
# Число положительное целое, произвольной длины. Задача требует работать только с числами
# (без конвертации числа в строку или что-нибудь еще)

num = input("Введите число: ")
num = int(num)
copy_num = num
result = 0

while num != 0:
    digit = num % 10
    result = result * 10 + digit
    num = int(num / 10)

if result == copy_num:
    print("{res} палиндром!".format(res=result))
else:
    print("{res} не палиндром!".format(res=result))
