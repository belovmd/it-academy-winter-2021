"""Cities.

A list of countries and cities in each country is given.
Then the names of the cities are given.
For each city, specify in which country it is located.

Input data
The program gets as input the number of countries N.
Then follows N lines, each line starts with the name of the country,
then follows the names of the cities of that country.
The next line contains number M, then M queries - the names of some M cities,
listed above.

Output data
For each of the queries print the name of the country
in which the city is located."""

country_count = int(input('Input the number of countries: '))

country_town = dict()
for num in range(country_count):
    input_country_town = input('Enter country and towns: ').split()
    country = input_country_town[0]
    town = input_country_town[1:]
    country_town.update({country: town})

town_count = int(input('Number of cities: '))

towns = list()
for num in range(town_count):
    towns.append(input("Enter city name: "))

countries = list()
for town in towns:
    for key, value in country_town.items():
        if town in value:
            countries.append(key)

while countries:
    print(countries.pop(), end=", ")
