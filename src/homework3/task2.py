# Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
# Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
# Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
# Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
# Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке этого элемента не было.

list_ = [(a + b) for a in 'ab' for b in 'bcd']
print(list_)
print(list_[::2])
list_two = [b + 'a' for b in '1234']
print(list_two.pop(1))
list_three = list_two.copy()
list_three.append("2a")
print(list_two)
print(list_three)
