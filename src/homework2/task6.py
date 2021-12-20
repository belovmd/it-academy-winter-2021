n = int(input('Введите число: '))
n_copy = n
reverse_ = 0
while n > 0:
    last_digit = n % 10
    reverse_ = reverse_ * 10 + last_digit
    n //= 10
if n_copy == reverse_:
    print('Число является палиндромом')
else:
    print('Число не является палиндромом')
