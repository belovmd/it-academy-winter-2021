number = num_w = int(input('input number = '))
result = 0

while num_w / 10:
    result = result*10 + num_w % 10
    num_w = num_w // 10

if number == result:
    print('palindrome')
else:
    print('not palindrome')
