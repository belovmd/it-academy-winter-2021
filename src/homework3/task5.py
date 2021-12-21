# 5. Уникальные элементы в списке
# Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.

# Если список дан изначально:
# lst = ["abc", 1, 2, 2, 3, 4, 5, 3, "elem", "abc"]
# Либо, если список составляет пользователь:
lst_quantity = int(input("Введите количество элементов в списке: "))
lst = []
for lst_obj in range(lst_quantity):
    lst.append(input('Введите объект списка: '))

lst_result = []
for elem in lst:
    if elem not in lst_result:
        lst_result.append(elem)

print(lst_result)
