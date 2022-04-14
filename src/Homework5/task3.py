'''
3.	Реализовать функцию get_ranges которая получает на вход
непустой список неповторяющихся целых чисел, отсортированных по возрастанию,
которая этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"
Задачу поместите в файл task3.py в папке src/homework5.
'''


def get_ranges(lst):
    str_ = ''
    str_ = str_ + str(lst[0])
    for i in range(1,  (len(lst) - 1)):
        if (lst[i] - lst[i - 1] > 1) and (lst[i + 1] - lst[i] == 1):
            str_ = str_ + ','
            str_ = str_ + str(lst[i])
        if (lst[i] - lst[i - 1] == 1) and (lst[i + 1] - lst[i] > 1):
            str_ = str_ + '-'
            str_ = str_ + str(lst[i])
        elif (lst[i] - lst[i - 1] > 1) and (lst[i + 1] - lst[i] > 1):
            str_ = str_ + ','
            str_ = str_ + str(lst[i])
    if lst[-1] - lst[-2] > 1:
        str_ = str_ + ','
    if lst[-1] - lst[-2] == 1:
        str_ = str_ + '-'
    str_ = str_ + str(lst[-1])
    return str_


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
