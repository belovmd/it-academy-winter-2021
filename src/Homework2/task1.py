﻿'''
1. Напишите программу, которая считает общую цену.
Вводится M рублей и N копеек цена, а также количество S товара
Посчитайте общую цену в рублях и копейках за L товаров. 
Пример: 
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета. 
Output: Общая цена 9 рублей 60 копеек
Задачу поместите в файл task1.py в папке src/homework2.
'''
while True:
    m = int(input("Цена товара, руб.: "))
    n = int(input("Цена товара, коп.: "))
    qantity = int(input("Введите количество товара: "))
    sm = int(m * qantity)
    sl = int(n * qantity)
    if sl > 100:
        sm = sm + sl // 100
        ssl = int(sl % 100)
        print('Общая цена ' + str(sm) + ' рублей ' + str(ssl) + ' копеек')
    else:
        print('Общая цена ' + str(sm) + ' рублей ' + str(sl) + ' копеек')
