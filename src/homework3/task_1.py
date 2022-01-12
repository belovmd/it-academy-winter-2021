# Напишите программу, которая печатает цифры от 1 до 100,
# но вместо чисел, кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz,
# а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz

for elem in range(1, 100):
    if elem % 3 == 0 and elem % 5 == 0:
        print('Fizz')
    elif elem % 3 == 0:
        print('Buzz')
    elif elem % 5 == 0:
        print('FizzBuzz')
    else:
        print(elem)
