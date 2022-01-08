# task 1 FizzBuzz

"""Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел, кратных 3 пишет Fizz,
вместо чисел кратный 5 пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz"""

list_ = [number for number in range(1, 101)]
final_list = []

for number in list_:
    if not (number % 3):
        final_list.append("Fizz")
    elif not (number % 5):
        final_list.append("Buzz")
    elif not (number % 3) and not (number % 5):
        final_list.append("FizzBuzz")
    else:
        final_list.append(number)

print(final_list)
