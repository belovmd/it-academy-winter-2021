# Напишите программу, которая печатает цифры от 1 до 100,
# но вместо чисел, кратных 3 пишет Fizz,
# вместо чисел кратный 5 пишет Buzz,
# а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz

list_ = [elem for elem in range(1, 101)]
result = []

for elem in list_:
    if not(elem % 3) and not(elem % 5):
        result.append("FizzBuzz")
    elif not(elem % 5):
        result.append("Buzz")
    elif not (elem % 3):
        result.append("Fizz")
    else:
        result.append(elem)

print(result)
