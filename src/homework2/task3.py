# 3 Вводится строка. Требуется удалить из нее повторяющиеся
# символы и все пробелы. Например, если было введено "abc cde def",
# то должно быть выведено "abcdef".

str_ = input('Введите строку: ')
str_new = ''
for element in str_:
    if element != ' ' and element not in str_new:
        str_new += element
print(str_new)
