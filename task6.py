def div(num):
    divider = 1
    elem = 1
    while elem <= num:
        elem = elem << 1
        if not num % elem:
            divider = elem
    print(divider)


div(int(input('Введите число: ')))