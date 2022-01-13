# 2. List practice

# 1 Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
lst_gen = [elem1 + elem2 for elem1 in "ab" for elem2 in "bcd"]
print(lst_gen)

# 2 Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
print(lst_gen[::2])

# 3 Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
lst_gen2 = [elem + "a" for elem in "1234"]
print(lst_gen2)

# 4 Одной строкой удалите элемент '2a' из прошлого списка и напечатайте его.
print(lst_gen2.pop(1))

# 5 Скопируйте список и добавьте в него элемент '2a' так,
# чтобы в исходном списке этого элемента не было.
lst_gen3 = lst_gen2.copy()

lst_gen3.append("2a")   # или lst_gen3.insert(1, "2a")
print(lst_gen2)
print(lst_gen3)
