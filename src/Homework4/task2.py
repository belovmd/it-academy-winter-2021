'''2.	Города
Дан список стран и городов каждой страны.
Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N.
Далее идет N строк, каждая строка начинается с названия страны,
затем идут названия городов этой страны.
В следующей строке записано число M,
далее идут M запросов — названия каких-то M городов,
перечисленных выше.

Выходные данные

Для каждого из запроса выведите название страны,
в котором находится данный город.
Примеры

Входные данные
4
Russia Moscow Petersburg Novgorod Kaluga
France Brest Paris
Ukraine Kiev Donetsk Odessa
Belarus Minsk Brest

3
Odessa
Moscow
Novgorod

Выходные данные
Ukraine
Russia
Russia
Задачу поместите в файл task2.py в папке src/homework4.
'''
dict_countries = {}
list_request = []
dict_input = dict.fromkeys(key for key in range(int(input('Введите количество стран: '))))
for key in dict_input:
    dict_input[key] = input('Введите страну и города: ').split()
for list_ in dict_input.values():
    dict_countries[tuple([list_[elem] for elem in range(1, len(list_))])] = list_[0]
n = int(input('Введите количество городов: '))
for _ in range(n):
    list_request.append(str(input('Введите город: ')))
for key in dict_countries:
    for elem in key:
        for city in list_request:
            if elem == city:
                print(dict_countries[key])
