"""Required to remove duplicate characters and spaces from the input string.

For example, if "abc cde def" was entered, then "abcdef" should be output.
"""


import string

sentence = input('Input sentence:').replace(' ','')
output = ''

for _ in sentence:
    if _ not in string.punctuation and _ not in output:
        output = output + _
print(output)
