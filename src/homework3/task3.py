# Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
# Создайте кортеж ('a', 'b', 'c'), И сделайте из него список

list_ = ['a', 'b', 'c']
tuple_ = tuple(list_)
print(tuple_, type(tuple_))

# Создайте кортеж ('a', 'b', 'c'), И сделайте из него список

list_two = list(tuple_)
print(list_two, type(list_two))

# Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.

a, b, c = 'a', 2, 'python'
print(a, b, c)

# Создайте кортеж из одного элемента, чтобы при итерировании по этому
# элементы последовательно выводились значения 1, 2, 3.
# Убедитесь что len() исходного кортежа возвращает 1.

tuple_two = [1, 2, 3],
print(len(tuple_two))
