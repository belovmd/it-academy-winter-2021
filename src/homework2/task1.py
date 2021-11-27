# task 1
"""Напишите программу, которая считает общую цену.
Вводится M рублей и N копеек цена, а также количество S товара
Посчитайте общую цену в рублях и копейках за L товаров."""
rubbles_number = int(input("Введите число рублей в цене: "))
cent_number = int(input("Введите число копеек в цене: "))
item_number = int(input("Введите количество предметов: "))

total_cost = item_number * (100 * rubbles_number + cent_number)

total_rubbles = total_cost // 100
total_cents = total_cost % 100
print(f"Общая цена {total_rubbles} рублей {total_cents} копеек")
