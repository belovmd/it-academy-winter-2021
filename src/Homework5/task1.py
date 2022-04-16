'''
Оформите решение задач из прошлых домашних работ в функции. Напишите функцию runner.
(все станет проще когда мы изучим модули, getattr и setattr)
a. runner() – все фукнции вызываются по очереди
b. runner(‘func_name’) – вызывается только функцию func_name.
c. runner(‘func’, ‘func1’...) - вызывает все переданные функции
'''


import homeworks3


def runner(*args):
    if args:
        for arg in args:
            if arg in dir(homeworks3):
                func = getattr(homeworks3, arg)
                print('Result: ', func())
    else:
        func = [fu for fu in dir(homeworks3) if fu[0] != '_']
        for arg in func:
            f = getattr(homeworks3, arg)
            print('Result: ', f())


runner()
runner('counter_couples')
runner('counter_couples', 'mover')


'''
import math

def runner2(*args):
    if args:
        for arg in args:
            if arg in dir(math):
                f = getattr(math, *args)
        print(f(math.pi / 2))

runner2('sin')
'''