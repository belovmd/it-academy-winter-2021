m = int(input('Enter price in rubles '))
n = int(input('Enter price in kopecks '))
s = int(input('Enter quantity '))
q = int(input('Enter how much do you wanna buy '))
while q > s:
    print('Sorry, but there are only', s, ':( How much do you need?')
    q = int(input())
m = m * q + (n * q // 100)
n = n % 100
print('Total cost is', m, 'rubles', n, 'kopecks')
