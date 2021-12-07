# У вас есть число и нужно определить какая цифра из этого числа является наибольшей

number = input("Enter numbers: ")
max_number = 0

for elem in number:
    elem = int(elem)
    if elem > max_number:
        max_number = elem
print("Max digit is:", max_number)
