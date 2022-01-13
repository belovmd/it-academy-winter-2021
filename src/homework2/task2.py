# 2. Найти самое длинное слово в введенном предложении.
# Учтите что в предложении есть знаки препинания.

import string

str_ = input("Введите строку: ").translate(str.maketrans("", "", string.punctuation))
long_word = ""

for word in str_.split():
    if len(word) > len(long_word):
        long_word = word

print("Самое длинное слово:", long_word)
