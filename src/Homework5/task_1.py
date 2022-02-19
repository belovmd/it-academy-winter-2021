# # Оформите решение задач из прошлых домашних работ в функции.
# # Напишите функцию runner. (все станет проще когда мы изучим модули, getattr и setattr)
# # a. runner() – все фукнции вызываются по очереди
# # b. runner(‘func_name’) – вызывается только функцию func_name.
# # c. runner(‘func’, ‘func1’...) - вызывает все переданные функции


from sys import _getframe


class MyClass:

    def __init__(self, lst):
        self.lst = lst

    def output_of_different(self):

        list_ = self.lst
        new_list = []
        for elem in list_:
            if list_.count(elem) == 1:
                new_list.append(elem)
        return new_list

    def sorted_fun(self):

        for elem in self.lst:
            if elem == 0:
                self.lst.remove(elem)
                self.lst.append(elem)
        return self.lst

    def runner(self, *name):

        lst_func = []
        result = []
        if not name:
            for func in dir(MyClass):
                lst_func.append(func)
                if func[0] == '_' and func[0:: -1] == '_':
                    lst_func.remove(func)
            lst_func.remove(_getframe().f_code.co_name)
            for func in lst_func:
                get_func = getattr(MyClass, func)
                result.append(get_func(self))
        else:
            for func in name:
                if func in dir(MyClass):
                    get_func = getattr(MyClass, func)
                    result.append(get_func(self))
                else:
                    result = 'Function not found!!! {name}'.format(name=name)
        return result


run = MyClass([1, 2, 0, 3, 1, 2, 3, 4, 5, 0, 2, 10])

print(run.runner())
print(run.runner("sorted_fun"))
print(run.runner("sorted_fun", 'output_of_different'))
