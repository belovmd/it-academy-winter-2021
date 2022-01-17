# Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def", то должно быть выведено "abcdef".
init_string = 'abc cde def'
new_string = init_string.replace(' ', '')
my_list = list(new_string)
for el in my_list:
    if my_list.count(el) >= 2:
        my_list.remove(el)
else:
    final_string = ''.join(my_list)
    print(final_string)
