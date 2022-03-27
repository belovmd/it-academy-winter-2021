# В файле хранятся данные с сайта IMDB. Скопированные данные хранятся
# в файле ./data_hw5/ ratings.list.
# Откройте и прочитайте файл(если его нет необходимо вывести ошибку). 
# Найдите ТОП250 фильмов и извлеките заголовки.
# Программа создает 3 файла  top250_movies.txt – названия файлов,
# ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.


import os.path


if os.path.exists('ratings.list'):
    with open('ratings.list', 'r') as fh:
        histogr_years = {}
        histogr_rating = {}
        films = []
        for numline, line in enumerate(fh):
            if 27 < numline < 278:
                line = line.split()
                films.append(' '.join(line[3:-1]))
                rating = line[2]
                histogr_rating[rating] = histogr_rating.get(rating, 0) + 1
                year = line[-1].strip("()")
                histogr_years[year] = histogr_years.get(year, 0) + 1
            elif numline > 278:
                break

    with open('top250_movies.txt', 'w') as fh:
        for film in films:
            fh.write(film + '\n')

    with open('years.txt', 'w') as fh:
        for year in histogr_years:
            fh.write(f'{year}:{histogr_years[year]}' + '\n')

    with open('ratings.txt', 'w') as fh:
        for rating in histogr_rating:
            fh.write(f'{rating}:{histogr_rating[rating]}' + '\n')
else:
    print('error, file does not exists')
