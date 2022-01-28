# Программа считает общую цену товара в рублях и копейках

price_rub = int(input('Цена товара, рублей: '))
price_coin = int(input('Цена товара, копеек: '))
product_amount = int(input('Количество товара: '))

total_price = product_amount * (price_rub * 100 + price_coin)

total_price_rub = total_price // 100
total_price_coin = total_price % 100
print(total_price_rub, 'рублей', total_price_coin, 'копейки')
