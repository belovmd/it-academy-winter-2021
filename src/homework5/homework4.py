# Создайте словарь с помощью генератора словарей, так чтобы его ключами были числа от 1
# до 20, а значениями кубы этих чисел.

def task1():
    dct = {element: element**3 for element in range(1, 21)}

    return print(dct)


# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.


def task2():
    str_ = (4, 'Russia Moscow Petersburg Novgorod Kaluga', 'France Brest Paris',
            'Ukraine Kiev Donetsk Odessa', 'Belarus Minsk Brest',
            3, 'Odessa', 'Moscow', 'Novgorod')

    dict_ = {}

    for elem in str_[1: str_[0] + 1]:
        elem = elem.split()
        country = elem.pop(0)
        for city in elem:
            if city not in dict_:
                dict_.update({city: country})
            else:
                dict_[city] = (dict_[city] + ', ' + country)

    for des_city in str_[str_[0] + 2:]:
        print(dict_[des_city])
    return


# Даны два списка чисел. Посчитайте, сколько различных чисел содержится одновременно
# как в первом списке, так и во втором.


def task3():
    lst1 = [1, 3, 5, 1, 4, 5, 9]
    lst2 = [3, 5, 8, 6, 2, 7]
    result = set(lst1) & set(lst2)

    return print(len(result))


# Даны два списка чисел. Посчитайте, сколько различных чисел входит только в
# один из этих списков


def task4():
    lst1 = [1, 3, 5, 1, 4, 5, 9]
    lst2 = [3, 5, 8, 6, 2, 7]
    result = set(lst1) ^ set(lst2)

    return print(len(result))


# Каждый из N школьников некоторой школы знает Mi языков. Определите, какие языки знают
# все школьники и языки, которые знает хотя бы один из школьников.


def task5():
    num_stud = int(input("Enter the number of students: "))
    lst = []

    for student in range(num_stud):
        num_lang = int(input("Enter the number of languages: "))
        for language in range(num_lang):
            lang = input("Enter the language: ")
            lst.append(lang)

    max_lang = {lang for lang in lst if lst.count(lang) == num_stud}

    print(len(max_lang))
    for lang in max_lang:
        print(lang)
    print(len(set(lst)))
    for lang in set(lst):
        print(lang)

    return


# Во входной строке записан текст. Словом считается последовательность непробельных
# символов идущих подряд, слова разделены одним или большим числом пробелов или символами
# конца строки. Определите, сколько различных слов содержится в этом тексте.


def task6():
    str_ = 'Во входной строке записан текст. Словом считается последовательность' \
           ' непробельных символов идущих подряд, слова разделены одним или большим' \
           ' числом пробелов или символами конца строки. Определите, сколько различных' \
           ' слов содержится в этом тексте.'.split()

    return print(len(set(str_)))


# Даны два натуральных числа. Вычислите их наибольший общий делитель при помощи
# алгоритма Евклида (мы не знаем функции и рекурсию).


def task7():
    a = 462
    b = 1071

    if a > b:
        while b > 0:
            n = a % b
            a, b = b, n
        print(a)
    elif a < b:
        while a > 0:
            n = b % a
            b, a = a, n
        print(b)
    elif a == b:
        print(a)

    return
