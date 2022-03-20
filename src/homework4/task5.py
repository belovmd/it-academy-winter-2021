# 5. Языки
# Каждый из N школьников некоторой школы знает Mi языков.
# Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.

students_amount = int(input("Введите количество школьников: "))
students_langs = []

for student in range(1, students_amount + 1):
    langs_amount = int(input("Введите количество языков для {s}-го школьника: ".format(s=student)))
    langs = set()

    for lang in range(1, langs_amount + 1):
        language = input("Введите {l}-й язык для {s}-го школьника: ".format(l=lang, s=student))
        langs.add(language)

    students_langs.append(langs)

all_knows = students_langs[0]
any_knows = set()

for num in range(students_amount):
    all_knows &= students_langs[num]
    any_knows |= students_langs[num]

print("Все школьники знают {n} язык(-а/ов):".format(n=len(all_knows)))
for elem in all_knows:
    print(elem)
print("Хотя бы один из школьников знает 1 из {n} язык(-а/ов):".format(n=len(any_knows)))
for elem2 in any_knows:
    print(elem2)
