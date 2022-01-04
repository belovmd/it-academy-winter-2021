# Write a program that calculates the total price.
# Enter m rubles and n kopecks price, as well as the quantity s of goods.
# Calculate the total price in rubles and kopecks for q goods.


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
