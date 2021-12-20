m = int(input('Введите количество рублей:'))
n = int(input('Введите количество копеек:'))
s = int(input('Введите количество товара:'))
x = int(input('Введите искомое количество товара:'))
price = x * (m + n / 100) / s
rubles = int(price // 1)
kopecks = int((price - rubles) * 100)
print('Общая цена', rubles, 'рублей', kopecks, 'копеек')
