# Найти самое длинное слово в введенном предложении.
# Учтите что в предложении есть знаки препинания.


PUNKT_MARKS = '''!"#$%&'()*+, -./:;<=>?@[\\]^_`{|}~'''

words = input('Введите предложение: ').split()
max_word = words[0].strip(PUNKT_MARKS)

for word in words:
    word = word.strip(PUNKT_MARKS)
    if len(word) > len(max_word):
        max_word = word

print(max_word)
