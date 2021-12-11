"""Write a program that calculates the total price.

Enter M rubles and N kopecks price, as well as the quantity S of goods.
Calculate the total price in rubles and kopecks for L goods.
Example:
Input: The price of one item is 3 rubles 20 kopecks, count 3 items.
Output: Total price 9 rubles 60 kopecs
"""


# 1st variant

roubles, kopecks, amount = (int(value) for value in input('Input roubles kopecks amount: ').split())

sum_roubles = roubles * amount + kopecks * amount // 100
sum_kopecks = kopecks * amount % 100
print('Summarized price: ', sum_roubles, 'roubles, ', sum_kopecks, ' kopecks.')


# 2nd variant

price = float(input('Input price (e.g. 2.65): '))
amount = int(input('Input amount: '))

sum_roubles2 = int(price * amount // 1)
sum_kopecks2 = int(price * amount % 1 * 100)
print('Summarized price: ', sum_roubles2, 'roubles, ', sum_kopecks2, ' kopecks.')
