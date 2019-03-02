print("%-6s%-11s%-11s%-6s" % ("Miles", "Kilometers", "Kilometers", "Miles"))

for i in range(1, 11):
  print("%-6i%-11.3f%-11i%-6.3f" % (i, i * 1.609, i * 5 + 15, (i * 5 + 15) / 1.609))
