# 2 Найти самое длинное слово в введенном предложении.
# Учтите что в предложении есть знаки препинания.
# Подсказки:
# my_string.split([chars]) возвращает список строк.
# len(list) - количество элементов в списке

import re

text = input('Введите предложение: ')
text_clear = re.sub(r'[^\w\s]', '', text)
lst = text_clear.split()
max_word = ''
for word in lst:
    if len(word) > len(max_word):
        max_word = word
print(max_word)
