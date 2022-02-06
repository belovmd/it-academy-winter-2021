"""Зарегистрируйтесь на одном (или нескольких) из сайтов:
https://py.checkio.org/ , https://www.codewars.com,
https://www.hackerrank.com/, https://acmp.ru
И решите 1-5 задач уровня Elementary и advanced.
Поместите 3 простых и 2 сложных задачи на Ваш выбор в пул реквест.
"""
# Elementary tasks - 1-3
# Advanced tasks - 4-5
# task 1 Given a string, you have to return(from codewars.com)
# a string in which each character (case-sensitive) is repeated once.
# Input:
# String
# Output:
# SSttrriinngg
# Input:
# Hello World
# Output:
# HHeelllloo  WWoorrlldd
# Input:
# 1234!_
# Output:
# 11223344!!__
# double_char("String") ==> "SSttrriinngg"
# double_char("Hello World") ==> "HHeelllloo  WWoorrlldd"
# double_char("1234!_ ") ==> "11223344!!__  """"
str_ = input("Enter your string: ")
print("".join(char * 2 for char in str_))

# task 2
# Try to find out how many zeros a given number has at the end (from py.checkio.org)
# Input: a positive Int
# Output: an Int
# Examples:
# Input: 0
# Output: 1
# Input: 1
# Output: 0
# Input: 10
# Output: 1
# Input: 101
# Output: 0
# Input: 100100
# Output: 2
input_number = int(input("Enter the number: "))
str_ = str(input_number)
zeros_amount = len(str_) - len(str_.rstrip("0"))
print(zeros_amount)

# task 3
"""The goal of this kata is to write a function that takes two inputs:
a string and a character. The function will count the number of times
that character appears in the string. The count is case insensitive.
For example:
count_char("fizzbuzz","z") => 4
count_char("Fancy fifth fly aloof","f") => 5"""


def count_char(our_string, char):
    total = 0
    low_char = char.lower()
    low_string = our_string.lower()
    for i in low_string:
        if i == low_char:
            total += 1
    return total


print(count_char("fizzbuzz", "z"))
print(count_char("Fancy fifth fly aloof", "f"))

# task 4
"""In a given text you need to sum the numbers
while excluding any digits that form part of a word.
The text consists of numbers, spaces and letters from the English alphabet.
Input: A string.
Output: An int."""
# Example
"""sum_numbers('hi') == 0
sum_numbers('who is 1st here') == 0
sum_numbers('my numbers is 2') == 2
sum_numbers('This picture is an oil on canvas '
'painting by Danish artist Anna '
'Petersen between 1845 and 1910 year') == 3755
sum_numbers('5 plus 6 is') == 11
sum_numbers('') == 0"""
"""The isnumeric() method returns True if all the characters are numeric (0-9),
otherwise False.
Exponents, like ² and ¾ are also considered to be numeric values.
"-1" and "1.5" are NOT considered numeric values, because all the characters
in the string must be numeric, and the - and the . are not."""


def sum_numbers(text):
    result = 0
    split_text = text.split(" ")
    for word in split_text:
        if word.isnumeric():
            number = int(word)
            result += number
    return result


print(sum_numbers('hi'))
print(sum_numbers('who is 1st here'))
print(sum_numbers('my numbers is 2'))
print(sum_numbers('This picture is an oil on canvas '
                  'painting by Danish artist Anna '
                  'Petersen between 1845 and 1910 year'))
print(sum_numbers('5 plus 6 is'))
print(sum_numbers(''))

# task 5
# Sieve of Eratosthenes
"""At this task we should find all prime numbers till some integer number
First of all we need to find the smallest prime number. It is 2.
Then we need to exclude all numbers which are multiples of 2 from 2**2 = 4
to our input number.
Then we need to repeat this procedure for next prime number. It is 3.
We need to exclude all multiples of 3 from 3**2 = 9 to our input number.
Then we need to repeat this procedure for 5. We exclude all multiples of 5 from
5**2 = 25 to our input number.

We need to repeat this process till
we have not prime numbers which are less than input number"""


# examples:
# sieve_eratosphenes(10) == [2, 3, 5, 7]
# sieve_eratosphenes(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# sieve_eratosphenes(120) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
# 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]

def sieve_eratosphenes(input_number):
    sieve = [item for item in range(input_number + 1)]
    # we need to exclude 1 which is not prime number from theory of school math, that's why
    sieve[1] = 0
    for divisor in sieve:
        if divisor >= 2:
            for number in range(divisor ** 2, len(sieve), divisor):
                sieve[number] = 0
    final_sieve = [prime for prime in sieve if prime != 0]
    return final_sieve


print(sieve_eratosphenes(30))
