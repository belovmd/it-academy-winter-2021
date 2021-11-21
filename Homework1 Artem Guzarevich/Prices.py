prices = {'apple': 0.45, 'banana': 0.57}
my_purchase = {
    'apple': 5,
    'banana': 10}
grocery_bill = sum(prices[fruit] * my_purchase[fruit]
                   for fruit in my_purchase)
print ('I owe the grocer $%.2f' % grocery_bill)