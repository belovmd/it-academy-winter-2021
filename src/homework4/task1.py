"""Dict comprehensions.

Create a dictionary with the dictionary generator,
so that its keys are numbers from 1 to 20,
and the values are cubes of these numbers."""

dict_ = {_: _ ** 3 for _ in range(1, 21)}
print(dict_)
