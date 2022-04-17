# Создайте декоратор, который хранит результаты вызовов функции
# (за все время вызовов, не только текущий запуск программы)

def dec(fun):
  call_number_fun = 0
  all_result = []

  def wrapper():
    nonlocal all_result, call_number_fun
    call_number_fun += fun()
    all_result.append(fun())
    return print('call number_fun:', call_number_fun, 'all_result:', all_result)

  return wrapper


@dec
def func():
    return 1


print(func())
print(func())
print(func())
