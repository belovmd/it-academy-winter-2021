# Каждый из N школьников некоторой школы знает Mi языков. Определите, какие языки знают
# все школьники и языки, которые знает хотя бы один из школьников.


num_stud = int(input("Enter the number of students: "))
lst = []

for student in range(num_stud):
    num_lang = int(input("Enter the number of languages: "))
    for language in range(num_lang):
        lang = input("Enter the language: ")
        lst.append(lang)

max_lang = {lang for lang in lst if lst.count(lang) == num_stud}

print(len(max_lang))
for lang in max_lang:
    print(lang)
print(len(set(lst)))
for lang in set(lst):
    print(lang)
