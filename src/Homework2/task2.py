'''
2. Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
Подсказки:
-	my_string.split([chars]) возвращает список строк.
-	len(list) - количество элементов в списке
Задачу поместите в файл task2.py в папке src/homework2.

'''
import re
while True:
    str_ = str(input("Введите строку: "))
    str_2 = re.sub('[^ A-Za-z]', '', str_)
    str_3 = str_2.split()
    ind_max = int()
    for ind in range(len(str_3)):
        if len(str_3[ind]) > len(str_3[ind_max]):
            ind_max = ind
    print(str_3[ind_max])
    
