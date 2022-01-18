# Найти самое длинное слово в введенном предложении.
# Учтите что в предложении есть знаки препинания.
# Подсказки:
# my_string.split([chars]) возвращает список строк.
# len(list) - количество элементов в списке

import re

my_string = "Hello, my dear friend! I am glad to see you here."
new_string = re.sub(r'[^\w\s]', '', my_string)
my_list = new_string.split()
largest_word = max(my_list, key=len)
print(largest_word)
