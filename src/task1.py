# Оформите решение задач из прошлых домашних работ в функции. Напишите функцию runner.
# (все станет проще когда мы изучим модули, getattr и setattr)
# runner() – все фукнции вызываются по очереди
# runner(‘func_name’) – вызывается только функцию func_name.
# runner(‘func’, ‘func1’...) - вызывает все переданные функции


import task1_prev


def runner(*args):
    input = {
        'new_string': 'abc cde def',
        'counter': [2, 6, 8, 2, 9, 6, 2, 2, 6],
        'fib2': 5
    }

    result = []
    for element in dir(task1_prev):
        if callable(getattr(task1_prev, element)):
            result.append(element)
    if args:
        for element in args:
            callable(getattr(task1_prev, element)(input.get(element)))
    else:
        for element in result:
            callable(getattr(task1_prev, element)(input.get(element)))


if __name__ == '__main__':
    runner()
    runner('counter')
    runner('new_string', 'counter', 'fib2')
