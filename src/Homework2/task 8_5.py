# Даны 2 целых числа a и b, которые могут быть положительными или отрицательными,
# найти сумму всех целых чисел между ними включительно и вернуть ее.
# Если два числа равны, верните a или b.

list_ = [int(input("Enter first number: ")), int(input("Enter second number: "))]
list_.sort()
result = 0

if list_[0] != list_[1]:
    for elem in range(list_[0],list_[1]+1):
        result += elem
else:
    result = list_[0]

print(result)