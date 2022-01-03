str_ = input('input string...')
count_big = 0
count_small = 0

for el in range(len(str_)):
    if 'A' <= str_[el] <= 'Z':
        count_big += 1
    elif 'a' <= str_[el] <= 'z':
        count_small += 1

print('count_big =' + str(count_big))
print('count_small =' + str(count_small))
