# 4
# В файле хранятся данные с сайта IMDB. Скопированные данные хранятся
# в файле ./data_hw5/ ratings.list.
# Откройте и прочитайте файл (если его нет, необходимо вывести ошибку).
# Найдите ТОП250 фильмов и извлеките заголовки.
# Программа создает 3 файла  top250_movies.txt – названия файлов,
# ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.

file = open(r'C:\Users\Marina\Documents\ratings.list')
top250_movies = open(r'C:\Users\Marina\Documents\top250_movies.txt', 'w')
ratings = open(r'C:\Users\Marina\Documents\ratings.txt', 'w')
years = open(r'C:\Users\Marina\Documents\years.txt', 'w')

content = file.readlines()
list_rating = []
list_year = []
for i in range(28, 28 + 250):
    list1 = content[i].split()
    name = ' '.join(list1[3:-1])
    top250_movies.write(name + '\n')
    list_rating.append(list1[2])
    list_year.append(list1[-1][1:5])

dict_ratings = {el1: list_rating.count(el1) for el1 in list_rating}
dict_years = {el2: list_year.count(el2) for el2 in list_year}

for key in dict_ratings:
    string = key + ' ' + '+' * dict_ratings[key] + '\n'
    ratings.write(string)
for key in dict_years:
    string = key + ' ' + '+' * dict_years[key] + '\n'
    years.write(string)

file.close()
top250_movies.close()
ratings.close()
years.close()
