# Напишите программу, которая считает общую цену.
# Вводится M рублей и N копеек цена, а также количество S товара
# Посчитайте общую цену в рублях и копейках за L товаров.


rub = float(input('Введите количество рублей: '))
kop = float(input('Введите количество копеек: ')) / 100
quantity = float(input('Введите количество товара: '))

grocery_bill = str((rub + kop) * quantity)
total_rub, total_kop = grocery_bill.split('.')

if len(total_kop) == 1:
    total_kop = int(total_kop) * 10

print('Общая цена ', total_rub, ' рублей ', total_kop, ' копеек')
