# Реализовать функцию get_ranges которая получает на вход
# непустой список неповторяющихся целых чисел,
# отсортированных по возрастанию,
# которая этот список “сворачивает”
#  get_ranges([0, 1, 2, 3, 4, 7, 8, 10])
#  // "0-4,7-8,10"
#  get_ranges([4,7,10]) // "4,7,10"
#  get_ranges([2, 3, 8, 9]) // "2-3,8-9"


def get_ranges(lst):
    result = ''
    for num in range(len(lst) - 1):
        if lst[num] + 1 == lst[num + 1] and lst[num] - 1 != lst[num - 1]:
            result += str(lst[num]) + '-'
        elif lst[num] + 1 == lst[num + 1] and lst[num] - 1 == lst[num - 1]:
            continue
        else:
            result += str(lst[num]) + ','
    result += str(lst[len(lst) - 1])
    return result


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
