# 3. Tuple practice

# 1 Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
lst = ["a", "b", "c"]
lst = tuple(lst)
print(lst, type(lst))

# 2 Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
tpl = ('a', 'b', 'c')
tpl = list(tpl)
print(tpl, type(tpl))

# 3 Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
a, b, c = "a", 2, "python"
print(a, b, c)

# 4 Создайте кортеж из одного элемента, чтобы при итерировании по этому элементы последовательно выводились
# значения 1, 2, 3. Убедитесь что len() исходного кортежа возвращает 1.
tpl2 = ([1, 2, 3], )
print(tpl2, type(tpl2), "\nTuple length: ", len(tpl2))
