'''
2.	List practice
1.	Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
2.	Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
3.	Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
4.	Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
5.	Скопируйте список и добавьте в него элемент '2a' так,
    чтобы в исходном списке этого элемента не было.
Задачу поместите в файл task2.py в папке src/homework3.

'''
list1 = [el1 + el2 for el1 in ['a', 'b'] for el2 in ['b', 'c', 'd']]
print('1. ', list1)
list2 = list1[::2]
print('2. ', list2)
list3 = [str(el) + 'a' for el in range(1, 5)]
print('3. ', list3)
print('4. ', list3.pop(1))
import copy
list5 = copy.copy(list3)
list5.insert(1, '2a')
print('5. list3:', list3)
print('5. list5:', list5)
