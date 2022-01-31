"""A list of integers is given.

You must move all non-zero elements to the left side of the list,
without changing their order, and all zeros to the right side.
The order of non-zero elements cannot be changed,
an additional list cannot be used.
The task must be performed in one pass through the list.
Print the resulting list."""

lst_ = [3, 0, 0, 1, 2, 1, 10, 0, 3, 1, 1, 0, 4, 1, 0]

for element in lst_:
    if not element:
        lst_.remove(element)
        lst_.append(element)
print(lst_)
