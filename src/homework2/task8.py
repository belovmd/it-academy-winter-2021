# Print multiplication table from 1 to 10

number = 10
for i in range(1, number + 1):
    for j in range(1, number + 1):
        print(i * j, end=' ')
    print()

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
