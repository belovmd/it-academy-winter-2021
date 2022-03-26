# Create the decorator that has results of function calls.

from datetime import datetime
from functools import wraps
from random import randint


def counter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        with open('text.txt', 'a', encoding='utf-8') as data_txt:
            data_txt.write('Function {name} was called {time} with '
                           'result :'
                           ' {result}\n'.format(name=func.__name__,
                                                time=datetime.now(),
                                                result=result))
        return result

    return wrapper


@counter
def random_num():
    return randint(1, 1000)


random_num()
random_num()
random_num()
random_num()
random_num()
random_num()
random_num()
random_num()
random_num()
