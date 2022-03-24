# Оформите решение задач из прошлых домашних работ в функции. Напишите функцию runner.
# (все станет проще когда мы изучим модули, getattr и setattr)


import homework4


def runner(*args):
    if args:
        for arg in args:
            f = getattr(homework4, arg)
            f()
    else:
        func = [a for a in dir(homework4) if a[0] != ('_')]
        for arg in func:
            f = getattr(homework4, arg)
            f()

runner()
runner('task1')
runner('task1', 'task2')
