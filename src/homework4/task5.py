# Each of N students knows M languages.
# Which languages is known by all, and which is known by at least one

n = int(input("Enter count of student "))
dct = {}
for student in range(n):
    m = int(input("Enter count of languages "))
    languages = []
    for language in range(m):
        languages.append(input("Enter language "))
    dct[student] = languages
all_lang = set()
for key in dct:
    all_lang |= set(dct[key])
mutual = set()
for lng in all_lang:
    for key in dct:
        if lng not in dct[key]:
            break
    else:
        mutual.add(lng)
print("Number of languages that every student knows is ", len(mutual))
print("These languages: ", mutual)
print("Number of languages at least one student knows is ", len(all_lang))
print("These languages: ", all_lang)
