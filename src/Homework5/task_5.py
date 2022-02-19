# Написать программу которая находит
# ближайшую степень двойки к введенному числу. 10(8), 20(16), 1(1), 13(16)


import math

number = int(input('Enter the number: '))
two = 2
degree = 0

while number >= two ** degree:
    degree += 1

degree = degree - 1
result = two ** degree

print('Result: ', result)

print('Closest power of two: ', two, '**', degree, '=', int(math.pow(two, degree)))
