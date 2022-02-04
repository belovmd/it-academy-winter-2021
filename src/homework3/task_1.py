# Напишите программу, которая печатает цифры от 1 до 100,
# но вместо чисел, кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz,
# а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz


for elem in range(1, 100):
    if elem % 15 == 0:
        print('FizzBuzz')
    elif elem % 3 == 0:
        print('Fizz')
    elif elem % 5 == 0:
        print('Buzz')
    else:
        print(elem)

print([('FizzBuzz' if (num % 15 == 0) else 'Fizz' if (num % 3 == 0) else 'Buzz' if (num % 5 == 0)
else num) for num in range(1, 100)])
