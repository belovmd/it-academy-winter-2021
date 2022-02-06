# Во входной строке записан текст. Словом считается последовательность непробельных
# символов идущих подряд, слова разделены одним или большим числом пробелов или
# символами конца строки. Определите, сколько различных слов содержится в этом тексте.

import string
string_ =  input('Введите текст: ')
without_punctuation = string_.translate(str.maketrans('', '', string.punctuation))
small_letter = without_punctuation.lower()
words = small_letter.split()
print(len(set(words)))
