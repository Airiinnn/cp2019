def find_num_uppercase(s):
  if len(s) == 0:
    return 0
  elif s[0].isupper():
    return 1 + find_num_uppercase(s[1:])
  else:
    return find_num_uppercase(s[1:])
    
find_num_uppercase('Good MorninG!')
