'''
2.	Создайте декоратор, который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы)
Задачу поместите в файл task2.py в папке src/homework5.
'''


def decore(func):
    calls_result = []

    def wrapper():
        nonlocal calls_result
        calls_result.append(func())
        return print('calls_result:', calls_result)
    return wrapper


@decore
def function():
    return 'function result'


print(function())
print(function())
print(function())
print(function())
print(function())