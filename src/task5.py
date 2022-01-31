"""Unique items in the list.
A list is given. Output the elements that occur only once in the list.
The items should be printed in the order in which they appear in the list."""

lst_ = [1, 1, 2, 3, 3, 2, 4, 5, 5, 7, 'a', 'b', 'a', 'c']

for _ in lst_:
    if lst_.count(_) == 1:
        print(_)
