"""Tuple practice.

1. Create a list ['a', 'b', 'c'] and make it into a tuple.
2. Create a tuple ('a', 'b', 'c'), And make a list of it.
3. Make the following one-line assignments a = 'a', b=2, c='python'.
4. Create a tuple of one item so that iterating over that,
   item will consistently output values 1, 2, 3.
   Make sure that len() of the original tuple returns 1."""

lst_ = ['a', 'b', 'c']
tuple_ = tuple(lst_)
print('1. Tuple converted from the list: ', tuple_, type(tuple_))

lst_ = list(tuple_)
print('2. List converted from the tuple: ', lst_, type(lst_))

a, b, c = 'a', 2, 'python'
print('3. Assigned variables: ', a, b, c)

tuple_ = ([1, 2, 3],)
print('4. Tuple lenght: ', len(tuple_), end=' | Iterated tuple: ')
for _ in tuple_[0]:
    print(_, end=', ')
