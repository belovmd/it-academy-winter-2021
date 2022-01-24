# 5 Языки
# Каждый из N школьников некоторой школы знает Mi языков.
# Определите, какие языки знают все школьники и языки, которые
# знает хотя бы один из школьников.

n_student = int(input('Введите кол-во учеников: '))
list1 = []
for student in range(n_student):
    m = int(input('Введите кол-во языков: '))
    languages = set()
    for _ in range(m):
        language = input('Введите язык: ')
        languages.add(language)
    list1.append(languages)
all_know = list1[0]
any_knows = set()
for i in range(n_student):
    all_know &= list1[i]
    any_knows |= list1[i]
print(len(all_know))
print(*all_know, sep='\n')
print(len(any_knows))
print(*any_knows, sep='\n')
