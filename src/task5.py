#Написать программу которая находит ближайшую степень двойки к введенному числу.
# 10(8), 20(16), 1(1), 13(16)

number = int(input("Enter your number: "))
bin_number = format(number, "b")

result_1 = 2 ** (len(bin_number)-1)
result_2 = 2 ** (len(bin_number))

if abs(result_1 - number) < abs(result_2 - number):
    print(result_1)
else:
    print(result_2)
