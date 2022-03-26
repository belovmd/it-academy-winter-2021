# Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся
# целых чисел, отсортированных по возрастанию, которая этот список “сворачивает”


def get_ranges(lst):
    result = []
    list_app = [lst[0]]
    first = lst[0]

    for i in lst:
        if i == (first + 1):
            if i != lst[-1]:
                list_app.append(i)
                first = i
            else:
                list_app.append(i)
                pair = str(list_app[0]) + '-' + str(list_app[-1])
                result.append(pair)
        elif len(list_app) > 1:
            if i != lst[-1]:
                pair = str(list_app[0]) + '-' + str(list_app[-1])
                result.append(pair)
                first = i
                list_app = [i]
            else:
                pair = str(list_app[0]) + '-' + str(list_app[-1])
                result.append(pair)
                result.append(i)
        elif (first + 1) not in lst:
            result.append(i)

    return print(result)


get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  # "0-4, 7-8, 10"
get_ranges([4, 7, 10])  # "4, 7, 10"
get_ranges([2, 3, 8, 9])  # "2-3, 8-9"
