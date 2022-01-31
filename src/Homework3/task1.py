'''
1.	FizzBuzz
Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,
кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz,
а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
'''
for i in range(1, 101):
    prn = i
    if i % 3 == 0:
        prn = 'Fizz'
    if i % 5 == 0:
        prn = 'Buzz'
    if i % 15 == 0:
        prn = 'FizzBuzz'
    print(prn)
