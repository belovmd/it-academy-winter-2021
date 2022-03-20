# 2. Города
# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.

import string

countries_amount = int(input("Введите количество стран: "))
countries_cities = {}

for countries in range(1, countries_amount + 1):
    input_countries = input("Введите название {n}-й страны и её города: ".format(n=countries)
                            ).translate(str.maketrans("", "", string.punctuation)).split()
    countries_cities[input_countries[0]] = input_countries[1:]

cities_amount = int(input("Введите количество городов: "))
cities = []

for city in range(1, cities_amount + 1):
    cities.append(input("Введите название {n}-го города: ".format(n=city)))

for city2 in cities:
    for country in countries_cities:
        if city2 in countries_cities[country]:
            print("{country}: {city}".format(country=country, city=city2))
