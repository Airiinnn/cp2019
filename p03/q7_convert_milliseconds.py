def convert_ms(n):
  h = 0
  m = 0
  if n < 60000:
    s = n // 1000
  elif 60000 < n < 3600000:
    m = n // 60000
    s = (n - m * 60000) // 1000
  else:
    h = n // 3600000
    m = (n - h * 3600000) // 60000
    s = (n - h * 3600000 - m * 60000) // 1000
  print("{}:{}:{}".format(h, m ,s))
  
num = int(input())
convert_ms(num)
