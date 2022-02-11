# There is list of countries and towns. Then the names of the towns are given.
# For each town print, which country is it belong.

n = int(input("Enter count of countries "))
dct = {}
for line in range(n):
    str_ = input("Enter country and towns ")
    str_ = str_.split()
    dct[str_[0]] = str_[1:]
print(dct)
m = int(input("How many towns do you wanna check? "))
towns = []
for line in range(m):
    towns.append(input("Which towns? "))
for town in towns:
    print(town, ":")
    for key in dct:
        if town in dct[key]:
            print(key)
