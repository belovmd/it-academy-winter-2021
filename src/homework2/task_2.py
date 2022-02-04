# 2. Найти самое длинное слово в введенном предложении.
# Учтите что в предложении есть знаки препинания.
# Подсказки:
# my_string.split([chars]) возвращает список строк.
# len(list) - количество элементов в списке


from string import punctuation

str_enter = input('Enter string: ')
new_str = ''

for word in str_enter:
    if word not in punctuation:
        new_str += word

str_split = max(new_str.split(), key=len)

print(str_split)
