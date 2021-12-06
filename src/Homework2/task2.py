# Найти самое длинное слово в введенном предложении.
# Учтите что в предложении есть знаки препинания.

import string

str_ = input("Enter the sentence:")
clear_punctuation = str_.translate(str.maketrans('', '', string.punctuation))
str_split = clear_punctuation.split()
max_word = str_split[0]

for word in str_split:
    if len(word) > len(max_word):
        max_word = word

print(max_word)
