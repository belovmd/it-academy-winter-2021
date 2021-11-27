"""Required to remove duplicate characters and spaces from the input string.

For example, if "abc cde def" was entered, then "abcdef" should be output.
"""


punctuation = '!"#$%&\'()*+,-./:;<=>?@[]^_`{|}~ '
output = ''
sentence = input('Input sentence:')

for _ in sentence:
    if _ not in punctuation and _ not in output:
        output = output + _
        print(output)
print(output)
