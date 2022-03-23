# Задачи из прошлых домашних работ, преобразованные в функции для task1.py

def hw3_task4():
    lst_ = [1, 1, 1, 1]
    counter = 0

    for elem in range(len(lst_)):
        for elem2 in range(elem + 1, len(lst_)):
            if lst_[elem] == lst_[elem2]:
                counter += 1

    return counter


def hw2_task3():
    str_ = "ABCABCDF-u"
    str_result = ""

    for elem in str_:
        if elem not in str_result and elem != " ":
            str_result += elem

    return str_result


def hw2_task5(num=42):
    fib_1 = 0
    fib_2 = 1

    if num == 1:
        return fib_1
    else:
        for elem in range(num):
            fib_1, fib_2 = fib_2, fib_1 + fib_2
        return fib_1


def hw3_task6():
    lst_ = [0, 0, 0, 2, 3, 3, 4]

    for elem in lst_:
        if not elem:
            lst_.remove(elem)
            lst_.append(0)

    return lst_


def hw4_task6():
    text = "text, text, example, lorem ipsum, text"
    return len(set(text))
