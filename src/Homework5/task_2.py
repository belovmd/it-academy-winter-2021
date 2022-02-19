# Создайте декоратор, который хранит результаты вызовов функции
# (за все время вызовов, не только текущий запуск программы)


from datetime import datetime
from functools import wraps


def my_dec(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        with open('result_task_2.txt', 'a', encoding='1251') as result_txt:
            result_txt.write('Имя функции: {name}\n'
                             'Функция запущена: {datetime_now}\n'
                             'Результат функции: {result}\n\n'
                             .format(name=func.__name__,
                                     datetime_now=datetime.strftime(datetime.now(), '%d-%b-%y '
                                                                                    '%H:%m'),
                                     result=result))
        return result

    return wrapper


@my_dec
def function_performed(a=1, b=1):
    return '{a} + {b} = {c}'.format(a=a, b=b, c=a + b)


@my_dec
def my_func():
    return 1 + 3


function_performed()
function_performed()
function_performed()
function_performed()
my_func()
my_func()
my_func()

