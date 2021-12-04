# task 2
"""Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания."""
import string

str_ = input("Введите текст: ")
for char in string.punctuation:
    altered_str_ = str_.replace(char, "")
longest = max(altered_str_.split(), key=lambda word: len(word))
print(longest)
