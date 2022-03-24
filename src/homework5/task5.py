# Написать программу которая находит ближайшую степень двойки к введенному числу.
# 10(8), 20(16), 1(1), 13(16)


def find_num(num):
    min_deg = num.bit_length() - 1
    max_deg = num.bit_length()

    if (num - 2 ** min_deg) < (2 ** max_deg - num):
        print('Degree: ', min_deg, ', closest number: ', 2 ** min_deg)
    else:
        print('Degree: ', max_deg, ', closest number: ', 2 ** max_deg)


find_num(10)
find_num(20)
find_num(1)
find_num(13)
