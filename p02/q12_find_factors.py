ognum = int(input())
num = ognum
list = []
i = 2

while i ** 2 < ognum:
  if i == 2 and num % i == 0:
    num = num / i
    list.append(i)
  elif i % 2 != 0 and num % i == 0:
    num = num / i
    list.append(i)
  else:
    i += 1
    
print(list)
