# Count numbers of lowercase and uppercase letters


src_ = input("Enter line ")
lower = upper = 0
for char in src_:
    if "a" <= char <= "z":
        lower += 1
    if "A" <= char <= "Z":
        upper += 1
print("Number of lowercase:", lower, "uppercase:", upper)
