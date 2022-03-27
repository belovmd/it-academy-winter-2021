# Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def", то должно быть выведено "abcdef".

def new_string(string):
    # string = 'abc cde def'
    new_string = ''
    for i in string:
        if i not in new_string and i != ' ':
            new_string += i
    return print(new_string)

# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать.
# Входные данные - строка из чисел, разделенная пробелами.
# Выходные данные - количество пар.
# Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар


def counter(lst):
    # lst = [2, 6, 8, 2, 9, 6, 2, 2, 6]
    dct = {}
    counter = 0
    for element in lst:
        dct[element] = dct.get(element, 0) + 1
    for key in dct:
        counter += (dct[key] * (dct[key] - 1)) / 2
    return print(int(counter))


# Выведите n-ое число Фибоначчи, используя только временные переменные, циклические операторы и
# условные операторы. n - вводится


def fib2(n):
    # n = 5
    fib1 = fib2 = 1
    for element in range(3, n + 1):
        fib1, fib2 = fib2, fib1 + fib2
    return print("Значение этого элемента:", fib2)
