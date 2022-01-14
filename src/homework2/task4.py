# Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
# Учитывать только английские буквы.


str_ = input('Введите строку: ')
upper_ = []
lower_ = []

for char_ in str_:
    if 'a' <= char_ <= 'z':
        lower_.append(char_)
    elif 'A' <= char_ <= 'Z':
        upper_.append(char_)

print('Строчных букв - ', len(lower_), ', прописных букв - ', len(upper_))
