import math

def is_prime(n):
  if n == 2:
    return True
  elif n % 2 == 0:
    return False
  else:
    for i in range(2, int(math.sqrt(n)) + 1):
      if n % i == 0:
        return False
    return True
    
a = []
b = 2
while len(a) < 1000:
  if is_prime(b) == True:
    a.append(b)
  b += 1
  
k = 0
m = 0
while k < 1000:
  if m != 9:
    print("%-5s" % (a[k]), end=" ")
    k += 1
    m += 1
  elif m == 9:
    print("%-5s" % (a[k]))
    k += 1
    m = 0
