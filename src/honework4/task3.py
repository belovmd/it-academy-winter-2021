# Даны два списка чисел.
# Посчитайте, сколько различных чисел содержится одновременно как в первом списке, так и во втором.

list_1 = [elem for elem in range(1, 10)]
list_2 = [elem for elem in range(1, 10, 2)]

set_1 = set(list_1)
set_2 = set(list_2)
print(set_1 & set_2)
