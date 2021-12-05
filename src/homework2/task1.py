"""Write a program that calculates the total price.

Enter M rubles and N pennies price, as well as the quantity S of goods.
Calculate the total price in rubles and pennies for L goods.
Example:
Input: The price of one item is 3 rubles 20 pennies, count 3 items.
Output: Total price 9 rubles 60 pennies
"""


# 1st variant

roubles, kopecks, amount = map(int, input('Input format: roubles kopecks amount: ').split())

sum_roubles = roubles * amount + kopecks * amount // 100
sum_kopecks = kopecks * amount % 100
print('Summarized price: ', sum_roubles, 'roubles, ', sum_kopecks, ' kopecks.')


# 2nd variant

price, amount2 = map(float, input('Input price (e.g. 2.65) and amount space separated: ').split())

sum_roubles2 = int(price * amount2 // 1)
sum_kopecks2 = int(price * amount % 1 * 100)
print('Summarized price: ', sum_roubles2, 'roubles, ', sum_kopecks2, ' kopecks.')
