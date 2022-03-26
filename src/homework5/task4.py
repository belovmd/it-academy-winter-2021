# File gas data from IMDB. Data is stored in a file ./data_hw5/ ratings.list.
# Open and read file (if it doesn't exist print error).
# Find top 250 and extract the headers.
# Program create 3 files top250_movies.txt – name of the movies,
# ratings.txt – bar graph of ratings, years.txt – bar graph of years.


def histogram(lst):
    lst.sort()
    dct = {}
    str_ = ""

    for el in lst:
        dct[el] = dct.get(el, 1) + 1

    for key, value in dct.items():
        str_ += "{key}: {value}\n".format(key=key, value=value)

    return str_


start = 28
end = 278
try:
    with open("data_hw5/ratings.list", "rt") as data_txt:
        movies_lst = data_txt.readlines()[start:end]
        top_lst = []
        rating_lst = []
        years_lst = []

        for line in movies_lst:
            line = line.split()
            top_lst.append(line[3:-1])
            rating_lst.append(line[2])
            years_lst.append(line[-1])

        with open("data_hw5/top250_movies.txt", "w") as names:
            for films in top_lst:
                line = " ".join(films) + "\n"
                names.write(line)

        with open("data_hw5/ratings.txt", "w") as rate:
            rate.write(histogram(rating_lst))

        with open("data_hw5/years.txt", "w") as years:
            years.write(histogram(years_lst))

except FileNotFoundError:
    print("ОШИБКА 404: Файл не найден")
