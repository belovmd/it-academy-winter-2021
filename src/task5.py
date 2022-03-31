number_of_students = int(input("Введите количество учеников: "))
lst = []

for student in range(number_of_students):
    number_of_lang = int(input("Введите количество языков: "))
    for language in range(number_of_lang):
        lang = input("Введите язык: ")
        lst.append(lang)

max_lang = {lang for lang in lst if lst.count(lang) == number_of_students}

print("Количество языков, которые знают все школьники", len(max_lang))
for lang in max_lang:
    print("Список языков", lang)
print("Количество языков, которые знает хотя бы один школьник", len(set(lst)))
for lang in set(lst):
    print("Список языков", lang)
