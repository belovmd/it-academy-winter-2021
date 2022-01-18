# 1_easy (pynative.com):
# Print multiplication table from 1 to 10

number = 10
for i in range(1, number + 1):
    for j in range(1, number + 1):
        print(i * j, end=' ')
    print()

# 2_easy (pynative.com):
# Write a function called exponent(base, exp) that returns an int value
# of base raises to the power of exp.
# Note here exp is a non-negative integer, and the base is an integer.
base = 2
exponent = 5


def exponent_function(bas, exp):
    result = 1
    for i in range(1, exp + 1):
        result = result * bas
    return


print(exponent_function(base, exponent))

# 3_easy (pynative.com):
# Write a program to display all prime numbers within a range
# Note: A Prime Number is a number that cannot be made by multiplying other whole numbers.
# A prime number is a natural number greater than 1
# that is not a product of two smaller natural numbers
# Examples:
# 6 is not a prime number because it can be made by 2×3 = 6
# 37 is a prime number because no other whole numbers multiply together to make it.

for number in range(1, 55):
    for i in range(2, number):
        if not number % i:
            break
    else:
        print(number)

# 4_hard (codewars.com):
# In this kata you are required to, given a string, replace every letter with
# its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
# "a" = 1, "b" = 2, etc.
# Example
# alphabet_position("The sunset sets at twelve o' clock.")
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
# ( as a string )

my_string = 'What a marvelous day!'
my_list = list(my_string)
new_list = []
for el in my_list:
    if el.isalpha():
        new_list.append(ord(el))
for i in range(len(new_list)):
    # for uppercase letters in ASCII
    if new_list[i] <= 90:
        new_list[i] = str(new_list[i] - 64)
    else:
        # for lowercase letters in ASCII
        new_list[i] = str(new_list[i] - 96)
new_string = ' '.join(new_list)
print(new_string)

# 5_hard (codewars.com)
# A pangram is a sentence that contains every single letter of the alphabet at least once.
# For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
# because it uses the letters A-Z at least once (case is irrelevant).
# Given a string, detect whether or not it is a pangram. Return True if it is, False if not.
# Ignore numbers and punctuation.

my_string = 'The quick, brown fox jumps over the lazy dog!'
new_string = my_string.lower()
D = dict.fromkeys('abcdefghijklmnopqrstuvwxyz', 0)
for el in new_string:
    if el in D:
        D[el] += 1
for value in D.values():
    if not value:
        print('False')
        break
else:
    print('True')
