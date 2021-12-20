str_ = input('Введите строку: ')
str_new = ''
for element in str_:
    if element != ' ' and element not in str_new:
        str_new += element
print(str_new)
