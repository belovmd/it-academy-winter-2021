# Даны два списка чисел.
# Посчитайте, сколько различных чисел входит только в один из этих списков

list_1 = [elem for elem in range(5, 15)]
list_2 = [elem for elem in range(1, 10,)]

set_1 = set(list_1)
set_2 = set(list_2)
print(set_1 - set_2)
