# Определить, является ли число палиндромом

input_number = int(input("Enter number: "))
fix_number = input_number
reverse_number = 0

while input_number > 0:
    last_number = input_number % 10
    reverse_number = reverse_number * 10 + last_number
    input_number //= 10
if reverse_number == fix_number:
    print("This is polindrome")
else:
    print("This is not polindrome")


