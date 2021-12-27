# 1. Напишите программу, которая считает общую цену.
# Вводится M рублей и N копеек цена, а также количество S товара
# Посчитайте общую цену в рублях и копейках за L товаров.
# Пример: Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
# Output: Общая цена 9 рублей 60 копеек


product_price_rub = int(input('Enter product rub: '))
product_price_coins = int(input('Enter product penny: '))
quantity_of_goods = int(input('Enter the quantity of goods: '))

sum_price_rub = product_price_rub * quantity_of_goods
sum_price_coins = product_price_coins * quantity_of_goods

print(f"Общая цена {sum_price_rub} рублей {sum_price_coins} копеек")
