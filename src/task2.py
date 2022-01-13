s = input("Введите ваш текст: ")
w = max(s.split(), key=len)
print("Самое длинное слово в предложении: ", w)
