# List practice

# 1. Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].

my_list = [first_el + second_el for first_el in 'ab' for second_el in 'bcd']
print(my_list)

# 2. Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].

my_list = my_list[:1] + my_list[2:3] + my_list[4:5]
print(my_list)

# 3. Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].

new_list = [digit + letter for digit in '1234' for letter in 'a']
print(new_list)

# 4. Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.

new_list.remove('2a')
print(new_list)

# 5. Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке этого элемента не было.

final_list = new_list.copy()
final_list.insert(1, '2a')
print(final_list)
