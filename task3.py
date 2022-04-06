def get_ranges(list):
    string = ""
    dict = {}
    num1 = num2 = 0
    for element in list:
        if element == num2 + 1:
            num2 = element
            dict[num1] = dict.get(num1, 0) + 1
        else:
            dict.setdefault(element, 0)
            num1 = num2 = element
    for key, value in dict.items():
        if value:
            string += str(key) + "-" + str(key + value) + ","
        else:
            string += str(key) + ","
    return string.strip(",")


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))