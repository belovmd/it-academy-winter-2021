# Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def", то должно быть выведено "abcdef".

string = input('Введите строку: ')
new_string = ''
for i in string:
    if i not in new_string and i != ' ':
        new_string += i
print(new_string)
