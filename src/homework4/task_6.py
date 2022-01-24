# Слова
# Во входной строке записан текст.
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.
# Определите, сколько различных слов содержится в этом тексте.


import string
str_ = input('Enter text: ')
table = str.maketrans(dict.fromkeys(string.punctuation))
new_str = str_.translate(table)
new_str = new_str.split()

print(len(set(new_str)))
