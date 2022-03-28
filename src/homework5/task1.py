# 1
# Оформите решение задач из прошлых домашних работ в функции.
# Напишите функцию runner. (все станет проще когда мы изучим
# модули, getattr и setattr)
# runner() – все фукнции вызываются по очереди
# runner(‘func_name’) – вызывается только функцию func_name.
# runner(‘func’, ‘func1’...) - вызывает все переданные функции


def unic_elements():
    string = input('Введите числа через пробел: ')
    list_ = string.split()
    result = [el for el in list_ if list_.count(el) == 1]
    return result


def zero_to_end():
    string = input('Введите числа через пробел: ')
    lst = [int(el) for el in string.split()]
    count_zero = lst.count(0)
    while count_zero > 0:
        lst.remove(0)
        lst.append(0)
        count_zero -= 1
    return lst


def fizzbuzz():
    a = int(input('Введите первое число: '))
    b = int(input('Введите последнее число: '))
    result = []
    for number in range(a, b + 1):
        if not number % 15:
            result.append('FizzBuzz')
        elif not number % 3:
            result.append('Fizz')
        elif not number % 5:
            result.append('Buzz')
        else:
            result.append(number)
    return print(*result, sep='\n')


def count_of_couple():
    string = input('Введите строку: ')
    str_new = string + ' '
    counter = 0
    n = len(str_new)
    for i in range(0, n, 2):
        counter += str_new.count(str_new[i], i + 2, n)
    return counter


def runner(*args):
    function_dict = {name: obj for (name, obj) in globals().items()
                     if hasattr(obj, '__class__') and obj.__class__.__name__ == 'function'}
    del function_dict['runner']
    if not args:
        functions_to_run = function_dict
    else:
        functions_to_run = {name: function_dict[name] for name in args}
    result = []
    for name in functions_to_run:
        result.append(functions_to_run[name]())
    return print(*result, sep='\n')


runner('fizzbuzz')
