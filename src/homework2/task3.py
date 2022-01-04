# 3. Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def", то должно быть выведено "abcdef".

str_ = input("Введите строку: ")
str_result = ""

for elem in str_:
    if elem not in str_result and elem != " ":
        str_result += elem

print("Строка без повторяющихся символов:", str_result)
