# Создайте декоратор, который хранит результаты вызовов функции
# (за все время вызовов, не только текущий запуск программы)

import time


def dec(func):

    def wrapper(*args, **kwargs):

        write = "Function {}, Time {}, Result {}, Variables {} "
        with open("result_task2", 'a') as fh:
            fh.write(write.format(func.__name__, time.asctime(), func(*args), args) + "\n")
        return func
    return wrapper


@dec
def func(b):
    return b


@dec
def func_two(a):
    return a


@dec
def func_three(a, b, c):
    return a + b + c


func("bbb")
func_two(7)
func_three("a", "124", "mmm")
