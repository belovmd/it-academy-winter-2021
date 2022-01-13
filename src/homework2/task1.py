# Напишите программу, которая считает общую цену. Вводится M рублей и N копеек цена,
# а также количество S товара Посчитайте общую цену в рублях и копейках за L товаров.
# Пример:
# Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
# Output: Общая цена 9 рублей 60 копеек

price_m = int(input('Цена товара, руб'))
price_n = int(input('Цена товара, коп'))
quantity_s = int(input('Количество товаров, шт'))
quantity_l = int(input('Количество приобретаемых товаров, шт'))
price_ml = price_m * quantity_l
price_nl = price_n * quantity_l
divisor_n = 100
price_div = price_nl / divisor_n
if price_div < 1:
    print('Общая цена:', price_ml, 'рублей', price_nl, 'копеек')
else:
    print('Общая цена:', price_ml + price_nl // divisor_n, 'рублей', price_nl % divisor_n, 'копеек')
