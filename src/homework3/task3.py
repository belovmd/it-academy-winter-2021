lst_1 = ['a', 'b', 'c']

tpl_1 = tuple(lst_1)
print(tpl_1, type(tpl_1))

a, b, c = 'a', 2, 'python'
print(a, b, c)

tpl_2 = ('1, 2, 3',)
len_tpl_2 = len(tpl_2)

for i in tpl_2:
    print(i)

print(len_tpl_2)
