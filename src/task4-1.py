lst = [int(s) for s in input().split()]
counter = 0
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] == lst[j]:
            counter += 1
print(counter)
