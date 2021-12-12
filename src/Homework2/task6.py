import copy
while True:
    chislo = int(input('Введите число: '))
    lst_ = []
    lst_rev = []
    while chislo > 0:
        lst_.append(chislo % 10)
        chislo = chislo // 10
    lst_rev = copy.deepcopy(lst_)
    lst_rev.reverse()
    if lst_ == lst_rev:
        print('Это палиндром')
    else:
        print('Это не палиндром')
