# 1. Оформите решение задач из прошлых домашних работ в функции. Напишите функцию runner.
# runner() – все фукнции вызываются по очереди.
# runner(‘func_name’) – вызывается только функция func_name.
# runner(‘func’, ‘func1’...) - вызывает все переданные функции.

import task1_functions


def runner(*args):
    counter = 0
    for func in dir(task1_functions):
        funk = getattr(task1_functions, func)
        if not args:
            if callable(funk):
                counter += 1
                print("Имя функции #{fh}: {fn}\n"
                      "Результат выполнения: {fr}\n".format(fh=counter,
                                                            fn=funk.__name__,
                                                            fr=funk(),
                                                            )
                      )
        else:
            if callable(funk) and func in args:
                counter += 1
                print("Имя функции #{fh}: {fn}\n"
                      "Результат выполнения: {fr}\n".format(fh=counter,
                                                            fn=funk.__name__,
                                                            fr=funk(),
                                                            )
                      )
    print(">>> Все вызываемые функции выполнены\n")


runner()
runner("hw2_task3")
runner("hw2_task3", "hw2_task5", "hw3_task6")
