# Найти самое длинное слово в введенном предложении.
# Учтите что в предложении есть знаки препинания.


import string


words = input('Введите предложение: ').split()
max_word = words[0].strip(string.punctuation)

for word in words:
    word = word.strip(string.punctuation)
    if len(word) > len(max_word):
        max_word = word

print(max_word)
