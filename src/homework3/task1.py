# FizzBuzz

# Write a program that prints numbers from 1 to 100, but instead of multiples of 3, writes Fizz,
# instead of multiples of 5, writes Buzz, and instead of multiples of both 3 and 5, FizzBuzz

for el in range(1, 101):
    if not el % 3:
        if not el % 5:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif not el % 5:
        print("Buzz")
    else:
        print(el)
