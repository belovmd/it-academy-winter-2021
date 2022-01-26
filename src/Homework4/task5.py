'''
5.	Языки
Каждый из N школьников некоторой школы знает Mi языков.
Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
Входные данные
Первая строка входных данных содержит количество школьников N.
Далее идет N чисел Mi, после каждого из чисел идет Mi строк,
содержащих названия языков, которые знает i-й школьник.
Пример входных данных:
3          # N количество школьников
2          # M1 количество языков первого школьника
Russian    # языки первого школьника
English
3          # M2 количество языков второго школьника
Russian
Belarusian
English
3
Russian
Italian
French
Выходные данные
В первой строке выведите количество языков, которые знают все школьники.
Начиная со второй строки - список таких языков. Затем - количество языков,
которые знает хотя бы один школьник, на следующих строках - список таких языков.
Задачу поместите в файл task5.py в папке src/homework4.
'''

dict_pupils_langs = {}
var_lst = []
summ = []
n = int(input('Введите количество школьников: '))
for pupils in range(n):
    mi = int(input('Введите количество языков школьника: '))
    for langs in range(mi):
        var_lst.append(str(input('Введите язык: ')))
    dict_pupils_langs[pupils] = set(var_lst)
    var_lst = []
for list_ in dict_pupils_langs.values():
    summ.extend(list_)
key = int(0)
set_all = dict_pupils_langs[0]
while key < (len(dict_pupils_langs) - 1):
    set_all = set_all & dict_pupils_langs[key + 1]
    key += 1
else:
    print(len(set_all))
    lst_all = list(set(set_all))
    for elem in lst_all:
        print(elem)
print(len(set(summ)))
lst_summ = list(set(summ))
for elem in lst_summ:
    print(elem)
