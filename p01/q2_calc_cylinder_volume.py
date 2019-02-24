import math

radius = float(input("Enter radius of base: "))
length = float(input("Enter length of cylinder: "))

area = radius ** 2 * math.pi
volume = area * length

print(volume)
