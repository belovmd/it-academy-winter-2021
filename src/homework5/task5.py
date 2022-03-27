num = int(input("Enter number: "))
b_num = f'{14:b}'
result_1 = 2 ** (len(b_num))
result_2 = 2 ** (len(b_num) - 1)

if abs(result_1 - num) < abs(result_2 - num):
    print('power : ', (len(b_num)), '; two in power : ', result_1)
else:
    print('power : ', (len(b_num)), '; two in power : ', result_2)