# Написать программу которая находит ближайшую степень двойки к введенному числу.
# 10(8), 20(16), 1(1), 13(16)

def degree_two(number):
    big_degree = 2 ** (len(format(number, "b")))
    small_degree = 2 ** (len(format(number, "b")) - 1)
    if number - small_degree > big_degree - number:
        print(big_degree)
    else:
        print(small_degree)
