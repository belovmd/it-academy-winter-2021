# Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
# Учитывать только английские буквы.

str_ = input("Enter the sentence:")
lowercase = 0
uppercase = 0

for elem in str_:
    if "a" <= elem <= "z":
        lowercase += 1
    elif "A" <= elem <= "Z":
        uppercase += 1
print("Number lowercase: ", lowercase, "Nomber uppercase:", uppercase, sep='\n')
