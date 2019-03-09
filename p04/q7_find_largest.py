def find_largest(alist):
    if len(alist) == 0:
      return 0
    elif alist[0] > find_largest(alist[1:]):
      return alist[0]
    else:
      return find_largest(alist[1:])
      
alist = [5, 1, 8, 7, 2]
print(find_largest(alist))
