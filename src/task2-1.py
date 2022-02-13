lst = ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']
a = [x for x in lst]
print(a)
print(a[::2])
lst2 = [elem + "a" for elem in "1234"]
print(lst2)
print(lst2.pop(1))
lst3 = lst2.copy()
lst3.append('2a')
print(lst2)
print(lst3)