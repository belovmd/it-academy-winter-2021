"""Count the number of lowercase and uppercase letters in the entered line.

Consider only English letters.
"""

lowercase = 0
uppercase = 0
sentence = input('Sentence:')

for char in sentence:
    if 65 <= ord(char) <= 90:
        uppercase += 1
    elif 97 <= ord(char) <= 122:
        lowercase += 1
print('Uppercase:', uppercase, 'Lowercase:', lowercase)
