"""Third task for the lesson.

Given: three sides of a triangle.
Required: check if these are actually the sides of a triangle.
If the sides define a triangle, find its area.
If not, display an invalid data message.
"""

input_ = input('Input triangle sides separately: ').split()
side1, side2, side3 = (int(value) for value in input_)

if ((side1 < side2 + side3)
        and (side2 < side1 + side3)
        and (side3 < side1 + side2)):
    p = (side1 + side2 + side3) / 2
    area = (p * (p - side1) * (p - side2) * (p - side3)) ** 0.5
    print('It is triangle. Area:', area)
else:
    print('Incorrect data: it is not triangle')
