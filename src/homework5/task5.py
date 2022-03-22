# 5. Написать программу которая находит ближайшую степень двойки к введенному числу.
# 10(8), 20(16), 1(1), 13(16)

num = int(input("Введите число: "))
degree = 1

if not num % 2 and num > 0:
    while degree < (num / 2):
        degree = degree * 2     # или degree << 1, но я разницу не увидел при подсчёте
elif num % 2 and num > 0:       # или просто что-то неправильно сделал
    while degree < num:
        degree = degree * 2

print("Ближайшая степень двойки к числу {n}: {d}".format(n=num, d=degree))
