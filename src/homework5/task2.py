# Создайте декоратор, который хранит результаты вызовов функции (за все время вызовов,
# не только текущий запуск программы)


from datetime import datetime


def memoize_func(f):
    memo = dict()
    counter = 0

    def func(*args):
        nonlocal memo
        nonlocal counter
        result = f(*args)
        start_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        lst = [f.__name__, start_time, args, result]
        memo[counter] = lst
        print(memo)
        counter += 1
        return result

    return func


@memoize_func
def my_func(a, b):
    return a ** b


print(my_func(3, 5), '\n')
print(my_func(3, 4), '\n')
print(my_func(3, 2), '\n')
print(my_func(3, 5), '\n')
print(my_func(3, 4), '\n')
print(my_func(3, 5), '\n')
