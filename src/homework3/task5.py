# task 5 Уникальные элементы в списке

"""
Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""

list_ = [int(number) for number in input("Enter the elements: ").split()]

for element in list_:
    if list_.count(element) == 1:
        print(element)
