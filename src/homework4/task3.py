"""Two lists of numbers are given.

Count how many different numbers are contained simultaneously
in both the first list and the second."""

import random

random_list_1 = random.sample(range(0, 50), 15)
random_list_2 = random.sample(range(0, 50), 15)

list1 = set(random_list_1)
list2 = set(random_list_2)

print('List1: ', list1)
print('List2: ', list2)
print('Different nubmers in the lists: ', list1 & list2)
print('How many different numbers in the lists: ', len(list1 & list2))
