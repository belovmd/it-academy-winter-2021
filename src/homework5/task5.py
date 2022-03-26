# Write a program that finds the nearest power of two to the number you enter

def power(number):
    prev = 1
    step = prev << 1
    while step <= number:
        prev = step
        step = step << 1
    if step - number < number - prev:
        print(step)
    else:
        print(prev)


power(int(input('Enter number ')))
