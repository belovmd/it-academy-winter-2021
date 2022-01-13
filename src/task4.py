a = int(input("Введите число:"))
number = a
rev = 0
while a > 0:
    dig = a % 10
    rev = rev * 10 + dig
    a = a // 10
if(number == rev):
    print("Это палиндром!")
else:
    print("Это не палиндром!")
