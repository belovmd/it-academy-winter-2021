# Оформите решение задач из прошлых домашних работ в функции. Напишите функцию runner.
# (все станет проще когда мы изучим модули, getattr и setattr)
# runner() – все фукнции вызываются по очереди
# runner(‘func_name’) – вызывается только функцию func_name.
# runner(‘func’, ‘func1’...) - вызывает все переданные функции

from src import functions


def runner(*args):
    if not args:
        for func in dir(functions):
            if func[0] != "_":
                f = getattr(functions, func)
                print("Function", f.__name__)
                print("Result: ", f())
    else:
        for func in args:
            if func in dir(functions):
                f = getattr(functions, func)
                print("Function", f.__name__)
                print("Result: ", f())


runner("sum_numbers")
runner("bank", "number_of_pairs")
runner()
