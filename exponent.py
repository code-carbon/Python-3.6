a=int(input("~ "))
l=[]
k=[]
for b in range(1,a+1):
  k.append(b)
  for c in range(1,a+1):
    l.append(c)
for t in l:
  for h in k:
    if(t**h==a):
      print("~)",t,"power",h)
      l.remove(t)
      k.remove(h)
      break