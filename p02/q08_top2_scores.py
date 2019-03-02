t = int(input("Number of students: "))
dict = {}

for i in range(t):
  name = input("Name: ")
  score = int(input("Score: "))
  dict[score] = name
  
list = []
for i in dict:
  list.append(i)
list.sort(reverse=True)
print("{} got highest with {} points.".format(dict.get(list[0]), list[0]))
print("{} got second highest with {} points.".format(dict.get(list[1]), list[1]))
