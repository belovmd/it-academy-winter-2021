"""Write a program that calculates the total price.

Enter M rubles and N kopecks price, as well as the quantity S of goods.
Calculate the total price in rubles and kopecks for L goods.
Example:
Input: The price of one item is 3 rubles 20 kopecks, count 3 items.
Output: Total price 9 rubles 60 kopecs
"""

input_ = input('Input roubles kopecks amount: ').split()
roubles, kopecks, amount = (int(value) for value in input_)

sum_roubles = roubles * amount + kopecks * amount // 100
sum_kopecks = kopecks * amount % 100
print('Total price: ', sum_roubles, 'roubles, ', sum_kopecks, ' kopecks.')
