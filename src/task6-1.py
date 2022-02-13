lst = [4, 0, 0, 1, 0, 2]
for el in lst:
    if el == 0:
        lst.remove(el)
        lst.append(0)
print(lst)