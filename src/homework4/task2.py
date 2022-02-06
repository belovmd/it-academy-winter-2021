# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.
# Входные данные
# Программа получает на вход количество стран N. Далее идет N строк, каждая
# строка начинается с названия страны, затем идут названия городов этой страны.
# В следующей строке записано число M, далее идут M запросов — названия
# каких-то M городов, перечисленных выше.
# Выходные данные
# Для каждого из запроса выведите название страны, в котором находится данный город.

numb_countries = int(input('Введите число стран: '))
dict_cities = {}
for _ in range(numb_countries):
    country_cities = input('Введите страну и города:').split()
    country, cities = country_cities[0], country_cities[1:]
    dict_cities[country] = cities
numb_request = int(input('Введите число запросов: '))
list_cities = []
for _ in range(numb_request):
    list_cities.append(input('Введите название города: '))
list_countries = []
for city in list_cities:
    for key, value in dict_cities.items():
        if city in value:
            list_countries.append(key)
print(list_countries)
