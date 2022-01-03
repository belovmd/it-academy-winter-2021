n = int(input('input n = '))
a = 0
b = 1

for i in range(0, n - 2):
    a, b = b, a + b

print('Fibonacci numbers for n = ' + str(n) + ' = ' + str(b))
