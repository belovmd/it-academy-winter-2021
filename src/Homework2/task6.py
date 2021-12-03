# Определить, является ли число палиндромом

input_number = int(input("Введите число: "))
last_number = input_number % 10

while input_number > 10:
    input_number //= 10
if input_number == last_number:
    print("Это число полиндром")
else:
    print("Это число не полиндром")
