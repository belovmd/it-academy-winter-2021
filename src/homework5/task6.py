# Вводится число найти его максимальный делитель, являющийся степенью двойки.
# 10(2) 16(16), 12(4)


def binary_gcd(num):
    rev_bin = bin(num)[::-1]
    max_div = 2 ** rev_bin.find('1')
    return print('Maximum divisor: ', max_div)


binary_gcd(10)
binary_gcd(16)
binary_gcd(12)
