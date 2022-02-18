'''
5.  Написать программу которая находит ближайшую степень двойки
к введенному числу. 10(8), 20(16), 1(1), 13(16)
Задачу поместите в файл task5.py в папке src/homework5.
'''

chislo = int(input('Введите число: '))
step_a = step_b = 1
while step_a < chislo and step_b < chislo:
    step_a = step_b * 2
    if step_a < chislo:
        step_b = step_a * 2
else:
    if abs(chislo - step_a) < abs(chislo - step_b):
        print(step_a)
    elif abs(chislo - step_b) < abs(chislo - step_a):
        print(step_b)
    else:
        print(step_a)
