# Вводится число найти его максимальный делитель, являющийся степенью двойки.
# 10(2) 16(16), 12(4).

def max_divider(number):
    bin_number = format(number, "b")
    reverse_ = bin_number[::-1]
    return 2 ** (reverse_.find("1"))


print(max_divider(10))
print(max_divider(16))
print(max_divider(12))
print(max_divider(128))
