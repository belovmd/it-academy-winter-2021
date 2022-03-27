# Вводится число найти его максимальный делитель, являющийся степенью двойки. 10(2) 16(16), 12(4).

def max_divisor(number):
    degree = len(format(number, "b")) - 1
    while degree > 0:
        divisor = 2 ** degree
        if not number % divisor:
            print(divisor)
            break
        degree -= 1
    else:
        print(number)


max_divisor(10)
max_divisor(16)
max_divisor(12)
