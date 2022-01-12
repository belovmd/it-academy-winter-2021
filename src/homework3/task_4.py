# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать.
# Входные данные - строка из чисел, разделенная пробелами.
# Выходные данные - количество пар.
# Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар


str_ = input('Enter a string of numbers separated by a space: ').split()
str_ran = [int(elem) for elem in str_]
count = 0
for elem in range(len(str_ran)):
    for elem1 in range(elem + 1, len(str_ran)):
        if str_ran[elem] == str_ran[elem1]:
            count += 1
print(count)

