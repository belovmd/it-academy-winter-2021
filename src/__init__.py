#while True :
   a = int(input('Введите число: '))
   if a%2 > 0 :
      print('ого')
   elif a%2 == 0 and a < 0 :
      print('маловато')
   elif a%2 == 0 and  a > 0 :
      print('нормально')
   elif a == 0 :
      print('на нет спроса нет')
   
S = float()
#while True:
      a = float(input("Введите длину первой стороны: "))
      b = float(input("Введите длину второй стороны: "))
      c = float(input("Введите длину третьей стороны: "))
      if a + b > c or a + c > b or b + c > a :
         p = float((a+b+c)/2)
         S = (p*(p-a)*(p-b)*(p-c))**.5
         print ('Площадь треугольника =', S)
      else :
         print ('Это не треугольник')
