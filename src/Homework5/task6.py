'''
6. Вводится число найти его максимальный делитель,
являющийся степенью двойки. 10(2) 16(16), 12(4).
Задачу поместите в файл task6.py в папке src/homework5.

'''
chislo = int(input('Введите число: '))
step = 1
while not (chislo % (step * 2)):
    step = step * 2
print(step)
