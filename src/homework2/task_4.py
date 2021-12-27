# 4. Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
# Учитывать только английские буквы.


str_enter = input('Enter string: ')

uppers = 0
lowers = 0

for elem in str_enter:
    if 'a' <= elem <= 'z':
        lowers += 1
    else:
        if 'A' <= elem <= 'Z':
            uppers += 1
else:
    print('Enter the string in English!')

print('upper:', uppers, 'lower:', lowers)
