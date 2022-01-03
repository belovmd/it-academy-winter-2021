# m - number rub, n - number kop, s - number of things, l - result
m, n, s = input('input m, n, s by space').split()
L = int(s)*(int(m) * 100 + int(n))
print(str(L // 100) + 'rub' + str(L % 100) + 'kop')