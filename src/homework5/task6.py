# Entering number. Find his max divisor that is power of 2.

def div(number):
    divisor = 1
    step = 1
    while step <= number:
        step = step << 1
        if not number % step:
            divisor = step
    print(divisor)


div(int(input('Enter number ')))
