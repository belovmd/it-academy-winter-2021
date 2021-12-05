"""Third task for the lesson.

Given: three sides of a triangle.
Required: check if these are actually the sides of a triangle.
If the sides define a triangle, find its area.
If not, display an invalid data message.
"""


side1, side2, side3 = map(int, input('Input triangle sides space separated: ').split())

if (side1 < side2 + side3) and (side2 < side1 + side3) and (side3 < side1 + side2):
    p = (side1 + side2 + side3) / 2
    S = p * (p - side1) * (p - side2) * (p - side3) ** 0.5
    print('It is triangle. Area:', S)
else:
    print('Incorrect data: it is not triangle')
