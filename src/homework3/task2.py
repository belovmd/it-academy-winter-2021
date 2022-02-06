# task 2 List practice

"""
1. Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
2. Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
3. Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
4. Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
5. Скопируйте список и добавьте в него элемент '2a' так,
чтобы в исходном списке этого элемента не было.
"""

# subtask 1
list_1 = [letter_1 + letter_2 for letter_1 in "ab" for letter_2 in "bcd"]
print(list_1)

# subtask 2
print(list_1[::2])

# subtask 3
list_2 = [str(number) + "a" for number in "1234"]
print(list_2)

# subtask 4
print(list_2.pop(1))

# subtask 5
list_3 = list_2.copy()
list_3.append("2a")
print(list_3)
