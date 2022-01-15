# task 3
"""Даны два списка чисел. Посчитайте, сколько различных чисел содержится
одновременно как в первом списке, так и во втором."""

list1_ = [int(number1) for number1 in input("Enter the first list of numbers: ").split()]
list2_ = [int(number2) for number2 in input("Enter the second list of numbers: ").split()]
print("Numbers amount in both of sets is: ", len(set(list1_) & set(list2_)))
