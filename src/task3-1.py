lst1 = ['a', 'b', 'c']
lst2 = tuple(lst1)
print(lst2, type(lst2))
tpl1 = ('a', 'b', 'c')
tpl2 = list(tpl1)
print(tpl2, type(tpl2))
a, b, c = "a", 2, "python"
print(a, b, c)
tpl3 = ([1, 2, 3], )
for element in tpl3[0]:
    print(element)
print(len(tpl3))
