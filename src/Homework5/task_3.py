# Реализовать функцию get_ranges
# которая получает на вход непустой список неповторяющихся целых чисел,
# отсортированных по возрастанию, которая этот список “сворачивает”
#  get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
#  get_ranges([4,7,10]) // "4,7,10"
#  get_ranges([2, 3, 8, 9]) // "2-3,8-9"


def get_ranges(lst):
    dct = dict()
    last_num = first_num = 0
    res = ''
    for elem in lst:
        if elem == last_num + 1:
            last_num = elem
            dct[first_num] = dct.get(first_num, 0) + 1
        else:
            dct.setdefault(elem, 0)
            last_num = first_num = elem

    for key, value in dct.items():
        if value:
            res += '{first} - {end}, \t'.format(first=key, end=key + value)
        else:
            res += '{first}, \t'.format(first=key)
    return res.strip(', ')


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
