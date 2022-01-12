import copy

# Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].


list_ab = ['a', 'b']
list_bcd = ['b', 'c', 'd']

list_rez = [elem1 + elem2 for elem1 in list_ab for elem2 in list_bcd]

print(list_rez, sep='\n')

# Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].


list_slice = list_rez[::2]

print(list_slice)

# Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].


list_numb = ['1', '2', '3', '4']
list_char = ['a']

list_rez = [elem1 + elem2 for elem1 in list_numb for elem2 in list_char]

print(list_rez)

# Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.


list_pop = list_rez.pop(1)

print(list_pop)

# Скопируйте список и добавьте в него элемент '2a'
# так чтобы в исходном списке этого элемента не было.


list_copy = copy.deepcopy(list_rez)
list_copy.append(list_pop)

print(list_copy)
