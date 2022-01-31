"""Required to remove duplicate characters and spaces from the input string.

For example, if "abc cde def" was entered, then "abcdef" should be output.
"""

import string

sentence = input('Input sentence: ').replace(' ', '')
output = ''

for char in sentence:
    if char not in string.punctuation and char not in output:
        output = output + char
print(output)
