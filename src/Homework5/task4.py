'''
4.	В файле хранятся данные с сайта IMDB.
Скопированные данные хранятся в файле ./data_hw5/ ratings.list.
a.	Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
b.	Найдите ТОП250 фильмов и извлеките заголовки.
c.	Программа создает 3 файла  top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.
Задачу поместите в файл task4.py в папке src/homework5.
'''
#  a
try:
    fh = open('ratings.list', 'r')
except FileNotFoundError:
    print('File not found')
else:
    fh.close()
#  b
str_file = ''
list_title = []
list_rank = []
list_year = []
try:
    open('ratings.list', 'rt')
except FileNotFoundError:
    print('File not found')
else:
    with open('ratings.list', 'rt') as fh:
        while str_file != 'New  Distribution  Votes  Rank  Title\n':
            str_file = fh.readline()  # found begin of TOP
        while str_file != '\n':
            str_file = fh.readline().replace('/I', '')
            list_title.append(str_file[(str_file.find('.') + 4):(len(str_file) - 8)])
            list_rank.append(str_file[(str_file.find('.') - 1):(str_file.find('.') + 2)])
            list_year.append(str_file[(len(str_file) - 6):(len(str_file) - 2)])
#  c
        list_title.pop()
        list_rank.pop()
        list_year.pop()
#        print(list_title)
#        print(list_rank)
#        print(list_year)
        file1 = open('top250_movies.txt', 'w')
        file1.writelines(line + '\n' for line in list_title)
        file1.close()
        file2 = open('ratings.txt', 'w')
        file2.writelines(line + '\n' for line in list_rank)
        file2.close()
        file3 = open('years.txt', 'w')
        file3.writelines(line + '\n' for line in list_year)
        file3.close()
        print('Complete')
