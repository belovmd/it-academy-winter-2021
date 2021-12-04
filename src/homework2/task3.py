# task 3
"""Вводится строка.
Требуется удалить из нее повторяющиеся символы и все пробелы."""
str_ = input("Введите строку: ")
final_str_ = ""
for char in str_:
    if char not in final_str_ and char != " ":
        final_str_ += char
print(final_str_)
