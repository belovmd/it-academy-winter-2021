# FizzBuzz

# Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,
# кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz, а вместо чисел
# одновременно кратных и 3 и 5 - FizzBuzz

i = 0
while i < 100:
    i += 1
    if not (i % 3 or i % 5):
        print('FizzBuzz')
    elif not i % 5:
        print('Buzz')
    elif not i % 3:
        print('Fizz')
    else:
        print(i)
