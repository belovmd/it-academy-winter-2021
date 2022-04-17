list = ['a', 'b', 'c', 'd', 'b', 'c', 'd', 'c', 'f', 5]
result = []

for i in range(len(list)):
    if list.count(list[i]) == 1:
        result.append(list[i])

print(result)
