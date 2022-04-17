# Вводится число найти его максимальный делитель,
# являющийся степенью двойки. 10(2) 16(16), 12(4).

def max_div(num):
    power = len(f'{num:b}') - 1
    while power > 0:
        divisor = 2 ** power
        if not num % divisor:
            print(divisor)
            break
        power -= 1
    else:
        print(num)


max_div(10)
max_div(16)
max_div(4)
