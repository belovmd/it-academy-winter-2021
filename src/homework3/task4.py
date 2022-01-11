# Couples

# Count how many same couples. Any same elements are couples.
# Input data - line of numbers with spaces. Output data - number of couples.

lst = [int(number) for number in input("Elements: ").split()]
count = 0
step = 1
for el in lst:
    count += lst[step::].count(el)
    print(lst[step::])
    step += 1
print(count)
