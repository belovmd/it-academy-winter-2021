# Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
# Число положительное целое, произвольной длины.
# Задача требует работать только с числами (без конвертации числа в строку или что-нибудь еще)
initial = int(input())
copy_of_initial = initial
p = 0
while copy_of_initial > 1:
    p = p * 10 + (copy_of_initial % 10)
    copy_of_initial = copy_of_initial // 10

if initial == p:
    print('палиндром')
else:
    print('не палиндром')
