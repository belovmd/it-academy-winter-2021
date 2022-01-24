'''
4.	Пары элементов
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается,
что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
'''
counter_elements = int()
counter_par = int()
antirepeat = []
str_ = '1 1 1 2 2 2 2 3 3 3 3 3'
list_ = [int(elem) for elem in str_.split()]
for element in list_:
    if element not in antirepeat:
        counter_elements = list_.count(element)
        antirepeat.append(element)
        if counter_elements > 1:
            for factorial in range(1, counter_elements):  # counter_par = (counter_elements - 1)!
                counter_par += factorial
print(counter_par)
print(list_)
