# Оформите решение задач из прошлых домашних работ в функции. Напишите функцию runner.
# (все станет проще когда мы изучим модули, getattr и setattr)
# a. runner() – все фукнции вызываются по очереди
# b. runner(‘func_name’) – вызывается только функцию func_name.
# c. runner(‘func’, ‘func1’...) - вызывает все переданные функции


import homework3


def runner(*args):
    if args:
        for arg in args:
            if arg in dir(homework3):
                f = getattr(homework3, arg)
                print('Result: ', f())
    else:
        func = [a for a in dir(homework3) if a[0] != ('_')]
        for arg in func:
            f = getattr(homework3, arg)
            print('Result: ', f())


runner()
runner('task5')
runner('task5', 'task6')
