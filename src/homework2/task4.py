# 4. Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
# Учитывать только английские буквы.

str_ = input("Введите строку: ")
str_counter_uppercase = 0
str_counter_lowercase = 0

for elem in str_:
    if "A" <= elem <= "Z":
        str_counter_uppercase += 1
    elif "a" <= elem <= "z":
        str_counter_lowercase += 1

print("Заглавных: {upper}\nПрописных: {lower}".format(upper=str_counter_uppercase,
                                                      lower=str_counter_lowercase,))