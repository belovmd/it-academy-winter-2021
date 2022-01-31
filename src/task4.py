"""Pairs of elements.

A list of numbers is given.
Count how many pairs of elements in it are equal to each other.
Any two elements equal to each other are considered to form one pair to be counted.
The input is a string of numbers separated by spaces.
The output is the number of pairs.
Important: 1 1 1 1 is 3 pairs, 1 1 1 1 is 6 pairs"""

input_ = '1 1 1 2 2 8 8 8 8 8 2 4 2 1 1'
input_split = input_.split()
dict_ = {}
pairs = 0
for _ in input_split:
    dict_.update(dict.fromkeys(_, input_split.count(_)))

for _ in dict_:
    # Number of pairs = (Total number of items X Total number of items - 1) / 2
    pairs = pairs + (dict_[_] * (dict_[_] - 1)) / 2
print(pairs)
