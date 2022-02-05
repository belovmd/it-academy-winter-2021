# 8. Зарегистрируйтесь на одном (или нескольких) из сайтов:
# https://py.checkio.org/ , https://www.codewars.com, https://www.hackerrank.com/, https://acmp.ru
# И решите 1-5 задач уровня Elementary и advanced.
# Поместите 3 простых и 2 сложных задачи на Ваш выбор в пул реквест.


# 1. codewars.com, 7 kyu
# Remove all of the vowels from string
# Note: for this kata "y" isn't considered a vowel.
def disemvowel(string_):
    for elem in string_:
        if elem in "aoeuiAOEUI":
            string_ = string_.replace(elem, "")
    return string_


# 2. hackerrank.com, easy
# The provided code stub reads and integer, n, from STDIN.
# For all non-negative integers i < n, print i in square.
if __name__ == '__main__':
    n = int(input())

if n:
    for elem in range(0, n):
        print(elem ** 2)

# 3. hackerrank.com, easy
# Given an integer, n, perform the following conditional actions:
# If n is odd, print Weird
#   If n is even and in the inclusive range of 2 to 5, print Not Weird
#       If n is even and in the inclusive range of 6 to 20, print Weird
#           If n is even and greater than 20, print Not Weird
if __name__ == '__main__':
    n = int(input().strip())

if (n % 2) or (not n % 2 and n in range(6, 21)):
    print("Weird")
elif (n > 20) or (not n % 2 and n in range(2, 6)):
    print("Not Weird")


# 4. hackerrank.com, medium
# Given a year, determine whether it is a leap year.
# If it is a leap year, return the Boolean True, otherwise return False.
# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function.
# It is only necessary to complete the is_leap function.
# In the Gregorian calendar, three conditions are used to identify leap years:
#   The year can be evenly divided by 4, is a leap year, unless:
#       The year can be evenly divided by 100, it is NOT a leap year, unless:
#           The year is also evenly divisible by 400. Then it is a leap year.
def is_leap(year):
    leap = False

    if (not year % 4) and (year % 100) or (not year % 400):
        leap = True

    return leap


year = int(input())
print(is_leap(year))


# 5. codewars.com, 5 kyu
# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.
def generate_hashtag(s):
    hashtag = "#" + s.title().replace(" ", "")

    if len(hashtag) > 140 or not len(s):
        return False
    else:
        return hashtag


# 6. codewars.com, 4 kyu
# Complete the solution so that it strips all text that follows any of a set of comment markers
# passed in. Any whitespace at the end of the line should also be stripped out.
"""
Input:
    apples, pears # and bananas
    grapes
    bananas !apples
Output:
    apples, pears
    grapes
    bananas
"""


def solution(string, markers):
    str_list = string.split("\n")
    new_list = []

    for item in str_list:
        str_ = ""
        for char in item:
            if char in markers:
                break
            else:
                str_ = str_ + char
        new_list.append(str_.strip())
    return "\n".join(new_list)
