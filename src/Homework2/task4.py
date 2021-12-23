'''
4. Посчитать количество строчных (маленьких) и прописных (больших)
букв в введенной строке. Учитывать только английские буквы.
Задачу поместите в файл task4.py в папке src/homework2.

'''
propis = int()
stroch = int()
str_ = str(input("Введите строку: "))
for i in str_:
    if 'A' <= i <= 'Z':
        propis += 1
    if 'a' <= i <= 'z':
        stroch += 1
print(f'{propis} прописных букв, {stroch} строчных букв')
dict_ = {"propis": 0, "stroch": 0}
str_ = str(input("Введите строку: "))
for i in str_:
    if 'A' <= i <= 'Z':
        dict_["propis"] += 1
    if 'a' <= i <= 'z':
        dict_["stroch"] += 1      
print(f'{dict_["propis"]} прописных букв, {dict_["stroch"]} строчных букв')
