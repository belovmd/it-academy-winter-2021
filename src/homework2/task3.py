# task 3
"""Вводится строка.
Требуется удалить из нее повторяющиеся символы и все пробелы."""
input_string = input("Введите строку: ")
final_string = ""
for char in input_string:
    if char not in final_string and char != " ":
        final_string += char
print(final_string)
