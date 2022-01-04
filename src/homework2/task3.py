# Delete spaces and duplicate characters from string


str_ = input("Enter line ")
str_ = str_.replace(" ", "")
str2_ = ""
for char in str_:
    for el in str2_:
        if char == el:
            break
    else:
        str2_ += char
print(str2_)
