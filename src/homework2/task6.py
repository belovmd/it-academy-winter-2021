# Palindrome test using only numbers (without strings)


number = int(input('Enter number '))
front = number
back = 0
while number:
    back = (back * 10) + (number % 10)
    number //= 10
if front == back:
    print(front, 'is a palindrome')
else:
    print(front, 'is not a palindrome')
