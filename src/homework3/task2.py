#List practice
# 1. Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
# 2. Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
# 3. Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
# 4. Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
# 5. Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке этого элемента не было.

import copy
lst1 = [(el1 + el2) for el1 in 'ab' for el2 in 'bcd']
print('1. ', lst1)
print('2. ', lst1[::2])
lst2 = [(str(el) + 'a') for el in range(1, 5)]
print('3. ', lst2)
print('4. ', lst2.pop(1))
lst3 = copy.copy(lst2)
lst3.insert(1, '2a')
print('5. ', lst2, '\n', lst3)
