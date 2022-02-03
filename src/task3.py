# Реализовать функцию get_ranges которая получает
# на вход непустой список неповторяющихся целых чисел,
# отсортированных по возрастанию, которая этот список “сворачивает”
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
# get_ranges([4,7,10]) // "4,7,10"
# get_ranges([2, 3, 8, 9]) // "2-3,8-9"

def get_ranges(lst):
    str_ = ""
    dict_ = {}
    first_number = last_number = 0
    for elem in lst:
        if elem == last_number + 1:
            last_number = elem
            dict_[first_number] = dict_.get(first_number, 0) + 1
        else:
            dict_.setdefault(elem, 0)
            first_number = last_number = elem
    for key, value in dict_.items():
        if value:
            str_ += str(key) + "-" + str(key + value) + ","
        else:
            str_ += str(key) + ","
    return str_.strip(",")

print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
