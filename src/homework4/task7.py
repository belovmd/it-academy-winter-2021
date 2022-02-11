# There are two natural number. Calculate their greatest common divisor using Euclid's algorithm

number1 = int(input("Enter first number "))
number2 = int(input("Enter second number "))
while number1 != 0 and number2 != 0:
    if number1 > number2:
        number1 = number1 % number2
    else:
        number2 = number2 % number1
print("GCD: ", number1 + number2)
