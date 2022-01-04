# Print nth Fibonacci number using only temporary variables, looping statements and conditional statements


index = int(input('Which fibonacci number do you wanna see? '))
fib1, fib2 = 0, 1
if index == 1:
    print(fib1)
elif index == 2:
    print(fib2)
else:
    for el in range(2, index):
        fib = fib1 + fib2
        fib1 = fib2
        fib2 = fib
    print(fib)
