"""Find the longest word in the entered sentence.

Please note that the sentence contains punctuation marks.
Hints:
my_string.split ([chars]) returns a list of strings.
len (list) - the number of items in the list
"""

import string

input_ = input('Source sentence: ')

words = input_.split()
for word in words:
    word = word.strip(string.punctuation)
print('Longest word:', max(words, key=len))
