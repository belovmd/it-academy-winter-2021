lst = ['a', 'b', 'b', 'c', 'd']
lst2 = []
for el in lst:
    if lst.count(el) == 1:
        lst2.append(el)
else:
    print(lst2)
