# Требуется удалить из строки повторяющиеся символы и все пробелы

input_str = input("Введите строку:")
str_without_space = input_str.replace(" ", "")
output_str = ""

for elem in str_without_space:
    if elem in output_str:
        continue
    else:
        output_str += elem

print(output_str)
