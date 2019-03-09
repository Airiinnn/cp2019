def sum_digits(n):  
  if len(str(n)) == 1:
    return n
  else:
    return(sum_digits(int(str(n)[0]) + int(str(n)[1:])))
    
print(sum_digits(234))
