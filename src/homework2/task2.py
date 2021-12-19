# 2. Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания.
# Подсказки:
# my_string.split([chars]) возвращает список строк.
# len(list) - количество элементов в списке

str_ = input("Введите строку:")
long_word = ""
str_list = str_.split()
str_list_len = len(str_list)

for i in str_list:
    if i > long_word:
        long_word = i

print(long_word)