# task 2 Города
"""
Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N. Далее идет N строк, каждая строка начинается с названия страны, затем идут названия городов этой страны. В следующей строке записано число M, далее идут M запросов — названия каких-то M городов, перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны, в котором находится данный город.
Примеры

Входные данные
3
USA LA Miami
France Brest Paris
Belarus Minsk Brest


3
Brest
LA
Minsk

Выходные данные
Belarus, France
USA
Belarus
"""

number_of_countries = int(input("Enter the number of strings: "))
dict_world = {}
list_of_cities, list_of_countries = [], []
for number in range(number_of_countries):
    input_string = input("Enter the country and cities: ").split()
    dict_world.setdefault(input_string[0], input_string[1:])

number_of_requests = int(input("Enter the number of cities: "))
for request in range(number_of_requests):
    list_of_cities.append(input("Enter the city: "))

for city in list_of_cities:
    for key, value in dict_world.items():
        if city in value:
            list_of_countries.append(key)
    while len(list_of_countries) > 1:
        print(list_of_countries.pop(), end=", ")
    else:
        print(list_of_countries.pop())
