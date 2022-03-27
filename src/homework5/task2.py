# 2
# Создайте декоратор, который хранит результаты вызовов функции
# (за все время вызовов, не только текущий запуск программы)

from datetime import datetime

history = []


def history_calls(func):
    def wrapper(*args, **kwargs):
        global history
        result = func(*args, **kwargs)
        name = func.__name__
        time_now = str(datetime.now())
        ar = args if args else ''
        kw = kwargs if kwargs else ''
        arguments = [*ar, *kw]
        about_func = {'Имя функции': name,
                      'Время вызова': time_now,
                      'Переданные аргументы': arguments,
                      'Результат': result}
        history.append(about_func)
        return history
    return wrapper


@history_calls
def add_one(x):
    return x + 1


@history_calls
def add_two(y):
    return y + 2


@history_calls
def hard_func(a, **kwargs):
    b = a + 1
    result = b, kwargs
    return result


print(add_one(3))
print(add_one(99))
print(add_two(1))
print(hard_func(1, b='one'))
