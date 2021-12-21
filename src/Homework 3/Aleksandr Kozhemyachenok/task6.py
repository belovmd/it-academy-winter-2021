list = [1, 0, 2, 0, 10, 33, 0, 1]

for i in range(len(list)):
    if list[i] == 0:
        list.append(list[i])
        del list[i]

print(list)
