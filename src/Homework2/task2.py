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
    sentence = str(input("Введите строку: "))
    sentence_cleared = re.sub('[^ A-Za-z]', '', sentence)
    sentence_separated = sentence_cleared.split()
    ind_max = int()
    for ind in range(len(sentence_separated)):
        if len(sentence_separated[ind]) > len(sentence_separated[ind_max]):
            ind_max = ind
    print(sentence_separated[ind_max])

