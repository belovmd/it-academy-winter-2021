# Вывод n-го число Фибоначчи

n = int(input("Введите n число Фибоначи: "))

fib_1 = 0
fib_2 = 1

for elem in range(n):
    fib_1, fib_2 = fib_2, fib_1 + fib_2

print("n число Фибоначи равно: ", fib_1)
