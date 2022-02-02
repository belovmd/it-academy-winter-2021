# Дан список чисел.
# Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать.

list_ = [3, 1, 1, 1, 1, 3, 3, 3, 5]
dict_ = {}
result = 0

for elem in list_:
    dict_[elem] = dict_.get(elem, 0) + 1

for value in dict_.values():
    if value > 1:
        result += (value * (value - 1)) / 2

print("Number of pairs:", int(result))
