"""Count the number of lowercase and uppercase letters in the entered line.

Consider only English letters.
"""


lowercase = 0
uppercase = 0
sentence = input('Sentence:')

for _ in sentence:
    # count upper case letters by code range
    if ord(_) in range(65, 91):
        uppercase += 1
    # count lower case letter by code range
    elif ord(_) in range(97, 123):
        lowercase += 1
print('Uppercase:', uppercase, 'Lowercase:', lowercase)
