side_a, side_b, side_c = map(int, input('input side_a, side_b, side_c by space').split())
print(side_a, side_b, side_c)

if side_a + side_b > side_c and side_b < side_b + side_c:
    print('this is a triangle')
else:
    print('this is a not triangle')
