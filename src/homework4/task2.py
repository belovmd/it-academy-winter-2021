# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.

cities = {}


for i in range(int(input('n = '))):
    line = input('input countries , cities ...').split()

    for f in line[1:]:
        cities[f] = line[0]


for m in range(int(input('m = '))):
    print(cities[input('input cities.')])
