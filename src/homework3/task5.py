# unique elements in list

# There is a list. Print elements that appear only ones. Print their in the origin order

lst = [element for element in input("Elements of the list: ").split()]
dct = {}
for el in lst:
    dct[el] = dct.get(el, 0) + 1
for key in dct:
    if dct[key] == 1:
        print(key)
