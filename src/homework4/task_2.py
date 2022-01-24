# Города
# Дан список стран и городов каждой страны.
# Затем даны названия городов. Для каждого города укажите, в какой стране он находится.
# Входные данные
# Программа получает на вход количество стран N.
# Далее идет N строк, каждая строка начинается с названия страны,
# затем идут названия городов этой страны. В следующей строке записано число M,
# далее идут M запросов — названия каких-то M городов, перечисленных выше.
# Выходные данные
# Для каждого из запроса выведите название страны, в котором находится данный город.
# Примеры
#
# Входные данные
# 2
# Russia Moscow Petersburg Novgorod Kaluga
# France Brest Paris
# Ukraine Kiev Donetsk Odessa
# Belarus Minsk Brest
#
# 3
# Odessa
# Moscow
# Novgorod
#
# Выходные данные
# Ukraine
# Russia
# Russia


number_countries = input('Number of countries: ')

dict_countries = dict()
for num in range(int(number_countries)):
    enter_countries = input('Enter country name followed by city: ')
    list_country_and_city = enter_countries.split()
    dict_countries.update({list_country_and_city[0]: list_country_and_city[1:]})

list_cities = list()
number_cities = input('Number of cities: ')
for num in range(int(number_cities)):
    list_cities.append(input("Enter city name: "))

list_countries = list()
for city in list_cities:
    for key, value in dict_countries.items():
        if city in value:
            list_countries.append(key)
    while len(list_countries) > 1:
        print('{city}: '.format(city=city), list_countries.pop(), end=', ')
    else:
        print('{city}: '.format(city=city), list_countries.pop())
