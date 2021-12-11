"""Print the n-th Fibonacci number.

Use only temporary variables, cyclic statements, and conditional statements.
n - inputed.
"""


n = input('Input n:')

fibnum1 = 1
fibnum2 = 1

for i in range(1, int(n)):
    fibnum1, fibnum2 = fibnum2, fibnum1 + fibnum2
print(fibnum1)
