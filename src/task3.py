import copy
lst = ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']
a = [x for x in lst]
print(a)
b = a[0:6:2]
print(b)
lst_2 = ['1a', '2a', '3a', '4a']
c = [x for x in lst_2]
print(c)
d = lst_2.pop(1)
# print(d)
print(lst_2)
lst_3 = copy.deepcopy(lst_2)
lst_3.append('2a')
print(lst_3)
