# 5. Выведите n-ое число Фибоначчи,
# используя только временные переменные, циклические операторы и
# условные операторы. n - вводится


number_enter = int(input('Enter number: '))

fib_1 = 1
fib_2 = 1

for num in range(number_enter):
    fib_1, fib_2 = fib_2, fib_1 + fib_2

print(fib_2)
