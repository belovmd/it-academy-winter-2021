# Check existence of a triangle. Count square


a = int(input('Enter side a '))
b = int(input('Enter side b '))
c = int(input('Enter side c '))
if a < b + c and b < a + c and c < a + b:
    print('Triangle with sides', a, b, c, 'exists')
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
    print('Area of the triangle is', area)
else:
    print('Triangle doesnt exist')
