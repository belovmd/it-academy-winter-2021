for i in range(1, 100):

    if i % 3 == 0:
        i = 'Fizz'
    elif i % 5 == 0:
        i = 'Buzz'
    elif i % 3 == 0 and i % 5 == 0:
        i = 'FizzBuzz'

    print(i)
