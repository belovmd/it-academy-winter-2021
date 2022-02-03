# Создайте декоратор, который хранит результаты вызовов функции
# (за все время вызовов, не только текущий запуск программы)

def dec(func):
    result = []

    def wrapper():
        nonlocal result
        result.append(func())
        return result

    return wrapper


@dec
def func():
    return 1


print(func())
print(func())
print(func())
print(func())
