# 4. В файле хранятся данные с сайта IMDB.
# Скопированные данные хранятся в файле ./data_hw5/ ratings.list.
# a. Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
# b. Найдите ТОП250 фильмов и извлеките заголовки.
# c. Программа создает 3 файла  top250_movies.txt – названия фильмов,
# ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.

def histogram(list_):
    list_.sort(reverse=True)
    dict_ = {}

    for elem in list_:
        dict_[elem] = dict_.get(elem, "") + ">"

    result = ""

    for key, value in dict_.items():
        result += "{key}: {value}\n".format(key=key, value=value)

    return result


RATING_START_LINE = 28
RATING_END_LINE = 278

try:
    with open("data_hw5/ratings.list", "rt") as imbd_txt:
        imbd250_list = imbd_txt.readlines()[RATING_START_LINE:RATING_END_LINE]

        top250_list = []
        ratings_list = []
        years_list = []

        for lines in imbd250_list:
            data = lines.split()
            top250_list.append(data[3:-1])
            ratings_list.append(data[2])
            years_list.append(data[-1])

        with open("data_hw5/top250_movies.txt", "w") as movies:
            for films in top250_list:
                line = " ".join(films) + "\n"
                movies.write(line)

        with open("data_hw5/ratings.txt", "w") as ratings:
            ratings.write(histogram(ratings_list))

        with open("data_hw5/years.txt", "w") as years:
            years.write(histogram(years_list))

except FileNotFoundError:
    print("ОШИБКА 404: Файл не найден")
