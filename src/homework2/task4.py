# task 4
"""Посчитать количество строчных (маленьких) и прописных (больших) букв
в введенной строке. Учитывать только английские буквы."""
import string

str_ = input("Введите текст: ")
low_case_letters = 0
upper_case_letters = 0
alphabet_str_ = string.ascii_letters
for char in range(len(str_)):
    if str_[char].islower() and str_[char] in alphabet_str_:
        low_case_letters += 1
    if str_[char].isupper() and str_[char] in alphabet_str_:
        upper_case_letters += 1
print(f"{low_case_letters} маленьких букв в строке:")
print(f"{upper_case_letters} больших букв в строке:")
