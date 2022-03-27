# Написать программу которая находит ближайшую степень
# к введенному числу

num = int(input("Enter number: "))
b_num = f'{num:b}'
result_1 = 2 ** (len(b_num))
result_2 = 2 ** (len(b_num) - 1)

if abs(result_1 - num) < abs(result_2 - num):
    print('two in power : ', result_1)
else:
    print('two in power : ', result_2)
