"""Pairs of elements.

A list of numbers is given.
Count how many pairs of elements in it are equal to each other.
Any two elements equal to each other are considered,
to form one pair to be counted.
The input is a string of numbers separated by spaces.
The output is the number of pairs.
Important: 1 1 1 1 is 3 pairs, 1 1 1 1 is 6 pairs"""

input_ = '1 1 1 2 2 8 8 8 8 8 2 4 2 1 1'
input_split = input_.split()
dict_ = {}
pairs = 0
for value in input_split:
    dict_.update(dict.fromkeys(value, input_split.count(value)))

for key in dict_:
    pairs = pairs + (dict_[key] * (dict_[key] - 1)) / 2
print(pairs)
