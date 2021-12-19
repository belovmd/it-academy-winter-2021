# 3. Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def", то должно быть выведено "abcdef".

str_ = input("Введите строку: ")
str_result = ""

for i in str_:
    if i not in str_result and i != " ":
        str_result += i

print(str_result)
