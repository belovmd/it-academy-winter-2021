# task 3 Tuple practice

"""
1. Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
2. Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
3. Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
4. Создайте кортеж из одного элемента, чтобы при итерировании по этому элементы последовательно
выводились значения 1, 2, 3. Убедитесь что len() исходного кортежа возвращает 1.
"""

# subtask 1
list_ = [letter for letter in "abc"]
print(tuple(list_))

# subtask 2
tuple_ = tuple([letter for letter in "abc"])
print(list(tuple_))

# subtask 3
a, b, c = "a", 2, "python"
print(a, b, c)

# subtask 4
new_tuple = ([1, 2, 3], )
for number in new_tuple[0]:
    print(number)
print("new_tuple's length is: ", len(new_tuple))
