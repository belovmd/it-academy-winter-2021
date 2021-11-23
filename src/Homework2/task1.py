# Программа считает общую цену товара в рублях и копейках

price_product_N = int(input('Цена товара, рублей: '))
price_product_M = int(input('Цена товара, копеек: '))
amount_product = int(input('Количество товара: '))
amount_product_N = price_product_N * amount_product
amount_product_M = price_product_M * amount_product
i = amount_product_M / 100
if i < 1:
    print(amount_product_N, 'рублей', amount_product_M, 'копеек')
else:
    amount_product_N = amount_product_N + int(i)
    amount_product_M = amount_product_M % 100
    print(amount_product_N, 'рублей', amount_product_M, 'копеек')
