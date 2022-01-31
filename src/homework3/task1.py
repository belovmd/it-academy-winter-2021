"""Write a program that prints numbers from 1 to 100.

But instead of numbers divisible by 3 it writes Fizz,
instead of numbers divisible by 5 it writes Buzz,
and instead of numbers simultaneously divisible by both 3 and 5,
it writes FizzBuzz.
"""

for number in range(101):
    if number % 3 and number % 5:
        print(number)
    elif number % 5:
        print('Fizz')
    elif number % 3:
        print('Buzz')
    else:
        print('FizzBuzz')
