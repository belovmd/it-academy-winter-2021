# Вывод n-го число Фибоначчи

n = int(input("Введите n число Фибоначи: "))
fib_1 = 0
fib_2 = 1
fib_n = 0

if n > 0:
    for counter in range(0, n):
        fib_n = fib_1 + fib_2
        fib_2 = fib_1
        fib_1 = fib_n
else:
    for counter in range(n, 0):
        fib_n = fib_2 - fib_1
        fib_2 = fib_1
        fib_1 = fib_n

print("n число Фибоначи равно: ", fib_1)
