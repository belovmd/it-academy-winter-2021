str_ = input('Введите текст: ')
little = 0
big = 0
for element in str_:
    if 'a' <= element <= 'z':
        little += 1
    if 'A' <= element <= 'Z':
        big += 1
print('Количество строчных букв', little)
print('Количество прописных букв', big)
