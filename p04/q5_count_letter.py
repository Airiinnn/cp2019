def count_letter(str, ch):
  if ch not in str:
    return 0
  elif str[0] == ch:
    return count_letter(str[1:], ch) + 1
  else:
    return count_letter(str[1:], ch)

print(count_letter("Welcome", 'e'))
