import random

def print_matrix(n):
  z = 1
  y = 0
  while y < n:
    for i in range(n):
      a = random.randint(0, 1)
      if z != n:
        print(str(a), end=" ")
        z += 1
      elif z == n:
        print(str(a))
        z = 1
    y += 1
  
num = int(input())
print_matrix(num)
