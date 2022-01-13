#Во входной строке записан текст. Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.
# Определите, сколько различных слов содержится в этом тексте.

import string

str_ = input("Enter the sentence: ")
result = set()
clear_punctuation = str_.translate(str.maketrans('', '', string.punctuation))
split = clear_punctuation.split()

for elem in split:
    result.add(elem)

print("Number of words: ", len(result))
