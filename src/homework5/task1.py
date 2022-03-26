# Execute task soling from the previous homeworks by functions.
# Write the function called runner.

class Tasks:
    @staticmethod
    def pairs(lst):
        count = 0
        step = 1
        for el in lst:
            count += lst[step::].count(el)
            print(lst[step::])
            step += 1
        print(count)

    @staticmethod
    def unique(lst):
        dct = {}
        for el in lst:
            dct[el] = dct.get(el, 0) + 1
        for key in dct:
            if dct[key] == 1:
                print(key)

    @staticmethod
    def sort(lst):
        for el in lst:
            if not el:
                lst.remove(el)
                lst.append(el)
        print(lst)


def runner(*args):
    if not args:
        for func in dir(Tasks):
            if func[0] != "_":
                function = getattr(Tasks, func)
                print(function.__name__)
                function([1, 2, 2, 0, 4, 5, 0, -2, -3])
    for func in args:
        if func in dir(Tasks):
            function = getattr(Tasks, func)
            print(function.__name__)
            function([1, 2, 2, 0, 4, 5, 0, -2, -3])


runner()
runner('pairs')
runner('sort', 'unique')
