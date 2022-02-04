# Напишите программу, которая считает общую цену.
# Вводится M рублей и N копеек цена, а также количество S товара
# Посчитайте общую цену в рублях и копейках за L товаров.


m, n, s = input('Введите М рублей: '), input('N копеек: '), input('S товара: ')

grocery_bill = (float(m) + (float(n) / 100)) * float(s)
total_rub = int(grocery_bill)
total_kop = int((grocery_bill - total_rub) * 100)

print('Общая цена ', total_rub, ' рублей ', total_kop, ' копеек')
