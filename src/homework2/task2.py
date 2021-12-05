"""Find the longest word in the entered sentence.

Please note that the sentence contains punctuation marks.
Hints:
my_string.split ([chars]) returns a list of strings.
len (list) - the number of items in the list
"""

import re
import string

sentence = input('Sentence: ')


# Solution 1:

sentence1_split = sentence.split()
for i in range(len(sentence1_split)):
    sentence1_split[i] = sentence1_split[i].strip(string.punctuation)
print('Solution 1:', max(sentence1_split, key=len), end='\n\n')


# Solution 2:

# duplication of input, just to make solutions independent
sentence2 = sentence
for _ in sentence2:
    if _ in string.punctuation:
        sentence2 = sentence2.replace(_, '')
sentence2_split = sentence2.split()
print('Solution 2:', max(sentence2_split, key=len), end='\n\n')


# Solution 3 (googled):

sentence3 = re.sub(r'[^\w\s]', ' ', sentence)
print('Solution 3 (googled):', max(sentence3.split(), key=len))
