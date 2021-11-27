"""Count the number of lowercase (small) and uppercase (uppercase) letters in the entered line.

Consider only English letters.
Uppercase codes: 65-90, lowercase codes: 97-122
"""


lowercase = 0
uppercase = 0
sentence = input('Sentence:')

for _ in sentence:
    if ord(_) in range(65, 91):
        uppercase += 1
    elif ord(_) in range(97, 123):
        lowercase += 1
print('Uppercase:', uppercase, 'Lowercase:', lowercase)
