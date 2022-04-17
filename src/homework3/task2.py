lst1 = [[a + b] for a in 'ab' for b in 'bcd']
print(lst1)

lst1 = lst1[::2]
print(lst1)

lst2 = [[str(a) + b] for a in range(1, 5) for b in 'a']

print(lst2)
print(lst2.pop(1))

lst3 = lst2.copy()
lst3.insert(1, '2a')
print(lst2)
print(lst3)
