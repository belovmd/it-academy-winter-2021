number = int(input("Введите количество стран: "))
dict = {}

for element in range(number):
    input_string = input("Введите страну и город: ").split()
    country, cities = input_string[0], input_string[1:]
    dict[country] = cities

number2 = int(input("Введите количество городов: "))
cities = []
for element in range(number2):
    cities.append(input("Введите город: "))

for city in cities:
    print(city)
    for key in dict:
        if city in dict[key]:
            print(key)
