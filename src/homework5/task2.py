# 2. Создайте декоратор, который хранит результаты вызовов функции
# (за все время вызовов, не только текущий запуск программы)

from datetime import datetime
import time


def logs_dec(func):
    def wrapper(*args, **kwargs):
        func_start = datetime.now()

        func_result = func(*args, **kwargs)

        func_finish = datetime.now()
        time_result = func_finish - func_start

        with open("data_hw5/task2_logs.txt", "a", encoding="utf-8") as logs:
            logs.write(
                "Имя функции: {f}\n"
                "Переданные аргументы: {arg}\n"
                "Результат выполнения функции: {r}\n"
                "Старт выполнения функции: {ts}\n"
                "Конец выполнения функции: {tf}\n"
                "Потрачено времени: {tr}\n\n".format(f=func.__name__,
                                                     arg=(args, kwargs),
                                                     r=func_result,
                                                     ts=func_start,
                                                     tf=func_finish,
                                                     tr=time_result,
                                                     )
            )

        return func_result
    return wrapper


@logs_dec
def example_func(a, b):
    time.sleep(2)
    return a * b


def example_func2(a, b):
    time.sleep(2)
    return a + b


func2 = logs_dec(example_func2)

example_func(2, 4)
time.sleep(2)
example_func(2, 6)
time.sleep(2)
example_func(2, 8)
time.sleep(2)
func2(2, 4)
time.sleep(2)
func2(2, 6)
time.sleep(2)
func2(2, 8)
