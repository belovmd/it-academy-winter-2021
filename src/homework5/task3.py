# 3. Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся
# целых чисел, отсортированных по возрастанию, которая этот список “сворачивает”
#  get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
#  get_ranges([4,7,10]) // "4,7,10"
#  get_ranges([2, 3, 8, 9]) // "2-3,8-9"

def get_ranges(list_):
    if list_:
        list_ = sorted(list_)
        first_num = last_num = 0
        dict_ = {}

        for num in list_:
            if num == last_num + 1:
                last_num = num
                dict_[first_num] = dict_.get(first_num, 0) + 1
            else:
                dict_.setdefault(num, 0)
                first_num = last_num = num

        result = ""

        for key, value in dict_.items():
            if value:
                result += "{first}-{last},".format(first=key, last=key+value)
            else:
                result += "{first},".format(first=key)

        return result.strip(",")
    else:
        return "Список пуст"


print(get_ranges([]))
print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
