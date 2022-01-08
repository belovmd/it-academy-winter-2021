# task 4 Пары элементов

"""Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""

# Input: 1 1 1
# Output: 3

# Input: 1 1 1 1
# Output: 6

# Input: 1 1 1 1 9 9 9 10 10 12 12 12 14 14 14 14 15
# Output: 19

list_ = [int(number) for number in input("Enter the elements: ").split()]
counter = 0

for element in list_:
    if list_.count(element) > 1:
        counter += (list_.count(element) - 1)
print(counter // 2)
