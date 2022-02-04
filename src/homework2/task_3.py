# 3. Вводится строка.
# Требуется удалить из нее повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def",
# то должно быть выведено "abcdef".


str_enter = input('Enter string: ')
new_str = ''

for word in str_enter:
    if word not in new_str:
        new_str += word

print(new_str)
