import matplotlib.pyplot as plt

try:
    with open("ratings.list", "rt") as fh:
        rating_list = fh.readlines()[28:278]

        films = []
        ratings_list = []
        years_list = []
        ratings = {}
        years = {}

        for lines in rating_list:
            data = lines.split()
            films.append(data[3:-1])
            ratings_list.append(data[2])
            years_list.append(data[-1])

        with open("top250_movies.txt", "w") as movies:
            for film in films:
                line = " ".join(film) + "\n"
                movies.write(line)

        def histogram(list_):
            list_.sort(reverse=True)
            dict_ = {}

            for elem in list_:
                dict_[elem] = dict_.get(elem, 0) + 1

            result = ""

            for key, value in dict_.items():
                result += "{key}: {value}\n".format(key=key, value=value)

            return result

        with open("ratings.txt", "w") as rate:
            rate.write(histogram(ratings_list))

        with open("years.txt", "w") as yea:
            yea.write(histogram(years_list))

except FileNotFoundError:
    print("Error")

for elem in sorted(ratings_list):
    ratings[elem] = ratings.get(elem, 0) + 1

for elem in sorted(years_list):
    years[elem] = years.get(elem, 0) + 1

plt.tick_params(axis='both', which='major', labelsize=16, labelcolor='green')
plt.bar(ratings.keys(), ratings.values())
plt.show()

plt.tick_params(axis='both', which='major', labelsize=7, rotation=90)
plt.bar(years.keys(), years.values())
plt.show()