# task 4
"""Посчитать количество строчных (маленьких) и прописных (больших) букв
в введенной строке. Учитывать только английские буквы."""
import string

input_string = input("Введите текст: ")
low_case_letters = 0
upper_case_letters = 0
alphabet_string = string.ascii_letters
for i in range(len(input_string)):
    if (input_string[i].islower()
            and input_string[i] in alphabet_string):
        low_case_letters += 1
    if (input_string[i].isupper() 
            and input_string[i] in alphabet_string):
        upper_case_letters += 1
print(f"{low_case_letters} маленьких букв в строке:")
print(f"{upper_case_letters} больших букв в строке:")
