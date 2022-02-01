# Каждый из N школьников некоторой школы знает Mi языков.
# Определите, какие языки знают все школьники и языки,
# которые знает хотя бы один из школьников

all_lang = set()
least_one = set()
n = int(input('input number pupils n = '))


for i in range(n):
    a = {input('input name lang. ...  ') for j in range(int(input('input number lang. mi = ')))}
    if n == 1:
        least_one.update(a)
        all_lang.update(a)
    else:
        least_one = all_lang & a
        all_lang.update(a)


print('number of languages that all pupils know = ' + str(len(all_lang)))
print('number of languages that all pupils know ' + str(all_lang))
print('number of languages at least one knows = ' + str(len(least_one)))
print('number of languages at least one knows ' + str(least_one))
