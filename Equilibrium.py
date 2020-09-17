equal=int(input("~ "))
point=[]
for part in str(equal):
  point.append(int(part))
for equal_part in point:
  if(sum(point[:point.index(equal_part)])==sum(point[point.index(equal_part):])):
    print(point[:point.index(equal_part)],point[point.index(equal_part):])
