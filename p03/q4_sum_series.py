def m_series(i):
  print("%-10s%-10s" % ("i", "m(i)"))
  for j in range(1, i+1):
    n = 0
    for a in range(2, j+2):
      m = 1 - 1/a 
      n += m
    print("%-10i%-10.4f" % (j, n))

m_series(20)
