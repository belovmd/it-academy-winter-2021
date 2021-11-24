m = int(input('Цена одной вещи, рублей:'))
n = int(input('копеек:'))
s = int(input('Количетсво товара:'))
stoimost = s * (m + n / 100)
rub = stoimost // 1
cent = stoimost % 1 * 100
print('Общая цена', int(rub), 'рублей', int(cent), 'копеек')
