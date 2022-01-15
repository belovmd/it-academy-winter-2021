# task 5 Языки
"""
Первая строка входных данных содержит количество школьников N.
Далее идет N чисел Mi, после каждого из чисел идет Mi строк, содержащих названия языков,
которые знает i-й школьник.

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
"""

# Examples:
"""
1. Input:
3
2
EnGLish
FRENCH
3
english
french
norsk
4
italiANO
ENGLISH
FrENch
espana

Output:
Number of everyone knowing languages is: 2
english
french
Total number of languages is: 4
english
espana
french
italiano

2. Input:
3
2
Russian
English
3
Russian
Belarusian
English
3
Russian
Italian
French

Output:
Number of everyone knowing languages is: 1
russian
Total number of languages is: 3
italian
russian
french
"""

students_dict = {}
all_known_langs = set([])
students = int(input("Enter the number of students: "))
for student in range(1, students + 1):
    langs_number = int(input("Enter the number of languages that are known by student: "))
    languages = []
    for lang in range(1, langs_number + 1):
        languages.append(input("Enter the language: ").lower())
    students_dict[student] = languages
    languages_set = set(languages)
all_known_langs = set(students_dict.get(1))
for student in range(2, students + 1):
    all_known_langs &= set(students_dict.get(student))

print("Number of everyone knowing languages is:", len(all_known_langs))
for language in range(len(all_known_langs)):
    print(list(all_known_langs)[language])
print("Total number of languages is:", len(languages_set))
for language in range(len(languages_set)):
    print(list(languages_set)[language])
