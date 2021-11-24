# Программа считает общую цену товара в рублях и копейках

price_rub = int(input('Цена товара, рублей: '))
price_coin = int(input('Цена товара, копеек: '))
product_amount = int(input('Количество товара: '))
total_price_rub = price_rub * product_amount
total_price_coin = price_coin * product_amount
converted_to_rub = total_price_coin / 100
if converted_to_rub < 1:
    print(total_price_rub, 'рублей', total_price_coin, 'копейки')
else:
    total_price_rub = total_price_rub + int(converted_to_rub)
    total_price_coin = total_price_coin % 100
    print(total_price_rub, 'рублей', total_price_coin, 'копейки')