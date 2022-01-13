string = input('Ведите строку: ')
small_l = 0
big_l = 0
for el in string:
    if 'a' <= el <= 'z':
        small_l += 1
    else:
        if 'A' <= el <= 'Z':
            big_l += 1
print('Строчных букв:', small_l)
print('Прописных букв:', big_l)
