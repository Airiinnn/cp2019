def reverse_int(n):
  n = str(n)
  if len(n) == 0:
    return n
  else:
    return reverse_int(n[1:]) + n[0]
    
a = int(input())
print(reverse_int(a))
