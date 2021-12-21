# Дан список чисел.
# Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать.

list_ = [3, 1, 1, 1, 1, 3, 3, 3]
result = 0

for elem in list_:
    if list_.count(elem) > 1:
        for i in range(list_.count(elem)):
            list_.remove(elem)
            result += list_.count(elem)
print("Number of pairs:", result)
