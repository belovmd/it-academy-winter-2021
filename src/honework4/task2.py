# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.
# Входные данные
# Программа получает на вход количество стран N. Далее идет N строк, каждая строка начинается с названия страны,
# затем идут названия городов этой страны. В следующей строке записано число M,
# далее идут M запросов — названия каких-то M городов, перечисленных выше.
# Выходные данные
# Для каждого из запроса выведите название страны, в котором находится данный город.

number_countries = int(input("Enter number of countries: "))
dict_ = {}
cities = []
countries = []

for elem in range(number_countries):
    str_ = input("Enter country and cities: ")
    list_2 = str_.split()
    dict_.setdefault(list_2[0],list_2[1:])

number_cities = int(input("Enter number of cities: "))

for elem in range(number_cities):
    cities.append(input("Enter city: "))

for elem in cities:
    for key, value in dict_.items():
        if elem in value:
            countries.append(key)
    while len(countries) > 1:
        print(countries.pop(), end=", ")
    else:
        print(countries.pop())
