import main


def runner(*args):
    if not args:
        for func in dir(main):
            if func[0] != "_":
                f = getattr(main, func)
                print("Функция", f.__name__)
                print("Ответ", f())
    else:
        for func in args:
            if func in dir(main):
                f = getattr(main, func)
                print("Функция", f.__name__)
                print("Ответ", f())


runner()
runner("task6_4")
runner("task6_4", "task5_3")
