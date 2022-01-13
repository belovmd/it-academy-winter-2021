# Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания.
# Подсказки:
# my_string.split([chars]) возвращает список строк.
# len(list) - количество элементов в списке

import string
sentence = input('Введите предложение: ')
without_punctuation = sentence.translate(str.maketrans('', '', string.punctuation))
words = without_punctuation.split()
max_word = words[0]
for word in words:
    if len(word) > len(max_word):
        max_word = word
print(max_word)
