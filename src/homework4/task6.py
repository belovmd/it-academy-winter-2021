# The input string has a text. Count unique words.

import string

str_ = input("Enter line ")
str_ = str_.lower()  # Different case words are still the same words
for char in str_:
    if char in string.punctuation:
        str_ = str_.replace(char, "")
str_ = str_.split()
print(str_)
print(len(set(str_)))
