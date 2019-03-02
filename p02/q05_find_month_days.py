import calendar

year = int(input("Enter year: "))
month = int(input("Enter month number: "))
m = calendar.month_name[month]

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
  leap = True
else:
  leap = False

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
  days = 31
elif month == 4 or month == 6 or month == 9 or month == 11:
  days = 30
elif month == 2 and leap == False:
  days = 28
else:
  days = 29
  
print("{} {} has {} days".format(m, year, days))
