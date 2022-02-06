# task 4 Пары элементов

"""Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""

# elements_value means possessive pronoun like element's value not plural values

# Input: 1 1 1
# Output: 3

# Input: 1 1 1 1
# Output: 6

# Input: 1 1 1 1 9 9 9 10 10 12 12 12 14 14 14 14 15
# Output: 19

list_ = [int(number) for number in input("Enter the elements: ").split()]
counter = 0
dict_ = {}

for element in list_:
    dict_[element] = dict_.get(element, 0) + 1

for elements_value in dict_.values():
    if elements_value > 1:
        counter += elements_value * (elements_value - 1) / 2
print(int(counter))
