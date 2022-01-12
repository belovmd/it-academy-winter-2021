# Каждый из N школьников некоторой школы знает Mi языков.
# Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.

number_students = int(input("Enter the number of students: "))
result_1 = set()
result_2 = set()
for _ in range(number_students):
    number_language = int(input("Enter number of languages the students know: "))
    set_ = set()
    for elem in range(number_language):
        set_.add(input("Enter language: "))
    if result_1:
        result_1 = result_1 & set_
    else:
        result_1 = set_
    result_2 = result_2 | set_

len_1 = len(result_1)
len_2 = len(result_2)
print("Number of languages that all students know: ", len_1)
for _ in range(len_1):
    print(result_1.pop())

print("Number of languages that at least one student know: ", len_2)
for _ in range(len_2):
    print(result_2.pop())
