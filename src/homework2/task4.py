# Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
# Учитывать только английские буквы.

my_string = 'Koshka Murka молодец'
number_of_upper = 0
number_of_lower = 0
for el in my_string:
    if 65 <= ord(el) <= 90:
        number_of_upper += 1
else:
    print(number_of_upper)
for el in my_string:
    if 97 <= ord(el) <= 122:
        number_of_lower += 1
else:
    print(number_of_lower)
