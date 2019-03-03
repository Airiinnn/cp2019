def gcd(m, n):
  i = 1
  while i <= m and i <= n:
    if m % i == 0 and n % i == 0:
      a = i
    i += 1
  print(a)

gcd(24, 16)
gcd(255, 25)
