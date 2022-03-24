# Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся
# целых чисел, отсортированных по возрастанию, которая этот список “сворачивает”


def get_ranges(lst):
    result = []
    appe = [lst[0]]
    st = lst[0]

    for i in lst:
        if i == (st + 1):
            if i != lst[-1]:
                appe.append(i)
                st = i
            else:
                appe.append(i)
                pair = str(appe[0]) + '-' + str(appe[-1])
                result.append(pair)
        elif len(appe) > 1:
            if i != lst[-1]:
                pair = str(appe[0]) + '-' + str(appe[-1])
                result.append(pair)
                st = i
                appe = [i]
            else:
                pair = str(appe[0]) + '-' + str(appe[-1])
                result.append(pair)
                result.append(i)
        elif (st + 1) not in lst:
            result.append(i)

    return print(result)


get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  # "0-4, 7-8, 10"
get_ranges([4, 7, 10])  # "4, 7, 10"
get_ranges([2, 3, 8, 9])  # "2-3, 8-9"
