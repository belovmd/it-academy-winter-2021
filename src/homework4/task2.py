# 2 Города
# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.

n = int(input('Введите кол-во строк: '))
dct = {}
for _ in range(n):
    str_ = input('Введите страну и города: ')
    first_space = str_.find(' ')
    country = str_[:first_space]
    cities = str_[first_space + 1:].split()
    dct[country] = cities
list1 = dct.items()
m = int(input('Введите кол-во запросов: '))
lst = [input('Введите запрос: ') for _ in range(m)]
result = []
for city in lst:
    for tpl in list1:
        if city in tpl[1]:
            result.append(tpl[0])
print(*result, sep='\n')
