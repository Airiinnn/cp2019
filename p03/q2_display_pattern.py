def display_pattern(n):
  a = [] 
  b = "1"
  a.append(b)
  for i in range(2, n+1):
    b = str(i) + " " + b
    a.append(b)
  
  for i in range(n):
    print(a[i].rjust(n*2))
    
num = int(input())
display_pattern(num)
