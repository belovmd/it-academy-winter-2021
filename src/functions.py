# Функции для task1

# hw2 task8

def bank():
    a = int(input("Enter deposit amount: "))
    years = int(input("Enter number of years: "))
    for elem in range(years):
        a = a * 1.1
    return a


# hw2 task8

def sum_numbers():
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    list_ = [first_number, second_number]
    list_.sort()
    result = 0

    if list_[0] != list_[1]:
        for elem in range(list_[0], list_[1] + 1):
            result += elem
    else:
        result = list_[0]

    return result


# hw2 task3

def clear_str():
    input_str = input("Enter string: ")
    str_without_space = input_str.replace(" ", "")
    output_str = ""

    for elem in str_without_space:
        if elem not in output_str:
            output_str += elem

    return output_str


# hw3 task4

def number_of_pairs():
    list_ = [1, 2, 3, 1, 1]
    dict_ = {}
    result = 0

    for elem in list_:
        dict_[elem] = dict_.get(elem, 0) + 1

    for value in dict_.values():
        if value > 1:
            result += (value * (value - 1)) / 2

    return int(result)


# hw4 task7

def max_divisor():
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    list_ = []

    if first_number and second_number:
        list_.append(first_number)
        list_.append(second_number)
        list_.sort(reverse=True)

        while list_[-1]:
            list_.append(list_[-2] % list_[-1])

        return list_[-2]
    else:
        print("Integer must be more than zero")
