def gcd(m, n):           # Euclidean algorithm
  if m % n == 0:
    return n
  else:
    return gcd(n, m % n)
    
print(gcd(24, 16))
print(gcd(255, 25))
