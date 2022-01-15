# task 4
"""
Даны два списка чисел. Посчитайте, сколько различных чисел входит только в один из этих списков
"""

list1_ = [int(number1) for number1 in input("Enter the first list of numbers: ").split()]
list2_ = [int(number2) for number2 in input("Enter the second list of numbers: ").split()]
print("Numbers amount only in one of sets is: ", len(set(list1_) ^ set(list2_)))
