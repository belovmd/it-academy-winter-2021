a = int(input())  # рубли
b = int(input())  # копейки
n = int(input())  # количество товара
print(((a * 100 + b) * n // 100), int(b * n % 100))
