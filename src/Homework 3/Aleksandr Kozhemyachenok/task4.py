list_1 = [int(s) for s in input('введите числа через пробел...').split()]
len_l = len(list_1)
container = 0
for i in range(len_l):
    for j in range(i + 1, len_l):
        if a[i] == a[j]:
            container += 1
print(container)