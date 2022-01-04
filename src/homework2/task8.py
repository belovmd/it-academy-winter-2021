# Register on one (or several) of the sites: (hackerrank.com) solve
# 1-5 tasks of the Elementary and advanced level.
# Place 3 easy and 2 hard tasks of your choice in the Pull Request.


# easy

# You are given a string and your task is to swap cases.
# In other words, convert all lowercase letters to uppercase letters and vice versa.

def swap_case(s):
    result_ = ""
    for char in s:
        if "a" <= char <= "z":
            result_ += char.upper()
        else:
            result_ += char.lower()
    return result_


# Ms. Gabriel Williams is a botany professor at District College.
# One day,she asked her student Mickey to compute
# the average of all the plants with distinct heights in her greenhouse.

def average(array):
    st = set(array)
    return (sum(st) / len(st))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


# Vasya offers a version of his four-digit number,
# consisting of different numbers, and Petya gives Vasya a hint:
# he tells the number of bulls and cows.
# Bulls is the number of digits in the number proposed by Vasya that coincide in
# meaning and are in the correct position in the number conceived by Petya.
# Cows - the number of digits that match in value, but are in the wrong position.
# The only line contains two four-digit natural numbers, you need to output two integers
# separated by a space - the number of bulls and cows

bulls = 0
cows = 0
n = list(map(str, input().split()))
for el in range(4):
    if n[0][el] in n[1]:
        if n[0][el] == n[1][el]:
            bulls += 1
        else:
            cows += 1
print(bulls, cows)


# hard

# Petya builds stairs from cubes.
# The staircase consists of several towers of blocks being built next to each other,
# each of which is exactly one cube higher than the previous one.
# It is required to determine the height of the last step
# in the cubes by the number of cubes available to the Petya.

k = int(input())
size = 0
while k:
    size += 1
    step = 0
    while step < size:
        step += 1
        k -= 1
        if k == 0:
            break
print(step)


# N baskets contain gold coins. In all but one of the baskets, the coins weigh w grams.
# In one basket the coins are# counterfeit and weigh w – d grams.
# The wizard takes 1 coin from the first basket, 2 coins from the second basket,
# and so on, and finally N-1 coins from the (N-1) th basket. He takes nothing from the N-th basket.
# He weighs the coins he has taken and immediately points to the basket of counterfeit coins.

n = int(input("Count of baskets "))
w = int(input("Weight "))
d = int(input("False weight "))
p = int(input("Total weight "))
dif = sum(range(1, n)) * w - p
if not dif:
    print(n)
else:
    print(int(dif / d))
