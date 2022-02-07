# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.


str_ = (4, 'Russia Moscow Petersburg Novgorod Kaluga', 'France Brest Paris',
        'Ukraine Kiev Donetsk Odessa', 'Belarus Minsk Brest',
        3, 'Odessa', 'Moscow', 'Novgorod')

dict_ = {}
des_country = []

for elem in str_[1: str_[0] + 1]:
  el = elem.split()
  country = el.pop(0)
  for city in el:
    if city not in dict_:
      dict_.update({city: country})
    else:
      dict_[city] = (dict_[city] + ', ' + country)

for des_city in str_[str_[0] + 2:]:
  des_country.append(dict_[des_city])

print(des_country)
