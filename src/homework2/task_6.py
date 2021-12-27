# 6. Определите, является ли число палиндромом
# (читается слева направо и справа налево одинаково).\
# Число положительное целое, произвольной длины.
# Задача требует работать только с числами (без конвертации числа в строку или что-нибудь еще)


enter_num = int(input('Enter string: '))

copy_num = enter_num
pal_num = 0

while enter_num > 0:
    dig = enter_num % 10
    pal_num = pal_num * 10 + dig
    enter_num //= 10
if copy_num == pal_num:
    print('Is a palindrome')
else:
    print('Is not a palindrome')
