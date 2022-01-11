# ordered list

# There is a list of integers. Need to move all nonzero elements to the left side of the list
# without changing their order, and all zeros to the right side. The order of nonzero elements
# can't be changed, an additional list cannot be used, the task must be completed in one pass
# through the list. Print the resulting list.

lst = [int(number) for number in input("Elements: ").split()]
for el in lst:
    if not el:
        lst.remove(el)
        lst.append(el)
print(lst)
