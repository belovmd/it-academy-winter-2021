def task6_4():
    text = "Hello World"
    return len(set(text))


def task5_3():
    lst = ['a', 'b', 'b', 'c', 'd']
    lst2 = []
    for el in lst:
        if lst.count(el) == 1:
            lst2.append(el)
    return lst2
