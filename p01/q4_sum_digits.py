number = int(input())

if number == 1000:
   print(1)

else:
   ones = number % 10
   tens = number // 10 % 10
   hundreds = number // 100 % 10

   print(ones + tens + hundreds)
