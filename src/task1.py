"""Write a program that prints numbers from 1 to 100.

But instead of numbers divisible by 3 it writes Fizz,
instead of numbers divisible by 5 it writes Buzz,
and instead of numbers simultaneously divisible by both 3 and 5 it writes FizzBuzz.
"""

for _ in range(101):
    if _ % 3 and _ % 5:
        print(_)
    elif _ % 5:
        print('Fizz')
    elif _ % 3:
        print('Buzz')
    else:
        print('FizzBuzz')


""" The one below is less readeable, but for me is more logical"""

# for _ in range(101):
#     if not _ % 3  and not _ % 5:
#         print('FizzBuzz')
#     elif not _ % 3:
#         print('Fizz')
#     elif not _ % 5:
#         print('Buzz')
#     else:
#         print(_)
