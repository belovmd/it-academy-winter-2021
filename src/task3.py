str_1 = input("")
str_2 = ""
for elem in str_1:
    if elem not in str_2 and elem != " ":
        str_2 += elem
print(str_2)
