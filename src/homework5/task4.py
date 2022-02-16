import matplotlib.pyplot as plt
import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

dict_ = {}
url = 'http://npk.by/tmp/ratings.list'
# file_ = 'ratings.list'


r = urllib.request.urlopen('https://npk.by/tmp/ratings.list', context=ctx).read()

file = open(r)
# file = open('ratings.list')

for line in file.readlines()[28:278]:
    lines = line.split('  ')
    dict_[lines[-1][:-1]] = lines[-2]
file.close()

with open('top250_movies.txt', 'w') as fh:
    for k, v in dict_.items():
        fh.write(k + '\n')

probability = []
dict1 = {}

with open('ratings.txt', 'w') as fh:
    for k, v in dict_.items():
        fh.write(v + '\n')
        probability.append(v)

for elem in probability:
    dict1[elem] = dict1.get(elem, 0) + 1


plt.bar(dict1.keys(), dict1.values())
plt.show()
