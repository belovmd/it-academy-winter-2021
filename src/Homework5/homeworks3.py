'''
4.	Пары элементов
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается,
что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
'''


def counter_couples():
    counter_elements = int()
    counter_par = int()
    antirepeat = []
    str_ = '1 1 1 2 2 2 2 3 3 3 3 3'
    list_ = [int(elem) for elem in str_.split()]
    for element in list_:
        if element not in antirepeat:
            counter_elements = list_.count(element)
            antirepeat.append(element)
            if counter_elements > 1:
                for a_progress in range(1, counter_elements):  # counter_par = (counter_elements - 1)!
                    counter_par += a_progress
    return counter_par


'''
5.	Уникальные элементы в списке
Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке.
Задачу поместите в файл task5.py в папке src/homework3.
'''


def counter_once():
    count = int()
    list_ = [1, 1, 1, 1, 2, 4, 2, 2, 3, 5, 4]
    list_new = []
    for element in list_:
        if list_.count(element) == 1:
            list_new.append(element)
    return list_new


'''
6.	Упорядоченный список.
Дан список целых чисел.
Требуется переместить все ненулевые элементы в левую часть списка,
не меняя их порядок, а все нули - в правую часть.
Порядок ненулевых элементов изменять нельзя, дополнительный список использовать нельзя,
задачу нужно выполнить за один проход по списку.
Распечатайте полученный список.
Задачу поместите в файл task6.py в папке src/homework3.

'''


def mover():
    list_ = [0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 3, 4, 0, 5, 0, 6, 0, 0, 7]
    for i in list_:
        if i == 0:
            list_.remove(i)
            list_.append(i)
    return list_
