# Вам дано положительное целое число. Определите сколько цифр оно имеет.

number = int(input("Enter positiv number:" ))

if number > 0:
    str_ = str(number)
    print("Number has digits:", len(str_))
else:
    print("Number must be greater than zero")
