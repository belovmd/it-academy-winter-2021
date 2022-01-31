"""List practice.

1. Use the list generator to get the following:
   ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
2. Use the previous slice list to get the following:
   ['ab', 'ad', 'bc'].
3. Use the list generator to get the following
   ['1a', '2a', '3a', '4a'].
4. With one line remove item '2a' from the previous list and print it.
5. Copy the list and add element '2a' to it,
   so that the original list does not contain this element."""

lst_ = [(a + b) for a in 'ab' for b in 'bcd']
print('1. Generated list: ', lst_)

lst_sliced = lst_[::2]
print('2. Sliced list: ', lst_sliced)

lst_num = [num + 'a' for num in '1234']
print('3. List with numbers: ', lst_num)

lst_num.pop(1)
print('4. List with removed elemetn: ', lst_num)

lst_copy = lst_num.copy()
lst_copy.append('2a')
print('5. Source list: ', lst_num, '\n   Copied list: ', lst_copy)
