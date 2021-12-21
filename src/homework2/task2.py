# 2. Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания.
# Подсказки:
# my_string.split([chars]) возвращает список строк.
# len(list) - количество элементов в списке

import string

str_ = input("Введите строку: ").translate(str.maketrans("", "", string.punctuation))
lst_ = str_.split()
long_word = ""

for word in lst_:   # А насколько правильно будет сразу проходить циклом по сплиту?
    if len(word) > len(long_word):
        long_word = word

print(long_word)
