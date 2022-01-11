# Tuple practice

# 1. Create list ['a', 'b', 'c'] and make tuple of it

lst1 = ['a', 'b', 'c']
tpl1 = tuple(lst1)
print(tpl1)

# 2. Create tuple ('a', 'b', 'c') and make list of it

tpl2 = ('a', 'b', 'c')
lst2 = list(tpl2)
print(lst2)

# 3. Make assignments a = 'a', b=2, c=’python’ in one line

a, b, c = 'a', 2, 'python'
print(a, b, c)

# 4. Create tuple with one element, so that when iterating over this the elements will sequentially
# output the values 1, 2, 3.

tpl3 = (1, 2, 3),
print('length of the tuple:', len(tpl3))
