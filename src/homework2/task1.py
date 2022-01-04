


m = int(input('Enter price in rubles '))
n = int(input('Enter price in kopecks '))
s = int(input('Enter quantity '))
l = int(input('Enter how much do you wanna buy '))
while l > s:
    print('Sorry, but there are only', s, ':( How much do you need?')
    l = int(input())
m = m * l + (n * l // 100)
n = n % 100
print('Total cost is', m, 'rubles', n, 'kopecks')
