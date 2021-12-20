'''
3. Вводится строка.
Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".
'''
while True:
    str_ = str(input("Введите строку: "))
    new_str = str()
    for i in str_:
        if ('a' <= i <= 'z' or 'A' <= i <= 'Z') and i not in new_str:
            new_str += i
    print(new_str)
