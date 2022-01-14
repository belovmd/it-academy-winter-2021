# Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def", то должно быть выведено "abcdef".


str_ = input('Введите строку: ').replace(' ', '')
char_clear = str_[0]

for char_ in str_:
    if char_ not in char_clear:
        char_clear = char_clear + char_

print(char_clear)
