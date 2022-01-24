# Языки
# Каждый из N школьников некоторой школы знает Mi языков.
# Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
# Входные данные
# Первая строка входных данных содержит количество школьников N.
# Далее идет N чисел Mi, после каждого из чисел идет Mi строк,
# содержащих названия языков, которые знает i-й школьник.
# Пример входных данных:
# 3          # N количество школьников
# 2          # M1 количество языков первого школьника
# Russian    # языки первого школьника
# English
# 3          # M2 количество языков второго школьника
# Russian
# Belarusian
# English
# 3          # M3 количество языков третьего школьника
# Russian
# Italian
# French
# Выходные данные
# В первой строке выведите количество языков, которые знают все школьники.
# Начиная со второй строки - список таких языков.
# Затем - количество языков, которые знает хотя бы один школьник,
# на следующих строках - список таких языков.


amount_students = int(input('Enter students amount: '))
languages_list = list()

for student in range(amount_students):
    amount_languages = int(input('Enter student languages amount: '))
    student_languages_list = set()

    for language in range(amount_languages):
        student_language = input('Enter student language: ')
        student_languages_list.add(student_language)
    languages_list.append(student_languages_list)

everybody_knows = languages_list[0]
somebody_knows = set()

for student in range(amount_students):
    everybody_knows &= languages_list[student]
    somebody_knows |= languages_list[student]

num_everybody_knows = len(everybody_knows)
num_somebody_knows = len(somebody_knows)

print('Number of languages known to all students: ', num_everybody_knows)
print('Languages list: ', list(everybody_knows))

print('Number of languages at least one student knows: ', num_somebody_knows)
print('Languages list: ', list(somebody_knows))
