# 2 Найти самое длинное слово в введенном предложении.
# Учтите что в предложении есть знаки препинания.
# Подсказки:
# my_string.split([chars]) возвращает список строк.
# len(list) - количество элементов в списке

punctuation = '!()-[]\\/;:\'",<>.?'

text = input('Введите предложение: ')
lst_ = text.split()
lst = [el.strip('!()-[]\\/;:\'",<>.?') for el in lst_]
max_word = ''
for word in lst:
    if len(word) > len(max_word):
        max_word = word
print(max_word)
