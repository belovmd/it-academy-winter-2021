# 5 Бинарные операции
# Написать программу которая находит ближайшую степень
# двойки к введенному числу. 10(8), 20(16), 1(1), 13(16)

num = int(input('Введите число: '))

for i in range(num):
    power_of_two = 2**i
    if power_of_two >= num:
        number_less = 2**(i-1)
        number_greater = power_of_two
        break

if number_greater - num > num - number_less:
    print(number_less)
else:
    print(number_greater)
