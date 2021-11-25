# Программа, которая считает общую цену товаров в рублях и копейках

price_m = int(input('Цена товара, руб'))
price_n = int(input('Цена товара, коп'))
quantity_s = int(input('Количество товаров, шт'))
quantity_l = int(input('Количество приобретаемых товаров, шт'))
price_ml = price_m * quantity_l
price_nl = price_n * quantity_l
divisor_n = 100
price_div = price_n * quantity_l / divisor_n
if price_div < 1:
    print('Общая цена', price_ml, 'рублей', price_nl, 'копеек')
else:
    print('Общая цена', price_ml + price_nl // divisor_n, 'рублей', price_nl % divisor_n, 'копеек')