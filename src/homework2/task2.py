# Longest word without punctuation


import string


str_ = input("Enter line ")
for char in str_:
    if char in string.punctuation:
        str_ = str_.replace(char, "")
lst = str_.split()
max_value = 0
max_word = "None(Empty line)"  # if there isn't' any word
for el in lst:
    if len(el) > max_value:
        max_word = el
        max_value = len(el)
print("Longest word:", max_word)
