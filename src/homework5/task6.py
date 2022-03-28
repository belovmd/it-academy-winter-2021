# 6 Бинарные операции
# Вводится число найти его максимальный делитель, являющийся
# степенью двойки. 10(2) 16(16), 12(4).

n = int(input('Введите число: '))

simple_numbers = [div for div in range(1, n + 1) if not n % div]
powers_of_two = [2 ** i for i in range(n + 1) if 2 ** i <= n][::-1]

for num in powers_of_two:
    if num in simple_numbers:
        print(num)
        break
