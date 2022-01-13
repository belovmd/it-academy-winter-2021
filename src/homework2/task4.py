# Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
# Учитывать только английские буквы.

string = input('Ведите строку: ')
small_letter = 0
big_letter = 0
for letter in string:
    if 'a' <= letter <= 'z':
        small_letter += 1
    else:
        if 'A' <= letter <= 'Z':
            big_letter += 1
print('Sum small letter:', small_letter)
print('Sum big letter:', big_letter)
