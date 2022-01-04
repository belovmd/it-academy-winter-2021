# Palindrome test using only numbers (without strings)


number = int(input('Enter number '))
long = int(0)
counter = 1
while number // counter:
    counter *= 10
    long += 1
for step in range(1, int((long / 2) + 1)):
    if ((number // (10 ** (long - step))) % 10) != ((number % 10 ** step) // (10 ** (step - 1))):
        print(number, 'is not a palindrome')
        break
else:
    print(number, 'is a palindrome')
