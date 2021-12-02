# task 2
"""Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания."""
import string

input_string = input("Введите текст: ")
for symbol in string.punctuation:
    input_string = input_string.replace(symbol, "")
longest = max(input_string.split(), key=lambda word: len(word))
print(longest)
