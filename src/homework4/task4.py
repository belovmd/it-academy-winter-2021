"""Two lists of numbers are given.

 Count how many different numbers are on only one of these lists."""

import random

random_list_1 = random.sample(range(20, 40), 15)
random_list_2 = random.sample(range(30, 50), 15)

list1 = set(random_list_1)
list2 = set(random_list_2)

print('List1: ', list1)
print('List2: ', list2)
print('Unique in 1st list: ', list1 - list2, ' count: ', len(list1 - list2))
print('Unique in 2nd list: ', list2 - list1, ' count: ', len(list2 - list1))
