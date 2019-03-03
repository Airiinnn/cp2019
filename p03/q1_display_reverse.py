def reverse_int(n):
  reverse = ''
  for i in range(len(n), 0, -1):
    reverse += num[i-1]
  print(int(reverse))
    
num = input()
reverse_int(num)
