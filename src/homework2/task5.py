"""Print the n-th Fibonacci number.

Useonly temporary variables, cyclic statements, and conditional statements.
n - inputed.
"""


n = input('Input n:')


# Splution 1 (newer and better):

fibnum1 = 1
fibnum2 = 1

for i in range(1, int(n)):
    fibnum1, fibnum2 = fibnum2, fibnum1 + fibnum2
print(fibnum1)


# Solution 2 (old):

fibnum = 0
fibnum1 = 1
fibnum2 = 1

for _ in range(2, int(n)):
    fibnum = fibnum1 + fibnum2
    fibnum1 = fibnum2
    fibnum2 = fibnum
print(fibnum)
