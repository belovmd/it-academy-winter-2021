# Вводится число найти его максимальный делитель,
# являющийся степенью двойки. 10(2) 16(16), 12(4).


number = int(input('Enter the number: '))
two = 2
degree = 1

while number >= two ** degree:
    degree += 1

power_of_two = two ** (degree - 1)
result = number % power_of_two

if result == 0:
    print('The maximum divisor, which is: ', number)
else:
    print('The maximum divisor, which is: ', power_of_two)

