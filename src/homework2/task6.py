"""Determine if the number is a palindrome (reads from left to right and right to left the same).

A positive integer number of arbitrary length.
The task requires you to work only with numbers
(without converting the number to a string or anything else)
"""

number = int(input('Input the number:'))
number_compute = number
rebnum = 0

while number_compute > 0:
    rebnum = rebnum * 10 + number_compute % 10
    number_compute = number_compute // 10
if number == rebnum:
    print('The number is palindrome')
else:
    print('The number is not palindrome')
