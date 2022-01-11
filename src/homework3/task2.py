# List practice

import copy

# 1. Use list comprehension to get: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].

lst = [a + b for a in "ab" for b in "bcd"]
print(lst)

# 2. Use slice on the previous list to get next: ['ab', 'ad', 'bc'].

lst = lst[::2]
print(lst)

# 3. Use list comprehension to get: ['1a', '2a', '3a', '4a'].

lst2 = [a + b for a in "1234" for b in "a"]
print(lst2)

# 4. Delete '2a' from last list by one line and print it.

print(lst2.pop(1))

# 5. Copy list and add '2a' in it so that in original

lst3 = copy.deepcopy(lst2)
lst3.insert(1, "2a")
print(lst3, "Origin list:", lst2)
