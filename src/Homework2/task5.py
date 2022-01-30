'''
Выведите n-ое число Фибоначчи, используя только временные переменные,
циклические операторы и условные операторы. n - вводится
Задачу поместите в файл task5.py в папке src/homework2.
'''
while True:
    n = int(input("Введите n: "))
    a = int(1)
    b = int(1)
    if n == 1 or n == 2:
        print(1)
    for i in range(3, n + 1):
        if i % 2 > 0:
            a = a + b
            if i == n:
                print(a)
        else:
            b = b + a
            if i == n:
                print(b)
