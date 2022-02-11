# There are two lists of numbers. Count, how many difference numbers belong to both of lists.

list1 = input("Enter first list: ")
list1 = list1.split()
list2 = input("Enter second list: ")
list2 = list2.split()
print(len(set(list1) & set(list2)))
