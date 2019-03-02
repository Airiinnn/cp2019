side1 = int(input("Enter side 1: "))
side2 = int(input("Enter side 2: "))
side3 = int(input("Enter side 3: "))

if side1 + side2 <= side3 or side2 + side3 <= side1 or side3 + side1 <= side2:
  print("Invalid triangle!")
  
else:
  perimeter = side1 + side2 + side3
  print("Perimeter = {}".format(perimeter))
