# 3
# Реализовать функцию get_ranges которая получает на вход
# непустой список неповторяющихся целых чисел, отсортированных
# по возрастанию, которая этот список “сворачивает”
#  get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
#  get_ranges([4,7,10]) // "4,7,10"
#  get_ranges([2, 3, 8, 9]) // "2-3,8-9"


def get_ranges(list1):
    x = len(list1)
    result = []
    str_ = str(list1[0])
    for number in range(1, x):
        if list1[number] == list1[number - 1] + 1:
            str_ = str_ + '-' + str(list1[number])
        else:
            if len(str_) > 1:
                result.append(str_[0] + '-' + str_[-1])
            else:
                result.append(str_)
            str_ = str(list1[number])
    result.append(str_)
    result_str = ','.join(result)
    return print(result_str)


lst1 = [0, 1, 2, 3, 4, 7, 8, 10]
get_ranges(lst1)
