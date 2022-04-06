from datetime import datetime
import time


def call(func):
    def wrapper(a, b, lag=0):
        start = datetime.now()
        func(a, b, lag)
        end = datetime.now()
        call = (end - start).total_seconds() * 1000
        print(f'>> функция {func.__name__} время: {call}')
    return wrapper


@call
def with_lag(a, b, lag=0):
    print('сложить', a, b, lag)
    time.sleep(lag)
    return a + b


print('старт')
with_lag(11, 33)
with_lag(11, 33, 1)
print('конец')
