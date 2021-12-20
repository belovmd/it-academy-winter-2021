import re

text = input('Введите предложение: ')
text_clear = re.sub(r'[^\w\s]','',text)
lst = text_clear.split()
max_word = ''
for word in lst:
    if len(word) > len(max_word):
        max_word = word
print(max_word)
