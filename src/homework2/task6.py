# Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
# Число положительное целое, произвольной длины. Задача требует работать только с числами
# (без конвертации числа в строку или что-нибудь еще)

n = int(input("Введите число: "))
var = n
new = 0
while n > 0:
    new = new * 10 + n % 10
    n = n // 10
if var == new:
    print("Это число является палиндромом")
else:
    print("Это число не является палиндромом")
