# В файле хранятся данные с сайта IMDB. Скопированные данные хранятся в файле
# ./data_hw5/ ratings.list.
# Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
# Найдите ТОП250 фильмов и извлеките заголовки.
# Программа создает 3 файла top250_movies.txt – названия файлов, ratings.txt –
# гистограмма рейтингов, years.txt – гистограмма годов.


import os
import matplotlib.pyplot as plt
from google_drive_downloader import GoogleDriveDownloader as gdd


gdd.download_file_from_google_drive(file_id='17ZjvONKYeKsmyKAy_xqss-Hl6xyLrvpa',
                                    dest_path='./ratings.list.zip',
                                    unzip=True)

dict_top = {}
sort_ratings = []
sort_years = []
dict_ratings = {}
dict_years = {}

file = open('ratings.list')

for line in file.readlines()[28:278]:
    lines = line.split('  ')
    dict_top[lines[-1][:-1]] = lines[-2]
file.close()

with open('top250_movies.txt', 'w') as fh:
    for k, v in dict_top.items():
        fh.write(k + '\n')
        sort_ratings.append(v)
        sort_years.append(k[-5:-1])

for elem in sorted(sort_ratings):
    dict_ratings[elem] = dict_ratings.get(elem, 0) + 1

for elem in sorted(sort_years):
    dict_years[elem] = dict_years.get(elem, 0) + 1

plt.bar(dict_ratings.keys(), dict_ratings.values())
plt.show()
plt.bar(dict_years.keys(), dict_years.values())
plt.show()

os.remove('ratings.list')
os.remove('ratings.list.zip')
